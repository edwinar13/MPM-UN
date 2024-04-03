
from PySide6.QtCore import (Slot, Signal, QObject)
from views.cards.view_WidgetCardProperty import viewCardDrawProperty
from models.model_Property import ModelProperty
from models.model_ProjectCurrent import ModelProjectCurrent
 
class ControllerCardProperty(QObject):

    signal_msn = Signal(str)
    signal_delete_property= Signal(str)
    signal_edit_property = Signal()

    def __init__(self, model_property:ModelProperty, model_current_project:ModelProjectCurrent) -> None:
        super().__init__()

        self.model_property = model_property
        self.model_current_project = model_current_project
        data = model_property.getData()
        '''
        {'f00e68c9-e12f-4b63-915c-215abcebad44':
    {
    'COLOR': '#646464',
    'NAME': 'material beam',
    'MODULOELASTICIDAD': 10000.0,
    'RELACIONPOISSON': 0.2,
    'COHESION': 5.0,
    'ANGULOFRICCION': 25.0,
    'DENSIDAD': 2000,
    'ANGULODILATANCIA': 5.0 }
}
        '''
        self.id = list(data.keys())[0]
        self.name = data[self.id]["NAME"]
        self.color = data[self.id]["COLOR"]
        self.modulus_elasticity = data[self.id]["MODULOELASTICIDAD"]
        self.poisson_ratio = data[self.id]["RELACIONPOISSON"]
        self.cohesion = data[self.id]["COHESION"]
        self.friction_angle = data[self.id]["ANGULOFRICCION"]
        self.density = data[self.id]["DENSIDAD"]
        self.angle_dilatancy = data[self.id]["ANGULODILATANCIA"]
        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_property = viewCardDrawProperty(self)
        self.view_card_property.showData(name = self.name,
                                         color  = self.color,
                                        modulus_elasticity=self.modulus_elasticity,
                                        poisson_ratio=self.poisson_ratio,
                                        cohesion=self.cohesion,
                                        friction_angle=self.friction_angle,
                                        density=self.density,
                                        angle_dilatancy=self.angle_dilatancy)

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        self.view_card_property.signal_delete_property.connect(self.deleteProperty)
        self.view_card_property.signal_update_property.connect(self.updateProperty)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
  
          

          

    @Slot(bool)
    def showHideProperties(self, value):  
        self.view_card_property.showHideProperties(value)
        
        
    @Slot()
    def deleteProperty(self):    
        # verificar que no este asignado a una MP
        models_materials_points = self.model_current_project.getModelsPointsMaterials()
        for id_model_material_point in models_materials_points:
            model_material_point = models_materials_points[id_model_material_point]
            
            name_MP =model_material_point.getName()
            id_property_to_MP= model_material_point.getProperty().getId()
                     
            if id_property_to_MP == self.id:
                self.signal_msn.emit("Material esta asignado a un MP [{}]".format(name_MP))
                return 
        self.view_card_property.deleteCardView()
        self.signal_delete_property.emit(self.id)
        del self
        
    @Slot()
    def updateProperty(self):
        self.name = self.view_card_property.getName()
        self.color = self.view_card_property.getColor()
        self.modulus_elasticity = self.view_card_property.getModulusElasticity()
        self.poisson_ratio= self.view_card_property.getPoissonRatio()
        self.cohesion= self.view_card_property.getCohesion()
        self.friction_angle= self.view_card_property.getFrictionAngle()
        self.density= self.view_card_property.getDensity()
        self.angle_dilatancy= self.view_card_property.getAngleDilatancy()

        self.model_property.updateProperty(
            id=self.id,
            name=self.name,
            color=self.color,
            modulus_elasticity=self.modulus_elasticity,
            poisson_ratio=self.poisson_ratio,
            cohesion=self.cohesion,
            friction_angle=self.friction_angle,
            density=self.density,
            angle_dilatancy=self.angle_dilatancy
            )
        self.signal_edit_property.emit()




