# MPM-UN

#!En construcción¡
```
MPM-UN
├─ .archivos_mpm_v1(ejemplos)
│  ├─ 1_beam.mpm
│  ├─ barra_axial_empotrada.mpm
│  └─ viga_en_voladizo.mpm
├─ clases
│  ├─ class_general.py
│  ├─ class_ui_dialog_loanding.py
│  ├─ class_ui_dialog_msg.py
│  ├─ command_GraphicsDraw.py
│  ├─ Controlador
│  │  ├─ controller_CardBoundary.py
│  │  ├─ controller_CardMaterialPoint.py
│  │  ├─ controller_CardMesh.py
│  │  ├─ controller_CardProject.py
│  │  ├─ controller_CardProperty.py
│  │  ├─ controller_graphicsDraw.py
│  │  ├─ controller_graphicsResult.py
│  │  ├─ controller_MainWindow.py
│  │  ├─ controller_MenuBoundary.py
│  │  ├─ controller_MenuData.py
│  │  ├─ controller_MenuExecute.py
│  │  ├─ controller_MenuMesh.py
│  │  ├─ controller_MenuPointMaterial.py
│  │  ├─ controller_MenuProperties.py
│  │  ├─ controller_PageDraw.py
│  │  ├─ controller_PageHome.py
│  │  ├─ controller_PageSetting.py
│  │  ├─ controller_ResultCardPoint.py
│  │  └─ Resultados
│  │     ├─ controller_MenuResultAnimation.py
│  │     ├─ controller_MenuResultGraph.py
│  │     ├─ controller_MenuResultTable.py
│  │     └─ controller_PageResult.py
│  ├─ general_functions.py
│  ├─ items_GraphicsDraw.py
│  ├─ items_GraphicsResult.py
│  ├─ Modelo
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
│  └─ Vista
│     ├─ Resultados
│     │  ├─ view_PageResult.py
│     │  ├─ view_WidgetResultMenuAnimation.py
│     │  ├─ view_WidgetResultMenuGraph.py
│     │  └─ view_WidgetResultMenuTable.py
│     ├─ view_GraphicsDraw.py
│     ├─ view_GraphicsResult.py
│     ├─ view_MainWindow.py
│     ├─ view_PageDraw.py
│     ├─ view_PageHome.py
│     ├─ view_PageSetting.py
│     ├─ view_SplashScreen.py
│     ├─ view_WidgetCardBoundary.py
│     ├─ view_WidgetCardMaterialPoint.py
│     ├─ view_WidgetCardMesh.py
│     ├─ view_WidgetCardProject.py
│     ├─ view_WidgetCardProperty.py
│     ├─ view_WidgetDrawMenuBoundary.py
│     ├─ view_WidgetDrawMenuData.py
│     ├─ view_WidgetDrawMenuExecute.py
│     ├─ view_WidgetDrawMenuMesh.py
│     ├─ view_WidgetDrawMenuPointMaterial.py
│     ├─ view_WidgetDrawMenuProperties.py
│     └─ view_WidgetResultCardPoint.py
├─ css
│  └─ styles_oscuro.css
├─ db
│  └─ db_mpmun.json
├─ ico.ico
├─ LICENSE
├─ main.py
├─ motorMPM
│  ├─ ejecutarMPM.py
│  ├─ explicit.py
│  ├─ explicit2.py
│  ├─ explicit3.py
│  ├─ graphics.py
│  └─ mesh.py
├─ README.md
├─ recursos
│  ├─ animations
│  │  └─ giphy.gif
│  ├─ ejemplos
│  │  ├─ Ejemplo capacidad portante.mpm
│  │  ├─ Ejemplo disco deslizando en plano inclinado.mpm
│  │  ├─ Ejemplo falla de talud elastoplastico.mpm
│  │  └─ Ejemplo vibracion barra empotrada.mpm
│  ├─ fuentes
│  │  ├─ Ubuntu-Bold.ttf
│  │  ├─ Ubuntu-BoldItalic.ttf
│  │  ├─ Ubuntu-Italic.ttf
│  │  ├─ Ubuntu-Light.ttf
│  │  ├─ Ubuntu-LightItalic.ttf
│  │  ├─ Ubuntu-Medium.ttf
│  │  ├─ Ubuntu-MediumItalic.ttf
│  │  └─ Ubuntu-Regular.ttf
│  ├─ iconos
│  │  ├─ excel.svg
│  │  ├─ iconos_analisis
│  │  │  └─ excute.svg
│  │  ├─ iconos_consola
│  │  │  ├─ code.svg
│  │  │  ├─ exit.svg
│  │  │  ├─ view_one.svg
│  │  │  ├─ view_two.svg
│  │  │  ├─ zoom_extend - copia.svg
│  │  │  ├─ zoom_extend.svg
│  │  │  └─ zoom_window.svg
│  │  ├─ iconos_frame_inicio
│  │  │  ├─ doc_basic.svg
│  │  │  ├─ doc_mpm.svg
│  │  │  ├─ new_p.svg
│  │  │  └─ open_p.svg
│  │  ├─ iconos_generales
│  │  │  ├─ edit.svg
│  │  │  ├─ exit_2.svg
│  │  │  └─ ok.svg
│  │  ├─ iconos_logo
│  │  │  ├─ Logo_V0.svg
│  │  │  ├─ Logo_V1.svg
│  │  │  └─ Logo_WindowIcon.svg
│  │  ├─ iconos_menu_draw_data
│  │  │  ├─ hide_show.svg
│  │  │  ├─ maximize.svg
│  │  │  └─ minimize.svg
│  │  ├─ iconos_menu_draw_mesh
│  │  │  ├─ click.svg
│  │  │  ├─ color.svg
│  │  │  ├─ colo_picker.svg
│  │  │  ├─ copy.svg
│  │  │  ├─ delete.svg
│  │  │  ├─ erase.svg
│  │  │  ├─ import.svg
│  │  │  ├─ label.svg
│  │  │  ├─ label_not.svg
│  │  │  ├─ line.svg
│  │  │  ├─ move.svg
│  │  │  ├─ not_view.svg
│  │  │  ├─ point.svg
│  │  │  ├─ point_in_lines.svg
│  │  │  ├─ polyline.svg
│  │  │  ├─ rectangle.svg
│  │  │  ├─ rotate.svg
│  │  │  ├─ rule.svg
│  │  │  ├─ select.svg
│  │  │  ├─ update.svg
│  │  │  ├─ view.svg
│  │  │  ├─ view_draw.svg
│  │  │  └─ view_draw_not.svg
│  │  ├─ iconos_menu_lateral
│  │  │  ├─ boundary.svg
│  │  │  ├─ config.svg
│  │  │  ├─ config_select.svg
│  │  │  ├─ control.svg
│  │  │  ├─ execute.svg
│  │  │  ├─ file.svg
│  │  │  ├─ home.svg
│  │  │  ├─ mesh.svg
│  │  │  ├─ particle.svg
│  │  │  └─ view.svg
│  │  ├─ iconos_menu_superior
│  │  │  ├─ export.svg
│  │  │  ├─ import.svg
│  │  │  ├─ new.svg
│  │  │  ├─ open.svg
│  │  │  ├─ recent.svg
│  │  │  ├─ redo.svg
│  │  │  ├─ save.svg
│  │  │  └─ undo.svg
│  │  ├─ iconos_msg
│  │  │  ├─ error.svg
│  │  │  ├─ ok.svg
│  │  │  ├─ question.svg
│  │  │  └─ warning.svg
│  │  ├─ iconos_status_bar
│  │  │  ├─ ortho.svg
│  │  │  ├─ osnap.svg
│  │  │  └─ snap_grid.svg
│  │  ├─ icono_result
│  │  │  ├─ add.svg
│  │  │  ├─ adelante.svg
│  │  │  ├─ atras.svg
│  │  │  ├─ graphics.svg
│  │  │  ├─ pause.svg
│  │  │  ├─ play.svg
│  │  │  ├─ stop.svg
│  │  │  ├─ view_board.svg
│  │  │  ├─ view_graphics.svg
│  │  │  └─ view_points.svg
│  │  └─ select.svg
│  └─ imagenes
│     ├─ ejemplo_capacidad_portante.png
│     ├─ ejemplo_disco.png
│     ├─ ejemplo_talud.png
│     └─ ejemplo_viga.png
├─ setup.py
└─ ui
   ├─ dialog_loanding.ui
   ├─ dialog_msg.ui
   ├─ frame_draw.ui
   ├─ frame_draw_1.ui
   ├─ frame_home.ui
   ├─ frame_result.ui
   ├─ frame_setting.ui
   ├─ main_window.ui
   ├─ splash_screen.ui
   ├─ ui_dialog_loanding.py
   ├─ ui_dialog_msg.py
   ├─ ui_frame_draw.py
   ├─ ui_frame_draw_1.py
   ├─ ui_frame_home.py
   ├─ ui_frame_result.py
   ├─ ui_frame_setting.py
   ├─ ui_main_window.py
   ├─ ui_splash_screen.py
   ├─ ui_widget_draw_boundary_card.py
   ├─ ui_widget_draw_material_point_card.py
   ├─ ui_widget_draw_menu_boundary.py
   ├─ ui_widget_draw_menu_data.py
   ├─ ui_widget_draw_menu_execute.py
   ├─ ui_widget_draw_menu_mesh.py
   ├─ ui_widget_draw_menu_pointMaterial.py
   ├─ ui_widget_draw_menu_properties.py
   ├─ ui_widget_draw_mesh_card.py
   ├─ ui_widget_draw_property_card.py
   ├─ ui_widget_home_card.py
   ├─ ui_widget_result_card_point.py
   ├─ ui_widget_result_menu_animation.py
   ├─ ui_widget_result_menu_graph.py
   ├─ ui_widget_result_menu_table.py
   ├─ Untitled-1.html
   ├─ widget_draw_boundary_card.ui
   ├─ widget_draw_material_point_card.ui
   ├─ widget_draw_menu_boundary.ui
   ├─ widget_draw_menu_data.ui
   ├─ widget_draw_menu_execute.ui
   ├─ widget_draw_menu_mesh.ui
   ├─ widget_draw_menu_pointMaterial.ui
   ├─ widget_draw_menu_properties.ui
   ├─ widget_draw_mesh_card.ui
   ├─ widget_draw_property_card.ui
   ├─ widget_home_card.ui
   ├─ widget_result_card_point.ui
   ├─ widget_result_menu_animation.ui
   ├─ widget_result_menu_graph.ui
   └─ widget_result_menu_table.ui

```