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
from motorMPM.dos_fases import deltatime_two_phases_CFL

RHO_W = 1.0  # densidad del agua [Mg/m³]


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


def undrained_cp(E, nu, rho_sat, kw, n0):
    """Velocidad de la onda de compresión no drenada (la que fija el dt de
    una etapa de consolidación). Misma expresión que deltatime_two_phases_CFL;
    acepta escalares o arrays y devuelve la máxima."""
    eedo = (1 - nu) / (1 + nu) / (1 - 2 * nu) * np.asarray(E, dtype=float)
    return math.sqrt(np.max((eedo + kw / n0) / np.asarray(rho_sat, dtype=float)))


def compute_two_phase_dt(materials, ele_size, courant):
    """dt de una etapa de consolidación (doble fase), con la misma función
    que usa el ejecutor.

    Args:
        materials: lista de tuplas (E, nu, rho_d, n0, Kw); rho_d es la
                   densidad seca en Mg/m³. La etapa admite un solo material:
                   se usa el primero.
    Returns:
        (dt, speed_cp) o (None, None) si no hay material o le faltan n0/Kw.
    """
    if not materials:
        return None, None
    E, nu, rho_d, n0, kw = materials[0]
    if not n0 or not kw:
        return None, None
    rho_sat = np.array([rho_d + n0 * RHO_W])
    dt = deltatime_two_phases_CFL(np.array([E]), nu, rho_sat, ele_size, courant, kw, n0)
    return dt, undrained_cp(E, nu, rho_sat, kw, n0)


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
