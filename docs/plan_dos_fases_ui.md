# Plan escenario B: etapa de consolidación (doble fase) en la aplicación

Fecha: 30 de septiembre de 2026. Antecedente: escenario A cerrado, el MPM de doble
fase reproduce Terzaghi a nivel de script
([evaluación §9](Importantes_para_tesis/evaluacion_motor_dos_fases.md)).

Objetivo: correr el mismo caso 1D desde la aplicación (proyecto, etapa, resultados)
y obtener el mismo resultado que el script. Nada más: alcance mínimo.

## Decisiones que acotan el trabajo

1. **Drenaje sin interfaz nueva.** Igual que en la referencia, la velocidad del
   agua se restringe en los mismos nodos que la del esqueleto: un contorno con
   restricción es impermeable en esa dirección y una superficie libre es drenante
   (p = 0 en forma débil). Un contorno con el esqueleto fijo pero permeable (base
   drenante) queda como trabajo futuro.
2. **Material: tres campos nuevos** — `POROSIDAD` (n0), `PERMEABILIDAD` (k, m/s) y
   `MODULOAGUA` (Kw, kPa). `DENSIDAD` se interpreta como densidad seca ρd, de modo
   que la masa de sólidos de cada partícula es la misma `Mp` de una fase y
   ρs = ρd / (1 − n0). La densidad del agua es fija (1000 kg/m³).
3. **Etapa nueva `consolidation`** con duración, Courant, amortiguamiento y
   `PRESIONPOROSINICIAL` (kPa, positiva en compresión, uniforme). Las fuerzas Fx/Fy
   de las partículas actúan al 100 % desde t = 0, como en la etapa dinámica.
   Restricciones (validadas antes de correr): un solo material en la etapa (la
   función SRI de la referencia usa n0, k0 y Kw escalares) y sin multicuerpo.
4. **Resultados:** campo nuevo `PRESIONPOROS` (kPa, positiva en compresión), solo
   si el análisis tiene alguna etapa de consolidación (en las demás etapas de ese
   análisis vale cero); los proyectos de una fase no cambian de tamaño. En la
   etapa de consolidación `SIGXX/SIGYY/SIGXY` son esfuerzos **efectivos**.
5. **dt** de la etapa con `deltatime_two_phases_CFL` (onda de compresión no
   drenada), igual que en el script.

## Pasos (cada uno con su verificación)

| Paso | Qué | Verificación |
|---|---|---|
| B1 | Ejecutor: tipo de etapa, estado de doble fase (wp, pp, n, k), paso acoplado, dt, handoff/checkpoint; proyecto 1D generado por script; `smoke_stages.py` acepta `consolidation` | Smoke sin interfaz: igual al script de A y a Terzaghi; los tres smokes de siempre siguen en 0.000e+00 |
| B2 | Resultados: `PRESIONPOROS` en modelo, repositorio, tabla, gráficas y animación | Proyecto 1D: la animación muestra la disipación |
| B3 | Interfaz: campos del material y tipo de etapa con su presión inicial | Armar y correr el caso desde la interfaz |
| B4 | Validación final y documentación | Resultado de la app igual al del script; evaluación §9 actualizada |

## Ejecución (30 de septiembre – 1 de octubre de 2026)

**B1 — ejecutor.** `StageType.CONSOLIDATION` y `PRESIONPOROSINICIAL` en
`model_analysis_config.py`. En `model_execute_analysis.py`: estado del agua
(`wp`, `pp`, `n_p`, `k_p`, creado al entrar a la primera etapa de consolidación),
`_run_one_mpm_step_two_phase` (mismo orden que `consolidacion_1d.py`), dt con
`deltatime_two_phases_CFL`, validación previa (`_check_consolidation`), handoff y
checkpoints con el estado del agua. La etapa usa el bucle dinámico.
`tools/experimentos/proyecto_consolidacion_1d.py` genera el proyecto
`test/6 archivos_mpm 2609/8_consolidacion_1d.json` con las partículas en el orden
del script.

- **Aplicación = script, bit a bit:** presión de poros, posiciones y esfuerzo
  efectivo con diferencia **0.0** en los 401 frames (4 s, 20 000 pasos, ~40 s).
- **Regresión:** viga, capacidad portante (geostático → carga) y talud mini
  (geostático → dinámico) contra el commit anterior: **0.000e+00** los tres, y sin
  el campo nuevo (los proyectos de una fase no cambian).

**B2 — resultados.** `PRESIONPOROS` en el modelo de resultados y el repositorio
(solo se escribe si hubo consolidación); animación ("PP→Presión de poros", escalar
como EQPLAS, con `result_key()` en `utils/general_functions.py`) y gráfica en el
tiempo ("Presión de poros"). Si los resultados no la tienen, el menú vuelve a
"Default".

**B3 — interfaz.** Material: tres campos (n0, k, Kw) en el formulario de crear y
en la tarjeta de editar (`TwoPhaseFields`, agregados por código como `MODELO`).
Diálogo de etapas: tipo "Consolidación (doble fase)" con duración y presión de
poros inicial; oculta la integración Gauss y explica cargas y drenaje.

**B4 — validación desde la interfaz (7 de octubre de 2026).** El proyecto
`8_consolidacion_1d.json` se corrió desde la aplicación (490 partículas, 122
frames). La presión de poros arranca en 10 kPa en todas las partículas y termina
por debajo de 0.001 kPa (máximo en toda la corrida 10.02 kPa, oscilación del
arranque). Punto 305 (y = 0.62 m, a 0.38 m de la superficie drenante) contra
Terzaghi:

| t (s) | Tv | App (kPa) | Terzaghi (kPa) | Diferencia |
|---|---|---|---|---|
| 0.07 | 0.07 | 6.77 | 6.97 | −0.19 |
| 0.10 | 0.10 | 5.84 | 5.99 | −0.15 |
| 0.27 | 0.27 | 3.48 | 3.67 | −0.19 |
| 0.50 | 0.51 | 1.98 | 2.04 | −0.06 |
| 1.00 | 1.02 | 0.59 | 0.58 | +0.01 |
| 2.00 | 2.03 | 0.05 | 0.05 | 0.00 |
| 4.00 | 4.08 | 0.00 | 0.00 | 0.00 |

Error máximo 1.9 % de p0 al inicio, que desaparece desde Tv ≈ 1; dentro de lo
medido en el escenario A (evaluación §9). La animación "PP→Presión de poros" y la
gráfica en el tiempo funcionan. **Escenario B cerrado.**

**Encontrado de paso (para la fase de pulir la aplicación):** la tabla de
resultados (`view_PageResult.updateViewTableResult`), el exportador de
`controller_MenuResultTable` y parte de la gráfica leen claves que no existen en
`RESULTADOSNODOS` (`EPSXX`, `VELX`, `DESPL`; las guardadas son `EPSEXX`, `VELXX`,
`DESPLXY`...). Es anterior a este trabajo.
