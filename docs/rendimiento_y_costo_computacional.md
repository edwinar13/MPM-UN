# Rendimiento y costo computacional del motor MPM-UN

> **Estado: análisis, no implementación.** Nada de lo aquí descrito se ha aplicado al
> código. Se documenta para (a) la sección de costo computacional y trabajo futuro de la
> tesis y (b) retomar la optimización cuando la validación numérica esté cerrada.
>
> **No implementar durante la validación.** Cualquier cambio en el motor invalida las
> corridas de referencia ya hechas y las que estén en curso. Ver §9 para el protocolo.

Fecha del análisis: 2026-09-10.
Documento hermano: [validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md).

---

## 1. La pregunta

El caso de capacidad portante con la discretización de la tesis (`ele_size = 0.5`) tarda
del orden de **9 horas** en un equipo de escritorio. La pregunta que motiva este documento
es si ese costo es inherente al Método del Punto Material, es inherente al esquema
numérico, o es de la implementación — y qué haría falta para que un análisis así corriera
en minutos.

La respuesta corta: **el MPM no es el culpable**. El costo se reparte entre un problema
de implementación (§3 y §4) que vale entre uno y dos órdenes de magnitud, y una decisión
de método (§5) que vale otros dos o tres. El MPM como tal aporta poco al sobrecosto.

---

## 2. Lo que cuesta hoy: medición

Caso: `Ca_portante2.py`, capacidad portante, gravedad 0, 56 incrementos de carga.

| | malla gruesa | malla tesis |
|---|---|---|
| `ele_size` | 1.0 m | 0.5 m |
| Malla de fondo (20 × 15 m) | 20 × 15 = 300 elem., 336 nodos | 40 × 30 = 1200 elem., 1271 nodos |
| Cuerpo de suelo (20 × 10 m) | 200 elem. activos | 800 elem. activos |
| Partículas (`nmpe = 4`) | 800 | **3200** |
| Nodos activos | 231 | **861** |
| `dtime` | 3.000e-4 s | 1.500e-4 s |
| Tiempo total | 3555 s (≈ 1 h) | ≈ 32 000 s (≈ 9 h, estimado) |

Ciclos y tiempo por incremento, malla 0.5 (medido, primeros seis incrementos):

| Incremento | Ciclos | Tiempo (s) | ms / ciclo |
|---|---|---|---|
| 1 | 17 367 | 1284.0 | 73.9 |
| 2 | 13 734 | 976.1 | 71.1 |
| 3 | 10 866 | 748.2 | 68.8 |
| 4 | 9 982 | 687.6 | 68.9 |
| 5 | 8 574 | 807.4 | 94.1 † |
| 6 | 7 019 | 549.0 | 78.2 |

† El incremento 5 incluye el primer volcado parcial a disco (`guardar_parcial`), más
contención con otros procesos. No es representativo.

**Costo por ciclo ≈ 73 ms** con 3200 partículas, es decir **23 µs por partícula por paso**.
Un kernel MPM ajustado en Numba debería estar en el orden de 0.1–0.2 µs por partícula por
paso. Estamos entre 100 y 200 veces por encima de lo que el hardware permite.

Ese factor es el objeto de las secciones 3 y 4.

---

## 3. Hallazgo principal: dos búsquedas lineales O(N²) en el camino caliente

Las dos funciones de transferencia que este análisis usa —`particles_to_nodes_gauss2` y
`nodes_to_particle_stress_gauss`, la rama gaussiana que corresponde a etapas geostáticas y
de incremento de carga— contienen dos patrones de búsqueda lineal anidados dentro de los
bucles de elementos y partículas. Ninguno de los dos hace física: son **contabilidad de
índices**.

### 3.1 `elem_i_mp`: rastrear todas las partículas para hallar las de un elemento

[`app/motorMPM/mesh.py:465-471`](../app/motorMPM/mesh.py#L465-L471)

```python
def elem_i_mp(mp_elem, active_elem):
    """ Funcion que determina que MP estan en el elemento i"""
    indx = []
    for j in range(len(mp_elem)):          # <-- recorre las 3200 particulas
        if mp_elem[j, 0] == active_elem:
            indx.append(j + 1)
    return np.array(indx)
```

Se invoca **una vez por elemento activo** dentro del bucle principal de cada función de
transferencia ([`explicit2.py:540`](../app/motorMPM/explicit2.py#L540), y análogos en las
líneas 254, 318, 440).

Costo por llamada a la función de transferencia:

```
800 elementos × 3200 partículas = 2 560 000 iteraciones
```

para producir una información que ya está implícita en `mp_elem` y que se puede obtener
en O(N) con un conteo. Adicionalmente asigna una lista y un array NumPy nuevos por
elemento, 800 asignaciones por llamada.

### 3.2 Traducción de nodo global a índice de nodo activo

[`app/motorMPM/explicit2.py:563-566`](../app/motorMPM/explicit2.py#L563-L566) y
[`explicit2.py:585-588`](../app/motorMPM/explicit2.py#L585-L588)

```python
for k in range(len(nodes)):          # 4 nodos del elemento
    nng = nodes[k]
    # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
    for m in range(len(active_nodes)):   # <-- recorre los 861 nodos activos
        if active_nodes[m] == nng:
            nna = m
            break
```

Este bloque aparece **11 veces** en `explicit2.py`; está en todas las funciones de
transferencia, no solo en la rama gaussiana. Está anidado dentro del bucle de partículas,
que a su vez está dentro del bucle de elementos.

Costo por llamada, con 861 nodos activos (recorrido medio ≈ 430 antes del `break`):

```
rama gauss     :  800 elem. × 4 nodos × 430 = 1 376 000
rama particulas: 3200 part. × 4 nodos × 430 = 5 504 000
                                              ---------
                                              6 880 000 iteraciones
```

**Detalle que abarata mucho la corrección:** `active_nodes` se construye con
`np.unique(...)` ([`Ca_portante2.py:137`](../../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/Ca_portante2.py#L137)),
y `np.unique` **devuelve el array ordenado**. Es decir, se está haciendo una búsqueda
lineal sobre un array ordenado. Cambiarla por búsqueda binaria son cinco líneas y baja el
recorrido medio de 430 a 10 (≈ 43x en ese bloque). Un array inverso `nodo_global →
índice_activo` lo baja a 1 (≈ 430x) y es igual de simple.

### 3.3 La aritmética predice el tiempo medido

Por ciclo del bucle cuasi-estático
([`Ca_portante2.py:132-181`](../../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/Ca_portante2.py#L132-L181))
hay **dos** llamadas a funciones de transferencia pesadas: `particles_to_nodes_gauss2`
(línea 143) y `nodes_to_particle_stress_gauss` (línea 163). Cada una arrastra los dos
patrones anteriores:

```
por llamada  : 2 560 000 (elem_i_mp) + 6 880 000 (lookup nodal) ≈  9 400 000
por ciclo    : × 2 llamadas                                     ≈ 18 800 000 iteraciones
```

A ~4 ns por iteración (acceso disperso a memoria, un solo núcleo, con verificación de
límites de Numba) eso da **≈ 75 ms por ciclo**.

**Medido: 73 ms por ciclo.**

La coincidencia es lo bastante estrecha como para concluir que estas dos búsquedas
explican prácticamente todo el tiempo de ejecución. La física real —evaluar funciones de
forma, dispersar masa y momentum, integrar la ley constitutiva— son unas 128 000
operaciones de punto flotante por ciclo, es decir **menos del 1 %** del trabajo que la
máquina está haciendo.

### 3.4 Consecuencia: refinar la malla castiga al cuadrado

Este es el efecto práctico más importante del hallazgo, y explica algo que veníamos
observando sin entender.

Ambos patrones son producto de dos cantidades que crecen con el refinamiento:
`elem_i_mp` es `nelem × nmp`, y el *lookup* nodal es `nmp × nnodes`. Como `nelem`, `nmp` y
`nnodes` son todos proporcionales a `(L/h)²` en 2D, **el costo por ciclo escala con
`(L/h)⁴`**: al partir `h` a la mitad, el trabajo por ciclo se multiplica por **16**, no
por 4.

Con un código O(N) el costo por ciclo escalaría con `(L/h)²` — factor 4. Es decir, la
implementación actual impone un sobrecosto de **4x adicional cada vez que se parte la
malla a la mitad**, y ese factor se compone: pasar de `h=1.0` a `h=0.25` costaría 16x más
de lo que debería, no 4x.

Comprobación con los dos casos corridos:

```
malla 1.0 : 200×800 + 800×4×115 + 200×4×115  ≈   620 000 × 2 llamadas ≈ 1.2 M / ciclo
malla 0.5 : 800×3200 + 3200×4×430 + 800×4×430 ≈ 9 400 000 × 2 llamadas ≈ 18.8 M / ciclo
                                                              razón ≈ 15x
```

15x contra el 16x teórico. El modelo cierra.

> **Nota para cerrar la medición:** falta el conteo de ciclos por incremento de la corrida
> malla 1.0 para descomponer el tiempo total en "costo por ciclo" × "número de ciclos".
> Ese `stdout` se perdió (se canalizó por `tail`, ver §9 de
> [validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md)). Es recuperable
> con una recorrida de ~1 h, o midiendo solo los primeros incrementos.

---

## 4. Hallazgo secundario: el motor corre en un solo núcleo

En `explicit2.py` aparecen seis ocurrencias de `parallel=True`, pero **todas están
comentadas**, dentro de las cadenas de firma desactivadas:

```python
@njit(cache=True)#('Tuple((...))')#, parallel=True)
def particles_to_nodes(grid, particle):
```

([`explicit2.py:289`](../app/motorMPM/explicit2.py#L289), y las líneas 625, 686, 715, 741,
766.) Las dos funciones gaussianas que dominan este análisis —líneas 511 y 2318— están
declaradas simplemente `@njit(cache=True)`, sin paralelización ni siquiera comentada.

El motor completo se ejecuta en **un hilo**. En un equipo de 8 a 16 núcleos eso deja sobre
la mesa un factor de 4 a 8 en las fases de dispersión y recolección, que son
vergonzosamente paralelas sobre partículas (con dispersión atómica o coloreado de
elementos para evitar carreras).

Advertencia importante: paralelizar **cambia el orden de suma** de las contribuciones
nodales y por tanto los resultados en el último bit, exactamente por el mismo mecanismo
documentado en
[validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md) §5. En un análisis
cuasi-estático con criterio de convergencia por tolerancia, esa perturbación de 1e-16 se
amplifica hasta la tolerancia (≈ 1 %). Es aceptable y explicable, pero hay que decidirlo y
documentarlo, no descubrirlo.

---

## 5. El problema estructural: relajación explícita para un problema estático

Los hallazgos anteriores son de implementación. Este es de método, y es más grande.

El bucle cuasi-estático resuelve cada incremento de carga dejando correr una **dinámica
amortiguada** hasta que el desbalance de fuerzas y la energía cinética caen bajo
tolerancia ([`Ca_portante2.py:132`](../../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/Ca_portante2.py#L132)):

```python
while (ff > 0.011) or (ee > 0.01):
```

con amortiguamiento no viscoso tipo Cundall, `dampfac = 0.75` (línea 146). Esto es
**relajación dinámica**: un método de primer orden cuya velocidad de convergencia está
gobernada por el número de condición de la matriz de rigidez, que escala como `(L/h)²`.

El precio, medido: entre 7 000 y 17 000 pasos explícitos para hallar **un** estado de
equilibrio. Para los 56 incrementos, del orden de **450 000 pasos**.

La alternativa implícita (Newton-Raphson con solución directa dispersa) halla ese mismo
equilibrio en 5 a 15 iteraciones. El sistema es de 861 nodos × 2 = **1722 grados de
libertad**, con ancho de banda ≈ 82; una factorización de Cholesky en banda son unos 12
millones de operaciones, milisegundos. Los 56 incrementos serían del orden de 300 a 800
soluciones lineales: **segundos a un minuto**, contra 450 000 pasos explícitos.

Ese es un factor estructural de **10² a 10³**, y es independiente de las optimizaciones de
§3 y §4 — se multiplica con ellas.

**Y no es culpa del MPM.** El costo por paso del MPM es comparable al del FEM: P2N y N2P
son dispersión y recolección baratas. Lo caro es usar un integrador explícito —diseñado
para propagación de ondas y grandes deformaciones dinámicas— para responder una pregunta
estática. El mismo sobrecosto tendría un FEM explícito.

### 5.1 Un intermedio mucho más barato: escalado de masa

Antes de escribir un solver implícito hay una palanca clásica y de bajo riesgo.

Como `dtime = Courant × ele_size / c` con `c = √(M/ρ)`, y como **en relajación dinámica el
tiempo físico no significa nada** (solo interesa el estado final de equilibrio), se puede
inflar artificialmente la densidad. Multiplicar `ρ` por 100 divide `c` por 10, multiplica
`dtime` por 10, y reduce el número de ciclos en la misma proporción.

Es lo que Abaqus/Explicit hace de rutina para problemas cuasi-estáticos. El criterio de
validez es que la energía cinética se mantenga pequeña frente a la energía interna — y
**este código ya calcula esa relación**: es el `ee` del criterio de convergencia
(`static_convergence`, [`Ca_portante2.py:170`](../../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/Ca_portante2.py#L170)).
La instrumentación para validarlo ya existe.

Ganancia esperable: **5x a 20x**, con un cambio de una línea y un chequeo que ya está
implementado.

### 5.2 Nota sobre la incompresibilidad

El caso usa `ν = 0.49` ([`Ca_portante2.py:56`](../../../1%20Referencia/Codigo%20MPM-UN%20Original_V1/Ca_portante2.py#L56)),
correcto para condición no drenada. Pero el módulo confinado

```
M = E(1-ν) / ((1+ν)(1-2ν))
```

se dispara cuando `ν → 0.5`: con `E = 10 MPa` y `ν = 0.49` da `M ≈ 171 MPa` y
`c ≈ 308 m/s`, frente a `M ≈ 38 MPa` y `c ≈ 145 m/s` con `ν = 0.45`. Es decir, **el paso
de tiempo es más de dos veces menor por el solo hecho de acercarse a la incompresibilidad**.

Esto se registra como diagnóstico, **no como recomendación**: bajar `ν` cambia la respuesta
física y la validación contra la solución de Prandtl. La vía correcta si la
incompresibilidad se vuelve limitante es una formulación mixta u–p, no relajar `ν`.

---

## 6. Vías de aceleración, ordenadas por relación beneficio / riesgo

| # | Intervención | Ganancia esperable | Riesgo numérico | Esfuerzo |
|---|---|---|---|---|
| A | Índice inverso `nodo → índice activo` (O(1)) | 10x – 40x | **Ninguno**: resultados bit a bit idénticos | 1 día |
| B | Estructura CSR de partículas por elemento (elimina `elem_i_mp`) | 2x – 5x | **Ninguno** si se preserva el orden | 1 día |
| C | Escalado de masa | 5x – 20x | Bajo, verificable con `ee` | Horas |
| D | Amortiguamiento adaptativo (reinicio en picos de energía cinética) | 2x – 5x | Bajo | 1–2 días |
| E | `parallel=True` + `prange` sobre partículas | 4x – 8x | Cambia el orden de suma (§4) | 2–3 días |
| F | Solver implícito para etapas cuasi-estáticas | 100x – 1000x | Alto: es otro método | Semanas–meses |
| G | Simetría del problema (medio modelo) | 2x, y 4x en el término O(N²) | Ninguno | 1 día |
| H | Malla graduada (fina bajo la zapata, gruesa lejos) | 2x – 4x | Medio | Semanas |

**A y B son la prioridad evidente.** No cambian ni un bit del resultado —solo sustituyen
búsquedas lineales por consultas directas— y entre las dos plausiblemente llevan las 9
horas a 20–40 minutos. Son, además, exactamente el tipo de cambio que el arnés de
validación ya construido puede verificar de forma concluyente (§9).

Combinando A + B + C + E sin tocar el método, un objetivo realista es **2 a 5 minutos** para
el caso de malla 0.5. La opción F llegaría más lejos pero es un proyecto de investigación
en sí mismo.

### 6.1 Bosquejo de A y B

Ambas estructuras se construyen una vez por ciclo, en O(N), justo después de
`search_MP`, y se pasan dentro de la tupla `grid`:

```python
# A: indice inverso. active_nodes ya viene ordenado de np.unique.
#    nodo_idx[g] = posicion de g en active_nodes, o -1 si no esta activo.
nodo_idx = np.full(len(cor) + 1, -1, dtype=np.int64)
nodo_idx[active_nodes] = np.arange(len(active_nodes))

# B: particulas por elemento en formato CSR, via conteo (counting sort).
#    mp_ini[e]:mp_ini[e+1] indexa mp_lista con las particulas del elemento e.
```

En el cuerpo de las funciones de transferencia, el bloque de las líneas 563-566 y 585-588
se reduce a `nna = nodo_idx[nng]`, y `mpe = elem_i_mp(...)` a un rebanado de `mp_lista`.

**Requisito crítico:** el CSR debe generar las partículas de cada elemento en el **mismo
orden ascendente** que produce hoy `elem_i_mp` (que recorre `mp_elem` de 0 a `nmp`). Un
*counting sort* estable lo garantiza. Si se preserva ese orden, los resultados son
idénticos bit a bit y la equivalencia es demostrable —no argumentable— con `dos_motores.py`.

---

## 7. Lo que *no* es el problema

Conviene dejarlo escrito para no perseguir fantasmas al retomar:

- **No es el MPM.** Su costo por paso es comparable al del FEM.
- **No es Numba ni Python.** Las funciones críticas ya están compiladas con `@njit`. El
  problema es la complejidad algorítmica dentro del código compilado, no el lenguaje.
- **No es el criterio de convergencia.** `static_convergence` es O(N) y se ejecuta una vez
  por ciclo; es despreciable.
- **No es la plasticidad.** El retorno de Mohr-Coulomb es local por partícula, O(N).
- **No es la escritura a disco.** Se guarda una vez por incremento (56 veces en 9 horas).
- **No son los `np.dot` de la rama gaussiana.** Fue la primera hipótesis y quedó descartada
  al hacer la aritmética de §3.3: las búsquedas lineales ya explican el tiempo medido.

---

## 8. Encuadre: cuándo el MPM es la herramienta correcta

Este apartado es el que más valor tiene para la discusión de la tesis, y también el que
responde a la pregunta práctica de si un flujo así sería viable en consultoría.

El valor diferencial del MPM es la **gran deformación**: runout, colapso progresivo,
penetración, geometría post-falla, interacción con el terreno después del fallo. Si la
pregunta es únicamente la carga última `qu`, se está pagando esa capacidad sin usarla.

Para capacidad portante en suelo estratificado, las herramientas adecuadas son:

| Necesidad | Herramienta | Orden de tiempo |
|---|---|---|
| `qu` con factores de corrección | Formulación clásica (Terzaghi, Meyerhof, Vesić) | Instantáneo |
| `qu` con cotas rigurosas superior e inferior | Análisis límite por EF (FELA, p. ej. OptumG2) | Segundos |
| Curva carga-asentamiento, campo de deformaciones | FEM implícito (Plaxis, RS2) | Minutos |
| Qué ocurre **después** de la falla | **MPM** | Horas |

En un flujo de consultoría con 10 variantes de estratigrafía, la respuesta correcta no es
acelerar el MPM: es usar FELA o FEM implícito para el dimensionamiento y reservar el MPM
para los casos donde la pregunta sea la cinemática post-falla. La estrategia que ya se
está aplicando en esta validación —malla gruesa para iterar, malla fina para la entrega
final— es la correcta, pero no cambia esa conclusión de fondo.

Para el caso concreto de esta tesis, el costo es aceptable porque el objetivo es
**verificar que el método reproduce una solución conocida**, no producir un diseño. El
análisis de este documento entra como capítulo de trabajo futuro, no como limitación del
aporte.

---

## 9. Cómo retomar esto: protocolo de validación

La ventaja de haber construido el arnés de validación primero es que las optimizaciones A,
B y G son **demostrables**, no opinables.

1. **Congelar la referencia.** `resultados_referencia/capacidad_portante_malla1.npz`
   (800 partículas, ≈ 1 h) es el oráculo barato. La malla 0.5 es la verificación final.
2. **Optimizar una cosa a la vez**, con un commit por intervención.
3. **Verificar equivalencia bit a bit** con
   [`tools/experimentos/dos_motores.py`](../tools/experimentos/dos_motores.py), que ya
   compara paso a paso dos motores desde un estado inicial idéntico. Para A, B y G el
   criterio de aceptación es diferencia **exactamente `0.000e+00`**; cualquier cosa
   distinta de cero indica que se alteró el orden de suma y hay que averiguar por qué.
4. **Para C, D y E** —que sí cambian los resultados— el criterio pasa a ser
   [`tools/compare_ref.py`](../tools/compare_ref.py) con tolerancia acorde a la tolerancia
   de convergencia (≈ 1 %), más el contraste con Prandtl (`qu = (2+π)·Su = 102.8 kPa`)
   como verificación independiente.
5. **Medir antes de optimizar.** Todo lo anterior sale de leer el código y hacer
   aritmética, no de un *profiler*. Antes de tocar nada, correr `cProfile` o
   `line_profiler` sobre el caso malla 1.0 y confirmar la atribución. Si el perfil no
   señala `elem_i_mp` y el bloque de búsqueda nodal como los dos primeros, este análisis
   está equivocado y hay que rehacerlo.

---

## 10. Pendientes de medición

- [ ] Perfilado real (`cProfile` / `line_profiler`) del caso malla 1.0 para confirmar §3.3.
- [ ] Conteo de ciclos por incremento de la corrida malla 1.0, para descomponer el tiempo
      total en costo-por-ciclo × número-de-ciclos y verificar cómo escala el número de
      ciclos con el refinamiento (§3.4).
- [ ] Verificar si el patrón O(N²) afecta también la rama dinámica sin gauss
      (`particles_to_nodes` / `nodes_to_particle_stress2`), que es la que usa el talud. Las
      11 ocurrencias del bloque de búsqueda nodal sugieren que sí, pero no se ha medido el
      costo de la viga ni del talud.
- [ ] Medir el impacto real del escalado de masa en un caso pequeño antes de proponerlo
      como vía.
