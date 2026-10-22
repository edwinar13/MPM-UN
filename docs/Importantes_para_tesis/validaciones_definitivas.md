# Validaciones definitivas de la aplicación (octubre de 2026)

Corridas finales de los cuatro casos de referencia, **armadas y ejecutadas desde la
interfaz** (malla, puntos materiales, cargas, contornos y etapas), sin generar ni
modificar proyectos por script. Archivos en `test/7 archivos_mpm 2610/`; las
carpetas de prueba anteriores (`test/4`–`test/6`) ya no cuentan.

| Caso | Proyecto | Tipo de análisis | Referencia | Resultado |
|---|---|---|---|---|
| Viga en voladizo | `1_viga.json` | dinámico, elástico | `beam.py` (León, 2019) | **numéricamente igual** (5.7e-11) |
| Capacidad portante | `2_capacidad_portante.json` | carga incremental, Mohr-Coulomb | `Ca_portante2.py` (León, 2019) | ≤ 1.1 % hasta 108 kPa; misma carga de colapso |
| Talud | `3_Talud falla.json` | geostático → falla dinámica con dos cuerpos y contacto | `talud_2021` (Sandoval Montoya, 2021) | avance del pie dentro del 1 % |
| Consolidación 1D | `4_consolidacion_1d.json` | doble fase (v-w) | Terzaghi; caso 7.1 de Caro González (2024) | error máx. 1.9 % de p₀, solo al inicio |
| Consolidación 2D | `5_consolidacion_2d.json` | doble fase (v-w), carga en franja | caso 7.3 de Caro González (2024), Figuras 7-28 y 7-29 | mismos patrones de σyy y p en los seis tiempos (comparación visual: el caso no tiene solución analítica) |

Las referencias numéricas son los `.npz` de
`1 Referencia/Codigo MPM-UN Original_V1/resultados_referencia/`, escritos por los
scripts originales sin tocar su cálculo, y se comparan con `tools/compare_ref.py`.
El porqué de las diferencias que no son de redondeo (orden de las partículas,
función de partículas de frontera) está en
[validacion_motor_vs_referencia.md](../validacion_motor_vs_referencia.md) y
[deteccion_particulas_frontera.md](../deteccion_particulas_frontera.md).

---

## 1. Viga en voladizo

**Montaje.** Malla de fondo 4 × 4 m, elemento 0.2 m; un grupo de 304 partículas
(4 por elemento); material elástico E = 10 000 kPa, ν = 0.2, ρ = 2 Mg/m³;
gravedad 9.81. Etapa dinámica de 4 s, Courant 0.5 (dt = 0.001 s, 4000 pasos),
damping 0, FPS 40 (161 frames). Extremo izquierdo empotrado.

**Resultado.** Contra `beam.npz`: los 18 campos coinciden en las 304 partículas y
los 161 frames, con error relativo máximo **5.7e-11**. Es redondeo de máquina: en
un esquema explícito de paso fijo el orden de las operaciones solo se acumula como
redondeo. El resultado es el mismo con el material declarado Elástico o
Mohr-Coulomb, porque la etapa es elástica.

## 2. Capacidad portante

**Montaje** (la discretización del script de la tesis). Malla de fondo 20 × 15 m,
elemento 0.5 m; suelo de 20 × 10 m con 3200 partículas (4 por elemento, volumen
0.0625 m²); material Mohr-Coulomb E = 10 000 kPa, ν = 0.49, c = 20 kPa, φ = ψ = 0,
ρ = 1.8 Mg/m³; **gravedad 0**. Zapata: las 20 partículas de la fila superior con
x ∈ [0.125, 4.875], Fy = −28 kN/m cada una (560 kN/m = 112 kPa × 5 m). Etapa de
carga incremental: 56 incrementos, Courant 0.1, damping 0.75, elastoplástica,
integración Gauss, tolerancias ff = 0.011 y ee = 0.01 (las de `Ca_portante2.py`).

**Entradas.** Nodos de la malla, posiciones de las partículas y fuerzas de la
zapata idénticas a las del script (Δ = 0.0).

**Resultado.** Incrementos 0–54 (hasta 108 kPa), todos convergidos:

| Campo | Error relativo máximo |
|---|---|
| σyy | 0.59 % |
| σxx | 1.12 % |
| τxy | 1.50 % |
| Deformación plástica equivalente | 1.19 % |
| Posición y | 0.02 % |

La plasticidad aparece en el mismo incremento en las dos corridas (frame 31,
62 kPa). Curva carga–asentamiento bajo la zapata:

| q (kPa) | Referencia (m) | App (m) | Diferencia |
|---|---|---|---|
| 10 | −0.003710 | −0.003710 | 0.00 % |
| 50 | −0.018559 | −0.018601 | 0.23 % |
| 90 | −0.045506 | −0.045588 | 0.18 % |
| 100 | −0.062472 | −0.062465 | 0.01 % |
| 106 | −0.083991 | −0.084038 | 0.06 % |
| 108 | −0.109222 | −0.107264 | 1.8 % |

Las dos corridas **sostienen 108 kPa y no 110 kPa**, frente a los 102.8 kPa de
Prandtl (+5 %). El incremento 55 (110 kPa) no converge en ninguna: por encima de
la carga de colapso no hay equilibrio, y cada corrida corta por un criterio
distinto (tiempo en el script, iteraciones en la app). Ese frame no se compara.

Las diferencias de los incrementos convergidos son del orden de la tolerancia de
convergencia: la app recorre las partículas en otro orden, el redondeo cambia y la
iteración se detiene en otro estado que también cumple la tolerancia. La corrida es
además **reproducible**: idéntica bit a bit a la corrida anterior de la app.

## 3. Talud (geostático → falla)

**Montaje.** Malla de fondo 60 × 32 m, elemento 0.5 m. Dos polígonos dibujados con
coordenadas exactas:

- Base: (0, 0), (60, 0), (60, 0.5), (0, 0.5) → 480 partículas.
- Talud: (0, 0.5), (18, 0.5), (8, 30.5), (0, 30.5) → 6260 partículas.

Las partículas se generan con la malla *Estructurada* (subdivisión 4, sub-celdas de
0.25 m alineadas con la malla de fondo) y un punto por sub-celda. Es la misma regla
del script: se conserva una sub-celda si su centro está dentro del polígono,
incluidos los centros que caen sobre la línea del talud. Resultado: **las mismas
6740 partículas del script**, con posiciones idénticas (Δ = 0.0). Antes de ajustar
esa regla (9 de octubre) la interfaz dejaba por fuera los 40 centros sobre la
pendiente, y por eso el proyecto validado en septiembre se armó inyectando las
partículas en el `.json`.

Contornos: fondo fijo en x e y, laterales fijos en x. Gravedad 9.81.

| Material | Modelo | E (kPa) | ν | c (kPa) | φ (°) | ψ (°) | ρ (Mg/m³) |
|---|---|---|---|---|---|---|---|
| Base geostático | Mohr-Coulomb | 15 000 | 0.3 | 200 | 35 | 35 | 2.6 |
| Talud geostático | Mohr-Coulomb | 15 000 | 0.3 | 5 | 35 | 35 | 1.8 |
| Base falla | Elástico | 10 000 | 0.3 | 200 | 35 | 35 | 2.6 |
| Talud falla | Mohr-Coulomb | 3 800 | 0.3 | 20 | 20 | 10 | 1.8 |

| | Etapa 1: geostático | Etapa 2: falla |
|---|---|---|
| Tipo | geostático (rampa de gravedad) | dinámico |
| Incrementos / duración | 10 | 8 s (dt 0.0006 s, 161 frames) |
| Courant / damping | 0.6 / 0.75 | 0.1 / 0.10 |
| Comportamiento | elástico | elastoplástico |
| Tolerancias ff / ee | 0.01 / 0.01 | — |
| Interfaz entre grupos | adherida (un cuerpo) | friccional, μ = 0.268 |
| Otros | — | reinicio de deformaciones; cambio de material a los de la falla |

Respecto del script original hay dos diferencias deliberadas, ya decididas y
documentadas en [plan_fase_b.md](../plan_fase_b.md): en la falla la base sí tiene
peso propio (+0.6 % en el avance del pie) y la falla parte de las posiciones del
geostático (el script devuelve las partículas a su sitio inicial y pierde hasta
0.40 m de asentamiento). Por eso la referencia de la falla es
`talud_2021_falla_app.py`, una copia del script con esos dos cambios marcados.

**Geostático.** Contra el script con la misma función de partículas de frontera que
usa la app (`bp3`): posiciones a 0.11 mm, esfuerzos a 1.1–1.7 % (5 kPa en σyy),
desplazamiento máximo 0.3962 m frente a 0.3961 m. Es el orden de la tolerancia
(1 %), por la misma razón que en capacidad portante. Contra el script puro (`bp2`)
subsiste la diferencia conocida en la punta de la cuña, debida a la función de
partículas de frontera.

**Falla** (8 s), comparada contra la referencia arrancando del geostático del
script y contra la misma referencia arrancando del geostático de la app:

| Medida | Desde geostático del script | Desde geostático de la app | App |
|---|---|---|---|
| Avance del pie a 1 s (m) | 2.290 | 2.280 | 2.278 |
| Avance del pie a 4 s (m) | 11.224 | 11.496 | 11.436 |
| **Avance del pie a 8 s (m)** | 13.567 (+1.0 %) | 13.761 (−0.4 %) | **13.709** |
| Desplazamiento medio del talud a 8 s (m) | 6.131 | 6.149 | 6.118 |
| Altura final de la cresta (m) | 23.41 | 23.37 | 23.35 |

Todas las medidas quedan dentro del 1 % de ambas referencias (la mayor diferencia
puntual es +1.9 %, en el avance del pie a 4 s), y la app cae entre las dos. Partícula
a partícula, la posición final difiere en 0.11 m de media sobre un flujo de 13.7 m:
el flujo amplifica diferencias de entrada del orden de la tolerancia del
geostático. Cuando las dos fallas arrancan exactamente del mismo estado, la de la
app es idéntica bit a bit a la referencia (plan_fase_b.md §6.4).

## 4. Consolidación unidimensional (doble fase)

**Montaje.** Columna de 0.1 × 1.0 m; malla de fondo de 0.1 m (10 elementos); malla
base de cuadriláteros de 0.0142 m (7 × 70) con un punto por celda → **490
partículas**, 49 por elemento como en la Tabla 7-1 de Caro González (2024).
Material elástico E' = 10 MPa, ν' = 0, n₀ = 0.3, k = 1e-3 m/s, K_w = 100 MPa,
densidad seca 1.89 Mg/m³; gravedad 0. Carga q₀ = 10 kPa como Fy = −0.142857142857143
kN/m en las 7 partículas de la superficie. Laterales fijos en x y fondo fijo en y,
impermeables; la superficie drena. Etapa de consolidación de 4 s, Courant 0.98
(dt = 0.0002 s por la onda no drenada, 20 000 pasos), presión de poros inicial
10 kPa.

**Resultado.** Contra el script de validación (`consolidacion_1d.py`, con las mismas
partículas): presión de poros 2e-14, posición 3e-16 y esfuerzo efectivo 1e-14 de
error relativo, es decir, redondeo. Contra Terzaghi (cv = 1.019 m²/s), en la
partícula a 0.38 m de la superficie drenante:

| t (s) | Tv | U app | U Terzaghi | p app (kPa) | p Terzaghi (kPa) |
|---|---|---|---|---|---|
| 0.07 | 0.07 | 0.277 | 0.294 | 6.77 | 6.96 |
| 0.10 | 0.10 | 0.337 | 0.360 | 5.84 | 5.99 |
| 0.27 | 0.27 | 0.577 | 0.584 | 3.48 | 3.67 |
| 0.50 | 0.51 | 0.759 | 0.768 | 1.98 | 2.04 |
| 1.00 | 1.02 | 0.928 | 0.934 | 0.59 | 0.58 |
| 2.00 | 2.03 | 0.994 | 0.995 | 0.05 | 0.05 |
| 4.00 | 4.08 | 1.000 | 1.000 | 0.00 | 0.00 |

El error es como máximo 1.9 % de p₀, al inicio, y desaparece desde Tv ≈ 1. Al final
la presión de poros es menor de 0.001 kPa y el asentamiento es 0.986 mm (teórico
0.993 mm a la altura de esa partícula).

---

## 4b. Consolidación bidimensional (doble fase)

**Montaje** (sección 7.3 de Caro González, 2024). Medio dominio de 10 × 7 m con el
eje de simetría a la izquierda; malla de fondo de 0.5 m (10 × 8 m); malla base de
cuadriláteros de 0.1666 m (60 × 42) → **2520 partículas**, 9 por elemento como en
la tesis. Material de la Tabla 7-1 (el mismo del caso 1D); gravedad 0. Carga
q₀ = 20 kPa en B = 2 m: Fy = −3.333333333333333 kN/m en las 12 partículas de la
superficie con x < 2 m (suma −40 kN/m). Laterales fijos en x y fondo fijo en y,
impermeables; la superficie drena. Etapa de consolidación de 3 s con presión de
poros inicial 0 (la carga entra en t = 0), Courant 0.2 (dt = 0.0002 s, 15 000
pasos) y amortiguamiento local α = 0.05.

**Resultado.** El caso no tiene solución analítica; la tesis lo presenta como
aplicación, con mapas de σ'yy y de p a 0, 0.1, 0.25, 0.5, 1 y 3 s. Los mapas de la
aplicación reproducen los mismos patrones: presión de poros alta bajo la carga
justo después de aplicarla (con la zona de p positiva cerca de la superficie que
la tesis atribuye a oscilaciones numéricas), disipación desde la superficie hacia
abajo, presión aún alta en profundidad a los 3 s y bulbo de σyy que crece bajo la
carga. En la partícula junto a P(0, H/2):

| t (s) | p (kPa, compresión −) | σyy (kPa) | Asentamiento bajo la carga (mm) |
|---|---|---|---|
| 0.10 | −10.47 | −8.42 | 4.71 |
| 0.25 | −9.52 | −7.09 | 4.82 |
| 0.50 | −5.52 | −6.30 | 4.99 |
| 1.00 | −7.72 | −5.82 | 5.19 |
| 3.00 | −6.56 | −6.83 | 6.23 |

**Dos ajustes que pidió este caso.**

- *Paso de tiempo.* Con Courant 0.5 el dt de la onda no drenada fue 6e-4 s, por
  encima del límite del arrastre de Darcy explícito, 2k / (n·g·(1 + n·ρw/ρd)) ≈
  5.9e-4 s: la velocidad relativa agua–suelo creció ~4.6 % por paso y la corrida
  explotó en el paso 386. Con Courant 0.2 (dt 2e-4 s, el del caso 1D) es estable.
  En el 1D no aparece porque la malla de 0.1 m ya da un dt menor.
- *Amortiguamiento.* Sin amortiguamiento (α = 0) la carga súbita deja el bloque
  vibrando: p y el asentamiento oscilan con periodo ~0.2 s alrededor de la
  disipación. Con α = 0.025 y α = 0.05 la oscilación desaparece y las dos curvas
  coinciden desde ~0.8 s, es decir, el amortiguamiento solo limpia el arranque y
  no cambia la respuesta de largo plazo (misma conclusión de Caro González en el
  caso 1D). Los mapas de la tesis corresponden a la solución amortiguada.

---

## 5. Ajustes de la aplicación que salieron de estas corridas

Armar los modelos desde la interfaz, en lugar de generarlos por script, mostró
problemas que las corridas sin interfaz no veían:

- Tamaño de malla con 4 decimales (antes 2: no se podía armar 7 × 7 partículas por
  elemento).
- Fuerzas y velocidades aceptan coma decimal; tooltip con los datos de cada punto
  material y suma de fuerzas de la selección.
- Búsqueda del borde con tolerancia en `traction_forces` (en la consolidación una
  de las 7 partículas de la superficie quedaba sin carga por un bit de redondeo).
- Malla Estructurada: un centro sobre el borde del polígono cuenta como dentro
  (talud con las 6740 partículas del script).
- dt de la consolidación calculado con la onda no drenada también en el panel y en
  el diálogo de etapas; `DATOSTIEMPOS` guarda los valores reales de la corrida.
- Barra de colores de la animación con nombre, componente y unidades; etiqueta de
  un punto que se puede arrastrar.
