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

Example projects are located in `test
/4  archivos_mpm 2502` (`.mpm` files).

## Dependencies

```bash
pip install -r requirements.txt
```

Key packages: PySide6 6.6.1, NumPy 1.26.2, Numba 0.60.0, Matplotlib 3.8.2, gmsh 4.12.0, meshio 5.3.4, scipy 1.0. Python 3.9+ required (64-bit recommended due to memory requirements).

## Testing

There is no automated test suite. Validation is done manually by loading `.mpm` project files from `tests/` and verifying simulation outputs visually through the UI.

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

### `app/models/` — Data Layer

- **[model_ProjectCurrent.py](app/models/model_ProjectCurrent.py)** — Central project state hub: geometry, mesh, material points, properties, boundaries. The UI reads/writes through this model.
- **[model_analysis_config.py](app/models/model_analysis_config.py)** — `AnalysisConfig` dataclass: the standard interface between UI and solver. Contains `AnalysisType` (DYNAMIC / QUASI_STATIC / MIXED), `LoadMode`, `AnalysisStage`, and `TimeConfig`. **This is the new decoupled approach being adopted.**
- **[model_execute_analysis.py](app/models/model_execute_analysis.py)** — Orchestrates solver execution. Currently being refactored to consume `AnalysisConfig` instead of legacy case-specific methods (`runViga`, `runAnalysisCE`).
- **[model_Result.py](app/models/model_Result.py)** — Stores simulation output arrays (stresses, displacements, velocities, positions per time step).
- Other models: `ModelMesh`, `ModelMaterialPoint`, `ModelProperty`, `ModelBoundary`, `ModelRepository`.

### `app/controllers/` — Interaction Logic

Controllers wire UI events to model operations. `ControllerMainWindow` is the top-level orchestrator. Sub-controllers handle each panel (draw menu, execute, results, cards).

### `app/views/` and `app/ui/` — Presentation Layer

- `app/ui/` contains Qt Designer `.ui` files and their generated Python counterparts (`ui_*.py`). **Do not manually edit generated `ui_*.py` files** — regenerate from `.ui` with `pyside6-uic`.
- `app/views/` contains custom view classes that extend generated UI classes.

### `app/config.py`

Singleton `ConfigManager` handling theme/style settings, read from `app/resources/db/Config.json`.

## Active Refactoring: UI–Engine Decoupling

The branch `feature/generalize-ui-engine-connection` is migrating from tight coupling (case-specific `run*` methods) to a general interface:

1. **UI controller** extracts data from `ModelProjectCurrent` and builds an `AnalysisConfig`.
2. **`model_execute_analysis.py`** receives `AnalysisConfig` and drives the solver generically.
3. **`motorMPM/`** functions receive plain NumPy arrays — they must never import from `models/` or `views/`.

The factory methods `AnalysisConfig.from_legacy_viga()` and `AnalysisConfig.from_legacy_ce()` in [model_analysis_config.py](app/models/model_analysis_config.py) bridge old and new flows during migration.

## Important Conventions

- **Numba functions** in `explicit2.py` use `@njit`. They only accept NumPy arrays and Python scalars — no Python objects, dicts, or dataclasses. Translate `AnalysisConfig` to plain arrays/scalars before calling them.
- **Project files** use the `.mpm` extension and are serialized by `ModelRepository` (likely pickle or JSON — check before modifying serialization).
- **`use_gauss_integration`** in `AnalysisConfig` selects `particles_to_nodes_gauss2` (for Capacity/CE-type problems) vs. `particles_to_nodes` (standard). This must match the problem type.
- **`plasticity_flag`** (aka `elapla` in `explicit2.py`): `0` = linear elastic, `1` = elastoplastic (Mohr-Coulomb). Matches the solver's `nodes_to_particle_stress*` (`if elapla == 0: lineal elastico`). In Fase A this becomes per-stage (`AnalysisStage.plasticity_flag`).
- **Damping**: quasi-static stages use ~0.75; dynamic stages use 0.0–0.05.
