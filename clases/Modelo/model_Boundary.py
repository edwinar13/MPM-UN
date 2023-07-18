from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository

from clases.items_GraphicsDraw import TextFrameItem, PointBoundaryTxItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelBoundary:

    def __init__(self, scene_draw:QGraphicsScene, model_project_current_repository:ModelProjectCurrentRepository,
                  id, name, points, Tx , Ty) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository

        self.__id = id
        self.__name = name
        self.__points = points 
        self.__restrictionX = Tx
        self.__restrictionY = Ty


        #crear item escena
        self.group_boundary  = QGraphicsItemGroup()
        for point in points:
            item = PointBoundaryTxItem(id=id,
                                      name=name,
                                     coordinatesX=point[0],
                                     coordinatesY=point[1],
                                     Tx=Tx,
                                     Ty=Ty
                                     )
            self.group_boundary.addToGroup(item)
        self.scene_draw.addItem(self.group_boundary)
        self.group_boundary.setZValue(15)

        sum_x = 0
        sum_y = 0
        for point in self.__points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(points)
        average_y = sum_y / len(points)

        self.text_name = TextFrameItem("B:{}".format(self.__name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(20)
        
              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPoints(self):
        return self.__points   
    
    def getRestrictionX(self):
        return self.__restrictionX

    def getRestrictionY(self):
        return self.__restrictionY

    def getData(self):
        """return: id, name,  points, restrictionX, restrictionY]]"""
        return[self.__id,self.__name, self.__points, self.__restrictionX, self.__restrictionY]


         


    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideBoundary(self, value):
        self.group_boundary.setVisible(value)
        
    def showHideLabel(self, value):   
        self.text_name.setVisible(value)   

    
    def updateBoundary(self,id_boundary, name= None, points= None, restrictionX = None, restrictionY = None):

        if name != None:
            self.__name = name
            self.text_name.text= "B:{}".format(self.__name)
        if points != None:
            self.__points = points
        if restrictionX != None:
            self.__restrictionX = restrictionX
        if restrictionY != None:
            self.__restrictionY = restrictionY
        self.model_project_current_repository.updateBoundaryDB(
            id_boundary=id_boundary,
            name=name,
            points=points,
            restrictionX=restrictionX,
            restrictionY=restrictionY
        )


    def deleteBoundary(self):
        for item in self.group_boundary.childItems():
            self.group_boundary.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_boundary)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()


    def stateViewBoundary(self, data):   
        for item in self.group_boundary.childItems():
            if isinstance(item, PointBoundaryTxItem):
                item.isSelectedBoundary = data["state_view"]
        self.scene_draw.update()