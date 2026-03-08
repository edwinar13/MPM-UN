# Plan de Implementación: Generalización UI → Motor MPM

## Objetivo

Reemplazar los métodos específicos (`runViga`, `runAnalysisCE`, `runAnalysisDisc`) por un **único flujo de ejecución genérico** (`run`) que funcione para cualquier tipo de análisis (dinámico, cuasi-estático, mixto), parametrizado por la configuración que el usuario define en la UI.

---

## Diagnóstico del Estado Actual

### Flujo Actual (Acoplado)

```
controller_MenuExecute.py (línea 323-325)
│
├─ if tipo == "CE":  → analysis_mpm.runAnalysisCE()
│                        ├─ initConditionsAnalysisCE()   ← ESPECÍFICO (incrementos de carga)
│                        ├─ initConditions()             ← GENÉRICO ✅
│                        ├─ initBoundary()               ← GENÉRICO ✅
│                        ├─ initMaterialPoint()          ← GENÉRICO ✅
│                        ├─ initProperties()             ← GENÉRICO ✅
│                        ├─ initVectorAndMatrix()        ← GENÉRICO ✅
│                        ├─ initBoundaryParticles()      ← GENÉRICO ✅
│                        ├─ executeAnalysisCE()          ← ESPECÍFICO (while + damping 0.75)
│                        └─ saveResults()                ← GENÉRICO ✅
│
└─ else:             → analysis_mpm.runViga()
                         ├─ initConditions()             ← GENÉRICO ✅
                         ├─ initBoundary()               ← GENÉRICO ✅
                         ├─ initMaterialPoint()          ← GENÉRICO ✅
                         ├─ initProperties()             ← GENÉRICO ✅
                         ├─ initVectorAndMatrix()        ← GENÉRICO ✅
                         ├─ initBoundaryParticles()      ← GENÉRICO ✅
                         ├─ executeAnalysisViga()         ← ESPECÍFICO (for t + damping 0.0)
                         └─ saveResults()                ← GENÉRICO ✅
```

**Problema**: El 90% del código ya es genérico. Solo difieren:
1. `executeAnalysisCE` (~340 líneas) vs `executeAnalysisViga` (~296 líneas) — **código duplicado** con la única diferencia real siendo el tipo de bucle y el damping.
2. `initConditionsAnalysisCE` — configura incrementos de carga, solo ~20 líneas.

### Flujo Propuesto (Desacoplado)

```
controller_MenuExecute.py
│
└─ analysis_mpm.run()         ← UN SOLO MÉTODO
    ├─ initConditions()        ← Lee tipo de análisis de la config
    ├─ initBoundary()          ← Sin cambios
    ├─ initMaterialPoint()     ← Sin cambios
    ├─ initProperties()        ← Sin cambios
    ├─ initVectorAndMatrix()   ← Sin cambios
    ├─ initBoundaryParticles() ← Sin cambios
    ├─ execute()               ← UN SOLO MÉTODO parametrizado
    │   ├─ if cuasi_estatico: bucle while con convergencia
    │   └─ else:              bucle for en el tiempo
    └─ saveResults()           ← Sin cambios
```

---

## Fases de Implementación

### FASE 1: Definir el Diccionario de Configuración de Análisis
**Riesgo: Bajo | Impacto: Alto | Esfuerzo: Pequeño**

> [!NOTE]
> Esta fase NO modifica código existente. Solo agrega una nueva estructura de datos.

#### 1.1 Crear estructura `AnalysisConfig`
- **Archivo**: `app/models/model_analysis_config.py` [NUEVO]
- **Qué hace**: Define un dataclass o diccionario que empaqueta toda la configuración del análisis.

```python
class AnalysisConfig:
    # Tipo de análisis
    analysis_type: str           # "dynamic" | "quasi_static" | "mixed"
    
    # Parámetros temporales (para dinámico)
    total_time: float            # Tiempo total de simulación (s)
    courant_number: float        # Número de Courant para dt
    fps: int                     # Frames por segundo para gráficos
    
    # Parámetros cuasi-estáticos
    damping_factor: float        # Factor de amortiguamiento (0.0 - 0.80)
    convergence_tol_ff: float    # Tolerancia desbalance de fuerzas
    convergence_tol_ee: float    # Tolerancia energía cinética
    max_iterations: int          # Máximo de iteraciones cuasi-estáticas
    
    # Parámetros de carga
    load_mode: str               # "instant_gravity" | "gravity_ramp" | "load_increments"
    gravity: float               # Aceleración de gravedad (m/s²)
    n_increments: int            # Número de incrementos (si aplica)
    load_increment_value: float  # Valor de cada incremento (kN/m)
    gravity_ramp_steps: int      # Pasos de la rampa de gravedad
    
    # Integración numérica
    use_gauss_integration: bool  # True = particles_to_nodes_gauss2
    plasticity_flag: int         # 0 o 1 para nodes_to_particle_stress
```

#### 1.2 Conectar a la UI existente
- **Archivo**: `app/controllers/draw/controller_MenuExecute.py` [MODIFICAR]
- **Qué hace**: En vez de decidir `runViga` vs `runAnalysisCE`, construye un `AnalysisConfig` y lo pasa a un nuevo `run(config)`.

---

### FASE 2: Unificar el Bucle de Ejecución
**Riesgo: Medio | Impacto: Alto | Esfuerzo: Medio**

#### 2.1 Crear método `execute(config)` genérico
- **Archivo**: `app/models/model_execute_analysis.py` [MODIFICAR]
- **Qué hace**: Reemplaza `executeAnalysisViga` y `executeAnalysisCE` por un solo `execute()`.
- **Lógica interna**:

```python
def execute(self):
    config = self.config  # AnalysisConfig
    
    if config.load_mode == "load_increments":
        # BUCLE EXTERNO: Incrementos de carga
        for i in range(config.n_increments):
            tp = (i+1) * config.load_increment_value * tp0
            self._run_quasi_static_loop(config, tp)
            self._save_step_results(i)
    
    elif config.load_mode == "gravity_ramp":
        # BUCLE EXTERNO: Rampa de gravedad
        grav_steps = np.linspace(0.01, 1, config.gravity_ramp_steps)
        for j, g in enumerate(grav_steps):
            bp[:,1] = config.gravity * g
            self._run_quasi_static_loop(config)
    
    elif config.analysis_type == "dynamic":
        # BUCLE TEMPORAL SIMPLE
        self._run_dynamic_loop(config)
    
    elif config.analysis_type == "mixed":
        # ETAPA 1: Geoestático
        self._run_quasi_static_loop(config)
        # ETAPA 2: Dinámico  
        config.damping_factor = config.dynamic_damping
        self._run_dynamic_loop(config)
```

#### 2.2 Extraer sub-funciones del bucle
- **`_run_one_mpm_step()`**: El código que es idéntico en ambos execute (particles_to_nodes → BC → nodes_to_particle). Es el "corazón" del MPM que no cambia NUNCA. ~30 líneas.
- **`_run_dynamic_loop(config)`**: Bucle `for t` que llama a `_run_one_mpm_step()`.
- **`_run_quasi_static_loop(config)`**: Bucle `while` que llama a `_run_one_mpm_step()` + `static_convergence()`.

#### 2.3 Eliminar métodos obsoletos
- Eliminar `executeAnalysisViga()`, `executeAnalysisCE()`, `executeAnalysisDisc()`.
- Eliminar `runViga()`, `runAnalysisCE()`, `runAnalysisDisc()`.
- Reemplazar por un único `run()`.

---

### FASE 3: Generalizar la Configuración en la UI
**Riesgo: Bajo | Impacto: Medio | Esfuerzo: Medio**

#### 3.1 Modificar el diálogo de ejecución
- **Archivo**: `app/views/draw/` [diálogo de ejecución existente]
- **Qué hace**: En vez de tener un combo "Viga / Capacidad Portante", ofrecer campos para configurar:
  - Tipo de análisis: Dinámico / Cuasi-estático
  - Modo de carga: Gravedad instantánea / Rampa / Incrementos
  - Factor de amortiguamiento
  - Parámetros de convergencia

#### 3.2 Mover lógica del controlador
- **Archivo**: `app/controllers/draw/controller_MenuExecute.py` [MODIFICAR]
- **Qué hace**: Simplificar de `if/else` a una sola construcción de `AnalysisConfig` + llamada a `run()`.

---

### FASE 4: Soporte para Etapas (Stages)
**Riesgo: Medio | Impacto: Alto | Esfuerzo: Medio-Alto**

> [!IMPORTANT]
> Esta fase habilita los casos de uso 3.3 (Colapso), 3.5-3.7 (Pilote, Dado, MSE). Sin esta fase, solo funcionan análisis de una sola etapa.

#### 4.1 Definir estructura de Etapas
- **Archivo**: `app/models/model_analysis_config.py` [MODIFICAR]
- **Qué hace**: `AnalysisConfig` ahora tiene una lista de `stages`:

```python
class Stage:
    stage_type: str           # "geostatic" | "dynamic" | "load_increment"
    damping_factor: float
    load_settings: dict       # Configuración específica de esta etapa
    boundary_changes: dict    # Cambios en condiciones de contorno (ej: liberar nodos)

class AnalysisConfig:
    stages: list[Stage]       # Lista ordenada de etapas
    # ... resto de config global
```

#### 4.2 Ejecutar etapas secuencialmente
- **Archivo**: `app/models/model_execute_analysis.py` [MODIFICAR]
- **Qué hace**: El método `execute()` itera sobre las etapas:

```python
def execute(self):
    for stage in self.config.stages:
        self._apply_stage_boundary_changes(stage)
        if stage.stage_type == "geostatic":
            self._run_quasi_static_loop(stage)
        elif stage.stage_type == "dynamic":
            self._run_dynamic_loop(stage)
        elif stage.stage_type == "load_increment":
            self._run_load_increment_loop(stage)
```

#### 4.3 UI para definir etapas
- **Archivo**: `app/views/draw/` [diálogo nuevo o modificado]
- **Qué hace**: Permite al usuario agregar/quitar etapas y configurar cada una.

---

### FASE 5: Validación y Testing
**Riesgo: Bajo | Impacto: Crítico**

#### 5.1 Validar caso Viga (dinámico)
- Cargar "Ejemplo viga.mpm" → Ejecutar → Comparar resultados visuales con la versión anterior.
- Verificar que la barra de progreso funciona correctamente.
- Comparar arrays de esfuerzos/deformaciones numéricamente.

#### 5.2 Validar caso Capacidad Portante (cuasi-estático)
- Cargar "Ejemplo capacidad portante.mpm" → Ejecutar → Comparar curva Carga vs Desplazamiento.

#### 5.3 Validar caso nuevo (etapas)
- Crear un ejemplo de Colapso → Ejecutar con 2 etapas → Verificar que el geoestático converge y el dinámico corre correctamente.

---

## Orden de Ejecución Recomendado

```
FASE 1 (Config)  ──► FASE 2 (Unificar bucle)  ──► FASE 5.1 y 5.2 (Validar)
                                                         │
                                                         ▼
                     FASE 3 (UI generalizada)  ──► FASE 4 (Etapas)  ──► FASE 5.3 (Validar)
```

**Explicación**: Las Fases 1 y 2 son las más críticas y deben hacerse primero. Después de validar que los casos existentes siguen funcionando (Fase 5.1/5.2), recién avanzamos a la UI generalizada (Fase 3) y las etapas (Fase 4).

---

## Archivos Afectados

| Archivo | Acción | Fase |
|---------|--------|------|
| `app/models/model_analysis_config.py` | NUEVO | 1, 4 |
| `app/models/model_execute_analysis.py` | MODIFICAR (principal) | 2, 4 |
| `app/controllers/draw/controller_MenuExecute.py` | MODIFICAR | 1, 3 |
| `app/views/draw/` (diálogo de ejecución) | MODIFICAR | 3, 4 |

> [!WARNING]
> **Riesgo principal**: La Fase 2 toca el corazón del motor. Se recomienda trabajar en una rama de Git y mantener los métodos viejos comentados hasta validar completamente con la Fase 5.

---

## Estimación de Esfuerzo

| Fase | Descripción | Archivos | Complejidad |
|------|-------------|----------|-------------|
| 1 | Diccionario de configuración | 1 nuevo + 1 modificado | ⭐ Baja |
| 2 | Unificar bucle de ejecución | 1 modificado (grande) | ⭐⭐⭐ Alta |
| 3 | Generalizar UI | 2 modificados | ⭐⭐ Media |
| 4 | Soporte para etapas | 2 modificados | ⭐⭐⭐ Alta |
| 5 | Validación | 0 modificados | ⭐⭐ Media |
