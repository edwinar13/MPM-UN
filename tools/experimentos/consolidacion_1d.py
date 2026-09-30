# -*- coding: utf-8 -*-
"""Consolidación unidimensional con el MPM de doble fase (formulación v-w),
comparada con la solución analítica de Terzaghi.

Reproduce el caso 7.1 de Caro González (2024) (pequeñas deformaciones). El
programa principal de la referencia no se conserva; el ciclo se reconstruye del
Algoritmo 2 (cap. 6.3) y del Algoritmo 4 (ecuación nodal), usando las funciones
de doble fase de app/motorMPM/dos_fases.py sin cambios.

Datos (Tabla 7-1), en las unidades de la app (kPa, m, Mg, s):
    columna 0.1 × 1.0 m, elementos de 0.1 m, 49 partículas por elemento
    E' = 10 MPa, ν' = 0, n0 = 0.3, Kw = 100 MPa, k = 1e-3 m/s
    ρs = 2.7 Mg/m³, ρw = 1.0 Mg/m³, q0 = 10 kPa, sin gravedad
    Δt = 0.0002 s, 4 s  →  cv ≈ 1.02 m²/s, Tv ≈ 4

Condiciones de frontera:
    laterales: v_x = w_x = 0 (rodillo, impermeable)
    fondo:     v_y = w_y = 0 (fijo en y, impermeable)
    superficie libre: el agua sale; p = 0 queda impuesta débilmente (condición
    natural de la ecuación del agua con presión prescrita nula)
Condición inicial: p = q0 en toda la columna, σ' = 0, en equilibrio con la carga.

Signos (mecánica del medio continuo, como la referencia): compresión negativa.
La presión de poros de las funciones de la referencia entra al esfuerzo total
como σ = σ' + pp, así que pp = −p (pp = −q0 al inicio).

USO
    python tools/experimentos/consolidacion_1d.py <salida> [--t 4.0] [--alpha 0.0] [--nmpe 49]
"""
import argparse
import math
import os
import sys
import time

import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(RAIZ, "app"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from motorMPM.mesh import create_uniform_quadrilateral, setup_MP, search_MP, traction_forces  # noqa: E402
from motorMPM.dos_fases import (deltatime_two_phases_CFL, particles_to_nodes_two_phases,  # noqa: E402
                                nodes_to_particle_vel_two_phases, nodes_to_particle_xp_two_phases,
                                BC_Dirichlet_acele_force_two_phases, BC_Dirichlet_vel_two_phases,
                                nodes_to_particle_stress_MP_and_pore_pressure_SRI_k_act_NUMBA)
import terzaghi  # noqa: E402

# --- Tabla 7-1 ---
LX, H, ELE = 0.1, 1.0, 0.1
E, NU = 1.0e4, 0.0
N0, KW, K = 0.3, 1.0e5, 1.0e-3
RHO_S, RHO_W = 2.7, 1.0
Q0 = 10.0
DT_REF = 2.0e-4          # Δt de la referencia (Courant 0.98)
FRAME = 0.01             # s entre frames guardados
TVS = (0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0)   # isócronas a comparar


def armar(nmpe):
    cor, inci, nelex = create_uniform_quadrilateral(LX, H, ELE)
    nnx = nelex + 1
    nny = len(cor) // nnx
    ids = np.arange(1, len(cor) + 1)
    col = (ids - 1) % nnx
    fila = (ids - 1) // nnx
    fixed_x = ids[(col == 0) | (col == nnx - 1)]       # laterales
    fixed_y = ids[fila == 0]                            # fondo
    mp_elem, xp, _ = setup_MP(0.0, 0.0, LX, H, cor, inci, nmpe)
    return cor, inci, nelex, fixed_x, fixed_y, mp_elem, xp


def correr(t_total, alpha, nmpe, dt=None, verbose=True):
    cor, inci, nelex, fixed_x, fixed_y, mp_elem, xp = armar(nmpe)
    nmp = len(xp)

    # --- estado de las partículas ---
    Vp0 = np.full(nmp, ELE * ELE / nmpe)
    Vp = Vp0.copy()
    n_p = np.full(nmp, N0)
    n_0p = n_p.copy()
    k_p = np.full(nmp, K)
    Mp_s0 = (1 - N0) * RHO_S * Vp0                 # masa de sólidos, constante (4-90)
    vp = np.zeros((nmp, 2))
    wp = np.zeros((nmp, 2))
    sig_e = np.zeros((nmp, 4))                     # esfuerzo efectivo xx, yy, xy, zz
    pp = np.full((nmp, 3), -Q0)                    # presión de poros (compresión < 0)
    sig_t = sig_e.copy()
    sig_t[:, :2] += pp[:, :2]
    Fp = np.zeros((nmp, 4))
    Fp[:, 0] = Fp[:, 3] = 1.0
    epse = np.zeros((nmp, 3))
    epsp = np.zeros((nmp, 3))
    Prop = np.zeros((nmp, 6))
    Prop[:, 0], Prop[:, 1] = E, NU
    bp = np.zeros((nmp, 2))                        # sin gravedad
    tp = traction_forces(xp, 3, -Q0, 0.0, LX)      # q0 en las partículas de la superficie
    pb_p = np.zeros((nmp, 2))                      # presión prescrita en la frontera: 0
    bound_val = np.zeros(nmp, dtype=np.int64)      # no lo usa la función SRI

    rho_sat = (1 - N0) * RHO_S + N0 * RHO_W
    dt_cfl = deltatime_two_phases_CFL(np.array([E]), NU, np.array([rho_sat]), ELE, 0.98, KW, N0)
    dt = dt or dt_cfl
    nsteps = int(round(t_total / dt))
    cada = max(1, int(round(FRAME / dt)))
    if verbose:
        print(f"{nmp} partículas, Δt = {dt:g} s (CFL no drenado con Courant 0.98: {dt_cfl:g}), "
              f"{nsteps} pasos, α = {alpha}")

    y0 = xp[:, 1].copy()
    tiempos, PP, SY, YY = [0.0], [pp[:, 0].copy()], [sig_e[:, 1].copy()], [xp[:, 1].copy()]
    t0 = time.time()
    for it in range(nsteps):
        # 2: incidencias
        mp_elem, active_elem = search_MP(mp_elem, xp, ELE, nelex)
        active_nodes = np.unique(inci[active_elem - 1, :])
        grid = (inci, cor, active_elem, active_nodes, mp_elem)

        # 3-13: transferencia a los nodos; masa del agua según la porosidad actual (4-89)
        Mp_w = n_p * RHO_W * Vp
        Mp_weq = RHO_W * Vp
        Mp = Mp_w + Mp_s0
        particle = (xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, Mp_weq, sig_t, sig_e, pp,
                    bp, tp, pb_p, n_p, k_p, RHO_W)
        (nmass_s, nmass_w, nmass_weq, nmass, nmom_s, nmom_w, niforce_w, neforce_w,
         ndforce_w, neforce_m, niforce_m, shfnp) = particles_to_nodes_two_phases(grid, particle)

        # 14-19: ecuación nodal con amortiguamiento local (5-28, 5-29; Algoritmo 2)
        fw = niforce_w + neforce_w
        fm = niforce_m + neforce_m
        if alpha > 0:
            w_n = np.divide(nmom_w, nmass_w, out=np.zeros_like(nmom_w), where=nmass_w != 0)
            v_n = np.divide(nmom_s, nmass_s, out=np.zeros_like(nmom_s), where=nmass_s != 0)
            damp_w = -alpha * np.abs(fw) * np.sign(w_n)
            damp_s = -alpha * np.abs(fm - fw) * np.sign(v_n)
        else:
            damp_w = damp_s = 0.0
        nforce_w = fw + ndforce_w + damp_w
        nforce_m = fm + damp_s + damp_w

        # 20-23: aceleraciones (Algoritmo 4) y nodos de Dirichlet
        nacele_w = nforce_w / nmass_weq
        nacele_s = (nforce_m - nmass_w * nacele_w) / nmass_s
        nq = (nacele_w, nacele_s, nforce_w, niforce_w, neforce_w, ndforce_w,
              nforce_m, neforce_m, niforce_m)
        nacele_s, nacele_w = BC_Dirichlet_acele_force_two_phases(active_nodes, fixed_x, fixed_y, nq)[:2]

        # 26-30: velocidades de las partículas y velocidades nodales (MUSL)
        vp, wp, nvel_s, nvel_w = nodes_to_particle_vel_two_phases(
            grid, (xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, shfnp),
            (nacele_w, nacele_s, nmass, nmass_w, nmass_s, nmass_weq), dt)
        nvel_s, nvel_w = BC_Dirichlet_vel_two_phases(active_nodes, fixed_x, fixed_y, nvel_s, nvel_w)

        # 31-32: posiciones
        xp = nodes_to_particle_xp_two_phases(xp, nvel_s, grid, shfnp, dt)

        # 33-48: esfuerzo efectivo en partículas, presión de poros con SRI, porosidad
        Fp, Vp, epse, epsp, sig_e, pp, n_p, k_p = \
            nodes_to_particle_stress_MP_and_pore_pressure_SRI_k_act_NUMBA(
                grid, (Fp, Vp, Vp0, n_p, n_0p, k_p, K, N0, epse, epsp, sig_e, sig_t, pp, shfnp, Prop),
                bound_val, nvel_s, nvel_w, dt, 0, KW)
        sig_t = sig_e.copy()                       # 46: esfuerzo total
        sig_t[:, :2] += pp[:, :2]

        if (it + 1) % cada == 0:
            tiempos.append((it + 1) * dt)
            PP.append(pp[:, 0].copy())
            SY.append(sig_e[:, 1].copy())
            YY.append(xp[:, 1].copy())
        if verbose and (it + 1) % max(1, nsteps // 10) == 0:
            print(f"  {100 * (it + 1) / nsteps:5.1f} %  t = {(it + 1) * dt:.3f} s  "
                  f"p medio / q0 = {-pp[:, 0].mean() / Q0:.4f}  ({time.time() - t0:.0f} s)")

    if verbose:
        print(f"tiempo de cómputo: {time.time() - t0:.1f} s")
    return dict(t=np.array(tiempos), pp=np.array(PP).T, sig_e_yy=np.array(SY).T,
                y=np.array(YY).T, y0=y0, dt=dt)


def comparar(r, alpha, ruta_png=None):
    c = terzaghi.cv(K, E, NU)
    Tv = c * r["t"] / H ** 2
    p_rel = -r["pp"] / Q0                          # p / p0
    y0 = r["y0"]
    # grado de consolidación a partir de la presión media (partículas de igual volumen)
    U_num = 1 - p_rel.mean(axis=0)
    U_ana = np.array([terzaghi.grado_consolidacion(tv) for tv in Tv])
    # partícula más cercana a media altura
    im = int(np.argmin(np.abs(y0 - H / 2) + 1e-9 * np.abs(r["y0"] - LX / 2)))
    err_mid = np.abs(p_rel[im] - np.array([terzaghi.presion(1 - y0[im] / H, tv) for tv in Tv]))

    print(f"\ncv = {c:.3f} m²/s   α = {alpha}")
    print(f"{'Tv':>5s} | {'U MPM':>6s} {'U Terz.':>7s} | {'error máx p/p0 en la columna':>28s}")
    for tv in TVS:
        k = int(np.argmin(np.abs(Tv - tv)))
        p_ana = terzaghi.presion(1 - y0 / H, Tv[k])
        print(f"{Tv[k]:5.2f} | {U_num[k]:6.3f} {U_ana[k]:7.3f} | {np.max(np.abs(p_rel[:, k] - p_ana)):28.3f}")
    for lim in (0.5, 1.5):
        sel = Tv >= lim
        if sel.any():
            print(f"error absoluto en la partícula media (y = {y0[im]:.3f}) para Tv ≥ {lim}: "
                  f"máx {err_mid[sel].max():.4f}")

    if ruta_png:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(14, 5))
        ys = np.linspace(0, 1, 201)
        orden = np.argsort(y0)
        for j, tv in enumerate(TVS):
            k = int(np.argmin(np.abs(Tv - tv)))
            color = f"C{j}"
            a1.plot(terzaghi.presion(1 - ys, Tv[k]), ys, color=color, lw=1)
            a1.plot(p_rel[orden, k], y0[orden] / H, ".", color=color, ms=2, label=f"Tv = {Tv[k]:.2f}")
        a1.set(xlabel="p / p0", ylabel="y / H", xlim=(0, 1.05), ylim=(0, 1),
               title=f"Isócronas (líneas: Terzaghi, puntos: MPM), α = {alpha}")
        a1.legend(fontsize=7, loc="lower left")
        a2.plot(Tv, U_ana, "k-", lw=1, label="Terzaghi")
        a2.plot(Tv, U_num, "r--", lw=1, label="MPM")
        a2.set(xlabel="Tv", ylabel="U", title="Grado de consolidación promedio", ylim=(0, 1.02))
        a2.legend()
        a3.plot(Tv, err_mid, lw=1)
        a3.set(xlabel="Tv", ylabel="|p num − p ana| / p0",
               title=f"Error en la partícula media (y = {y0[im]:.2f} m)")
        for a in (a1, a2, a3):
            a.grid(alpha=0.3)
        fig.tight_layout()
        fig.savefig(ruta_png, dpi=150)
        print(f"figura: {ruta_png}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--t", type=float, default=4.0, help="duración (s)")
    ap.add_argument("--alpha", type=float, default=0.0, help="amortiguamiento local")
    ap.add_argument("--nmpe", type=int, default=49, help="partículas por elemento (cuadrado perfecto)")
    ap.add_argument("--dt", type=float, default=None, help="Δt (por defecto el CFL con Courant 0.98)")
    args = ap.parse_args()
    os.makedirs(args.salida, exist_ok=True)
    r = correr(args.t, args.alpha, args.nmpe, args.dt)
    base = os.path.join(args.salida, f"consol1d_a{args.alpha:g}_n{args.nmpe}_t{args.t:g}")
    np.savez_compressed(base + ".npz", **r)
    comparar(r, args.alpha, base + ".png")


if __name__ == "__main__":
    main()
