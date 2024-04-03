from models.model_Repository import ModelRepository
from views.view_GraphicsDraw import QGraphicsScene

class ModelProperty:

    def __init__(self, scene_draw:QGraphicsScene, 
                        model_repository:ModelRepository,
                        id) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository

        self.__id = id



        
              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        return self.__id
    
    def getColor(self):
        """ funcion para obtener el color del conjunto de puntos material"""
        color = self.getData()[self.__id]["COLOR"]
        return color

    def getName(self):
        name = self.getData()[self.__id]["NAME"]
        return name
    
    def getModulusElasticity(self):
        modulus_elasticity = self.getData()[self.__id]["MODULOELASTICIDAD"]
        return modulus_elasticity

    def getPoissonRatio(self):
        poisson_ratio = self.getData()[self.__id]["RELACIONPOISSON"]
        return poisson_ratio

    def getCohesion(self):
        cohesion = self.getData()[self.__id]["COHESION"]
        return cohesion  
    
    def getFrictionAngle(self):
        friction_angle = self.getData()[self.__id]["ANGULOFRICCION"]
        return friction_angle
    
    def getDensity(self):
        density = self.getData()[self.__id]["DENSIDAD"]
        return density
    
    def getAngleDilatancy(self):
        angle_dilatancy = self.getData()[self.__id]["ANGULODILATANCIA"]
        return angle_dilatancy 

    def getData(self):
        
        """return: dict con los datos de la propiedad, por ejemplo:
        
        {'f00e68c9-e12f-4b63-915c-215abcebad44': 
            {
            'COLOR': '#646464',
            'NAME': 'material beam', 
            'MODULOELASTICIDAD': 10000.0,
            'RELACIONPOISSON': 0.2,
            'COHESION': 5.0,
            'ANGULOFRICCION': 25.0, 
            'DENSIDAD': 2000, 
            'ANGULODILATANCIA': 5.0
            }
        }
        """
    
        
        properties =  self.model_repository.readPropertiesDB()
        property_data ={
            self.__id: properties[self.__id]
        }
        return property_data
        

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    

    
    def updateProperty(self,id, name= None, color= None,
                       modulus_elasticity= None,
                        poisson_ratio= None,
                        cohesion= None,
                        friction_angle= None,
                        density= None,
                        angle_dilatancy= None ):

        
        self.model_repository.updatePropertiesDB(
            id_properties=id,
            name=name,
            color=color,
            modulus_elasticity=modulus_elasticity,
            poisson_ratio=poisson_ratio,
            cohesion=cohesion,
            friction_angle=friction_angle,
            density=density,
            angle_dilatancy=angle_dilatancy
            )

                