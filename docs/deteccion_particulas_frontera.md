# Detección de partículas de frontera: por qué existe `boundary_particles3`

> **Material para la tesis.** Documenta por qué la aplicación MPM-UN sustituyó la
> función de detección de partículas de frontera del código original, qué
> algoritmo se implementó, cómo se validó, y cuál es la única diferencia que
> subsiste entre la aplicación y el motor de referencia en el caso del talud.
>
> Documento hermano: [validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md)
> (validación general) y [rendimiento_y_costo_computacional.md](rendimiento_y_costo_computacional.md).

Fecha del análisis: 2026-09-15 / 2026-09-17.

---

## 1. Para qué sirven las partículas de frontera

En la formulación de **integración mixta** del MPM-UN, cada elemento de la malla
de fondo se integra de una de dos maneras, y la decisión se toma en
[`particles_to_nodes_gauss2`](../app/motorMPM/explicit2.py#L544):

```python
if np.sum(bound_val[mpe - 1]) >= 1 and np.sum(Vp[mpe - 1]) < 0.9 * Vele:
    inte_ptcl = True    # elemento de borde y parcialmente lleno -> integracion por particulas
else:
    inte_ptcl = False   # elemento interior o lleno -> integracion de Gauss (1 punto)
```

Es decir, `bound_val` **no es un dato decorativo**: gobierna el esquema de
integración de cada elemento. Un elemento que se integra por Gauss recibe un
esfuerzo promedio único en su punto de Gauss; uno que se integra por partículas
conserva el esfuerzo individual de cada punto material. En elementos parcialmente
llenos —los del borde libre— la integración de Gauss introduce error, porque
promedia sobre un volumen que en realidad está vacío en parte.

De ahí que un error en la detección de frontera se traduzca directamente en
esfuerzos equivocados cerca de la superficie libre.

---

## 2. Las tres variantes y por qué no bastaban las originales

El código original (`mpm_un/mesh.py`) trae dos funciones:

### `boundary_particles` (línea 436)

```python
left  = np.where(xp[:,0] == np.min(xp[:,0]))[0] + 1
right = np.where(xp[:,0] == np.max(xp[:,0]))[0] + 1
down  = np.where(xp[:,1] == np.min(xp[:,1]))[0] + 1
up    = np.where(xp[:,1] == np.max(xp[:,1]))[0] + 1
```

Toma los cuatro extremos del rectángulo envolvente. Su propio docstring lo
advierte: *"solo valido para la distribucion inicial rectangular"*. Sirve para
viga y capacidad portante; sobre un talud marcaría como "superficie" únicamente
la fila más alta del dominio completo, ignorando toda la cara inclinada.

### `boundary_particles2` (línea 456)

```python
xxp = np.unique(np.round(xp[:,0], 10))      # columnas de x distintas
for i in range(len(xxp)):
    idxi   = np.where(np.absolute(xp[:,0] - xxp[i]) < 1e-10)[0]
    idymax = np.where(xp[idxi,1] == np.max(xp[idxi,1]))[0]
    up[i]  = idxi[idymax] + 1                # la particula mas alta de esa columna
```

Pensada para el talud: *"Valido para frontera superior inclinada"*. Para cada
columna de `x` toma la partícula de mayor `y`. **Su limitación es estructural**:
supone que las partículas están alineadas en columnas perfectas, y solo reconoce
**una** partícula de superficie por columna.

Eso falla en dos situaciones:

1. **Mallas no estructuradas.** La aplicación genera puntos materiales a partir
   de elementos que pueden ser irregulares; los centroides no se alinean en
   columnas exactas. `np.unique(xp[:,0])` devuelve entonces casi tantas
   "columnas" como partículas, y la detección se vuelve ruido.
2. **Superficies inclinadas discretizadas en escalera.** Aunque las columnas
   estén alineadas, una cara inclinada se representa como una escalera. La
   partícula más alta de cada columna es el "peldaño", pero las que forman la
   **contrahuella vertical** también están expuestas al aire y `boundary_particles2`
   no las ve.

### `boundary_particles3` (app, línea 572) — alpha shape

Implementada para la aplicación, sustituye el criterio geométrico por uno
topológico:

1. Triangulación de Delaunay de toda la nube de puntos.
2. Longitud de todas las aristas; se toma la **mediana** como espaciado típico.
3. Se descartan los triángulos cuya arista más larga supere
   `alpha_factor × mediana`, con `alpha_factor = 2.5`. Esto elimina los
   triángulos gigantes que Delaunay crea para cerrar la envolvente convexa
   cruzando zonas vacías.
4. De los triángulos que sobreviven, se cuentan las aristas: **las que aparecen
   en un solo triángulo son frontera**.
5. Las partículas de esas aristas son las partículas de borde.

La técnica es independiente de la orientación y de que la nube sea convexa o
cóncava, y no supone ninguna alineación en columnas.

---

## 3. Qué detecta cada una sobre la geometría del talud

Experimento: [`tools/experimentos/frontera_talud.py`](../tools/experimentos/frontera_talud.py).
Reconstruye la nube exacta de `talud_2021.py` (geometría G8: `x1 = 8`, `x2 = 18`,
`y1 = 0.5`, dominio 60 × 30.5 m) y aplica ambas funciones. **No simula nada**:
ambas son funciones puras de `xp`.

| `ele_size` | nmp | `bp2` | `bp3` | solo `bp2` | solo `bp3` | dif. simétrica |
|---|---|---|---|---|---|---|
| 0.5 (la del script) | 6740 | 600 | 639 | **0** | **39** | 0.6 % |
| 1.0 | 1674 | 214 | 152 | **82** | 20 | 6.1 % |

### Con `ele_size = 0.5`: `bp3` es superconjunto estricto

Las 39 partículas adicionales están **todas** en la cara inclinada
(8 < x ≤ 18), ninguna en la corona ni en el pie. Son exactamente las
contrahuellas de la escalera que `bp2` no puede ver por tomar un solo máximo por
columna. Aquí `bp3` detecta más, y con mejor criterio geométrico.

### Con `ele_size = 1.0`: `bp3` degenera

Las 82 partículas que `bp3` pierde están todas en `y = 0.25`, con `x` de 19.25 a
59.75: es **la capa basal completa** del pie.

**Causa:** con `ele_size = 1.0`, el estrato inferior (`y ≤ y1 = 0.5`) conserva
solo la fila `y = 0.25`, o sea queda de **una partícula de espesor**. Una fila de
puntos colineales no genera triángulos de Delaunay, así que el alpha shape no
puede construir ninguna arista de frontera y los descarta. `bp2` los captura
porque toma la fila inferior entera (`down = argmin` de `y`).

> **Limitación de `boundary_particles3` que conviene declarar en la tesis:**
> degenera en regiones de **una partícula de espesor**. No afecta la malla de la
> tesis (`ele_size` 0.5, donde el pie tiene dos filas), pero sí afectaría a
> cualquier estrato delgado mal discretizado. Es un requisito de uso, no un
> defecto oculto.
>
> **Corolario práctico:** `ele_size = 1.0` no sirve como versión barata de este
> caso. A ese tamaño la capa basal de 0.5 m no se puede representar, así que se
> mediría un artefacto de la discretización y no la pregunta de interés.

---

## 4. Cuánto cambia el resultado: experimento controlado

La pregunta de fondo no es cuántas partículas marca cada función, sino **cuánto
cambia el resultado físico**. Para aislarlo se corrió el geostático del talud
**dos veces con el mismo motor, la misma nube de partículas, el mismo orden y los
mismos parámetros**, cambiando únicamente la función de frontera.

### Montaje

- Script base: `talud_2021_2pasos.py` (copia de `talud_2021.py` con un único
  cambio, marcado en el archivo: rampa de gravedad de 10 pasos a 2 pasos
  `[0.5, 1.0]`, para abaratar el experimento).
- Variante `bp3`: [`exp_frontera_bp3.py`](../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/exp_frontera_bp3.py),
  que **no modifica el script**: lo importa como módulo y sustituye el nombre
  `boundary_particles2` en su espacio de nombres antes de llamar a
  `fase_geoestatica()`.
- Parámetros: 6740 partículas, `ele_size` 0.5, Courant 0.6, damping 0.75,
  tolerancias ff = ee = 0.01, elástico (`elapla = 0`), gravedad en 2 pasos.

### Resultado: el esquema numérico cambia de trayectoria

| | iteraciones paso 1 | iteraciones paso 2 |
|---|---|---|
| `bp2` | 2206 | 1866 |
| `bp3` | 2358 | 1798 |

### Diferencia en los campos (`SIGYY`, frame final)

| Zona | n | error mediano | error máximo | > 10 % |
|---|---|---|---|---|
| Corona (x ≤ 8) | 3904 | 1.18e-03 | 2.06e-02 | 0 |
| **Cuña (8 < x ≤ 18)** | 2500 | 5.08e-03 | **3.49e-01** | **7 (0.3 %)** |
| Pie (x > 18) | 336 | **7.01e-11** | 2.25e-03 | 0 |

El efecto está **confinado a la cara inclinada**. La corona y el pie —zonas
planas— coinciden dentro del ruido de tolerancia; el pie, de hecho, coincide
prácticamente bit a bit (7e-11).

Las siete partículas afectadas están en la punta de la cuña, donde la pendiente
se estrecha hasta encontrarse con la base:

| x | y | `bp2` (kPa) | `bp3` (kPa) | dif. |
|---|---|---|---|---|
| 17.625 | 1.125 | −137.99 | −293.79 | 34.9 % |
| 17.625 | 1.375 | −137.99 | −248.86 | 24.8 % |
| 17.125 | 2.625 | −94.81 | −194.28 | 22.3 % |
| 16.625 | 4.125 | −72.71 | −153.42 | 18.1 % |
| 16.125 | 5.625 | −58.84 | −127.82 | 15.5 % |
| 15.625 | 7.125 | −49.32 | −104.90 | 12.4 % |
| 17.625 | 1.625 | −96.16 | −47.38 | 10.9 % |

---

## 5. La prueba decisiva: la app **es** el motor original con `bp3`

El paso que cierra el argumento. Se construyó un proyecto de la aplicación con
las **posiciones exactas** de las 6740 partículas de la referencia (inyectadas
desde `geostatic_state_v2.npz`: `xp0`, `Vp0` y el reparto `idM1`/`idM2`), de modo
que la única diferencia posible con el script fuera la función de frontera.

Comparando ese proyecto contra la corrida de referencia:

| Referencia usada | Resultado |
|---|---|
| V1 con `bp2` | difiere: 7 partículas con error > 10 %, todas en la punta de la cuña |
| **V1 con `bp3`** | **`0.000e+00` en los 18 campos** |

```
  partículas:  referencia=6740   app=6740
  emparejadas por posición inicial (desajuste máx 0.000e+00 m)
  ...
  CORX       0.000000e+00   SIGXX      0.000000e+00   VELXX      0.000000e+00
  CORY       0.000000e+00   SIGYY      0.000000e+00   VELYY      0.000000e+00
  ...
COINCIDEN  (peor error relativo 0.000e+00 <= rtol 1e-09)
Comparados 18 campos, 6740 partículas, 3 frames.
```

**Coincidencia exacta, sin residuo.** Y las diferencias que se observaban contra
`bp2` —las 7 partículas, con sus valores hasta el último dígito— son
reproducidas exactamente por la corrida `bp2` vs `bp3` del §4.

### Qué queda demostrado

1. **El motor de la aplicación es el motor original**, también en la rama
   gaussiana y en geometría irregular. No hay diferencia numérica de ninguna
   clase.
2. **La única diferencia entre la aplicación y la referencia en el talud es la
   función de detección de frontera**, y su efecto está acotado y localizado: 7
   de 6740 partículas (0.1 %), todas en la punta de la cuña.
3. **Con la rampa de 2 pasos, el orden de acumulación no interviene**: el
   resultado es cero absoluto, porque las partículas se inyectaron en el mismo
   orden de la referencia. Con la rampa completa (§5 bis) reaparece un residuo
   pequeño y acotado, del mismo tipo que en capacidad portante
   (ver [validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md) §5).

Este es el nivel de validación más fuerte alcanzado en todo el proyecto: más
estricto que el de la viga (5.7e-11) y que el de capacidad portante.

---

## 5 bis. Confirmación con la rampa completa (10 pasos)

El experimento del §4-§5 se hizo con una rampa de gravedad reducida a 2 pasos
(`[0.5, 1.0]`) para abaratarlo. Quedaba la pregunta de si las conclusiones se
sostienen con la rampa completa de la tesis (10 pasos, `[0.1, 0.2, …, 1.0]`,
igual que `talud_2021.py` original). Se repitió todo el experimento sin ese
atajo.

### Montaje

Igual que en §4-§5, pero usando `talud_2021.py` sin modificar (rampa completa)
en vez de `talud_2021_2pasos.py`, y un proyecto de la app con la etapa
geostática configurada a 10 incrementos (con lo que `dincreGrav = 1/10 = 0.1`
reproduce exactamente el mismo array `grav`).

### App (`bp3`) contra V1 con `bp2`: el hallazgo se sostiene

| Zona | n | error mediano | error máximo | > 10 % |
|---|---|---|---|---|
| Corona (x ≤ 8) | 3904 | 9.70e-04 | 9.23e-03 | 0 |
| **Cuña (8 < x ≤ 18)** | 2500 | 4.70e-03 | **3.44e-01** | **8 (0.3 %)** |
| Pie (x > 18) | 336 | **9.86e-12** | 4.46e-03 | 0 |

Prácticamente idéntico al experimento de 2 pasos (7 partículas, error máximo
34.9 %): con la rampa completa son **8** partículas, error máximo **34.4 %**,
misma localización exacta en la punta de la cuña, pie otra vez a nivel de ruido
de máquina. La conclusión del §5 no dependía de haber acortado la rampa.

### App (`bp3`) contra V1 con `bp3`: ya no da cero, y eso también se explica

Con la **misma** función de frontera en ambos lados, el resultado a 10 pasos
**no** repite el `0.000e+00` de §5:

| Fracción de gravedad | 0.1 | 0.2 | 0.3 | 0.5 | 0.7 | 1.0 |
|---|---|---|---|---|---|---|
| Error máximo (`SIGYY`) | 0.000e+00 | 0.000e+00 | 1.2e-03 | 6.9e-03 | 1.21e-02 | 8.3e-03 |

Los dos primeros incrementos siguen siendo exactos. A partir del tercero
aparece un residuo que crece y se estabiliza por debajo del **1.3 %**, sin
ninguna partícula por encima del 10 % y **sin localización geométrica** (el
error se reparte parejo entre corona, cuña y pie).

| Zona | n | error mediano | error máximo | > 10 % |
|---|---|---|---|---|
| Corona (x ≤ 8) | 3904 | 1.78e-04 | 4.08e-03 | 0 |
| Cuña (8 < x ≤ 18) | 2500 | 2.02e-04 | 8.26e-03 | 0 |
| Pie (x > 18) | 336 | **9.23e-12** | 4.92e-05 | 0 |

**Interpretación.** Con todo controlado —mismas partículas, mismo orden, misma
función de frontera— siguen quedando dos procesos de Python separados
ejecutando ~13 000 ciclos acumulados del bucle cuasi-estático (contra ~4 000 en
el experimento de 2 pasos). El ruido de punto flotante entre esos dos procesos,
amplificado por el mismo mecanismo de "bola de tolerancia" descrito en
[validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md) §5.5
(la tolerancia de convergencia `tolff = 0.01` admite todo un entorno de estados
igualmente "convergidos"), termina apareciendo cuando hay suficientes
iteraciones acumuladas para que se note. Con 2 pasos no hubo tiempo de que
apareciera; con 10 sí, pero se queda por debajo de la tolerancia misma y sin
ningún valor atípico.

Esto **no debilita** la atribución a `bp2`/`bp3`: la separa con más nitidez
todavía. Compárense los dos efectos lado a lado, ambos con la rampa completa:

| Comparación | Partículas > 10 % | Error máximo | Patrón |
|---|---|---|---|
| app (`bp3`) vs V1-`bp2` | **8** | **34.4 %** | localizado en la punta de la cuña |
| app (`bp3`) vs V1-`bp3` | **0** | 0.83 % | disperso, sin localización |

Son dos fenómenos distintos y ninguno se confunde con el otro: uno tiene firma
geométrica y valores atípicos grandes; el otro es ruido genérico, acotado y sin
atípicos — el mismo patrón, con la misma explicación, que ya se había cerrado
para capacidad portante.

---

## 6. Qué afirmar en la tesis

1. **Por qué se sustituyó la función.** `boundary_particles2` supone partículas
   alineadas en columnas perfectas y reconoce una sola partícula de superficie
   por columna. Ninguna de las dos hipótesis se sostiene en una aplicación
   general, que debe admitir mallas no estructuradas y geometrías arbitrarias.
2. **Qué se implementó.** Un alpha shape (Delaunay filtrado por longitud de
   arista, `alpha_factor = 2.5`), que identifica la frontera por topología —
   aristas pertenecientes a un solo triángulo— en vez de por extremos
   coordenados.
3. **Qué detecta de más.** Sobre la geometría G8 con `ele_size` 0.5,
   `boundary_particles3` reconoce 39 partículas adicionales, todas en la cara
   inclinada: las contrahuellas de la escalera de discretización, que son
   superficie libre real y que `boundary_particles2` omite.
4. **Cuál es su limitación conocida.** Degenera en regiones de una partícula de
   espesor, donde la triangulación de Delaunay no puede formarse. Debe evitarse
   discretizar estratos delgados con menos de dos filas de partículas.
5. **Cuánto cambia el resultado.** Con la discretización de la tesis, el efecto
   se limita a 7-8 partículas de 6740 (0.1 %) en la punta de la cuña, con
   diferencias de hasta 35 % en `SIGYY` local. Corona y pie no se ven afectados;
   el pie coincide a nivel de ruido de máquina. Verificado tanto con una rampa
   de gravedad reducida (2 pasos) como con la rampa completa de la tesis
   (10 pasos, §5 bis): el hallazgo no depende del atajo.
6. **Que el motor es el mismo.** Alimentando el motor original con
   `boundary_particles3` se reproduce la salida de la aplicación
   **exactamente** con la rampa de 2 pasos (0.000e+00 en 18 campos × 6740
   partículas × 3 frames). Con la rampa completa de 10 pasos reaparece un
   residuo pequeño (máximo 0.83 %, cero partículas atípicas, sin localización
   geométrica) — el mismo ruido de acumulación entre procesos, acotado por la
   tolerancia de convergencia, ya documentado para capacidad portante. No
   afecta la atribución del punto 5: esa comparación (8 partículas, hasta
   34 %, todas en la punta de la cuña) es dos órdenes de magnitud mayor y de
   patrón completamente distinto.

### Lo que queda como discusión de método, no como defecto

Cuál de las dos funciones representa mejor la física en la punta de la cuña es
una pregunta abierta de criterio, no un error del software. Ahí `bp3` produce
esfuerzos mayores (−293.8 contra −138.0 kPa). El argumento a favor de `bp3` es
geométrico: esas partículas **están** en la superficie libre y deben integrarse
por partículas, no por Gauss. Confirmarlo requeriría un caso con solución
analítica en una cuña, o un estudio de convergencia con la malla.

---

## 7. Cómo reproducir

```bash
# 1. Comparacion pura de las dos funciones (segundos, no simula nada)
cd "2 Software/MPM-UN"
python tools/experimentos/frontera_talud.py          # ele_size 1.0 y 0.5
python tools/experimentos/frontera_talud.py 0.5      # solo uno

# 2. Geostatico de referencia con bp2 (el del script original)
cd "1 Referencia/Codigo MPM-UN Original_V1"
MPLBACKEND=Agg ./.venv/Scripts/python.exe -u talud_2021_2pasos.py \
    > logs/talud_2pasos.log 2>&1
#    detener el proceso cuando aparezca "guardado: ...talud_geostatico.npz":
#    el script continua solo hacia fase_falla(), que son horas.
mv resultados_referencia/talud_geostatico.npz resultados_referencia/talud_geostatico_bp2.npz

# 3. El mismo geostatico con bp3, sin tocar el script
MPLBACKEND=Agg ./.venv/Scripts/python.exe -u exp_frontera_bp3.py \
    > logs/talud_2pasos_bp3.log 2>&1
mv resultados_referencia/talud_geostatico.npz resultados_referencia/talud_geostatico_bp3.npz

# 4. Comparar la app contra cada una
cd "2 Software/MPM-UN"
python tools/compare_ref.py \
    "…/resultados_referencia/talud_geostatico_bp3.npz" \
    "test/6 archivos_mpm 2609/3_talud_elastoplastico full 2 pasos - particulas igual a V1.json" \
    --por-indice
```

### Nota sobre el proyecto con partículas inyectadas

`3_talud_elastoplastico full 2 pasos - particulas igual a V1.json` no se generó
dibujando el polígono en la interfaz, sino **escribiendo directamente en el JSON**
las coordenadas, volúmenes y reparto de materiales de `geostatic_state_v2.npz`.

Fue necesario porque ajustar el polígono a mano no alcanza la precisión
requerida: el esfuerzo cerca de una superficie libre inclinada depende de
**cuántas capas de partículas hay exactamente encima de cada punto, columna por
columna**, y el ratón no tiene resolución de sub-partícula (0.25 m). Se
comprobó experimentalmente:

| Proyecto | nmp total | partículas con error > 10 % en la cuña |
|---|---|---|
| Polígono dibujado, 1er intento | 6840 (+100) | 71 |
| Polígono reajustado a mano | 6700 (−40) | 67 |
| **Puntos inyectados** | **6740 (exacto)** | **7** |

Acercar el **conteo total** no mejora el ajuste: pueden sobrar partículas en unas
columnas y faltar en otras, compensándose en el total mientras empeora
localmente. Solo la coincidencia exacta, columna por columna, resuelve el
problema.

---

## 8. Pendientes

- [x] Geostático completo (10 pasos de gravedad) con `bp2` y con `bp3` — hecho,
      ver §5 bis. Las conclusiones se sostienen con la rampa completa.
- [ ] Decidir y justificar cuál de las dos funciones se adopta como correcta en
      la punta de la cuña (§6, última sección).
- [ ] Fase de falla: la referencia es de dos cuerpos con contacto y la
      aplicación es mono-cuerpo. Requiere la Fase B. **Nota:** la fase de falla
      del original **no usa partículas de frontera** —las llamadas a
      `boundary_particles2` están comentadas (`talud_2021.py` líneas 551 y 615)
      porque usa `particles_to_nodes` sin integración gaussiana—, así que este
      hallazgo no la afecta.
