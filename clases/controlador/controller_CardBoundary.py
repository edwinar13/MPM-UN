
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardBoundary import viewCardDrawBoundary
from clases.Modelo.model_Boundary import ModelBoundary

class ControllerCardBoundary(QObject):

  
    signal_delete_boundary = Signal(str)


    def __init__(self, model_boundary:ModelBoundary) -> None:
        super().__init__()

        self.model_boundary = model_boundary
        self.id, self.name, self.nodes, self.points, self.restrictionX, self.restrictionY = model_boundary.getData()


        self.__initCard()
        self.__initEvent()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_boundary = viewCardDrawBoundary(self)
        self.view_card_boundary.showData(name = self.name, Tx=self.restrictionX, Ty=self.restrictionY)
    
    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_card_boundary.signal_hide_show_boundary.connect(self.showHideBoundary)
        self.view_card_boundary.signal_delete_boundary.connect(self.deleteBoundary)
        self.view_card_boundary.signal_update_boundary.connect(self.updateBoundary)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    @Slot(bool)
    def showHideBoundary(self, value):
        self.model_boundary.showHideBoundary(value)
        self.view_card_boundary.showHideBoundary(value)

    @Slot(bool)
    def showHideLabel(self, value):
        self.model_boundary.showHideLabel(value)

    @Slot()
    def deleteBoundary(self):        
        self.signal_delete_boundary.emit(self.id)
        del self


    @Slot()
    def updateBoundary(self):        
        self.name = self.view_card_boundary.getName()

        self.model_boundary.updateBoundary(
            id_boundary = self.id,
            name=self.name,
            )





