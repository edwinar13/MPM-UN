# MPM-UN

MPM-UN es una aplicación de simulación numérica desarrollada para análisis de elementos finitos utilizando el Método de Partículas de Malla (MPM). Esta herramienta está diseñada para facilitar la simulación y visualización de problemas de mecánica de sólidos deformables.

## Características

- **Interfaz Gráfica Intuitiva:** MPM-UN ofrece una interfaz de usuario intuitiva que permite a los usuarios configurar y ejecutar simulaciones de manera sencilla.
  
- **Simulación Numérica:** Utiliza el Método de Partículas de Malla (MPM) para resolver problemas de mecánica de sólidos deformables, permitiendo simular una amplia gama de fenómenos físicos.

- **Visualización de Resultados:** La aplicación proporciona herramientas para visualizar de forma interactiva los resultados de las simulaciones, incluyendo gráficos y animaciones.

- **Personalización y Configuración:** Permite a los usuarios personalizar los parámetros de simulación y configurar diferentes condiciones de contorno y materiales.

## Estructura del Proyecto

El proyecto sigue una estructura organizada que separa claramente la lógica de la aplicación en diferentes módulos:

- **app:** Contiene el código fuente de la aplicación, incluyendo los módulos para las vistas, modelos y controladores.
  
- **tests:** Contiene pruebas unitarias y de integración para garantizar la calidad del código.

- **docs:** Documentación del proyecto, incluyendo guías de instalación, uso y referencia técnica.

- **requirements.txt:** Archivo que especifica las dependencias del proyecto para facilitar la instalación del entorno de desarrollo.

## Requisitos del Sistema

- Python 3.x
- Bibliotecas especificadas en `requirements.txt`
- Sistema operativo compatible (Windows, Linux, macOS)

## Instalación

1. Clona el repositorio desde GitHub:

   ```bash
   git clone https://github.com/tu_usuario/MPM-UN.git
   ```

2. Navega al directorio del proyecto:

   ```bash
   cd MPM-UN
   ```

3. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Ejecuta el archivo `main.py` para iniciar la aplicación:

   ```bash
   python main.py
   ```

2. Utiliza la interfaz gráfica para configurar los parámetros de la simulación y ejecutarla.

## Contribución

Si deseas contribuir al desarrollo de MPM-UN, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu contribución (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commits (`git commit -am 'Agrega nueva característica'`).
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`).
5. Crea un pull request en GitHub.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).




#!En construcción¡

```
MPM-UN
├─ LICENSE
├─ README.md
├─ requirements.txt
├─ .gitignore
├─ .vscode/
├─ env/ 
├─ .git/
├─ app
│  ├─ ico.ico
│  ├─ main.py
│  ├─ controllers
│  │  ├─ controller_graphicsDraw.py
│  │  ├─ controller_graphicsResult.py
│  │  ├─ controller_MainWindow.py
│  │  ├─ controller_PageHome.py
│  │  ├─ controller_PageSetting.py
│  │  ├─ cards
│  │  │  ├─ controller_CardBoundary.py
│  │  │  ├─ controller_CardMaterialPoint.py
│  │  │  ├─ controller_CardMesh.py
│  │  │  ├─ controller_CardProject.py
│  │  │  ├─ controller_CardProperty.py
│  │  │  └─ controller_ResultCardPoint.py
│  │  ├─ draw
│  │  │  ├─ controller_MenuBoundary.py
│  │  │  ├─ controller_MenuData.py
│  │  │  ├─ controller_MenuExecute.py
│  │  │  ├─ controller_MenuMesh.py
│  │  │  ├─ controller_MenuPointMaterial.py
│  │  │  ├─ controller_MenuProperties.py
│  │  │  └─ controller_PageDraw.py
│  │  └─ results
│  │     ├─ controller_MenuResultAnimation.py
│  │     ├─ controller_MenuResultGraph.py
│  │     ├─ controller_MenuResultTable.py
│  │     └─ controller_PageResult.py
│  ├─ models
│  │  ├─ model_Boundary.py
│  │  ├─ model_ItemLine.py
│  │  ├─ model_ItemPoint.py
│  │  ├─ model_MaterialPoint.py
│  │  ├─ model_Mesh.py
│  │  ├─ model_ProjectCurrent.py
│  │  ├─ model_ProjectCurrentRepository.py
│  │  ├─ model_Projects.py
│  │  ├─ model_Property.py
│  │  ├─ model_Result.py
│  │  └─ model_SettingApp.py
│  ├─ motorMPM
│  │  ├─ ejecutarMPM.py
│  │  ├─ explicit.py
│  │  ├─ explicit2.py
│  │  ├─ explicit3.py
│  │  ├─ graphics.py
│  │  └─ mesh.py
│  ├─ resources
│  │  ├─ animations
│  │  │  └─ giphy.gif
│  │  ├─ css
│  │  │  └─ styles_oscuro.css
│  │  ├─ db_mpmun.json
│  │  ├─ ejemplos
│  │  │  ├─ Ejemplo capacidad portante.mpm
│  │  │  ├─ Ejemplo disco deslizando en plano inclinado.mpm
│  │  │  ├─ Ejemplo falla de talud elastoplastico.mpm
│  │  │  └─ Ejemplo vibracion barra empotrada.mpm
│  │  ├─ fuentes
│  │  │  ├─ Ubuntu-Bold.ttf
│  │  │  ├─ Ubuntu-BoldItalic.ttf
│  │  │  ├─ Ubuntu-Italic.ttf
│  │  │  ├─ Ubuntu-Light.ttf
│  │  │  ├─ Ubuntu-LightItalic.ttf
│  │  │  ├─ Ubuntu-Medium.ttf
│  │  │  ├─ Ubuntu-MediumItalic.ttf
│  │  │  └─ Ubuntu-Regular.ttf
│  │  ├─ iconos
│  │  │  ├─ excel.svg
│  │  │  ├─ iconos_analisis
│  │  │  │  └─ excute.svg
│  │  │  ├─ iconos_consola
│  │  │  │  ├─ code.svg
│  │  │  │  ├─ exit.svg
│  │  │  │  ├─ view_one.svg
│  │  │  │  ├─ view_two.svg
│  │  │  │  ├─ zoom_extend - copia.svg
│  │  │  │  ├─ zoom_extend.svg
│  │  │  │  └─ zoom_window.svg
│  │  │  ├─ iconos_frame_inicio
│  │  │  │  ├─ doc_basic.svg
│  │  │  │  ├─ doc_mpm.svg
│  │  │  │  ├─ new_p.svg
│  │  │  │  └─ open_p.svg
│  │  │  ├─ iconos_generales
│  │  │  │  ├─ edit.svg
│  │  │  │  ├─ exit_2.svg
│  │  │  │  └─ ok.svg
│  │  │  ├─ iconos_logo
│  │  │  │  ├─ Logo_V0.svg
│  │  │  │  ├─ Logo_V1.svg
│  │  │  │  └─ Logo_WindowIcon.svg
│  │  │  ├─ iconos_menu_draw_data
│  │  │  │  ├─ hide_show.svg
│  │  │  │  ├─ maximize.svg
│  │  │  │  └─ minimize.svg
│  │  │  ├─ iconos_menu_draw_mesh
│  │  │  │  ├─ click.svg
│  │  │  │  ├─ color.svg
│  │  │  │  ├─ colo_picker.svg
│  │  │  │  ├─ copy.svg
│  │  │  │  ├─ delete.svg
│  │  │  │  ├─ erase.svg
│  │  │  │  ├─ import.svg
│  │  │  │  ├─ label.svg
│  │  │  │  ├─ label_not.svg
│  │  │  │  ├─ line.svg
│  │  │  │  ├─ move.svg
│  │  │  │  ├─ not_view.svg
│  │  │  │  ├─ point.svg
│  │  │  │  ├─ point_in_lines.svg
│  │  │  │  ├─ polyline.svg
│  │  │  │  ├─ rectangle.svg
│  │  │  │  ├─ rotate.svg
│  │  │  │  ├─ rule.svg
│  │  │  │  ├─ select.svg
│  │  │  │  ├─ update.svg
│  │  │  │  ├─ view.svg
│  │  │  │  ├─ view_draw.svg
│  │  │  │  └─ view_draw_not.svg
│  │  │  ├─ iconos_menu_lateral
│  │  │  │  ├─ boundary.svg
│  │  │  │  ├─ config.svg
│  │  │  │  ├─ config_select.svg
│  │  │  │  ├─ control.svg
│  │  │  │  ├─ execute.svg
│  │  │  │  ├─ file.svg
│  │  │  │  ├─ home.svg
│  │  │  │  ├─ mesh.svg
│  │  │  │  ├─ particle.svg
│  │  │  │  └─ view.svg
│  │  │  ├─ iconos_menu_superior
│  │  │  │  ├─ export.svg
│  │  │  │  ├─ import.svg
│  │  │  │  ├─ new.svg
│  │  │  │  ├─ open.svg
│  │  │  │  ├─ recent.svg
│  │  │  │  ├─ redo.svg
│  │  │  │  ├─ save.svg
│  │  │  │  └─ undo.svg
│  │  │  ├─ iconos_msg
│  │  │  │  ├─ error.svg
│  │  │  │  ├─ ok.svg
│  │  │  │  ├─ question.svg
│  │  │  │  └─ warning.svg
│  │  │  ├─ iconos_status_bar
│  │  │  │  ├─ ortho.svg
│  │  │  │  ├─ osnap.svg
│  │  │  │  └─ snap_grid.svg
│  │  │  ├─ icono_result
│  │  │  │  ├─ add.svg
│  │  │  │  ├─ adelante.svg
│  │  │  │  ├─ atras.svg
│  │  │  │  ├─ graphics.svg
│  │  │  │  ├─ pause.svg
│  │  │  │  ├─ play.svg
│  │  │  │  ├─ stop.svg
│  │  │  │  ├─ view_board.svg
│  │  │  │  ├─ view_graphics.svg
│  │  │  │  └─ view_points.svg
│  │  │  └─ select.svg
│  │  └─ imagenes
│  │     ├─ ejemplo_capacidad_portante.png
│  │     ├─ ejemplo_disco.png
│  │     ├─ ejemplo_talud.png
│  │     └─ ejemplo_viga.png
│  ├─ ui
│  │  ├─ dialog_loanding.ui
│  │  ├─ dialog_msg.ui
│  │  ├─ frame_draw.ui
│  │  ├─ frame_draw_1.ui
│  │  ├─ frame_home.ui
│  │  ├─ frame_result.ui
│  │  ├─ frame_setting.ui
│  │  ├─ main_window.ui
│  │  ├─ splash_screen.ui
│  │  ├─ ui_dialog_loanding.py
│  │  ├─ ui_dialog_msg.py
│  │  ├─ ui_frame_draw.py
│  │  ├─ ui_frame_draw_1.py
│  │  ├─ ui_frame_home.py
│  │  ├─ ui_frame_result.py
│  │  ├─ ui_frame_setting.py
│  │  ├─ ui_main_window.py
│  │  ├─ ui_splash_screen.py
│  │  ├─ ui_widget_draw_boundary_card.py
│  │  ├─ ui_widget_draw_material_point_card.py
│  │  ├─ ui_widget_draw_menu_boundary.py
│  │  ├─ ui_widget_draw_menu_data.py
│  │  ├─ ui_widget_draw_menu_execute.py
│  │  ├─ ui_widget_draw_menu_mesh.py
│  │  ├─ ui_widget_draw_menu_pointMaterial.py
│  │  ├─ ui_widget_draw_menu_properties.py
│  │  ├─ ui_widget_draw_mesh_card.py
│  │  ├─ ui_widget_draw_property_card.py
│  │  ├─ ui_widget_home_card.py
│  │  ├─ ui_widget_result_card_point.py
│  │  ├─ ui_widget_result_menu_animation.py
│  │  ├─ ui_widget_result_menu_graph.py
│  │  ├─ ui_widget_result_menu_table.py
│  │  ├─ widget_draw_boundary_card.ui
│  │  ├─ widget_draw_material_point_card.ui
│  │  ├─ widget_draw_menu_boundary.ui
│  │  ├─ widget_draw_menu_data.ui
│  │  ├─ widget_draw_menu_execute.ui
│  │  ├─ widget_draw_menu_mesh.ui
│  │  ├─ widget_draw_menu_pointMaterial.ui
│  │  ├─ widget_draw_menu_properties.ui
│  │  ├─ widget_draw_mesh_card.ui
│  │  ├─ widget_draw_property_card.ui
│  │  ├─ widget_home_card.ui
│  │  ├─ widget_result_card_point.ui
│  │  ├─ widget_result_menu_animation.ui
│  │  ├─ widget_result_menu_graph.ui
│  │  └─ widget_result_menu_table.ui
│  ├─ utils
│  │  ├─ class_general.py
│  │  ├─ class_ui_dialog_loanding.py
│  │  ├─ class_ui_dialog_msg.py
│  │  ├─ command_GraphicsDraw.py
│  │  ├─ general_functions.py
│  │  ├─ items_GraphicsDraw.py
│  │  └─ items_GraphicsResult.py
│  └─ views
│     ├─ view_GraphicsDraw.py
│     ├─ view_GraphicsResult.py
│     ├─ view_MainWindow.py
│     ├─ view_PageHome.py
│     ├─ view_PageSetting.py
│     ├─ view_SplashScreen.py
│     ├─ cards
│     │  ├─ view_WidgetCardBoundary.py
│     │  ├─ view_WidgetCardMaterialPoint.py
│     │  ├─ view_WidgetCardMesh.py
│     │  ├─ view_WidgetCardProject.py
│     │  ├─ view_WidgetCardProperty.py
│     │  └─ view_WidgetResultCardPoint.py
│     ├─ draw
│     │  ├─ view_PageDraw.py
│     │  ├─ view_WidgetDrawMenuBoundary.py
│     │  ├─ view_WidgetDrawMenuData.py
│     │  ├─ view_WidgetDrawMenuExecute.py
│     │  ├─ view_WidgetDrawMenuMesh.py
│     │  ├─ view_WidgetDrawMenuPointMaterial.py
│     │  └─ view_WidgetDrawMenuProperties.py
│     ├─ results
│     │  ├─ view_PageResult.py
│     │  ├─ view_WidgetResultMenuAnimation.py
│     │  ├─ view_WidgetResultMenuGraph.py
│        └─ view_WidgetResultMenuTable.py
└─ tests
   └─ archivos_mpm
      ├─ 0_archivos_mpm_dwg
      │  ├─ 000.mpm
      │  ├─ 1 - copia.mpm
      │  ├─ 1.mpm
      │  ├─ 123.mpm
      │  ├─ Borar ok.mpm
      │  ├─ borrar 2.mpm
      │  ├─ borrar banda.mpm
      │  ├─ borrar.csv
      │  ├─ borrar.json
      │  ├─ borrar.mpm
      │  ├─ Borrarrarr.mpm
      │  ├─ EJEMPLO.mpm
      │  ├─ intersecciones.dwg
      │  ├─ intersecciones.dxf
      │  ├─ iones.mpm
      │  ├─ Modelo-2.dxf
      │  ├─ Modelo.dwg
      │  ├─ Modelo.dxf
      │  ├─ out.txt
      │  ├─ Prueba.py
      │  ├─ sample_.mpm
      │  ├─ sample_basic.mpm
      │  ├─ sample_x10.mpm
      │  ├─ viga simple 20231120.mpm
      │  ├─ viga simple 20231129-c.mpm
      │  ├─ viga simple 20231129-d.mpm
      │  ├─ viga simple 20231129-e.mpm
      │  ├─ viga simple 20231129-f.mpm
      │  ├─ viga simple 20231129-g.mpm
      │  ├─ viga simple 20231129.mpm
      │  └─ viga simple.mpm
      └─ 1_archivos_mpm_v1
         ├─ 1_beam.mpm
         ├─ barra_axial_empotrada.mpm
         └─ viga_en_voladizo.mpm

```