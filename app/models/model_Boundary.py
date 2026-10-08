from models.model_Repository import ModelRepository
from models.model_Mesh import ModelMeshBack
from utils.items_GraphicsDraw import TextFrameItem, PointBoundaryTxItem
from views.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup

class ModelBoundary:

    def __init__(self, scene_draw:QGraphicsScene, model_repository:ModelRepository,
                 model_mesh_back:ModelMeshBack, id, on_visibility_changed=None) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository
        self. model_mesh_back = model_mesh_back
        self.id = id
        self.on_visibility_changed = on_visibility_changed
        self.items = {}  # id del nodo -> PointBoundaryTxItem

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

        # Bounding box de la malla para determinar la dirección
        # "hacia afuera" de cada nodo de frontera por proximidad al borde
        all_coords = [n["COORDINATES"] for n in nodes_mesh.values()]
        all_x = [c[0] for c in all_coords]
        all_y = [c[1] for c in all_coords]
        min_x, max_x = min(all_x), max(all_x)
        min_y, max_y = min(all_y), max(all_y)
        tol = 1e-6 * max(max_x - min_x, max_y - min_y, 1.0)

        coor_points = []
        #crear item escena
        for node_boundary in nodes_boundary:
            node_id = node_boundary
            point = nodes_mesh[node_boundary]["COORDINATES"]
            px, py = point[0], point[1]
            # Bordes del bounding box más cercanos (más de uno en las esquinas)
            dist = {"left": abs(px - min_x), "right": abs(px - max_x),
                    "bottom": abs(py - min_y), "top": abs(py - max_y)}
            min_dist = min(dist.values())
            edges = [e for e, d in dist.items() if d <= min_dist + tol]

            item = PointBoundaryTxItem(node_id=node_id,
                                      name=name,
                                      coordinatesX=px,
                                      coordinatesY=py,
                                      Tx=Tx,
                                      Ty=Ty,
                                      size=marker_size,
                                      edges=edges
                                      )
            coor_points.append(point)
            self.items[node_id] = item
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
        if self.on_visibility_changed:
            self.on_visibility_changed()

    def isVisible(self):
        return self.group_boundary.isVisible()

    def getItems(self) -> dict[str, PointBoundaryTxItem]:
        """ return: {id del nodo: símbolo dibujado} """
        return self.items

    def showHideLabel(self, value):
        """ funcion para mostrar/ocultar el nombre del contorno """
        self.text_name.setVisible(value)
        
        
