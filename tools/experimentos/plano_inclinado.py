# -*- coding: utf-8 -*-
"""Bloque sobre un plano inclinado con fricción de Coulomb: valida las normales
de contacto calculadas (contact2, modo 'gradiente') contra la solución analítica.

La referencia (talud_2021_v2.py) solo tiene contactos horizontales y nunca
calculó normales, así que no hay con qué comparar bit a bit. Este caso sí tiene
respuesta exacta para un bloque rígido que arranca en reposo:

    tan θ > μ  →  desliza con  a = g·(sen θ − μ·cos θ)
    tan θ ≤ μ  →  se queda quieto

Se arma un proyecto con la malla y los contornos del talud completo (60 × 32 m,
elementos de 0.5 m): una rampa elástica rígida apoyada en el fondo y un bloque
elástico sobre ella, ambos con 4 partículas por elemento (0.25 m). Se corre una
etapa dinámica sin amortiguamiento, con contacto, y se mide el desplazamiento
del centroide del bloque a lo largo de la pendiente.

Antes de soltar el bloque se corre un geostático con los cuerpos adheridos, como
en el talud; sin él la rampa se asienta de golpe y vibra.

USO
    python tools/experimentos/plano_inclinado.py <salida> [--casos exacta:0.2,gradiente:0.2]

<salida> es una carpeta de trabajo (proyectos, logs y resultados). Modos:
    exacta     normal constante (−sen θ, cos θ): la del plano, dada a mano
    gradiente  normal calculada por gradiente de masa (contact2)
    fija_y     normal vertical, la de la referencia

RESULTADO (2026-09-26, θ = 30°, μ = 0.2, a teórica 3.206 m/s², avance 2.308 m)

    exacta     a = 3.206 m/s², avance 2.308 m   → igual a la teoría
    gradiente  a ≈ 0, avance 0.02 m             → el bloque se traba

    El algoritmo de Coulomb es correcto; lo que falla es la normal por
    gradiente de masa en una superficie inclinada respecto a la malla (errores
    de 15–40° en varios nodos). Decisión: la app usa solo la normal vertical
    (contactos horizontales, como todos los ejemplos del código original; Disc.py
    simula el plano inclinado girando la gravedad). Detalle en
    docs/contacto_multicuerpo.md.
"""
import argparse
import json
import math
import os
import subprocess
import sys

import numpy as np

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PLANTILLA = os.path.join(RAIZ, "test", "6 archivos_mpm 2609",
                         "4_talud_elastoplastico full 10 pasos - particulas igual a V1.json")

THETA = 30.0          # inclinación de la rampa (grados)
L_RAMPA = 14.0        # largo horizontal de la rampa (m)
S0 = 10.0             # posición inicial del bloque a lo largo de la pendiente (m)
LARGO, ALTO = 2.0, 1.0  # bloque, en ejes de la pendiente (m)
H = 0.25              # separación entre partículas (4 por elemento de 0.5)
T = 1.2               # duración (s)
G = 9.81

# (normales, mu): con la normal exacta desliza rápido, lento y no desliza
# (tan 30° = 0.577); y la normal calculada en el caso que debería deslizar
CASOS = [("exacta", 0.2), ("exacta", 0.4), ("exacta", 0.7), ("gradiente", 0.2)]

# Modo 'exacta': el ejecutor pasa a contact2 la normal del plano. No es una
# opción de la app, así que se inyecta en este proceso antes de correr el smoke.
_EXACTA = """
import math, sys
sys.path[:0] = [{app!r}, {tools!r}]
import models.model_execute_analysis as mea, motorMPM.explicit2 as ex2
th = math.radians({theta})
N = (-math.sin(th), math.cos(th))
mea.contact2 = lambda b, nS, pS, mesh, dt, mu, normales=None: ex2.contact2(b, nS, pS, mesh, dt, mu, normales=N)
import smoke_stages
sys.argv = ["smoke_stages"] + sys.argv[1:]
sys.exit(smoke_stages.main())
"""


def particulas():
    th = math.radians(THETA)
    # rampa: centros de celda bajo la recta y = x·tan θ
    rampa = [(x, y) for x in np.arange(H / 2, L_RAMPA, H)
             for y in np.arange(H / 2, L_RAMPA * math.tan(th), H)
             if y <= x * math.tan(th)]
    # bloque: rejilla en ejes (s, n) de la pendiente, girada
    t_ = np.array([math.cos(th), math.sin(th)])    # hacia arriba de la pendiente
    n_ = np.array([-math.sin(th), math.cos(th)])   # normal hacia afuera de la rampa
    bloque = [tuple(S0 * t_ + s * t_ + n * n_)
              for s in np.arange(H / 2, LARGO, H) for n in np.arange(H / 2, ALTO, H)]
    return rampa, bloque


def armar_proyecto(ruta):
    d = json.load(open(PLANTILLA, encoding="utf-8"))
    rampa, bloque = particulas()
    grupos = list(d["PUNTOSMATERIAL"].values())  # [Base, Material Talud]
    mats = {}
    for grupo, pts, nombre, props in (
            (grupos[0], rampa, "Rampa", dict(MODULOELASTICIDAD=2e5, DENSIDAD=2000.0)),
            (grupos[1], bloque, "Bloque", dict(MODULOELASTICIDAD=1e5, DENSIDAD=2000.0))):
        grupo["NAME"] = nombre
        grupo["POINTS"] = {f"POINT#{i + 1}": {"COORDINATES": [float(x), float(y)], "VOLUME": H * H,
                                             "VELOCITY": {"X": 0.0, "Y": 0.0},
                                             "FORCE": {"X": 0.0, "Y": 0.0}}
                           for i, (x, y) in enumerate(pts)}
        mats[grupo["IDPROPIEDAD"]] = dict(COLOR="#888888", NAME=nombre, RELACIONPOISSON=0.3,
                                          COHESION=0.0, ANGULOFRICCION=0.0, ANGULODILATANCIA=0.0,
                                          MODELO="ELASTICO", **props)
    d["MATERIALES"] = mats
    d.setdefault("CONFIGANALISIS", {})["ETAPAS"] = []
    json.dump(d, open(ruta, "w", encoding="utf-8"), ensure_ascii=False)
    return len(rampa), len(bloque)


def correr(proyecto, normales, mu, salida):
    npz = os.path.join(salida, f"plano_{normales}_mu{mu}.npz")
    # Primero un geostático (cuerpos adheridos, un solo campo) para que rampa y
    # bloque arranquen en equilibrio bajo su peso, como en el talud. Sin él, la
    # rampa se asienta de golpe y vibra (0.6 m/s sin amortiguamiento) y eso
    # enmascara el contacto. Después se suelta el bloque con fricción.
    modo = "fija_y" if normales == "exacta" else normales  # 'exacta' se inyecta aparte
    spec = (f"geostatic:n=5,courant=0.6,damp=0.75,plast=0,gauss=1,tolff=0.05;"
            f"dynamic:t={T},courant=0.1,damp=0,plast=0,gauss=0,multi=1,"
            f"mu={mu},normales={modo}")
    if normales == "exacta":
        cmd = [sys.executable, "-c", _EXACTA.format(app=os.path.join(RAIZ, "app"),
                                                    tools=os.path.join(RAIZ, "tools"), theta=THETA)]
    else:
        cmd = [sys.executable, os.path.join(RAIZ, "tools", "smoke_stages.py")]
    log = npz.replace(".npz", ".log")
    with open(log, "w", encoding="utf-8") as fh:
        r = subprocess.run(cmd + [proyecto, "--stages", spec, "--fps", "20", "--export", npz],
                           stdout=fh, stderr=subprocess.STDOUT,
                           env=dict(os.environ, PYTHONIOENCODING="utf-8"))
    return npz if r.returncode == 0 else None


def analizar(npz, n_rampa, mu):
    d = np.load(npz)
    # Solo la etapa dinámica. El eje concatenado avanza de a 1 en el
    # geostático (incrementos) y de a 0.05 s en la dinámica; el último frame
    # del geostático es el estado con que arranca la dinámica.
    k0 = int(np.argmax(np.diff(d["EJE"]) < 0.5))
    d = {k: d[k][:, k0:] for k in ("CORX", "CORY")} | {"EJE": d["EJE"][k0:] - d["EJE"][k0]}
    th = math.radians(THETA)
    abajo = np.array([-math.cos(th), -math.sin(th)])   # dirección pendiente abajo
    normal = np.array([-math.sin(th), math.cos(th)])
    cx, cy = d["CORX"][n_rampa:].mean(axis=0), d["CORY"][n_rampa:].mean(axis=0)
    s = (cx - cx[0]) * abajo[0] + (cy - cy[0]) * abajo[1]      # avance pendiente abajo
    n = (cx - cx[0]) * normal[0] + (cy - cy[0]) * normal[1]    # hundimiento (<0) o despegue
    t = d["EJE"]
    # s = s0 + v0·t + a·t²/2 por mínimos cuadrados, desde t = 0.1 s (sin el
    # transitorio elástico del arranque)
    k = t >= 0.1
    A = np.column_stack((np.ones(k.sum()), t[k], 0.5 * t[k] ** 2))
    a_med = np.linalg.lstsq(A, s[k], rcond=None)[0][2]
    a_teo = max(0.0, G * (math.sin(th) - mu * math.cos(th)))
    return a_med, a_teo, s[-1], n.min(), n.max(), t[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida")
    ap.add_argument("--casos", default=None,
                    help="lista normales:mu separada por comas (default: la tabla CASOS)")
    args = ap.parse_args()
    os.makedirs(args.salida, exist_ok=True)
    casos = CASOS if not args.casos else [
        (c.split(":")[0], float(c.split(":")[1])) for c in args.casos.split(",")]

    proyecto = os.path.join(args.salida, "plano_inclinado.json")
    n_rampa, n_bloque = armar_proyecto(proyecto)
    th = math.radians(THETA)
    print(f"θ = {THETA}° (tan θ = {math.tan(th):.3f}), rampa {n_rampa} part., bloque {n_bloque} part., "
          f"T = {T} s, sin amortiguamiento")
    print(f"\n{'normales':10s} {'μ':>5s} | {'a medida':>9s} {'a teórica':>9s} {'error':>7s} | "
          f"{'avance a T':>10s} {'teórico':>8s} | {'mov. normal mín/máx (m)':>24s}")
    for normales, mu in casos:
        npz = correr(proyecto, normales, mu, args.salida)
        if npz is None:
            print(f"{normales:10s} {mu:5.2f} | FALLÓ la corrida (ver el .log)")
            continue
        a_med, a_teo, s_fin, n_min, n_max, t_fin = analizar(npz, n_rampa, mu)
        err = (f"{100 * (a_med - a_teo) / a_teo:+6.1f}%" if a_teo > 0 else "   —   ")
        print(f"{normales:10s} {mu:5.2f} | {a_med:9.3f} {a_teo:9.3f} {err:>7s} | "
              f"{s_fin:10.3f} {0.5 * a_teo * t_fin ** 2:8.3f} | {n_min:11.4f} / {n_max:.4f}")


if __name__ == "__main__":
    main()
