# -*- coding: utf-8 -*-
"""Genera el proyecto de la aplicación para el caso de consolidación 1D.

Mismos datos, malla y partículas que consolidacion_1d.py (Tabla 7-1 de Caro
González, 2024), escritos en el formato .json de MPM-UN, para validar la etapa
de consolidación de la aplicación contra el script (docs/plan_dos_fases_ui.md).
Las partículas se escriben en el orden de setup_MP, el mismo del script.

    - malla de fondo 0.1 × 1.0 m, elementos de 0.1 m
    - un grupo "Columna" de 490 partículas con el material "Suelo saturado"
      (elástico; DENSIDAD = densidad seca ρd; POROSIDAD, PERMEABILIDAD, MODULOAGUA)
    - contornos: laterales con restricción en x, fondo con restricción en y
      (impermeables); superficie libre (drenante)
    - carga q0 = 10 kPa como fuerzas Fy en la fila superior de partículas
    - gravedad 0 y una etapa "consolidation" de 4 s con p0 = q0

USO
    python tools/experimentos/proyecto_consolidacion_1d.py [<salida.json>] [--nmpe 49]
"""
import argparse
import json
import os
import sys
import uuid

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import consolidacion_1d as c1d  # noqa: E402  (agrega app/ al path)
from motorMPM.mesh import traction_forces  # noqa: E402

RAIZ = c1d.RAIZ
SALIDA = os.path.join(RAIZ, "test", "6 archivos_mpm 2609", "8_consolidacion_1d.json")
PLANTILLA = os.path.join(RAIZ, "test", "6 archivos_mpm 2609", "5_talud mini.json")


def _id(nombre):
    """Identificador fijo (el archivo sale igual en cada corrida)."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"mpm-un/consolidacion_1d/{nombre}"))


def armar(nmpe):
    cor, inci, nelex, fixed_x, fixed_y, mp_elem, xp = c1d.armar(nmpe)
    nnx = nelex + 1
    nny = len(cor) // nnx
    tp = traction_forces(xp, 3, -c1d.Q0, 0.0, c1d.LX)
    vol = c1d.ELE * c1d.ELE / nmpe

    d = json.load(open(PLANTILLA, encoding="utf-8"))
    d["INFORMACION"] = {"NOMBREPROYECTO": "Consolidación 1D (Caro González, 2024, §7.1)",
                        "LOCALIZACION": "", "AUTOR": "",
                        "DESCRIPCION": "Validación de la etapa de consolidación contra Terzaghi"}
    d["CONFIGURACION"] = {"GRAVEDAD": 0.0}

    # --- dibujo: el rectángulo de la columna ---
    esquinas = [(0.0, 0.0), (c1d.LX, 0.0), (c1d.LX, c1d.H), (0.0, c1d.H)]
    pids = [_id(f"punto{i}") for i in range(4)]
    d["ITEMSDIBUJO"] = {
        "PUNTOS": {pids[i]: {"NAME": f"POINT#{i + 1}", "COORDINATES": list(esquinas[i])}
                   for i in range(4)},
        "LINEAS": {_id(f"linea{i}"): {"NAME": f"LINE#{i + 1}", "STARTPOINT": pids[i],
                                      "ENDPOINT": pids[(i + 1) % 4]} for i in range(4)},
    }

    # --- malla de fondo (misma numeración que create_uniform_quadrilateral) ---
    nodo = lambda n: f"NODE#{n}"  # noqa: E731
    ids = np.arange(1, len(cor) + 1)
    col, fila = (ids - 1) % nnx, (ids - 1) // nnx
    id_malla = _id("malla_columna")
    d["MESH"] = {
        "MESHBACK": {
            "SIZEDX": c1d.LX, "SIZEDY": c1d.H, "SIZEELEMENT": c1d.ELE,
            "NODES": {nodo(i + 1): {"COORDINATES": [float(cor[i, 0]), float(cor[i, 1])]}
                      for i in range(len(cor))},
            "ELEMENTS": {f"ELEMENT#{e + 1}": [nodo(n) for n in inci[e]] for e in range(len(inci))},
            "NODESBOUNDARYTOP": [nodo(n) for n in ids[fila == nny - 1]],
            "NODESBOUNDARYBOTTOM": [nodo(n) for n in ids[fila == 0]],
            "NODESBOUNDARYLEFT": [nodo(n) for n in ids[col == 0]],
            "NODESBOUNDARYRIGHT": [nodo(n) for n in ids[col == nnx - 1]],
        },
        "TRIANGULARES": {id_malla: {
            "NAME": "Columna", "COLOR": "#4f7fb8",
            "NODES": {nodo(i + 1): {"COORDINATES": list(esquinas[i])} for i in range(4)},
            "ELEMENTS": {"ELEMENT#1": [nodo(1), nodo(2), nodo(3)],
                         "ELEMENT#2": [nodo(1), nodo(3), nodo(4)]},
        }},
        "CUADRILATEROS": {},
    }

    # --- material y puntos materiales ---
    id_mat = _id("suelo_saturado")
    d["MATERIALES"] = {id_mat: {
        "COLOR": "#4f7fb8", "NAME": "Suelo saturado", "MODELO": "ELASTICO",
        "MODULOELASTICIDAD": c1d.E, "RELACIONPOISSON": c1d.NU,
        "COHESION": 0.0, "ANGULOFRICCION": 0.0, "ANGULODILATANCIA": 0.0,
        "DENSIDAD": (1 - c1d.N0) * c1d.RHO_S * 1000.0,          # ρd en kg/m³ (1890)
        "POROSIDAD": c1d.N0, "PERMEABILIDAD": c1d.K, "MODULOAGUA": c1d.KW,
    }}
    d["PUNTOSMATERIAL"] = {_id("grupo_columna"): {
        "NAME": "Columna",
        "POINTS": {f"POINT#{i + 1}": {
            "COORDINATES": [float(xp[i, 0]), float(xp[i, 1])], "VOLUME": vol,
            "VELOCITY": {"X": 0.0, "Y": 0.0},
            "FORCE": {"X": float(tp[i, 0]), "Y": float(tp[i, 1])}} for i in range(len(xp))},
        "IDPROPIEDAD": id_mat, "IDMALLABASE": id_malla,
    }}

    # --- contornos: laterales en x, fondo en y ---
    d["CONTORNOS"] = {
        _id("contorno_laterales"): {"NAME": "Laterales", "NODES": [nodo(n) for n in fixed_x],
                                    "Tx": True, "Ty": False},
        _id("contorno_fondo"): {"NAME": "Fondo", "NODES": [nodo(n) for n in fixed_y],
                                "Tx": False, "Ty": True},
    }

    d["CONFIGANALISIS"] = {"ETAPAS": [{
        "NOMBRE": "Consolidación", "TIPO": "consolidation", "DAMPING": 0.0,
        "COURANT": 0.98, "NUMEROINCREMENTOS": 1, "TIEMPOANALISIS": 4.0,
        "TOLFF": 0.01, "TOLEE": 0.01, "PLASTICIDAD": 0, "GAUSS": False,
        "MULTICUERPO": False, "FRICCION": 0.0, "NORMALESCONTACTO": "fija_y",
        "CAMBIOMATERIAL": {}, "REINICIARDEFORMACIONES": False,
        "PRESIONPOROSINICIAL": c1d.Q0,
    }]}
    for k in d["RESULTADOS"]:
        d["RESULTADOS"][k] = [] if isinstance(d["RESULTADOS"][k], list) else {}
    return d, len(xp)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("salida", nargs="?", default=SALIDA)
    ap.add_argument("--nmpe", type=int, default=49)
    args = ap.parse_args()
    d, nmp = armar(args.nmpe)
    os.makedirs(os.path.dirname(os.path.abspath(args.salida)), exist_ok=True)
    with open(args.salida, "w", encoding="utf-8") as fh:
        json.dump(d, fh, ensure_ascii=False, indent=1)
    print(f"proyecto: {args.salida}  ({nmp} partículas)")


if __name__ == "__main__":
    main()
