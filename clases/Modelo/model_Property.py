from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextFrameItem, PointMaterialItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelProperty:

    def __init__(self, scene_draw:QGraphicsScene, 
                        model_project_current_repository:ModelProjectCurrentRepository,
                        id, 
                        name,
                        modulus_elasticity,
                        poisson_ratio,
                        cohesion,
                        friction_angle,
                        density,
                        angle_dilatancy) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository

        self.__id = id
        self.__name = name
        self.__modulus_elasticity=modulus_elasticity
        self.__poisson_ratio=poisson_ratio
        self.__cohesion=cohesion
        self.__friction_angle=friction_angle
        self.__density=density
        self.__angle_dilatancy=angle_dilatancy


        
              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getModulusElasticity(self):
        return self.__modulus_elasticity

    def getPoissonRatio(self):
        return self.__poisson_ratio

    def getCohesion(self):
        return self.__cohesion  
    
    def getFrictionAngle(self):
        return self.__friction_angle
    
    def getDensity(self):
        return self.__density
    
    def getAngleDilatancy(self):
        return self.__angle_dilatancy 

    def getData(self):
        """return: id, name, 
        modulus_elasticity, poisson_ratio,
        cohesion,friction_angle,
        angle_dilatancy]"""
        return[self.__id,self.__name, 
                self.__modulus_elasticity,
                self.__poisson_ratio,
                self.__cohesion,
                self.__friction_angle,
                self.__density,
                self.__angle_dilatancy
                ]


    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    

    
    def updateProperty(self,id, name= None, 
                       modulus_elasticity= None,
                        poisson_ratio= None,
                        cohesion= None,
                        friction_angle= None,
                        density= None,
                        angle_dilatancy= None ):

        if name != None:
            self.__name = name
        if modulus_elasticity != None:
            self.__modulus_elasticity = modulus_elasticity
        if poisson_ratio != None:
            self.__poisson_ratio = poisson_ratio
        if cohesion != None:
            self.__cohesion = cohesion
        if friction_angle != None:
            self.__friction_angle = friction_angle
        if density != None:
            self.__density = density
        if angle_dilatancy != None:
            self.__angle_dilatancy = angle_dilatancy
        
        self.model_project_current_repository.updatePropertiesDB(
            id_properties=id,
            name=name,
            modulus_elasticity=modulus_elasticity,
            poisson_ratio=poisson_ratio,
            cohesion=cohesion,
            friction_angle=friction_angle,
            density=density,
            angle_dilatancy=angle_dilatancy
            )

                