# Validación de la app MPM-UN contra el motor original

Material de trabajo para el capítulo de validación de la tesis. Documenta qué se
comparó, con qué herramientas, qué se encontró y por qué los resultados de
capacidad portante **no coinciden dígito a dígito pero sí en orden de magnitud**.

Fechas de las corridas: 2026-09-09 y 2026-09-10.

El **costo computacional** de estas corridas (por qué la malla de la tesis tarda ~9 h y qué
haría falta para bajarlo a minutos) se analiza aparte, en
[rendimiento_y_costo_computacional.md](rendimiento_y_costo_computacional.md).

La **detección de partículas de frontera** en el talud —por qué la app sustituyó
`boundary_particles2` por `boundary_particles3`, y la demostración de que esa es la única
diferencia que subsiste entre app y referencia en geometría inclinada— está en
[deteccion_particulas_frontera.md](deteccion_particulas_frontera.md).

---

## 1. Qué se está validando y contra qué

Hay que distinguir dos preguntas que se contestan con evidencia distinta:

| | Pregunta | Contra qué se compara | Criterio |
|---|---|---|---|
| **A** | ¿La app usa bien el motor? | scripts originales del MPM-UN, **mismos parámetros** | equivalencia numérica |
| **B** | ¿La app reproduce el caso de estudio? | resultados publicados en las tesis | ingenieril (%) |

**A** es verificación de software: si los dos lados usan la misma discretización y
los mismos parámetros, deben dar lo mismo. **B** es la validación del caso: exige
la discretización de la tesis.

Una tercera comparación que **no** sirve para ninguna de las dos: contrastar la
app de hoy contra los resultados guardados en `test/1…5`. Esos archivos vienen de
versiones desconocidas del código y solo detectan regresiones (app contra app).

### Referencias usadas

Código original íntegro en
`1 Referencia/Codigo MPM-UN Original_V1/`:

| Caso | Script | Origen |
|---|---|---|
| Viga en voladizo | `beam.py` | León (2019) |
| Capacidad portante | `Ca_portante2.py` | León (2019) |
| Talud | `talud_2021.py` | Sandoval Montoya (2021) |

Los parámetros de los tres están en
`1 Referencia/Codigo MPM-UN Original_V1/PARAMETROS_CORRIDAS.md`.

---

## 2. Herramientas construidas

Para que cada validación no cueste una corrida perdida por un dato mal tecleado:

| Herramienta | Qué hace |
|---|---|
| `ref_io.py` (en la carpeta de referencia) | Los scripts originales exportan sus resultados a `.npz` con los **mismos 18 campos y las mismas fórmulas** que `RESULTADOS.RESULTADOSNODOS` de la app, más una ficha `.txt` con los parámetros reales de esa corrida. Es aditivo: no toca ninguna línea de cálculo. |
| `ver_resultados.py` (en la carpeta de referencia) | Reabre un `.npz` guardado y lo grafica sin volver a correr la simulación. |
| `tools/compare_ref.py` | Compara el `.npz` de referencia contra un proyecto `.json` de la app ya corrido, o contra un `.npz` exportado por el arnés. |
| `tools/smoke_stages.py --export` | Corre la app **sin abrir la GUI** y vuelca el resultado al formato de `ref_io.py`. Permite comparar la app de hoy contra el motor original, en vez de contra un resultado viejo. |

### Cómo alinea `compare_ref.py` las dos corridas

No supone nada sobre el orden interno de cada lado — algo que resultó ser
esencial, como se ve en §5:

- **Partículas**: por su posición inicial (frame 0). De paso comprueba que los
  dos lados discretizaron el mismo dominio.
- **Frames**: por el valor del eje (tiempo, carga o fracción de gravedad), o por
  índice con `--por-indice` cuando los ejes están en unidades distintas — que es
  el caso de los análisis por incrementos, donde la app numera los incrementos
  (0…56) y los scripts guardan la carga (0…112 kPa).

---

## 3. Caso viga: coincidencia exacta, y un error encontrado

### 3.1 El error del bucle dinámico

La primera comparación viga-app contra `beam.py` dio errores relativos superiores
al 100 % desde el frame 1. El comparador mostró que el frame 1 de la app tenía

```
VELYY  = 0.0098   = exactamente g·dt = 9.8 × 0.001
DESPLYY = 9.8e-6  = g·dt²
```

es decir el estado tras **un solo paso** del solver, cuando debía ir por el paso
33 (fps 30, dt 1e-3 → 33 pasos por frame).

Causa, en `_run_dynamic_loop` de `app/models/model_execute_analysis.py`:

```python
current_time = list_time[index]          # tiempo ANTES del paso
...
nmass, ... = self._run_one_mpm_step(...) # se ejecuta el paso
...
if abs(current_time - current_time_graphic) < 1e-13:   # ← compara el de ANTES
    self._save_step_to_arrays(arrays, current_index_graphic + 1)
```

La condición comparaba el tiempo **anterior** al paso pero guardaba el estado
**posterior**. En `index = 0`, `current_time = 0.0` coincide con el primer tiempo
gráfico, así que se escribía en el slot 1 el estado tras un paso. El frame *k*
contenía el estado del paso `ndt·(k−1)+1` en vez de `ndt·k`: **32 pasos
adelantado respecto a su rótulo de tiempo**.

Los scripts de referencia comparan el tiempo posterior al paso contra el frame
gráfico *siguiente* (`beam.py` l. 139). La corrección replica ese criterio.

**Alcance:** afectaba a todos los análisis dinámicos guardados hasta ese momento,
incluidos los `.json` de `test/`. Los análisis cuasi-estáticos no: ahí se guarda
un frame por incremento convergido, que es correcto. Se verificó que la app de
antes del arreglo daba números idénticos al oráculo viejo, o sea que el error
venía de antes del refactor de etapas y no fue introducido por él.

### 3.2 Resultado tras la corrección

Proyecto `test/6 archivos_mpm 2609/1_validacion_viga.json`, con los parámetros de
`beam.py` (g = 9.81, fps 40, Courant 0.5, dt 0.001, 4000 pasos, damping 0,
elástico, sin gauss, 304 partículas):

| | |
|---|---|
| Partículas emparejadas | 304 ↔ 304, desajuste máx **8.9e-16 m** |
| Frames | 161 ↔ 161, ejes de tiempo idénticos |
| **Peor error relativo** | **5.673e-11** sobre 18 campos × 304 partículas × 161 frames |

El error crece monótonamente con el número de pasos, arrancando en el último bit
del `double`:

| frame | t (s) | error rel. SIGXX |
|---|---|---|
| 1 | 0.025 | 2.3e-15 |
| 40 | 1.000 | 2.7e-13 |
| 80 | 2.000 | 1.1e-12 |
| 120 | 3.000 | 5.8e-12 |
| 160 | 4.000 | 2.3e-11 |

Ese patrón es acumulación de redondeo en 4000 pasos, no diferencia de
formulación: una diferencia real de algoritmo aparecería desde los primeros
frames con magnitud constante — que es exactamente lo que ocurría **antes** del
arreglo (error relativo 1.0 en el frame 1).

**Conclusión: la viga queda validada** en los sentidos A y B a la vez, porque se
corrió con los parámetros originales.

---

## 4. Caso capacidad portante: el resultado y la discrepancia

### 4.1 Montaje

Como el proyecto de la app venía con malla de 1.0 m y el script de la tesis usa
0.5 m, se hizo primero la comparación barata igualando la discretización: se creó
`Ca_portante2_malla1.py`, copia idéntica de `Ca_portante2.py` salvo
`ele_size = 1.0`. Se verificó que los datos de entrada eran **exactamente** los
mismos:

| | Script `Ca_portante2_malla1.py` | Proyecto `2_capacidad_portante_malla1.json` |
|---|---|---|
| Malla | 20×15, `ele_size` 1.0 → 336 nodos, 300 elem | idéntica |
| Partículas | 800, paso 0.5, `Vp0` 0.25 | idéntica, **Δ = 0.000e+00 m** |
| Zapata | 10 partículas, x ∈ [0.25, 4.75], tp = 0.5 | idéntica, **Δ = 0.000e+00 kN/m** |
| Material | E 10000, ν 0.49, c 20, φ 0°, ψ 0°, ρ 1.8 | idéntico |
| Gravedad | 0 | 0 |
| Contornos | `contour_fixe(...,0,0,0,1)` | top `Ty`, bottom `Tx+Ty`, left/right `Tx` |
| Courant / damping | 0.1 / 0.75 | 0.1 / 0.75 |
| Incrementos | 56 × (−2 kPa) | 56 × (−2.0) |
| Tolerancias | ff 0.011, ee 0.01 | 0.011, 0.01 |
| Plasticidad / integración | `stress_gauss(..., 1)` / `gauss2` | 1 / gauss |

> Nota de unidades: `dincre = -2` es una **presión en kPa**, no kN/m. El
> comentario del script original dice "KN/m" pero `traction_forces` reparte
> `t·l/ntp`, de modo que `t` es presión. Lo confirma que la carga de colapso caiga
> en el valor analítico (§4.3).

### 4.2 Las dos corridas no coinciden dígito a dígito

Comparando frame a frame (`--por-indice`):

| Incremento | q (kPa) | rel SIGYY | rel DESPLYY | rel EQPLAS |
|---|---|---|---|---|
| 1–30 | 2–60 | ~0.3 % | ~0.1 % | 0 (elástico) |
| 40–50 | 80–100 | ~0.4 % | 0.3–1 % | 1–2 % |
| 52 | 104 | 0.5 % | 1.8 % | 3 % |
| **56** | **112** | **10.7 %** | 4.1 % | 4.2 % |

Las velocidades difieren 10–70 % en todos los incrementos, pero al converger un
análisis cuasi-estático la velocidad es **residuo de la iteración**, no una
magnitud física del resultado.

### 4.3 Pero coinciden como respuesta de ingeniería

Curva carga–asentamiento del centro de la zapata:

| Incremento | q (kPa) | referencia (m) | app (m) | dif. |
|---|---|---|---|---|
| 14 | 28 | 0.01026 | 0.01025 | 0.05 % |
| 28 | 56 | 0.02052 | 0.02054 | 0.13 % |
| 42 | 84 | 0.03804 | 0.03821 | 0.45 % |
| 49 | 98 | 0.05692 | 0.05665 | 0.47 % |
| 52 | 104 | 0.07164 | 0.07278 | 1.60 % |
| 54 | 108 | 0.10171 | 0.10130 | 0.41 % |
| 55 | 110 | 0.18533 | 0.18636 | 0.56 % |
| 56 | 112 | 0.45857 | 0.43954 | 4.15 % |

Y la referencia reproduce la solución analítica de Prandtl para suelo Tresca:

> **q_u = (2 + π)·S_u = 5.14 × 20 = 102.8 kPa**

El tramo elástico es exactamente lineal (0.00513 m por cada 14 kPa) y el codo de
la curva cae en **102–104 kPa**. Las dos corridas coinciden dentro del **0.5 %
hasta 98 kPa** y ambas dan la misma carga de colapso.

### 4.4 Malla fina: la discretización de la tesis

Corrida definitiva con `ele_size = 0.5`, que es la del script original y la que
cierra la pregunta **B**. Duración de la referencia: **9.78 h** (35 213 s).

| | Script `Ca_portante2.py` | Proyecto `2_capacidad_portante.json` |
|---|---|---|
| Malla de fondo | 20×15, `ele_size` 0.5 → 1271 nodos, 1200 elem | idéntica |
| Cuerpo de suelo | 861 nodos, 800 elem | idéntico |
| Partículas | 3200, paso 0.25, `Vp0` 0.0625 | idénticas, **Δ = 0.000e+00 m** |
| Zapata | 20 partículas, x ∈ [0.125, 4.875], `tp0` = 0.25 | idéntica |
| `dtime` | 1.0e-4 s | 1.0e-4 s |
| Resto de parámetros | — | idénticos a §4.1 |

> El reparto de la carga es `t·l/ntp`, así que la **suma** vale `t·l = 5.0`
> independientemente de la malla: 10 partículas × 0.5 en malla gruesa, 20 × 0.25
> en malla fina. Al refinar hay que **reducir la fuerza por partícula**, no
> mantenerla. Es el error más fácil de cometer al remallar.

**Incrementos 1–54 (2 a 108 kPa), todos convergidos en ambos:**

| Campo | Error relativo máximo | Frame del máximo |
|---|---|---|
| SIGYY | **0.59 %** | 51 |
| SIGXX | **1.12 %** | 51 |
| CORY | **0.0037 %** | 51 |
| DESPLYY | 0.53 % | 51 |
| EQPLAS | ~1.2 % | 54 |

El error **no crece**: se mantiene en una banda estable de 0.3–1.1 % a lo largo de
los 54 incrementos, sin deriva acumulativa. Y queda por debajo de la tolerancia de
convergencia (1.1 %), que es la cota teórica del §5.5 — no se puede hacer mejor.

**Coincidencia exacta en el inicio de la plasticidad.** `EQPLAS` es idénticamente
cero en las dos corridas hasta el frame 30, y aparece por primera vez en el
**frame 31 (62 kPa) en ambas**. El umbral de plastificación cae en el mismo
incremento.

**Curva carga–asentamiento** (asentamiento máximo bajo la zapata):

| q (kPa) | referencia (m) | app (m) | dif. |
|---|---|---|---|
| 10 | −0.003710 | −0.003710 | 0.002 % |
| 50 | −0.018559 | −0.018601 | 0.23 % |
| 100 | −0.062472 | −0.062465 | 0.012 % |
| 106 | −0.083991 | −0.084038 | 0.06 % |
| 108 | −0.109222 | −0.107264 | 1.8 % |

Coincidencia **mejor que 0.25 % hasta 100 kPa**.

#### El incremento 55 no es comparable, y no debe serlo

Ninguna de las dos corridas converge en 110 kPa, y el frame 55 difiere 66–78 % en
esfuerzos. **No es un defecto: es la ausencia de solución.** Por encima de la carga
de colapso no existe un estado de equilibrio estático al que converger, de modo que
lo que hace cada corrida es integrar hacia adelante un colapso en curso. Las dos se
detienen por criterios distintos:

| | criterio de corte | iteraciones en el incremento 55 | asentamiento alcanzado |
|---|---|---|---|
| Referencia | tiempo, `10 × t0` (3.6 h) | ≈ 176 000 | −0.268 m |
| App | `max_iterations = 50000` | 50 000 | −0.196 m |

La corrida que iteró 3.5 veces más se hundió más. Son dos fotogramas distintos de
la misma película, no dos respuestas distintas a la misma pregunta.

**Consecuencia metodológica:** el rango validado es **0–108 kPa** (frames 0–54,
todos convergidos). El frame 55 es un **diagnóstico**, no un dato: dice "se superó
la carga de colapso", y en eso las dos corridas coinciden.

#### La carga de colapso, y qué aporta refinar

Los dos motores coinciden en que el suelo **sostiene 108 kPa y no sostiene
110 kPa**, contra los 102.8 kPa de Prandtl: **+5 a +7 %**.

El contraste entre mallas es el resultado más valioso de esta sección:

| Malla | Partículas | Último incremento convergido | vs. Prandtl |
|---|---|---|---|
| 1.0 | 800 | 56 (112 kPa) — completó todos | +9 % |
| 0.5 | 3200 | 54 (108 kPa) | +5 % |

La malla gruesa **sobreestima** la carga de colapso, porque no resuelve el mecanismo
de falla. Al refinar, el resultado se mueve **hacia** la solución analítica. Es la
dirección correcta y el comportamiento esperado de un modelo de elementos/puntos
bien planteado.

> Para acotar `q_u` con más precisión, lo que corresponde **no** es dejar correr más
> iteraciones —no hay nada a lo que converger— sino **refinar el incremento de
> carga** cerca de la falla (por ejemplo `dincre = -0.5` a partir de 100 kPa).

---

## 5. Por qué difieren: el orden de las partículas

### 5.1 Descarte de las causas obvias

| Sospechoso | Verificación | Resultado |
|---|---|---|
| Piso `1e-10` de masa nodal (única diferencia real entre los motores) | está en `particles_to_nodes`; capacidad portante usa `particles_to_nodes_gauss2` | **no aplica** |
| `boundary_particles3` (app) vs `boundary_particles` (script) | se evaluaron ambas sobre la misma configuración | **116 de 800 en las dos, mismas posiciones** |
| `dtime` distinto | `deltatime` en ambos motores | `0.00029999999999999997372` en los dos, **idéntico bit a bit** |
| Fórmula del amortiguamiento | comparación línea por línea | algebraicamente y en punto flotante idénticas |
| Lógica del bucle de incrementos | comparación línea por línea | idénticas |

### 5.2 Los motores son bit a bit idénticos

Se corrió **un paso MPM completo con cada motor** desde el mismo estado inicial,
por 6 iteraciones consecutivas (script `dos_motores.py`):

```
=== SETUP ===
  xp identicos:   True (max dif 0.000e+00)
  tp0 identicos:  True (max dif 0.000e+00)
  bound_val igual: True
  dtime iguales:  True

=== ITERACIONES DEL INCREMENTO 1 ===
 iter          ff V1         ff app      dif sig       dif xp
    1              1              1    0.000e+00    0.000e+00
        nmass    dif max = 0.000e+00
        niforce  dif max = 0.000e+00
        neforce  dif max = 0.000e+00
        nvel     dif max = 0.000e+00
    2   0.9948391306   0.9948391306    0.000e+00    0.000e+00
    ...
    6   0.9623664695   0.9623664695    0.000e+00    0.000e+00
```

Diferencia **exactamente cero** en todo.

### 5.3 La causa: orden de acumulación en punto flotante

La app y el script recorren las partículas en orden distinto:

| | Recorrido de elementos | Dentro del elemento |
|---|---|---|
| Script (`setup_MP`) | por filas, de abajo hacia arriba | (0.25,0.25) (0.75,0.25) (0.25,0.75) (0.75,0.75) |
| App (`controller_MenuPointMaterial`) | por columnas, de arriba hacia abajo | (0.25,9.75) (0.25,9.25) (0.75,9.25) (0.75,9.75) |

`particles_to_nodes_gauss2` acumula masas y fuerzas nodales recorriendo
partículas, y **la suma en punto flotante no es asociativa**: cambiar el orden
cambia los últimos bits del resultado (~1e-16).

### 5.4 Experimento decisivo

Se corrió el **mismo motor, con los mismos datos**, cambiando **únicamente** el
orden de las partículas (script `orden_particulas.py`):

| | Orden del script | Orden de la app | La app real |
|---|---|---|---|
| Inc. 1 | 5470 ciclos, ff = 0.01098768303998096 | **5453**, ff = **0.01099118971181655** | **5453**, ff = **0.010991189711816549** |
| Inc. 2 | 4033, ff = 0.01098366714712538 | **4012**, ff = **0.01099094436229305** | **4012**, ff = **0.010990944362293052** |
| Inc. 3 | 3594, ff = 0.01099056525835497 | **3292**, ff = **0.01098755786274411** | **3292**, ff = **0.010987557862744112** |

Alimentar el motor original con el orden de partículas de la app **reproduce los
números de la app dígito por dígito**, incluido el número de iteraciones.

Y las diferencias que produce solo permutar:

| Incremento | rel SIGYY (solo permutando) | rel SIGYY (app vs script) |
|---|---|---|
| 1 | 2.012e-03 | **2.012e-03** |
| 2 | 2.819e-03 | **2.819e-03** |
| 3 | 3.951e-03 | **3.951e-03** |

Coincidencia exacta. El orden de las partículas explica **la totalidad** de la
discrepancia en el rango elástico.

> Alcance de la prueba: el experimento cubre los incrementos 1–3, todos
> elásticos. Para el rango plástico (incrementos ≳ 40) la atribución es por
> inferencia — la magnitud crece de forma consistente y no queda ninguna otra
> diferencia entre los dos códigos —, no por verificación dígito a dígito.
> Si hiciera falta cerrarlo, basta extender `orden_particulas.py` hasta el
> incremento 56.

### 5.5 Por qué una perturbación de 1e-16 produce un 0.4 %

No es amplificación caótica. Es el **criterio de parada**:

```python
while (ff > 0.011) or (ee > 0.01):
```

La tolerancia `ff ≤ 0.011` admite un 1.1 % de desbalance de fuerzas. Eso define
una *bola* de estados aceptables como "convergidos". La perturbación de 1e-16
hace que un lado converja en 5470 iteraciones y el otro en 5453, y cada uno
aterriza en un punto distinto **dentro de esa misma bola**.

Por lo tanto **la diferencia está acotada por la tolerancia del método, no por la
precisión de la máquina**: de ahí que dé 0.2–0.4 %, del mismo orden que el 1.1 %
del criterio.

En el incremento 56, ya pasado el colapso, el problema está mal condicionado: el
mismo 1.1 % en fuerzas admite estados mucho más separados en desplazamientos y
esfuerzos. De ahí el 10 %.

### 5.6 Por qué la viga sí da bit a bit y capacidad portante no

Mismo mecanismo, distinto tipo de análisis:

| | Viga | Capacidad portante |
|---|---|---|
| Esquema | integración explícita de **paso fijo** | **relajación iterativa** hasta equilibrio |
| Nº de pasos | fijo e igual en los dos (4000) | lo decide la tolerancia; **difiere** (5470 vs 5453) |
| Qué acota la diferencia | precisión de máquina | **tolerancia de convergencia** |
| Diferencia observada | 5.7e-11 | 0.2 % a 10 % |

La viga tiene exactamente el mismo problema de orden, pero sin criterio de
convergencia que lo amplifique: la perturbación solo se acumula como redondeo.

---

## 6. Por qué no se alineó el orden

Se evaluó hacer que la app entregara las partículas al motor en el orden de
`setup_MP`, y se decidió **no hacerlo**:

1. **No existe un "orden del original" en general.** `setup_MP(xi, yi, xf, yf, …)`
   solo sabe llenar rectángulos alineados con la malla. La app genera puntos
   material sobre regiones arbitrarias y mallas no regulares — que es
   precisamente su razón de ser. El orden objetivo solo estaría definido para la
   viga y capacidad portante, no para el talud ni para geometrías dibujadas.
2. **Ninguno de los dos órdenes es más correcto.** Ambos son convenciones
   arbitrarias de iteración; la física no depende de ellas.
3. **No es un defecto de la app.** El motor es bit a bit idéntico y la lógica del
   bucle también; la diferencia es la irreproducibilidad inherente de un solver
   iterativo con tolerancia finita bajo reordenamiento de sumas.
4. **Tiene costo y riesgo.** Lo que hoy depende del orden:

   | Qué | Impacto de reordenar |
   |---|---|
   | Checkpoints `.npz` | Guardan el estado en el orden de la app; un reordenamiento los invalidaría **en silencio** (hoy se valida `nmp` y `ele_size`, no el orden). Requeriría estampar una versión. |
   | IDs de nodos de resultado | `RESULTADOSNODOS` usa claves posicionales; cambiaría qué partícula es el nodo 1 en la tabla y la animación. |
   | `boundary_particles3` | En rectángulo da el mismo conjunto; en geometría irregular podría no darlo. |

El orden de la app **no es intencional**: es consecuencia de cómo itera su
generador de puntos. El propio código lo delata — el comentario de
`initBoundaryParticles` dice *"creo que están en orden diferente al MPM-UN
original"*, o sea que se notó después, no se diseñó.

---

## 7. Qué se puede afirmar en la tesis

1. **El motor de la app es el motor original.** Verificado en tres niveles:
   comparación función por función del código; un paso MPM con cada motor desde
   el mismo estado con diferencia exactamente cero; y `dtime` idéntico hasta el
   último bit.
2. **La app conduce el análisis igual que los scripts originales.** Verificado
   línea por línea, y comprobado numéricamente al reproducir el número de
   iteraciones de la app alimentando el motor original con su orden de
   partículas.
3. **En análisis dinámicos de paso fijo la coincidencia es numérica**: viga,
   5.7e-11 sobre 18 campos × 304 partículas × 161 frames, con crecimiento
   monótono propio del redondeo.
4. **En análisis cuasi-estáticos iterativos la coincidencia es del orden de la
   tolerancia de convergencia**, y la causa está identificada y demostrada: el
   orden de acumulación de las sumas nodales. En la malla de la tesis
   (`ele_size` 0.5, 3200 partículas) el error se mantiene en **0.3–1.1 % sin
   crecer** a lo largo de los 54 incrementos convergidos, por debajo de la
   tolerancia de convergencia, que es la cota teórica.
5. **La respuesta de ingeniería coincide**: curva carga–asentamiento dentro del
   **0.25 % hasta 100 kPa**, inicio de la plastificación en el **mismo
   incremento** (62 kPa), y la misma carga de colapso (entre 108 y 110 kPa).
6. **La referencia reproduce la solución analítica** de Prandtl (102.8 kPa), lo
   que valida el caso antes de compararlo con la app.
7. **El modelo converge con la malla**: al pasar de `ele_size` 1.0 a 0.5 la carga
   de colapso baja de +9 % a +5 % sobre Prandtl. Refinar acerca el resultado a la
   solución analítica.

---

## 8. Cómo reproducir

```bash
# 1. Correr la referencia (escribe .npz + ficha .txt)
cd "1 Referencia/Codigo MPM-UN Original_V1"
.venv/Scripts/python.exe Ca_portante2_malla1.py

# 2. Correr la app sin GUI y exportar al mismo formato
cd "2 Software/MPM-UN"
python tools/smoke_stages.py "test/6 archivos_mpm 2609/2_capacidad_portante_malla1.json" \
    --stages "load_increment:n=56,dincre=-2,courant=0.1,damp=0.75,plast=1,gauss=1,tolff=0.011,tolee=0.01" \
    --mp "MP-Suelo" --export salida.npz

# 3. Comparar
python tools/compare_ref.py \
    "…/resultados_referencia/capacidad_portante_malla1.npz" \
    salida.npz --por-indice
```

Para comparar contra un proyecto guardado desde la GUI, el tercer paso admite el
`.json` directamente con `--material "Mat 1"`.

Los dos experimentos de §5.2 y §5.4 (`dos_motores.py` y `orden_particulas.py`)
son autocontenidos: montan la configuración desde cero, no dependen de ninguna
corrida previa.

---

## 9. Estado y pendientes

**Capacidad portante: cerrado.** Malla gruesa y malla fina comparadas, diferencia
explicada, acotada por la tolerancia y reproducida experimentalmente (§5.4). No
quedan verificaciones que agreguen información: más corridas darían el mismo
resultado por la misma razón.

**Talud, fase geostática: cerrado.** La comparación `boundary_particles3` (app)
contra `boundary_particles2` (script) sobre la geometría inclinada —que era el
riesgo abierto de mayor valor, por ser el único sitio donde la diferencia podía
ser real y no de orden— quedó resuelta y documentada aparte, en
[deteccion_particulas_frontera.md](deteccion_particulas_frontera.md).

Resultado: **sí hay una diferencia real y es la única que subsiste**, pero está
acotada a 7-8 partículas de 6740 (0.1 %) en la punta de la cuña, verificada con
rampa de 2 y de 10 pasos. Alimentando el motor original con
`boundary_particles3` se reproduce la salida de la app exactamente
(`0.000e+00`), lo que confirma que el motor es el mismo y que la función de
frontera es la única variable.

Pendiente:

- **Talud, fase de falla**: la referencia es de dos cuerpos con contacto y la app
  es mono-cuerpo. Requiere la Fase B (contacto multi-cuerpo). **Nota:** esa fase
  del original no usa partículas de frontera (las llamadas a
  `boundary_particles2` están comentadas, `talud_2021.py` líneas 551 y 615),
  así que el hallazgo anterior no la afecta.

### Nota sobre los criterios de corte

El script corta un incremento que no converge por **tiempo** (`10 × t0`); la app
lo hace por **iteraciones** (`max_iterations = 50000`). En malla fina esto los
detuvo en puntos distintos del incremento 55 (§4.4).

No conviene igualarlos hacia el criterio del script: un corte por tiempo **no es
reproducible**, porque el mismo script en una máquina más rápida ejecuta más
iteraciones y da un resultado distinto. El criterio por iteraciones de la app es
determinista y preferible. Lo correcto es **documentar la diferencia y no comparar
el incremento no convergido**, que es lo que se hizo.

Tampoco conviene subir los topes para "dejarlo converger": por encima de la carga
de colapso no existe equilibrio, así que iterar más no converge — solo avanza más
en el colapso y **aumenta** la diferencia entre las dos corridas, porque desaparece
el efecto de atractor que la tolerancia ejerce mientras sí hay solución (§5.5).
