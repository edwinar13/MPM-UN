from models.model_Repository import ModelRepository
from models.model_Mesh import ModelMeshBack
from utils.items_GraphicsDraw import TextFrameItem, PointBoundaryTxItem
from views.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelBoundary:

    def __init__(self, scene_draw:QGraphicsScene, model_repository:ModelRepository, 
                 model_mesh_back:ModelMeshBack, id) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository
        self. model_mesh_back = model_mesh_back
        self.id = id

        self.group_boundary  = QGraphicsItemGroup()
        self.scene_draw.addItem(self.group_boundary)
        self.createBoundary()
              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        """ funcion para obtener el id del contorno """
        return self.id

    def getName(self):
        """ funcion para obtener el nombre del contorno """
        name = self.getData()[self.id]["NAME"]
        return name

    def getNodes(self):
        """ return: lista con los nodos del contorno"""            
        nodes = self.getData()[self.id]["NODES"]
        return nodes   
    
    
    def getRestrictionX(self):
        """ funcion para obtener la restriccion en X del contorno """
        restrictionX = self.getData()[self.id]["Tx"]
        return restrictionX

    def getRestrictionY(self):
        """ funcion para obtener la restriccion en Y del contorno """
        restrictionY = self.getData()[self.id]["Ty"]
        return restrictionY

    def getData(self):
        """ return: lista con los datos de analisis de los puntos material, por ejemplo
         {
                "7d9d6673-d287-4df8-b9ef-f546de9a1f58": {
                    "NAME": "boundary_top",
                    "NODES": [
                        "NODE#43",
                        ...
                    ],
                    "Tx": false,
                    "Ty": true
                    }
            ...
        }"""
        boundaries = self.model_repository.readBoundaryDB()
        boundary = {
            self.id:  boundaries[self.id]
        }
        return boundary
         
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    def updateBoundary(self,id_boundary, name= None, nodes=None, 
                       restrictionX = None, restrictionY = None):
        """ funcion para actualizar los datos del contorno """
        if name != None:
            self.__name = name
            self.text_name.text= "B:{}".format(self.__name)

        self.model_repository.updateBoundaryDB(
            id_boundary=id_boundary,
            name=name,
            nodes=nodes,
            restrictionX=restrictionX,
            restrictionY=restrictionY
        )

    def deleteBoundary(self):
        """ funcion para eliminar el contorno """
        for item in self.group_boundary.childItems():
            self.group_boundary.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_boundary)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

    
    def createBoundary(self):
        """ funcion para crear el contorno """
        name = self.getName()
        Tx = self.getRestrictionX()
        Ty = self.getRestrictionY()
        nodes_boundary = self.getNodes()
        nodes_mesh = self.model_mesh_back.getNodes()
        marker_size = self.model_mesh_back.getSizeElement() * 0.4

        # Centroide de todos los nodos de la malla para determinar
        # la dirección "hacia afuera" de cada nodo de frontera
        all_coords = [n["COORDINATES"] for n in nodes_mesh.values()]
        cx = sum(c[0] for c in all_coords) / len(all_coords)
        cy = sum(c[1] for c in all_coords) / len(all_coords)

        coor_points = []
        #crear item escena
        for node_boundary in nodes_boundary:
            node_id = node_boundary
            point = nodes_mesh[node_boundary]["COORDINATES"]
            px, py = point[0], point[1]
            dx, dy = px - cx, py - cy
            if abs(dx) > abs(dy):
                dir_x, dir_y = (1.0 if dx > 0 else -1.0), 0.0
            else:
                dir_x, dir_y = 0.0, (1.0 if dy > 0 else -1.0)

            item = PointBoundaryTxItem(node_id=node_id,
                                      name=name,
                                      coordinatesX=px,
                                      coordinatesY=py,
                                      Tx=Tx,
                                      Ty=Ty,
                                      size=marker_size,
                                      dir_x=dir_x,
                                      dir_y=dir_y
                                      )
            coor_points.append(point)
            self.group_boundary.addToGroup(item)
        self.group_boundary.setZValue(15)

        sum_x = 0
        sum_y = 0
        for point in coor_points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(coor_points)
        average_y = sum_y / len(coor_points)

        self.text_name = TextFrameItem("B:{}".format(name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(20)
            
    def showHideBoundary(self, value):
        """ funcion para mostrar/ocultar el contorno """
        self.group_boundary.setVisible(value)
        
    def showHideLabel(self, value):   
        """ funcion para mostrar/ocultar el nombre del contorno """
        self.text_name.setVisible(value)   

    
    def stateViewBoundary(self, data):   
        """ funcion para mostrar/ocultar el contorno """
        for item in self.group_boundary.childItems():
            if isinstance(item, PointBoundaryTxItem):
                item.isSelectedBoundary = data["state_view"]
        self.scene_draw.update()
        
        
