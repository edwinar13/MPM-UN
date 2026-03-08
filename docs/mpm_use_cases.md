# Catálogo de Casos de Uso del Motor MPM

## Resumen de Tipos de Análisis

| # | Ejemplo | Tipo de Análisis | Cuerpos | Etapas | Damping | Convergencia | ¿UI Compatible? |
|---|---------|-------------------|---------|--------|---------|--------------|-----------------|
| 1 | `beam.py` | Dinámico puro | 1 | 1 | 0.00 | Ninguna | ✅ Sí |
| 2 | `Ca_portante2.py` | Cuasi-estático (incrementos de carga) | 1 | N incrementos | 0.75 | `static_convergence` | ✅ Sí |
| 3 | `Collapse.py` | Cuasi-estático → Dinámico (2 etapas) | 1 | 2 | 0.75 → 0.04 | `static_convergence` → `static_convergence2` | ⚠️ Parcial |
| 4 | `Collapse_contact.py` | Dinámico con contacto | 2 | 1 | 0.04 | Ninguna | ❌ No |
| 5 | `Disc.py` | Dinámico con contacto + fricción | 2 | 1 | 0.00 | Ninguna | ❌ No |
| 6 | `talud_2021.py` | Cuasi-estático (rampa de gravedad) | 1 (2 materiales) | N incrementos | 0.75 | `static_convergence` | ⚠️ Parcial |
| 7 | `ejecutarMPM.py` | Dinámico puro (lee JSON) | 1 | 1 | 0.00 | Ninguna | ✅ Es la base actual |

---

## Detalle por Caso

### 1. `beam.py` — Viga Empotrada (Gravedad Instantánea)
- **Física**: Una viga rectangular suspendida en el aire. Se activa la gravedad instantáneamente (`bp[:,1] = -9.81`) y se observa la deflexión dinámica (oscilación).
- **Tipo**: **Dinámico puro**. Un solo bucle `for t` en el tiempo, sin convergencia estática.
- **Damping**: `0.00` (sin amortiguamiento, oscila libremente).
- **Geometría**: Rectángulo simple definido por `(xi, yi, xf, yf)`.
- **Un solo material**, un solo cuerpo.
- **UI**: ✅ Tu UI actual ya soporta este caso perfectamente. Es prácticamente lo que hace `ejecutarMPM.py`.

---

### 2. `Ca_portante2.py` — Capacidad Portante de Zapata (Tresca)
- **Física**: Un suelo bajo un cimiento corrido. Se aplica carga incrementalmente sobre la zapata para encontrar la capacidad portante última. El suelo tiene un modelo constitutivo Tresca (cohesión pura, sin fricción).
- **Tipo**: **Cuasi-estático con incrementos de carga**. Bucle externo `for i in range(nincre)` donde cada incremento aplica más carga. Dentro de cada incremento, un bucle `while` hasta alcanzar equilibrio estático.
- **Damping**: `0.75` (altísimo, para "matar" la inercia y llegar al equilibrio rápido).
- **Convergencia**: `static_convergence()` evalúa el desbalance de fuerzas (`ff`) y la energía cinética (`ee`).
- **Carga**: Usa `traction_forces()` para aplicar fuerza distribuida en partículas de la superficie.
- **UI**: ✅ Tu UI ya soporta este caso. Es como el ejemplo `.mpm` de "capacidad portante" que revisamos.

> [!IMPORTANT]
> **¿Por qué etapas aquí?** No son "etapas" en el sentido de geoestático→dinámico. Aquí cada "incremento" es un escalón de carga. Se aplica un poco más de fuerza, se espera al equilibrio, se guarda el resultado, y se repite. Esto permite construir la curva **Carga vs Desplazamiento**.

---

### 3. `Collapse.py` — Colapso de Columna Granular
- **Física**: Una columna de arena vertical (0.09m×0.63m) contenida por una pared. Se retira la pared y se observa el colapso dinámico. Basado en el artículo de Solowski (2013).
- **Tipo**: **2 Etapas reales**:
  1. **Geoestática**: Bucle `while` con `dampfac=0.75` y `static_convergence()`. Establece el equilibrio bajo gravedad con la pared puesta (nodos fijos en `xBC=0.09`).
  2. **Dinámica**: Se retiran los nodos fijos de la pared (`fixed_nodesX` se recalcula sin ellos). Bucle `for t` con `dampfac=0.04` y `static_convergence2()`.
- **UI**: ⚠️ **Parcial**. Tu UI no tiene un mecanismo para definir "primero equilibrio geoestático, luego liberar una condición de contorno y correr dinámicamente".

> [!IMPORTANT]
> **¿Por qué geostático + dinámico aquí?** Porque si aplicas la gravedad instantáneamente Y quitas la pared al mismo tiempo, el suelo "rebota" por la inercia. En la realidad, el suelo ya estaba en equilibrio bajo gravedad ANTES de que quitaran el muro. Las 2 etapas simulan esa secuencia real.

---

### 4. `Collapse_contact.py` — Colapso con Contacto (2 Cuerpos)
- **Física**: Similar al Collapse, pero ahora hay un **muro rígido** (Cuerpo 1: cohesión alta, E alto) y un **suelo granular** (Cuerpo 2: arena con fricción). Usan el algoritmo de **contacto** para que no se interpenetren.
- **Tipo**: **Dinámico con contacto**. Un solo bucle `for t`. Sin paso geoestático (los esfuerzos iniciales se ponen en 0).
- **Contacto**: Usa `contact()` de `explicit2.py` con coeficiente de fricción `mu`.
- **Cuerpos separados**: Arrays independientes `xp_1, vp_1, Prop_1` y `xp_2, vp_2, Prop_2`. Se mapean a la misma malla pero se resuelven por separado, y la función `contact()` ajusta los momentos nodales para evitar interpenetración.
- **UI**: ❌ **No soportado**. Tu UI no tiene concepto de "cuerpos separados" ni algoritmo de contacto. Tus materiales comparten la misma malla de forma continua (un solo medio).

---

### 5. `Disc.py` — Disco en Plano Inclinado (Contacto + Fricción)
- **Física**: Un disco circular rueda/se desliza sobre un plano inclinado (`theta = π/3`). Es un problema de validación clásico de mecánica de contacto. 
- **Tipo**: **Dinámico con contacto**. Un solo bucle `for t`. El disco (Cuerpo 2) tiene geometría de malla triangular irregular importada desde archivos `.txt`.
- **Contacto**: Mismo algoritmo `contact()` con `mu=0.3`.
- **Particularidad**: El Cuerpo 2 (disco) usa una malla triangular importada (`disc-coord.txt`, `disc-inci.txt`), NO la función `setup_MP()`.
- **UI**: ❌ **No soportado**. Mismas limitaciones del caso 4, más la necesidad de importar geometrías no rectangulares.

---

### 6. `talud_2021.py` — Estabilidad de Talud (Rampa de Gravedad)
- **Física**: Un talud (ladera inclinada) de 60m×20m. Se aplica la gravedad en 50 incrementos lineales (rampa de `0.01g` a `1.0g`) para llegar al equilibrio geoestático sin oscilaciones. Tiene 2 materiales diferentes pero como un **solo medio continuo** (no usa contacto).
- **Tipo**: **Cuasi-estático con rampa de gravedad**. Bucle externo `for j in range(len(grav))` donde cada paso incrementa la gravedad. Dentro, bucle `while` con `dampfac=0.75` y `static_convergence()` hasta el equilibrio.
- **Geometría especial**: El dominio NO es un simple rectángulo. Usa un filtro `for j` tipo piecewise para "recortar" la geometría inclinada del talud.
- **2 Materiales, 1 Cuerpo**: Usa `idM1` para asignar diferentes propiedades (cohesión distinta) a las partículas del estrato inferior. No hay algoritmo de contacto.
- **UI**: ⚠️ **Parcial**. Tu UI sí soporta múltiples materiales en un solo cuerpo. Pero la geometría inclinada (recorte piecewise) y la rampa de gravedad no están disponibles directamente.

---

### 7. `ejecutarMPM.py` — Motor genérico (lee desde JSON)
- **Física**: Es el puente actual entre tu UI y el motor. Lee la malla y las partículas desde el JSON que genera la UI.
- **Tipo**: **Dinámico puro**. Un solo bucle `for t`, sin convergencia estática.
- **UI**: ✅ **Es la base actual**. Sin embargo, tiene valores hardcodeados (como `rhop = 2.0`, `time = 2`, `dampfac = 0.00`, propiedades de material fijas). Eso es lo que debemos generalizar.

---

## Conclusión: ¿Qué puede analizar el programa?

El motor MPM es **capaz de todo lo anterior** desde el punto de vista numérico. Las funciones en `explicit2.py` y `mesh.py` son genéricas. Lo que cambia entre ejemplos son **3 variantes**:

### Variante 1: Tipo de Bucle Temporal
| Tipo | Bucle | Se usa cuando... |
|------|-------|------------------|
| **Dinámico** | `for t` simple | Se quiere ver la evolución en el tiempo (vibración, colapso, impacto) |
| **Cuasi-estático** | `while (ff > tol)` con damping alto | Se busca el equilibrio (estado geoestático, capacidad portante) |
| **Mixto** | `while` → `for t` | Se necesita equilibrio inicial y luego evolución dinámica |

### Variante 2: Número de Cuerpos
| Tipo | Se usa cuando... |
|------|------------------|
| **1 Cuerpo** | Suelo continuo, viga, talud |
| **Multi-Cuerpo + Contacto** | Hay objetos rígidos interactuando (muro+suelo, disco+plano) |

### Variante 3: Cómo se aplica la carga
| Tipo | Se usa cuando... |
|------|------------------|
| **Gravedad instantánea** | `beam.py`, `Collapse.py` (fase dinámica) |
| **Rampa de gravedad** | `talud_2021.py` (incrementos de `0.01g` a `1.0g`) |
| **Incrementos de carga** | `Ca_portante2.py` (zapata: `dincre = -2 kN/m` por paso) |

---

## ¿En qué se debería centrar la UI?

> [!TIP]
> **Recomendación**: Para tu tesis, concéntrate en los casos **sin contacto** (Variante 2 = 1 Cuerpo). Esto cubre los casos 1, 2, 3, 6 y 7, que representan los problemas geotécnicos clásicos: vigas, zapatas, taludes, y colapsos. El contacto (casos 4 y 5) es un tema de investigación aparte y añadiría mucha complejidad a la UI.

Con eso, tu motor genérico solo necesita manejar:
1. **Tipo dinámico o cuasi-estático** (un flag en la configuración).
2. **Incrementos de carga o tiempo fijo** (otro flag).
3. **Múltiples materiales en un solo dominio** (que ya lo soportas en la UI).
