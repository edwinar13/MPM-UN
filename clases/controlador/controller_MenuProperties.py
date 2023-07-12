
from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from clases.Vista.view_WidgetDrawMenuProperties import ViewWidgetDrawMenuProperties
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardProperty import ControllerCardProperty

class ControllerMenuProperties():

    def __init__(self) -> None:

        
        self.view_menu_properties = ViewWidgetDrawMenuProperties()
        self.model_current_project = None
        self.list_controller_card=[]


        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
   

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_properties.signal_new_property.connect(self.newProperty)

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
       
    def configDrawMenuProperties(self):
        
        self.view_menu_properties.removeCardProperty()
        self.list_controller_card=[]

        models_properties = self.model_current_project.getModelsProperties()
        for id_properties in models_properties:
            self.createPropertyCard(models_properties[id_properties])

        
    def getView(self):
        return self.view_menu_properties
    

    def createPropertyCard(self, model_property):
        controller_card_property = ControllerCardProperty( model_property = model_property)
        self.view_menu_properties.addCardProperty(controller_card_property.view_card_property)
        controller_card_property.signal_delete_property.connect(self.deleteProperty)
        #controller_card_property.signal_edit_property.connect(self.editProperty)

        self.list_controller_card.append(controller_card_property)




    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::

    @Slot()
    def newProperty(self):

        property_name =self.view_menu_properties.getName()
        modulus_elasticity=self.view_menu_properties.getPropertiesE()
        poisson_ratio =self.view_menu_properties.getPropertiesV()
        cohesion =self.view_menu_properties.getPropertiesC()
        friction_angle =self.view_menu_properties.getPropertiesPhi()
        angle_dilatancy =self.view_menu_properties.getPropertiesPsi()


    
         
        if property_name == "":
            self.view_menu_properties.msnAlertName(True, "Revisa el nombre  de la propiedad")
            return     
        else:
            self.view_menu_properties.msnAlertName(False)
    
   
            
        id = self.model_current_project.createProperty(name=property_name,
                                                    modulus_elasticity=modulus_elasticity,
                                                    poisson_ratio=poisson_ratio,
                                                    cohesion=cohesion,
                                                    friction_angle=friction_angle,
                                                    angle_dilatancy = angle_dilatancy)
        model_property = self.model_current_project.getModelsProperties()[id]
        self.createPropertyCard(model_property)

        self.view_menu_properties.endProperty()

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(list)
    def deleteProperty(self, id):       
        self.model_current_project.deleteProperty(id)

        


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

