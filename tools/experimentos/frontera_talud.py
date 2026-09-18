# -*- coding: utf-8 -*-
"""Compara la deteccion de particulas de frontera sobre la geometria del talud.

El script de referencia (talud_2021.py, fase geoestatica) usa
`boundary_particles2`, que recorre columnas de x unicas y toma la particula de
mayor y en cada una. La app usa `boundary_particles3`, un alpha shape
(Delaunay + filtro de longitud de arista).

Sobre el dominio rectangular de capacidad portante las dos dan el mismo
resultado. Sobre la superficie inclinada del talud no se habia verificado, y
`bound_val` decide que elementos se integran por Gauss y cuales por particulas
en `particles_to_nodes_gauss2`, asi que una diferencia aqui SI cambia el
resultado del geostatico.

No simula nada: ambas funciones son funciones puras de `xp`.

USO
    python tools/experimentos/frontera_talud.py            # 1.0 y 0.5
    python tools/experimentos/frontera_talud.py 0.5        # solo uno

RESULTADO (2026-09-12)

    ele_size 0.5  (la del script original)
        bp2 = 600, bp3 = 639, solo bp3 = 39, dif. simetrica 0.6 %
        bp3 es SUPERCONJUNTO de bp2. Las 39 extra estan en la cara inclinada:
        son las contrahuellas de la escalera de discretizacion, que bp2 no ve
        porque solo toma el maximo y de cada columna. Aqui la app detecta mas,
        y con mejor criterio geometrico.

    ele_size 1.0
        bp2 = 214, bp3 = 152, solo bp2 = 82, solo bp3 = 20, dif. simetrica 6.1 %
        Ya NO es superconjunto. Las 82 que bp3 pierde estan todas en y = 0.25,
        x de 19.25 a 59.75: es la capa basal completa (el pie, x > 18).

        CAUSA: con ele_size 1.0 el estrato inferior (y <= y1 = 0.5) conserva
        solo la fila y = 0.25, o sea queda de UNA particula de espesor. Una
        fila de puntos colineales no genera triangulos de Delaunay, asi que el
        alpha shape no puede construir el borde y los descarta. bp2 los captura
        porque toma la fila inferior entera (down = argmin de y).

        LIMITACION A RECORDAR: boundary_particles3 degenera en regiones de una
        particula de espesor. No es un problema en la malla de la tesis, donde
        el pie tiene dos filas, pero si lo seria en cualquier estrato delgado
        mal discretizado.

        COROLARIO: ele_size 1.0 no sirve como version barata de este caso. A
        ese tamano la capa basal de 0.5 m no se puede representar, asi que se
        estaria midiendo un artefacto de la discretizacion y no la pregunta de
        interes.
"""
import os
import sys

import numpy as np

V1 = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\1 Referencia\Codigo MPM-UN Original_V1"
APP = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\2 Software\MPM-UN\app"

sys.path.insert(0, APP)
sys.path.insert(0, V1)

from mpm_un import mesh as mesh_v1
from motorMPM import mesh as mesh_app


def nube_talud(ele_size=0.5):
    """Reproduce la nube de particulas de talud_2021.py::fase_geoestatica."""
    dimx, dimy = 60, 32
    cor, inci, nelex = mesh_v1.create_uniform(dimx, dimy, ele_size)[:3]
    xi, yi, xf, yf = 0.0, 0.0, 60.0, 30.5
    nmpe = 4
    mp_elem, xp, active_elem = mesh_v1.setup_MP(xi, yi, xf, yf, cor, inci, nmpe)

    # +++ recorte al dominio inclinado - talud +++  (lineas 48-75 del original)
    x1, x2, y1 = 8, 18, 0.5
    idpa = np.zeros(len(xp[:, 0])).astype(int)
    idcont = 0
    for j in range(len(xp[:, 0])):
        if xp[j, 0] <= x1:
            idpa[idcont] = j
            idcont += 1
        elif xp[j, 0] <= x2:
            ylim = ((yf * x2 - y1 * x1) / (x2 - x1)
                    - (yf - y1) / (x2 - x1) * xp[j, 0])
            if xp[j, 1] <= (ylim + 1e-10):
                idpa[idcont] = j
                idcont += 1
        else:
            if xp[j, 1] <= y1:
                idpa[idcont] = j
                idcont += 1
    idpa = idpa[:idcont]
    return xp[idpa, :]


def resumen(nombre, bval, xp):
    n = int(bval.sum())
    print("  %-22s %5d de %d particulas marcadas (%.1f %%)"
          % (nombre, n, len(xp), 100.0 * n / len(xp)))
    return n


def main():
    tamanos = [float(a) for a in sys.argv[1:]] or [1.0, 0.5]
    malos = 0
    for es in tamanos:
        malos += analizar(es)
    return 1 if malos else 0


def analizar(ele_size):
    xp = nube_talud(ele_size)
    print("=" * 74)
    print("FRONTERA DEL TALUD - boundary_particles2 (script) vs 3 (app)")
    print("ele_size = %.2f m" % ele_size)
    print("=" * 74)
    print("  particulas: %d" % len(xp))
    print("  x: [%.3f, %.3f]   y: [%.3f, %.3f]"
          % (xp[:, 0].min(), xp[:, 0].max(), xp[:, 1].min(), xp[:, 1].max()))
    print()

    _, bval2 = mesh_v1.boundary_particles2(xp)
    _, bval3 = mesh_app.boundary_particles3(xp)

    n2 = resumen("boundary_particles2", bval2, xp)
    n3 = resumen("boundary_particles3", bval3, xp)

    solo2 = np.where((bval2 == 1) & (bval3 == 0))[0]
    solo3 = np.where((bval3 == 1) & (bval2 == 0))[0]
    ambas = int(((bval2 == 1) & (bval3 == 1)).sum())

    print()
    print("  coinciden en          %5d particulas" % ambas)
    print("  solo boundary_2       %5d" % len(solo2))
    print("  solo boundary_3       %5d" % len(solo3))
    print("  diferencia simetrica  %5d  (%.1f %% del total)"
          % (len(solo2) + len(solo3),
             100.0 * (len(solo2) + len(solo3)) / len(xp)))

    if len(solo2) == 0 and len(solo3) == 0:
        print("\n  IDENTICAS -> el geostatico del talud no corre riesgo por aqui.")
        return 0

    # Donde estan las discrepancias: por tramo de la geometria
    print("\n  Ubicacion de las discrepancias (x1=8, x2=18 definen el talud):")
    for etiqueta, idx in (("solo boundary_2", solo2), ("solo boundary_3", solo3)):
        if not len(idx):
            continue
        x, y = xp[idx, 0], xp[idx, 1]
        print("    %s:" % etiqueta)
        print("        x: [%.3f, %.3f]   y: [%.3f, %.3f]"
              % (x.min(), x.max(), y.min(), y.max()))
        for nom, m in (("corona   x<=8 ", x <= 8),
                       ("talud  8<x<=18", (x > 8) & (x <= 18)),
                       ("pie      x>18 ", x > 18)):
            if m.sum():
                print("        %s : %4d" % (nom, int(m.sum())))
    return 1


if __name__ == "__main__":
    sys.exit(main())
