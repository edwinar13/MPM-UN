# Pendientes del proyecto

Lista única de lo que queda por hacer o decidir. Cada ítem dice de dónde salió y
enlaza el documento con el detalle; los planes conservan su historia, pero **lo
pendiente se lleva aquí**. Al cerrar un ítem: marcarlo `[x]` con la fecha y el
commit, y dejarlo hasta la siguiente limpieza.

Última revisión: 8 de octubre de 2026. Próxima entrega: revisión de avance de la
aplicación (≈ 15 de octubre de 2026).

## 1. Interfaz (revisión vista por vista, en curso)

- [x] Íconos como recursos de Qt (`iconos.qrc`) — 7 oct.
- [x] Resultados: animación, gráficas (claves corregidas, desplazamientos) y tabla
      (columnas únicas, csv) — 7–8 oct.
- [x] Dibujo: datos, mallado, materiales, puntos materiales y contornos; gravedad al
      diálogo de etapas; flecha de fuerza corregida — 8 oct.
- [x] Menú de ejecutar: selección y fps guardados en el proyecto
      (`CONFIGANALISIS.PUNTOSMATERIAL_ANALISIS`, `CONTORNOS_ANALISIS`, `FPS`),
      resumen de etapas en el panel, fps al diálogo de etapas, verificación de
      puntos dentro de la malla corregida — 8 oct. Consolidación 1D desde el botón
      Ejecutar igual bit a bit a la corrida del 7 oct.
- [x] Proyectos leídos y escritos en UTF-8 (antes cp1252: un archivo UTF-8 hecho
      fuera de la aplicación quedaba con tildes dañadas al guardarlo) — 8 oct.
- [ ] Revisar las vistas que faltan: ventana principal, inicio, configuración,
      tarjetas y diálogo de progreso del análisis.
- [ ] Reporte PDF: el botón está oculto. Rehacerlo con etapas, gráficas reales y
      claves actuales (`controller_MenuResultTable.signalGeneratePdf`).
- [ ] "Campo de vectores" de la animación de resultados: confirmar que las flechas
      apuntan en el sentido correcto (la del dibujo estaba invertida).
- [ ] Unas 80 rutas `app/resources/...` escritas en las vistas: pasarlas a `:/...`
      para que la aplicación funcione aunque no se ejecute desde la raíz del repo.
- [ ] Etapa cuasi-estática que se detiene sin converger: hoy solo avisa en consola;
      el mensaje final debería decirlo ([plan_fase_b.md](plan_fase_b.md), nota del
      25 sep.).
- [ ] Menor: reglas de estilo sobrantes de widgets borrados en
      `widget_draw_menu_data.ui` (`frame_data2`, `SubTitle3`).

## 2. Cargas

- [ ] **Cargas por etapa**: la velocidad inicial se queda en las partículas; cada
      etapa activa sus propios juegos de fuerzas. Lo pide el muro (relleno y
      sobrecarga en etapas distintas)
      ([plan_simplificacion_cargas.md §8](plan_simplificacion_cargas.md)).

## 3. Doble fase (consolidación)

- [ ] **Base drenante**: casilla "Drenante" en cada restricción (clave `DRENANTE`,
      apagada por defecto = comportamiento actual). El motor recibe una lista de
      nodos para el esqueleto y otra para el agua; variante nueva de las funciones
      de contorno de `dos_fases.py` sin tocar las originales. Validación: la
      consolidación 1D sigue idéntica bit a bit y, con la base drenante, reproduce
      Terzaghi con doble drenaje (camino H/2). Estimado: 1 día. Al hacerlo, poner
      en los contornos el tooltip sobre drenaje/impermeabilidad.
- [ ] Borde impermeable que se mueve (p. ej. placa de carga): en la formulación v-w
      exige w·n = v·n, no w = 0. Necesita una condición nueva en el motor y su
      validación. Trabajo futuro.
- [ ] Restricciones actuales de la etapa de consolidación: un solo material y sin
      multicuerpo ([plan_dos_fases_ui.md](plan_dos_fases_ui.md), decisión 3).

## 4. Validación y decisiones de modelo

- [ ] Tolerancia de la capacidad portante: el oráculo solo se reproduce con
      `tolff = 0.011`; con 0.01 los esfuerzos cambian ~15 %. Estudio de
      sensibilidad y decidir la línea base
      ([plan_pre_validacion.md §5.5](plan_pre_validacion.md)).
- [ ] Talud: fase de falla de dos cuerpos reanudando desde el checkpoint del
      geostático ([plan_pre_validacion.md](plan_pre_validacion.md),
      [plan_fase_b.md](plan_fase_b.md)).
- [ ] Partículas de frontera: decidir y justificar qué función se adopta en la punta
      de la cuña ([deteccion_particulas_frontera.md §8](deteccion_particulas_frontera.md)).
- [ ] Extras si queda tiempo: `Disc.py` (contacto con solución analítica) y
      `Collapse_contact.py` ([plan_fase_b.md](plan_fase_b.md)).

## 5. Contacto

- [ ] Normales en superficies inclinadas: el gradiente de masa da errores de
      15–40° y frena el deslizamiento; hoy se usa la normal vertical. Trabajo
      futuro: normales desde la geometría
      ([contacto_multicuerpo.md](contacto_multicuerpo.md)).
- [ ] Caso del muro en voladizo (objetivo de la tesis), trabajado fuera de este
      repositorio: requiere normales horizontales en el contacto muro–relleno y
      revisar el amortiguamiento local en el paso multicuerpo antes de traerlo.

## 6. Rendimiento

- [ ] Índice inverso nodo → índice activo y partículas por elemento (CSR): sin
      cambio en los resultados, 10–40x estimado. Luego escalado de masa
      ([rendimiento_y_costo_computacional.md §6](rendimiento_y_costo_computacional.md)).
