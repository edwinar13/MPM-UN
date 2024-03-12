from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from views.results.view_WidgetResultMenuAnimation import ViewWidgetResultMenuAnimation
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMesh import ControllerCardMesh
from motorMPM.mesh import create_uniform
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
        self.view_menu_result_animation.signal_result_animation_color_styles.connect(self.signalResultAnimationColorStyles)
        self.view_menu_result_animation.signal_result_animation_grid.connect(self.signalResultAnimationGrid)   
        self.view_menu_result_animation.signal_result_animation_axis.connect(self.signalResultAnimationAxis)
        self.view_menu_result_animation.signal_result_animation_base.connect(self.signalResultAnimationBase)
        self.view_menu_result_animation.signal_result_animation_label.connect(self.signalResultAnimationLabel)
        self.view_menu_result_animation.signal_result_animation_values_text.connect(self.signalResultAnimationValuesText)
        
        self.view_menu_result_animation.signal_result_animation_size_points.connect(self.signalResultAnimationSizePoints)
        self.view_menu_result_animation.signal_result_animation_size_texts.connect(self.signalResultAnimationSizeTexts)
        self.view_menu_result_animation.signal_scene_type_result.connect(self.signalSceneTypeResult)
        self.view_menu_result_animation.signal_scene_regress.connect(self.signalSceneRegress)
        self.view_menu_result_animation.signal_scene_advance.connect(self.signalSceneAdvance)
        self.view_menu_result_animation.signal_scene_play.connect(self.signalScenePlay)
        self.view_menu_result_animation.signal_scene_stop.connect(self.signalSceneStop)
        self.view_menu_result_animation.signal_scene_animation_velocity.connect(self.signalSceneAnimationVelocity)    
                
                

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
        size = self.model_result.model_mesh_back.getSizeDx()/60
        self.view_menu_result_animation.setSizePoint(size=size)
        self.view_menu_result_animation.resetTypeResult()
        


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS ESTILOS VISUALIZACION        ::::::::::::::::::::

    @Slot(int)
    def signalModelResultTimeStepsChanged(self,steps):
        self.view_menu_result_animation.setStepView(steps)
        time_view = self.model_result.getGrapihcsTimes()[steps]
        time_view = round(time_view, 3)
        self.view_menu_result_animation.setTimeView(time_view)
        
        #verificar si es el ultimo paso
        if steps == len(self.model_result.getGrapihcsTimes())-1 and not self.scene_is_play:  
            self.scene_is_play = False
            self.view_menu_result_animation.playPauseAnimation(self.scene_is_play)
        
    @Slot()
    def signalModelResultTimeStepsEnd(self):
        self.view_menu_result_animation.playPauseAnimation(self.scene_is_play)       
        self.scene_is_play = not self.scene_is_play
        
        
        
    @Slot()
    def signalResultAnimationColorStyles(self):
        color_style = self.view_menu_result_animation.getColorStyle()
        hue = self.view_menu_result_animation.getColorCustomHue()
        if color_style == 'Escala color':
            self.model_result.changedColorStyle(color_style, hue)
        else:
            self.model_result.changedColorStyle(color_style) 
        self.model_result.scene_result.update()
    
    @Slot()
    def signalResultAnimationGrid(self):
        self.model_result.hideShowItemBasic('grid')
    
    @Slot()
    def signalResultAnimationAxis(self):
        self.model_result.hideShowItemBasic('axis')
    
    @Slot()
    def signalResultAnimationBase(self):
        self.model_result.hideShowItemBasic('base')
        
            
    @Slot()
    def signalResultAnimationLabel(self):
        self.model_result.hideShowItemBasic('label')
        
    @Slot()
    def signalResultAnimationValuesText(self):
        is_visible_values_text = self.view_menu_result_animation.getValuesText()
        self.model_result.hideShowItemBasic('values', is_visible_values_text)
                 
    @Slot()
    def signalResultAnimationSizePoints(self):
        self.model_result.setSizePoints(self.view_menu_result_animation.getSizePoints())
           
    @Slot()
    def signalResultAnimationSizeTexts(self):
        self.model_result.setSizeTexts(self.view_menu_result_animation.getSizeTexts())
        
    
    
           

        
    # ::::::::::::::::::::         MÉTODOS DATOS VISUALIZACION        ::::::::::::::::::::
    @Slot()
    def signalSceneTypeResult(self):
        type_result = self.view_menu_result_animation.getTypeResult()
        if type_result == 'default':
            self.view_menu_result_animation.setEnableColorStyle(False)
        else:
            self.view_menu_result_animation.setEnableColorStyle(True)
        self.model_result.setTypeResult(type_result)
    
    @Slot()
    def signalSceneAnimationVelocity(self):
        velolity = self.view_menu_result_animation.getVelocity()
        self.model_result.setVelocity(velolity)
        
        
        
        
        
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
        
        
        