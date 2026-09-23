# Contacto entre cuerpos: del algoritmo original a la versión general

> **Material para la tesis.** Documenta el algoritmo de contacto friccional del
> código original (`contact()`), las limitaciones que se encontraron al revisarlo,
> y la versión general que implementa la aplicación (`contact2()` y `normals2()`):
> qué cambia, por qué y cómo se valida cada cambio.
>
> Documentos hermanos: [plan_fase_b.md](plan_fase_b.md) (plan de trabajo),
> [deteccion_particulas_frontera.md](deteccion_particulas_frontera.md) (mismo
> método: función nueva junto a la original, validada contra ella) y
> [validacion_motor_vs_referencia.md](validacion_motor_vs_referencia.md).

Inicio: 2026-09-22. Estado: **copia de partida hecha; versión general pendiente**
(ver §6, registro de cambios).

---

## 1. Para qué hace falta el contacto

En el MPM, las partículas transfieren masa y momentum a los nodos de la malla de
fondo, y la ecuación de movimiento se resuelve en los nodos. Lo que decide cómo
interactúan dos materiales es **cuántos campos de velocidad** hay en los nodos
que comparten:

| | Un solo campo de velocidad | Un campo por cuerpo + contacto |
|---|---|---|
| En un nodo compartido | una única velocidad para todo | una velocidad por cuerpo |
| Comportamiento de la interfaz | **adherida**: no desliza ni se separa | **friccional**: desliza o se pega según Coulomb, y se puede separar |
| Equivale a | fricción infinita, sin despegue | fricción μ, sin tracción |

Un solo campo no significa "sin contacto", sino contacto rígido. Por eso la
elección es de modelado y depende de la etapa:

- **Geostático de un talud**: interesa establecer el estado inicial de
  esfuerzos sin movimientos relativos espurios entre materiales. Interfaz
  adherida (un solo campo).
- **Falla del talud**: el fenómeno a estudiar es el deslizamiento sobre la base.
  Interfaz friccional.
- **Refuerzos o muros** (ejemplo ilustrativo; no se modela en esta tesis): la
  interacción suelo-refuerzo es friccional desde el inicio del problema.

---

## 2. El algoritmo original: `contact()`

[`explicit2.py:2521`](../app/motorMPM/explicit2.py#L2521). Se usa en la fase de
falla de `talud_2021_v2.py` (l. 652-665), en `Disc.py` y en
`Collapse_contact.py`, siempre con dos cuerpos.

### 2.1 Dónde entra en el paso de tiempo

```
1. particles_to_nodes por cuerpo            → m_i^b, p_i^b, fuerzas nodales
2. guardar p_i^b(t)
3. p_i^b += (f_int + f_ext + amortiguamiento)·Δt       (predictor, por cuerpo)
4. campo del sistema: m_i^S = Σ_b m_i^b,  p_i^S = Σ_b p_i^b
5. contact(...)                              → p_i^b corregido     (corrector)
6. f_i^b = (p_i^b − p_i^b(t)) / Δt           (fuerza consistente con la corrección)
7. condiciones de Dirichlet, nodos → partículas, esfuerzos, por cuerpo
```

### 2.2 Qué hace `contact()` en cada nodo

La formulación es **cada cuerpo contra el campo del sistema** (centro de masa),
no cuerpo contra cuerpo. Con `v^b = p^b/m^b` y `v^S = p^S/m^S`:

1. **Nodos de contacto**: aquellos donde `|v^b − v^S| > 1e-10`, es decir, donde
   hay otro cuerpo con masa en el mismo nodo.
2. **Velocidad normal relativa**: `v_n = (v^b − v^S)·n^b`, con `n^b` la normal
   hacia afuera del cuerpo `b`. Si `v_n > 0` los cuerpos se aproximan; si no, se
   separan y no se corrige nada.
3. **Corrección normal** (impide la interpenetración):
   `v^b ← v^b − v_n·n^b`.
4. **Velocidad tangencial relativa**: `v_t = (v^b − v^S) − v_n·n^b`.
5. **Criterio de Coulomb**: fuerza tangencial de prueba `F_t = m^b·|v_t|/Δt`
   contra el límite `μ·F_n = μ·m^b·v_n/Δt`.
   - Si `F_t > μ·F_n`, **desliza**: `v^b ← v^b − μ·v_n·t̂`, con `t̂ = v_t/|v_t|`.
   - Si no, **se pega**: `v^b ← v^b − v_t` (el cuerpo queda con la velocidad del
     sistema).
6. Devuelve `p^b = m^b·v^b` corregido.

---

## 3. Lo que se encontró al revisarlo

### 3.1 Las normales están fijas en +y

```python
#norm_1 = normals(ncontac_1G, node_support, active_elem_1, mp_elem_1, inci, cor, Mp_1, xp_1)
norm_1 = np.zeros((len(ncontac_1G),2))
norm_1[:,1] = 1
```

La normal es la misma, vertical, en todos los nodos de contacto. Es correcta para
el talud de referencia, donde el único contacto es la cara superior horizontal de
la base. En un contacto inclinado, la corrección normal (paso 3) solo quita la
componente vertical: el cuerpo se interpenetra en la dirección real de contacto
y la fricción (paso 5) se aplica sobre un plano que no es el de la interfaz.
**Con geometría arbitraria, esto no sirve.**

### 3.2 `normals()` existe, pero nunca se usó

[`explicit2.py:221`](../app/motorMPM/explicit2.py#L221) calcula la normal por el
método del gradiente de masa nodal:

```
∇m_i^b = Σ_p M_p ∇N_i(x_p)        (sobre las partículas del cuerpo b)
n_i^b  = ∇m_i^b / |∇m_i^b|
```

Sin embargo, **ningún script del repositorio la usa**: la llamada está comentada
en las dos ramas de `contact()` y no aparece activa en ningún ejemplo. Además
tiene un problema que explica por qué se desactivó: la normalización final

```python
normal = np.divide(nor, np.transpose(magnitud))
```

no protege contra magnitud cero, así que devuelve **NaN**, que se propagaría a
las velocidades. Los mensajes de diagnóstico que quedaron comentados dentro de la
función ("Magnitudes normales igual a cero", "vector de normales unitario con
NaN") son el rastro de ese problema.

Activarla no es descomentar una línea: es poner en servicio código que nunca se
ejecutó, corregirlo y validarlo.

### 3.3 Dos cuerpos por duplicación, y por qué `norm_2 = −norm_1`

La matemática (cada cuerpo contra el sistema) vale para N cuerpos, pero el código
tiene el mismo bloque copiado dos veces. La única línea propia de dos cuerpos es

```python
norm_2 = - norm_1 # garantizar colinealidad de las normales
```

Esa línea no es solo un atajo: es lo que hace que **el contacto conserve el
momentum**. En un nodo compartido por dos cuerpos, la definición de `v^S` da

```
q ≡ m^1·(v^1 − v^S) = −m^2·(v^2 − v^S)
```

y las correcciones normales de momentum son

```
Δp^1 = −(q·n^1)·n^1          Δp^2 = +(q·n^2)·n^2
```

Su suma es cero para cualquier `q` **solo si `n^2 = −n^1`**. Con normales opuestas
también coinciden los criterios de aproximación de ambos cuerpos (los dos ven
`q·n^1 > 0`), y la corrección tangencial se cancela del mismo modo. Si cada cuerpo
calculara su normal por separado, con el ruido propio del MPM, las normales no
serían exactamente opuestas: el contacto crearía o destruiría momentum, y podría
pasar que un cuerpo "se aproxime" mientras el otro "se separa".

Consecuencia para la versión general: **no basta con calcular la normal de cada
cuerpo**; hay que usar una normal común por par de cuerpos en cada nodo.

### 3.4 Costo

`contact()` no está acelerada con Numba y mapea índices con un `np.where` por nodo
activo, que es O(N²), el mismo patrón descrito en
[rendimiento_y_costo_computacional.md](rendimiento_y_costo_computacional.md).
Se llama una vez por paso, así que se medirá antes de decidir si hay que
optimizarla.

---

## 4. La versión general: `contact2()` y `normals2()`

### 4.1 Punto de partida

Se tomó una **copia literal** de `normals()` y `contact()` al final de
`explicit2.py`, con los nombres `normals2()` y `contact2()`. Las originales no se
modifican: siguen siendo la referencia contra la que se valida, igual que
`boundary_particles2` frente a `boundary_particles3` y `talud_2021.py` frente a
`talud_2021_2pasos.py`.

La copia se hizo leyendo el texto de las funciones del propio archivo, no
reescribiéndolas, y se verificó que el código fuente de cada copia es idéntico
al original salvo el nombre (ver §6).

### 4.2 Cambios previstos

| # | Cambio | Motivo |
|---|---|---|
| 1 | Recorrer N cuerpos en vez de dos bloques duplicados | Geometrías con más de dos materiales que deslizan |
| 2 | Normal calculada por gradiente de masa (`normals2`) | Contactos no horizontales (§3.1) |
| 3 | Normal común por par de cuerpos en cada nodo | Conservar el momentum (§3.3) |
| 4 | Protección contra `|∇m| = 0` | Evitar NaN (§3.2) |
| 5 | Modo de compatibilidad: dos cuerpos y normal fija +y | Reproducir `contact()` bit a bit para validar |

Sobre el cambio 3: la opción natural para dos cuerpos es construir la normal con
los gradientes de ambos, `n = (∇m^1 − ∇m^2)/|∇m^1 − ∇m^2|`, y usar `n` para el
cuerpo 1 y `−n` para el 2. Más de dos cuerpos en un **mismo** nodo es un caso de
esquina (tres materiales que se tocan en un punto) que se tratará aparte. La
decisión final se toma con la prueba de conservación de §5.

---

## 5. Cómo se va a validar

| Prueba | Qué demuestra | Criterio |
|---|---|---|
| `contact2` en modo compatibilidad contra `contact` (experimento `tools/experimentos/dos_cuerpos.py`, mismo estado de entrada) | La reescritura a N cuerpos no cambió el algoritmo | **0.000e+00** |
| Conservación de momentum en cada paso | Las normales comunes funcionan | `Σ_b Δp^b = 0` a precisión de máquina |
| Bloque sobre plano inclinado con fricción μ | Normales no horizontales + Coulomb | Si `tan θ > μ`: `a = g·(sen θ − μ·cos θ)`; si no, reposo |
| Fase de falla del talud contra `talud_2021_v2.py` | El caso completo de la tesis | Comparación con `compare_ref.py` |

El plano inclinado tiene solución analítica, así que valida las normales
calculadas sin depender del código de referencia, que nunca las usó.

---

## 6. Registro de cambios

| Fecha | Cambio en `contact2` / `normals2` | Verificación |
|---|---|---|
| 2026-09-22 | Copia literal de `contact` / `normals` (solo cambia el nombre). 209 líneas agregadas al final de `explicit2.py`, ninguna línea existente modificada | Fuente idéntica salvo el nombre (`inspect.getsource`); smoke de la viga contra la línea base: **0.000e+00** |

---

## 7. Qué afirmar en la tesis

*(Se completa al terminar la validación.)*
