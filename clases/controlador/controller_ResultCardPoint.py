
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetResultCardPoint import viewResultCardPoint
from clases.Modelo.model_Mesh import ModelMeshTriangle, ModelMeshQuadrilateral

class ControllerResultCardPoint(QObject):

  
    signal_hide_show_point = Signal(dict)
    signal_delete_point= Signal(str) 
    signal_update_color_point= Signal(dict) 

    #def __init__(self, model_mesh:ModelMeshTriangle|ModelMeshQuadrilateral) -> None:
    def __init__(self, id, color) -> None:
        super().__init__()

        #self.model_mesh = model_mesh
        #self.id, self.name, self.color, self.points, self.elements = model_mesh.getData()
        self.id =id
        self.color = color

   
        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_point = viewResultCardPoint(self)
        self.view_card_point.showData(name = self.id, color = self.color)
    
    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_card_point.signal_hide_show_point.connect(self.showHidePoint)
        self.view_card_point.signal_delete_point.connect(self.deletePoint)
        self.view_card_point.signal_update_color_point.connect(self.updateColorPoint)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    @Slot(bool)
    def showHidePoint(self, value):
        self.signal_hide_show_point.emit({'id':self.id, 'show':value})
        self.view_card_point.ShowHidePoint(value)
    
    @Slot(bool)
    def showHideAllPoint(self, value):
        self.view_card_point.ShowHidePoint(value)
    

    @Slot()
    def deletePoint(self):
        self.signal_delete_point.emit(self.id)
        del self
        
    def deleteAllSeries(self):        
        self.view_card_point.deleteLater()
        del self


    @Slot()
    def updateColorPoint(self):        
        self.color = self.view_card_point.getColor()

        self.signal_update_color_point.emit({'id':self.id, 'color':self.color})





