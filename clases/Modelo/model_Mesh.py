from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextFrameItem, PointMeshBackItem, TriangleMeshItem, QuadrilateraLMeshItem, QuadrilateraLMeshBackItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup


'''
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

'''

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
        self.group_mesh.setZValue(5)

        sum_x = 0
        sum_y = 0
        for point in self.__points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(points)
        average_y = sum_y / len(points)

        self.text_name = TextFrameItem("MT:{}".format(self.__name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(5)
        

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    def getType(self):
        return "TRIANGULAR"
    
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

    def showHideLabel(self, value):
        self.text_name.setVisible(value)

    
    def updateMesh(self,id_mesh, name= None, color= None, points= None, triangles = None):

        if name != None:
            self.__name = name
            self.text_name.text= "MT:{}".format(self.__name)
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
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

class ModelMeshQuadrilateral:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                 id, name, color, points, quadrilaterals) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__id = id
        self.__name = name
        self.__color = color
        self.__points = points
        self.__quadrilaterals = quadrilaterals    

        #crear item escena
        self.group_mesh  = QGraphicsItemGroup()

        for quadrilateral in quadrilaterals:
            coordinates=[
                [points[quadrilateral[0]][0],points[quadrilateral[0]][1]],
                [points[quadrilateral[1]][0],points[quadrilateral[1]][1]],
                [points[quadrilateral[2]][0],points[quadrilateral[2]][1]],
                [points[quadrilateral[3]][0],points[quadrilateral[3]][1]]
                ]
            item = QuadrilateraLMeshItem(id=id,
                                      name=name,
                                     color=color,
                                     coordinates = coordinates)
            self.group_mesh.addToGroup(item)
        self.scene_draw.addItem(self.group_mesh)
        self.group_mesh.setZValue(5)

        sum_x = 0
        sum_y = 0
        for point in self.__points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(points)
        average_y = sum_y / len(points)

        self.text_name = TextFrameItem("MQ:{}".format(self.__name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(5)

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    
    def getType(self):
        return "QUADRILATERAL"
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color

    def getPoints(self):
        return self.__points

    def getQuadrilaterals(self):
        return self.__quadrilaterals
    
    def getData(self):
        """return: id, name, color, points, quadrilaterals]"""
        return[self.__id, self.__name, self.__color, self.__points, self.__quadrilaterals]
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)

    def showHideLabel(self, value):
        self.text_name.setVisible(value)
    
    def updateMesh(self,id_mesh, name= None, color= None, points= None, quadrilaterals = None):

        if name != None:
            self.__name = name
            self.text_name.text= "MQ:{}".format(self.__name)
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)
        if points != None:
            self.__points = points

        if quadrilaterals != None:
            self.__quadrilaterals = quadrilaterals

        self.model_project_current_repository.updateMeshQuadrilateralDB(
            id_Mesh =id_mesh,
            name=name,
            color=color,
            points=points,
            quadrilaterals=quadrilaterals
        )

    def setColorItem(self, color):
        for item in self.group_mesh.childItems():
            if isinstance(item, QuadrilateraLMeshItem):
                item.setColor(color)
        self.scene_draw.update()
    
    def deleteMesh(self):

        for item in self.group_mesh.childItems():
            self.group_mesh.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_mesh)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()


class ModelMeshBack:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                size_dx, size_dy, size_element, color, points, quadrilaterals) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__size_dx = size_dx
        self.__size_dy = size_dy
        self.__size_element = size_element
        self.__color = color
        self.__points = points
        self.__quadrilaterals = quadrilaterals    

        #crear item escena
        self.group_mesh  = QGraphicsItemGroup()

        for quadrilateral in quadrilaterals:


            coordinates=[
                [points[quadrilateral[0]][0],points[quadrilateral[0]][1]],
                [points[quadrilateral[1]][0],points[quadrilateral[1]][1]],
                [points[quadrilateral[2]][0],points[quadrilateral[2]][1]],
                [points[quadrilateral[3]][0],points[quadrilateral[3]][1]]
                ]
            
            p1 = PointMeshBackItem(quadrilateral[0], points[quadrilateral[0]][0], points[quadrilateral[0]][1])
            p2 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[1]][0], points[quadrilateral[1]][1])
            p3 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[2]][0], points[quadrilateral[2]][1])
            p4 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[3]][0], points[quadrilateral[3]][1])
            self.group_mesh.addToGroup(p1)
            self.group_mesh.addToGroup(p2)
            self.group_mesh.addToGroup(p3)
            self.group_mesh.addToGroup(p4)
            
            item = QuadrilateraLMeshBackItem(
                                        color=color,
                                        coordinates = coordinates,
                                        p1=p1,
                                        p2=p2,
                                        p3=p3,
                                        p4=p4)
            self.group_mesh.addToGroup(item)
        self.scene_draw.addItem(self.group_mesh)
        self.group_mesh.setZValue(4)
        self.showHideMesh(False)

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    
        

    
    def getSizeDx(self):
        return self.__size_dx
    
    def getSizeDy(self):
        return self.__size_dy

    def getSizeElement(self):
        return self.__size_element
    
    def getColor(self):
        return self.__color

    def getPoints(self):
        return self.__points

    def getQuadrilaterals(self):
        return self.__quadrilaterals
    
    def getData(self):
        """return: size_dx, size_dy, size_element, color, points, quadrilaterals]"""
        return[self.__size_dx, self.__size_dy, self.__size_element, self.__color, self.__points, self.__quadrilaterals]
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)
    
    def updateMesh(self,size_dx=None, size_dy= None, size_element=None, color= None, points= None, quadrilaterals = None):

        if size_dx != None:
            self.__size_dx = size_dx
        if size_dy != None:
            self.__size_dy = size_dy
        if size_element != None:
            self.__size_element = size_element
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)
        if points != None:
            self.__points = points
        if quadrilaterals != None:
            self.__quadrilaterals = quadrilaterals


        self.model_project_current_repository.updateMeshBackDB(
            size_dx=size_dx,
            size_dy=size_dy,
            size_element = size_element,
            color=color,
            points=points,
            quadrilaterals=quadrilaterals
        )
        self.setPointsQuadrilateralsItem()



    def setPointsQuadrilateralsItem(self):
        for item in self.group_mesh.childItems():
            self.group_mesh.removeFromGroup(item)
            self.scene_draw.removeItem(item)   

        color = self.__color
        points = self.__points
        quadrilaterals = self.__quadrilaterals


        for quadrilateral in quadrilaterals:
            coordinates=[
                [points[quadrilateral[0]][0],points[quadrilateral[0]][1]],
                [points[quadrilateral[1]][0],points[quadrilateral[1]][1]],
                [points[quadrilateral[2]][0],points[quadrilateral[2]][1]],
                [points[quadrilateral[3]][0],points[quadrilateral[3]][1]]
                ]

            p1 = PointMeshBackItem(quadrilateral[0], points[quadrilateral[0]][0], points[quadrilateral[0]][1])
            p2 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[1]][0], points[quadrilateral[1]][1])
            p3 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[2]][0], points[quadrilateral[2]][1])
            p4 = PointMeshBackItem(quadrilateral[1], points[quadrilateral[3]][0], points[quadrilateral[3]][1])
            self.group_mesh.addToGroup(p1)
            self.group_mesh.addToGroup(p2)
            self.group_mesh.addToGroup(p3)
            self.group_mesh.addToGroup(p4)
            
            item = QuadrilateraLMeshBackItem(
                                        color=color,
                                        coordinates = coordinates,
                                        p1=p1,
                                        p2=p2,
                                        p3=p3,
                                        p4=p4)


            self.group_mesh.addToGroup(item)

        self.scene_draw.update()
        
        

    def setColorItem(self, color):
        for item in self.group_mesh.childItems():
            if isinstance(item, QuadrilateraLMeshBackItem):
                item.setColor(color)
        self.scene_draw.update()
    

