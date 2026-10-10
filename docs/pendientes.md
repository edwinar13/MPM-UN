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
- [x] Ventana principal y configuración: menú Vista conectado (F5–F9), menús sin
      función retirados (importar/exportar, copiar/pegar/cortar, regla, dibujo,
      ayuda), tabla de atajos corregida, caja de búsqueda retirada — 8 oct.
- [x] Ejemplos de la página de inicio: las cuatro tarjetas abren los proyectos
      validados de `test/7` (viga, capacidad portante, talud, consolidación 1D),
      guardados en `app/resources/ejemplos` sin resultados. Al hacer clic se pide
      dónde guardar la copia y se abre lista para correr; el original no se toca.
      Se retiraron los `.mpm` de 2022 y la tarjeta del disco — 9 oct.
- [ ] Imágenes de las tarjetas de ejemplo (las cambia el autor).
- [ ] Reporte PDF: el botón está oculto. Rehacerlo con etapas, gráficas reales y
      claves actuales (`controller_MenuResultTable.signalGeneratePdf`).
- [x] "Campo de vectores" de la animación de resultados: revisado, apunta bien
      (la flecha se dibuja en coordenadas de escena y la vista invierte el eje y;
      la del dibujo fallaba porque ignora la transformación) — 8 oct.
- [x] Rutas `app/resources/...` del código: íconos a `:/iconos/...`; fuentes y
      `db_mpmun.json`/`Config.json` desde `config.RESOURCES_DIR`. La aplicación ya
      no depende del directorio desde el que se ejecute — 8 oct.
- [x] Etapa cuasi-estática que se detiene sin converger (tope de iteraciones o de
      tiempo) o sin convergencia evaluable: diálogo de avisos al terminar — 8 oct.
- [x] Reglas de estilo con `#nombre` de widgets que ya no existen: 121 selectores
      retirados de 12 `.ui`, vistas idénticas píxel a píxel antes y después — 8 oct.
- [x] Tamaño de malla con 4 decimales (antes 2: no se podía armar 7×7 partículas
      por elemento de 0.1 m); tooltip con los datos del punto material bajo el
      puntero y, al seleccionar puntos, suma y valores de sus fuerzas — 8 oct.
- [x] Animación de resultados: selector de etapa (reproduce todas o una, con el
      tiempo propio de la etapa: incremento o segundos) y campo "Ir al frame".
      Los resultados guardan el material de cada grupo por etapa y el color por
      material cambia al entrar a la etapa que lo cambia (falla del talud) — 9 oct.

## 2. Cargas

- [ ] **Cargas por etapa**: la velocidad inicial se queda en las partículas; cada
      etapa activa sus propios juegos de fuerzas. Lo pide el muro (relleno y
      sobrecarga en etapas distintas)
      ([plan_simplificacion_cargas.md §8](plan_simplificacion_cargas.md)).
- [ ] **Carga distribuida sobre una línea**: dar q [kPa] y un tramo, y que la app
      reparta F = q·L/n entre las partículas de ese borde. Hoy se escribe la fuerza
      de cada partícula a mano (p. ej. −0.142857142857143 en la consolidación 1D),
      con riesgo de decimales mal copiados o de dejar alguna sin carga. El borde
      se debe buscar con tolerancia (ver `traction_forces` en `motorMPM/mesh.py`,
      corregido el 8 oct.: la igualdad exacta dejaba una partícula por fuera).

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

- [x] Tolerancia de la capacidad portante: `tolff = 0.011`, la misma de
      `Ca_portante2.py` (con 0.01 los esfuerzos cambian ~15 %;
      [plan_pre_validacion.md §5.5](plan_pre_validacion.md)) — 9 oct.
- [x] Talud: fase de falla de dos cuerpos reanudando desde el checkpoint del
      geostático — idéntica bit a bit a la referencia desde el mismo geostático
      ([plan_fase_b.md §6.4](plan_fase_b.md)), 25 sep.
- [x] Talud armado desde la interfaz con las mismas 6740 partículas del script:
      la malla Estructurada dejaba por fuera los 40 centros que caen justo sobre
      la línea del talud (ahora un punto sobre el borde cuenta como dentro, como
      en el script) — 9 oct.
- [x] Corridas definitivas en `test/7`: viga, capacidad portante, talud de dos
      etapas y consolidación armados y corridos desde la interfaz y comparados
      con sus referencias
      ([validaciones_definitivas.md](Importantes_para_tesis/validaciones_definitivas.md))
      — 9 oct.
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
- [x] Animación de resultados en modelos grandes, arreglos rápidos: no se mueven
      ni recolorean flechas y etiquetas ocultas, las visibilidades ya no se
      cambian al pintar y la escena de resultados no usa índice espacial. Talud
      de 6740 partículas: de ~1.1 s a ~0.4 s por frame, imagen idéntica píxel a
      píxel — 9 oct.
- [ ] **Animación con una sola capa de partículas** (postergado, 9 oct.: no se
      hace por ahora): un ítem que dibuja todas las
      partículas de una vez, con los colores del frame calculados con numpy, en
      lugar de 4 ítems de Qt por partícula (punto, círculo, flecha, texto).
      Estimado: decenas de ms por frame en el talud (hoy ~0.4 s). Hay que
      rehacer encima etiquetas, flechas, panel de detalle y la selección de
      puntos para gráficas. ~1 día.
- [ ] **Tamaño de los proyectos con resultados** (postergado, 9 oct.: no se hace
      por ahora): el talud definitivo pesa 430 MB y tarda ~75 s en abrir
      (`json` con todos los frames de las 6740 partículas, 18 campos, como
      listas de texto). Medido el 9 oct.: ~26 s leer el `json` y ~41 s armar la
      escena de resultados; igual antes y después de los cambios de la
      animación. Opciones: guardar los resultados aparte en binario (`.npz`
      junto al `.json`), o en float32 y sin campos derivables (DESPL*,
      magnitudes XY); revisar también por qué tarda tanto armar la escena.
      Decidir antes de que crezcan los casos del muro.
