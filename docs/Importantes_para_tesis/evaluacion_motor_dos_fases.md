# Evaluación: incorporar el motor MPM de doble fase a MPM-UN (aplicación)

**Autor:** Edwin Arévalo — Maestría en Ingeniería, Geotecnia (UNAL)
**Fecha:** Julio de 2026 — **actualizada el 30 de septiembre de 2026** tras una revisión
detallada del código fuente y del documento de referencia (sección 5).
**Propósito:** Evaluar técnicamente qué implica incorporar el motor de doble fase a la
aplicación y dimensionar el trabajo restante.

---

## 1. Contexto

El trabajo de esta tesis es la **aplicación de escritorio MPM-UN** (interfaz gráfica,
preprocesamiento y posprocesamiento) construida alrededor del motor de cálculo MPM
desarrollado previamente en el grupo. A la fecha de esta actualización:

- El acoplamiento UI–motor está generalizado mediante **etapas de análisis**
  (geostático, incrementos de carga, dinámico), validado contra los tres casos de
  referencia (viga, capacidad portante, talud).
- El **contacto multicuerpo** está implementado y validado: la falla del talud
  reproduce bit a bit el script de referencia de dos cuerpos.
- El muro estabilizado con geomalla quedó fuera del alcance.

El motor de **doble fase y único punto** (formulación *v–w*, hidromecánicamente
acoplada) fue desarrollado por Wilson Guillermo Caro González (2024), bajo la misma
dirección (Ph.D. Mauricio Tapias) y codirección (MSc. David León), es decir, del mismo
linaje del motor MPM-UN actual.

## 2. Qué aporta el motor de doble fase

Simula la **generación y disipación de presión de poros** en suelos saturados,
permitiendo representar condiciones drenadas y no drenadas, y por tanto procesos de
consolidación y comportamiento hidromecánicamente acoplado en grandes deformaciones.

**Ventaja de partida:** el código es un *superconjunto* del motor actual —conserva las
mismas funciones de una fase y agrega las variantes `*_two_phases`— y mantiene el mismo
estilo de implementación (funciones Numba `@njit` que reciben arreglos NumPy). La
arquitectura UI–motor de la aplicación **no tendría que rehacerse**: el análisis
acoplado se modela como un tipo de etapa adicional.

## 3. Limitación determinante del alcance

La tesis de referencia **valida exclusivamente problemas de consolidación**:

- Consolidación 1D en pequeñas deformaciones (contra solución analítica de Terzaghi).
- Consolidación 1D en grandes deformaciones (contra Xie y Leo, 2004).
- Consolidación 2D.

**No se validaron** taludes, capacidad portante ni muros en formulación de doble fase;
cualquier caso distinto a la consolidación carecería de patrón de comparación. Por eso
el alcance propuesto se limita a reproducir la consolidación.

La carpeta del motor de doble fase contiene únicamente los módulos de cálculo y el
documento de tesis; **no incluye los scripts de los casos validados** (el Anexo C del
documento tampoco: contiene las funciones, no el programa principal). El procedimiento
de solución debe reconstruirse a partir del Algoritmo 2 (Capítulo 6) y la Tabla 7-1.

## 4. Implicaciones técnicas de la integración

| Frente | Motor actual (1 fase) | Motor de doble fase |
|---|---|---|
| Estado por partícula | 7 arreglos (`xp, vp, Vp, Mp, sig, bp, tp`) | **17 arreglos**: agrega velocidad del agua, masas de cada fase, esfuerzo total y efectivo por separado, presión de poros, porosidad, permeabilidad, densidad del agua |
| Propiedades de material (UI) | E, ν, c′, φ′, ψ, ρ | Agrega porosidad inicial, permeabilidad, módulo volumétrico del agua, densidades de sólidos y del agua |
| Condiciones de frontera | Restricción de movimiento X/Y | Agrega **fronteras de drenaje** (permeable / impermeable): concepto inexistente hoy en la interfaz |
| Condiciones iniciales | Esfuerzos nulos o estado geostático | Agrega **presión de poros inicial** |
| Ciclo de cálculo | 6 pasos | Dos ecuaciones de momento (fase líquida y mezcla), fuerza de arrastre, condiciones de frontera en aceleración para ambas fases, integración selectiva reducida (SRI) para presión de poros |
| Paso de tiempo crítico | Courant sobre la onda del esqueleto | CFL acoplado dominado por el **módulo volumétrico del agua** → paso de tiempo menor. En los casos de validación se usa un Kw reducido (100 MPa), lo que mantiene tiempos de cómputo del orden de minutos |
| Posprocesamiento | Esfuerzos, deformaciones, velocidades, desplazamientos | Agrega presión de poros y la distinción esfuerzo total/efectivo |

## 5. Revisión detallada del código (septiembre de 2026)

Se comparó función por función el motor de doble fase con el motor de la aplicación:

- **Las funciones comunes son idénticas** en ambos motores (funciones de forma, modelo
  Mohr-Coulomb, matriz elástica, búsqueda de partículas por elemento). Solo difiere la
  opción de caché de Numba.
- En consecuencia, las funciones de doble fase pueden incorporarse en un **módulo nuevo**
  del motor que reutiliza las funciones existentes, **sin modificar el motor de una fase**.
  Las validaciones ya obtenidas no se ven afectadas.
- Las funciones de doble fase necesarias (transferencia partícula–nodo, velocidades y
  posiciones, condiciones de frontera, actualización de esfuerzo efectivo y presión de
  poros con SRI) **ya están compiladas con Numba**.
- Lo que falta reconstruir es la parte que hacía el programa principal: ensamble de la
  ecuación nodal y cálculo de aceleraciones de ambas fases, amortiguamiento local de
  doble fase, condición de drenaje (Δp = 0 en la frontera permeable), presión de poros
  inicial y aplicación de la carga. Todo está descrito en el Algoritmo 2 del documento.
- El caso de consolidación 1D en pequeñas deformaciones es pequeño: columna de
  0.1 × 1 m, 490 partículas, Δt = 0.0002 s, 4 s de simulación (111 s de cómputo
  reportados). Se valida contra la solución analítica de Terzaghi, que es independiente
  de los resultados numéricos de la tesis de referencia.

## 6. Escenarios de alcance y esfuerzo estimado (actualizado)

Estimaciones en días de trabajo efectivo.

**Escenario A. Demostración a nivel de script** — consolidación 1D reproducida y
comparada contra Terzaghi, fuera de la interfaz.

| Tarea | Dificultad | Días |
|---|---|---|
| Módulo de doble fase en el motor (funciones existentes, sin tocar el motor de una fase) | Baja | 0.5 |
| Script del caso: malla, partículas, fronteras y ciclo del Algoritmo 2 | Media (ajuste del drenaje y el amortiguamiento) | 2–3 |
| Solución de Terzaghi, isócronas, error y figuras | Baja | 0.5–1 |
| **Total** | | **4–5** |

Opcional: consolidación 1D en grandes deformaciones con el mismo script (≈ 1 día más).

**Escenario B. Integración mínima en la interfaz** (posterior a A).

| Tarea | Dificultad | Días |
|---|---|---|
| Tipo de etapa "Consolidación" en el diálogo de etapas | Baja | 1 |
| Propiedades de material de doble fase | Baja | 1 |
| Condición de drenaje en los contornos existentes | Media | 1–1.5 |
| Presión de poros inicial por grupo de partículas | Baja | 0.5 |
| Ejecutor: estado de doble fase y paso de cálculo acoplado | Media | 2 |
| Resultados: presión de poros en tablas, gráficas y animación | Baja (extensa) | 1–1.5 |
| Validación: el caso 1D desde la interfaz igual al script de A | Baja | 0.5–1 |
| **Total** | | **7–9** |

**Escenario C. Integración completa** (nivel freático, drenaje general, casos nuevos):
no viable en el plazo y **sin referencia de validación**.

## 7. Recomendación

Con el cierre del software previsto para el **19 de octubre de 2026** (≈ 14 días
hábiles desde esta actualización), A + B suman 11–14 días: es posible, pero sin margen.
Se recomienda:

1. Ejecutar el **escenario A** de inmediato.
2. Si A queda terminado alrededor del **7 de octubre**, continuar con el **escenario B**.
3. En caso contrario, documentar B como trabajo futuro, con el desglose de la sección 6
   como hoja de ruta, y dejar constancia de que el sistema de etapas de la aplicación
   está diseñado para acoger un tipo de etapa de consolidación acoplada.

## 8. Acción que reduciría el riesgo

Solicitar a Wilson Caro o a David León los **scripts de ejecución de los casos de
consolidación validados**. No es bloqueante —el procedimiento puede reconstruirse del
documento—, pero aclararía cómo se aplicaron el drenaje y la carga y acortaría la
depuración del escenario A.

---

### Referencias

- Caro González, W. G. (2024). *Implementación del Método del Punto Material con
  formulación acoplada de doble fase para aplicaciones geotécnicas bajo cargas
  estáticas.* Trabajo final de maestría, Universidad Nacional de Colombia.
- León Vanegas, D. E. (2019). Código MPM-UN (formulación de una fase), base del motor
  de cálculo actual de la aplicación.
- Terzaghi, K. (1925). *Erdbaumechanik auf bodenphysikalischer Grundlage.* Deuticke.
