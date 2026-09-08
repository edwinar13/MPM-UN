"""
analysis_utils.py
=================

Utilidades de cálculo temporal para el análisis MPM, compartidas por:
  - el controlador del menú Ejecutar (display de dt),
  - el diálogo de etapas (dt estimado por etapa),
  - el modelo de ejecución (dt/pasos por etapa).

Centraliza la lógica que antes vivía embebida en
`controller_MenuExecute.updateTime()`, para no duplicarla.
"""

import math
import numpy as np

from motorMPM.explicit2 import deltatime


def compute_min_dt(materials, ele_size, courant):
    """Calcula el dt mínimo (más restrictivo) entre varios materiales.

    Args:
        materials: lista de tuplas (E, nu, rho) donde rho está en Mg/m³
                   (¡ya convertido!). Cada material es el de un punto material.
        ele_size:  tamaño de elemento de la malla de fondo.
        courant:   número de Courant de la etapa (factor de deltatime).

    Returns:
        (dt, speed_cp, index): dt mínimo, velocidad de onda del material
        crítico, e índice de ese material en la lista `materials`.
        Si `materials` está vacío, retorna (None, None, None).
    """
    if not materials:
        return None, None, None

    best_dt = None
    best_cp = None
    best_idx = None
    for i, (E, nu, rho) in enumerate(materials):
        dt_i, cp_i = deltatime(Ep=E, nu=nu, rhop=rho, ele_size=ele_size, factor=courant)
        if best_dt is None or dt_i < best_dt:
            best_dt = dt_i
            best_cp = cp_i
            best_idx = i
    return best_dt, best_cp, best_idx


def build_time_arrays(dt, analysis_time, fps):
    """Construye los arrays temporales de análisis y de graficado.

    Réplica exacta de la lógica de `controller_MenuExecute.updateTime()`.

    Args:
        dt:            paso de tiempo del análisis.
        analysis_time: duración total de la etapa (s).
        fps:           cuadros por segundo para el graficado.

    Returns:
        dict con: tiempo, tiempographic, dt_graphic, steps, steps_graphic.
    """
    time = math.ceil(analysis_time / dt) * dt
    tiempo = np.arange(0, time, dt)
    tiempo = np.append(tiempo, time)

    if dt < 1.0 / fps:
        ndt = math.floor(1.0 / fps / dt)
        dt_graphic = ndt * dt
    else:
        dt_graphic = dt
    tiempographic = np.arange(0, time, dt_graphic)
    tiempographic = np.append(tiempographic, time)

    return {
        'tiempo': tiempo,
        'tiempographic': tiempographic,
        'dt_graphic': dt_graphic,
        'steps': len(tiempo) - 1,
        'steps_graphic': len(tiempographic) - 1,
    }
