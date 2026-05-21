from models.model_Repository import ModelRepository
from utils.items_GraphicsDraw import (TextFrameItem, NodeMeshBackItem,
                                      TriangleMeshItem, QuadrilateraLMeshItem,
                                    ElementMeshBackItem, TextMeshBackItem)
from views.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelMeshTriangle:

    def __init__(self, scene_draw:QGraphicsScene,
                 model_repository:ModelRepository,
                 id ) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository
        self.id = id
        
        self.group_mesh  = QGraphicsItemGroup()
        self.scene_draw.addItem(self.group_mesh)
        
        self.createMeshTriangle()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    def getType(self):
        """ funcion para obtener el tipo de malla"""
        return "TRIANGULAR"
    
    def getId(self):
        """ funcion para obtener el id de la malla"""
        return self.id

    def getName(self):
        """ funcion para obtener el nombre de la malla"""
        name = self.getData()[self.id]["NAME"]
        return name
    
    def getColor(self):
        """ funcion para obtener el color de la malla"""
        color = self.getData()[self.id]["COLOR"]
        return color

    def getNodes(self):
        """ funcion para obtener los nodos de la malla"""
        nodes = self.getData()[self.id]["NODES"]
        return nodes

    def getElements(self):
        """ funcion para obtener los elementos de la malla"""
        elements = self.getData()[self.id]["ELEMENTS"]
        return elements
    
    def getData(self):
        """ return: dict con los datos de la malla, por ejemplo
        {
            "c88150a3-9171-4560-ab52-fc346c87c02d":        {
                "NAME": "Malla triangular",
                "COLOR": "#414ac8",
                "NODES": {
                    "NODE#1": { "COORDINATES": [2.0, 1.0] },
                    ...
                },
                "ELEMENTS": {
                    "ELEMENT#1": ["NODE#0", "NODE#1", "NODE#4"],
                    ...
                }
            }
        }
        """
        
        meshs_triangular = self.model_repository.readMeshTriangularDB()
        mesh_triangular = {
            self.id: meshs_triangular[self.id]
        }
        
        return mesh_triangular
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    

    def updateMesh(self,id_mesh, name= None, color= None, nodes= None, elements = None):
        """ funcion para actualizar los datos de la malla"""
        if name != None:
            self.__name = name
            self.text_name.text= "MT:{}".format(self.__name)
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)

        self.model_repository.updateMeshTriangularDB(
            id_Mesh =id_mesh,
            name=name,
            color=color,
            nodes=nodes,
            elements=elements
        )
        
    def deleteMesh(self):
        """ funcion para eliminar la malla de la escena y
        eliminar los grupos de items de la escena"""
        self.scene_draw.removeItem(self.group_mesh)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

    def createMeshTriangle(self):
        """ funcion para crear una malla triangular en la escena"""        
        name = self.getName()
        color = self.getColor()
        nodes = self.getNodes()
        elements = self.getElements()  

        #crear item escena
        for element in elements:
            node_a = elements[element][0]
            node_b = elements[element][1]
            node_c = elements[element][2]
            
            coordinates=[
                [nodes[node_a]['COORDINATES'][0],nodes[node_a]['COORDINATES'][1]],
                [nodes[node_b]['COORDINATES'][0],nodes[node_b]['COORDINATES'][1]],
                [nodes[node_c]['COORDINATES'][0],nodes[node_c]['COORDINATES'][1]]
                ]
            item = TriangleMeshItem(id=element,
                                      name=name,
                                     color=color,
                                     coordinates = coordinates)            
            self.group_mesh.addToGroup(item)
        self.group_mesh.setZValue(5)

        # Crear etiqueta de la malla
        sum_x = 0
        sum_y = 0
        for node in nodes:
            sum_x += nodes[node]['COORDINATES'][0]
            sum_y += nodes[node]['COORDINATES'][1]
        average_x = sum_x / len(nodes)
        average_y = sum_y / len(nodes)

        self.text_name = TextFrameItem("MT:{}".format(name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(100)
    
    def showHideMesh(self, value):
        """ funcion para mostrar u ocultar la malla"""
        self.group_mesh.setVisible(value)

    def showHideLabel(self, value):
        """ funcion para mostrar u ocultar la etiqueta de la malla"""
        self.text_name.setVisible(value)

    def setColorItem(self, color):
        """ funcion para cambiar el color de la malla"""
        for item in self.group_mesh.childItems():
            if isinstance(item, TriangleMeshItem):
                item.setColor(color)
        self.scene_draw.update()
    


class ModelMeshQuadrilateral:

    def __init__(self, scene_draw:QGraphicsScene,
                 model_repository:ModelRepository,
                 id) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository        
        self.id = id        
        
        self.group_mesh  = QGraphicsItemGroup()
        self.scene_draw.addItem(self.group_mesh)
                
        self.createMeshQuadrilateral()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    
    def getType(self):
        """ funcion para obtener el tipo de malla"""
        return "QUADRILATERAL"
    
    def getId(self):
        """ funcion para obtener el id de la malla"""
        return self.id

    def getName(self):
        """ funcion para obtener el nombre de la malla"""
        name = self.getData()[self.id]["NAME"]
        return name
    
    def getColor(self):
        """ funcion para obtener el color de la malla"""
        color = self.getData()[self.id]["COLOR"]
        return color

    def getNodes(self):
        """ funcion para obtener los nodos de la malla"""
        nodes = self.getData()[self.id]["NODES"]
        return nodes

    def getElements(self):
        """ funcion para obtener los elementos de la malla"""
        elements = self.getData()[self.id]["ELEMENTS"]
        return elements
    
    def getData(self):
        
        """ return: dict con los datos de la malla, por ejemplo
        {
            "c88150a3-9171-4560-ab52-fc346c87c02d":        {
                "NAME": "Malla cuadrilatera",
                "COLOR": "#414ac8",
                "NODES": {
                    "NODE#1": { "COORDINATES": [2.0, 1.0] },
                    ...
                },
                "ELEMENTS": {
                    "ELEMENT#1": ["NODE#0", "NODE#1", "NODE#4", "NODE#3"],
                    ...
                }
            }
        }
        """        

        meshs_quadrilateral = self.model_repository.readMeshQuadrilateralDB()
        mesh_quadrilateral = {
            self.id: meshs_quadrilateral[self.id]
        }
        return mesh_quadrilateral
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def updateMesh(self,id_mesh, name= None, color= None, nodes= None, elements = None):
        """ funcion para actualizar los datos de la malla"""
        if name != None:
            self.__name = name
            self.text_name.text= "MQ:{}".format(self.__name)
            
        if color != None:
            self.__color = color
            self.setColorItem(self.__color)           

        self.model_repository.updateMeshQuadrilateralDB(
            id_Mesh =id_mesh,
            name=name,
            color=color,            
            nodes=nodes,
            elements=elements
        )
        
        
    def deleteMesh(self):
        """ funcion para eliminar la malla de la escena y
        eliminar los grupos de items de la escena"""
        self.scene_draw.removeItem(self.group_mesh)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

    def createMeshQuadrilateral(self):
        """ funcion para crear una malla cuadrilateral en la escena"""
        name = self.getName()
        color = self.getColor()
        nodes = self.getNodes()
        elements = self.getElements()

        #crear item escena
        for element in elements:
            node_a = elements[element][0]
            node_b = elements[element][1]
            node_c = elements[element][2]
            node_d = elements[element][3]   
            
            coordinates=[
                [nodes[node_a]['COORDINATES'][0],nodes[node_a]['COORDINATES'][1]],
                [nodes[node_b]['COORDINATES'][0],nodes[node_b]['COORDINATES'][1]],
                [nodes[node_c]['COORDINATES'][0],nodes[node_c]['COORDINATES'][1]],
                [nodes[node_d]['COORDINATES'][0],nodes[node_d]['COORDINATES'][1]]
            ]
            
            item = QuadrilateraLMeshItem(id=element,
                                      name=name,
                                     color=color,
                                     coordinates = coordinates)
            self.group_mesh.addToGroup(item)
        
        self.group_mesh.setZValue(10)
        
        # Crear etiqueta de la malla
        sum_x = 0
        sum_y = 0
        for node in nodes:
            sum_x += nodes[node]['COORDINATES'][0]
            sum_y += nodes[node]['COORDINATES'][1]
        average_x = sum_x / len(nodes)
        average_y = sum_y / len(nodes)
        
        self.text_name = TextFrameItem("MQ:{}".format(name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(100)
        self.scene_draw.update()
    
    def showHideMesh(self, value):
        """ funcion para mostrar u ocultar la malla"""
        self.group_mesh.setVisible(value)

    def showHideLabel(self, value):
        """ funcion para mostrar u ocultar la etiqueta de la malla"""
        self.text_name.setVisible(value)

    def setColorItem(self, color):
        """ funcion para cambiar el color de la malla"""
        for item in self.group_mesh.childItems():
            if isinstance(item, QuadrilateraLMeshItem):
                item.setColor(color)
        self.scene_draw.update()

class ModelMeshBack:

    def __init__(self, scene_draw:QGraphicsScene,model_repository:ModelRepository) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository              

        self.group_MeshBack  = QGraphicsItemGroup()
        self.group_mesh_element  = QGraphicsItemGroup()
        self.group_mesh_point  = QGraphicsItemGroup()
        self.group_mesh_label  = QGraphicsItemGroup()
        self.scene_draw.addItem(self.group_MeshBack)

        self.createMeshBack()
        
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getSizeDx(self):
        """ funcion para obtener el tamaño de la malla en x"""
        size_dx = self.getData()["SIZEDX"]
        return size_dx
    
    def getSizeDy(self):
        """ funcion para obtener el tamaño de la malla en y"""
        size_dy = self.getData()["SIZEDY"]
        return size_dy

    def getSizeElement(self):
        """ funcion para obtener el tamaño de los elementos de la malla"""
        size_element = self.getData()["SIZEELEMENT"]
        return size_element    

    def getNodes(self):
        """ funcion para obtener los nodos de la malla"""
        nodes = self.getData()["NODES"]
        return nodes

    def getElements(self):
        """ funcion para obtener los elementos de la malla"""
        elements = self.getData()["ELEMENTS"]
        return elements    

    def getBoundaryNodes(self):
        """ funcion para obtener los nodos de la malla en la frontera
            return: list con los nodos de la frontera en cada lado
            [
                nodes_boundary_top, 
                nodes_boundary_bottom,
                nodes_boundary_left ,
                nodes_boundary_right
            ]
        """
        nodes_boundary_top = self.getData()["NODESBOUNDARYTOP"]
        nodes_boundary_bottom = self.getData()["NODESBOUNDARYBOTTOM"]
        nodes_boundary_left = self.getData()["NODESBOUNDARYLEFT"]
        nodes_boundary_right = self.getData()["NODESBOUNDARYRIGHT"]        
        return [nodes_boundary_top,nodes_boundary_bottom ,nodes_boundary_left ,nodes_boundary_right]
    
    def getData(self):
        """return: dict con los datos de la malla de fondo, por ejemplo
            {
                'SIZEDX': 2.0,
                'SIZEDY': 2.0,
                'SIZEELEMENT': 1.0,
                'NODES': {
                        'NODO#1': {'COORDINATES': [0.0, 0.0]},
                        ...
                    },
                'ELEMENTS': {
                        'ELEMENT#1': ['NODO#1', 'NODO#2', 'NODO#5', 'NODO#4'],
                        ...
                    },
                'NODESBOUNDARYTOP': ['NODO#7', 'NODO#8', 'NODO#9'],
                'NODESBOUNDARYBOTTOM': ['NODO#1', 'NODO#2', 'NODO#3'],
                'NODESBOUNDARYLEFT': ['NODO#1', 'NODO#4', 'NODO#7'],
                'NODESBOUNDARYRIGHT': ['NODO#3', 'NODO#6', 'NODO#9']
            }     

        
        """
        mesh_back = self.model_repository.readMeshBackDB() 
        return mesh_back
        
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    def deleteMesh(self):
        """ funcion para eliminar la malla de fondo de la escena y 
        eliminar los grupos de items de la escena"""
        
        # Borrar los items del grupo label        
        for item in self.group_mesh_label.childItems():
            self.scene_draw.removeItem(item)
        self.group_mesh_label.childItems().clear()
        
        # Borrar los items del grupo point
        for item in self.group_mesh_point.childItems():
            self.scene_draw.removeItem(item)
        self.group_mesh_point.childItems().clear()       
        
        # Borrar los items del grupo element
        for item in self.group_mesh_element.childItems():
            self.scene_draw.removeItem(item)      
        self.group_mesh_element.childItems().clear()

    def createMeshBack(self):    
        """ funcion para crear la malla de fondo por grupos de items en la escena"""    
        
        nodes = self.getNodes()
        node_items = {}

        for node in nodes:      
            
            coordinates = nodes[node]['COORDINATES']       
            # por ejemplo de NODE#1 dejar solo 1 
            text = f'  {node.split("#")[1]}'
            text_name = TextMeshBackItem( 
                                 text=text, 
                                 coordinatesX= coordinates[0],
                                 coordinatesY= coordinates[1])  
     
            #text_name.setZValue(100)     
            self.group_mesh_label.addToGroup(text_name)
            
            node_item = NodeMeshBackItem(
                                    id=node,
                                    coordinatesX= coordinates[0],
                                    coordinatesY= coordinates[1]
                                    )
            self.group_mesh_point.addToGroup(node_item)
            node_items[node] = node_item
                            
        elements = self.getElements()
        for element in elements:
            node_a = elements[element][0]
            node_b = elements[element][1]
            node_c = elements[element][2]
            node_d = elements[element][3]            
            
            
            # agergar la etiqueta del elemento
            center = [
                (nodes[node_a]['COORDINATES'][0] + nodes[node_b]['COORDINATES'][0] + nodes[node_c]['COORDINATES'][0] + nodes[node_d]['COORDINATES'][0]) / 4,
                (nodes[node_a]['COORDINATES'][1] + nodes[node_b]['COORDINATES'][1] + nodes[node_c]['COORDINATES'][1] + nodes[node_d]['COORDINATES'][1]) / 4
            ]
            
            text = f'{element.split("#")[1]}'
            text_name = TextMeshBackItem(
                                    text=text,
                                    coordinatesX=center[0],
                                    coordinatesY=center[1]
                                    )
            self.group_mesh_label.addToGroup(text_name)
            
            

            item = ElementMeshBackItem(  
                                        node1=node_items[node_a],
                                        node2=node_items[node_b],
                                        node3=node_items[node_c],
                                        node4=node_items[node_d]
                                        )
            self.group_mesh_element.addToGroup(item)
            
        self.group_MeshBack.addToGroup(self.group_mesh_label)
        self.group_MeshBack.addToGroup(self.group_mesh_point)
        self.group_MeshBack.addToGroup(self.group_mesh_element)
        
        self.group_mesh_point.setVisible(False)
        self.group_mesh_label.setVisible(False)
        self.group_mesh_element.setVisible(True)
        
        #self.group_MeshBack.setZValue(0)
        self.scene_draw.update()

    def updateMesh(self,size_dx, size_dy, size_element, nodes, elements ,
                   nodes_boundary_top, nodes_boundary_bottom,
                   nodes_boundary_left, nodes_boundary_right):


        self.model_repository.updateMeshBackDB(
            size_dx=size_dx, size_dy=size_dy, size_element = size_element,
            nodes=nodes, elements=elements,
            nodes_boundary_top = nodes_boundary_top,
            nodes_boundary_bottom = nodes_boundary_bottom,
            nodes_boundary_left = nodes_boundary_left,
            nodes_boundary_right = nodes_boundary_right
        )

        self.deleteMesh()
        self.createMeshBack()


    def showHideMesh(self, value):
        """ funcion para mostrar u ocultar la malla de fondo"""
        self.group_MeshBack.setVisible(value)

    def showMeshBackPoint(self, value):
        """ funcion para mostrar u ocultar los puntos y etiquetas de la malla de fondo"""
        self.group_mesh_point.setVisible(value)
        self.group_mesh_label.setVisible(value)






