# -*- coding: utf-8 -*-
"""Corre el mismo paso MPM con el motor original (V1) y con el de la app,
desde un estado inicial identico, y compara salida por salida.

Configuracion: capacidad portante malla 1.0 (Ca_portante2_malla1.py).
"""
import sys
import math
import numpy as np

V1 = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\1 Referencia\Codigo MPM-UN Original_V1"
APP = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\2 Software\MPM-UN\app"

sys.path.insert(0, APP)
sys.path.insert(0, V1)

from mpm_un import mesh as mesh_v1
from mpm_un import explicit2 as ex_v1
from motorMPM import mesh as mesh_app
from motorMPM import explicit2 as ex_app


def montar(mesh_mod):
    dimx, dimy, ele_size = 20, 15, 1.0
    cor, inci, nelex = mesh_mod.create_uniform(dimx, dimy, ele_size)[:3]
    nnodesx = int(nelex + 1)
    nnodesy = int(len(cor) / nnodesx)
    fx, fy = mesh_mod.contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)
    mp_elem, xp, active_elem = mesh_mod.setup_MP(0, 0, 20, 10, cor, inci, 4)
    nmp = len(mp_elem)
    Vp = (ele_size ** 2) / 4 * np.ones(nmp)
    Vp0 = Vp.copy()
    rhop = 1.8 * np.ones(nmp)
    Mp = rhop * Vp
    Prop = np.zeros((nmp, 6))
    Prop[:, 0] = 10e3
    Prop[:, 1] = 0.49
    Prop[:, 2] = 20
    Prop[:, 3] = 0.0
    Prop[:, 4] = 0.0
    tp0 = mesh_mod.traction_forces(xp, 3, 1, 0, 5)
    bound_ptcl, bound_val = mesh_mod.boundary_particles(xp)
    return dict(cor=cor, inci=inci, nelex=nelex, fx=fx, fy=fy, mp_elem=mp_elem,
                xp=xp, active_elem=active_elem, nmp=nmp, Vp=Vp, Vp0=Vp0,
                rhop=rhop, Mp=Mp, Prop=Prop, tp0=tp0, bound_val=bound_val,
                ele_size=ele_size)


def un_paso(ex, mesh_mod, S, estado, dtime, dincre, i):
    """Una iteracion del while, tal cual el script."""
    xp, vp, Vp, Fp, epse, epsp, sig = estado
    mp_elem = S['mp_elem_run']
    inci, cor, nelex = S['inci'], S['cor'], S['nelex']

    mp_elem, active_elem = mesh_mod.search_MP(mp_elem, xp, S['ele_size'], nelex)
    S['mp_elem_run'] = mp_elem
    active_nodes = np.unique(inci[active_elem - 1, :])

    bp = np.zeros((S['nmp'], 2))
    tp = (i + 1) * dincre * S['tp0']

    grid = inci, cor, active_elem, active_nodes, mp_elem
    particle = xp, vp, Vp, S['Mp'], sig, bp, tp
    nmass, nmomentum, niforce, neforce, shfnp = ex.particles_to_nodes_gauss2(
        grid, particle, S['bound_val'])

    dampfac = 0.75
    ndamping = -dampfac * np.multiply(np.absolute(niforce + neforce),
                                      np.sign(nmomentum))
    nforce = niforce + neforce + ndamping
    nmomentum = nmomentum + nforce * dtime

    nmomentum, nforce, niforce, neforce = ex.BC_Dirichlet_momentum(
        active_nodes, S['fx'], S['fy'], nmomentum, nforce, niforce, neforce)

    nquantities = nmass, nmomentum, nforce
    particle = xp, vp, Vp, S['Mp'], sig, shfnp
    xp, vp, nvel = ex.nodes_to_particle_vel(grid, particle, nquantities, dtime)
    nvel = ex.BC_Dirichlet_vel(active_nodes, S['fx'], S['fy'], nvel)

    particle = Fp, Vp, S['Vp0'], epse, epsp, sig, shfnp, S['Prop']
    Fp, Vp, epse, epsp, sig = ex.nodes_to_particle_stress_gauss(
        grid, particle, S['bound_val'], nvel, dtime, 1)

    ff, ee, nework = ex.static_convergence(nmass, niforce, neforce, nvel,
                                           dtime, 0.0)
    return (xp, vp, Vp, Fp, epse, epsp, sig), (ff, ee), (nmass, niforce, neforce, nvel)


def dt_de(ex, Prop, rhop, ele_size):
    r = ex.deltatime(Prop[:, 0], Prop[:, 1], rhop, ele_size, 0.1)
    return r[0] if isinstance(r, tuple) else r


S1, S2 = montar(mesh_v1), montar(mesh_app)

print("=== SETUP ===")
print("  nmp:            V1=%d  app=%d" % (S1['nmp'], S2['nmp']))
print("  xp identicos:   %s (max dif %.3e)"
      % (np.array_equal(S1['xp'], S2['xp']), np.abs(S1['xp'] - S2['xp']).max()))
print("  tp0 identicos:  %s (max dif %.3e)"
      % (np.array_equal(S1['tp0'], S2['tp0']), np.abs(S1['tp0'] - S2['tp0']).max()))
print("  bound_val igual:%s" % np.array_equal(np.asarray(S1['bound_val']).ravel(),
                                              np.asarray(S2['bound_val']).ravel()))
print("  cor identicos:  %s" % np.array_equal(S1['cor'], S2['cor']))
print("  inci identicos: %s" % np.array_equal(S1['inci'], S2['inci']))
print("  fixedX igual:   %s   fixedY igual: %s"
      % (np.array_equal(S1['fx'], S2['fx']), np.array_equal(S1['fy'], S2['fy'])))

dt1 = dt_de(ex_v1, S1['Prop'], S1['rhop'], 1.0)
dt2 = dt_de(ex_app, S2['Prop'], S2['rhop'], 1.0)
print("  dtime:          V1=%.20g" % dt1)
print("                  app=%.20g" % dt2)
print("  dtime iguales:  %s" % (dt1 == dt2))

nmp = S1['nmp']


def estado0():
    return (S1['xp'].copy(), np.zeros((nmp, 2)), S1['Vp'].copy(),
            np.hstack([np.ones((nmp, 1)), np.zeros((nmp, 2)), np.ones((nmp, 1))]),
            np.zeros((nmp, 3)), np.zeros((nmp, 3)), np.zeros((nmp, 4)))


e1, e2 = estado0(), estado0()
S1['mp_elem_run'] = S1['mp_elem'].copy()
S2['mp_elem_run'] = S2['mp_elem'].copy()

print("\n=== ITERACIONES DEL INCREMENTO 1 (dincre=-2) ===")
print("%5s %14s %14s %12s %12s" % ("iter", "ff V1", "ff app", "dif sig", "dif xp"))
for k in range(6):
    e1, (ff1, ee1), n1 = un_paso(ex_v1, mesh_v1, S1, e1, dt1, -2, 0)
    e2, (ff2, ee2), n2 = un_paso(ex_app, mesh_app, S2, e2, dt2, -2, 0)
    dsig = np.abs(e1[6] - e2[6]).max()
    dxp = np.abs(e1[0] - e2[0]).max()
    print("%5d %14.10g %14.10g %12.3e %12.3e" % (k + 1, ff1, ff2, dsig, dxp))
    if k == 0:
        for nom, a, b in (("nmass", n1[0], n2[0]), ("niforce", n1[1], n2[1]),
                          ("neforce", n1[2], n2[2]), ("nvel", n1[3], n2[3])):
            print("        %-8s dif max = %.3e" % (nom, np.abs(a - b).max()))
