
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardMaterialPoint import viewCardDrawMaterialPoint
from clases.Modelo.model_MaterialPoint import ModelMaterialPoint
 
class ControllerCardMaterialPoint(QObject):

    signal_hide_show_material_point = Signal(list)
    signal_delete_material_point= Signal(str)

    def __init__(self, model_point_material:ModelMaterialPoint) -> None:
        super().__init__()

        self.model_point_material = model_point_material
        self.id, self.name, self.color, self.points = model_point_material.getData()

        self.__initCard()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_material_point = viewCardDrawMaterialPoint(self)
        self.view_card_material_point.showData(name = self.name, color = self.color)

        self.view_card_material_point.signal_hide_show_material_point.connect(self.showHideMaterialPoint)
        self.view_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)
        self.view_card_material_point.signal_update_material_point.connect(self.updateMaterialPoint)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    @Slot(bool)
    def showHideMaterialPoint(self, value):
        self.model_point_material.showHideMaterialPoint(value)        

    @Slot()
    def deleteMaterialPoint(self):        
        self.signal_delete_material_point.emit(self.id)
        del self
        
    @Slot()
    def updateMaterialPoint(self):
        self.name = self.view_card_material_point.getName()
        self.color = self.view_card_material_point.getColor()
        self.model_point_material.updateMaterialPoint(
            id_MP= self.id,
            name=self.name,
            color=self.color
            )




