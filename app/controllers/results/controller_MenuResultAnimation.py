from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from views.results.view_WidgetResultMenuAnimation import ViewWidgetResultMenuAnimation
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMesh import ControllerCardMesh
from motorMPM.mesh import create_uniform
from utils.general_functions import SCALAR_RESULTS
from views.view_DialogStages import STAGE_TYPES
import pygmsh
import math
import time
class ControllerMenuResultAnimation(QObject):



    
    
    def __init__(self) -> None:
        super().__init__()

        self.view_menu_result_animation= ViewWidgetResultMenuAnimation()
     
        self.model_current_project = None
        self.model_result = None
        self.scene_is_play = True

        self.__config()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __config(self): 
        pass

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_result_animation.signal_result_animation_color_styles.connect(self.signalSceneTypeResult)
        self.view_menu_result_animation.signal_result_animation_grid.connect(self.signalResultAnimationGrid)   
        self.view_menu_result_animation.signal_result_animation_axis.connect(self.signalResultAnimationAxis)
        self.view_menu_result_animation.signal_result_animation_label.connect(self.signalResultAnimationLabel)
        self.view_menu_result_animation.signal_result_animation_values_text.connect(self.signalResultAnimationValuesText)
        self.view_menu_result_animation.signal_result_animation_loads.connect(self.signalResultAnimationLoads)
        
        self.view_menu_result_animation.signal_result_animation_size_points.connect(self.signalResultAnimationSizePoints)
        self.view_menu_result_animation.signal_result_animation_size_texts.connect(self.signalResultAnimationSizeTexts)
        self.view_menu_result_animation.signal_result_animation_add_point_label.connect(self.signalResultAnimationAddPointLabel)
        self.view_menu_result_animation.signal_result_animation_close_point_labels.connect(self.signalResultAnimationClosePointLabels)
        self.view_menu_result_animation.signal_scene_type_result.connect(self.signalSceneTypeResult)

        self.view_menu_result_animation.signal_scene_regress.connect(self.signalSceneRegress)
        self.view_menu_result_animation.signal_scene_advance.connect(self.signalSceneAdvance)
        self.view_menu_result_animation.signal_scene_play.connect(self.signalScenePlay)
        self.view_menu_result_animation.signal_scene_stop.connect(self.signalSceneStop)
        self.view_menu_result_animation.signal_scene_animation_velocity.connect(self.signalSceneAnimationVelocity)    
        self.view_menu_result_animation.signal_scene_stage.connect(self.signalSceneStage)
        self.view_menu_result_animation.signal_scene_frame.connect(self.signalSceneFrame)
                
                

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        
        self.model_current_project = model_current_project
        self.model_result = self.model_current_project.getModelResult()  
              
        self.view_menu_result_animation.setSteps(len(self.model_result.getGrapihcsTimes())-1)
        self.updateMenuResults()
        
        
        self.model_result.signal_time_steps_changed.connect(self.signalModelResultTimeStepsChanged)
        self.model_result.signal_time_steps_end.connect(self.signalModelResultTimeStepsEnd)
        
        #self.signalSceneStop()

    def getView(self):
        return self.view_menu_result_animation
    
    def updateMenuResults(self):
        # Calcular radio inicial basado en volumen promedio de los puntos (igual a drawItemPointsScene)
        import math
        volumes_list = []
        point_materials = self.model_result.getPointMaterials()
        for id_MP in point_materials:
            pts = point_materials[id_MP].get("POINTS", {})
            for pk in pts:
                v = pts[pk].get("VOLUME", None)
                if v and v > 0:
                    volumes_list.append(v)

        if volumes_list:
            avg_v = sum(volumes_list) / len(volumes_list)
            size = (math.sqrt(avg_v / math.pi)) / 2
        else:
            size = self.model_result.model_mesh_back.getSizeElement() / 7

        self.view_menu_result_animation.setSizePoint(size=size)
        self.view_menu_result_animation.resetTypeResult()

        # Selector de etapa: cada análisis nuevo vuelve a "todas"
        names = dict((value, label) for label, value in STAGE_TYPES)
        stages = [(f"{st['ETAPA']}: {st.get('NOMBRE') or ''} ({names.get(st['TIPO'], st['TIPO'])})",
                   (st['FRAME_INICIO'], st['FRAME_FIN']))
                  for st in self.model_result.getStagesFrames()]
        self.view_menu_result_animation.setStages(stages)
        self.model_result.setLoadsVisible(self.view_menu_result_animation.getShowLoads())
        self.signalSceneStage()
        


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS ESTILOS VISUALIZACION        ::::::::::::::::::::

    @Slot(int)
    def signalModelResultTimeStepsChanged(self,steps):

        times_view = self.model_result.getGrapihcsTimes()
        if len(times_view) == 0:
            return
        lo, hi = self.model_result.frameRange()
        self.view_menu_result_animation.setStepView(steps - lo)
        # tiempo propio de la etapa del frame: incremento o segundos desde su inicio
        value, is_increment = self.model_result.localTime(steps)
        self.view_menu_result_animation.setTimeView(round(value, 3))
        self.view_menu_result_animation.setTimeCaption("Incremento" if is_increment else "Tiempo (s)")
        
        #verificar si es el ultimo paso
        if steps == hi and not self.scene_is_play:  
            self.scene_is_play = False
            self.view_menu_result_animation.playPauseAnimation(self.scene_is_play)
        
    @Slot()
    def signalModelResultTimeStepsEnd(self):
        self.view_menu_result_animation.playPauseAnimation(self.scene_is_play)       
        self.scene_is_play = not self.scene_is_play
        
        
        

    @Slot()
    def signalResultAnimationGrid(self):
        self.model_result.hideShowItemBasic('grid')
    
    @Slot()
    def signalResultAnimationAxis(self):
        self.model_result.hideShowItemBasic('axis')   

            
    @Slot()
    def signalResultAnimationLabel(self):
        self.model_result.hideShowItemBasic('label')
        
    @Slot()
    def signalResultAnimationValuesText(self):
        is_visible_values_text = self.view_menu_result_animation.getValuesText()
        self.model_result.hideShowItemBasic('values', is_visible_values_text)

    @Slot(bool)
    def signalResultAnimationLoads(self, visible):
        self.model_result.setLoadsVisible(visible)
                 
    @Slot()
    def signalResultAnimationSizePoints(self):
        self.model_result.setSizePoints(self.view_menu_result_animation.getSizePoints())
           
    @Slot()
    def signalResultAnimationSizeTexts(self):
        self.model_result.setSizeTexts(self.view_menu_result_animation.getSizeTexts())

    @Slot()
    def signalResultAnimationAddPointLabel(self):
        id_text = self.view_menu_result_animation.getLabelByPointId()
        size_text = self.view_menu_result_animation.getSizeTexts()
        self.model_result.addDetailPanelForNode(id_text, size_text)

    @Slot()
    def signalResultAnimationClosePointLabels(self):
        self.model_result.clearAllDetailPanels()
        
    
    
           

        
    # ::::::::::::::::::::         MÉTODOS DATOS VISUALIZACION        ::::::::::::::::::::
    @Slot()
    def signalSceneTypeResult(self):
        type_result = self.view_menu_result_animation.getTypeResult()
        axis = self.view_menu_result_animation.getAxisResult()
        vector = self.view_menu_result_animation.getVectorResult()

        # La presión de poros solo existe si el análisis tuvo consolidación
        if type_result == 'pp' and not self.model_result.hasResult('PRESIONPOROS'):
            print("[RESULTADOS] este análisis no tiene presión de poros (sin etapa de consolidación)")
            self.view_menu_result_animation.resetTypeResult()
            return

        if type_result == 'default' or type_result in SCALAR_RESULTS:
            self.view_menu_result_animation.setEnabledSeletedAxis(False)
            self.view_menu_result_animation.setEnabledSeletedVector(False)
        elif type_result == 'despl' or type_result == 'vel':
            self.view_menu_result_animation.setEnabledSeletedAxis(True)
            self.view_menu_result_animation.setEnabledSeletedVector(True)
        else:
            self.view_menu_result_animation.setEnabledSeletedAxis(True)
            self.view_menu_result_animation.setEnabledSeletedVector(False)
        
        if type_result == 'default':
            self.view_menu_result_animation.showStyleColor(0)
        else:
            self.view_menu_result_animation.showStyleColor(1)

        color_style = self.view_menu_result_animation.getColorStyle()
        hue = self.view_menu_result_animation.getColorCustomHue()
         
        if color_style == 'Escala color':
            self.model_result.setTypeResult(type_result, axis, vector, color_style, hue)
        else:   
            self.model_result.setTypeResult(type_result, axis, vector, color_style)
        self.model_result.scene_result.update()
    

    @Slot()
    def signalSceneAnimationVelocity(self):
        velolity = self.view_menu_result_animation.getVelocity()
        self.model_result.setVelocity(velolity)
        
        
        
        
        
    @Slot()
    def signalSceneStage(self):
        """Reproduce todas las etapas o solo la elegida."""
        # detener sin volver al frame 0: setFrameRange ya va al primero del
        # rango nuevo (cada salto de frame recorre todas las partículas)
        self.view_menu_result_animation.stopAnimation()
        self.scene_is_play = True
        frames = self.view_menu_result_animation.getStageFrames()
        lo, hi = frames if frames else (0, len(self.model_result.getGrapihcsTimes()) - 1)
        self.view_menu_result_animation.setFrameCount(hi - lo)
        self.model_result.setFrameRange(lo, hi)
        self.signalModelResultTimeStepsChanged(self.model_result.frameRange()[0])

    @Slot(int)
    def signalSceneFrame(self, frame):
        """'Ir al frame': el número es relativo al rango que se reproduce."""
        self.model_result.goToFrame(self.model_result.frameRange()[0] + frame)

    @Slot()
    def signalSceneRegress(self):
        self.model_result.regressTime()
            
    @Slot()
    def signalScenePlay(self):
        self.view_menu_result_animation.playPauseAnimation(self.scene_is_play)
        self.model_result.playPauseTime(self.scene_is_play)        
        self.scene_is_play = not self.scene_is_play
        
    @Slot()
    def signalSceneStop(self):
        self.view_menu_result_animation.stopAnimation()
        self.model_result.stopTime()        
        self.scene_is_play = True
        
    @Slot()
    def signalSceneAdvance(self):
        self.model_result.advanceTime()
        
        
        