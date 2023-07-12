
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardProperty import viewCardDrawProperty
from clases.Modelo.model_Property import ModelProperty
 
class ControllerCardProperty(QObject):

    
    signal_delete_property= Signal(str)

    def __init__(self, model_property:ModelProperty) -> None:
        super().__init__()

        self.model_property = model_property
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




