from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from clases.Vista.Resultados.view_WidgetResultMenuTable import ViewWidgetResultMenuTable
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardMesh import ControllerCardMesh
import pygmsh
import math
import time
from clases.general_functions import isNumber

class ControllerMenuResultTable(QObject):    
    signal_table_search_point = Signal(str)
    signal_table_clear = Signal()
    signal_table_hise_show_column = Signal(dict)
    
    def __init__(self) -> None:
        super().__init__()

        self.view_menu_result_table= ViewWidgetResultMenuTable()
     
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

        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
        self.view_menu_result_table.signal_table_search_point.connect(self.signalTableSearchPoint)
        self.view_menu_result_table.signal_table_clear.connect(self.signalTableClear)
        self.view_menu_result_table.signal_table_hise_show_column.connect(self.signalTableHiseShowColumn)   
        self.view_menu_result_table.signal_save_data.connect(self.signalSaveData) 
                
    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_result = self.model_current_project.getModelResult()     

    def getView(self):
        return self.view_menu_result_table

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
        
    # ::::::::::::::::::::      SLOT PAGE TABLE     ::::::::::::::::::::
    @Slot()
    def signalTableSearchPoint(self):        
        ids_point = self.view_menu_result_table.getIdPointSearch()
        self.signal_table_search_point.emit(ids_point)
        
    @Slot()
    def signalTableClear(self):
        self.signal_table_clear.emit()
        self.view_menu_result_table.clearLineEdit()
    
    @Slot(dict)
    def signalTableHiseShowColumn(self,dict_data):
        self.signal_table_hise_show_column.emit(dict_data)
        
    @Slot(str)
    def signalSaveData(self, path_data):
        graphic_times = self.model_result.getData()[1]
        result_nodes = self.model_result.getData()[2]
        with open(path_data, 'w') as file:
            for data_node in result_nodes:
                dt = graphic_times
                corx = result_nodes[data_node]['CORX']
                cory = result_nodes[data_node]['CORY']    

                sigxx = result_nodes[data_node]['SIGXX']            
                sigyy = result_nodes[data_node]['SIGYY']            
                sigxy = result_nodes[data_node]['SIGXY']   

                epsxx = result_nodes[data_node]['EPSXX']            
                epsyy = result_nodes[data_node]['EPSYY']            
                epsxy = result_nodes[data_node]['EPSXY'] 
                file.write('NODO TIMEPO CORX CORY SIGXX SIGYY SIGXY EPSXX EPSYY EPSXY\n')
                for i in range(len(graphic_times)):
                    file.write(str(data_node)+' '+str(dt[i])+' '+str(corx[i])+' '+str(cory[i])+' '+str(sigxx[i])+' '+str(sigyy[i])+' '+str(sigxy[i])+' '+str(epsxx[i])+' '+str(epsyy[i])+' '+str(epsxy[i])+'\n')      
                


        
      