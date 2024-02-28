from models.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from utils.items_GraphicsDraw import TextItem, PointItem
from views.view_GraphicsDraw import QGraphicsScene


class ModelItemPoint:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                 id, name, coordinates) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__id = id
        self.__name = name     
        self.__coordinates = coordinates
        
        

 
        x = coordinates[0]
        y = coordinates[1]

        
        text_name = TextItem(self.__name, 0, 0)        
        self.scene_draw.addItem(text_name)
        text_name.setZValue(100)
        

        self.point_item = PointItem(id, name,x,y, text_name)  
        self.scene_draw.addItem(self.point_item)
        self.point_item.setZValue(5)

  

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################


    
    def getPointItem(self):
        return self.point_item
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
 
    def getCoordinates(self):
        return self.__coordinates


    
    def getData(self):
        """return: id, name, type, coordinates]"""
        return[self.__id, self.__name, self.__coordinates]
       

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def deletePoint(self):
        self.scene_draw.removeItem(self.point_item)
        self.scene_draw.removeItem(self.point_item.text_name)
        self.scene_draw.update()


    def updatePoint(self,  id_point, name = None, coordinates = None):

        if name != None:
            self.__name = name
        if coordinates != None:
            self.__coordinates = coordinates
  

        self.model_project_current_repository.updateItemPointDrawDB(
            id_point=id_point,
            name=name,
            coordinates=coordinates
        )      

    def showHideItems(self, value):
        item_point = self.getPointItem()
        item_point.setVisible(value)



