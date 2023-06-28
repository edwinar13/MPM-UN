from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextItem, PointItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene





class ModelItemPoint:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                 id, name, coordinates, lines) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__id = id
        self.__name = name     
        self.__coordinates = coordinates
        self.__lines = lines   
        

 
        x = coordinates[0]
        y = coordinates[1]

        
        text_name = TextItem(self.__name, 0, 0)        
        self.scene_draw.addItem(text_name)

        self.point_item = PointItem(id, name,x,y, text_name)  
        self.scene_draw.addItem(self.point_item)

  

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

    def getLines(self):
        return self.__lines
    
    def getData(self):
        """return: id, name, type, coordinates, lines]"""
        return[self.__id, self.__name, self.__coordinates, self.__lines]
       

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def deletePoint(self):
        self.scene_draw.removeItem(self.point_item)
        self.scene_draw.removeItem(self.point_item.text_name)
        self.scene_draw.update()

    
    def updatePoint(self,  id_point, name = None, coordinates = None, lines = None):

        if name != None:
            self.__name = name
        if coordinates != None:
            self.__coordinates = coordinates
        if lines != None:
            self.__lines = lines

        self.model_project_current_repository.updateItemPointDrawDB(
            id_point=id_point,
            name=name,
            coordinates=coordinates,
            lines=lines
        )        


    '''
   
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)
    def setColorItem(self, color):
        for item in self.group_mesh.childItems():
            if isinstance(item, TriangleMeshItem):
                item.setColor(color)
        self.scene_draw.update()
    
    def deleteMesh(self):

        for item in self.group_mesh.childItems():
            self.group_mesh.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_mesh)
        self.scene_draw.update()

        
    '''