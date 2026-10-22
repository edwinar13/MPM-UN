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

Inicio: 2026-09-22. **Cerrado el 2026-09-26.** La app usa la normal vertical
(`'fija_y'`, contactos horizontales), idéntica a la referencia. Las normales
calculadas quedaron implementadas y probadas, pero **no se usan**: fallan en
superficies inclinadas (ver el hallazgo del 2026-09-26 al final de §6 y §7).

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
| 2026-09-23 | `contact2` (aún igual a `contact`) conectado al ejecutor: `_run_one_mpm_step_multibody`, con cada cuerpo como un rango de los arrays de partículas | `tools/experimentos/dos_cuerpos.py`: N pasos de la app frente al ciclo de `fase_falla()` con el motor original, mismo estado de entrada (geostático). Talud mini (221 part., 100 pasos) y talud completo (6740 part., 50 pasos): **0.000e+00** en `xp, vp, Vp, Fp, sig, epse, epsp, mp_elem`, con movimiento y plastificación reales |
| 2026-09-25 | Sin cambios en `contact2`; corrida completa de la falla del talud (8 s, 13 334 pasos) desde la app | Contra `talud_2021_falla_app.py` arrancando del mismo geostático: **0.000e+00** en los 18 campos y 162 frames (ver plan_fase_b.md §6.4) |
| 2026-09-26 | **Paso 1 (cambios 1 y 5 de §4.2).** `contact2(bodies, nmassS, nmomentumS, mesh, dt, miu, normales='fija_y')`: recibe una **lista** de cuerpos; el bloque duplicado de `contact()` pasa a una sola función `_contact_correct()` que se aplica a cada cuerpo, con las mismas operaciones en el mismo orden. Modo `'fija_y'` = el de `contact()` (2 cuerpos, normal +y y su opuesta). Dos cambios de costo sin efecto en los números: el índice de cada nodo con `np.searchsorted` en vez de un `np.where` por nodo (mismo resultado porque `active_nodes` sale ordenado de `np.unique`), y `(v − vS)·n` fila a fila en vez de la diagonal de un producto N×N | `dos_cuerpos.py`: talud mini (100 pasos) y completo (50 pasos) **0.000e+00**. `contact` frente a `contact2` sobre el mismo estado con velocidades perturbadas al azar: **0.000e+00**, y 44 ms → 0.7 ms por llamada (6740 partículas). Falla completa del talud (8 s) con `contact2` nueva frente a la corrida anterior (idéntica a la referencia): **0.000e+00** en todos los campos y frames |
| 2026-09-26 | **Pasos 2 y 3.** `mass_gradient2()` (Numba, recorre las partículas una vez; reemplaza la copia de `normals()`) y modo `'gradiente'`: normal del par `d = g₁ − g₂`, la del otro cuerpo exactamente `−d`, normal nula si `|d| = 0`. Ojo con el signo: `g = Σ Mp ∇N_i(x_p)` apunta **hacia afuera** del cuerpo (en un nodo de borde las partículas quedan de un lado y ∇N_i apunta hacia el nodo), no hacia adentro. También se admite una normal constante `(nx, ny)` para pruebas | Talud: normales a 0.01° de +y en la interfaz (salvo el borde x = 0 y el pie x = 18, 8° y 15°); momentum conservado (suma de correcciones ~1e-19). `'fija_y'` sigue a 0.000e+00. **Plano inclinado** (`tools/experimentos/plano_inclinado.py`, θ = 30°, μ = 0.2, geostático previo): con la **normal exacta** a = 3.206 m/s², igual a la teórica 3.206, y avance 2.308 m igual al teórico → el algoritmo de Coulomb es correcto. Con la normal **por gradiente** el bloque **no desliza** (a ≈ 0): en los 11 nodos de contacto el error de la normal tiene mediana 6° y máximos de 28–42° (escalera de la rampa y esquinas del bloque), y esos nodos frenan el deslizamiento. Suavizar o usar un solo cuerpo baja el máximo a ~15°, insuficiente |

### Hallazgo 2026-09-26: la normal por gradiente de masa no sirve en superficies inclinadas a esta resolución

El algoritmo de contacto es exacto si la normal es correcta (prueba anterior).
El gradiente de masa nodal da normales con errores de 15–40° en superficies que
no están alineadas con la malla: la superficie de partículas es una escalera y
en las esquinas de un cuerpo el gradiente apunta de lado. Un nodo con la normal
girada δ lee el deslizamiento como aproximación y le quita la componente
sen δ en cada paso: con δ ≈ 15° eso frena el cuerpo por completo. En la
interfaz horizontal del talud no se nota porque ahí la escalera no existe.

---

### Decisión 2026-09-26

- La app usa **solo la normal vertical**: contactos horizontales, como el talud
  de la tesis. Es lo mismo que hace todo el código original: `talud_2021_v2.py`,
  `Collapse_contact.py` (columna granular sobre una placa) y `Disc.py` (disco
  sobre un plano inclinado, simulado **girando la gravedad** con la placa
  horizontal) usan `contact()` con la normal fija en +y.
- Se conservan en el motor, sin interfaz: `contact2` para una lista de cuerpos,
  el modo `'gradiente'`, `mass_gradient2` y la normal constante `(nx, ny)`. El
  ejecutor sigue limitado a 2 cuerpos (el modo vertical es de dos).
- `tools/experimentos/plano_inclinado.py` reproduce el hallazgo.
- **Trabajo futuro** (otra tesis): normales a partir de la geometría de la
  superficie (p. ej. un ajuste local por las partículas de borde) en vez del
  gradiente de masa, validadas con este mismo plano inclinado.
- **Extras, solo si queda tiempo al final** (en orden): `Disc.py` como
  validación analítica del contacto (requiere gravedad con ángulo en el
  proyecto e importar las partículas del disco; ~1-2 días), y
  `Collapse_contact.py` (misma estructura que el talud; solo armar el proyecto).

## 7. Qué afirmar en la tesis

1. La fase de falla del talud con dos cuerpos y contacto friccional es idéntica
   bit a bit a la referencia en 8 s de simulación, arrancando del mismo
   geostático (plan_fase_b.md §6.4).
2. El algoritmo de contacto de Coulomb es exacto cuando la normal es correcta:
   bloque sobre plano inclinado, aceleración y avance iguales a la solución
   analítica a tres cifras.
3. La normal por gradiente de masa nodal no es confiable en superficies
   inclinadas respecto a la malla: errores de 15–40° que traban el
   deslizamiento. Por eso la aplicación se limita a contactos horizontales, como
   el código original, y se deja como trabajo futuro.
