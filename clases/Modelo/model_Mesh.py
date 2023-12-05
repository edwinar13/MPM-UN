from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextFrameItem, PointMeshBackItem, TriangleMeshItem, QuadrilateraLMeshItem, QuadrilateraLMeshBackItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

import time

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
        self.text_name.setZValue(100)
        

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
        self.group_mesh.setZValue(10)

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
        self.text_name.setZValue(100)

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
                size_dx, size_dy, size_element, color_style, points, quadrilaterals,
                points_boundary_top, points_boundary_bottom, points_boundary_left, points_boundary_right,
                nodes_boundary_top, nodes_boundary_bottom, nodes_boundary_left, nodes_boundary_right) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__size_dx = size_dx
        self.__size_dy = size_dy
        self.__size_element = size_element
        self.__color_style = color_style
        self.__points = points
        self.__quadrilaterals = quadrilaterals    

        self.points_boundary_top = points_boundary_top
        self.points_boundary_bottom = points_boundary_bottom
        self.points_boundary_left = points_boundary_left
        self.points_boundary_right = points_boundary_right

        self.nodes_boundary_top = nodes_boundary_top
        self.nodes_boundary_bottom = nodes_boundary_bottom
        self.nodes_boundary_left = nodes_boundary_left
        self.nodes_boundary_right = nodes_boundary_right         

        self.group_mesh  = QGraphicsItemGroup()
        self.group_mesh_point  = QGraphicsItemGroup()
        
        index = 0
        points_items = []
        for point in points:
            points_items.append(PointMeshBackItem(name=str(index),
                                                  coordinatesX= point[0], 
                                                  coordinatesY=point[1]))
            index += 1

        for quadrilateral in quadrilaterals:


            coordinates=[
                [points[quadrilateral[0]-1][0],points[quadrilateral[0]-1][1]],
                [points[quadrilateral[1]-1][0],points[quadrilateral[1]-1][1]],
                [points[quadrilateral[2]-1][0],points[quadrilateral[2]-1][1]],
                [points[quadrilateral[3]-1][0],points[quadrilateral[3]-1][1]]
                ]

            p1 = points_items[quadrilateral[0]-1]
            p2 = points_items[quadrilateral[1]-1]
            p3 = points_items[quadrilateral[2]-1]
            p4 = points_items[quadrilateral[3]-1]

            self.group_mesh_point.addToGroup(p1)
            self.group_mesh_point.addToGroup(p2)
            self.group_mesh_point.addToGroup(p3)
            self.group_mesh_point.addToGroup(p4)
            
            item = QuadrilateraLMeshBackItem(
                                        color_style=color_style,
                                        coordinates = coordinates,
                                        p1=p1,
                                        p2=p2,
                                        p3=p3,
                                        p4=p4)
            self.group_mesh.addToGroup(item)
        self.group_mesh.addToGroup(self.group_mesh_point)
        self.scene_draw.addItem(self.group_mesh)
        self.group_mesh_point.setVisible(False)
        self.group_mesh.setZValue(0)
    

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    
        

    
    def getSizeDx(self):
        return self.__size_dx
    
    def getSizeDy(self):
        return self.__size_dy

    def getSizeElement(self):
        return self.__size_element
    
    def getColorStyle(self):
        return self.__color_style

    def getPoints(self):
        return self.__points

    def getQuadrilaterals(self):
        return self.__quadrilaterals    


    def getBoundaryPoints(self):
        points_boundary_top = self.points_boundary_top
        points_boundary_bottom = self.points_boundary_bottom 
        points_boundary_left = self.points_boundary_left
        points_boundary_right = self.points_boundary_right
        
        return [points_boundary_top,points_boundary_bottom ,points_boundary_left ,points_boundary_right]
        

    def getBoundaryNodes(self):
        nodes_boundary_top = self.nodes_boundary_top
        nodes_boundary_bottom = self.nodes_boundary_bottom 
        nodes_boundary_left = self.nodes_boundary_left
        nodes_boundary_right = self.nodes_boundary_right
        
        


        return [nodes_boundary_top,nodes_boundary_bottom ,nodes_boundary_left ,nodes_boundary_right]
        
    
    def getData(self):
        """return: size_dx, size_dy, size_element, color, points, getBoundaryPoints, getBoundaryNodes]"""
        return[self.__size_dx, self.__size_dy, self.__size_element, self.__color_style, self.__points, self.getBoundaryPoints(), self.getBoundaryNodes()]
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)

    def showMeshBackPoint(self, value):
        self.group_mesh_point.setVisible(value)
    
    def updateMesh(self,size_dx=None, size_dy= None, size_element=None, color= None, points= None, quadrilaterals = None, 
                   points_boundary_top= None, points_boundary_bottom= None, points_boundary_left= None, points_boundary_right= None,
                   nodes_boundary_top= None, nodes_boundary_bottom= None, nodes_boundary_left= None, nodes_boundary_right= None
                   ):
        
        if size_dx != None:
            self.__size_dx = size_dx
        if size_dy != None:
            self.__size_dy = size_dy
        if size_element != None:
            self.__size_element = size_element

        if points != None:
            self.__points = points
        if quadrilaterals != None:
            self.__quadrilaterals = quadrilaterals
            self.__points = points

        if points_boundary_top != None:
            self.points_boundary_top = points_boundary_top
        if points_boundary_bottom != None:
            self.points_boundary_bottom = points_boundary_bottom
        if points_boundary_left != None:
            self.points_boundary_left = points_boundary_left
        if points_boundary_right != None:
            self.points_boundary_right = points_boundary_right

        if nodes_boundary_top != None:
            self.nodes_boundary_top = nodes_boundary_top
        if nodes_boundary_bottom != None:
            self.nodes_boundary_bottom = nodes_boundary_bottom
        if nodes_boundary_left != None:
            self.nodes_boundary_left = nodes_boundary_left
        if nodes_boundary_right != None:
            self.nodes_boundary_right = nodes_boundary_right


        

        self.model_project_current_repository.updateMeshBackDB(
            size_dx=size_dx,
            size_dy=size_dy,
            size_element = size_element,
            color=color,
            points=points,
            quadrilaterals=quadrilaterals,
            points_boundary_top = points_boundary_top,
            points_boundary_bottom = points_boundary_bottom,
            points_boundary_left = points_boundary_left,
            points_boundary_right = points_boundary_right,
            nodes_boundary_top = nodes_boundary_top,
            nodes_boundary_bottom = nodes_boundary_bottom,
            nodes_boundary_left = nodes_boundary_left,
            nodes_boundary_right = nodes_boundary_right
        )
        
        self.setPointsQuadrilateralsItem()
        

    def setPointsQuadrilateralsItem(self):

        for item in self.group_mesh.childItems():
            self.scene_draw.removeItem(item)      
        self.group_mesh.childItems().clear()

        color_style = self.__color_style
        points = self.__points
        quadrilaterals = self.__quadrilaterals

        index = 0
        points_items = []
        for point in points:
            points_items.append(PointMeshBackItem(index, point[0], point[1]))
            index =+ 1

        for quadrilateral in quadrilaterals:

            coordinates=[
                [points[quadrilateral[0]-1][0],points[quadrilateral[0]-1][1]],
                [points[quadrilateral[1]-1][0],points[quadrilateral[1]-1][1]],
                [points[quadrilateral[2]-1][0],points[quadrilateral[2]-1][1]],
                [points[quadrilateral[3]-1][0],points[quadrilateral[3]-1][1]]
                ]

            p1 = points_items[quadrilateral[0]-1]
            p2 = points_items[quadrilateral[1]-1]
            p3 = points_items[quadrilateral[2]-1]
            p4 = points_items[quadrilateral[3]-1]

            self.group_mesh_point.addToGroup(p1)
            self.group_mesh_point.addToGroup(p2)
            self.group_mesh_point.addToGroup(p3)
            self.group_mesh_point.addToGroup(p4)
            
            item = QuadrilateraLMeshBackItem(
                                        color_style=color_style,
                                        coordinates = coordinates,
                                        p1=p1,
                                        p2=p2,
                                        p3=p3,
                                        p4=p4)


            self.group_mesh.addToGroup(item)
        
        self.group_mesh.addToGroup(self.group_mesh_point)
        self.group_mesh_point.setVisible(False)  
        
        self.scene_draw.update()
           
    def changeTheme(self,index_style):

        if index_style == 0:
            self.setColorItem(color=0)
        elif index_style == 1:
            self.setColorItem(color=1)


    def setColorItem(self, color):
        for item in self.group_mesh.childItems():
            if isinstance(item, QuadrilateraLMeshBackItem):
                item.setColor(color)
        self.scene_draw.update()