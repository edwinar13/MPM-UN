from PySide6.QtCore import (Slot, Signal, QObject)
from PySide6.QtWidgets import QDialog
from views.draw.view_WidgetDrawMenuExecute import ViewWidgetDrawMenuExecute
from models.model_ProjectCurrent import ModelProjectCurrent

from models.model_execute_analysis import ModelExcuteAnalysisMPM
from models.model_analysis_config import AnalysisConfig, TimeConfig, StageType
from models.analysis_utils import compute_min_dt, compute_two_phase_dt, build_time_arrays
from views.view_DialogStages import DialogStages, stages_summary_html

from ui.ui_dialog_loanding import Ui_DialogLoanding
from utils.class_ui_dialog_msg import DialogMsg


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
        self.view_menu_execute.signal_selection_changed.connect(self.saveSelection)

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_result = model_current_project.getModelResult()

    def configDrawMenuExecute(self):
        """Puebla las listas de puntos materiales / contornos y el resumen.

        La configuración del análisis (etapas, gravedad, fps) vive en
        DialogStages; el panel muestra qué se analiza y un resumen.
        """
        self.setListPointsMaterialView()
        self.setListBoundariesView()
        self.updateStagesSummary()

    def getFps(self):
        """fps del proyecto; si no lo guarda (proyecto anterior), el de sus
        resultados, y si tampoco hay, 30."""
        fps = self.model_current_project.getFps()
        if fps is None and self.model_result.getDataTimes():
            fps = self.model_result.getDataTimes().get('FPS')
        return int(fps or 30)

    def updateStagesSummary(self):
        if self.model_current_project is None:
            return
        self.view_menu_execute.setStagesSummary(stages_summary_html(
            self.model_current_project.getStages() or [],
            self.model_current_project.getGravity(),
            self.getFps(),
            self.model_current_project.getResumeFrom()))

    def _selected_ids(self):
        """(ids de puntos materiales, ids de contornos) a analizar: los guardados
        en el proyecto; si no los guarda (proyecto anterior), los de sus resultados."""
        ids_mp, ids_bo = self.model_current_project.getAnalysisSelection()
        if ids_mp is None:
            ids_mp = list(self.model_result.getPointMaterials().keys())
        if ids_bo is None:
            ids_bo = list(self.model_result.getBoundarys().keys())
        return set(ids_mp), set(ids_bo)

    @Slot()
    def saveSelection(self):
        self.model_current_project.updateAnalysisSelection(
            self.view_menu_execute.getListExecutePointMaterial().keys(),
            [b['id'] for b in self.view_menu_execute.getListExecuteBoundaries()])

    def setListPointsMaterialView(self):
        self.view_menu_execute.removeItemsListsMaterialPoint()

        ids_result_point_materia = self._selected_ids()[0]

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

        ids_result_boundaries = self._selected_ids()[1]

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
        msg = self.view_menu_execute.msnAlertDefault
        list_point_material = self.view_menu_execute.getListExecutePointMaterial()
        list_boundaries = self.view_menu_execute.getListExecuteBoundaries()

        # Validaciones antes de abrir el diálogo de progreso
        if not list_point_material:
            msg(True, "Selecciona los puntos materiales")
            return
        if not list_boundaries:
            msg(True, "Selecciona los contornos")
            return
        for id_mp in list_point_material:
            model_mp = self.model_current_project.getModelsPointsMaterials()[id_mp]
            if not self.pointsInsideMeshBack(model_mp.getPoints()):
                msg(True, "Puntos fuera de la malla de fondo: '{}'".format(model_mp.getName()))
                return
        stage_dicts = self.model_current_project.getStages()
        if not stage_dicts:
            msg(True, "Configura al menos una etapa de análisis")
            return

        # ── Construir AnalysisConfig desde las ETAPAS configuradas ──
        gravity = self.model_current_project.getGravity()
        fps = self.getFps()
        time_config = TimeConfig(fps=fps)
        analysis_config = AnalysisConfig.from_stage_dicts(
            stage_dicts=stage_dicts, gravity=gravity, time_config=time_config,
            resume_from_stage=self.model_current_project.getResumeFrom())

        # Semilla de tiempo (el executor recalcula dt/pasos por etapa)
        seed = self._build_seed_time(analysis_config, fps)
        if seed is None:
            msg(True, "No se pudo calcular dt (revisa los materiales)")
            return
        dtime, tiempo, dtimegraphic, tiempographic, steps_time, steps_timegraphic, dataTime = seed

        self.saveSelection()
        analysis_dialog = AnalysisProgressDialog(self.view_menu_execute)
        analysis_dialog.show()
        analysis_dialog.rejected.connect(analysis_dialog.cancelAnalysis)

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
            elif analysis_mpm.warnings:
                self.view_menu_execute.msnAlertDefault(True, "Análisis ejecutado con avisos")
                print("[OK→] Análisis finalizado con avisos")
            else:
                self.view_menu_execute.msnAlertDefault(False,"Análisis ejecutado")
                print("[OK→] Análisis finalizado")
            self.signal_update_menu_result.emit()
            if analysis_mpm.warnings:
                # El mensaje del panel se borra a los 4 s: los avisos van en un diálogo
                DialogMsg(self.view_menu_execute, 0, "El análisis terminó con avisos",
                          "\n\n".join(analysis_mpm.warnings), 0).exec()

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

    def _gather_two_phase_materials(self):
        """Como _gather_selected_materials, con lo que pide el dt de doble
        fase: (E, nu, rho_d[Mg/m³], n0, Kw)."""
        list_mp = self.view_menu_execute.getListExecutePointMaterial()
        models_mp = self.model_current_project.models_material_point
        materials = []
        for id_mp in list_mp:
            data = models_mp[id_mp].getProperty().getData()
            mat = data[list(data.keys())[0]]
            materials.append((mat["MODULOELASTICIDAD"], mat["RELACIONPOISSON"],
                              mat["DENSIDAD"] / 1000.0,
                              mat.get("POROSIDAD"), mat.get("MODULOAGUA")))
        return materials

    def _stage_dt(self, courant, stage_type):
        """(dt, cp, índice del material crítico) de una etapa, con la misma
        fórmula que usará el ejecutor: la de doble fase en consolidación."""
        if stage_type == StageType.CONSOLIDATION.value:
            dt, cp = compute_two_phase_dt(self._gather_two_phase_materials(),
                                          self.model_current_project.model_mesh_back.getSizeElement(),
                                          courant)
            return dt, cp, 0
        materials, _ = self._gather_selected_materials()
        ele_size = self.model_current_project.model_mesh_back.getSizeElement()
        return compute_min_dt(materials, ele_size, courant)

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
        stage0 = config.stages[0]
        dt, cp, idx = self._stage_dt(stage0.courant_number, stage0.stage_type.value)
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
        def dt_provider(courant, stage_type):
            return self._stage_dt(courant, stage_type)[0]

        dlg = DialogStages(self.model_current_project,
                           dt_provider=dt_provider,
                           parent=self.view_menu_execute,
                           fps=self.getFps())
        dlg.exec()
        self.updateStagesSummary()

    @Slot(dict)
    def stateViewBoundary(self, data):
        self.model_current_project.stateViewBoundary(data)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def pointsInsideMeshBack(self, points) -> bool:
        """True si todos los puntos caen dentro de la malla de fondo, que es el
        rectángulo [0, SIZEDX] × [0, SIZEDY]."""
        mesh_back = self.model_current_project.model_mesh_back
        dx, dy = mesh_back.getSizeDx(), mesh_back.getSizeDy()
        for point in points.values():
            x, y = point['COORDINATES']
            if not (0.0 <= x <= dx and 0.0 <= y <= dy):
                return False
        return True
