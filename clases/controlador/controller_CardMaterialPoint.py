
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardMaterialPoint import viewCardDrawMaterialPoint
from clases.Modelo.model_MaterialPoint import ModelMaterialPoint
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
 
class ControllerCardMaterialPoint(QObject):

    
    signal_delete_material_point= Signal(str)

    def __init__(self,model_project_current:ModelProjectCurrent, model_point_material:ModelMaterialPoint) -> None:
        super().__init__()
        self.model_project_current = model_project_current
        self.model_point_material = model_point_material      
        self.id, self.name, self.color, self.points, self.name_property = model_point_material.getData()


        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_material_point = viewCardDrawMaterialPoint(self)
        self.view_card_material_point.showData(name = self.name, color = self.color, name_property=self.name_property )

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_card_material_point.signal_hide_show_material_point.connect(self.showHideMaterialPoint)
        self.view_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)
        self.view_card_material_point.signal_update_material_point.connect(self.updateMaterialPoint)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    @Slot(bool)
    def showHideMaterialPoint(self, value):
        self.model_point_material.showHideMaterialPoint(value)  

    @Slot(bool)
    def showHideLabel(self, value):
        self.model_point_material.showHideLabel(value)     
          
    @Slot(bool)
    def ChangeSizePoint(self, value):
        self.model_point_material.ChangeSizePoint(value)     

          

    @Slot()
    def deleteMaterialPoint(self):        
        self.signal_delete_material_point.emit(self.id)
        del self
        
    @Slot()
    def updateMaterialPoint(self):
        self.name = self.view_card_material_point.getName()
        self.color = self.view_card_material_point.getColor()
        self.id_property, self.name_property = self.view_card_material_point.getProperty()

        property_ = self.model_project_current.getModelsProperties()[self.id_property]

        self.model_point_material.updateMaterialPoint(
            id_MP= self.id,
            name=self.name,
            color=self.color,
            property=property_
            )


    def setListPropertiesViews(self, properties_data):   
        self.name_property = self.model_point_material.getProperty().getName()
        self.view_card_material_point.setListProperties(properties_data=properties_data, selected_property=self.name_property)     




