# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**MPM-UN** is a GUI application for geotechnical numerical simulation using the Material Point Method (MPM). It is a graduate research project at Universidad Nacional de Colombia. The GUI wraps a Python-based explicit MPM solver accelerated with Numba.

## Running the Application

Must be run from the repository root:

```bash
python app/main.py
```

The app uses relative paths like `app/resources/...`, so running from a different directory will fail. On first run, it creates `app/resources/db/Config.json` automatically.

Example projects are located in `test/4  archivos_mpm 2502/` and `test/5 archivos_mpm 2607/` (`.json` project files). The large ones embed the results of validated legacy runs under `RESULTADOS` and serve as numerical oracles; the "(reducido)"/"mini" ones are for smoke tests (seconds).

## Dependencies

```bash
pip install -r requirements.txt
```

Key packages: PySide6 6.6.1, NumPy 1.26.2, Numba 0.60.0, Matplotlib 3.8.2, gmsh 4.12.0, meshio 5.3.4, scipy 1.0. Python 3.9+ required (64-bit recommended due to memory requirements).

## Testing

There is no automated test suite. Validation is done manually by loading project files from `test/` and verifying simulation outputs visually through the UI. Full validation runs take hours; **always run the smoke matrix in [docs/plan_pre_validacion.md](docs/plan_pre_validacion.md) first** (same project, tiny stage parameters), and compare against the embedded legacy results with `tools/compare_results.py`.

## Architecture

The app follows a strict MVC pattern with PySide6. The three layers never cross-reference:

```
UI Event → Controller → Model → motorMPM (solver) → Model → View
```

### `app/motorMPM/` — The Solver Engine (most critical)

This is the computational core, fully decoupled from the UI.

- **[explicit2.py](app/motorMPM/explicit2.py)** — Main solver (~124KB). Contains Numba-`@njit` functions for the full explicit time integration loop: shape function evaluation, P2N (particle-to-node) mapping, N2P (node-to-particle) velocity/stress updates, boundary condition enforcement, and elastoplastic constitutive models.
- **[explicit.py](app/motorMPM/explicit.py)** and **[explicit3.py](app/motorMPM/explicit3.py)** — Alternative explicit schemes (legacy/experimental).
- **[mesh.py](app/motorMPM/mesh.py)** — Background mesh generation and node connectivity (triangular and quadrilateral elements). Wraps gmsh/pygmsh.
- **[graphics.py](app/motorMPM/graphics.py)** — Post-processing: generates per-frame result images for animation.
- **`Ejemplos/`** — Reference scripts the app must reproduce: `beam.py` (viga, elástico dinámico), `Ca_portante2.py` (capacidad portante, carga incremental, **gravedad 0**), `talud_2021_v2.py` (geostático → colapso; guarda/carga el estado geostático en `.npz`, dos cuerpos con contacto).

### `app/models/` — Data Layer

- **[model_ProjectCurrent.py](app/models/model_ProjectCurrent.py)** — Central project state hub: geometry, mesh, material points, properties, boundaries. The UI reads/writes through this model.
- **[model_analysis_config.py](app/models/model_analysis_config.py)** — `AnalysisConfig` dataclass: the interface between UI and solver. Holds an ordered list of `AnalysisStage` (per-stage type, damping, Courant, plasticity, gauss integration, increments/duration), the global gravity and `resume_from_stage`. Stages are persisted in the project under `CONFIGANALISIS.ETAPAS` and edited in [view_DialogStages.py](app/views/view_DialogStages.py). `AnalysisConfig.from_stage_dicts()` is the only entry point.
- **[analysis_utils.py](app/models/analysis_utils.py)** — `compute_min_dt` / `build_time_arrays`: the single dt formula shared by controller, stage dialog and executor.
- **[model_execute_analysis.py](app/models/model_execute_analysis.py)** — Orchestrates solver execution: `run()` → init pipeline → `execute()` loops all stages with state handoff (`_capture_state`/`_inject_state`) → `saveResults()`. Legacy case-specific methods (`runViga`, `runAnalysisCE`, `executeAnalysis*`) are kept only as numerical reference until validation passes; do not extend them.
- **[model_Result.py](app/models/model_Result.py)** — Stores simulation output arrays (stresses, displacements, velocities, positions per time step).
- Other models: `ModelMesh`, `ModelMaterialPoint`, `ModelProperty`, `ModelBoundary`, `ModelRepository`.

### `app/controllers/` — Interaction Logic

Controllers wire UI events to model operations. `ControllerMainWindow` is the top-level orchestrator. Sub-controllers handle each panel (draw menu, execute, results, cards).

### `app/views/` and `app/ui/` — Presentation Layer

- `app/ui/` contains Qt Designer `.ui` files and their generated Python counterparts (`ui_*.py`). **Do not manually edit generated `ui_*.py` files** — regenerate from `.ui` with `pyside6-uic`.
- `app/views/` contains custom view classes that extend generated UI classes. `view_DialogStages.py` is built in code (no `.ui`).

### `app/config.py`

Singleton `ConfigManager` handling theme/style settings, read from `app/resources/db/Config.json`.

## Active Work: stage system, pre-validation closure

The branch `feature/generalize-ui-engine-connection` replaced the case-specific `run*` flow with a generic stage pipeline:

1. **UI controller** (`controller_MenuExecute.py`) reads `ModelProjectCurrent.getStages()` and builds an `AnalysisConfig` via `from_stage_dicts()`.
2. **`model_execute_analysis.py`** drives the solver stage by stage, recomputing dt per stage from its Courant.
3. **`motorMPM/`** functions receive plain NumPy arrays — they must never import from `models/` or `views/`.

The current plan (results concatenated across stages, per-stage checkpoints `.npz` with resume, alignment with the reference scripts, cleanup) is in [docs/plan_pre_validacion.md](docs/plan_pre_validacion.md). After validation, [docs/plan_simplificacion_cargas.md](docs/plan_simplificacion_cargas.md) simplifies load definition.

## Important Conventions

- **Numba functions** in `explicit2.py` use `@njit`. They only accept NumPy arrays and Python scalars — no Python objects, dicts, or dataclasses. Translate `AnalysisStage` fields to plain scalars before calling them.
- **Project files** are JSON (loaded with `json.load` in `ModelRepository`), with Spanish upper-case keys (`CONFIGURACION`, `PUNTOSMATERIAL`, `CONFIGANALISIS`, `RESULTADOS`, ...). New keys follow that convention.
- **Gauss integration** is per stage: `AnalysisStage.use_gauss` (`None` = decided by type in `stage_use_gauss()`: geostatic/load_increment → `particles_to_nodes_gauss2` + `nodes_to_particle_stress_gauss`; dynamic → `particles_to_nodes` + `nodes_to_particle_stress2`).
- **Plasticity** is per stage: `AnalysisStage.plasticity_flag` (aka `elapla` in `explicit2.py`): `0` = linear elastic, `1` = elastoplastic (Mohr-Coulomb).
- **Damping** is per stage: quasi-static stages use ~0.75; dynamic stages use 0.0–0.10 (talud reference: 0.10).
- **Units**: kN, kPa, m, Mg, s. Density is converted to Mg/m³ (`DENSIDAD / 1000`) before reaching the solver. `Fx`/`Fy` on particles are forces in kN per metre of thickness, not stresses.
