from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from views.results.view_WidgetResultMenuGraph import ViewWidgetResultMenuGraph
from models.model_ProjectCurrent import ModelProjectCurrent
from utils.general_functions import isNumber

class ControllerMenuResultGraph(QObject):   
    
    signal_change_graphics_type = Signal(str) 
    signal_chart_add_card = Signal(str)
    signal_change_graphics_type_style = Signal()
    signal_show_hide_series = Signal(bool)
    signal_show_hide_label = Signal(bool)
    signal_delete_series = Signal()
    
    signal_set_max_min = Signal(list)        
    signal_update_limit = Signal(str)
    
    def __init__(self) -> None:
        super().__init__()

        self.view_menu_result_graph= ViewWidgetResultMenuGraph()
     
        self.model_current_project = None
        self.model_result = None
        self.scene_is_play = True        
        
        self.graphics_list_point =[]

        self.__config()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __config(self): 
        pass

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """         
        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
        self.view_menu_result_graph.signal_chart_type_result.connect(self.signalChartTypeResult)
        self.view_menu_result_graph.signal_chart_add_card.connect(self.signalChartAddCard)
        self.view_menu_result_graph.signal_chart_type_style.connect(self.signalChartTypeStyle)
        
        self.view_menu_result_graph.signal_show_hide_series.connect(self.signalShowHideSeries)
        self.view_menu_result_graph.signal_show_hide_label.connect(self.signalShowHideLabel)
        self.view_menu_result_graph.signal_delete_series.connect(self.signalDeleteSeries)  
        
        self.view_menu_result_graph.signal_max_min.connect(self.signalSetMaxMIn)  
        self.view_menu_result_graph.signal_update_limit.connect(self.signalUpdateLimit)  
        

    
        
        
        
                
    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_result = self.model_current_project.getModelResult()  
   
    def getView(self):
        return self.view_menu_result_graph

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
        
    # ::::::::::::::::::::      SLOT PAGE CHART     ::::::::::::::::::::
    @Slot()
    def signalChartAddCard(self):  
        ids_point = self.view_menu_result_graph.getIdPointGraphics()
        self.signal_chart_add_card.emit(ids_point)
        self.view_menu_result_graph.lineEdit_chartPointName.setText("")

    @Slot()
    def signalChartTypeResult(self): 
        self.graphics_type_result = self.view_menu_result_graph.getTypeResult() 
        self.signal_change_graphics_type.emit(self.graphics_type_result)

    @Slot()
    def signalChartTypeStyle(self):       
        self.signal_change_graphics_type_style.emit() 
        
    @Slot(bool)
    def signalShowHideSeries(self, show_series):
        self.signal_show_hide_series.emit(show_series)
    
    @Slot(bool)
    def signalShowHideLabel(self, show_label):
        self.signal_show_hide_label.emit(show_label)
    
    @Slot()
    def signalDeleteSeries(self):
        self.signal_delete_series.emit()
    
    @Slot(list)
    def signalSetMaxMIn(self, limits):
        self.signal_set_max_min.emit(limits)
    
    @Slot()
    def signalUpdateLimit(self):
        type_data = self.view_menu_result_graph.getTypeResult()
        self.signal_update_limit.emit(type_data)




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
    
    def addCardPoint(self, card_point): 
        self.view_menu_result_graph.addCardPoint(card_point)       

    def updateMenuResults(self):        
        self.view_menu_result_graph.resetTypeResult()