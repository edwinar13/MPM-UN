# Plan Fase B: varios cuerpos con contacto friccional

> **Estado:** B0 terminado el 2026-09-20. B1 y B2 el 2026-09-23. **B3 terminado
> el 2026-09-25**: la falla del talud es idéntica bit a bit a la referencia (§6.4).
> Pendiente: la versión general de `contact2` (N cuerpos, normales calculadas),
> ver [contacto_multicuerpo.md](contacto_multicuerpo.md).
>
> **Pendiente anotado (2026-09-25), sin hacer todavía:** cuando una etapa
> cuasi-estática se corta sin converger (máximo de iteraciones o tiempo), el
> análisis sigue con la siguiente y termina con "Análisis finalizado"; el aviso
> solo queda en la consola. El mensaje final debería decirlo (p. ej. "La etapa 1
> se detuvo sin converger en el incremento 1 de 2, ff = 0.100"). Se vio con el
> talud mini de malla 1.0, que con tolerancia 0.01 no converge (ff se estanca
> en 0.100); con 0.15 converge en 2 s.
>
> **Decisión 2026-09-22:** se va por la **versión general** del contacto (N cuerpos y
> normales calculadas), no por reproducir primero el caso de dos cuerpos. Se trabaja
> sobre copias (`contact2`, `normals2`) sin tocar las originales. El algoritmo, sus
> limitaciones y cada cambio se documentan aparte, para la tesis, en
> [contacto_multicuerpo.md](contacto_multicuerpo.md). Esto reemplaza lo dicho
> abajo sobre "fuera de alcance" para más de dos cuerpos y para `normals()`.
> **Alcance (2026-09-22):** el contacto multicuerpo se valida con los casos de
> referencia (la fase de falla del talud es el que lo usa) y con pruebas
> analíticas. El muro con geomalla **queda congelado**: no entra en esta etapa
> de la tesis. La versión general se mantiene porque la geometría la dibuja el
> usuario, no por el muro.
>
> **Por qué:** sin esto no se puede correr la fase de falla del talud (la referencia
> es de dos cuerpos).

Antecedente: un intento de hacer todo de una vez se revirtió (commit `31b0aaf`).
Este plan lo parte en tres pasos, cada uno con su criterio de aceptación.

---

## 1. Qué hace la referencia

`app/motorMPM/Ejemplos/talud_2021_v2.py :: fase_falla()`. Dos cuerpos
independientes, cada uno con su estado completo (`xp, vp, Vp, Vp0, Mp, rhop,
Prop, Fp, sig, epse, epsp, bp, tp, mp_elem`):

| | Cuerpo 1 (base) | Cuerpo 2 (talud) |
|---|---|---|
| Geometría | franja `y ∈ [0, 0.5]`, todo el ancho | el resto del dominio |
| E / ν | 10e3 kPa / 0.3 | 3.8e3 kPa / 0.3 |
| c / φ / ψ | 200 kPa / 35° / 35° | 20 kPa / 20° / 10° |
| ρ | 2.6 Mg/m³ | 1.8 Mg/m³ |
| **Peso propio** | **`bp = 0`** (no pesa) | `bp_y = −9.81` |
| **Plasticidad** | **0 (elástico)** | 1 (Mohr-Coulomb) |

Parámetros del caso G9: `Mu = 0.268` (fricción entre cuerpos), `alpha = 0.10`
(damping), `tie = 8.0 s`, Courant 0.1, `dt = min(dt_cuerpo1, dt_cuerpo2)`.

### 1.1 Estructura del ciclo de tiempo (l. 616-693)

```
por cada paso t:
  search_MP por cuerpo              → mp_elem_i, active_elem_i
  active_elem  = unión de los dos   → active_nodes del SISTEMA
  particles_to_nodes por cuerpo     → usa la malla activa del SISTEMA
                                       pero el mp_elem de cada cuerpo
  guardar nmomentum_i(t)            (para recalcular fuerzas tras el contacto)
  damping + nmomentum += nforce·dt   por cuerpo
  cantidades del sistema = suma de los dos cuerpos
  contact(body1, body2, nmassS, nmomentumS, mesh, dt, mu)
                                    → devuelve nmomentum_1, nmomentum_2 corregidos
  nforce_i = (nmomentum_i − nmomentum_i(t)) / dt
  BC_Dirichlet_momentum3 por cuerpo
  nodes_to_particle_vel por cuerpo  → xp_i, vp_i, nvel_i
  BC_Dirichlet_vel por cuerpo
  nodes_to_particle_stress2 por cuerpo, con SU flag de plasticidad (0 y 1)
```

Detalles que importan:

- La fase de falla **no usa integración gauss ni partículas de frontera**: es
  `particles_to_nodes` + `nodes_to_particle_stress2`. Por eso el hallazgo de
  `deteccion_particulas_frontera.md` no afecta a esta fase.
- Usa `BC_Dirichlet_momentum3` (no la que ya usa la app): es igual salvo que no
  anula `niforce`/`neforce`, irrelevante aquí porque tras el contacto la fuerza
  se recalcula desde el momentum.
- Los resultados se guardan concatenando `[cuerpo 1 | cuerpo 2]`, que es el mismo
  orden en que la app arma sus arrays por grupo de puntos materiales.

### 1.2 La función `contact()` (`explicit2.py:2521`)

Predictor-corrector de Coulomb sobre las velocidades nodales: detecta nodos
compartidos, separa la velocidad relativa en normal y tangencial, corrige la
normal si los cuerpos se aproximan, y la tangencial según deslice
(`|F_tan| > μ·F_n`) o quede pegado. Devuelve los momentos corregidos.

**Dos limitaciones que hay que tener presentes:**

1. **Las normales están fijas en +y.** La llamada a `normals()` (que las calcula
   por gradiente de masa nodal, `explicit2.py:221`) está comentada y en su lugar
   hace `norm_1[:,1] = 1`. Es válido para un contacto horizontal como la base del
   talud, pero no para una superficie inclinada ni para el muro con geomalla.
2. **Está escrita para exactamente dos cuerpos**, no es `@njit` (numpy puro) y
   usa un `np.where` por nodo activo para mapear índices, que es O(N²) del mismo
   tipo que lo descrito en `rendimiento_y_costo_computacional.md`.

Para reproducir la referencia basta tal cual. Para el muro habrá que activar
`normals()`; queda fuera de este plan y se decide al llegar a ese ejemplo.

---

## 2. Qué tiene hoy la app

`model_execute_analysis.py` es de un solo cuerpo: `initMaterialPoint` (l. 1150)
aplana **todos** los grupos de puntos materiales seleccionados en un solo juego
de arrays, y `_run_one_mpm_step` (l. 355) hace un paso sobre ese juego único.
El orden de las partículas es grupo por grupo, así que las fronteras entre
cuerpos son simples rangos de índices.

Lo que ya sirve sin cambios:

- `MeshBack.nodeSupport()` (l. 78) da el `node_support` que pide `contact()`.
- `_capture_state`/`_inject_state` y los checkpoints: solo hay que extenderlos a
  listas por cuerpo.
- Los arrays de resultados son por partícula: concatenar cuerpos encaja directo.
- El handoff geostático → dinámico (`_handoff`, l. 551) ya pone `vp = 0`.

---

## 3. Decisiones de diseño

### 3.1 Un cuerpo por grupo de puntos materiales, pero **solo si se pide**

Si cada grupo pasara a ser un cuerpo automáticamente, el geostático del talud
(hoy validado como **un** cuerpo con dos materiales) cambiaría de resultado. Por
eso el modo es explícito y **por etapa**:

- `AnalysisStage.multi_body` (clave `MULTICUERPO`, default `False`) →
  comportamiento actual, un solo cuerpo con todos los grupos.
- `True` → cada grupo de puntos materiales seleccionado es un cuerpo, con
  contacto entre ellos.

Así el talud queda: etapa 1 geostática mono-cuerpo (idéntica a la validada),
etapa 2 dinámica multi-cuerpo.

### 3.2 Fricción por etapa

`AnalysisStage.friction` (clave `FRICCION`, default 0.0), visible en el diálogo
solo cuando `multi_body` está activo. Es el `mu` de `contact()`.

### 3.3 Plasticidad y peso propio **por cuerpo** — *decidido (2026-09-23)*

> **Plasticidad: decidido 2026-09-23.** El material gana un campo "Modelo"
> (Elástico lineal / Mohr-Coulomb). Una partícula plastifica si su material es
> Mohr-Coulomb **y** la etapa tiene la plasticidad activa. Cada interruptor tiene
> un solo significado: el material dice si *puede* plastificar, la etapa si se
> *permite ahora*. Reproduce la referencia (base elástica, talud M-C en la falla).
> La propuesta original de abajo (`PLASTICIDAD` por grupo) queda descartada.
>
> **Peso propio: resuelto con experimento (2026-09-22), no se agrega campo.**
> `tools/experimentos/peso_base.py` corre la falla de referencia 8 s con la base
> sin peso (como el script) y con peso. Runout 14.83 m frente a 14.92 m (+0.6 %),
> cresta +0.5 %, la base se mueve 7.6 mm en ambos. Además, en el geostático la
> base sí pesa: quitarle el peso en la falla es la opción menos consistente. La
> app deja que todos los cuerpos pesen, y la validación de B3 se hace contra la
> variante con peso (script de referencia con esa línea cambiada y documentada).

La referencia necesita, en la misma etapa, el cuerpo 1 elástico y sin peso
propio, y el cuerpo 2 elastoplástico con gravedad. Hoy ambas cosas son globales
(la plasticidad por etapa, la gravedad por proyecto). Propuesta: dos campos
opcionales en el grupo de puntos materiales (`PUNTOSMATERIAL.<grupo>`):

- `PLASTICIDAD`: `null` = usar la de la etapa; `0`/`1` = forzar.
- `PESOPROPIO`: `true` por defecto; `false` = ese cuerpo no recibe gravedad.

Van en el grupo y no en la etapa porque describen el material/cuerpo, no el
momento del análisis. **A confirmar contigo antes de implementar B3**: es la
única parte del plan que agrega campos visibles al usuario.

### 3.4 dt

`dt = min` sobre todos los cuerpos, que es lo que ya hace `_prepare_stage_time`
al calcularlo sobre todos los materiales presentes. Sin cambios.

---

## 4. Pasos

### B1 — Reestructurar a "lista de cuerpos", sin contacto

Convertir el estado de la app en una lista de cuerpos y hacer que el ciclo
recorra esa lista. Con **un solo** cuerpo en la lista, todo debe dar igual.

- `initMaterialPoint` guarda además los rangos de índice de cada grupo.
- Nueva clase o dict `Body` con sus arrays; `self.__bodies = [body]`.
- `_run_one_mpm_step` pasa a `_run_one_mpm_step(bodies, ...)`, recorriendo la
  lista; con un cuerpo hace exactamente las mismas operaciones y en el mismo
  orden que hoy.
- `_capture_state`/`_inject_state`/checkpoints: por cuerpo.
- Resultados: concatenar en el orden de los cuerpos (ya coincide con el actual).

**Aceptación:** los tres smokes (viga, capacidad portante reducido
geostático→carga, talud mini geostático→dinámico) a **0.000e+00** contra la
línea base guardada. Es el mismo criterio que usamos en el PASO 6 y en cargas.

### B2 — Contacto entre dos cuerpos

- Importar `contact` y `BC_Dirichlet_momentum3` en el ejecutor.
- En el ciclo dinámico, si `multi_body` y hay ≥2 cuerpos: cantidades del sistema,
  `contact()`, recálculo de fuerzas y `BC_Dirichlet_momentum3` por cuerpo, tal
  como la referencia.
- Plasticidad por cuerpo en `nodes_to_particle_stress2`.

**Aceptación:** experimento `tools/experimentos/dos_cuerpos.py`, con el mismo
espíritu que `dos_motores.py`: arma el mismo estado inicial de dos cuerpos,
corre N pasos con el ciclo de la app y N pasos con el ciclo de la referencia
copiado, y compara **bit a bit**. Es más barato y más concluyente que comparar
corridas completas, porque elimina el ruido de arranque.

### B3 — Interfaz y corrida completa

- Diálogo de etapas: casilla "Varios cuerpos con contacto" + campo de fricción.
- Panel de Punto Material: los dos campos de §3.3 (previa confirmación).
- Proyecto de talud con los dos grupos (ya existe
  `4_talud_elastoplastico full 10 pasos - particulas igual a V1.json`, con las
  partículas iguales a las de V1).
- Correr la referencia `fase_falla()` (caso G9, `Mu = 0.268`, 8 s) y la app,
  y comparar con `tools/compare_ref.py`.

**Costo de la corrida completa (medido 2026-09-22):** el dt lo fija la base
(`E = 10e3`, `ρ = 2.6`): `dt ≈ 6e-4 s`, 8 s son ~13 400 pasos. Con el motor de
referencia cuesta ~0.45 s por paso (el contacto sin Numba pesa), o sea **~100
minutos**. La estimación anterior de 15-25 min estaba mal. Antes de lanzarla,
una prueba corta (0.05 s) contra la referencia.

---

## 5. Riesgos

| Riesgo | Mitigación |
|---|---|
| B1 cambia resultados sin querer | Criterio 0.000e+00 en los tres smokes, antes de seguir |
| `contact()` es O(N²) y no `@njit` | Solo se llama una vez por paso; medir en B2 y, si pesa, optimizar el mapeo de índices (sin cambiar resultados) |
| Normales fijas en +y | Sirve para el talud; para el muro habrá que activar `normals()`. Documentado, fuera de alcance |
| Los dos cuerpos comparten nodos y el contacto no detecta bien | El propio `contact()` avisa ("diferentes nodos en contacto"); vigilar ese mensaje en B2 |
| Campos nuevos en la UI (§3.3) | Confirmar contigo antes de B3 |

---

## 6. Ejecución

### 6.1 B1 — cuerpos como rangos (2026-09-23)

No hizo falta una clase `Body` ni partir el estado: los arrays de partículas
siguen siendo uno solo (ya estaban ordenados grupo por grupo) y un cuerpo es un
rango `[start, end)` de ellos (`self.__bodies`, armado en `initMaterialPoint`).
Checkpoints, handoff y resultados no cambian. El paso mono-cuerpo solo cambió en
el punto 6: si los cuerpos tienen distinto flag de plasticidad, `stress2` se
llama por cuerpo (actualiza cada partícula por separado, así que da lo mismo que
una sola llamada).

Campos nuevos: etapa `MULTICUERPO` / `FRICCION`; material `MODELO`
(`MOHR_COULOMB` por defecto, `ELASTICO`; aún sin interfaz, el smoke lo fija con
`--elastico`). Todas las etapas se validan antes de correr la primera.

**Aceptación:** viga, capacidad portante (geostático → carga) y talud mini
(geostático → dinámico) contra la línea base: **0.000e+00** los tres.

### 6.2 B2 — contacto (2026-09-23)

`_run_one_mpm_step_multibody`: el ciclo de `fase_falla()` con vistas por cuerpo
y `contact2`. Por ahora exactamente 2 cuerpos (la generalización a N es trabajo
de `contact2`, ver [contacto_multicuerpo.md](contacto_multicuerpo.md)).

**Aceptación:** `tools/experimentos/dos_cuerpos.py`, bit a bit contra el ciclo de
la referencia con el motor original: **0.000e+00** en talud mini (100 pasos) y
talud completo (50 pasos).

### 6.3 Hallazgo para B3: la referencia cambia de material y de estado entre fases

Comparando el proyecto de la app con el script:

| | Geostático (script) | Falla (script) | Proyecto de la app |
|---|---|---|---|
| E base / talud (kPa) | 15e3 / 15e3 | 10e3 / 3.8e3 | 15e3 / 15e3 |
| c talud (kPa) | 5 | 20 | 5 |
| φ / ψ talud | 35° / 35° | 20° / 10° | 35° / 35° |

Además, la falla **no hereda** posiciones, `Fp`, `epse` ni `epsp` del geostático:
recrea las partículas en su posición inicial y solo toma `sig`. La app hoy
hereda todo y tiene un material fijo por grupo.

**Decidido 2026-09-24** (como en el software comercial):

1. **Material por etapa.** El grupo se arma con un material, y cada etapa puede
   cambiárselo (`CAMBIOMATERIAL = {id_grupo: id_material}`). El cambio persiste
   en las etapas siguientes hasta que otra lo cambie; al reanudar se recalcula
   desde las etapas anteriores. Al cambiar: `Prop` nueva (columna 5 en cero) y
   `Mp = rho·Vp0`, igual que la falla de la referencia.
2. **Reiniciar deformaciones, opcional por etapa** (`REINICIARDEFORMACIONES`):
   `Fp = I`, `epse = epsp = 0`, `Vp = Vp0`. Se conservan esfuerzos y
   **posiciones**: devolver las partículas a su sitio inicial, como hace el
   script, descarta el asentamiento del geostático, que en este talud llega a
   **0.40 m**.
3. Material: campo "Modelo" (Mohr-Coulomb / Elástico) en el panel y la tarjeta
   de materiales.

Para validar se usa `talud_2021_falla_app.py` (carpeta de la referencia): copia
de `talud_2021.py` con cambios marcados, que arranca la falla desde las
posiciones del geostático y con la base con peso.

### 6.4 B3 — falla completa, 8 s (2026-09-25)

App: proyecto del talud completo (6740 partículas) con los materiales de la
falla agregados, reanudando desde el checkpoint geostático; etapa dinámica 8 s,
Courant 0.1, damping 0.10, contacto μ = 0.268, reiniciar deformaciones, cambio
de material (base elástica). dt = 6.0e-4 s en ambos, 13 334 pasos, 162 frames,
~75 min cada corrida.

**(a) Contra la referencia desde SU geostático** (`geostatic_state_v2.npz`):

| t (s) | runout del pie ref / app (m) | desplazamiento medio talud ref / app (m) |
|---|---|---|
| 1 | 2.29 / 2.28 | 1.11 / 1.10 |
| 4 | 11.22 / 11.50 | 5.28 / 5.31 |
| 8 | **13.57 / 13.76 (+1.4 %)** | **6.13 / 6.15 (+0.3 %)** |

Los dos arrancan de geostáticos que ya difieren en t = 0 (1e-4 m en posición,
3.7 kPa en σyy: la tolerancia con que se validó el geostático). El flujo
amplifica esa diferencia; partícula a partícula llega a 0.7 m (media 0.07 m).

**(b) Contra la referencia desde el geostático DE LA APP** (mismo estado de
entrada; malla, contornos y volúmenes verificados idénticos):
`talud_2021_falla_app.py <geo.npz> _geo_app`, con `sig` y `xp` del checkpoint de
la app. **0.000e+00 en los 18 campos y los 162 frames, durante los 8 s.**

Conclusión: la fase de falla de la app (contacto, cambio de material, reinicio
de deformaciones, handoff y guardado de resultados) es idéntica a la de la
referencia. El 1.4 % de (a) viene entero de la diferencia entre los dos
geostáticos, ya documentada en la validación del geostático.

---

## 7. Fuera de alcance

- Más de dos cuerpos (la función de la referencia es para dos; generalizar
  después, si el muro lo pide).
- Normales por gradiente de masa (`normals()`).
- Contacto en etapas cuasi-estáticas: la referencia solo lo usa en la dinámica.
