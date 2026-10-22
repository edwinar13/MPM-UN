from models.model_Repository import ModelRepository
from models.model_Property import ModelProperty
from models.model_Mesh import ModelMeshTriangle, ModelMeshQuadrilateral
from utils.items_GraphicsDraw import (TextMptem, TextFrameItem, PointMaterialItem, 
                                      PointForceItem, PointVelocityItem)
from views.view_GraphicsDraw import QGraphicsScene
from PySide6.QtWidgets import QGraphicsItemGroup, QGraphicsItem

class ModelMaterialPoint:

    def __init__(self, scene_draw:QGraphicsScene, model_repository:ModelRepository,
                  id, property:ModelProperty, mesh_base:ModelMeshTriangle|ModelMeshQuadrilateral
                  ) -> None:

        self.scene_draw = scene_draw
        self.model_repository = model_repository
        self.id = id
        self.property =property
        self.mesh_base = mesh_base

        self.group_material_point  = QGraphicsItemGroup()
        self.group_label = QGraphicsItemGroup()
        self.scene_draw.addItem(self.group_material_point)
        self.scene_draw.addItem(self.group_label)
        self.createMaterialPoint()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getId(self):
        """ funcion para obtener el id del conjunto de puntos material"""
        return self.id

    def getName(self):
        """ funcion para obtener el nombre del conjunto de puntos material"""
        name = self.getData()[self.id]["NAME"]
        return name
    


    def getPoints(self):        
        """ return: lista con los datos de analisis de los puntos material, por ejemplo
         {
            "POINT#1": { 
                "COORDINATES": [0.0, 0.0],
                "VOLUME": 1.0,
                "VELOCITY": {"X": 0.0,"Y": 0.0},
                "FORCE": {"X": 0.0,"Y": 0.0},
            }
            ...
        }
        
        """
        points = self.getData()[self.id]["POINTS"]
        return points       

    def getIdProperty(self):
        """ funcion para obtener el id de la propiedad del conjunto de puntos material"""
        id_property = self.getData()[self.id]["IDPROPIEDAD"]
        return id_property
    
    def getIdMeshBase(self):
        """ funcion para obtener el id de la malla base del conjunto de puntos material"""
        id_mesh_base = self.getData()[self.id]["IDMALLABASE"]
        return id_mesh_base

    def getProperty(self):
        """ funcion para obtener el modelop de la propiedad del conjunto de puntos material"""
        return self.property
    
    def getMeshBase(self):
        """ funcion para obtener el modelop de la malla base del conjunto de puntos material"""
        return self.mesh_base
    
    def getData(self):
        """ return: dict con los datos de los puntos material, por ejemplo
        {
            "c88150a3-9171-4560-ab52-fc346c87c02d":        {
                "NAME": "Punto Material 1",
                "COLOR": "#414ac8",
                "POINTS": {
                    "POINT#1": { 
                        "COORDINATES": {"X": 0.0,"Y": 0.0},
                        "VOLUME": 1.0,
                        "VELOCITY": {"X": 0.0,"Y": 0.0},
                        "FORCE": {"X": 0.0,"Y": 0.0},
                    ...
                },
                "IDPROPIEDAD": "d867a483-01a2-4710-9cf7-4b01a32e0aea",
                "IDMALLABASE": "cbd8f56c-533b-4e13-84ef-f2ae98e6364e"
            }
            ...
        }"""
        materials_points = self.model_repository.readMaterialPointDB()
        material_point = {
            self.id: materials_points[self.id]
        }                
        return material_point

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def updateMaterialPoint(self,id_MP, name= None,  points= None,
                            property = None, mesh_base = None):
        """ funcion para actualizar los datos de un conjunto de puntos material"""
        if name != None:
            self.__name = name
            self.text_name.text= "PM:{}".format(self.__name)

           
        self.model_repository.updateMaterialPointDB(
            id_MP=id_MP,
            name=name,
            points=points,
            id_property=property.getId(),
            id_mesh_base= mesh_base.getId()
        )        
        self.property = property

    
    def deleteMaterialPoint(self):
        """ funcion para eliminar un conjunto de puntos material"""
        self.scene_draw.removeItem(self.group_material_point)
        self.scene_draw.removeItem(self.group_label)
        self.scene_draw.removeItem(self.text_name)
        self.scene_draw.update()

                
    def createMaterialPoint(self):
        """ funcion para crear un conjunto de puntos material """
        name = self.getName()
        group_id = self.getId()
        color = self.property.getColor()
        points = self.getPoints()

        coor_points = []
        #crear item escena
        for point in points:
            coordinates = points[point]["COORDINATES"]    
            volume = points[point]["VOLUME"]
            forces = points[point]["FORCE"]
            velocities = points[point]["VELOCITY"]


            text =f'#{point.split("#")[1]}'
            text_item = TextMptem(text, coordinates[0], coordinates[1])
            self.group_label.addToGroup(text_item)
            

            item_force = PointForceItem(
                id_mp= point,
                id_group=group_id,
                coordinatesX=coordinates[0],
                coordinatesY=coordinates[1],
                Fx=forces["X"],
                Fy=forces["Y"],
            )
            
            item_velocity = PointVelocityItem(
                id_mp = point,
                id_group=group_id,
                coordinatesX=coordinates[0],
                coordinatesY=coordinates[1],
                Vx=velocities["X"],
                Vy=velocities["Y"]
            )
            item = PointMaterialItem(pm_id=point,
                                      group_id=group_id,
                                     color=color,
                                     coor=coordinates,
                                     volume=volume,
                                     force=item_force,
                                     velocity=item_velocity,)            
            coor_points.append(coordinates)
            item.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)
            item_force.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)
            item_velocity.setCacheMode(QGraphicsItem.CacheMode.DeviceCoordinateCache)
            self.group_material_point.addToGroup(item)
            self.group_material_point.addToGroup(item_force)
            self.group_material_point.addToGroup(item_velocity)
        
        self.group_material_point.setZValue(15)
        self.group_label.setZValue(50)
        self.group_label.setVisible(False)
        

        sum_x = 0
        sum_y = 0
        for point in coor_points:
            sum_x += point[0]
            sum_y += point[1]
        average_x = sum_x / len(points)
        average_y = sum_y / len(points)

        self.text_name = TextFrameItem("PM:{}".format(name), average_x,average_y)
        self.scene_draw.addItem(self.text_name)
        self.text_name.setVisible(False)
        self.text_name.setColor("#222333")
        self.text_name.setZValue(100)
        
   
    def showHideMaterialPoint(self, value):
        """ funcion para mostrar/ocultar un conjunto de puntos material"""
        self.group_material_point.setVisible(value)
        
    def showHideLabel(self, value):   
        """ funcion para mostrar/ocultar la etiqueta de un conjunto de puntos material"""
        self.group_label.setVisible(value)
        
    def showHideLabelTitle(self, value):   
        """ funcion para mostrar/ocultar la etiqueta de un conjunto de puntos material"""
        self.text_name.setVisible(value)   

    def ChangeSizePoint(self, value):   
        """ funcion para cambiar el tamaño de un conjunto de puntos material"""
        for item in self.group_material_point.childItems():
            if isinstance(item, PointMaterialItem):
                item.setRadius(value)
        self.scene_draw.update()
    
    def setColorItem(self, color):
        """ funcion para cambiar el color de un conjunto de puntos material"""
        for item in self.group_material_point.childItems():
            if isinstance(item, PointMaterialItem):
                item.setColor(color)
        self.scene_draw.update()


    def updateVectorQuantityPointsMaterial(self, id_MP, id_node, 
                                           vox:float, voy:float, fx:float, fy:float):
        """ funcion para actualizar la cantidad vectorial de un punto material"""
        self.model_repository.updateVectorQuantityPointsMaterialDB(
            id_MP=id_MP,
            id_node=id_node,
            vox=vox,
            voy=voy,
            fx=fx,
            fy=fy
        )
        
        for item in self.group_material_point.childItems():
            if isinstance(item, PointForceItem) or isinstance(item, PointVelocityItem):
                if item.id_mp == id_node and item.id_group == id_MP and isinstance(item, PointForceItem):
                    item.setForce(fx, fy)
                if item.id_mp == id_node and item.id_group == id_MP and isinstance(item, PointVelocityItem):
                    item.setVelocity(vox, voy)
            if isinstance(item, PointMaterialItem):
                item.isSelectedPointMaterial = False
                item.update()
        self.scene_draw.update()
        