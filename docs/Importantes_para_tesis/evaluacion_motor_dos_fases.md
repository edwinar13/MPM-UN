# Evaluación: incorporar el motor MPM de doble fase a MPM-UN (aplicación)

**Autor:** Edwin Arévalo — Maestría en Ingeniería, Geotecnia (UNAL)
**Fecha:** Julio de 2026
**Propósito:** Evaluar técnicamente qué implicaría cambiar el motor de cálculo actual
(MPM de una fase) por el motor de doble fase, para decidir conjuntamente el alcance
del trabajo restante.

---

## 1. Contexto

El trabajo de esta tesis es la **aplicación de escritorio MPM-UN** (interfaz gráfica,
preprocesamiento y posprocesamiento) construida alrededor del motor de cálculo MPM
desarrollado previamente en el grupo. La aplicación se encuentra en fase de
generalización del acoplamiento UI–motor, con un sistema de **etapas de análisis**
(geostático, incrementos de carga, dinámico) recientemente implementado.

Se plantea la posibilidad de incorporar el motor de **doble fase y único punto**
(formulación *v–w*, hidromecánicamente acoplada) desarrollado por Wilson Guillermo
Caro González (2024), bajo la misma dirección (Ph.D. Mauricio Tapias) y codirección
(MSc. David León), es decir, del mismo linaje del motor MPM-UN actual.

## 2. Qué aporta el motor de doble fase

Simula la **generación y disipación de presión de poros** en suelos saturados,
permitiendo representar condiciones drenadas y no drenadas, y por tanto procesos de
consolidación y comportamiento hidromecánicamente acoplado en grandes deformaciones.

**Ventaja de partida:** el código es un *superconjunto* del motor actual —conserva las
mismas funciones de una fase y agrega las variantes `*_two_phases`— y mantiene el mismo
estilo de implementación (funciones Numba `@njit` que reciben arreglos NumPy). La
arquitectura UI–motor recién construida en la aplicación **no tendría que rehacerse**:
el análisis acoplado podría modelarse como un tipo de etapa adicional.

## 3. Limitación determinante del alcance

La tesis de referencia **valida exclusivamente problemas de consolidación**:

- Consolidación 1D en pequeñas deformaciones (contra solución analítica de Terzaghi).
- Consolidación 1D en grandes deformaciones (contra Xie y Leo, 2004).
- Consolidación 2D.

**No se validaron** taludes, capacidad portante ni muros de contención en formulación
de doble fase. Llevar el ejemplo de aplicación de esta tesis (muro de suelo
internamente estabilizado con geomalla) a régimen acoplado significaría ir **más allá
de lo demostrado por la propia tesis de referencia**, sin un patrón de comparación
disponible para verificar los resultados.

Adicionalmente, la carpeta del motor de doble fase contiene únicamente los módulos de
cálculo y el documento de tesis; **no incluye los scripts de los casos validados**. El
procedimiento de solución tendría que reconstruirse a partir del Capítulo 6 y el
Anexo B del documento.

## 4. Implicaciones técnicas de la integración

| Frente | Motor actual (1 fase) | Motor de doble fase |
|---|---|---|
| Estado por partícula | 7 arreglos (`xp, vp, Vp, Mp, sig, bp, tp`) | **17 arreglos**: agrega velocidad del agua, masas de cada fase, esfuerzo total y efectivo por separado, presión de poros, porosidad, permeabilidad, densidad del agua |
| Propiedades de material (UI) | E, ν, c′, φ′, ψ, ρ | Agrega porosidad inicial, permeabilidad, módulo volumétrico del agua, viscosidad, densidades saturada y del agua |
| Condiciones de frontera | Restricción de movimiento X/Y | Agrega **fronteras de drenaje** (permeable / impermeable): concepto inexistente hoy en la interfaz |
| Condiciones iniciales | Esfuerzos nulos o estado geostático | Agrega **nivel freático / presión de poros inicial** |
| Ciclo de cálculo | 6 pasos | Dos ecuaciones de momento (fase líquida y mezcla), fuerza de arrastre, condiciones de frontera en aceleración para ambas fases, integración selectiva reducida (SRI) para presión de poros, integración mixta y promediado de deformaciones volumétricas |
| Paso de tiempo crítico | Courant sobre la onda del esqueleto | CFL acoplado dominado por el **módulo volumétrico del agua (≈2,2 GPa)** → paso de tiempo sustancialmente menor → **tiempos de cómputo mucho mayores** |
| Posprocesamiento | Esfuerzos, deformaciones, velocidades, desplazamientos | Agrega presión de poros, distinción esfuerzo total/efectivo y velocidad del agua → afecta el modelo de resultados y los tres menús de posprocesamiento |

## 5. Escenarios de alcance y esfuerzo estimado

| Escenario | Entregable | Estimación |
|---|---|---|
| **A. Demostración a nivel de script** | Motor de doble fase integrado al proyecto y caso de consolidación 1D reproducido y comparado contra la solución analítica, **fuera de la interfaz**. Sin modificar la UI. | 1–2 semanas |
| **B. Integración mínima en la interfaz** | Tipo de etapa "Consolidación (doble fase)": propiedades de material extendidas, dominio totalmente saturado, drenaje únicamente en superficie, visualización básica de presión de poros. | 3–4 semanas |
| **C. Integración completa** | Nivel freático, drenaje definido por contorno, posprocesamiento completo y ejemplo de muro en doble fase. | 6 semanas o más, **sin referencia de validación** para el ejemplo propuesto |

*Estimaciones sobre trabajo efectivo y sujetas a disponer de los scripts de los casos
validados; sin ellos, agréguese aproximadamente una semana al escenario A.*

## 6. Recomendación

Con la entrega del documento prevista para **septiembre de 2026**, y estando aún
pendiente la implementación del **contacto multicuerpo** requerido por el ejemplo de
aplicación (muro estabilizado), se recomienda el **escenario A**:

1. Integrar el motor de doble fase al proyecto y reproducir el caso de **consolidación
   1D** a nivel de script, comparándolo contra la solución analítica.
2. Documentar en la tesis que la arquitectura de la aplicación —en particular el
   sistema de etapas de análisis— **está diseñada para acoger** un tipo de etapa de
   consolidación acoplada, dejando la integración completa en la interfaz como
   **trabajo futuro**, con la presente evaluación como hoja de ruta.

Esto incorpora la formulación de doble fase al alcance de la tesis de manera
verificable, sin comprometer el resultado principal del trabajo (la aplicación y su
ejemplo de validación).

**El escenario C no se considera viable** en el tiempo restante: consumiría la
totalidad del plazo disponible y obligaría a sacrificar el ejemplo de aplicación.

Si se prefiere una integración visible en la interfaz, se sugiere negociar el
**escenario B acotado**, asumiendo explícitamente la reducción de alcance en otro
frente (previsiblemente el contacto multicuerpo o parte de la validación del muro).

## 7. Acción que reduciría el riesgo

Solicitar a Wilson Caro o a David León los **scripts de ejecución de los casos de
consolidación validados**. Disponer de ellos reduciría de manera importante el riesgo
y el tiempo de cualquiera de los escenarios, al evitar reconstruir el procedimiento de
solución desde el documento.

---

### Referencias

- Caro González, W. G. (2024). *Implementación del Método del Punto Material con
  formulación acoplada de doble fase para aplicaciones geotécnicas bajo cargas
  estáticas.* Trabajo final de maestría, Universidad Nacional de Colombia.
- León Vanegas, D. E. (2019). Código MPM-UN (formulación de una fase), base del motor
  de cálculo actual de la aplicación.
