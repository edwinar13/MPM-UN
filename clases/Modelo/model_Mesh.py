from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TriangleMeshItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup



class ModelMesh:

    def __init__(self, name, color, points, triangles) -> None:


        self.__name = name
        self.__color = color
        self.__points = points
        self.__triangles = triangles    

   

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    

    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color

    def getPoints(self):
        return self.__points

    def getTriangles(self):
        return self.__triangles
    
    def getData(self):
        """return: id, name, color, points, triangles]"""
        return[self.__name, self.__color, self.__points, self.__triangles]
       


class ModelMeshTriangle:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                 id, name, color, points, triangles) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__id = id
        self.__name = name
        self.__color = color
        self.__points = points
        self.__triangles = triangles    

        #crear item escena
        self.group_mesh  = QGraphicsItemGroup()
        for triangle in triangles:
            coordinates=[
                [points[triangle[0]][0],points[triangle[0]][1]],
                [points[triangle[1]][0],points[triangle[1]][1]],
                [points[triangle[2]][0],points[triangle[2]][1]],
                ]
            item = TriangleMeshItem(id=id,
                                      name=name,
                                     color=color,
                                     coordinates = coordinates)
            self.group_mesh.addToGroup(item)
        self.scene_draw.addItem(self.group_mesh)
        self.group_mesh.setZValue(-10)

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

    def getTriangles(self):
        return self.__triangles
    
    def getData(self):
        """return: id, name, color, points, triangles]"""
        return[self.__id, self.__name, self.__color, self.__points, self.__triangles]
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)
    
    def updateMesh(self,id_mesh, name= None, color= None, points= None, triangles = None):

        if name != None:
            self.__name = name
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)
        if points != None:
            self.__points = points

        if triangles != None:
            self.__triangles = triangles

        self.model_project_current_repository.updateMeshTriangularDB(
            id_Mesh =id_mesh,
            name=name,
            color=color,
            points=points,
            triangles=triangles
        )

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
