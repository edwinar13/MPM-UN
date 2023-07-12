
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardProperty import viewCardDrawProperty
from clases.Modelo.model_Property import ModelProperty
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
 
class ControllerCardProperty(QObject):

    signal_msn = Signal(str)
    signal_delete_property= Signal(str)
    signal_edit_property = Signal()

    def __init__(self, model_property:ModelProperty, model_current_project:ModelProjectCurrent) -> None:
        super().__init__()

        self.model_property = model_property
        self.model_current_project = model_current_project
        self.id, self.name, self.modulus_elasticity, self.poisson_ratio, self.cohesion, self.friction_angle, self.angle_dilatancy= model_property.getData()
        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_property = viewCardDrawProperty(self)
        self.view_card_property.showData(name = self.name,
                                        modulus_elasticity=self.modulus_elasticity,
                                        poisson_ratio=self.poisson_ratio,
                                        cohesion=self.cohesion,
                                        friction_angle=self.friction_angle,
                                        angle_dilatancy=self.angle_dilatancy)

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        self.view_card_property.signal_delete_property.connect(self.deleteProperty)
        self.view_card_property.signal_update_property.connect(self.updateProperty)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
  
          

          

    @Slot()
    def showHideProperty(self):        
        pass
        
    @Slot()
    def deleteProperty(self):    
        # verificar que no este asignado a una MP
        models_materials_points = self.model_current_project.getModelsPointsMaterials()
        for id_model_material_point in models_materials_points:
            model_material_point = models_materials_points[id_model_material_point]
            name_MP =model_material_point.getName()
            name_property_to_MP= model_material_point.getProperty().getName()
            print(self.name , name_property_to_MP)
            if self.name == name_property_to_MP:
                self.signal_msn.emit("Material este asignado a un MP [{}]".format(name_MP))
                return 
        self.view_card_property.deleteCardView()
        self.signal_delete_property.emit(self.id)
        del self
        
    @Slot()
    def updateProperty(self):
        self.name = self.view_card_property.getName()
        self.modulus_elasticity = self.view_card_property.getModulusElasticity()
        self.poisson_ratio= self.view_card_property.getPoissonRatio()
        self.cohesion= self.view_card_property.getCohesion()
        self.friction_angle= self.view_card_property.getFrictionAngle()
        self.angle_dilatancy= self.view_card_property.getAngleDilatancy()

        self.model_property.updateProperty(
            id=self.id,
            name=self.name,
            modulus_elasticity=self.modulus_elasticity,
            poisson_ratio=self.poisson_ratio,
            cohesion=self.cohesion,
            friction_angle=self.friction_angle,
            angle_dilatancy=self.angle_dilatancy
            )
        self.signal_edit_property.emit()




