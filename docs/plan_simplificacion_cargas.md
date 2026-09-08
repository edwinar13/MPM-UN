# Plan: simplificación de la definición de cargas

> **Estado:** pendiente. Ejecutar **después** de validar el ejemplo de capacidad
> portante contra `Ca_portante2.py` con el esquema actual.
> **Fecha de acuerdo:** 2026-07-29

---

## 1. Objetivo

Hoy la magnitud de una carga externa está repartida en **tres** números que se
multiplican entre sí. Este plan la deja en **uno solo**: la fuerza por partícula.

| | Hoy | Después |
|---|---|---|
| Panel Punto Material | `Fy` = semilla de referencia | **`Fy` = fuerza final por partícula [kN]** |
| Diálogo de etapas | `Δ carga por incremento` | *(eliminado)* |
| Diálogo de etapas | `N.º de incrementos` | `N.º de incrementos` (solo divide) |

Regla única resultante:

> **`Fy` es la fuerza total que llega a esa partícula.
> `nincre` solo dice en cuántos pasos se llega a ella.**

---

## 2. Estado actual (verificado en código)

### 2.1 Cadena de multiplicación

`Fy` se lee en [model_execute_analysis.py:1197-1200](../app/models/model_execute_analysis.py#L1197-L1200)
y se guarda en `self.__vm_tp0`. Luego:

| Tipo de etapa | Qué se aplica | Dónde |
|---|---|---|
| `LOAD_INCREMENT` | `tp = (i+1) · dincre · tp0` | [:730](../app/models/model_execute_analysis.py#L730) |
| `GEOSTATIC` | `dincre` forzado a `0.0` → **`tp = 0`** | [:678-681](../app/models/model_execute_analysis.py#L678-L681) |
| `DYNAMIC` | `tp = tp0` (100 %, instantáneo) | [:590](../app/models/model_execute_analysis.py#L590) |

**El problema:** el mismo campo `Fy` significa cosas distintas según la etapa.
En dinámica es la fuerza real; en incrementos de carga es una semilla que hay que
multiplicar mentalmente por `dincre × nincre`.

### 2.2 Unidades (para el texto de ayuda)

De [explicit2.py:362-363](../app/motorMPM/explicit2.py#L362-L363):

```python
neforce[nna,0] += Np[0,k]*Mp[mp-1]*bp[mp-1,0]  +  Np[0,k]*tp[mp-1,0]
#                 └──── gravedad: Mg·m/s² = kN ──┘   └── Np·tp ⇒ tp en kN ──┘
```

> **`tp` (es decir `Fx`/`Fy`) es una FUERZA en kN por metro de espesor**, no un esfuerzo.

Conversión desde una presión, tal como la hace
[mesh.py:507-515](../app/motorMPM/mesh.py#L507-L515):

```
F = q · L / n      q = presión [kPa]   L = longitud del tramo [m]   n = n.º partículas
```

Sistema de unidades del programa: **kN, kPa, m, Mg, s** (la densidad se convierte a
Mg/m³ en [model_execute_analysis.py:1119](../app/models/model_execute_analysis.py#L1119)).

---

## 3. Decisiones tomadas

### 3.1 Aceptadas

- **`Fy` = fuerza final por partícula.** Un solo número, mismo significado en toda etapa.
- **Se elimina `Δ carga por incremento` (`dincre`).** El multiplicador pasa a ser
  `(i+1)/nincre`: rampa de 0 a 100 %.
- **La conversión esfuerzo → fuerza la hace el usuario**, ayudado por un texto en el panel.

### 3.2 Descartadas (y por qué)

- **Entrada por esfuerzo (kPa) en la UI.** Descartada porque la herramienta de
  selección permite escoger partículas dispersas o interiores, donde una presión
  no tiene significado físico y cualquier longitud `L` calculada automáticamente
  sería una adivinanza silenciosamente incorrecta.
- **Independencia de malla.** No aporta: al re-mallar se destruye el grupo de
  puntos materiales con sus cargas, así que hay que reasignar de todos modos.

### 3.3 Corrección sobre la etapa geostática

Quitar `dincre` **no** resuelve por sí solo el que la geostática ignore las fuerzas.
De hecho, el comportamiento **debe conservarse**: en un flujo de 2 etapas
(geostática → carga) las fuerzas se asignan una sola vez a las partículas y
persisten; si la geostática también las rampara, la carga de la zapata ya estaría
aplicada durante el estado inicial, que es justo lo que no se quiere.

> **Decisión:** la etapa geostática sigue aplicando **solo peso propio**.
> Lo que cambia es que deja de ser silencioso: se avisa en la UI.

### 3.4 Etapa dinámica

No requiere cambios. `tp = tp0` al 100 % ya es el comportamiento correcto bajo el
nuevo esquema, y `VISIBLE_FIELDS` en [view_DialogStages.py](../app/views/view_DialogStages.py)
ya oculta `nincre` y `dincre` para `dynamic` (solo muestra `tiempo`).

---

## 4. Cambios a implementar

### PASO 1 — Bucle cuasi-estático

[model_execute_analysis.py:678-685](../app/models/model_execute_analysis.py#L678-L685):

```python
# ANTES
if stage.stage_type == StageType.GEOSTATIC:
    dincre = 0.0
    dincreGrav = 1.0 / nincre
else:  # LOAD_INCREMENT
    dincre = stage.load_increment_value
    dincreGrav = stage.gravity_increment_value

# DESPUÉS
if stage.stage_type == StageType.GEOSTATIC:
    load_step = 0.0              # geostática: solo peso propio
    dincreGrav = 1.0 / nincre
else:  # LOAD_INCREMENT
    load_step = 1.0 / nincre     # rampa 0 → 100 % de tp0
    dincreGrav = stage.gravity_increment_value
```

[model_execute_analysis.py:730](../app/models/model_execute_analysis.py#L730):

```python
# ANTES
self.__vm_tp_current = (i + 1) * dincre * self.__vm_tp0
# DESPUÉS
self.__vm_tp_current = (i + 1) * load_step * self.__vm_tp0
```

`charge` (línea 685) es solo para etiquetas de gráfica; recalcularlo como
`-np.linspace(0, 1, nincre+1)` o dejarlo en función de la carga total.

### PASO 2 — Modelo de datos

En [model_analysis_config.py](../app/models/model_analysis_config.py):

- Eliminar `load_increment_value` de `AnalysisStage` y de `to_dict()`.
- En `from_dict()`: dejar de leer `DELTAINCREMENTO` (o leerlo solo si se
  implementa la migración automática del PASO 5).

Clave JSON `DELTAINCREMENTO` deja de escribirse. `NUMEROINCREMENTOS` se conserva.

### PASO 3 — Diálogo de etapas

En [view_DialogStages.py](../app/views/view_DialogStages.py):

- Quitar `spDincre` y su fila (líneas ~321, 442-443, 475-476, 495-496, 219-221).
- Quitar `"dincre"` de `VISIBLE_FIELDS["load_increment"]` y de la tupla de
  `_apply_type_visibility` (línea 505).
- Quitar `DELTAINCREMENTO` de los defaults por tipo (líneas ~42-46).
- **Agregar nota** en la etapa geostática:

  > *Esta etapa aplica únicamente peso propio. Las fuerzas asignadas a las
  > partículas no se usan aquí.*

### PASO 4 — Ayuda en el panel de Punto Material

`widget_draw_menu_pointMaterial.ui` — sección *«Asignar fuerzas y velocidades»*.
Un `QToolButton` con ícono de ayuda que abra un `QMessageBox`, o un `QLabel` gris
pequeño bajo los campos Fx/Fy. Texto propuesto:

```
Fx, Fy = fuerza por partícula  [kN por metro de espesor]

Para repartir una presión q sobre un tramo:

        F = q × L / n

    q = presión [kPa]
    L = longitud del tramo [m]
    n = partículas seleccionadas (ver contador arriba)

Ejemplo:  112 kPa sobre 5 m con 5 partículas
          F = 112 × 5 / 5 = 112 kN

⚠ Si cambias la malla, recalcula: F depende de n.
```

El contador de partículas seleccionadas **ya existe**:
[view_WidgetDrawMenuPointMaterial.py:481](../app/views/draw/view_WidgetDrawMenuPointMaterial.py#L481)
(`lineEdit_textMPSelected`).

### PASO 5 — Migración de proyectos existentes

Fórmula: **`Fy_nuevo = Fy_viejo × DELTAINCREMENTO × NUMEROINCREMENTOS`**

**Recomendación: hacerla a mano.** Solo existen 2-3 proyectos de ejemplo y se están
reconstruyendo de todos modos. Evita tocar la serialización de puntos materiales,
que es la parte más delicada.

Si se quisiera automática: one-shot al abrir un proyecto que aún tenga
`DELTAINCREMENTO`, recorriendo todos los grupos de `PUNTOSMATERIAL` y borrando
después la clave.

---

## 5. Verificación

1. **Equivalencia numérica** — capacidad portante con `Fy = 112` y `nincre = 16`
   debe dar el mismo resultado que hoy con `Fy = 1.0`, `dincre = −7`, `nincre = 16`.
2. **Viga (dinámica)** — sin cambios; confirmar que `Fy` sigue significando lo mismo.
3. **Geostática** — confirmar que sigue ignorando las fuerzas y que ahora lo avisa.
4. **Cadena geostática → carga** — la etapa 2 arranca con `sig ≠ 0` y aplica la carga
   completa al final.
5. **Diálogo** — `Δ carga` ya no aparece; `nincre` visible en geostática e
   incrementos, oculto en dinámica.

---

## 6. Fuera de alcance

- Entrada por esfuerzo (descartada, §3.2).
- Factor de carga por etapa tipo ΣMstage de Plaxis.
- Cargas que varían en el tiempo dentro de una etapa dinámica.
