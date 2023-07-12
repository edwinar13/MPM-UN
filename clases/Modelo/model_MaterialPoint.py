from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextFrameItem, PointMaterialItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelMaterialPoint:

    def __init__(self, scene_draw:QGraphicsScene, model_project_current_repository:ModelProjectCurrentRepository,
                  id, name, color, points) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository

        self.__id = id
        self.__name = name
        self.__color = color
        self.__points = points 

        #crear item escena
        self.group_material_point  = QGraphicsItemGroup()
        for point in points:
            item = PointMaterialItem(id=id,
                                      name=name,
                                     color=color,
                                     coor=point)
            self.group_material_point.addToGroup(item)
        self.scene_draw.addItem(self.group_material_point)
        self.group_material_point.setZValue(10)

        sum_x = 0
        sum_y = 0
        for point in self.__points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(points)
        average_y = sum_y / len(points)

        self.text_name = TextFrameItem("PM:{}".format(self.__name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(10)
        
              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color

    def getPoints(self):
        return self.__points   

    def getData(self):
        """return: id, name, color, points]"""
        return[self.__id,self.__name, self.__color, self.__points]


    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideMaterialPoint(self, value):
        self.group_material_point.setVisible(value)
        
    def showHideLabel(self, value):   
        self.text_name.setVisible(value)   

    def ChangeSizePoint(self, value):   
        for item in self.group_material_point.childItems():
            if isinstance(item, PointMaterialItem):
                item.setRadius(value)
        self.scene_draw.update()
    
    def updateMaterialPoint(self,id_MP, name= None, color= None, points= None ):

        if name != None:
            self.__name = name
            self.text_name.text= "PM:{}".format(self.__name)
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)
        if points != None:
            self.__points = points

        self.model_project_current_repository.updateMaterialPointDB(
            id_MP=id_MP,
            name=name,
            color=color,
            points=points
        )

    def setColorItem(self, color):
        for item in self.group_material_point.childItems():
            if isinstance(item, PointMaterialItem):
                item.setColor(color)
        self.scene_draw.update()
    
    def deleteMaterialPoint(self):
        for item in self.group_material_point.childItems():
            self.group_material_point.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_material_point)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

                