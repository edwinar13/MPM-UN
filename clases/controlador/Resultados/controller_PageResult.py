
from PySide6.QtCore import ( Slot, QObject)
from clases.general_functions import isNumber
from clases.Vista.Resultados.view_PageResult import  ViewPageResult
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent


from clases.Controlador.controller_graphicsResult import ControllerGraphicsResult
from clases.Controlador.controller_ResultCardPoint import ControllerResultCardPoint

from clases.Controlador.Resultados.controller_MenuResultAnimation import ControllerMenuResultAnimation
from clases.Controlador.Resultados.controller_MenuResultTable import ControllerMenuResultTable
from clases.Controlador.Resultados.controller_MenuResultGraph import ControllerMenuResultGraph

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


        # crea el controlador de los menus 
        self.controller_menu_result_animation = ControllerMenuResultAnimation()
        self.controller_menu_result_graph = ControllerMenuResultGraph()
        self.controller_menu_result_summary_table = ControllerMenuResultTable()
        
        self.view_page_result.setMenuWidget("animation",self.controller_menu_result_animation.getView())
        self.view_page_result.setMenuWidget("graph",self.controller_menu_result_graph.getView())
        self.view_page_result.setMenuWidget("summary_table",self.controller_menu_result_summary_table.getView())
        

        self.scene_type_result = "default"

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
        
        self.controller_menu_result_graph.signal_change_graphics_type.connect(self.changedGraphicsType)
        self.controller_menu_result_graph.signal_chart_add_card.connect(self.signalChartAddCard)
        self.controller_menu_result_graph.signal_change_graphics_type_style.connect(self.signalChartTypeStyle)
        self.controller_menu_result_graph.signal_show_hide_series.connect(self.signalCardShowHideSeries)
        self.controller_menu_result_graph.signal_show_hide_label.connect(self.signalShowHideLabel)  
        self.controller_menu_result_graph.signal_delete_series.connect(self.signalDeleteSeries)
        
        self.controller_menu_result_summary_table.signal_table_search_point.connect(self.signalTableSearchPoint)
        self.controller_menu_result_summary_table.signal_table_clear.connect(self.signalTableClear)
        self.controller_menu_result_summary_table.signal_table_hise_show_column.connect(self.signalTableHiseShowColumn)      
 
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
   
    @Slot(dict)
    def signalCardShowHidePoint(self,data): 
        id_point = data['id']
        is_visible = data['show']
        self.view_page_result.showPointChart(id_point=id_point, is_visible=is_visible)
    
    @Slot(bool)
    def signalCardShowHideSeries(self,show_series):  
        self.view_page_result.showAllPointChart(show_series)
        for controller_card_point in self.list_controller_card:
            controller_card_point.showHideAllPoint(show_series)
            
    @Slot(bool)
    def signalShowHideLabel(self,show_label):
        self.view_page_result.setHideShowLabel(show_label)
        
    @Slot()
    def signalDeleteSeries(self):                    
        for controller_card_point in self.list_controller_card:
            controller_card_point.deleteAllSeries()
        
        self.view_page_result.deleteAllPointChart()
        self.list_controller_card = []   
        self.graphics_list_point = []         
        
       
       
    @Slot(str)
    def signalCardDeletePoint(self,data):  
        id_point = data
        self.graphics_list_point.remove(id_point)
        self.view_page_result.deletePointChart(id_point=id_point)
        
        for controller_card_point in self.list_controller_card:
            if controller_card_point.id == id_point:
                self.list_controller_card.remove(controller_card_point)
                break
        
        
    @Slot(dict)
    def signalCardUpdateColorPoint(self,data):  
        id_point = data['id']
        color = data['color']
        self.view_page_result.updateColorPointChart(id_point=id_point,color=color)

    @Slot(dict)
    def signalTableHiseShowColumn(self,dict_data):
        self.view_page_result.hideShowColumnTable(dict_data) 
        
    @Slot()
    def signalTableClear(self):
        self.view_page_result.updateViewTableResult('')

    @Slot(str)
    def signalTableSearchPoint(self, list_point_search):
        if self.model_result == None:
            return

        ids_point = list_point_search

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
        data_time = self.model_result.getGrapihcsTimes()
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

            self.view_page_result.updateViewTableResult(list_data_point, data_time)        
        else:
            self.view_page_result.clearViewTableResult()

    # ::::::::::::::::::::      SLOT PAGE CHART     ::::::::::::::::::::
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
        
    @Slot(str)
    def signalChartAddCard(self, ids_point):
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
        times_x = self.model_result.getGrapihcsTimes()
        for id_point in ids_point:
            if id_point in list_keys:
                list_point_search.append(id_point)

        if len(list_point_search)>0:    
            for point_search in list_point_search:
                if not point_search in self.graphics_list_point:                   
                    
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

    @Slot(str)
    def changedGraphicsType(self, type_result):
        
        self.view_page_result.setTitleChart(type_result)
        self.view_page_result.setLabelYChart(type_result)
        self.view_page_result.canvas.draw()

        data = self.model_result.getResultNodes()    
        ymax = -1000*100
        ymin = 1000*100
        self.graphics_type_result  = type_result
        
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
               
    ###############################################################################
	# ::::::::::::::::::::          OTROS  MÉTODOS             ::::::::::::::::::::
	###############################################################################

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):
        self.current_project = model_current_project
        self.model_result = self.current_project.getModelResult()
        self.controller_menu_result_animation.setCurrentProject(self.current_project)
        self.controller_menu_result_graph.setCurrentProject(self.current_project)
        self.controller_menu_result_summary_table.setCurrentProject(self.current_project)
        
    def configResult(self):        
        if self.model_result != None:         
            self.view_page_result.updateViewTableResult('')           
            
           
    def getView(self):
        return self.view_page_result

    def animation(self):
        self.controller_graphics_result.animation()

    def createCardPoint(self, id_point, color):
        controller_card_point = ControllerResultCardPoint(id=id_point, color=color)
        self.controller_menu_result_graph.addCardPoint(controller_card_point.view_card_point)
        controller_card_point.signal_hide_show_point.connect(self.signalCardShowHidePoint)
        controller_card_point.signal_delete_point.connect(self.signalCardDeletePoint)
        controller_card_point.signal_update_color_point.connect(self.signalCardUpdateColorPoint)

        self.list_controller_card.append(controller_card_point)



