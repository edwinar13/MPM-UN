# -*- coding: utf-8 -*-
"""Compara una corrida de referencia contra los resultados de la app.

La referencia es el `.npz` que dejan los scripts originales del MPM-UN
(`1 Referencia/Codigo MPM-UN Original_V1/resultados_referencia/*.npz`, escritos
por `ref_io.py`). El otro lado es un proyecto `.json` de la app, ya corrido, con
sus resultados en `RESULTADOS.RESULTADOSNODOS`.

Esto NO es lo mismo que `smoke_stages.py --compare`: ese compara la app contra
la propia app (regresión). Este compara la app contra el motor original, que es
lo que valida la integración.

Uso:

    python tools/compare_ref.py REFERENCIA.npz PROYECTO.json
    python tools/compare_ref.py ref/beam.npz "test/5 .../1_validacion_viga.json" \
        --material "Material  Beam" --frames-comunes
    python tools/compare_ref.py ref/beam.npz proyecto.json --campos SIGXX,SIGYY --top 5

Sale con código 0 si todo entra en la tolerancia, 1 si no, 2 si ni siquiera se
pudieron alinear las dos corridas.

Cómo alinea las dos corridas:

* **Partículas**: por su posición inicial (frame 0), no por el orden en que
  aparecen. Así el resultado no depende de cómo cada lado numeró los puntos, y
  de paso comprueba que los dos discretizaron el mismo dominio.
* **Frames**: por el valor del eje (tiempo, carga o fracción de gravedad). Si los
  dos ejes no coinciden — típicamente porque el FPS del proyecto no es el del
  script — lo dice y con `--frames-comunes` compara solo los que sí calzan.
"""

from __future__ import annotations

import argparse
import json
import os
import sys

import numpy as np

CAMPOS = (
    "CORX", "CORY",
    "SIGXX", "SIGYY", "SIGXY",
    "EPSEXX", "EPSEYY", "EPSEXY",
    "EPSPXX", "EPSPYY", "EPSPXY",
    "VELXX", "VELYY", "VELXY",
    "DESPLXX", "DESPLYY", "DESPLXY",
    "EQPLAS",
)

ANCHO = 78


# ----------------------------------------------------------------- carga ---
def cargar_referencia(ruta):
    if not os.path.isfile(ruta):
        sys.exit(f"No existe la referencia: {ruta}")
    d = np.load(ruta, allow_pickle=False)
    campos = {c: np.asarray(d[c], dtype=float) for c in CAMPOS if c in d.files}
    if not campos:
        sys.exit(f"{ruta} no tiene ninguno de los campos esperados.")
    meta = {}
    if "META_JSON" in d.files:
        try:
            meta = json.loads(str(d["META_JSON"]))
        except (ValueError, TypeError):
            meta = {}
    eje = np.asarray(d["EJE"], dtype=float) if "EJE" in d.files else None
    nombre_eje = str(d["EJE_NOMBRE"]) if "EJE_NOMBRE" in d.files else "FRAME"
    unidad_eje = str(d["EJE_UNIDAD"]) if "EJE_UNIDAD" in d.files else ""
    if eje is None:
        eje = np.arange(next(iter(campos.values())).shape[1], dtype=float)
    return campos, eje, nombre_eje, unidad_eje, meta


def cargar_app(ruta, material=None):
    """Lado app: un proyecto .json ya corrido, o un .npz de smoke_stages --export.

    El .npz viene de la app de HOY; el .json trae el resultado de la corrida que
    se guardó en su momento, que puede ser de otra versión del código.
    """
    if not os.path.isfile(ruta):
        sys.exit(f"No existe el proyecto: {ruta}")

    if ruta.lower().endswith(".npz"):
        if material:
            sys.exit("--material solo aplica a proyectos .json; el .npz ya viene "
                     "filtrado por los grupos que se pasaron a --mp.")
        campos, eje, _, _, _ = cargar_referencia(ruta)
        return campos, eje, {}, campos["CORX"].shape[0]

    with open(ruta, encoding="utf-8") as fh:
        proyecto = json.load(fh)
    R = proyecto.get("RESULTADOS") or {}
    nodos = R.get("RESULTADOSNODOS") or {}
    if not nodos:
        sys.exit(f"{ruta} no trae resultados guardados. Corré el análisis primero.")

    materiales = R.get("MATERIALES") or {}
    if material:
        uuids = [u for u, m in materiales.items()
                 if m.get("NAME", "").strip().lower() == material.strip().lower()
                 or u == material]
        if not uuids:
            disponibles = ", ".join(sorted(
                repr(m.get("NAME", u)) for u, m in materiales.items()))
            sys.exit(f"No hay un material '{material}'. Hay: {disponibles}")
        ids = [k for k in nodos if nodos[k].get("MATERIAL") in uuids]
        if not ids:
            sys.exit(f"Ningún punto material pertenece a '{material}'.")
    else:
        ids = list(nodos)

    try:
        ids.sort(key=int)
    except (TypeError, ValueError):
        ids.sort()

    campos = {}
    for c in CAMPOS:
        if c in nodos[ids[0]] and isinstance(nodos[ids[0]][c], list):
            campos[c] = np.array([nodos[i][c] for i in ids], dtype=float)
    eje = np.asarray(R.get("TIEMPOSGRAFICAR") or [], dtype=float)
    if eje.size == 0:
        eje = np.arange(next(iter(campos.values())).shape[1], dtype=float)
    return campos, eje, materiales, len(nodos)


# ------------------------------------------------------------ alineación ---
def orden_por_posicion(x, y):
    """Permutación que ordena las partículas por su posición inicial."""
    return np.lexsort((np.round(y, 9), np.round(x, 9)))


def emparejar_particulas(ref, app, tol_pos):
    n_ref = ref["CORX"].shape[0]
    n_app = app["CORX"].shape[0]
    print(f"  partículas:  referencia={n_ref}   app={n_app}")
    if n_ref != n_app:
        print("  >> Distinto número de partículas. Revisá el dominio, ele_size y")
        print("     nmpe del proyecto, o filtrá el grupo con --material.")
        return None, None

    p_ref = orden_por_posicion(ref["CORX"][:, 0], ref["CORY"][:, 0])
    p_app = orden_por_posicion(app["CORX"][:, 0], app["CORY"][:, 0])

    dx = np.abs(ref["CORX"][p_ref, 0] - app["CORX"][p_app, 0])
    dy = np.abs(ref["CORY"][p_ref, 0] - app["CORY"][p_app, 0])
    peor = float(max(dx.max(), dy.max()))
    if peor > tol_pos:
        print(f"  >> Las posiciones iniciales no coinciden (máx {peor:.3e} m > "
              f"{tol_pos:.0e}).")
        print("     Los dos lados no están discretizando el mismo dominio.")
        return None, None
    print(f"  emparejadas por posición inicial (desajuste máx {peor:.3e} m)")
    return p_ref, p_app


def emparejar_frames(eje_ref, eje_app, nombre_eje, unidad, comunes):
    n_ref, n_app = len(eje_ref), len(eje_app)
    print(f"  frames:      referencia={n_ref}   app={n_app}")

    if n_ref == n_app:
        desfase = float(np.abs(eje_ref - eje_app).max())
        if desfase <= 1e-6 * max(1.0, float(np.abs(eje_ref).max())):
            print(f"  ejes {nombre_eje} idénticos "
                  f"({eje_ref[0]:.4g} a {eje_ref[-1]:.4g} {unidad})")
            return np.arange(n_ref), np.arange(n_app)
        print(f"  >> Mismo número de frames pero el eje difiere (máx {desfase:.3e})")

    # La mediana y no el mínimo: el último frame se agrega aparte y suele quedar
    # a un intervalo mucho más corto que el resto, lo que falsearía el paso.
    paso_ref = np.median(np.diff(eje_ref)) if n_ref > 1 else 1.0
    paso_app = np.median(np.diff(eje_app)) if n_app > 1 else 1.0
    # Tope de 5.1e-4: la app redondea TIEMPOSGRAFICAR a 3 decimales, así que esa
    # es la única holgura legítima. Con medio paso se emparejarían frames que
    # están a un dt del solver de distancia, que son estados distintos.
    tol = min(0.4 * min(abs(paso_ref), abs(paso_app)), 5.1e-4)

    i_ref, i_app, desfases = [], [], []
    for j, t in enumerate(eje_app):
        k = int(np.argmin(np.abs(eje_ref - t)))
        if abs(eje_ref[k] - t) <= tol:
            i_ref.append(k)
            i_app.append(j)
            desfases.append(abs(eje_ref[k] - t))

    print(f"  paso del eje: referencia={paso_ref:.4g}  app={paso_app:.4g} {unidad}")
    print(f"  frames en común: {len(i_app)}", end="")
    if desfases:
        print(f"   (desajuste máx {max(desfases):.3e} {unidad})")
    else:
        print()
    if len(i_app) < 2:
        print("  >> Los ejes no calzan: casi no hay frames comparables.")
        print(f"     Ajustá el FPS del proyecto para que el paso sea {paso_ref:.4g} "
              f"{unidad}.")
        return None, None
    if not comunes:
        print("  >> Los ejes no son iguales. Con --frames-comunes se comparan solo")
        print(f"     los {len(i_app)} frames que coinciden.")
        return None, None
    return np.array(i_ref), np.array(i_app)


# ------------------------------------------------------------ comparación ---
def comparar(ref, app, p_ref, p_app, f_ref, f_app, campos, rtol, piso, top,
             eje_ref, nombre_eje, unidad):
    print("-" * ANCHO)
    print("DIFERENCIAS POR CAMPO")
    print(f"  {'campo':<9} {'máx |Δ|':>13} {'máx rel':>11} {'escala':>13}   dónde")

    peor_global = 0.0
    filas_malas = []
    detalle = {}

    for c in campos:
        a = ref[c][np.ix_(p_ref, f_ref)]
        b = app[c][np.ix_(p_app, f_app)]
        dif = np.abs(a - b)
        escala = max(float(np.abs(a).max()), piso)
        rel = float(dif.max()) / escala
        detalle[c] = (dif, rel)
        peor_global = max(peor_global, rel)

        idx = np.unravel_index(int(np.argmax(dif)), dif.shape)
        marca = " " if rel <= rtol else " <<"
        print(f"  {c:<9} {dif.max():13.6e} {rel:11.3e} {escala:13.6e}   "
              f"part {p_app[idx[0]]}, frame {f_app[idx[1]]}{marca}")
        if rel > rtol:
            filas_malas.append((c, rel))

    if not filas_malas:
        print(f"\n  Todos los campos dentro de rtol={rtol:.0e}.")
        return peor_global, True

    # Primer frame donde se separan: en un análisis por incrementos señala el
    # incremento exacto en que las dos corridas dejaron de coincidir.
    print("-" * ANCHO)
    print("POR FRAME (peor campo en cada uno, solo los que exceden la tolerancia)")
    n_frames = len(f_app)
    malos = []
    for f in range(n_frames):
        peor, cual = 0.0, ""
        for c in campos:
            dif, _ = detalle[c]
            escala = max(float(np.abs(ref[c][np.ix_(p_ref, f_ref)][:, f]).max()),
                         piso)
            r = float(dif[:, f].max()) / escala
            if r > peor:
                peor, cual = r, c
        if peor > rtol:
            malos.append((f, peor, cual))

    if malos:
        print(f"  {len(malos)} de {n_frames} frames difieren. Primeros {min(top, len(malos))}:")
        for f, peor, cual in malos[:top]:
            print(f"    frame {f_app[f]:>5}  {nombre_eje.lower()}="
                  f"{eje_ref[f_ref[f]]:>10.4g} {unidad:<5} peor={peor:.3e} ({cual})")
        if len(malos) > top:
            print(f"    ... y {len(malos) - top} más")
        if malos[0][0] == 0:
            print("\n  Difieren desde el frame 0: el estado inicial ya no es el mismo")
            print("  (propiedades del material, gravedad o estado de esfuerzos).")
    return peor_global, False


# ------------------------------------------------------------------ main ---
def main():
    ap = argparse.ArgumentParser(
        description="Compara una corrida de referencia (.npz) contra los "
                    "resultados guardados en un proyecto de la app (.json).")
    ap.add_argument("referencia", help="ruta al .npz escrito por ref_io.py")
    ap.add_argument("proyecto", help="ruta al .json de la app, ya corrido")
    ap.add_argument("--material", help="nombre del material a comparar, si el "
                                       "proyecto tiene más de un grupo")
    ap.add_argument("--campos", help="lista separada por comas; por defecto todos")
    ap.add_argument("--rtol", type=float, default=1e-9,
                    help="tolerancia relativa (por defecto 1e-9)")
    ap.add_argument("--tol-pos", type=float, default=1e-9,
                    help="tolerancia al emparejar posiciones iniciales, en m")
    ap.add_argument("--piso", type=float, default=1e-30,
                    help="escala mínima para el error relativo")
    ap.add_argument("--frames-comunes", action="store_true",
                    help="si los ejes no coinciden, comparar solo los frames "
                         "que sí calzan")
    ap.add_argument("--top", type=int, default=8,
                    help="cuántos frames malos listar")
    args = ap.parse_args()

    ref, eje_ref, nombre_eje, unidad, meta = cargar_referencia(args.referencia)
    app, eje_app, materiales, n_total = cargar_app(args.proyecto, args.material)

    print("=" * ANCHO)
    print("REFERENCIA (motor original)  vs  APP MPM-UN")
    print("=" * ANCHO)
    caso = (meta.get("caso") or {}).get("nombre", "?")
    print(f"  caso:       {caso}")
    print(f"  referencia: {args.referencia}")
    print(f"  proyecto:   {args.proyecto}")
    if args.material:
        print(f"  material:   {args.material}  "
              f"({app['CORX'].shape[0]} de {n_total} puntos)")
    print("-" * ANCHO)
    print("ALINEACIÓN")

    p_ref, p_app = emparejar_particulas(ref, app, args.tol_pos)
    if p_ref is None:
        return 2

    f_ref, f_app = emparejar_frames(eje_ref, eje_app, nombre_eje, unidad,
                                    args.frames_comunes)
    if f_ref is None:
        return 2

    comunes = [c for c in CAMPOS if c in ref and c in app]
    if args.campos:
        pedidos = [c.strip().upper() for c in args.campos.split(",")]
        faltan = [c for c in pedidos if c not in comunes]
        if faltan:
            sys.exit(f"Estos campos no están en ambos lados: {', '.join(faltan)}")
        comunes = pedidos
    if not comunes:
        sys.exit("Los dos archivos no comparten ningún campo.")

    peor, ok = comparar(ref, app, p_ref, p_app, f_ref, f_app, comunes,
                        args.rtol, args.piso, args.top,
                        eje_ref, nombre_eje, unidad)

    print("=" * ANCHO)
    if ok:
        print(f"COINCIDEN  (peor error relativo {peor:.3e} <= rtol {args.rtol:.0e})")
        print(f"Comparados {len(comunes)} campos, {p_app.size} partículas, "
              f"{len(f_app)} frames.")
        return 0
    print(f"DIFIEREN  (peor error relativo {peor:.3e} > rtol {args.rtol:.0e})")
    return 1


if __name__ == "__main__":
    sys.exit(main())
