from PySide6.QtCore import (Slot, Signal, QObject)
from PySide6.QtWidgets import QDialog
from views.draw.view_WidgetDrawMenuExecute import ViewWidgetDrawMenuExecute
from models.model_ProjectCurrent import ModelProjectCurrent

from models.model_execute_analysis import ModelExcuteAnalysisMPM
from models.model_analysis_config import AnalysisConfig, TimeConfig
from models.analysis_utils import compute_min_dt, build_time_arrays
from views.view_DialogStages import DialogStages

from ui.ui_dialog_loanding import Ui_DialogLoanding


class AnalysisProgressDialog(QDialog, Ui_DialogLoanding):
    signal_cancelled = Signal()
    signal_paused = Signal()
    signal_resumed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("Ejecutando análisis")
        self.cancel_button.clicked.connect(self.cancelAnalysis)
        self.pause_button.clicked.connect(self.pauseAnalysis)
        self.acept_button.clicked.connect(self.acceptAnalysis)


        self.cancelled = False
        self.paused = False
        self.accepted = False
        self.configUI()
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def configUI(self):
        self.acept_button.setEnabled(False)
        self.acept_button.setVisible(False)

    def acceptAnalysis(self):
        self.accepted = True


    def cancelAnalysis(self):
        self.cancelled = True
        self.close()

    def pauseAnalysis(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.setText("Reanudar")
            self.signal_paused.emit()

        else:
            self.pause_button.setText("Pausar")
            self.signal_resumed.emit()

    def setQuestion(self, question):
        self.question_label.setText(question)

    def setStatus(self, error=False, status =""):
        self.status_label.setText(status)
        if error:
            self.status_label.setStyleSheet("color: #f36c42")
        else:
            '''
            QLabel#status_label{
                    font: 300 10pt "Ubuntu";
                    color: #DDDDDD;
                margin-left: 10px;
                }
            '''
            self.status_label.setStyleSheet("color: #DDDDDD")

    def setTimer(self, time):
        self.timer_label.setText(time)

    def setProgress(self, value):
        self.progress_bar.setValue(value)

    def setViewError(self):
        self.acept_button.setEnabled(True)
        self.acept_button.setVisible(True)

        self.pause_button.setEnabled(False)
        self.pause_button.setVisible(False)




class ControllerMenuExecute(QObject):

    signal_enable_results =Signal()
    signal_update_menu_result = Signal()

    def __init__(self) -> None:
        super().__init__()
        self.view_menu_execute = ViewWidgetDrawMenuExecute()
        self.model_current_project = None
        self.model_result = None
        self.list_controller_card=[]

        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """
        self.view_menu_execute.signal_execute.connect(self.executeAnalysis)
        self.view_menu_execute.signal_state_view_boundary.connect(self.stateViewBoundary)
        self.view_menu_execute.signal_stages.connect(self.openStagesDialog)

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_result = model_current_project.getModelResult()

    def activateMenu(self):
        self.view_menu_execute.activateMenu()

    def configDrawMenuExecute(self):
        """Puebla las listas de puntos materiales / contornos y el fps.

        Toda la configuración del análisis (Courant, tiempo, damping,
        incrementos, plasticidad...) vive en las ETAPAS y se edita en
        DialogStages; el panel solo conserva lo que no es por-etapa.
        """
        self.setListPointsMaterialView()
        self.setListBoundariesView()
        if self.model_result.getDataTimes():
            fps = self.model_result.getDataTimes()['FPS']
            self.view_menu_execute.setFps(fps)

    def setListPointsMaterialView(self):
        self.view_menu_execute.removeItemsListsMaterialPoint()

        result_point_materia = self.model_result.getPointMaterials()
        ids_result_point_materia = list(result_point_materia.keys())

        points_material_from = []
        points_material_to = []
        models_points_materials = self.model_current_project.getModelsPointsMaterials()

        for id_PM in models_points_materials:
            name_PM = models_points_materials[id_PM].getName()
            property_PM = models_points_materials[id_PM].getProperty()
            color_PM = property_PM.getColor()
            if id_PM in ids_result_point_materia:
                points_material_to.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
            else:
                points_material_from.append({'name': name_PM, 'id': id_PM, 'color': color_PM})

        self.view_menu_execute.addItemsListsMaterialPointFrom(points_material_from)
        self.view_menu_execute.addItemsListsMaterialPointTo(points_material_to)

    def setListBoundariesView(self):
        self.view_menu_execute.removeItemsListsBoundaries()

        result_boundaries = self.model_result.getBoundarys()
        ids_result_boundaries = list(result_boundaries.keys())

        boundaries_from = []
        boundaries_to = []
        models_boundaries = self.model_current_project.getModelsBoundaries()

        for id_boundary in models_boundaries:
            name_boundary = models_boundaries[id_boundary].getName()
            if id_boundary in ids_result_boundaries:
                boundaries_to.append({'name': name_boundary, 'id': id_boundary})
            else:
                boundaries_from.append({'name': name_boundary, 'id': id_boundary})

        self.view_menu_execute.addItemsListsBoundariesFrom(boundaries_from)
        self.view_menu_execute.addItemsListsBoundariesTo(boundaries_to)

    def newItemsListsMaterialPoint(self, id_material_point):
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        name_PM = models_points_materials[id_material_point].getName()
        color_PM = models_points_materials[id_material_point].getColor()
        self.view_menu_execute.addItemsListsMaterialPointFrom([{'name': name_PM, 'id': id_material_point, 'color': color_PM}])

    def newItemsListsBoundaries(self, id_boundary):
        models_boundaries = self.model_current_project.getModelsBoundaries()
        name_boundary = models_boundaries[id_boundary].getName()
        self.view_menu_execute.addItemsListsBoundariesFrom([{'name': name_boundary, 'id': id_boundary}])

    def getView(self):
        return self.view_menu_execute

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################

    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::
    @Slot()
    def executeAnalysis(self):
        analysis_dialog = AnalysisProgressDialog(self.view_menu_execute)
        analysis_dialog.show()
        analysis_dialog.rejected.connect(analysis_dialog.cancelAnalysis)

        list_point_material = self.view_menu_execute.getListExecutePointMaterial()
        list_boundaries = self.view_menu_execute.getListExecuteBoundaries()

        # verificar que los puntos materiales y los contornos esten seleccionados
        if not list_point_material:
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los puntos materiales")
            return

        elif not list_boundaries:
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los contornos")
            return

        # verificar que los puntos materiales esten en la malla de fondo
        model_mesh_back = self.model_current_project.model_mesh_back
        nodes = model_mesh_back.getNodes()
        cells = model_mesh_back.getElements()

        for id_mp in list_point_material:
            model_mp = self.model_current_project.getModelsPointsMaterials()[id_mp]
            points = model_mp.getPoints()
            cells_by_point = self.findCellForPoints(material_points=points,
                                                    elements=cells,
                                                    nodes=nodes)

            if len(cells_by_point) != len(points):
                self.view_menu_execute.msnAlertDefault(True," pm fuera la malla de fondo '{}'".format(model_mp.getName()))
                analysis_dialog.close()
                return

        # ── Construir AnalysisConfig desde las ETAPAS configuradas ──
        gravity = self.model_current_project.getGravity()
        stage_dicts = self.model_current_project.getStages()
        if not stage_dicts:
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True, "Configura al menos una etapa de análisis")
            return

        fps = self.view_menu_execute.getFps()
        time_config = TimeConfig(fps=fps)
        analysis_config = AnalysisConfig.from_stage_dicts(
            stage_dicts=stage_dicts, gravity=gravity, time_config=time_config,
            resume_from_stage=self.model_current_project.getResumeFrom())

        # Semilla de tiempo (el executor recalcula dt/pasos por etapa)
        seed = self._build_seed_time(analysis_config, fps)
        if seed is None:
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True, "No se pudo calcular dt (revisa los materiales)")
            return
        dtime, tiempo, dtimegraphic, tiempographic, steps_time, steps_timegraphic, dataTime = seed

        print(f"[Controller] AnalysisConfig: {analysis_config}")

        analysis_mpm = ModelExcuteAnalysisMPM(
                                    analysis_dialog= analysis_dialog,
                                    model_current_project=self.model_current_project,
                                    model_result=self.model_result,
                                    dataTime=dataTime,
                                    list_boundaries=list_boundaries,
                                    list_point_material=list_point_material,
                                    dt_time=dtime,
                                    list_time=tiempo,
                                    steps_time=steps_time,
                                    dt_graphic= dtimegraphic,
                                    list_time_graphic=tiempographic,
                                    steps_time_graphic=steps_timegraphic,
                                    analysis_config=analysis_config)

        # Ejecutar con el método unificado
        state_ok = analysis_mpm.run()

        if state_ok:
            self.signal_enable_results.emit()
            analysis_dialog.close()
            if analysis_mpm.cancelled_partial:
                self.view_menu_execute.msnAlertDefault(
                    True, "Análisis cancelado: se guardaron los resultados parciales")
                print("[OK→] Análisis cancelado con resultados parciales guardados")
            else:
                self.view_menu_execute.msnAlertDefault(False,"Análisis ejecutado")
                print("[OK→] Análisis finalizado")
            self.signal_update_menu_result.emit()

        else:
            analysis_dialog.close()
            motivo = analysis_mpm.error_message or "Análisis cancelado"
            self.view_menu_execute.msnAlertDefault(True, motivo)
            print(f"[NOT→] {motivo}")

    # ::::::::::::::::::::   ETAPAS DE ANÁLISIS   ::::::::::::::::::::
    def _gather_selected_materials(self):
        """Materiales de los puntos materiales seleccionados en Ejecutar.

        Returns:
            (materials, prop_ids) donde materials es lista de
            (E, nu, rho[Mg/m³]) y prop_ids es la lista paralela de ids de
            propiedad. Ambas vacías si no hay selección.
        """
        list_mp = self.view_menu_execute.getListExecutePointMaterial()
        models_mp = self.model_current_project.models_material_point
        materials = []
        prop_ids = []
        for id_mp in list_mp:
            data = models_mp[id_mp].getProperty().getData()
            k = list(data.keys())[0]
            materials.append((
                data[k]["MODULOELASTICIDAD"],
                data[k]["RELACIONPOISSON"],
                data[k]["DENSIDAD"] / 1000.0,
            ))
            prop_ids.append(k)
        return materials, prop_ids

    def _build_seed_time(self, config, fps):
        """Semilla de dt/arrays de tiempo desde la 1ª etapa y los materiales
        seleccionados. El executor recalcula dt por etapa; esto solo
        inicializa el modelo y alimenta el diálogo de progreso y el guardado
        de metadatos (dataTime).

        Returns:
            (dt, tiempo, dt_graphic, tiempographic, steps, steps_graphic, dataTime)
            o None si no se pudo calcular.
        """
        materials, prop_ids = self._gather_selected_materials()
        if not materials:
            return None
        ele_size = self.model_current_project.model_mesh_back.getSizeElement()
        stage0 = config.stages[0]
        dt, cp, idx = compute_min_dt(materials, ele_size, stage0.courant_number)
        if dt is None:
            return None
        id_property = prop_ids[idx] if idx is not None else prop_ids[0]
        dur = stage0.analysis_time if (stage0.analysis_time and stage0.analysis_time > 0) else 1.0
        ta = build_time_arrays(dt, dur, fps)
        dataTime = {
            'id_property': id_property,
            'courant_number': stage0.courant_number,
            'analysis_time': dur,
            'fps': fps,
            'dt_analysis': dt,
            'dt_graphic': ta['dt_graphic'],
            'analysis_steps': ta['steps'],
            'graphic_steps': ta['steps_graphic'],
            'speed_cp': cp,
        }
        return (dt, ta['tiempo'], ta['dt_graphic'], ta['tiempographic'],
                ta['steps'], ta['steps_graphic'], dataTime)

    @Slot()
    def openStagesDialog(self):
        """Abre el diálogo de configuración de etapas de análisis."""
        def dt_provider(courant):
            materials, _ = self._gather_selected_materials()
            if not materials:
                return None
            ele_size = self.model_current_project.model_mesh_back.getSizeElement()
            dt, _, _ = compute_min_dt(materials, ele_size, courant)
            return dt

        dlg = DialogStages(self.model_current_project,
                           dt_provider=dt_provider,
                           parent=self.view_menu_execute)
        dlg.exec()

    @Slot(dict)
    def stateViewBoundary(self, data):
        self.model_current_project.stateViewBoundary(data)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def findCellForPoints(self, material_points, elements, nodes) -> dict:
        """Encuentra la celda a la que pertenece cada punto.
        Descripcion detallada de la función:
        Encuentra la celda a la que pertenece cada punto, para lo cual se
        recorre cada punto y se compara con las coordenadas de cada celda.

        Args:
            material_points (list): Lista de puntos materiales.
            elements (list): Lista de elementos  de la malla de fondo.
            nodes (list): Lista de nodos de la malla de fondo.
        Returns:
            dict: Diccionario con el punto y la celda a la que pertenece.
        """


        print("esto se puede optimizar no buscando primero en los vencinos hacia afura, sin tener que rrecorrer todos los elementos de la malla de fondo, solo los que estan cerca del punto material.")
        print("creo que esto se peude aplicar tambien en la busqueda de los puntos en el analisis, salbo que s eaga con gunciones d eforma o algo asi que sea mas directo")
        result = {}
        for point in material_points:
            ''' result: POINT#1'''
            ''' punto data:  {
                'COORDINATES': [1.25, 11.25],
                'VOLUME': 6.250000000000009,
                'VELOCITY': {'X': 0.0, 'Y': 0.0},
                'FORCE': {'X': 0.0, 'Y': 0.0}} '''
            for i, element in enumerate(elements):
                ''' element: ELEMENT#1'''
                ''' elemento data:  ['NODE#1', 'NODE#2', 'NODE#13', 'NODE#12'] '''

                '''   esto es de otra version
                x_values = [nodes[idx-1][0] for idx in element]
                y_values = [nodes[idx-1][1] for idx in element]
                min_x = min(x_values)
                max_x = max(x_values)
                min_y = min(y_values)
                max_y = max(y_values)

                '''
                min_x = 0
                min_y = 0

                max_x = max(
                    nodes[elements[element][0]]['COORDINATES'][0],
                    nodes[elements[element][1]]['COORDINATES'][0],
                    nodes[elements[element][2]]['COORDINATES'][0],
                    nodes[elements[element][3]]['COORDINATES'][0]
                )

                max_y = max(
                    nodes[elements[element][0]]['COORDINATES'][1],
                    nodes[elements[element][1]]['COORDINATES'][1],
                    nodes[elements[element][2]]['COORDINATES'][1],
                    nodes[elements[element][3]]['COORDINATES'][1]
                )


                x = material_points[point]['COORDINATES'][0]
                y = material_points[point]['COORDINATES'][1]
                if min_x <=  x <= max_x and min_y <= y <= max_y:
                    result.update({point: element})
                    break

        return result
