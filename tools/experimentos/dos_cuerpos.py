# -*- coding: utf-8 -*-
"""Paso multicuerpo de la app contra el ciclo de falla de la referencia, bit a bit.

Criterio de aceptación de B2 en docs/plan_fase_b.md. Mismo espíritu que
dos_motores.py: el MISMO estado de entrada se avanza N pasos por dos caminos
y se compara todo al final.

    APP         ModelExcuteAnalysisMPM._run_one_mpm_step_multibody
                (motorMPM.explicit2: contact2, stress2, ...)
    REFERENCIA  el cuerpo del ciclo de fase_falla() de talud_2021_v2.py
                (l. 616-693), copiado tal cual, con las funciones del motor
                ORIGINAL (V1/mpm_un) y los arrays de cada cuerpo por separado

Malla, contornos, masas y propiedades salen del proyecto de la app, así que
lo único que se compara es el ciclo: el orden de operaciones, las vistas por
cuerpo y la escritura de vuelta en los arrays únicos.

Estado de entrada: el checkpoint de la etapa 1 (geostático) del proyecto, si
existe; si no, el estado inicial del proyecto.

USO
    python tools/experimentos/dos_cuerpos.py "<proyecto.json>" [N] [--elastico Grupo]

RESULTADO (2026-09-23): ver docs/contacto_multicuerpo.md, registro de cambios.
"""
import argparse
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
V1 = r"D:\01 PROGRAMACION Y DESARROLLO\Tesis UNAL Geotecnia\1 Referencia\Codigo MPM-UN Original_V1"
sys.path.insert(0, os.path.join(RAIZ, "app"))
sys.path.insert(0, os.path.join(RAIZ, "tools"))
sys.path.insert(0, V1)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import numpy as np  # noqa: E402
from PySide6.QtWidgets import QApplication  # noqa: E402

from mpm_un.mesh import search_MP  # noqa: E402  (motor original)
from mpm_un.explicit2 import (particles_to_nodes, contact, nodes_to_particle_vel,  # noqa: E402
                              BC_Dirichlet_vel, nodes_to_particle_stress2,
                              BC_Dirichlet_momentum3)

P = "_ModelExcuteAnalysisMPM__"   # prefijo de los atributos privados del ejecutor


def montar_app(ruta, elasticos):
    app = QApplication.instance() or QApplication([])
    from views.view_GraphicsDraw import ViewGraphicsSceneDraw, ViewGraphicsViewDraw
    from views.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult
    from models.model_ProjectCurrent import ModelProjectCurrent
    from models.model_analysis_config import AnalysisStage, StageType
    from models.model_execute_analysis import ModelExcuteAnalysisMPM
    from smoke_stages import FakeDialog

    sd = ViewGraphicsSceneDraw()
    v1, v2 = ViewGraphicsViewDraw(), ViewGraphicsViewDraw()
    sr, vr = ViewGraphicsSceneResult(), ViewGraphicsViewResult()
    v1.setScene(sd); v2.setScene(sd); vr.setScene(sr)
    project = ModelProjectCurrent(sr, vr, sd, v1, v2, path_doc=ruta)

    models_mp = project.getModelsPointsMaterials()
    for m in models_mp.values():
        if m.getName() in elasticos:
            data = m.getProperty().getData()
            data[list(data.keys())[0]]["MODELO"] = "ELASTICO"
    lpm = {k: {"name": m.getName()} for k, m in models_mp.items()}
    lb = [{"id": k, "name": m.getName()} for k, m in project.getModelsBoundaries().items()]

    ex = ModelExcuteAnalysisMPM(
        analysis_dialog=FakeDialog(), model_current_project=project,
        model_result=project.getModelResult(), dataTime={}, list_boundaries=lb,
        list_point_material=lpm, dt_time=0.0, list_time=None, steps_time=0,
        dt_graphic=0.0, list_time_graphic=None, steps_time_graphic=0)
    ex.initConditions(); ex.initBoundary(); ex.initMaterialPoint()
    ex.initProperties(); ex.initVerctorAndMatrix(); ex.initBoundaryParticles()

    stage = AnalysisStage(stage_type=StageType.DYNAMIC, damping_factor=0.10,
                          courant_number=0.1, plasticity_flag=1, use_gauss=False,
                          multi_body=True, friction=0.268, analysis_time=1.0)
    ck = project.getCheckpointPath(1)
    if os.path.exists(ck):
        state, meta = ex._load_checkpoint(1)
        if state is not None:
            ex._inject_state(state)
            print(f"estado de entrada: checkpoint {ck} ({meta['fecha']})")
    getattr(ex, P + "vm_vp")[:] = 0.0        # como el handoff a dinámico
    ex._prepare_stage_time(stage)
    setattr(ex, P + "step_dampfac", stage.damping_factor)
    setattr(ex, P + "vm_tp_current", getattr(ex, P + "vm_tp0").copy())
    getattr(ex, P + "vm_bp")[:] = getattr(ex, P + "vm_bp0")
    return app, ex, stage


def copia_por_cuerpo(ex):
    """Arrays de cada cuerpo, COPIADOS (como en el script: arrays sueltos)."""
    g = lambda n: getattr(ex, P + n)
    out = []
    for b in g("bodies"):
        s = slice(b["start"], b["end"])
        out.append({k: np.array(v[s]) for k, v in (
            ("xp", g("mp_xp")), ("vp", g("vm_vp")), ("Vp", g("vm_Vp")),
            ("Vp0", g("vm_Vp0")), ("Mp", g("vm_Mp")), ("sig", g("vm_sig")),
            ("bp", g("vm_bp")), ("tp", g("vm_tp_current")), ("Fp", g("vm_Fp")),
            ("epse", g("vm_epse")), ("epsp", g("vm_epsp")), ("Prop", g("mp_prop")),
            ("mp_elem", g("mp_mp_elem")))})
    return out


def paso_referencia(c1, c2, ex, flags, mu):
    """Cuerpo del ciclo de fase_falla(), talud_2021_v2.py l. 618-693."""
    mesh_app = ex.mesh
    inci, cor = mesh_app.inci(), mesh_app.cor()
    ele_size, nelex = mesh_app.ele_size(), mesh_app.nelex()
    fixed_nodesX = getattr(ex, P + "bo_fixed_nodesX")
    fixed_nodesY = getattr(ex, P + "bo_fixed_nodesY")
    node_support = getattr(ex, P + "node_support")
    dtime = getattr(ex, P + "tm_dt_time")
    alpha = getattr(ex, P + "step_dampfac")

    xp_1, vp_1, Vp_1, Vp0_1, Mp_1 = c1["xp"], c1["vp"], c1["Vp"], c1["Vp0"], c1["Mp"]
    sig_1, bp_1, tp_1, Fp_1 = c1["sig"], c1["bp"], c1["tp"], c1["Fp"]
    epse_1, epsp_1, Prop_1, mp_elem_1 = c1["epse"], c1["epsp"], c1["Prop"], c1["mp_elem"]
    xp_2, vp_2, Vp_2, Vp0_2, Mp_2 = c2["xp"], c2["vp"], c2["Vp"], c2["Vp0"], c2["Mp"]
    sig_2, bp_2, tp_2, Fp_2 = c2["sig"], c2["bp"], c2["tp"], c2["Fp"]
    epse_2, epsp_2, Prop_2, mp_elem_2 = c2["epse"], c2["epsp"], c2["Prop"], c2["mp_elem"]

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
    ndamping_1 = -dampfac*np.multiply(np.absolute(niforce_1 + neforce_1), np.sign(nmomentum_1))
    nforce_1 = niforce_1 + neforce_1 + ndamping_1
    nmomentum_1 += nforce_1*dtime
    ndamping_2 = -dampfac*np.multiply(np.absolute(niforce_2 + neforce_2), np.sign(nmomentum_2))
    nforce_2 = niforce_2 + neforce_2 + ndamping_2
    nmomentum_2 += nforce_2*dtime

    nmassS = nmass_1 + nmass_2
    nmomentumS = nmomentum_1 + nmomentum_2
    mesh = inci, cor, node_support, active_nodes
    body1 = nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1
    body2 = nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2
    nmomentum_1, nmomentum_2 = contact(body1, body2, nmassS, nmomentumS, mesh, dtime, mu)
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
    Fp_1, Vp_1, epse_1, epsp_1, sig_1 = nodes_to_particle_stress2(grid_1, particle_1, nvel_1, dtime, flags[0])
    particle_2 = Fp_2, Vp_2, Vp0_2, epse_2, epsp_2, sig_2, shfnp_2, Prop_2
    Fp_2, Vp_2, epse_2, epsp_2, sig_2 = nodes_to_particle_stress2(grid_2, particle_2, nvel_2, dtime, flags[1])

    c1.update(xp=xp_1, vp=vp_1, Vp=Vp_1, Fp=Fp_1, sig=sig_1, epse=epse_1, epsp=epsp_1, mp_elem=mp_elem_1)
    c2.update(xp=xp_2, vp=vp_2, Vp=Vp_2, Fp=Fp_2, sig=sig_2, epse=epse_2, epsp=epsp_2, mp_elem=mp_elem_2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("n", nargs="?", type=int, default=50)
    ap.add_argument("--elastico", default="")
    args = ap.parse_args()
    elasticos = [s.strip() for s in args.elastico.split(",") if s.strip()]

    _app, ex, stage = montar_app(args.project, elasticos)
    bodies = getattr(ex, P + "bodies")
    flags = ex._body_plasticity_flags(stage)
    print(f"cuerpos: {[(b['name'], b['end'] - b['start']) for b in bodies]}  "
          f"plasticidad={flags}  dt={getattr(ex, P + 'tm_dt_time'):.4e}  pasos={args.n}")
    assert len(bodies) == 2, "el experimento es para dos cuerpos"

    ref = copia_por_cuerpo(ex)
    ini = copia_por_cuerpo(ex)
    setattr(ex, P + "node_support", ex.mesh.nodeSupport())
    for _ in range(args.n):
        paso_referencia(ref[0], ref[1], ex, flags, stage.friction)
        ex._run_one_mpm_step_multibody(flags, stage.friction)

    app_out = copia_por_cuerpo(ex)
    peor = 0.0
    print(f"\n{'campo':8s} {'max|dif|':>12s}   (cuerpo 1 | cuerpo 2)")
    for k in ("xp", "vp", "Vp", "Fp", "sig", "epse", "epsp", "mp_elem"):
        d = [float(np.abs(np.asarray(a[k], float) - np.asarray(r[k], float)).max())
             for a, r in zip(app_out, ref)]
        peor = max(peor, *d)
        print(f"{k:8s} {max(d):12.3e}   ({d[0]:.3e} | {d[1]:.3e})")
    # Que el caso no sea trivial: los cuerpos se movieron y hubo plasticidad
    print(f"\ndesplazamiento máx. en {args.n} pasos: cuerpo 1 "
          f"{np.abs(ref[0]['xp'] - ini[0]['xp']).max():.3e} m, cuerpo 2 "
          f"{np.abs(ref[1]['xp'] - ini[1]['xp']).max():.3e} m; "
          f"epsp máx. cuerpo 2 {np.abs(ref[1]['epsp']).max():.3e}")
    print("RESULTADO:", "IDÉNTICO (0.000e+00)" if peor == 0.0 else f"DIFIERE (max {peor:.3e})")
    return 0 if peor == 0.0 else 1


if __name__ == "__main__":
    sys.exit(main())
