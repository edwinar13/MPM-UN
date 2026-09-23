# -*- coding: utf-8 -*-
"""¿Hace falta quitarle el peso propio a la base en la fase de falla del talud?

En `talud_2021.py :: fase_falla()` el cuerpo 1 (franja y <= 0.5 m, la base
friccional) tiene `bp_1 = 0`, mientras el talud tiene gravedad. Pero el estado
geostático del que arranca se calculó con gravedad en TODAS las partículas,
base incluida. Si la app no tiene que ofrecer "sin peso propio" por cuerpo, es
porque esa diferencia no cambia el resultado.

Este experimento corre la fase de falla dos veces con el motor original (V1),
desde el mismo `geostatic_state_v2.npz`, y solo cambia una línea:

    A (referencia):  bp_1[:,1] = 0
    B (con peso):    bp_1[:,1] = -9.81

El resto del ciclo es copia literal de `fase_falla()` (l. 616-693 de
talud_2021_v2.py), sin gráficas.

USO
    python tools/experimentos/peso_base.py [T] [cada] [A|B|AB|comparar]
        T     duración en s (default 1.0; la referencia usa 8.0)
        cada  intervalo entre frames guardados, en s (default 0.25)
    Para ahorrar tiempo se pueden correr A y B en dos procesos y luego
    `... T cada comparar`.

Guarda los frames en la carpeta indicada por la variable PESO_BASE_OUT
(default: carpeta actual) y compara.

RESULTADO (2026-09-22, T = 8 s, ~83 min por variante)

    Observación previa: en el geostático la base SÍ tiene peso; la referencia
    se lo quita solo en la falla, así que arranca con esfuerzos que incluyen un
    peso que ya no está. Su peso es ~13 kPa en la cara inferior, contra una
    sigma_yy media de -121 kPa en la base.

                                       A (sin peso)   B (con peso)   dif.
        runout del pie (m)                14.828         14.921      +0.6 %
        desplazamiento de la cresta (m)   12.042         12.102      +0.5 %
        desplazamiento medio talud (m)     6.588          6.635      +0.7 %
        eqplas máxima                      5.68           5.78       +1.7 %
        desplazamiento máx. de la base   7.6 mm         7.6 mm

    Partícula a partícula la diferencia llega a 0.67 m (media 0.07 m): el
    flujo amplifica la pequeña diferencia inicial, como en toda corrida de
    runout, pero las medidas globales cambian menos del 1 %.

    CONCLUSIÓN: quitarle el peso a la base no es necesario para el fenómeno.
    La base casi no se mueve en ninguno de los dos casos. La app no necesita
    un campo "sin peso propio"; para validar contra la referencia se usa la
    variante B (el script de referencia con esa única línea cambiada,
    documentada), igual que se hizo con talud_2021_2pasos.py.
"""
import sys
import os
import math
import time as tm
import numpy as np

V1 = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\1 Referencia\Codigo MPM-UN Original_V1"
sys.path.insert(0, V1)

from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP, node_conectivity
from mpm_un.explicit2 import (deltatime, particles_to_nodes, contact, nodes_to_particle_vel,
                              BC_Dirichlet_vel, nodes_to_particle_stress2, BC_Dirichlet_momentum3)

GEO = os.path.join(V1, "result_talud_2021", "geostatic_state_v2.npz")


def montar(peso_base):
    """Estado inicial de fase_falla(), tal cual el script."""
    Young, Coh, Phi, Psi = 3.8e3, 20, 20, 10
    sig = np.load(GEO)['sig']

    dimx, dimy, ele_size = 60, 32, 0.5
    cor, inci, nelex = create_uniform(dimx, dimy, ele_size)
    nnodesx = int(nelex + 1)
    nnodesy = int(len(cor) / nnodesx)
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)
    node_support = node_conectivity(inci, len(cor[:, 0]))

    # --- cuerpo 1 (base) ---
    xi, yi, xf, yf = 0, 0, 60, 0.5
    mp_elem_1, xp_1, _ = setup_MP(xi, yi, xf, yf, cor, inci, 4)
    nmp_1 = len(mp_elem_1)
    Vp_1 = (ele_size ** 2) / 4 * np.ones(nmp_1)
    Vp0_1 = (ele_size ** 2) / 4 * np.ones(nmp_1)
    rhop_1 = 2.6 * np.ones(nmp_1)
    Mp_1 = np.multiply(rhop_1, Vp_1)
    Prop_1 = np.zeros((nmp_1, 6))
    Prop_1[:, 0] = 10e3
    Prop_1[:, 1] = 0.3
    Prop_1[:, 2] = 200
    Prop_1[:, 3] = 35 / 180 * math.pi
    Prop_1[:, 4] = 35 / 180 * math.pi
    Fp_1 = np.ones((nmp_1, 4)); Fp_1[:, 1:3] = 0
    sig_1 = np.array(sig[:nmp_1, :])
    epse_1 = np.zeros((nmp_1, 3)); epsp_1 = np.zeros((nmp_1, 3))
    vp_1 = np.zeros((nmp_1, 2))
    bp_1 = np.zeros((nmp_1, 2))
    bp_1[:, 1] = -9.81 if peso_base else 0     # <-- LA UNICA DIFERENCIA
    tp_1 = np.zeros((nmp_1, 2))

    # --- cuerpo 2 (talud) ---
    xi, yi, xf, yf = 0.0, 0.5, 60, 30.5
    mp_elem_2, xp_2, _ = setup_MP(xi, yi, xf, yf, cor, inci, 4)
    x1, x2, y1 = 8, 18, 0.5
    idpa = np.zeros(len(xp_2[:, 0])).astype(int)
    idcont = 0
    for j in range(len(xp_2[:, 0])):
        if xp_2[j, 0] <= x1:
            idpa[idcont] = j; idcont += 1
        else:
            ylim = (yf * x2 - y1 * x1) / (x2 - x1) - (yf - y1) / (x2 - x1) * xp_2[j, 0]
            if xp_2[j, 1] <= (ylim + 1e-10):
                idpa[idcont] = j; idcont += 1
    idpa = idpa[:idcont]
    xp_2 = xp_2[idpa, :]
    mp_elem_2 = mp_elem_2[idpa, :]
    nmp_2 = len(mp_elem_2)
    Vp_2 = (ele_size ** 2) / 4 * np.ones(nmp_2)
    Vp0_2 = (ele_size ** 2) / 4 * np.ones(nmp_2)
    rhop_2 = 1.8 * np.ones(nmp_2)
    Mp_2 = np.multiply(rhop_2, Vp_2)
    Prop_2 = np.zeros((nmp_2, 6))
    Prop_2[:, 0] = Young
    Prop_2[:, 1] = 0.3
    Prop_2[:, 2] = Coh
    Prop_2[:, 3] = Phi / 180 * math.pi
    Prop_2[:, 4] = Psi / 180 * math.pi
    Fp_2 = np.ones((nmp_2, 4)); Fp_2[:, 1:3] = 0
    sig_2 = np.array(sig[nmp_1:, :])
    epse_2 = np.zeros((nmp_2, 3)); epsp_2 = np.zeros((nmp_2, 3))
    vp_2 = np.zeros((nmp_2, 2))
    bp_2 = np.zeros((nmp_2, 2)); bp_2[:, 1] = -9.81
    tp_2 = np.zeros((nmp_2, 2))

    assert nmp_1 + nmp_2 == len(sig), "el npz no corresponde a esta geometria"

    dtime_1 = deltatime(Prop_1[:, 0], Prop_1[:, 1], rhop_1, ele_size, 0.1)
    dtime_2 = deltatime(Prop_2[:, 0], Prop_2[:, 1], rhop_2, ele_size, 0.1)
    dtime = np.min([dtime_1, dtime_2])

    return locals()


def correr(peso_base, T, cada):
    S = montar(peso_base)
    g = S
    inci, cor, nelex, ele_size = g['inci'], g['cor'], g['nelex'], g['ele_size']
    fixed_nodesX, fixed_nodesY, node_support = g['fixed_nodesX'], g['fixed_nodesY'], g['node_support']
    dtime = g['dtime']
    xp_1, vp_1, Vp_1, Vp0_1, Mp_1, sig_1, bp_1, tp_1 = (g[k] for k in
        ('xp_1', 'vp_1', 'Vp_1', 'Vp0_1', 'Mp_1', 'sig_1', 'bp_1', 'tp_1'))
    Fp_1, epse_1, epsp_1, Prop_1, mp_elem_1 = (g[k] for k in ('Fp_1', 'epse_1', 'epsp_1', 'Prop_1', 'mp_elem_1'))
    xp_2, vp_2, Vp_2, Vp0_2, Mp_2, sig_2, bp_2, tp_2 = (g[k] for k in
        ('xp_2', 'vp_2', 'Vp_2', 'Vp0_2', 'Mp_2', 'sig_2', 'bp_2', 'tp_2'))
    Fp_2, epse_2, epsp_2, Prop_2, mp_elem_2 = (g[k] for k in ('Fp_2', 'epse_2', 'epsp_2', 'Prop_2', 'mp_elem_2'))
    nmp_1 = g['nmp_1']
    Mu, alpha = 0.268, 0.10

    nsteps = int(math.ceil(T / dtime))
    ncada = max(1, int(round(cada / dtime)))
    frames = []

    def snap(t):
        frames.append(dict(
            t=t * dtime,
            xp=np.concatenate((xp_1, xp_2)).copy(),
            sig=np.concatenate((sig_1, sig_2)).copy(),
            epsp=np.concatenate((epsp_1, epsp_2)).copy(),
            vp=np.concatenate((vp_1, vp_2)).copy(),
        ))

    snap(0)
    t0 = tm.time()
    for t in range(nsteps):
        mp_elem_1, active_elem_1 = search_MP(mp_elem_1, xp_1, ele_size, nelex)
        mp_elem_2, active_elem_2 = search_MP(mp_elem_2, xp_2, ele_size, nelex)
        active_elem = np.unique(np.concatenate((active_elem_1, active_elem_2), axis=0))
        active_nodes_1 = np.unique(inci[active_elem_1 - 1, :])
        active_nodes_2 = np.unique(inci[active_elem_2 - 1, :])
        active_nodes = np.unique(inci[active_elem - 1, :])

        grid_1 = inci, cor, active_elem, active_nodes, mp_elem_1
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, bp_1, tp_1
        nmass_1, nmomentum_1, niforce_1, neforce_1, shfnp_1 = particles_to_nodes(grid_1, particle_1)
        grid_2 = inci, cor, active_elem, active_nodes, mp_elem_2
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, bp_2, tp_2
        nmass_2, nmomentum_2, niforce_2, neforce_2, shfnp_2 = particles_to_nodes(grid_2, particle_2)

        nmomentum_1t = np.copy(nmomentum_1)
        nmomentum_2t = np.copy(nmomentum_2)
        dampfac = alpha
        ndamping_1 = -dampfac * np.multiply(np.absolute(niforce_1 + neforce_1), np.sign(nmomentum_1))
        nforce_1 = niforce_1 + neforce_1 + ndamping_1
        nmomentum_1 += nforce_1 * dtime
        ndamping_2 = -dampfac * np.multiply(np.absolute(niforce_2 + neforce_2), np.sign(nmomentum_2))
        nforce_2 = niforce_2 + neforce_2 + ndamping_2
        nmomentum_2 += nforce_2 * dtime

        nmassS = nmass_1 + nmass_2
        nmomentumS = nmomentum_1 + nmomentum_2
        mesh = inci, cor, node_support, active_nodes
        body1 = nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1
        body2 = nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2
        nmomentum_1, nmomentum_2 = contact(body1, body2, nmassS, nmomentumS, mesh, dtime, Mu)
        nforce_1 = 1 / dtime * (nmomentum_1 - nmomentum_1t)
        nforce_2 = 1 / dtime * (nmomentum_2 - nmomentum_2t)

        nmomentum_1, nforce_1 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_1, nforce_1)
        nmomentum_2, nforce_2 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_2, nforce_2)

        nquantities_1 = nmass_1, nmomentum_1, nforce_1
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, shfnp_1
        xp_1, vp_1, nvel_1 = nodes_to_particle_vel(grid_1, particle_1, nquantities_1, dtime)
        nvel_1 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_1)
        nquantities_2 = nmass_2, nmomentum_2, nforce_2
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, shfnp_2
        xp_2, vp_2, nvel_2 = nodes_to_particle_vel(grid_2, particle_2, nquantities_2, dtime)
        nvel_2 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_2)

        particle_1 = Fp_1, Vp_1, Vp0_1, epse_1, epsp_1, sig_1, shfnp_1, Prop_1
        Fp_1, Vp_1, epse_1, epsp_1, sig_1 = nodes_to_particle_stress2(grid_1, particle_1, nvel_1, dtime, 0)
        particle_2 = Fp_2, Vp_2, Vp0_2, epse_2, epsp_2, sig_2, shfnp_2, Prop_2
        Fp_2, Vp_2, epse_2, epsp_2, sig_2 = nodes_to_particle_stress2(grid_2, particle_2, nvel_2, dtime, 1)

        if (t + 1) % ncada == 0 or t == nsteps - 1:
            snap(t + 1)
            print(f"  {'B' if peso_base else 'A'}  t = {(t + 1) * dtime:6.3f} s  "
                  f"({t + 1}/{nsteps}, {tm.time() - t0:.0f} s)", flush=True)

    out = {k: np.array([f[k] for f in frames]) for k in frames[0]}
    out['nmp_1'] = nmp_1
    out['dtime'] = dtime
    return out


def eqplas(epsp):
    return np.sqrt(4 / 9 * (epsp[..., 0] ** 2 - epsp[..., 0] * epsp[..., 1] + epsp[..., 1] ** 2)
                   + 4 / 3 * epsp[..., 2] ** 2)


def comparar(A, B):
    n1 = int(A['nmp_1'])
    print()
    print(f"{'t (s)':>6} | {'base dy A':>10} {'base dy B':>10} | {'talud |d| max A':>15} {'B':>8} "
          f"{'max|dA-dB|':>10} | {'eqp max A':>9} {'B':>9} | {'frente x A':>10} {'B':>8}")
    for k in range(len(A['t'])):
        dA = A['xp'][k] - A['xp'][0]
        dB = B['xp'][k] - B['xp'][0]
        nA = np.linalg.norm(dA[n1:], axis=1)
        nB = np.linalg.norm(dB[n1:], axis=1)
        dif = np.linalg.norm(dA[n1:] - dB[n1:], axis=1)
        eA = eqplas(A['epsp'][k][n1:]); eB = eqplas(B['epsp'][k][n1:])
        print(f"{A['t'][k]:6.2f} | {dA[:n1, 1].mean():10.2e} {dB[:n1, 1].mean():10.2e} | "
              f"{nA.max():15.4f} {nB.max():8.4f} {dif.max():10.2e} | "
              f"{eA.max():9.4f} {eB.max():9.4f} | "
              f"{A['xp'][k][n1:, 0].max():10.3f} {B['xp'][k][n1:, 0].max():8.3f}")

    # esfuerzos de la base al inicio: cuanto de su sigma_yy es peso propio
    s0 = A['sig'][0][:n1, 1]
    print()
    print(f"sigma_yy de la base al inicio: media {s0.mean():.1f} kPa, min {s0.min():.1f} kPa")
    print(f"peso propio de la base (0.5 m x 2.6 x 9.81): {0.5 * 2.6 * 9.81:.2f} kPa en la cara inferior")


if __name__ == "__main__":
    T = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
    cada = float(sys.argv[2]) if len(sys.argv) > 2 else 0.25
    que = sys.argv[3] if len(sys.argv) > 3 else "AB"   # A, B, AB o comparar
    out_dir = os.environ.get("PESO_BASE_OUT", ".")
    ruta = {v: os.path.join(out_dir, f"peso_base_{v}.npz") for v in "AB"}
    if que != "comparar":
        print(f"Fase de falla, T = {T} s, frame cada {cada} s, variantes {que}")
        for v in que:
            np.savez_compressed(ruta[v], **correr(v == "B", T, cada))
    if que in ("AB", "comparar"):
        comparar(*(dict(np.load(ruta[v])) for v in "AB"))
