"""
smoke_stages.py — corre un análisis por etapas SIN abrir la interfaz.

Sirve para verificar en segundos que el encadenado de etapas, el handoff,
la concatenación de resultados y los checkpoints funcionan, antes de gastar
horas en una validación larga.

NO escribe el proyecto a disco: los resultados quedan solo en memoria, así
que es seguro correrlo sobre los archivos de referencia de test/.
(Los checkpoints .npz sí se escriben, en <proyecto>_checkpoints/.)

Uso
---
    python tools/smoke_stages.py "<proyecto.json>" --stages "<spec>" [opciones]

El spec de etapas son etapas separadas por ';', cada una:

    tipo:clave=valor,clave=valor

    tipo   geostatic | load_increment | dynamic
    n      n.º de incrementos (cuasi-estático)
    t      duración en segundos (dinámico)
    courant, damp, plast (0|1), gauss (0|1), dincre, tolff, tolee
    nombre etiqueta de la etapa

Ejemplos
--------
    # capacidad portante reducido: geostático + carga
    python tools/smoke_stages.py "test/4  archivos_mpm 2502/3_capacidad_portante (reducido).json" \
        --stages "geostatic:n=2,courant=0.5,damp=0.75,plast=1,gauss=1,nombre=Geo;load_increment:n=2,dincre=-2,courant=0.5,damp=0.75,plast=1,gauss=1,nombre=Carga"

    # reanudar desde el checkpoint de la etapa 1
    python tools/smoke_stages.py "<proyecto>" --stages "..." --resume 2
"""

import argparse
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app"))
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import numpy as np  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402


# --------------------------------------------------------------- spec
_ALIAS = {
    "n": "NUMEROINCREMENTOS", "t": "TIEMPOANALISIS", "courant": "COURANT",
    "damp": "DAMPING", "plast": "PLASTICIDAD", "gauss": "GAUSS",
    "dincre": "DELTAINCREMENTO", "tolff": "TOLFF", "tolee": "TOLEE",
    "nombre": "NOMBRE", "maxit": "MAXITER",
}
_TIPOS = ("geostatic", "load_increment", "dynamic")


def parse_stages(spec):
    """Convierte el spec de la línea de comandos en dicts de etapa."""
    stages = []
    for i, chunk in enumerate(s for s in spec.split(";") if s.strip()):
        tipo, _, rest = chunk.partition(":")
        tipo = tipo.strip()
        if tipo not in _TIPOS:
            raise SystemExit(f"Tipo de etapa desconocido: '{tipo}' (usa {'|'.join(_TIPOS)})")
        st = {
            "NOMBRE": f"Etapa {i + 1}", "TIPO": tipo,
            "DAMPING": 0.75 if tipo != "dynamic" else 0.05,
            "COURANT": 0.6 if tipo == "geostatic" else 0.1,
            "NUMEROINCREMENTOS": 1, "DELTAINCREMENTO": 0.0,
            "DELTAINCREMENTO_GRAV": 0.0,
            "TIEMPOANALISIS": 1.0 if tipo == "dynamic" else 0.0,
            "TOLFF": 0.01, "TOLEE": 0.01,
            "PLASTICIDAD": 0 if tipo == "geostatic" else 1,
            "GAUSS": tipo != "dynamic",
        }
        for pair in (p for p in rest.split(",") if p.strip()):
            k, _, v = pair.partition("=")
            k = k.strip().lower()
            if k not in _ALIAS:
                raise SystemExit(f"Clave desconocida '{k}' en la etapa {i + 1}")
            key = _ALIAS[k]
            v = v.strip()
            if key == "NOMBRE":
                st[key] = v
            elif key in ("NUMEROINCREMENTOS", "PLASTICIDAD", "MAXITER"):
                st[key] = int(v)
            elif key == "GAUSS":
                st[key] = bool(int(v))
            else:
                st[key] = float(v)
        stages.append(st)
    if not stages:
        raise SystemExit("El spec de etapas está vacío")
    return stages


# ------------------------------------------------------- diálogo falso
class FakeDialog:
    """Reemplaza AnalysisProgressDialog: acepta las mismas llamadas y no
    dibuja nada. `cancel_at` permite simular una cancelación del usuario."""

    def __init__(self, cancel_at=None):
        self.cancelled = False
        self.paused = False
        self.accepted = False
        self._calls = 0
        self._cancel_at = cancel_at

    def setProgress(self, v):
        self._calls += 1
        if self._cancel_at is not None and self._calls >= self._cancel_at:
            self.cancelled = True

    def setStatus(self, error=False, status=""):
        pass

    def setTimer(self, t):
        pass

    def setQuestion(self, q):
        pass

    def setViewError(self):
        pass

    def pauseAnalysis(self):
        self.paused = not self.paused

    def close(self):
        pass


def export_npz(ruta, nodes, graphic_time, project_path, stage_dicts, fps):
    """Vuelca los resultados recién calculados al mismo formato que ref_io.py.

    Así `tools/compare_ref.py` puede contrastar la app de HOY contra el motor
    original, en vez de contra el resultado viejo embebido en el `.json`.
    """
    import json as _json

    campos = ("CORX", "CORY", "SIGXX", "SIGYY", "SIGXY",
              "EPSEXX", "EPSEYY", "EPSEXY", "EPSPXX", "EPSPYY", "EPSPXY",
              "VELXX", "VELYY", "VELXY", "DESPLXX", "DESPLYY", "DESPLXY",
              "EQPLAS")
    try:
        ids = sorted(nodes, key=int)
    except (TypeError, ValueError):
        ids = sorted(nodes)

    datos = {}
    for c in campos:
        if c in nodes[ids[0]] and isinstance(nodes[ids[0]][c], list):
            datos[c] = np.array([nodes[i][c] for i in ids], dtype=float)

    meta = {
        "caso": {
            "nombre": f"App MPM-UN — {os.path.basename(project_path)}",
            "proyecto": project_path,
            "fps": fps,
        },
        "etapas": {str(i + 1): s for i, s in enumerate(stage_dicts)},
        "_registro": {
            "nmp": len(ids),
            "nframes": len(graphic_time),
            "eje": "TIEMPO",
            "unidad_eje": "s",
            "campos": [c for c in campos if c in datos],
        },
    }
    datos["EJE"] = np.asarray(graphic_time, dtype=float)
    datos["EJE_NOMBRE"] = np.array("TIEMPO")
    datos["EJE_UNIDAD"] = np.array("s")
    datos["META_JSON"] = np.array(_json.dumps(meta, ensure_ascii=False,
                                              default=str))

    carpeta = os.path.dirname(os.path.abspath(ruta))
    if carpeta and not os.path.exists(carpeta):
        os.makedirs(carpeta)
    if not ruta.endswith(".npz"):
        ruta += ".npz"
    np.savez_compressed(ruta, **datos)
    print(f"EXPORTADO: {ruta}  ({len(ids)} partículas x {len(graphic_time)} frames)")


def load_oracle(path):
    """Lee los resultados que ya están guardados dentro del proyecto.

    Son los de la última corrida que se guardó en ese archivo y sirven de
    patrón para comprobar que un refactor no cambió ningún número.
    """
    import json
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    R = d.get("RESULTADOS") or {}
    return R.get("RESULTADOSNODOS") or {}, R.get("TIEMPOSGRAFICAR") or []


def compare_to_oracle(oracle_nodes, oracle_times, new_nodes, new_times, rtol):
    """Compara campo por campo. Devuelve True si todo entra en la tolerancia."""
    print("-" * 78)
    print("COMPARACIÓN CONTRA EL RESULTADO GUARDADO EN EL PROYECTO")
    if not oracle_nodes:
        print("  El proyecto no trae resultados guardados: no hay con qué comparar.")
        return None

    print(f"  nodos:  guardado={len(oracle_nodes)}  nuevo={len(new_nodes)}")
    print(f"  frames: guardado={len(oracle_times)}  nuevo={len(new_times)}")
    if len(oracle_nodes) != len(new_nodes):
        print("  >> Distinto número de partículas: ¿seleccionaste los mismos grupos?")
        return False

    ids = [k for k in oracle_nodes if k in new_nodes]
    if len(ids) != len(oracle_nodes):
        print(f"  >> {len(oracle_nodes) - len(ids)} nodos del guardado no están en el nuevo")
        return False

    k0 = ids[0]
    campos = [c for c in oracle_nodes[k0]
              if c != "MATERIAL" and c in new_nodes[k0]
              and isinstance(oracle_nodes[k0][c], list)]
    n_old = len(oracle_nodes[k0][campos[0]])
    n_new = len(new_nodes[k0][campos[0]])
    n = min(n_old, n_new)
    if n_old != n_new:
        print(f"  >> Distinto número de frames ({n_old} vs {n_new}); se comparan los primeros {n}")

    # Resumen por FRAME: en un análisis por incrementos, el primer frame que
    # difiere señala el incremento donde las dos corridas se separaron.
    print(f"\n  Por frame (máximo relativo sobre todos los campos):")
    A_all = {c: np.array([oracle_nodes[i][c][:n] for i in ids], dtype=float)
             for c in campos}
    B_all = {c: np.array([new_nodes[i][c][:n] for i in ids], dtype=float)
             for c in campos}
    primer_frame_malo = None
    malos = []
    for f in range(n):
        peor, peor_c = 0.0, ""
        for c in campos:
            a, b = A_all[c][:, f], B_all[c][:, f]
            esc = max(float(np.abs(a).max()), 1e-30)
            r = float(np.abs(a - b).max()) / esc
            if r > peor:
                peor, peor_c = r, c
        if peor > rtol:
            if primer_frame_malo is None:
                primer_frame_malo = f
            malos.append((f, peor, peor_c))
    if not malos:
        print(f"    los {n} frames coinciden (rel <= {rtol:g})")
    else:
        # Solo se listan los frames que difieren: con 100+ frames el resto es ruido
        for f, peor, peor_c in malos[:15]:
            print(f"    frame {f:3d}: rel={peor:11.4e}  DIFIERE (peor: {peor_c})")
        if len(malos) > 15:
            print(f"    ... y {len(malos) - 15} frames más")
        print(f"  >> {len(malos)} de {n} frames difieren; "
              f"se separan a partir del frame {primer_frame_malo}")

    ok = True
    print(f"\n  {'campo':10s} {'max |dif|':>12s} {'max rel':>12s}   dónde")
    for c in sorted(campos):
        A, B = A_all[c], B_all[c]
        dif = np.abs(A - B)
        amax = float(dif.max()) if dif.size else 0.0
        escala = max(float(np.abs(A).max()), 1e-30) if A.size else 1.0
        rel = amax / escala
        donde = ""
        if amax > 0 and dif.size:
            r, f = np.unravel_index(int(dif.argmax()), dif.shape)
            donde = f"nodo {ids[r]}, frame {f}"
        marca = "" if rel <= rtol else "   <-- DIFIERE"
        if rel > rtol:
            ok = False
        print(f"  {c:10s} {amax:12.4e} {rel:12.4e}   {donde}{marca}")

    print("-" * 78)
    print("  RESULTADO: IDÉNTICO (dentro de la tolerancia)" if ok else
          "  RESULTADO: HAY DIFERENCIAS")
    return ok


def main():
    ap = argparse.ArgumentParser(description="Smoke test de etapas sin GUI")
    ap.add_argument("project", help="ruta del .json del proyecto")
    ap.add_argument("--stages", required=True, help="spec de etapas (ver docstring)")
    ap.add_argument("--mp", default=None,
                    help="nombres de grupos de puntos materiales a usar, separados por coma "
                         "(por defecto: todos)")
    ap.add_argument("--resume", type=int, default=0,
                    help="reanudar desde la etapa N usando el checkpoint de la N-1")
    ap.add_argument("--cancel-at", type=int, default=None,
                    help="simular cancelación tras N actualizaciones de progreso")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--compare", action="store_true",
                    help="comparar el resultado nuevo contra el que ya está guardado "
                         "dentro del .json (oráculo de la corrida anterior)")
    ap.add_argument("--rtol", type=float, default=1e-9,
                    help="tolerancia relativa para --compare (default 1e-9)")
    ap.add_argument("--export", metavar="SALIDA.npz",
                    help="volcar los resultados de esta corrida al formato de "
                         "ref_io.py, para contrastarlos con tools/compare_ref.py")
    args = ap.parse_args()

    if not os.path.exists(args.project):
        raise SystemExit(f"No existe el proyecto: {args.project}")

    stage_dicts = parse_stages(args.stages)

    app = QApplication.instance() or QApplication([])
    from views.view_GraphicsDraw import ViewGraphicsSceneDraw, ViewGraphicsViewDraw
    from views.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult
    from models.model_ProjectCurrent import ModelProjectCurrent
    from models.model_analysis_config import AnalysisConfig, TimeConfig
    from models.model_execute_analysis import ModelExcuteAnalysisMPM
    from models.analysis_utils import compute_min_dt, build_time_arrays

    print("=" * 78)
    print(f"PROYECTO : {os.path.basename(args.project)}")

    # El oráculo hay que leerlo del disco ANTES de correr: saveResults() borra
    # los resultados previos del modelo en memoria.
    oracle_nodes, oracle_times = ({}, [])
    if args.compare:
        oracle_nodes, oracle_times = load_oracle(args.project)

    sd = ViewGraphicsSceneDraw()
    v1, v2 = ViewGraphicsViewDraw(), ViewGraphicsViewDraw()
    sr, vr = ViewGraphicsSceneResult(), ViewGraphicsViewResult()
    v1.setScene(sd); v2.setScene(sd); vr.setScene(sr)
    project = ModelProjectCurrent(sr, vr, sd, v1, v2, path_doc=args.project)

    # --- selección de puntos materiales y contornos ---
    models_mp = project.getModelsPointsMaterials()
    wanted = [s.strip() for s in args.mp.split(",")] if args.mp else None
    list_point_material = {}
    for id_mp, m in models_mp.items():
        if wanted is None or m.getName() in wanted:
            list_point_material[id_mp] = {"name": m.getName()}
    if not list_point_material:
        raise SystemExit(f"Ningún grupo coincide con --mp {args.mp}. "
                         f"Disponibles: {[m.getName() for m in models_mp.values()]}")
    list_boundaries = [{"id": k, "name": m.getName()}
                       for k, m in project.getModelsBoundaries().items()]

    npts = sum(len(models_mp[k].getPoints()) for k in list_point_material)
    print(f"GRUPOS   : {[v['name'] for v in list_point_material.values()]}  ({npts} partículas)")
    print(f"CONTORNOS: {len(list_boundaries)}  |  gravedad={project.getGravity()}")
    print(f"MALLA    : ele={project.model_mesh_back.getSizeElement()}")
    print("ETAPAS   :")
    for i, s in enumerate(stage_dicts):
        extra = (f"t={s['TIEMPOANALISIS']}s" if s["TIPO"] == "dynamic"
                 else f"n={s['NUMEROINCREMENTOS']}, dincre={s['DELTAINCREMENTO']}")
        print(f"   {i+1}. {s['TIPO']:15s} '{s['NOMBRE']}'  courant={s['COURANT']} "
              f"damp={s['DAMPING']} plast={s['PLASTICIDAD']} gauss={s['GAUSS']}  {extra}")
    if args.resume:
        print(f"REANUDAR : desde la etapa {args.resume}")
    print("=" * 78)

    config = AnalysisConfig.from_stage_dicts(
        stage_dicts=stage_dicts, gravity=project.getGravity(),
        time_config=TimeConfig(fps=args.fps), resume_from_stage=args.resume)

    # MAXITER no se persiste en el .mpm: es solo para diagnóstico desde aquí
    for st, spec in zip(config.stages, stage_dicts):
        if "MAXITER" in spec:
            st.max_iterations = spec["MAXITER"]

    # --- semilla de tiempo (igual que el controlador) ---
    materials, prop_ids = [], []
    for id_mp in list_point_material:
        data = models_mp[id_mp].getProperty().getData()
        k = list(data.keys())[0]
        materials.append((data[k]["MODULOELASTICIDAD"], data[k]["RELACIONPOISSON"],
                          data[k]["DENSIDAD"] / 1000.0))
        prop_ids.append(k)
    ele = project.model_mesh_back.getSizeElement()
    dt, cp, idx = compute_min_dt(materials, ele, config.stages[0].courant_number)
    dur = config.stages[0].analysis_time or 1.0
    ta = build_time_arrays(dt, dur, args.fps)
    dataTime = {
        "id_property": prop_ids[idx if idx is not None else 0],
        "courant_number": config.stages[0].courant_number, "analysis_time": dur,
        "fps": args.fps, "dt_analysis": dt, "dt_graphic": ta["dt_graphic"],
        "analysis_steps": ta["steps"], "graphic_steps": ta["steps_graphic"], "speed_cp": cp,
    }

    dialog = FakeDialog(cancel_at=args.cancel_at)
    mpm = ModelExcuteAnalysisMPM(
        analysis_dialog=dialog, model_current_project=project,
        model_result=project.getModelResult(), dataTime=dataTime,
        list_boundaries=list_boundaries, list_point_material=list_point_material,
        dt_time=dt, list_time=ta["tiempo"], steps_time=ta["steps"],
        dt_graphic=ta["dt_graphic"], list_time_graphic=ta["tiempographic"],
        steps_time_graphic=ta["steps_graphic"], analysis_config=config)

    t0 = time.time()
    ok = mpm.run()
    elapsed = time.time() - t0

    print("=" * 78)
    print(f"RESULTADO: run()={ok}  parcial={mpm.cancelled_partial}  "
          f"({elapsed:.1f}s incluyendo compilación Numba)")
    if mpm.error_message:
        print(f"MOTIVO   : {mpm.error_message}")

    if ok:
        res = project.getModelResult().getData()
        nodes = res.get("RESULT_NODES") or {}
        gt = res.get("GRAPHIC_TIME") or []
        db = res.get("DATA_BASE") or {}
        print(f"NODOS    : {len(nodes)}  (esperado {npts})")
        print(f"FRAMES   : {len(gt)}")
        print("ETAPAS_FRAMES:")
        for f in db.get("ETAPAS_FRAMES", []):
            print(f"   Etapa {f['ETAPA']} ({f['TIPO']:15s}) frames {f['FRAME_INICIO']}-{f['FRAME_FIN']}"
                  f"  dt={f['DT']:.3e}")
        if nodes:
            k0 = next(iter(nodes))
            sy = nodes[k0].get("SIGYY", [])
            print(f"SIGYY nodo {k0}: primero={sy[0]:.4g}  último={sy[-1]:.4g}" if sy else "")

        if args.compare:
            compare_to_oracle(oracle_nodes, oracle_times, nodes, gt, args.rtol)

        if args.export:
            export_npz(args.export, nodes, gt, args.project, stage_dicts, args.fps)

    ck_dir = project.getCheckpointDir()
    if os.path.isdir(ck_dir):
        files = sorted(os.listdir(ck_dir))
        print(f"CHECKPOINTS ({ck_dir}):")
        for f in files:
            kb = os.path.getsize(os.path.join(ck_dir, f)) / 1024
            print(f"   {f}  ({kb:.0f} KB)")
    else:
        print("CHECKPOINTS: ninguno")

    print("=" * 78)
    print("NOTA: el proyecto NO se guardó a disco; los resultados quedaron en memoria.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
