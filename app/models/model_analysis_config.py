"""
model_analysis_config.py
========================

Define la configuración de análisis para el motor MPM.

Este módulo centraliza todos los parámetros que controlan la ejecución
de una simulación MPM, independientemente del tipo de análisis
(dinámico, cuasi-estático, mixto).

La UI construye un AnalysisConfig y lo pasa al modelo de ejecución.
"""

from dataclasses import dataclass, field
from typing import Optional
from enum import Enum


class AnalysisType(Enum):
    """Tipo de solución temporal del análisis."""
    DYNAMIC = "dynamic"
    QUASI_STATIC = "quasi_static"
    MIXED = "mixed"  # geoestático seguido de dinámico


class LoadMode(Enum):
    """Modo de aplicación de carga."""
    INSTANT_GRAVITY = "instant_gravity"      # Gravedad instantánea
    GRAVITY_RAMP = "gravity_ramp"            # Rampa de gravedad incremental
    LOAD_INCREMENTS = "load_increments"      # Incrementos de carga externa


class StageType(Enum):
    """Tipo de etapa de análisis."""
    GEOSTATIC = "geostatic"          # Equilibrio bajo peso propio
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
    # - Dinámico puro:     0.00 - 0.05
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
    # Valor del incremento de carga (kN/m por incremento, signo negativo = hacia abajo)
    load_increment_value: float = 0.0
    # Valor del incremento de gravedad (kN/m por incremento)
    gravity_increment_value: float = 0.0

    # ─── Parámetros temporales (solo para dinámico) ───
    # Número de pasos de tiempo para la etapa dinámica
    time_steps: int = 0
    # dt se calcula automáticamente por Courant, pero puede sobreescribirse
    dt_override: Optional[float] = None

    # ─── Configuración por etapa (Fase A: panel de etapas) ───
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

    Estos valores se derivan del panel de tiempo de la UI.
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
        UI (controller) → construye AnalysisConfig → pasa a model_execute_analysis

    Atributos principales:
        analysis_type:  Tipo general (dinámico / cuasi-estático / mixto)
        load_mode:      Cómo se aplica la carga
        gravity:        Aceleración de gravedad (m/s²)
        time_config:    Configuración temporal
        stages:         Lista de etapas de análisis
        use_gauss:      Si se usa integración gaussiana para traction forces
    """

    # ─── Tipo de análisis ───
    analysis_type: AnalysisType = AnalysisType.DYNAMIC
    load_mode: LoadMode = LoadMode.INSTANT_GRAVITY

    # ─── Parámetros físicos ───
    # Gravedad en m/s² (positiva, se aplica como -gravity en la dirección Y)
    gravity: float = 9.81

    # ─── Configuración de tiempo ───
    time_config: TimeConfig = field(default_factory=TimeConfig)

    # ─── Etapas de análisis ───
    # Lista ordenada de etapas. Si está vacía, se crea una etapa por defecto
    # basada en analysis_type y load_mode
    stages: list = field(default_factory=list)

    # ─── Integración numérica ───
    # True = usar particles_to_nodes_gauss2 (para traction forces / CE)
    # False = usar particles_to_nodes (estándar)
    use_gauss_integration: bool = False
    # Flag de plasticidad (elapla en explicit2.py):
    #   0 = elástico lineal
    #   1 = elastoplástico (Mohr-Coulomb)
    # NOTA: en Fase A la plasticidad pasa a ser por-etapa (AnalysisStage.plasticity_flag).
    # Este campo se mantiene como fallback/compatibilidad. Default 0 = elástico
    # (coincide con el comportamiento de la viga/beam validada).
    plasticity_flag: int = 0

    def build_default_stages(self):
        """
        Construye las etapas de análisis por defecto basadas en
        el analysis_type y load_mode, si no se han definido manualmente.

        Se llama automáticamente si stages está vacío al iniciar
        la ejecución.
        """
        if self.stages:
            return  # Ya hay etapas definidas, no sobreescribir

        if self.analysis_type == AnalysisType.DYNAMIC:
            # Una sola etapa dinámica
            self.stages = [
                AnalysisStage(
                    stage_type=StageType.DYNAMIC,
                    damping_factor=0.0,
                    time_steps=self.time_config.analysis_steps
                )
            ]

        elif self.analysis_type == AnalysisType.QUASI_STATIC:
            if self.load_mode == LoadMode.LOAD_INCREMENTS:
                # Cuasi-estático con incrementos de carga
                self.stages = [
                    AnalysisStage(
                        stage_type=StageType.LOAD_INCREMENT,
                        damping_factor=0.75,
                    )
                ]
            elif self.load_mode == LoadMode.GRAVITY_RAMP:
                # Cuasi-estático con rampa de gravedad
                self.stages = [
                    AnalysisStage(
                        stage_type=StageType.GEOSTATIC,
                        damping_factor=0.75,
                    )
                ]
            else:
                # Cuasi-estático con gravedad instantánea
                self.stages = [
                    AnalysisStage(
                        stage_type=StageType.GEOSTATIC,
                        damping_factor=0.75,
                    )
                ]

        elif self.analysis_type == AnalysisType.MIXED:
            # Primero geoestático, luego dinámico
            self.stages = [
                AnalysisStage(
                    stage_type=StageType.GEOSTATIC,
                    damping_factor=0.75,
                ),
                AnalysisStage(
                    stage_type=StageType.DYNAMIC,
                    damping_factor=0.04,
                    time_steps=self.time_config.analysis_steps
                )
            ]

    @staticmethod
    def from_stage_dicts(stage_dicts: list, gravity: float,
                         time_config: 'TimeConfig' = None) -> 'AnalysisConfig':
        """Construye un AnalysisConfig desde la lista de etapas persistida.

        Es el punto de entrada del panel de etapas: la UI entrega
        `model_current_project.getStages()` (lista de dicts) + la gravedad
        global + la config de tiempo (para fps). El analysis_type se deriva
        de la mezcla de etapas.

        Args:
            stage_dicts: lista de dicts (ver AnalysisStage.to_dict()).
            gravity: gravedad global (m/s²).
            time_config: TimeConfig con al menos fps (para pasos gráficos).
        """
        stages = [AnalysisStage.from_dict(d) for d in stage_dicts]
        if not stages:
            # Sin etapas: una dinámica por defecto (no debería pasar tras migración)
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
        )

    @staticmethod
    def from_legacy_viga(dataTime: dict, gravity: float, dampfac: float) -> 'AnalysisConfig':
        """
        Crea un AnalysisConfig a partir de los parámetros legacy
        de un análisis tipo Viga (dinámico puro).

        Esto permite mantener compatibilidad con el flujo actual
        mientras se migra gradualmente.

        Args:
            dataTime: Diccionario con los parámetros de tiempo de la UI.
            gravity: Gravedad (m/s²).
            dampfac: Factor de amortiguamiento.
        """
        time_config = TimeConfig(
            id_property_courant=dataTime.get('id_property', ''),
            courant_number=dataTime.get('courant_number', 0.1),
            analysis_time=dataTime.get('analysis_time', 1.0),
            fps=dataTime.get('fps', 30),
            dt_analysis=dataTime.get('dt_analysis', 0.0),
            dt_graphic=dataTime.get('dt_graphic', 0.0),
            analysis_steps=dataTime.get('analysis_steps', 0),
            graphic_steps=dataTime.get('graphic_steps', 0),
            speed_cp=dataTime.get('speed_cp', 0.0),
        )

        config = AnalysisConfig(
            analysis_type=AnalysisType.DYNAMIC,
            load_mode=LoadMode.INSTANT_GRAVITY,
            gravity=gravity,
            time_config=time_config,
            use_gauss_integration=False,
            stages=[
                AnalysisStage(
                    stage_type=StageType.DYNAMIC,
                    damping_factor=dampfac,
                    time_steps=time_config.analysis_steps,
                )
            ]
        )
        return config

    @staticmethod
    def from_legacy_ce(dataTime: dict, gravity: float, dampfac: float,
                       nincre: int, dincre: float,
                       dincreGrav: float) -> 'AnalysisConfig':
        """
        Crea un AnalysisConfig a partir de los parámetros legacy
        de un análisis tipo Capacidad Portante / Cuasi-Estático.

        Args:
            dataTime: Diccionario con los parámetros de tiempo de la UI.
            gravity: Gravedad (m/s²).
            dampfac: Factor de amortiguamiento.
            nincre: Número de incrementos de carga.
            dincre: Valor del incremento de carga (kN/m).
            dincreGrav: Valor del incremento de gravedad (kN/m).
        """
        time_config = TimeConfig(
            id_property_courant=dataTime.get('id_property', ''),
            courant_number=dataTime.get('courant_number', 0.1),
            analysis_time=dataTime.get('analysis_time', 1.0),
            fps=dataTime.get('fps', 30),
            dt_analysis=dataTime.get('dt_analysis', 0.0),
            dt_graphic=dataTime.get('dt_graphic', 0.0),
            analysis_steps=dataTime.get('analysis_steps', 0),
            graphic_steps=dataTime.get('graphic_steps', 0),
            speed_cp=dataTime.get('speed_cp', 0.0),
        )

        config = AnalysisConfig(
            analysis_type=AnalysisType.QUASI_STATIC,
            load_mode=LoadMode.LOAD_INCREMENTS,
            gravity=gravity,
            time_config=time_config,
            use_gauss_integration=True,
            stages=[
                AnalysisStage(
                    stage_type=StageType.LOAD_INCREMENT,
                    damping_factor=dampfac,
                    n_increments=nincre,
                    load_increment_value=dincre,
                    gravity_increment_value=dincreGrav,
                )
            ]
        )
        return config

    def __repr__(self):
        stages_str = '\n    '.join(
            f"Stage {i+1}: {s.stage_type.value} (damping={s.damping_factor})"
            for i, s in enumerate(self.stages)
        )
        return (
            f"AnalysisConfig(\n"
            f"  type={self.analysis_type.value},\n"
            f"  load={self.load_mode.value},\n"
            f"  gravity={self.gravity},\n"
            f"  gauss={self.use_gauss_integration},\n"
            f"  stages=[\n    {stages_str}\n  ]\n"
            f")"
        )
