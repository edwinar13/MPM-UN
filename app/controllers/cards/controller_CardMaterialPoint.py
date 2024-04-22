
from PySide6.QtCore import (Slot, Signal, QObject)
from views.cards.view_WidgetCardMaterialPoint import viewCardDrawMaterialPoint
from models.model_MaterialPoint import ModelMaterialPoint
from models.model_ProjectCurrent import ModelProjectCurrent
 
class ControllerCardMaterialPoint(QObject):

    
    signal_delete_material_point= Signal(str)
    signal_edit_material_point= Signal()

    def __init__(self,model_project_current:ModelProjectCurrent, model_point_material:ModelMaterialPoint) -> None:
        super().__init__()
        self.model_project_current = model_project_current
        self.model_point_material = model_point_material    

        data = self.model_point_material.getData()
        self.id = list(data.keys())[0]
        self.name = data[self.id]["NAME"]
        self.name_property = self.model_point_material.getProperty()
        self.color = self.name_property.getColor()
        self.mesh_base = self.model_point_material.getMeshBase()
        
        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_material_point = viewCardDrawMaterialPoint(self)
        self.view_card_material_point.showData(name = self.name, color = self.color, name_property=self.name_property, name_mesh=self.mesh_base.getName())

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_card_material_point.signal_hide_show_material_point.connect(self.showHideMaterialPoint)
        self.view_card_material_point.signal_hide_show_label.connect(self.showHideLabel)
        self.view_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)
        self.view_card_material_point.signal_update_material_point.connect(self.updateMaterialPoint)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################

    
    @Slot(bool)
    def showHideMaterialPoint(self, value):
        self.model_point_material.showHideMaterialPoint(value)  
        self.view_card_material_point.ShowHideMaterialPoint(value)
        if value == False:
            self.showHideLabel(value)
    
    @Slot(bool)
    def showHideLabel(self, value):
        self.model_point_material.showHideLabel(value)     
        self.view_card_material_point.showHideLabel(value)
    
    @Slot(bool)
    def showHideLabelTitle(self, value):
        self.model_point_material.showHideLabelTitle(value)    
          
    @Slot(bool)
    def ChangeSizePoint(self, value):
        self.model_point_material.ChangeSizePoint(value)     

          

    @Slot()
    def deleteMaterialPoint(self):
        #verficar que no este seleccionado para ejecutar un analisis
        
                
        self.signal_delete_material_point.emit(self.id)
        del self
        
    @Slot()
    def updateMaterialPoint(self):
        self.name = self.view_card_material_point.getName()
        self.id_property, self.name_property = self.view_card_material_point.getProperty()

        property_ = self.model_project_current.getModelsProperties()[self.id_property]

        self.model_point_material.updateMaterialPoint(
            id_MP= self.id,
            name=self.name,
            property=property_,
            mesh_base=self.mesh_base
            )
        self.setColor()
        self.signal_edit_material_point.emit()
        

    def setListPropertiesViews(self, properties_data):   
        self.name_property = self.model_point_material.getProperty().getName()
        self.view_card_material_point.setListProperties(properties_data=properties_data, selected_property=self.name_property)     
    
    def setColor(self):
        
        color = self.model_point_material.getProperty().getColor()
        self.view_card_material_point.setColor(color)
        self.model_point_material.setColorItem(color)
        
    def setListBaseMeshViews(self):  
        name_mesh = self.mesh_base.getName()        
        self.view_card_material_point.setBaseMesh(name_mesh=name_mesh)


