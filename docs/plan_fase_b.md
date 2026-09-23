# Plan Fase B: varios cuerpos con contacto friccional

> **Estado:** B0 (estudio y diseño) terminado el 2026-09-20. B1 en adelante, pendientes.
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

### 3.3 Plasticidad y peso propio **por cuerpo** — *en discusión (2026-09-22)*

> Propuesta revisada, pendiente de confirmar: la plasticidad se toma del
> **material** ("¿puede plastificar?") combinada con la de la **etapa** ("¿se
> permite ahora?"). Lo de abajo es la propuesta original.
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

## 6. Fuera de alcance

- Más de dos cuerpos (la función de la referencia es para dos; generalizar
  después, si el muro lo pide).
- Normales por gradiente de masa (`normals()`).
- Contacto en etapas cuasi-estáticas: la referencia solo lo usa en la dinámica.
