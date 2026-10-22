# -*- coding: utf-8 -*-
"""Mismo motor, mismos datos, SOLO cambia el orden de las particulas.

Si el orden explica las diferencias app-vs-script en capacidad portante, dos
corridas identicas salvo por una permutacion deben separarse en la misma
magnitud que observamos (SIGYY ~0.4% al tercer incremento).
"""
import sys, json
import numpy as np

APP = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\2 Software\MPM-UN\app"
PROY = (r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\2 Software\MPM-UN"
        r"\test\6 archivos_mpm 2609\2_capacidad_portante_malla1.json")
sys.path.insert(0, APP)

from motorMPM.mesh import (create_uniform, contour_fixe, setup_MP, search_MP,
                           traction_forces, boundary_particles)
from motorMPM.explicit2 import (deltatime, particles_to_nodes_gauss2,
                                BC_Dirichlet_momentum, nodes_to_particle_vel,
                                BC_Dirichlet_vel, nodes_to_particle_stress_gauss,
                                static_convergence)

dimx, dimy, ele_size = 20, 15, 1.0
cor, inci, nelex = create_uniform(dimx, dimy, ele_size)[:3]
nnodesx = int(nelex + 1); nnodesy = int(len(cor) / nnodesx)
fx, fy = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)
mp_elem0, xp0, _ = setup_MP(0, 0, 20, 10, cor, inci, 4)
nmp = len(xp0)

# orden en que la app guarda las particulas
g = list(json.load(open(PROY, encoding="utf-8"))["PUNTOSMATERIAL"].values())[0]
vals = list(g["POINTS"].values()) if isinstance(g["POINTS"], dict) else g["POINTS"]
xp_app = np.array([v["COORDINATES"][:2] for v in vals], float)

# permutacion script -> app
clave_s = {tuple(np.round(p, 6)): i for i, p in enumerate(xp0)}
perm = np.array([clave_s[tuple(np.round(p, 6))] for p in xp_app])
assert np.allclose(xp0[perm], xp_app)
print("permutacion valida. ¿es la identidad? %s" % np.array_equal(perm, np.arange(nmp)))

r = deltatime(np.full(nmp, 10e3), np.full(nmp, 0.49), np.full(nmp, 1.8), ele_size, 0.1)
dtime = r[0] if isinstance(r, tuple) else r


def corrida(orden):
    """orden = array de indices; define en que secuencia van las particulas."""
    xp = xp0[orden].copy()
    mp_elem = mp_elem0[orden].copy()
    Vp = np.full(nmp, ele_size ** 2 / 4)
    Vp0 = Vp.copy()
    rhop = np.full(nmp, 1.8)
    Mp = rhop * Vp
    Prop = np.zeros((nmp, 6))
    Prop[:, 0] = 10e3; Prop[:, 1] = 0.49; Prop[:, 2] = 20
    Fp = np.hstack([np.ones((nmp, 1)), np.zeros((nmp, 2)), np.ones((nmp, 1))])
    epse = np.zeros((nmp, 3)); epsp = np.zeros((nmp, 3))
    sig = np.zeros((nmp, 4)); vp = np.zeros((nmp, 2))
    bp = np.zeros((nmp, 2))
    tp0 = traction_forces(xp, 3, 1, 0, 5)
    _, bound_val = boundary_particles(xp)

    salida = []
    for i in range(3):
        tp = (i + 1) * (-2) * tp0
        ff = ee = 1.0
        nework = 0.0
        tcont = 0
        while (ff > 0.011) or (ee > 0.01):
            tcont += 1
            mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)
            active_nodes = np.unique(inci[active_elem - 1, :])
            grid = inci, cor, active_elem, active_nodes, mp_elem
            particle = xp, vp, Vp, Mp, sig, bp, tp
            nmass, nmom, nif, nef, shfnp = particles_to_nodes_gauss2(
                grid, particle, bound_val)
            ndamp = -0.75 * np.multiply(np.absolute(nif + nef), np.sign(nmom))
            nforce = nif + nef + ndamp
            nmom = nmom + nforce * dtime
            nmom, nforce, nif, nef = BC_Dirichlet_momentum(
                active_nodes, fx, fy, nmom, nforce, nif, nef)
            particle = xp, vp, Vp, Mp, sig, shfnp
            xp, vp, nvel = nodes_to_particle_vel(
                grid, particle, (nmass, nmom, nforce), dtime)
            nvel = BC_Dirichlet_vel(active_nodes, fx, fy, nvel)
            particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
            Fp, Vp, epse, epsp, sig = nodes_to_particle_stress_gauss(
                grid, particle, bound_val, nvel, dtime, 1)
            nework0 = nework
            ff, ee, nework = static_convergence(nmass, nif, nef, nvel, dtime, nework0)
        print("   incremento %d: %6d ciclos, ff=%.16g" % (i + 1, tcont, ff))
        salida.append((xp.copy(), sig.copy()))
    return salida


print("\n--- orden del script (setup_MP) ---")
A = corrida(np.arange(nmp))
print("\n--- orden de la app (el del proyecto) ---")
B = corrida(perm)

print("\n=== DIFERENCIA POR SOLO CAMBIAR EL ORDEN ===")
print("%10s %14s %14s" % ("incremento", "rel SIGYY", "rel CORY"))
for k in range(3):
    xa, sa = A[k]
    xb, sb = B[k]
    xb = xb[np.argsort(perm)][np.arange(nmp)]  # devolver B al orden del script
    sb = sb[np.argsort(perm)][np.arange(nmp)]
    # argsort(perm) mapea app->script
    rs = np.abs(sa[:, 1] - sb[:, 1]).max() / max(np.abs(sa[:, 1]).max(), 1e-30)
    rc = np.abs(xa[:, 1] - xb[:, 1]).max() / max(np.abs(xa[:, 1]).max(), 1e-30)
    print("%10d %14.3e %14.3e" % (k + 1, rs, rc))
