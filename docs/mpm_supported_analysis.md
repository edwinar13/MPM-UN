# MPM-UN: Análisis Soportados por la UI

Este documento define las **variantes de análisis** que la UI de MPM-UN será capaz de ejecutar, los **casos de uso** que se contemplan, y las **limitaciones** del alcance actual.

---

## 1. Alcance General

MPM-UN se enfoca en problemas geotécnicos modelados como un **medio continuo único** (un solo cuerpo de partículas que puede tener múltiples materiales/estratos). El algoritmo de **contacto entre cuerpos rígidos** queda **fuera del alcance** de esta versión.

Todos los análisis comparten el mismo motor numérico basado en el **Método del Punto Material (MPM)** con:
- Integración explícita en el tiempo.
- Funciones de forma bilineales en una malla Euleriana de fondo uniforme.
- Modelo constitutivo elastoplástico (Mohr-Coulomb / Tresca).
- Grandes deformaciones (actualización del gradiente de deformación `Fp`).
- Geometrías de partículas arbitrarias (polígonos, formas irregulares).

> [!NOTE]
> **Sobre la malla de fondo**: La malla Euleriana de fondo **siempre es uniforme y se reinicia en cada iteración temporal**. Esto **no es una limitación**, sino una ventaja del MPM. La malla de fondo solo sirve como "pizarrón temporal" para resolver las ecuaciones; las partículas (material points) son las que realmente representan la geometría y pueden tener **cualquier forma**. La UI permite dibujar polígonos arbitrarios, mallarlos y crear partículas dentro de ellos, lo cual es totalmente compatible con el motor.

---

## 2. Variantes de Análisis

La UI debe permitir al usuario elegir **cómo** se ejecuta la simulación. Las variantes se definen por tres parámetros clave:

### 2.1 Tipo de Solución Temporal

| Tipo | Bucle | Damping | Convergencia | Cuándo usarlo |
|------|-------|---------|--------------|---------------|
| **Dinámico** | `for t in range(N)` | Bajo o nulo (0.00–0.05) | No se evalúa | Se quiere observar la evolución real en el tiempo: vibración, colapso, propagación de ondas |
| **Cuasi-estático** | `while (ff > tol) or (ee > tol)` | Alto (0.50–0.80) | `static_convergence()` | Se busca el estado de equilibrio: peso propio, capacidad portante, estabilidad |

**¿Por qué existe el Cuasi-estático?**
El MPM es un método *dinámico* por naturaleza (siempre calcula inercia). Para encontrar un equilibrio estático (como el estado de esfuerzos bajo peso propio), se usa un truco numérico: se agrega un **amortiguamiento artificial alto** (`dampfac = 0.75`) que "mata" las oscilaciones rápidamente. El sistema pierde energía cinética hasta que las fuerzas se balancean. Las funciones `static_convergence()` y `static_convergence2()` miden el desbalance de fuerzas (`ff`) y la energía cinética (`ee`) para decidir cuándo parar.

### 2.2 Modo de Aplicación de Carga

| Modo | Descripción | Ejemplo |
|------|-------------|---------|
| **Gravedad instantánea** | Se activa `bp[:,1] = -9.81` desde el paso 0 | Viga empotrada, colapso dinámico |
| **Rampa de gravedad** | Se incrementa linealmente la gravedad en N pasos: `bp[:,1] = -9.81 × grav[j]` | Talud (50 incrementos de `0.01g` a `1.0g`) |
| **Incrementos de carga externa** | Se aplica una fuerza distribuida en N incrementos, cada uno alcanzando equilibrio cuasi-estático | Capacidad portante de zapata |

### 2.3 Etapas (Stages)

Algunos problemas requieren **más de una fase** de análisis secuencial:

| Etapa | Propósito | Ejemplo |
|-------|-----------|---------|
| **Geoestática** | Establecer el campo de esfuerzos por peso propio antes de aplicar cargas | Todas las simulaciones que parten de un suelo "en reposo" |
| **Construcción / Carga** | Aplicar cargas externas incrementalmente | Zapata, muro, relleno |
| **Evento dinámico** | Liberar restricciones o aplicar sismos después del equilibrio | Colapso por remoción de soporte, sismo |

> [!IMPORTANT]
> **No todas las simulaciones necesitan etapas.** Si el problema parte del reposo sin cargas previas importantes (como una viga que cuelga), un solo paso dinámico es suficiente. Las etapas se usan cuando el estado inicial del suelo es relevante para el resultado.

---

## 3. Casos de Uso Contemplados

### 3.1 Viga o Estructura Simple
- **Descripción**: Elemento estructural sometido a gravedad instantánea o carga puntual.
- **Tipo de análisis**: Dinámico puro.
- **Materiales**: 1 (homogéneo).
- **Etapas**: 1 (directa).
- **Ejemplo en motor**: `beam.py`.

### 3.2 Capacidad Portante de Cimentación
- **Descripción**: Suelo bajo un cimiento superficial (zapata corrida). Se aplica carga incrementalmente hasta la falla.
- **Tipo de análisis**: Cuasi-estático con incrementos de carga.
- **Materiales**: 1 o más (suelo con diferentes estratos).
- **Etapas**: Puede ser 1 (solo carga incremental) o 2 (geoestático + carga).
- **Ejemplo en motor**: `Ca_portante2.py`.

### 3.3 Colapso de Columna / Material Granular
- **Descripción**: Masa de suelo que pierde soporte lateral y colapsa por gravedad.
- **Tipo de análisis**: Cuasi-estático (geoestático) → Dinámico (colapso).
- **Materiales**: 1.
- **Etapas**: 2 (equilibrar bajo gravedad, luego liberar contención).
- **Ejemplo en motor**: `Collapse.py`.

### 3.4 Estabilidad de Talud
- **Descripción**: Ladera natural o artificial cuya estabilidad se evalúa bajo peso propio.
- **Tipo de análisis**: Cuasi-estático con rampa de gravedad.
- **Materiales**: 2 o más (estratos con diferentes propiedades).
- **Etapas**: 1 (rampa de gravedad hasta equilibrio o falla).
- **Ejemplo en motor**: `talud_2021.py`.

### 3.5 Pilote Hincado (Driven Pile)
- **Descripción**: Simulación de un pilote siendo hincado o empujado dentro de una masa de suelo.
- **Tipo de análisis**: Dinámico (el hincado es un evento de impacto) o Cuasi-estático (pilote empujado lentamente con desplazamiento controlado).
- **Materiales**: 2 (pilote como material muy rígido + suelo).
- **Etapas**: 2 (geoestático del suelo, luego aplicación de desplazamiento/fuerza sobre el pilote).
- **Consideraciones**:
  - El pilote se modela como un bloque rectangular de partículas con propiedades muy rígidas (E de concreto u acero, cohesión altísima para que no se "rompa").
  - La penetración se logra aplicando una fuerza de cuerpo (`bp[:,1]`) descendente solo a las partículas del pilote, o bien un desplazamiento controlado por incrementos.
  - **Limitación sin contacto**: Al ser medio continuo, no hay interfaz suelo-pilote con fricción independiente. Las partículas del pilote y del suelo "se mezclan" en la interfaz. Esto puede subestimar la resistencia por fuste. Para resultados cuantitativos precisos se necesitaría el algoritmo de contacto.
  - **¿Es útil sin contacto?** Sí, para visualizar cualitativamente el mecanismo de falla (bulbo de presiones, desplazamientos laterales) y estimar la capacidad de punta.

### 3.6 Falla de un Dado de Pilotes (Pile Cap)
- **Descripción**: Un grupo de pilotes con un cabezal (dado) de concreto. Se evalúa la capacidad del sistema bajo carga vertical.
- **Tipo de análisis**: Cuasi-estático con incrementos de carga.
- **Materiales**: 3+ (dado de concreto, pilotes de concreto/acero, suelo con posibles estratos).
- **Etapas**: 2 (geoestático del suelo + carga incremental sobre el dado).
- **Consideraciones**:
  - El dado se modela como un bloque horizontal de partículas rígidas (concreto).
  - Los pilotes se modelan como columnas verticales delgadas de partículas rígidas.
  - La carga se aplica sobre el dado (como `traction_forces` o fuerza de cuerpo).
  - Al ser un modelo 2D (deformación plana), se representa una "fila de pilotes" infinita en la dirección perpendicular. Para un pilote individual sería más representativo un modelo axisimétrico (no disponible en este motor).
  - **Sin contacto**: Las mismas limitaciones que el pilote hincado aplican en la interfaz.
  - **Validación**: Se puede comparar contra fórmulas de capacidad portante de grupo de pilotes (eficiencia de grupo).

### 3.7 Muro de Tierra Armada / Mecánicamente Estabilizado (MSE Wall)
- **Descripción**: Un muro conformado por capas de relleno compactado con refuerzos horizontales (geomallas/geotextiles), y una cara frontal (facing).
- **Tipo de análisis**: Cuasi-estático con rampa de gravedad o incrementos de carga.
- **Materiales**: 3+ (relleno granular, refuerzo tipo geomalla, facing frontal).
- **Etapas**: 2+ (geoestático + aplicación de sobrecarga).

#### Análisis Detallado: ¿Por qué es un excelente caso de validación?

**Porqué es ideal para la tesis:**

Un muro MSE es uno de los mejores casos de validación para MPM-UN porque tiene **solución analítica conocida** contra la cual comparar directamente los resultados numéricos:

1. **Empuje de tierras (Rankine/Coulomb)**: La presión lateral del suelo sobre el muro se puede calcular analíticamente como:
   - Empuje activo: `σ_h = K_a × γ × z` donde `K_a = tan²(45° - φ/2)`
   - Esto nos da una distribución triangular de presiones que podemos comparar directamente con los esfuerzos `σ_xx` de nuestras partículas.

2. **Longitud mínima del refuerzo**: La teoría clásica establece que la longitud del refuerzo en la zona activa debe resistir el arranque (pullout). Se puede calcular como:
   - `L_e = T_max / (2 × f* × σ_v × α)` + longitud en la zona "resistente".
   - Esto se puede validar observando las deformaciones plásticas en el modelo.

3. **Superficie de falla**: La zona activa de Rankine predice una superficie de falla a `45° + φ/2`. En el modelo MPM, esta superficie debería manifestarse como una zona de concentración de deformaciones plásticas equivalentes (`eqplas`).

**Cómo modelarlo en MPM-UN:**

```
┌─────────────────────────────────────────────┐
│              MALLA DE FONDO                 │
│                                             │
│  ┌──┐ ═══════════════════════ (Geomalla 5)  │
│  │F │ ░░░░░░░░░░░░░░░░░░░░░░ (Relleno)     │
│  │A │ ═══════════════════════ (Geomalla 4)  │
│  │C │ ░░░░░░░░░░░░░░░░░░░░░░ (Relleno)     │
│  │I │ ═══════════════════════ (Geomalla 3)  │
│  │N │ ░░░░░░░░░░░░░░░░░░░░░░ (Relleno)     │
│  │G │ ═══════════════════════ (Geomalla 2)  │
│  │  │ ░░░░░░░░░░░░░░░░░░░░░░ (Relleno)     │
│  │  │ ═══════════════════════ (Geomalla 1)  │
│  └──┘ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ (Suelo fund.) │
│                                             │
└─────────────────────────────────────────────┘
```

Cada componente se modela como **un material diferente en el mismo medio continuo**:

| Componente | Material | Propiedades clave |
|------------|----------|-------------------|
| **Relleno granular** | Mohr-Coulomb | E = 30,000 kPa, ν = 0.3, c' = 0, φ' = 34°, ρ = 1.8 Mg/m³ |
| **Geomalla** | Elástico lineal (alta rigidez en dirección horizontal) | E = 500,000 kPa, ν = 0.2, c' muy alto (no falla), ρ = 0.1 Mg/m³ |
| **Facing (cara frontal)** | Rígido (concreto) | E = 25,000,000 kPa, ν = 0.2, c' muy alto, ρ = 2.4 Mg/m³ |
| **Suelo de fundación** | Mohr-Coulomb | E = 15,000 kPa, ν = 0.3, c' = 10, φ' = 28°, ρ = 1.9 Mg/m³ |

**Proceso de simulación:**
1. **Etapa 1 - Geoestático**: Activar gravedad con rampa. Todas las partículas alcanzan equilibrio bajo peso propio.
2. **Etapa 2 - Sobrecarga**: Aplicar carga incremental sobre la corona del muro hasta la falla.

**Resultados que se pueden validar analíticamente:**
- Distribución de presiones laterales vs profundidad → comparar con `K_a × γ × z`.
- Desplazamiento horizontal del facing → comparar con rangos típicos de la literatura (0.5% a 1% de la altura del muro para muros bien diseñados).
- Localización de la superficie de falla → comparar con la línea a `45° + φ/2` de Rankine.
- Tensión máxima en los refuerzos → comparar con `T_max = K_a × γ × z × S_v` (donde `S_v` es el espaciamiento vertical).

> [!TIP]
> **Este caso es especialmente interesante para la tesis** porque:
> 1. Tiene validación analítica directa (Rankine, Coulomb, FHWA).
> 2. Es un problema geotécnico real y práctico.
> 3. Se puede modelar completamente sin algoritmo de contacto.
> 4. Los resultados son visualmente impactantes (se ve la cuña de falla).
> 5. Es un tema relevante en ingeniería colombiana (muros en vías de montaña).

**Limitaciones del modelo sin contacto:**
- No se modela el deslizamiento ("pullout") de la geomalla como falla de interfaz. La geomalla y el relleno se portan como medio continuo, lo cual es conservador: la falla real ocurre primero en la interfaz, pero aquí fallará el material más débil (el relleno).
- El facing y el relleno no tienen una junta real. Esto es aceptable porque en muros MSE con facing rígido, la conexión es mecánica.

---

## 4. Escenarios Complejos: ¿Qué SÍ y qué NO se puede hacer?

### 4.1 Talud con Múltiples Estratos / Materiales

**✅ SÍ es posible.**

El motor ya lo soporta nativamente. En `talud_2021.py` se ve que un mismo conjunto de partículas puede tener **propiedades diferentes** según su posición:

```python
# Estrato superior: arcilla blanda
Prop[:,2] = 5      # Cohesión = 5 kPa

# Estrato inferior: roca blanda
Prop[idM1, 2] = 50  # Cohesión = 50 kPa (partículas debajo de y=0.5)
```

**¿Cómo funciona en la UI?** Ya lo soportas. Cada material dibujado en la interfaz genera un bloque de partículas con su propio conjunto de propiedades (`E`, `ν`, `c'`, `φ'`, `ψ'`, `ρ`). Al armar el arreglo `Prop` para el motor, simplemente se concatenan todos los bloques. **No se necesita contacto** porque son materiales dentro del mismo medio continuo (como capas de un suelo real).

**Ejemplo práctico**: Un talud con 3 estratos (arena suelta arriba, arcilla en medio, roca abajo) se modela como:
- 3 rectángulos de material en la UI, cada uno con sus propiedades.
- Las partículas se unen en un solo arreglo `xp` y el arreglo `Prop` tiene las filas correspondientes a cada material.
- El motor los trata como un solo cuerpo continuo.

---

### 4.2 Muro de Contención Simple

**✅ SÍ es posible, con una simplificación.**

Un muro de contención se puede modelar como un **material con propiedades muy rígidas** (módulo de elasticidad alto, cohesión alta) dentro del mismo medio continuo.

**Sin contacto**: El muro y el suelo comparten la misma malla y se tratan como un medio continuo. Esto significa que **no hay deslizamiento real** en la interfaz muro-suelo (no hay una superficie de contacto con fricción independiente). Pero para muchos problemas prácticos de ingeniería, esta simplificación es aceptable.

**¿Cómo funciona en la UI?**
1. Se dibuja un rectángulo con propiedades de "concreto" (E = 25,000,000 kPa, ρ = 2.4 Mg/m³, c muy alto).
2. Se dibuja el suelo detrás del muro con sus propiedades reales.
3. El motor los une en un solo arreglo y resuelve como medio continuo.

> [!NOTE]
> **Limitación**: Al ser un medio continuo, el muro y el suelo "se pegan" en la interfaz. No se modela el deslizamiento de la interfaz suelo-estructura. Sin embargo, esta simplificación es ampliamente usada en la literatura de MPM para problemas geotécnicos.

---

### 4.3 Zapata con Elemento Estructural (Cimiento Físico)

**✅ SÍ es posible, de dos formas:**

#### Opción A: Zapata como carga distribuida (actual)
La zapata **no se dibuja** como un objeto; solo se aplica una fuerza distribuida (`traction_forces`) sobre las partículas de la superficie del suelo. Es el método más simple y numéricamente estable.

#### Opción B: Zapata como material rígido
Se dibuja un rectángulo de "concreto" (E muy alto) encima del suelo. La carga se aplica sobre las partículas del concreto.

---

### 4.4 Relleno o Excavación por Etapas

**⚠️ Posible con extensión.**

Teóricamente se puede modelar:
- **Relleno**: Agregar partículas progresivamente (activar capas en cada etapa).
- **Excavación**: Eliminar partículas progresivamente (desactivar capas).

Esto requiere que el motor soporte **activación/desactivación de partículas por etapa**, lo cual no está implementado actualmente pero es una extensión natural del sistema de etapas.

---

### 4.5 Carga Sísmica

**⚠️ Posible con extensión.**

Se podría aplicar una aceleración variable en el tiempo (`bp[:,0] = f(t)`) para simular un sismo. El motor ya calcula fuerzas de cuerpo en cada paso de tiempo; solo faltaría leer un acelerograma y aplicarlo dinámicamente.

---

## 5. Lo que NO se contempla (Fuera de Alcance)

| Funcionalidad | Razón |
|---------------|-------|
| **Contacto entre cuerpos** | Requiere algoritmo `contact()` y concepto de "cuerpos independientes" en la UI |
| **Modelos constitutivos adicionales** | Solo Mohr-Coulomb/Tresca están implementados en `explicit2.py` |
| **3D** | El motor es estrictamente 2D (deformación plana) |
| **Acoplamiento hidromecánico (agua)** | No se modela la presión de poros ni el flujo de agua |

---

## 6. Resumen: Matriz de Capacidades

| Escenario | Materiales | Etapas | Tipo Análisis | Estado |
|-----------|-----------|--------|---------------|--------|
| Viga / estructura simple | 1 | 1 | Dinámico | ✅ Listo |
| Capacidad portante (carga) | 1-2 | 1-2 | Cuasi-estático | ✅ Listo |
| Colapso de material granular | 1 | 2 | Mixto | 🔧 Requiere UI de etapas |
| Talud con múltiples estratos | 2+ | 1 | Cuasi-estático | ✅ Motor listo, UI soporta materiales |
| Pilote hincado | 2 | 2 | Dinámico / Cuasi-est. | 🔧 Requiere UI de etapas |
| Dado de pilotes | 3+ | 2 | Cuasi-estático | 🔧 Requiere UI de etapas |
| **Muro tierra armada (MSE)** | **3+** | **2** | **Cuasi-estático** | **🔧 Caso de validación ideal** |
| Muro de contención simple | 2+ | 2 | Cuasi-estático | 🔧 Requiere UI de etapas |
| Zapata con elemento físico | 2+ | 2 | Cuasi-estático | 🔧 Requiere UI de etapas |
| Relleno / Excavación | 2+ | N | Cuasi-estático | ⏳ Extensión futura |
| Carga sísmica | 1+ | 2 | Mixto | ⏳ Extensión futura |

> [!TIP]
> Los ítems marcados con 🔧 solo necesitan que la UI permita **definir etapas** y **elegir tipo de análisis** (dinámico/cuasi-estático). El motor numérico ya tiene todas las funciones necesarias.
