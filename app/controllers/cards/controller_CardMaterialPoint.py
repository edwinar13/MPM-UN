
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
        #return[self.__id,self.__name, self.__color, self.__points, self.__volumes, self.__property, self.__mesh_base]  
        self.id, self.name, self.color, self.points,self.__volumes , self.name_property, self.mesh_base = model_point_material.getData()
       

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
        self.view_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)
        self.view_card_material_point.signal_update_material_point.connect(self.updateMaterialPoint)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################

    
    def showHideMaterialPoint(self, value):
        self.model_point_material.showHideMaterialPoint(value)  
        self.view_card_material_point.ShowHideMaterialPoint(value)

    @Slot(bool)
    def showHideLabel(self, value):
        self.model_point_material.showHideLabel(value)     
          
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
        self.color = self.view_card_material_point.getColor()
        self.id_property, self.name_property = self.view_card_material_point.getProperty()

        property_ = self.model_project_current.getModelsProperties()[self.id_property]

        self.model_point_material.updateMaterialPoint(
            id_MP= self.id,
            name=self.name,
            color=self.color,
            property=property_,
            mesh_base=self.mesh_base
            )
        self.signal_edit_material_point.emit()


    def setListPropertiesViews(self, properties_data):   
        self.name_property = self.model_point_material.getProperty().getName()
        self.view_card_material_point.setListProperties(properties_data=properties_data, selected_property=self.name_property)     

    def setListBaseMeshViews(self):  
        name_mesh = self.mesh_base.getName()        
        self.view_card_material_point.setBaseMesh(name_mesh=name_mesh)


