# Plan pre-validación: cerrar el sistema de etapas antes de correr modelos largos

> **Estado:** en ejecución. **Fecha de acuerdo:** 2026-09-08.
> Cada validación larga cuesta horas o días de cómputo: todo lo listado aquí se
> hace y se verifica con smoke tests de segundos **antes** de la primera corrida larga.

## Contexto

La rama `feature/generalize-ui-engine-connection` ya tiene implementado el sistema de
etapas (Fase A): `AnalysisStage` por-etapa, `DialogStages`, persistencia `ETAPAS`,
handoff `_capture_state`/`_inject_state` y dt por etapa. La revisión del 2026-09-08
encontró huecos que, si se validan primero y se corrigen después, obligan a repetir
corridas de horas/días. Este plan cierra esos huecos **antes** de la primera validación
larga y agrega dos herramientas que abaratan cada validación posterior:
**checkpoints por etapa** (correr el geostático una vez, iterar la falla en minutos) y un
**script de comparación numérica** contra los resultados legacy ya guardados en los
`.json` de `test/`.

Decisiones tomadas (2026-09-08):
1. Resultados multi-etapa → **concatenar** todas las etapas con índice de fronteras.
2. Checkpoints por etapa (.npz + reanudar) → **incluir ahora**.
3. Legacy → **borrar controlador ahora**, modelo después de validar.
4. Motor → **alinear con referencia**: `nodes_to_particle_stress2` en rama sin gauss y
   `vp = 0` al pasar de etapa cuasi-estática a dinámica.

Hechos verificados que condicionan el plan:
- La validación de capacidad portante (`Ca_portante2.py`, proyecto `3_capacidad_portante`)
  tiene **gravedad 0** (`CONFIGURACION.GRAVEDAD = 0.0`; en el script `bp[:,1]` está
  comentado). Por tanto la pérdida de la rampa de gravedad (`DELTAINCREMENTO_GRAV = 0`)
  **no afecta esa validación**. Flujo canónico para problemas con peso: etapa geostática +
  etapa de carga. `gravity_increment_value` se elimina junto con `dincre` en el plan de
  cargas (post-validación), no ahora.
- Referencia talud (`talud_2021_v2.py`): geostático = rampa de gravedad 10 pasos, Courant
  0.6, damping 0.75, gauss2 + `nodes_to_particle_stress_gauss(..., 0)`; colapso = Courant
  0.1, damping **0.10** (`alpha`), `particles_to_nodes` + `nodes_to_particle_stress2`,
  `vp = 0` al arrancar, `tie = 8.0 s`, **mismas** condiciones de contorno en ambas fases
  (`contour_fixe(...,0,0,0,1)` en líneas 36, 438 y 570 — el comentario "Retirar condición"
  es obsoleto). La referencia es de dos cuerpos con contacto (Fase B): la app mono-cuerpo
  solo puede validar cualitativamente hasta Fase B.
- `nodes_to_particle_stress2` difiere de `nodes_to_particle_stress` **solo** en la rama
  plástica (siempre 10 sub-incrementos vs. un intento + fallback). Rama elástica idéntica →
  la viga no cambia. `nodes_to_particle_stress_gauss` ya sub-incrementa (`deps/10`) → la
  rama gauss (CE, geostático) ya coincide con la referencia.
- `BC_Dirichlet_momentum3`/`static_convergence2` del script de referencia no requieren
  cambio (momentum3 solo omite anular `niforce/neforce`, irrelevante en dinámico;
  convergence2 es una variante con historial que la referencia importa pero no usa).
- `analysisViga` y `analysisCapacidadPoratnte` en el controlador (~1100 líneas) **no tenían
  ningún llamador**. `initStateStressGeo` solo se alcanza desde `runAnalysisDisc`, que tiene
  un `return` inalcanzable en su 2ª línea.
- Modelos pequeños existentes para smoke tests: `test/4  archivos_mpm 2502/3_capacidad_portante (reducido).json`
  (9 partículas, 9 KB), `7_talud_elastoplastico (reducido) 1-1_mini.json`, `1_validacion_viga (prueba).json`.
  Los `.json` grandes ya contienen `RESULTADOS.RESULT_NODES` de corridas legacy validadas →
  sirven como oráculo numérico sin volver a correr nada.

---

## PASO 0 — Respaldo

- Commit `4a815a0` "wip: sistema de etapas antes de cierre pre-validación". ✔

---

## PASO 1 — Limpieza sin cambio de comportamiento

Objetivo: una sola fuente de verdad (ETAPAS) y archivos legibles antes de tocar el motor.
Smoke al final: la app abre, `1_validacion_viga (prueba)` corre con 1 etapa dinámica de
0.01 s.

### 1.1 Ruta nueva del ejecutor — `app/models/model_execute_analysis.py`
- `run()`: quitar el bloque `initConditionsFromConfig` y `build_default_stages()`.
- `_run_quasi_static_increment_loop`: quitar `charge` (calculado, nunca usado).
- `_prepare_stage_time`: `RuntimeError` claro si `dt is None`.
- Mantener por ahora los métodos legacy del modelo y los campos `__dincre/__charge/...`
  del ctor (los usan los legacy). Se van en PASO 6.

### 1.2 Modelo de configuración — `app/models/model_analysis_config.py`
- Eliminar: `LoadMode`, `load_mode`, `use_gauss_integration`, `plasticity_flag` global,
  `build_default_stages`, `from_legacy_viga`, `from_legacy_ce`, `time_steps`, `dt_override`.
- Agregar `AnalysisConfig.resume_from_stage: int = 0` (PASO 4).
- Actualizar `CLAUDE.md`.

### 1.3 Controlador — `app/controllers/draw/controller_MenuExecute.py`
- Borrar `analysisViga` y `analysisCapacidadPoratnte` (sin llamadores).
- Borrar slots `changeStateAnalysisCE`, `updateDincre`, `updateNoIncre`, `updateTime` y sus
  `connect`. `configDrawMenuExecute` deja solo listas de PM/contornos y `setFps`.

### 1.4 Vista y `.ui` — `view_WidgetDrawMenuExecute.py`, `widget_draw_menu_execute.ui`
- Quitar del `.ui` el panel CE (`frame_ExecuteSubTitle3`, `frame_Execute3`) y, del panel
  de tiempo, Courant, tiempo de análisis y el `groupBox` de dt/pasos. **Conservar** FPS,
  las listas de PM/contornos, `toolButton_ExecuteStages` y `toolButton_Execute`.
- Regenerar `ui_widget_draw_menu_execute.py` con `pyside6-uic`.
- En la vista: quitar las señales y getters/setters de dincre, noIncre, courant, tiempo,
  `resetDataTime`, `setResultRTimes`.

---

## PASO 2 — Motor alineado con la referencia y handoff robusto

Archivo: `app/models/model_execute_analysis.py`. Smoke: talud mini con geostático (2
incrementos) + dinámico (0.01 s) termina sin excepción y la consola muestra `[HANDOFF] vp=0`.

- `_run_one_mpm_step`, rama sin gauss: `nodes_to_particle_stress2` (referencia
  `talud_2021_v2.py` l. 689-693; rama elástica idéntica a `nodes_to_particle_stress`).
- Nuevo `_handoff(prev_stage, stage)`: `_inject_state` → `initBoundaryParticles()` → si
  la etapa es dinámica y la anterior cuasi-estática, `vp[:] = 0`.
- `_run_dynamic_loop`: al inicio `bp[:] = bp0` (gravedad completa explícita).
- Mensajes de progreso con `Etapa i/n — nombre`.
- `_capture_state`/`_inject_state` incluyen `bp` (necesario para checkpoints).

---

## PASO 3 — Resultados concatenados + metadatos de etapas + guardado parcial

Smoke: `3_capacidad_portante (reducido)` con geostático (2) + carga (2) produce 5 frames
(1 + 2 + 2); cancelar a mitad de la etapa 2 deja resultados de la etapa 1 visibles.

### 3.1 Acumular por etapa
- `_append_stage_results(stage, arrays, list_time, list_time_graphic)` acumula en
  `self.__rs_stages`. `_finalize_results()` concatena antes de `saveResults()`:
  - descarta el frame 0 de la 2ª etapa ejecutada en adelante (duplica el último de la
    anterior); lo conserva en la 1ª ejecutada (en una corrida reanudada es el checkpoint);
  - eje de tiempo global monótono: `t_global = offset + t_local`;
  - desplazamientos **por etapa** (se reinician tras el geostático — convención geotécnica);
  - `ETAPAS_FRAMES = [{"ETAPA", "TIPO", "NOMBRE", "FRAME_INICIO", "FRAME_FIN", "DT"}]`.

### 3.2 Metadatos
- `ModelResult.updateResultDataBase(gravity, dampfac, stages, stages_frames)` →
  `RESULTADOS.DATOSBASE.ETAPAS` y `ETAPAS_FRAMES`. `dampfac` = el de la primera etapa.
- `updateResultDataTimes` sigue recibiendo la semilla (etapa 1); `time_reached` global.

### 3.3 Guardado parcial al cancelar
- Los loops truncan y `_append_stage_results` antes de `return False`; `run()` guarda lo
  acumulado y marca `cancelled_partial`; el controlador avisa
  "Análisis cancelado: se guardaron los resultados parciales".

---

## PASO 4 — Checkpoints por etapa (guardar y reanudar)

Smoke: CE reducido 2 etapas → aparece `..._checkpoints/etapa_1.npz`; "Reanudar desde:
Etapa 2" → la corrida salta la etapa 1, arranca con `sig ≠ 0` y produce 3 frames.

### 4.1 Guardar
- Ruta: `<proyecto sin extensión>_checkpoints/etapa_{N}.npz` (N 1-based). `*_checkpoints/`
  en `.gitignore`.
- Tras cada etapa OK: `np.savez_compressed(path, **state, nmp, ele_size, stage_index,
  stage_json, fecha)`. Mismo espíritu que `talud_2021_v2.py` l. 372-385.

### 4.2 Reanudar
- Persistencia `CONFIGANALISIS["REANUDAR_DESDE"]` (int, 0 = desde el inicio).
- `DialogStages`: combo "Reanudar desde" con "Desde el inicio" y "Etapa N (checkpoint etapa
  N-1 · fecha)" habilitado solo si el `.npz` existe; advertencia visible cuando ≠ 0.
- Ejecutor: valida `nmp` y `ele_size` del checkpoint; inyecta estado (incluye `bp`),
  `initBoundaryParticles()`, arranca el `for` en la etapa N. Diálogo de progreso muestra
  "Reanudando desde checkpoint etapa N-1 (fecha)".

---

## PASO 5 — Oráculo numérico y matriz de smoke tests

### 5.1 `tools/smoke_stages.py` — arnés sin GUI (implementado)
Corre un análisis por etapas sin abrir la interfaz y, con `--compare`, contrasta el
resultado nuevo contra el que ya está guardado dentro del `.json`. **No escribe el
proyecto a disco**, así que es seguro correrlo sobre los archivos de referencia.

```bash
python tools/smoke_stages.py "<proyecto.json>" \
    --stages "geostatic:n=10,courant=0.6,damp=0.75,plast=0,gauss=1" \
    --mp "Talud,Base" --compare --rtol 1e-9
```
Opciones: `--resume N` (reanudar desde checkpoint), `--cancel-at N` (simular cancelación),
`maxit=` dentro del spec (tope de iteraciones, solo diagnóstico).
La salida incluye un **desglose por frame**: el primer frame que difiere señala el
incremento donde las dos corridas se separaron — fue lo que permitió encontrar la
discrepancia de plasticidad del talud en minutos en vez de horas.

### 5.1b `tools/compare_ref.py` — referencia contra app (implementado)
`smoke_stages.py --compare` contrasta la app contra la propia app: detecta regresiones,
pero **no valida nada** contra el motor original. `compare_ref.py` cierra ese hueco:
compara el `.npz` que dejan los scripts de referencia
(`1 Referencia/Codigo MPM-UN Original_V1/resultados_referencia/`, escritos por `ref_io.py`)
contra `RESULTADOS.RESULTADOSNODOS` de un proyecto ya corrido.

```bash
python tools/compare_ref.py "<...>/resultados_referencia/beam.npz" \
    "test/5 archivos_mpm 2607/1_validacion_viga.json" \
    --material "Material  Beam" --frames-comunes --rtol 1e-9
```

Alinea las dos corridas sin suponer nada sobre el orden interno de cada lado:
* **partículas** por su posición inicial (de paso comprueba que los dos discretizaron
  el mismo dominio);
* **frames** por el valor del eje (tiempo, carga o fracción de gravedad). Si los ejes no
  calzan — típicamente porque el FPS del proyecto no es el del script — lo dice, y con
  `--frames-comunes` compara solo los que coinciden.

La tolerancia al emparejar frames está topeada en 5.1e-4 (la app redondea
`TIEMPOSGRAFICAR` a 3 decimales): con medio paso se emparejarían frames separados por un
`dt` del solver, que son estados distintos.

### 5.2 Qué archivos sirven de oráculo (verificado leyendo los .json)
Cada resultado guarda **qué grupos de puntos materiales se usaron**, así que se puede
comprobar si es reproducible. Sirven:

| Caso | Archivo | Grupos | Frames |
|---|---|---|---|
| Viga | `test/5 archivos_mpm 2607/1_validacion_viga.json` | **MP-Beam_2** (304), *no* MP-beam | 123 |
| Cap. portante | `test/4 .../3_capacidad_portante (medio).json` | **MP-Suelo** (800) | 57 |
| Talud geostático | `test/4 .../5_talud_elastoplastico (reducido).json` | Base + Talud (1308) | 11 |
| Talud geostático grande | `test/4 .../8_talud_elastoplastico full.json` | Base + Talud (6559) | 11 |

No sirven: `test/5/2_capacidad_portante.json` (cortada en el incremento 54 de 56),
`test/4/1_validacion_viga (prueba).json` (cortada en t=0.254 de 1.0),
`test/4/7_..._mini.json` (resultados de grupos que ya no existen).

> **`7_..._mini` no es un modelo válido**: tiene 221 partículas en 221 celdas, o sea
> **1 partícula por celda**, el caso degenerado del MPM. La integración gaussiana no
> tiene con qué reconstruir el esfuerzo y el residuo se clava en `ff ≈ 0.11` sin importar
> incrementos, plasticidad ni variante de `boundary_particles`. Sirve para "¿corre?",
> nunca para nada numérico. El modelo bueno es `5_talud (reducido)`: 2.43 partículas
> por celda.

### 5.3 Checklist de parámetros (verificado contra el contenido de los oráculos)

| Modelo | Etapa | Tipo | Courant | Damping | Plast. | Gauss | Otros |
|---|---|---|---|---|---|---|---|
| Viga | 1 | dynamic | 0.5 | 0.0 | 0 | No | t=4.0, fps=30 |
| Cap. portante | 1 | load_increment | 0.5 | 0.75 | **1** | Sí | n=56, dincre=−2.0, **gravedad 0** |
| Talud | 1 | geostatic | 0.6 | 0.75 | **0** | Sí | n=10, tol 0.01 |
| Talud | 2 | dynamic | 0.1 | **0.10** (no el default 0.05) | 1 | No | 8.0 s |

> **La plasticidad del geostático es 0, no 1.** Se comprobó leyendo los oráculos:
> `5_talud` y `8_talud` tienen `EPSP` exactamente cero en las 14.388 / 72.149 entradas
> → se corrieron elásticos. Coincide con `talud_2021_v2.py`, que usa
> `nodes_to_particle_stress_gauss(..., 0)` en el geostático, y con el default del
> diálogo. Con `plast=1` el talud plastifica en el incremento 2 y el residuo se dispara
> a 0.34 sin converger nunca.
>
> **Ojo con la tolerancia en capacidad portante.** El legacy `executeAnalysisCE` la tiene
> hardcodeada en **`ff > 0.011`**, mientras la ruta nueva y el script de referencia usan
> `0.01`. El oráculo del talud salió por la ruta nueva (0.01, ya verificado); el de
> capacidad portante lo produjo `executeAnalysisCE`, así que si no reproduce con 0.01,
> probar 0.011.
>
> `ff` es un **cociente normalizado** (`‖neforce+niforce‖/‖neforce‖`): subir el número de
> incrementos **no** ayuda a que converja, solo cambia la trayectoria plástica.

### 5.4 Estado de la validación — refactor verificado

| Caso | Rama del motor ejercitada | Frames | Tiempo | Resultado |
|---|---|---|---|---|
| Viga | dinámica, sin gauss, elástica (`stress2`) | 123 | 6 s | **IDÉNTICO bit a bit** |
| Talud geostático (1308 pts) | cuasi-estática, gauss, elástica | 11 | 59 s | **IDÉNTICO bit a bit** |
| Capacidad portante (medio) | cuasi-estática, gauss, **plástica** | 57 | 369 s | **IDÉNTICO bit a bit** (con `tolff=0.011`) |
| S3: CE reducido 2 etapas | handoff + concatenación + checkpoints | 5 | 2 s | ✔ |
| S5: talud mini 2 etapas | handoff `vp=0`, dt por etapa | 3 | 172 s | ✔ corre (modelo degenerado, no converge) |

`0.0000e+00` en los 18 campos de los tres oráculos. **Los PASOS 1–4 no cambiaron ningún
número**: ni el cambio a `nodes_to_particle_stress2`, ni la concatenación de resultados,
ni el handoff, ni los checkpoints.

Pendiente: talud de 2 etapas (falla) reanudando desde el checkpoint del geostático —
sin oráculo, evaluación cualitativa, y limitado a un cuerpo hasta la Fase B.

### 5.5 Decisión abierta: la tolerancia de capacidad portante

El oráculo de capacidad portante solo reproduce con **`tolff = 0.011`**, el valor
hardcodeado en el legacy `executeAnalysisCE`. Con `0.01` (el valor del script de
referencia `Ca_portante2.py` y el default del diálogo) la corrida **también completa los
56 incrementos**, pero da otro resultado:

| Campo | Diferencia absoluta | Relativa |
|---|---|---|
| SIGYY | 20.8 kPa | 14 % |
| SIGXX | 17.6 kPa | 17 % |
| DESPLYY | 0.033 m | 7.6 % |
| EQPLAS | 0.014 | 8.6 % |

La divergencia arranca en el frame 1 y **crece monótonamente** hasta el 56: es acumulación
en un problema dependiente de la trayectoria, no un error de código.

> **Esto es un hallazgo sobre el modelo, no sobre el refactor.** Que mover la tolerancia
> de 0.010 a 0.011 (un 10 %) cambie los esfuerzos un ~15 % significa que la solución no
> está convergida en el sentido útil de la palabra. Antes de usar ese caso como validación
> en la tesis conviene un estudio de sensibilidad (0.011 / 0.01 / 0.005 / 0.001) y ver si
> la respuesta se estabiliza. Cada corrida cuesta ~6 min con `tools/smoke_stages.py`.

Decisión a tomar: adoptar `0.01` (coherente con la referencia y con el resto de la app) y
**re-establecer la línea base** de ese caso documentando el cambio, o conservar `0.011`
por compatibilidad con el resultado histórico.

---

## PASO 6 — Post-validación (no ejecutar antes de que 5.3 pase)

- Borrar legacy del modelo: `runViga`, `runAnalysisCE`, `runAnalysisDisc`,
  `initConditionsAnalysisCE`, `initStateStressGeo`, `executeAnalysisDisc`,
  `executeAnalysisCE`, `executeAnalysisViga`, `save_results_excel`, campos
  `__dincre/__dincreGrav/__nincre/__charge/__chargeGrav`, fallback `if config is None` en
  `run()`, imports no usados (`ezdxf`, `deltatime2`, `graphic_*`).
- Borrar `ANALISISCUASIESTATICO` y sus getters/setters; quitar `DAMPFAC` del menú Data (o
  relabel "sin efecto").
- Ejecutar `docs/plan_simplificacion_cargas.md` **agregando** a su PASO 2 la eliminación de
  `gravity_increment_value` / `DELTAINCREMENTO_GRAV` y anotando en §5.1 que la equivalencia
  CE no depende de la rampa de gravedad (gravedad 0).

---

## Verificación end-to-end

1. Tras PASO 1: S1. Tras PASO 2: S5. Tras PASO 3: S3 y S6. Tras PASO 4: S4.
2. `python tools/compare_results.py "test/6 referencia/1_validacion_viga.json" <nuevo>.json`
   → 0 diferencias (rama elástica intacta).
3. Validaciones largas en el orden de 5.3, cada una precedida por su smoke con parámetros
   reducidos en el mismo proyecto.
4. Commit por paso (tras cada smoke verde), para aislar regresiones sin repetir corridas.
