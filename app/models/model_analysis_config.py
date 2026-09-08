"""
model_analysis_config.py
========================

Define la configuración de análisis para el motor MPM.

Toda la configuración vive en las ETAPAS (`AnalysisStage`): cada etapa
lleva su tipo, damping, Courant, plasticidad, integración y parámetros
de carga/tiempo. La UI (DialogStages) las persiste en el .mpm bajo
`CONFIGANALISIS.ETAPAS`; el controlador de Ejecutar construye un
`AnalysisConfig` con `from_stage_dicts()` y se lo entrega al modelo de
ejecución, que recorre las etapas en orden.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class AnalysisType(Enum):
    """Tipo general del análisis (derivado de la mezcla de etapas)."""
    DYNAMIC = "dynamic"
    QUASI_STATIC = "quasi_static"
    MIXED = "mixed"  # cuasi-estático seguido de dinámico


class StageType(Enum):
    """Tipo de etapa de análisis."""
    GEOSTATIC = "geostatic"          # Equilibrio bajo peso propio (rampa de gravedad)
    DYNAMIC = "dynamic"              # Evolución en el tiempo
    LOAD_INCREMENT = "load_increment"  # Carga incremental cuasi-estática


@dataclass
class AnalysisStage:
    """
    Define una etapa individual de análisis.

    Una simulación puede tener múltiples etapas que se ejecutan
    secuencialmente. Por ejemplo:
    1. Etapa geoestática (equilibrio por peso propio)
    2. Etapa dinámica (colapso, sismo, etc.)

    Cada etapa tiene su propio tipo, damping y configuración de carga.
    """

    # Tipo de etapa
    stage_type: StageType = StageType.DYNAMIC

    # Amortiguamiento para esta etapa
    # - Dinámico puro:     0.00 - 0.10
    # - Cuasi-estático:    0.50 - 0.80 (típicamente 0.75)
    damping_factor: float = 0.0

    # ─── Parámetros de convergencia (solo para cuasi-estático) ───
    # Tolerancia del desbalance de fuerzas normalizado
    convergence_tol_force: float = 0.01
    # Tolerancia de la energía cinética normalizada
    convergence_tol_energy: float = 0.01
    # Máximo de iteraciones antes de abortar (seguridad)
    max_iterations: int = 50000

    # ─── Parámetros de carga (solo si aplica) ───
    # Número de incrementos de carga o de rampa de gravedad
    n_increments: int = 1
    # Valor del incremento de carga (multiplica a Fx/Fy de las partículas).
    # Pendiente de eliminar: ver docs/plan_simplificacion_cargas.md
    load_increment_value: float = 0.0
    # Valor del incremento de gravedad. 0 = gravedad completa desde el
    # primer incremento. Pendiente de eliminar junto con load_increment_value.
    gravity_increment_value: float = 0.0

    # ─── Configuración por etapa ───
    # Etiqueta para la UI ("Geostático", "Falla", ...)
    name: str = ""
    # Número de Courant de ESTA etapa (talud: 0.6 geoestático / 0.1 falla)
    courant_number: float = 0.1
    # Duración en segundos (solo etapas dinámicas)
    analysis_time: float = 0.0
    # Flag de plasticidad de la etapa: 0 = elástico, 1 = elastoplástico (MC)
    plasticity_flag: int = 1
    # Integración: True = gauss (particles_to_nodes_gauss2), False = estándar.
    # None = se decide por el tipo de etapa (ver stage_use_gauss()).
    use_gauss: Optional[bool] = None

    # ─── Serialización (persistencia en el .mpm) ───
    def to_dict(self) -> dict:
        """Serializa la etapa a un dict con claves JSON (español)."""
        return {
            "NOMBRE": self.name,
            "TIPO": self.stage_type.value,
            "DAMPING": self.damping_factor,
            "COURANT": self.courant_number,
            "NUMEROINCREMENTOS": self.n_increments,
            "DELTAINCREMENTO": self.load_increment_value,
            "DELTAINCREMENTO_GRAV": self.gravity_increment_value,
            "TIEMPOANALISIS": self.analysis_time,
            "TOLFF": self.convergence_tol_force,
            "TOLEE": self.convergence_tol_energy,
            "PLASTICIDAD": self.plasticity_flag,
            "GAUSS": self.use_gauss,
        }

    @staticmethod
    def from_dict(d: dict) -> 'AnalysisStage':
        """Reconstruye una etapa desde un dict persistido."""
        return AnalysisStage(
            stage_type=StageType(d.get("TIPO", StageType.DYNAMIC.value)),
            damping_factor=d.get("DAMPING", 0.0),
            convergence_tol_force=d.get("TOLFF", 0.01),
            convergence_tol_energy=d.get("TOLEE", 0.01),
            n_increments=int(d.get("NUMEROINCREMENTOS", 1)),
            load_increment_value=d.get("DELTAINCREMENTO", 0.0),
            gravity_increment_value=d.get("DELTAINCREMENTO_GRAV", 0.0),
            name=d.get("NOMBRE", ""),
            courant_number=d.get("COURANT", 0.1),
            analysis_time=d.get("TIEMPOANALISIS", 0.0),
            plasticity_flag=int(d.get("PLASTICIDAD", 1)),
            use_gauss=d.get("GAUSS", None),
        )


def stage_use_gauss(stage: AnalysisStage) -> bool:
    """Decide si la etapa usa integración gaussiana.

    Si stage.use_gauss es None, se usa el default por tipo:
    geoestático/carga incremental → gauss ON, dinámico → OFF.
    """
    if stage.use_gauss is not None:
        return bool(stage.use_gauss)
    return stage.stage_type in (StageType.GEOSTATIC, StageType.LOAD_INCREMENT)


@dataclass
class TimeConfig:
    """
    Configuración de tiempo y discretización temporal.

    Hoy solo `fps` gobierna algo (cuadros por segundo del graficado);
    el dt y los pasos se recalculan por etapa en el ejecutor según el
    Courant de cada una. El resto de campos se conserva como metadato
    de la "semilla" que se guarda en los resultados.
    """

    # ID del material de referencia para calcular la velocidad de onda
    id_property_courant: str = ""
    # Número de Courant (controla dt = courant * ele_size / c_p)
    courant_number: float = 0.1
    # Tiempo total de simulación (s) - solo para análisis dinámico
    analysis_time: float = 1.0
    # Frames por segundo para la captura de resultados gráficos
    fps: int = 30

    # ─── Valores derivados (calculados por la UI) ───
    # Paso de tiempo del análisis
    dt_analysis: float = 0.0
    # Paso de tiempo para guardar gráficos
    dt_graphic: float = 0.0
    # Número total de pasos de análisis
    analysis_steps: int = 0
    # Número total de pasos gráficos
    graphic_steps: int = 0
    # Velocidad de onda de compresión (m/s)
    speed_cp: float = 0.0


@dataclass
class AnalysisConfig:
    """
    Configuración completa de un análisis MPM.

    Empaqueta todos los parámetros necesarios para ejecutar una
    simulación MPM, sin depender de los objetos de la UI.

    El flujo es:
        UI (controller) → from_stage_dicts() → pasa a model_execute_analysis

    Atributos:
        analysis_type:      Tipo general, derivado de las etapas (informativo)
        gravity:            Aceleración de gravedad (m/s²)
        time_config:        Configuración temporal (fps)
        stages:             Lista ordenada de etapas de análisis
        resume_from_stage:  0 = desde el inicio; N ≥ 2 = arrancar en la
                            etapa N usando el checkpoint guardado al
                            terminar la etapa N-1
    """

    # ─── Tipo de análisis (derivado, informativo) ───
    analysis_type: AnalysisType = AnalysisType.DYNAMIC

    # ─── Parámetros físicos ───
    # Gravedad en m/s² (positiva, se aplica como -gravity en la dirección Y)
    gravity: float = 9.81

    # ─── Configuración de tiempo ───
    time_config: TimeConfig = field(default_factory=TimeConfig)

    # ─── Etapas de análisis (lista ordenada, nunca vacía) ───
    stages: list = field(default_factory=list)

    # ─── Reanudar desde checkpoint ───
    resume_from_stage: int = 0

    @staticmethod
    def from_stage_dicts(stage_dicts: list, gravity: float,
                         time_config: 'TimeConfig' = None,
                         resume_from_stage: int = 0) -> 'AnalysisConfig':
        """Construye un AnalysisConfig desde la lista de etapas persistida.

        Es el punto de entrada del panel de etapas: la UI entrega
        `model_current_project.getStages()` (lista de dicts) + la gravedad
        global + la config de tiempo (para fps). El analysis_type se deriva
        de la mezcla de etapas.

        Args:
            stage_dicts: lista de dicts (ver AnalysisStage.to_dict()).
            gravity: gravedad global (m/s²).
            time_config: TimeConfig con al menos fps (para pasos gráficos).
            resume_from_stage: ver atributo del mismo nombre.
        """
        stages = [AnalysisStage.from_dict(d) for d in stage_dicts]
        if not stages:
            # Sin etapas: una dinámica por defecto (no debería pasar; el
            # controlador valida antes)
            stages = [AnalysisStage(stage_type=StageType.DYNAMIC, name="Etapa 1")]

        # Derivar el tipo general a partir de los tipos de etapa presentes
        types = {s.stage_type for s in stages}
        has_dynamic = StageType.DYNAMIC in types
        has_quasi = bool(types & {StageType.GEOSTATIC, StageType.LOAD_INCREMENT})
        if has_dynamic and has_quasi:
            analysis_type = AnalysisType.MIXED
        elif has_dynamic:
            analysis_type = AnalysisType.DYNAMIC
        else:
            analysis_type = AnalysisType.QUASI_STATIC

        return AnalysisConfig(
            analysis_type=analysis_type,
            gravity=gravity,
            time_config=time_config if time_config is not None else TimeConfig(),
            stages=stages,
            resume_from_stage=int(resume_from_stage or 0),
        )

    def __repr__(self):
        stages_str = '\n    '.join(
            f"Stage {i+1}: {s.stage_type.value} '{s.name}' "
            f"(damping={s.damping_factor}, courant={s.courant_number}, "
            f"plast={s.plasticity_flag}, gauss={stage_use_gauss(s)})"
            for i, s in enumerate(self.stages)
        )
        return (
            f"AnalysisConfig(\n"
            f"  type={self.analysis_type.value},\n"
            f"  gravity={self.gravity},\n"
            f"  resume_from_stage={self.resume_from_stage},\n"
            f"  stages=[\n    {stages_str}\n  ]\n"
            f")"
        )
