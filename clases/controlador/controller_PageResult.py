
from PySide6.QtCore import ( QFile, Slot, QObject,QPointF)
from clases.general_functions import isNumber
from clases.Vista.view_PageResult import  ViewPageResult
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent


from clases.Controlador.controller_graphicsResult import ControllerGraphicsResult
from clases.Controlador.controller_ResultCardPoint import ControllerResultCardPoint
import numpy as np
import math


class ControllerPageResult(QObject):

    def __init__(self, controller_main) -> None:    
        super().__init__()

        self.controller_main = controller_main         
        self.current_project = None
        self.model_result = None

        #Crea la vista page draw
        self.view_page_result = ViewPageResult()
        self.controller_graphics_result = ControllerGraphicsResult()
        self.view_page_result.setViewGraphicsWidget(self.controller_graphics_result.getView())

        self.scene_type_result = "default"
        self.scene_is_play = True

        self.graphics_type_result = "Coordenada X"
        self.graphics_list_point =[]
        self.graphics_type_view = 0
        self.list_controller_card=[]

        self.__initEventUi()

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
    ###############################################################################
      
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """

        # ::::::::::::::::::::      EVENTOS PAGE SCENE     ::::::::::::::::::::
        self.view_page_result.signal_scene_type_result.connect(self.signalSceneTypeResult)
        self.view_page_result.signal_scene_regress.connect(self.signalSceneRegress)
        self.view_page_result.signal_scene_stop.connect(self.signalSceneStop)
        self.view_page_result.signal_scene_play.connect(self.signalScenePlay)
        self.view_page_result.signal_scene_advance.connect(self.signalSceneAdvance)
   
        # ::::::::::::::::::::      EVENTOS PAGE CHART     ::::::::::::::::::::
        self.view_page_result.signal_chart_add_card.connect(self.signalChartAddCard)
        self.view_page_result.signal_chart_type_result.connect(self.signalChartTypeResult)
        self.view_page_result.signal_chart_type_style.connect(self.signalChartTypeStyle)

        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
        self.view_page_result.signal_table_search_point.connect(self.signalTableSearchPoint)
        self.view_page_result.signal_table_all_point.connect(self.signalTableAllPoints)
        
        
    

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):
        self.current_project = model_current_project
        self.model_result = self.current_project.getModelResult()
        #: ::::::::::::::::::::      EVENTOS MODEL RESULT     ::::::::::::::::::::
        #
        # 
        # 
        # 
        # 
        # 
        # 
        # self.model_result.signal_time_steps_changed.connect(self.timeStepsChanged)
    
    def configResult(self):        
        if self.model_result != None:
            data = self.model_result.getResultNodes()            
            self.view_page_result.updateViewTableResult(data)
           
    def getView(self):
        return self.view_page_result
  
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::      SLOT PAGE SCENE     ::::::::::::::::::::
   
    @Slot(int)    
    def timeStepsChanged(self, time_step):
        print("$$")
        return
        self.view_result.timeStepsChanged(time_step)
        
        
        
    @Slot()
    def signalSceneTypeResult(self): 
        self.scene_type_result = self.view_page_result.getTypeResultScene()
        
    @Slot()
    def signalSceneRegress(self): 
        self.model_result.regressTime()
                
                
    @Slot()
    def signalSceneStop(self): 
        self.view_page_result.stopAnimation()
        self.model_result.stopTime()        
        self.scene_is_play = True
        
    @Slot()
    def signalScenePlay(self): 

        self.view_page_result.playPauseAnimation(self.scene_is_play)
        self.model_result.playPauseTime(self.scene_is_play)        
        self.scene_is_play = not self.scene_is_play

    @Slot()
    def signalSceneAdvance(self): 
        self.model_result.advanceTime()
                
    # ::::::::::::::::::::      SLOT PAGE CHART     ::::::::::::::::::::
    @Slot()
    def signalChartAddCard(self):  
        ids_point = self.view_page_result.getIdPointGraphics()
        if ids_point == "":
            return
        # separamos los puntos
        ids_point = ids_point.split(",")        
        #validación con 1,5:3:4:1:4:d:::5j:,::,a,'b', , ' ', ""

        for id_point in ids_point:
            point_range_int = []
            point_range_str = []
            # verificamos si los puntos corresponde a rango de puntos 
            if ":" in id_point:
                #separamos los rangos en puntos
                point_range = id_point.split(":")  
                #verificamos que los puntos sean validos (Ejemplo NO: "", "d")
                for x in point_range:
                    if isNumber(x):
                        point_range_int.append(int(x))                
                if len(point_range_int) > 0:
                    point_range_init = min(point_range_int)
                    point_range_end = max(point_range_int)

                    # se asigna los puntos que están en el rango
                    for i in range(point_range_init, point_range_end+1):
                        point_range_str.append("{}".format(i))
            if len(point_range_str) > 0:            
                ids_point.extend(point_range_str)



        data = self.model_result.getResultNodes()          
        list_keys = data.keys()

        list_point_search = []
        for id_point in ids_point:
            if id_point in list_keys:
                list_point_search.append(id_point)

        if len(list_point_search)>0:    
            for point_search in list_point_search:
                if not point_search in self.graphics_list_point:
                    times_x = data[point_search]['TIEMPOS']
                    data_axis_y = None
                    if self.graphics_type_result.lower() == 'coordenada x':
                        data_axis_y = data[point_search]['CORX']
                    elif self.graphics_type_result.lower() == 'coordenada y':
                        data_axis_y = data[point_search]['CORY']
                    elif self.graphics_type_result.lower() == 'sigxx':
                        data_axis_y = data[point_search]['SIGXX']
                    elif self.graphics_type_result.lower() == 'sigyy':
                        data_axis_y = data[point_search]['SIGYY']
                    elif self.graphics_type_result.lower() == 'sigxy':
                        data_axis_y = data[point_search]['SIGXY']
                    elif self.graphics_type_result.lower() == 'epsxx':
                        data_axis_y = data[point_search]['EPSXX']
                    elif self.graphics_type_result.lower() == 'epsyy':
                        data_axis_y = data[point_search]['EPSYY']
                    elif self.graphics_type_result.lower() == 'epsxy':
                        data_axis_y = data[point_search]['EPSXY']

                    color = self.view_page_result.setDatePointChart(times_x, data_axis_y, point_search)
                    self.view_page_result.canvas.draw()

                    self.createCardPoint(point_search, color)
                    self.graphics_list_point.append(point_search)

            self.view_page_result.lineEdit_chartPointName.setText("")

    @Slot()
    def signalChartTypeResult(self): 
        self.graphics_type_result = self.view_page_result.getTypeResult() 
        self.changedGraphicsType(self.graphics_type_result)

    @Slot()
    def signalChartTypeStyle(self): 
        if self.graphics_type_view == 0:
            self.view_page_result.changeLinesTypeChart("points")
            self.graphics_type_view += 1
        elif self.graphics_type_view == 1:
            self.view_page_result.changeLinesTypeChart("line")
            self.graphics_type_view += 1
        elif self.graphics_type_view == 2:
            self.view_page_result.changeLinesTypeChart("curve")
            self.graphics_type_view += 1
        elif self.graphics_type_view == 3:
            self.view_page_result.changeLinesTypeChart("circles")
            self.graphics_type_view = 0

    # ::::::::::::::::::::      SLOT PAGE TABLE     ::::::::::::::::::::
    @Slot()
    def signalTableSearchPoint(self):

        if self.model_result == None:
            return

        ids_point = self.view_page_result.getIdPointSearch()

        # separamos los puntos
        ids_point = ids_point.split(",")        
        
        for id_point in ids_point:
            point_range_int = []
            point_range_str = []
            # verificamos si los puntos corresponde a rango de puntos 
            if ":" in id_point:
                #separamos los rangos en puntos
                point_range = id_point.split(":")  
                #verificamos que los puntos sean validos (Ejemplo NO: "", "d")
                for x in point_range:
                    if isNumber(x):
                        point_range_int.append(int(x))                
                if len(point_range_int) > 0:
                    point_range_init = min(point_range_int)
                    point_range_end = max(point_range_int)

                    # se asigna los puntos que están en el rango
                    for i in range(point_range_init, point_range_end+1):
                        point_range_str.append("{}".format(i))
            if len(point_range_str) > 0:            
                ids_point.extend(point_range_str)


        data = self.model_result.getResultNodes()          
        list_keys = data.keys()

        list_point_search = []
        for id_point in ids_point:
            if id_point in list_keys:
                list_point_search.append(id_point)

        if len(list_point_search)>0:
            
            list_data_point = {}
            for point_search in list_point_search:
                if point_search in list_keys:
                    list_data_point[point_search]  = data[point_search]    

            self.view_page_result.updateViewTableResult(list_data_point)        
        else:
            self.view_page_result.clearViewTableResult()
        
    @Slot()
    def signalTableAllPoints(self):

        if self.model_result == None:
            return

        data = self.model_result.getResultNodes()         
        self.view_page_result.updateViewTableResult(data)
        self.view_page_result.clearLineEdit()

    # ::::::::::::::::::::      SLOT PAGE CARD     ::::::::::::::::::::


    @Slot(dict)
    def signalCardShowHidePoint(self,data): 
        id_point = data['id']
        is_visible = data['show']
        self.view_page_result.showPointChart(id_point=id_point, is_visible=is_visible)
    
    @Slot(str)
    def signalCardDeletePoint(self,data):  
        id_point = data
        self.graphics_list_point.remove(id_point)
        self.view_page_result.signalCardDeletePointChart(id_point=id_point)
    
    @Slot(dict)
    def signalCardUpdateColorPoint(self,data):  

        id_point = data['id']
        color = data['color']
        self.view_page_result.updateColorPointChart(id_point=id_point,color=color)


        
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################



    def animation(self):
        self.controller_graphics_result.animation()




    def createCardPoint(self, id_point, color):
        controller_card_mesh = ControllerResultCardPoint(id=id_point, color=color)
        self.view_page_result.addCardPoint(controller_card_mesh.view_card_point)
        controller_card_mesh.signal_hide_show_point.connect(self.signalCardShowHidePoint)
        controller_card_mesh.signal_delete_point.connect(self.signalCardDeletePoint)
        controller_card_mesh.signal_update_color_point.connect(self.signalCardUpdateColorPoint)

        self.list_controller_card.append(controller_card_mesh)




    def changedGraphicsType(self, type):
        #self.view_page_result.ax.clear()
        self.view_page_result.setTitleChart(type)
        self.view_page_result.setLabelYChart(type)
        #self.view_page_result.ax.legend()
        self.view_page_result.canvas.draw()

        data = self.model_result.getResultNodes()    
        ymax = -1000*100
        ymin = 1000*100

        for point_graphics in self.graphics_list_point:   

            if self.graphics_type_result.lower() == 'coordenada x':
                data_axis_y = data[point_graphics]['CORX']
            elif self.graphics_type_result.lower() == 'coordenada y':
                data_axis_y = data[point_graphics]['CORY']
            elif self.graphics_type_result.lower() == 'sigxx':
                data_axis_y = data[point_graphics]['SIGXX']
            elif self.graphics_type_result.lower() == 'sigyy':
                data_axis_y = data[point_graphics]['SIGYY']
            elif self.graphics_type_result.lower() == 'sigxy':
                data_axis_y = data[point_graphics]['SIGXY']
            elif self.graphics_type_result.lower() == 'epsxx':
                data_axis_y = data[point_graphics]['EPSXX']
            elif self.graphics_type_result.lower() == 'epsyy':
                data_axis_y = data[point_graphics]['EPSYY']
            elif self.graphics_type_result.lower() == 'epsxy':
                data_axis_y = data[point_graphics]['EPSXY']

            self.view_page_result.changeTypeResultChart(id_point=point_graphics,
                                                     y_new=data_axis_y)
            ymin_ref = min(data_axis_y)            
            if ymin_ref < ymin:
                ymin = ymin_ref

            ymax_ref = max(data_axis_y)         
            if ymax_ref > ymax:
                ymax = ymax_ref
                    
        self.view_page_result.setYAxisLimitsChart(ymax=ymax,ymin=ymin)
        





    """



    @Slot(list)
    def msnLabelAndView(self,data):  
        '''
        tercer dato:
            type_msn=none colocar el msn en consola y view
            type_msn=1 view
        
        '''
        command = data[0]
        input = data[1]
        type_msn=data[2]
        if type_msn == None:
            self.msnConsoleView(["Command","_{}".format(command)])
            self.msnLabelConsole([command, input])
        if type_msn == 1:
            self.msnConsoleView([command,input])
        if type_msn == 2:
            self.msnLabelConsole([command, input])
        if type_msn == 3:
            self.endDrawGeometry()



    @Slot(bool)
    def endDrawGeometry(self, show_msn=True):
        self.controller_graphics_draw.endDrawGeometry()
        self.view_page_draw.endDrawGeometry(show_msn)

    @Slot(bool)
    def endDrawMesh(self, show_msn=True):
        self.controller_menu_mesh.endDrawMesh()


    @Slot()
    def endDrawBoundary(self):        
        self.controller_menu_boundary.endDrawBoudary()



    @Slot(list)
    def msnLabelConsole(self,data):
        command = data[0]
        input = data[1]
        self.view_page_draw.msnLabelConsole(command, input)



    @Slot(list)
    def msnConsoleView(self,data):
        type_msn = data[0]
        msn = data[1]
        self.view_page_draw.msnConsoleView(type_msn, msn)




    @Slot(int)
    def selectLineMesh(self, no_lines):
        selected_objects = self.controller_graphics_draw.getSelectedObjects()
        self.controller_menu_mesh.selectLineMesh(no_lines, selected_objects)


 

    @Slot(bool)
    def deselectDrawGeometry(self, shift_pressed ):
        self.current_project.deselectDrawGeometry(shift_pressed)
        

    @Slot(str)
    def zoomDraw(self,type_zoom):
        self.controller_graphics_draw.zoomDraw(type_zoom)
    
    def settingDraw(self,setting_update):
        self.controller_graphics_draw.settingDraw(setting_update)
        if setting_update[ "setting"] == "style_view_scene" and self.current_project != None:
            style=setting_update["setting_data"][2]
            self.current_project.changeTheme(index_style=style)
    
    def viewsTwo(self):
        self.view_page_draw.viewsTwo()
    """



    ###############################################################################
    # ::::::::::::::::         MÉTODOS TABLA DE RESULTADOS       ::::::::::::::::::
    ###############################################################################
 
