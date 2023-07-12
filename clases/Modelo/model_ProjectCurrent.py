
from PySide6.QtCore import (QFile, QTime,Signal, QObject, QPointF, Qt, QRectF, QLineF,)
from PySide6.QtWidgets import (QUndoView, QFileDialog)
from PySide6.QtGui import (QUndoStack)

from clases.Modelo.model_ItemPoint import ModelItemPoint
from clases.Modelo.model_ItemLine import ModelItemLine
from clases.Modelo.model_Mesh import ModelMeshTriangle, ModelMeshQuadrilateral, ModelMeshBack
from clases.Modelo.model_MaterialPoint import ModelMaterialPoint
from clases.Modelo.model_Property import ModelProperty
from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.Vista.view_GraphicsDraw import ViewGraphicsSceneDraw, ViewGraphicsViewDraw
from clases.items_GraphicsDraw import TextItem, PointItem, LineItem
from clases.command_GraphicsDraw import AddPointCommand, AddLineCommand, MoveCommand, RotateCommand, RemoveLineCommand,RemovePointCommand, UpdateCommand
import uuid
import math
import ezdxf


class ModelProjectCurrent(QObject):

    signal_select_line_mesh= Signal(int) 
    signal_size_mesh= Signal(float) 
    signal_msn_label_view = Signal(list)

    def __init__(self,scene:ViewGraphicsSceneDraw,view_draw_1:ViewGraphicsViewDraw, view_draw_2:ViewGraphicsViewDraw, path_doc) -> None:
        super().__init__() 
        self.__scene = scene
        self.view_draw_1 = view_draw_1
        self.view_draw_2 = view_draw_2

        self.__path_doc = path_doc
        self.__name_doc = path_doc.split('/')[-1]
        self.__name = None
        self.__location = None
        self.__author = None 
        self.__description = None
        self.__gravity = None

        self.model_project_current_repository = ModelProjectCurrentRepository(self.__path_doc)

        self.undo_stack = QUndoStack()
        self.createUndoView()



        self.items_points_models={}
        self.items_lines_models={}
        self.items_models={}
        self.meshs_models={}
        self.meshs_quadrilaterals_models={}
        self.material_point_models={}
        self.mesh_black_model= None
        self.properties_models={}


        self.__selected_objects = []
        self.deselect_draw_geometry = None
        self.mode_label_draw=False




        self.__initEvent()

        self.__scene.clear()
        self.__initData()
        self.__initItem()
        self.__initMesh()
        self.__initProperties()
        self.__initMaterialPoint()
        self.__scene.drawElementTemp()
        self.__scene.update()
        

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    
    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.__scene.signal_mesh_size.connect(self.commandMeshSize)      
        self.__scene.signal_mesh_select.connect(self.commandMeshSelectLine)      


                # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE MESH :::::::::::::::::   
        self.__scene.signal_point_point.connect(self.commandPoint)
        self.__scene.signal_point_line.connect(self.commandLine)
        self.__scene.signal_point_move.connect(self.commandMove)
        self.__scene.signal_point_copy.connect(self.commandCopy)
        self.__scene.signal_point_rotate.connect(self.commandRotate)
        self.__scene.signal_point_erase.connect(self.commandErase)
        self.__scene.signal_point_intersection.connect(self.commandIntersection)
        self.__scene.signal_point_rule.connect(self.commandRule)

        
    def __initData(self):
        # Informacion
        data = self.model_project_current_repository.readInformationDB()
        self.__name = data["NOMBREPROYECTO"]
        self.__location = data["LOCALIZACION"]
        self.__author = data["AUTOR"] 
        self.__description = data["DESCRIPCION"]
        # Configuracion
        data = self.model_project_current_repository.readConfigDB()
        self.__gravity = data["GRAVEDAD"]
    
    def __initItem(self):
        items_points = self.model_project_current_repository.readItemPointDrawDB()
        for id_items_point in items_points: 
            name = items_points[id_items_point]["NAME"]
            coordinates = items_points[id_items_point]["COORDINATES"]
            lines = items_points[id_items_point]["LINES"]
            self.addItemPointToCurrentProject(id=id_items_point,
                                              name=name,
                                              coordinates=coordinates,
                                              lines=lines)

        
        items_lines = self.model_project_current_repository.readItemLineDrawDB()

        for id_items_line in items_lines: 
            name = items_lines[id_items_line]["NAME"]
            id_start_point = items_lines[id_items_line]["STARTPOINT"]
            id_end_point = items_lines[id_items_line]["ENDPOINT"]
            self.addItemLineToCurrentProject(id=id_items_line,
                                              name=name,
                                              start_point=self.items_points_models[id_start_point],
                                              end_point= self.items_points_models[id_end_point])


    def __initMesh(self):

        mesh_back = self.model_project_current_repository.readMeshBackDB()

        
        size_dx = mesh_back["SIZEDX"]
        size_dy = mesh_back["SIZEDY"]
        size_element = mesh_back["SIZEELEMENT"]
        color = mesh_back["COLOR"]
        points = mesh_back["POINTS"]
        quadrilaterals = mesh_back["QUADRILATERALS"]




        model_mesh_back = ModelMeshBack(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      size_dx=size_dx,
                                                      size_dy=size_dy,
                                                      size_element=size_element,
                                                      color=color,
                                                      points=points,
                                                      quadrilaterals=quadrilaterals)
        
        self.mesh_black_model=model_mesh_back        




        meshs = self.model_project_current_repository.readMeshTriangularDB()
        for id_mesh_triangular in meshs: 
            name = meshs[id_mesh_triangular]["NAME"]
            color = meshs[id_mesh_triangular]["COLOR"]
            points = meshs[id_mesh_triangular]["POINTS"]
            triangles = meshs[id_mesh_triangular]["TRIANGLES"]
            self.addMeshTrianglesToCurrentProject(
                id=id_mesh_triangular,
                name=name,
                color=color,
                points=points,
                triangles=triangles)           
        
        meshs = self.model_project_current_repository.readMeshQuadrilateralDB()

        for id_mesh_quadrilateral in meshs: 
            name = meshs[id_mesh_quadrilateral]["NAME"]
            color = meshs[id_mesh_quadrilateral]["COLOR"]
            points = meshs[id_mesh_quadrilateral]["POINTS"]
            quadrilaterals = meshs[id_mesh_quadrilateral]["QUADRILATERALS"]
            self.addMeshQuadrilateralToCurrentProject(
                id=id_mesh_quadrilateral,
                name=name,
                color=color,
                points=points,
                quadrilaterals=quadrilaterals) 

    def __initMaterialPoint(self):
        materials_points = self.model_project_current_repository.readMaterialPointDB()
        for id_material_point in materials_points:
            name = materials_points[id_material_point]["NAME"]
            color = materials_points[id_material_point]["COLOR"]
            points = materials_points[id_material_point]["POINTS"]
            id_property = materials_points[id_material_point]["IDPROPIEDAD"]
            self.addMaterialPointToCurrentProject(
                id=id_material_point,
                name=name,
                color=color,
                points=points,
                id_property=id_property)
            
    def __initProperties(self):
        properties = self.model_project_current_repository.readPropertiesDB()
        for id_property in properties:
            name = properties[id_property]["NAME"]
            modulus_elasticity = properties[id_property]["MODULOELASTICIDAD"]
            poisson_ratio = properties[id_property]["RELACIONPOISSON"]
            cohesion = properties[id_property]["COHESION"]
            friction_angle = properties[id_property]["ANGULOFRICCION"]
            angle_dilatancy = properties[id_property]["ANGULODILATANCIA"]


            self.addPropertyToCurrentProject(
                id=id_property,
                name=name,
                modulus_elasticity=modulus_elasticity,
                poisson_ratio=poisson_ratio,
                cohesion=cohesion,
                friction_angle=friction_angle,
                angle_dilatancy=angle_dilatancy)


    def createUndoView(self):

        undoView = QUndoView(self.undo_stack)
        undoView.setWindowTitle("Command List")
        undoView.show()
        undoView.setAttribute(Qt.WA_QuitOnClose, False)

    def undo(self):
        self.undo_stack.undo()

    def redo(self):
        self.undo_stack.redo() 
           
    def getUndoStack(self):
        return self.undo_stack


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################  

    def getPathDoc(self):
        return self.__path_doc
    
    def getNameDoc(self):
        return self.__name_doc

    def getName(self):
        return self.__name
    
    def getLocation(self):
        return self.__location

    def getAuthor(self):
        return self.__author

    def getDescription(self):
        return self.__description
    
    def getGravity(self):
        return self.__gravity
    
    def getDataInfo(self):
        return[self.__name, self.__location, self.__author, self.__description]
    
    def getDataConfig(self):
        return[ self.__gravity]
       

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################

    # ::::::::::::::::::::                DATA               ::::::::::::::::::::

    def updateInformation(self, name_project=None, location=None,
                                 author=None,  description=None):
        

        self.model_project_current_repository.updateInformationDB()


        if name_project != None:     
            self.model_project_current_repository.updateInformationDB(name_project=name_project)
            self.__name = name_project
        if location != None:               
            self.model_project_current_repository.updateInformationDB(location=location)
            self.__location = location
        if author != None:               
            self.model_project_current_repository.updateInformationDB(author=author)
            self.__author = author
        if description != None:               
            self.model_project_current_repository.updateInformationDB(description=description)
            self.__description = description

    def updateConfig(self, gravity= None):
        if gravity != None:               
            self.model_project_current_repository.updateConfigDB(gravity=gravity)
            self.__gravity = gravity


    # ::::::::::::::::::::                ITEMS               ::::::::::::::::::::

    def addItemPointToCurrentProject(self,id, name, coordinates, lines):    
        model_point = ModelItemPoint(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      coordinates=coordinates,
                                                      lines=lines
                                                      )
        
        self.items_points_models[id]=model_point      

    def createItemPoint(self, id_point, name, coordinates ):
            
        lines = []
        self.model_project_current_repository.createItemPointDrawDB(
            id_point = id_point,
            name = name,  
            coordinates = coordinates,
                lines = lines)
        self.addItemPointToCurrentProject(
                id=id_point,
                name=name,
                coordinates=coordinates,
                lines = lines)
        return id_point
    
    def deleteItemPoint(self, id):
        self.model_project_current_repository.deleteItemPointDrawDB(id)  
        removed_model_item_point = self.items_points_models.pop(id, None)
        if removed_model_item_point is not None:
            removed_model_item_point.deletePoint()
            del removed_model_item_point
    
    def updateItemPoint(self,  id_point, name = None, coordinates = None, lines = None):

        model_item_point = self.items_points_models[id_point]
        model_item_point.updatePoint(id_point=id_point,
                                      name = name,
                                        coordinates = coordinates, 
                                        lines = lines)



    def addItemLineToCurrentProject(self,id, name, start_point, end_point):   
        
        model_line = ModelItemLine(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      start_point=start_point,
                                                      end_point=end_point)
        
        self.items_lines_models[id]=model_line       

    def createItemLine(self, id_line, name, id_start_point, id_end_point):

        

       
        self.model_project_current_repository.createItemLineDrawDB(
                id_line= id_line,
                name = name,  
                id_start_point = id_start_point,
                id_end_point = id_end_point)
        model_point_start=self.items_points_models[id_start_point]
        model_point_end =self.items_points_models[id_end_point]
        self.addItemLineToCurrentProject(
                id=id_line,
                name=name,
                start_point = model_point_start,
                end_point = model_point_end)

        model_point_start.addLineAnchored(id_line) 
        model_point_end.addLineAnchored(id_line)        
        return id_line
    
    def deleteItemLine(self, id):
        self.model_project_current_repository.deleteItemLineDrawDB(id)  
        removed_model_item_line = self.items_lines_models.pop(id)
        removed_model_item_line.deleteLine()


        model_start_point = removed_model_item_line.getStartPoint()
        model_end_point = removed_model_item_line.getEndPoint()

        model_start_point.deleteLineAnchored(removed_model_item_line.getId())
        model_end_point.deleteLineAnchored(removed_model_item_line.getId())


        del removed_model_item_line

    def updateItemLine(self,  id_line, name = None, id_start_point = None, id_end_point = None):

        model_item_line = self.items_lines_models[id_line]

        model_start_point = model_item_line.getStartPoint()
        model_end_point = model_item_line.getEndPoint()


        model_start_point.deleteLineAnchored(model_item_line.getId())
        model_end_point.deleteLineAnchored(model_item_line.getId())

        model_point_start=self.items_points_models[id_start_point]
        model_point_end =self.items_points_models[id_end_point]

        model_item_line.updateLine(id_line=id_line,
                                        start_point = model_point_start, 
                                        end_point = model_point_end)
        
        model_point_start.addLineAnchored(id_line) 
        model_point_end.addLineAnchored(id_line)  

    def getModelsPoints(self):
        return self.items_points_models
    
    def getModelsLines(self):
        return self.items_lines_models
    


    # ::::::::::::::::::::                MALLAS               ::::::::::::::::::::

    def getMeshBack(self):
        return self.mesh_black_model
         
    def createMeshTriangular(self, name, color, points, triangles):
        id = str(uuid.uuid4())
        self.model_project_current_repository.createMeshTriangularDB(
            id_Mesh = id,
            name = name, 
            color = color, 
            points = points,
            triangles = triangles)
        self.addMeshTrianglesToCurrentProject(
                id=id,
                name=name,
                color=color,
                points=points,
                triangles=triangles)
        return id
   
    def createMeshQuadrilateral(self, name, color, points, quadrilaterals):
        id = str(uuid.uuid4())
        self.model_project_current_repository.createMeshQuadrilateralDB(
            id_Mesh = id,
            name = name, 
            color = color, 
            points = points,
            quadrilaterals = quadrilaterals)
        
        self.addMeshQuadrilateralToCurrentProject(
                id=id,
                name=name,
                color=color,
                points=points,
                quadrilaterals=quadrilaterals)
        return id
    
    def addMeshTrianglesToCurrentProject(self,id, name, color, points, triangles):    
        model_mesh = ModelMeshTriangle(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      color=color,
                                                      points=points,
                                                      triangles=triangles)
        
        self.meshs_models[id]=model_mesh        

    def addMeshQuadrilateralToCurrentProject(self,id, name, color, points, quadrilaterals):    
        model_mesh_quadrilaterals = ModelMeshQuadrilateral(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      color=color,
                                                      points=points,
                                                      quadrilaterals=quadrilaterals)
        
        self.meshs_quadrilaterals_models[id]=model_mesh_quadrilaterals        

    def getModelsMeshsTriangular(self):
        return self.meshs_models
    
    def getModelsMeshsQuadrilaterals(self):
        return self.meshs_quadrilaterals_models
    
    def deleteMeshTriangular(self, id):
        self.model_project_current_repository.deleteMeshTriangularDB(id)  
        removed_model_mesh_triangular = self.meshs_models.pop(id)
        removed_model_mesh_triangular.deleteMesh()
        del removed_model_mesh_triangular

    def deleteMeshQuadrilaterals(self, id):
        self.model_project_current_repository.deleteMeshQuadrilateralDB(id)  
        removed_model_mesh_quadrilaterals = self.meshs_quadrilaterals_models.pop(id)
        removed_model_mesh_quadrilaterals.deleteMesh()
        del removed_model_mesh_quadrilaterals

    def removeMesh(self):
        self.meshs_models.clear()
        self.meshs_quadrilaterals_models.clear()

        
    # ::::::::::::::::::::           PUNTOS MATERIALES         ::::::::::::::::::::

    def createMaterialPoint(self, name, color, points, id_property):

        
        id = str(uuid.uuid4())
        self.model_project_current_repository.createMaterialPointDB(
            id_MP = id,
            name = name, 
            color = color, 
            points = points,
            id_property=id_property)
        self.addMaterialPointToCurrentProject(
                id=id,
                name=name,
                color=color,
                points=points,
                id_property=id_property)
        return id
    
    def addMaterialPointToCurrentProject(self,id, name, color, points, id_property):  

        
        property = self.properties_models[id_property]

        model_material_point = ModelMaterialPoint(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      color=color,
                                                      points=points,
                                                      property = property)
        self.material_point_models[id]=model_material_point        

    def getModelsPointsMaterials(self):
        return self.material_point_models
    
    def deleteMaterialPoint(self, id):
        self.model_project_current_repository.deleteMaterialPointDB(id)        
        removed_model_material_point = self.material_point_models.pop(id)
        removed_model_material_point.deleteMaterialPoint()
        del removed_model_material_point

    def removeMaterialPoint(self):
        self.material_point_models.clear()
        
        
    # ::::::::::::::::::::           PUNTOS PROPOIEDADES         ::::::::::::::::::::



    def createProperty(self, name, 
                            modulus_elasticity,
                            poisson_ratio,
                            cohesion,
                            friction_angle,
                            angle_dilatancy):
        id = str(uuid.uuid4())
        self.model_project_current_repository.createPropertiesDB(
            id_properties = id,
            name = name, 
            modulus_elasticity=modulus_elasticity,
            poisson_ratio=poisson_ratio,
            cohesion=cohesion,
            friction_angle=friction_angle,
            angle_dilatancy=angle_dilatancy)
        self.addPropertyToCurrentProject(
                id=id,
                name=name,
                modulus_elasticity=modulus_elasticity,
                poisson_ratio=poisson_ratio,
                cohesion=cohesion,
                friction_angle=friction_angle,
                angle_dilatancy=angle_dilatancy)
        return id
    
    def addPropertyToCurrentProject(self,id, name, 
                                    modulus_elasticity,
                                    poisson_ratio,
                                    cohesion,
                                    friction_angle,
                                    angle_dilatancy):    
        model_property = ModelProperty(scene_draw=self.__scene,
                                        model_project_current_repository=self.model_project_current_repository,
                                        id=id,
                                        name=name,
                                        modulus_elasticity=modulus_elasticity,
                                        poisson_ratio=poisson_ratio,
                                        cohesion=cohesion,
                                        friction_angle=friction_angle,
                                        angle_dilatancy=angle_dilatancy)
        self.properties_models[id]=model_property        

    def getModelsProperties(self):
        return self.properties_models
    
    def deleteProperty(self, id):
        self.model_project_current_repository.deletePropertiesDB(id)        
        removed_model_property = self.properties_models.pop(id)        
        del removed_model_property

    def removeProperties(self):
        self.properties_models.clear()
        
        









    def getSelectedObjects(self):
        return self.__selected_objects




    ###############################################################################
    # ::::::::::::::::::::          COMANDOS SCENE           ::::::::::::::::::::
    ###############################################################################

    def commandMeshSize(self, input:dict):
        
        step = input["step"]
        data = input["data"]        
        
        if step == 1:            
            self.__scene.isMeshSize= True           

        elif step == 2:
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )
            dist = (((dx)**2)+((dy)**2))**0.5

            self.signal_size_mesh.emit(dist)
            #self.signal_end_draw_geometry.emit(False)

    def commandMeshSelectLine(self, input:dict):
        
        step = input["step"]
        data = input["data"]


        if step == 1:    
            #self.hideShowSelectedObjects(False) 
            self.endMeshSelectLine()
            self.__selected_objects = []
            self.__scene.isMeshSelect = True            
            self.__scene.isMeshCua = True      

            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0


            for item in items:     


                
                if isinstance(item, TextItem) or isinstance(item,PointItem):                    
                    continue    
          
                elif isinstance(item, LineItem):
                    if not (item in self.__selected_objects) :
                        count += 1
                        self.__selected_objects.append(item)
                        item.isSelectedMesh = True
     

            if count > 0:
                no_lines = len(self.__selected_objects)
                self.signal_select_line_mesh.emit(no_lines)
                print( "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(no_lines,  count))

  

    def commandPoint(self, input:dict):        
        
        step = input["step"]
        coordinate = input["data"]
        if step == 1:
            self.__scene.endDrawGeometry()
            self.__scene.isDrawPoint = True  
            self.signal_msn_label_view.emit(["point","Ingrese un punto [Exit]:",None])
       

            
        elif step == 2:
            point_vertex = QPointF(coordinate[0],coordinate[1])
            items = self.__scene.items(point_vertex)
            cancel_point = False

            # verifica si el punto esta por fuera de los limites
            if not self.pointInRect(point_vertex,self.__scene.sceneRect()):
                cancel_point = True

                
                self.signal_msn_label_view.emit(["Warning","Posición fuera del límite del dibujo.",1])
                return cancel_point

            #verifica si hay puntos existentes
            for item in items:
                if type(item) == PointItem:
                    name = item.getData()["name"]
                    if name != "pointTemp":       
                        self.signal_msn_label_view.emit(["Warning", "En esta posición ya existe el punto {}".format(name), 1])                
     
                        return item.getId()
                    

            #::::::::::::  punto  ::::::::::::::::
            no_max = 0
            for id_point_item in self.items_points_models:
                model_point_item = self.items_points_models[id_point_item]
                name = model_point_item.getName()
                parts = name.split("POINT#")
                number = int(parts[1])
                if number > no_max:
                    no_max = number            

            no_id = no_max+1
            name =  f"POINT#{no_id}"
            coordinates = [point_vertex.x(), point_vertex.y()]    
            id =str(uuid.uuid4())
            add_point_command = AddPointCommand(current_project=self,
                                                data=[id, name, coordinates])    
                  
            self.undo_stack.push(add_point_command) 
            self.signal_msn_label_view.emit(["Command","Se ha creado el punto {}".format(name), 1])  
            return add_point_command.getId() 

    def commandLine(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        if step == 1:
            self.__scene.endDrawGeometry()
            self.__scene.isDrawLine = True     
            self.signal_msn_label_view.emit(["line","Ingrese el primer punto [Exit]:",None])       
             
        elif step == 2:
            
            point=data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertexAnt(point_vertex)
            self.signal_msn_label_view.emit(["line","Ingrese el siguiente punto [Exit]:", 2]) 
            
              
        elif step == 3:

            point_vertex1 = QPointF(data[0][0],data[0][1])
            point_vertex2 = QPointF(data[1][0],data[1][1])

            # verifica si el punto esta por fuera de los limites
            if not self.pointInRect(point_vertex1,self.__scene.sceneRect()) or not self.pointInRect(point_vertex2,self.__scene.sceneRect()):                             
                self.signal_msn_label_view.emit(["Warning","> Posición fuera del límite del dibujo.",1])
                return 
            
            id_point_start = self.commandPoint({"step":2, "data": [data[0][0],data[0][1]]}) 
            id_point_end = self.commandPoint({"step":2, "data": [data[1][0],data[1][1]]}) 

            if  id_point_start==id_point_end:
                return
            
            #verifica si hay lineas existentes      
            model_point_start = self.items_points_models[id_point_start]
            model_point_end = self.items_points_models[id_point_end]

            for id_line in self.items_lines_models:
                model_ref_point_start = self.items_lines_models[id_line].getStartPoint()
                model_ref_point_end = self.items_lines_models[id_line].getEndPoint()
                point_ref = [model_ref_point_start, model_ref_point_end]
                if (model_point_start in point_ref) and (model_point_end in point_ref):
                    name = self.items_lines_models[id_line].getName()
                    id = self.items_lines_models[id_line].getId()
                    self.signal_msn_label_view.emit(["Warning", "En esta posición ya existe la linea {}".format(name), 1])  
                    return id



            #::::::::::::  linea  ::::::::::::::::
            no_max = 0
            for id_line_item in self.items_lines_models:
                model_line_item = self.items_lines_models[id_line_item]
                name = model_line_item.getName()
                parts = name.split("LINE#")
                number = int(parts[1])
                if number > no_max:
                    no_max = number            

            no_id = no_max+1
            name =  f"LINE#{no_id}"
            id = str(uuid.uuid4())
            add_line_command = AddLineCommand(current_project=self,
                                                data=[id, name,id_point_start, id_point_end])            
            self.undo_stack.push(add_line_command) 
            self.signal_msn_label_view.emit(["Command","Se ha creado la linea {}".format(name), 1])  
            point=data[1]
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertexAnt(point_vertex) 

            id_new_line = add_line_command.getId()



            return id_new_line

    def commandMove(self, input:dict):
                
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.__scene.endDrawGeometry()
            # se activa modo mover
            self.__scene.isDrawSelect = True            
            self.__scene.isDrawMove= True            
            self.signal_msn_label_view.emit(["move","Seleccione un elemento [Exit]:",None])   
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
                #verificar cuales lineas si toca
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
              
            count = 0
            for item in items:    

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelectedDraw = True
                    if not (item in self.getSelectedItems()):
                        count += 1
                        self.addSelectedItems(item)


                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelectedDraw = True
                    point_B.isSelectedDraw = True
                    item.isSelectedDraw = True

                    if not (point_A in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_A)
                        
                    if not (point_B in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_B)

                    if not (item in self.getSelectedItems()) :
                        count += 1
                        self.__scene.selected_items_line.append(item)

                self.__scene.update()

                #    if item.getData()["name"] != "rectTemp":


            if count > 0:
                            
                self.signal_msn_label_view.emit(["Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ), 1]) 
                

                

        #Inicio de mover
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.__scene.update()
            self.__scene.isDrawSelect = False
            self.signal_msn_label_view.emit(["Command","{} Elementos seleccionados".format(selected_items), 1]) 
            self.signal_msn_label_view.emit(["move", "Ingrese el primer punto [Exit]:", 2]) 


        
        # Se recibe el primer punto
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)

            self.signal_msn_label_view.emit(["Command","Punto inicial = {}".format(data), 1]) 
            self.signal_msn_label_view.emit(["move", "Ingrese el segundo punto [Exit]:", 2]) 


        # Se recibe el segundo punto
        elif step == 5:
           
            items = self.getSelectedItems()
  
 
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_vertex=QPointF(xi+dx, yi+dy)

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.__scene.sceneRect()):                    
                    self.signal_msn_label_view.emit(["Warning","Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"]), 1]) 
                    return 
                
                items_in_new_pos = self.__scene.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.signal_msn_label_view.emit(["Error","En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name), 1]) 
                            return 


            move_command = MoveCommand(current_project=self,items= items,dx= dx,dy= dy)
            self.undo_stack.push(move_command) 



            self.signal_msn_label_view.emit(["Command","Punto Final = {}".format(data[1]), 1]) 
            self.signal_msn_label_view.emit(["Command","Se ha movido los elementos seleccionados".format(), 1]) 
            self.signal_msn_label_view.emit(["", "", 3])  
            self.__scene.endDrawGeometry()

    def commandRotate(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.__scene.endDrawGeometry()
            # se activa modo rotar
            self.__scene.isDrawSelect = True            
            self.__scene.isDrawRotate= True  
            self.signal_msn_label_view.emit(["rotate","Seleccione un elemento [Exit]:",None])  
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelectedDraw  = True
                    if not (item in self.getSelectedItems()):
                        count += 1
                        self.addSelectedItems(item)
                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelectedDraw  = True
                    point_B.isSelectedDraw  = True
                    item.isSelectedDraw  = True

                    if not (point_A in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_A)
                        
                    if not (point_B in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_B)

                    if not (item in self.__scene.selected_items_line) :
                        count += 1
                        self.__scene.selected_items_line.append(item)

                '''
                item.isSelectedDraw  = True
                if not (item in self.__scene.selected_items) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.addSelectedItems(item)
                '''


            if count > 0:
                
                self.signal_msn_label_view.emit(["Command","Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ) , 1]) 


        #Inicio de rotar
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.__scene.update()
            self.__scene.isDrawSelect = False
            self.signal_msn_label_view.emit(["Command","{} Elementos seleccionados".format(selected_items), 1]) 
            self.signal_msn_label_view.emit(["rotate", "Ingrese el punto base [Exit]:", 2])    

        
        # Se recibe el punto centro para rotar
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)      
            self.signal_msn_label_view.emit(["Command", "Punto base = {}".format(data), 1]) 
            self.signal_msn_label_view.emit(["rotate", "Ingrese el ángulo [Exit]:", 2])   

        # Se recibe el segundo punto
        elif step == 5:



            items = self.getSelectedItems()
            x_ref, y_ref = data[0][0], data[0][1]
            point_ref = QPointF(x_ref, y_ref)
            angle_ref = data[1]

            """
            group_selected = QGraphicsItemGroup()
            for item_i in items_i:                
                group_selected.addToGroup(item_i)
            self.__scene.addItem(group_selected)
            transform = QTransform().translate(pivot.x(), pivot.y()).rotate(angle_ref).translate(-pivot.x(), -pivot.y())
            group_selected.setTransform(transform, combine=False)

            elements = group_selected.childItems()
            self.__scene.removeItem(group_selected)
            """
            list_items_new_pos =[]

 
            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_to_rotate =  QPointF(xi,yi)
                angle_rad_ref = math.radians(angle_ref)     
                dx = point_to_rotate.x() - point_ref.x()
                dy = point_to_rotate.y() - point_ref.y()
                dist = math.sqrt(dx*dx + dy*dy)
                angle_point = math.atan2(dy, dx)
                if angle_point < 0:
                    angle_point = (2*math.pi) + angle_point

                angle_new = angle_point + angle_rad_ref

                # Calcular la nueva posición del punto después de la rotación
                new_x = point_ref.x() + dist * math.cos(angle_new)
                new_y = point_ref.y() + dist * math.sin(angle_new)              
                
                point_vertex=QPointF(new_x, new_y)            

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.__scene.sceneRect()):   
                    self.signal_msn_label_view.emit(["Warning", "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"]), 1]) 
                    return 
                
                items_in_new_pos = self.__scene.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.signal_msn_label_view.emit(["Error", "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name), 1]) 

             
                                
                                
                            return 
                
                list_items_new_pos.append([item, xi, yi, new_x, new_y])





            rotate_command = RotateCommand(current_project=self,items= list_items_new_pos)
            self.undo_stack.push(rotate_command) 



            self.signal_msn_label_view.emit(["Command","ángulo = {}".format(data[1]) , 1]) 
            self.signal_msn_label_view.emit(["Command", "Se ha rotado los elementos seleccionados".format(), 1]) 
            self.signal_msn_label_view.emit(["", "", 3])  

            self.__scene.endDrawGeometry()

    def commandCopy(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        # 1) Inicio, selección de elementos
        if step == 1:
            self.__scene.endDrawGeometry()
            # se activa modo copiar
            self.__scene.isDrawSelect = True            
            self.__scene.isDrawCopy = True            
        
            self.signal_msn_label_view.emit(["copy","Seleccione un elemento [Exit]:",None])  
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:       




                item.isSelectedDraw = True
                if not (item in self.getSelectedItems()) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.addSelectedItems(item)




            if count > 0:
                 self.signal_msn_label_view.emit(["Command","Copiar Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ), 1]) 
        
                    
        #Inicio de copiar
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.__scene.update()
            self.__scene.isDrawSelect = False
            self.signal_msn_label_view.emit(["Command","{} Elementos seleccionados".format(selected_items), 1]) 
            self.signal_msn_label_view.emit(["copy", "Ingrese el primer punto [Exit]:", 2]) 
        
        # Se recibe el primer punto
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)
            self.signal_msn_label_view.emit(["Command","Punto inicial = {}".format(data), 1]) 
            self.signal_msn_label_view.emit(["copy", "Ingrese el segundo punto [Exit]:", 2]) 
            

        # Se recibe el segundo punto
        elif step == 5:           

            items = self.getSelectedItems()
            
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                if isinstance(item, PointItem):
                    xi = item.getData()["coordinates"][0]
                    yi =item.getData()["coordinates"][1]
                    id_point = self.commandPoint({"step":2, "data": [xi+dx,yi+dy]})


                if isinstance(item, LineItem):
                    x_start_point = (item.start_point.getData()["coordinates"][0])+ dx
                    y_start_point = (item.start_point.getData()["coordinates"][1]) + dy
                    x_end_point =   (item.end_point.getData()["coordinates"][0]) + dx
                    y_end_point =   (item.end_point.getData()["coordinates"][1]) + dy                   
 
                    self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})

            self.signal_msn_label_view.emit(["Command","Punto final = {}".format(data[1]), 1]) 
            self.signal_msn_label_view.emit(["", "", 3])  

    def commandErase(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.__scene.endDrawGeometry()
            # se activa modo borrar
            self.__scene.isDrawSelect = True            
            self.__scene.isDrawErase= True  
            self.signal_msn_label_view.emit(["erase","Seleccione un elemento [Exit]:",None])
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0


            for item in items: 
                if isinstance(item, TextItem):                    
                    continue   
                elif isinstance(item,PointItem) or isinstance(item, LineItem):
                    count += 1
                    self.addSelectedItems(item)      
                    item.isSelectedDraw  = True


            if count > 0:

                self.signal_msn_label_view.emit(["Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ), 1]) 

           
                
        #Inicio de borrar
        elif step == 3:
            items= self.getSelectedItems()
            selected_items = len(items)      
            self.signal_msn_label_view.emit(["Command","{} Elementos seleccionados".format(selected_items), 1]) 


            point_items = []
            line_items = []

            for item in items:
                if isinstance(item, PointItem):
                    point_items.append(item)
                elif isinstance(item, LineItem):
                    line_items.append(item)

           
            remove_line_command = RemoveLineCommand(current_project=self, items= line_items)
            self.undo_stack.push(remove_line_command)

            point_items_corrected = []
            for point in point_items:                
                model_point = self.items_points_models[point.getId()]
                no_lines = len(model_point.getLines())
                if no_lines == 0:
                    point_items_corrected.append(point)
             

                
            remove_point_command = RemovePointCommand(current_project=self, items= point_items_corrected)
            self.undo_stack.push(remove_point_command)


            self.signal_msn_label_view.emit(["Command","Se ha eliminado {} de los elementos seleccionados".format(len(point_items_corrected)), 1]) 
            self.signal_msn_label_view.emit(["", "", 3]) 

 
            
            self.__scene.endDrawGeometry()

    def commandImport(self, input:dict):
        
        step = input["step"]
        data = input["data"]
               
 
        # 1) Inicio, selección de elementos
        if step == 1:
            options = QFileDialog.Options()
            dxf_file_path, _ = QFileDialog.getOpenFileName(self.view_draw_2,"Importar DXF","","Data files dxf (*.dxf)", options=options)

            if dxf_file_path:
                doc = ezdxf.readfile(dxf_file_path)            
                msp = doc.modelspace()

                for entity in msp:
                    if entity.dxftype() == "POINT":
                        xi = entity.dxf.location[0]
                        yi = entity.dxf.location[1]

                        self.commandPoint({"step":2, "data": [xi,yi]})

                    elif entity.dxftype() == "LINE":
                        start_point = entity.dxf.start
                        end_point = entity.dxf.end

                        x_start_point =start_point[0]
                        y_start_point =start_point[1]
                        x_end_point =end_point[0]
                        y_end_point =end_point[1]
                        self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})


                        
                    elif entity.dxftype() == "LWPOLYLINE":
                        points = [(vertex[0], vertex[1]) for vertex in entity.get_points()]
                        for i in range(len(points) - 1):
                            start_point = points[i]
                            end_point = points[i+1]
                            x_start_point, y_start_point = start_point
                            x_end_point, y_end_point = end_point
                            self.commandLine({"step": 3, "data": [[x_start_point, y_start_point], [x_end_point, y_end_point]]})

    def commandIntersection(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
        # 1) Inicio, selección de elementos
        if step == 1:
            self.__scene.endDrawGeometry()
            # se activa modo Interseccion
            self.__scene.isDrawSelect = True            
            self.__scene.isDrawIntersection= True    
            self.signal_msn_label_view.emit(["intersection","Seleccione un elemento [Exit]:",None])
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.__scene.items(self.__scene.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.__scene.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        
                
                if isinstance(item, TextItem):                    
                    continue    

                elif isinstance(item,PointItem):
                    continue

                elif isinstance(item, LineItem):

                    if (not self.deselect_draw_geometry) and (not (item in self.getSelectedItems())) :
                        count += 1
                        self.addSelectedItems(item)
                        item.isSelectedDraw  = True

                    elif self.deselect_draw_geometry and (item in self.getSelectedItems()):
                        item.isSelectedDraw  = False
                        self.removeSelectedItems(item)



            if count > 0:
                self.signal_msn_label_view.emit(["Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ), 1]) 

    
        #Inicio de interseccion a
        elif step == 3:

            
            selected_items = self.getSelectedItems()
            self.__scene.isDrawSelect = False
            self.signal_msn_label_view.emit(["Command","{} Elementos seleccionados".format(len(selected_items)), 1]) 


            self.intersectionLinesDraw(selected_items)

            self.signal_msn_label_view.emit(["Command","Se ha creado la intersección ", 1]) 
            self.signal_msn_label_view.emit(["", "", 3]) 
            self.__scene.endDrawGeometry()


    def commandRule(self, input:dict):

        
        step = input["step"]
        data = input["data"]

        if step == 1:   
            self.__scene.endDrawGeometry()     
            self.__scene.isDrawRule = True      
            self.signal_msn_label_view.emit(["rule", "Ingrese el primer punto [Exit]:",None])  

        if step == 2:                  
            self.signal_msn_label_view.emit(["rule", "Ingrese el segundo punto [Exit]:",None])

        elif step == 3:  
            x1, y1 = data[0][0],data[0][1]
            x2, y2 = data[1][0],data[1][1]

            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )
            dist = (((dx)**2)+((dy)**2))**0.5
            if dx != 0:
                angle = math.degrees(math.atan(dy/dx))
            else:
                angle = math.degrees(math.atan(dy/0.000000001))

            self.signal_msn_label_view.emit(["Command","Punto Inicial: [{},{}] Punto Final: [{}, {}]".format(x1,y1,x2,y2), 1])
            self.signal_msn_label_view.emit(["Command","dx:{} dy:{}".format(dx,dy), 1])
            self.signal_msn_label_view.emit(["Command","Distancia: {}".format(dist), 1])
            self.signal_msn_label_view.emit(["Command","Ángulo: {}".format(angle), 1])
            self.signal_msn_label_view.emit(["", "", 3]) 
            self.__scene.endDrawGeometry()



    def getSelectedItems(self):
        return self.__scene.getSelectedItems()

    def addSelectedItems(self, item):   
         self.__scene.addSelectedItems(item)

    def setPointVertex(self, point):
        self.__scene.setPointVertex(point)

    def setPointVertexAnt(self, point):
        self.__scene.setPointVertexAnt(point)

    def removeSelectedItems(self, item):   
         self.__scene.removeSelectedItems(item)

    def endMeshSelectLine(self):
        for item in self.__selected_objects:
            item.isSelectedMesh = False
        self.__selected_objects=[]
        self.__scene.update()




    def deselectDrawGeometry(self, shift_pressed ):
        self.deselect_draw_geometry = shift_pressed


  
    def showHideItems(self, show_items):

        for id_model_point in self.getModelsPoints():
            model_point = self.getModelsPoints()[id_model_point]
            model_point.showHideItems(show_items)

        for id_model_line in self.getModelsLines():
            model_line = self.getModelsLines()[id_model_line]
            model_line.showHideItems(show_items)
        
        self.__scene.update()


  
    def showHideLabel(self, show_label):

        for id_model_point in self.getModelsPoints():
            model_point = self.getModelsPoints()[id_model_point]
            item_point = model_point.getPointItem()
            item_point.showLabel = show_label


        for id_model_line in self.getModelsLines():
            model_line = self.getModelsLines()[id_model_line]
            item_line = model_line.getLineItem()
            item_line.showLabel = show_label        
        self.__scene.update()






    ###############################################################################
    # ::::::::::::::::::::          GUARDAR PROYECTO           ::::::::::::::::::::
    ###############################################################################

    def checkProjectChanges(self):
        return self.model_project_current_repository.checkProjectChanges()

    def saveDataDb(self):
        return self.model_project_current_repository.saveDataDb()
    
    def projectSaveAs(self, new_path_file):
        return self.model_project_current_repository.projectSaveAs(new_path_file)

    def pointInRect(self, point:QPointF, rec:QRectF):
        val = True
        x = point.x()
        y = point.y()

        xi = rec.x()
        yi = rec.y()
        xf = rec.x()+rec.width()
        yf = rec.y()+rec.height()

        if xi <= x <= xf:
            if yi <= y <=yf:
                pass
            else:
                val = False
        else:
            val = False
        return val
        
    def intersectionLinesDraw(self, selected_items:list):

            len_selected_items= len(selected_items)

            for i in range(len_selected_items): 
                for j in range(i+1,len_selected_items): 

                    line_A= selected_items[i]
                    line_B= selected_items[j]
                    

                    # Obtener los puntos finales de cada línea
                    lA_p1, lA_p2 = line_A.getPoints()
                    lB_p1, lB_p2 = line_B.getPoints()

                    
                    lA_p1f, lA_p2f  = lA_p1.getCoordinates(), lA_p2.getCoordinates()
                    lB_p1f, lB_p2f = lB_p1.getCoordinates(), lB_p2.getCoordinates()

                    line_Af = QLineF(lA_p1f, lA_p2f )
                    line_Bf = QLineF(lB_p1f, lB_p2f)
                    
                
                    # Calcular la intersección entre las dos líneas
                    intersection_type, intersection_point = line_Af.intersects(line_Bf)

                    # Verificar si las líneas se intersectan
                    if intersection_type == QLineF.IntersectionType.BoundedIntersection:# or intersection_type == QLineF.IntersectionType.IntersectsWithLine:

                        new_point = self.commandPoint({"step":2, "data": [intersection_point.x(),intersection_point.y()]})
                        new_point = self.items_points_models[new_point].getPointItem()
                        
                        line_A_new =None
                        line_B_new =None
                        
                        # Linea A
                        if new_point != lA_p1 and new_point != lA_p2:
                            update_command = UpdateCommand(current_project=self,
                                                            item = line_A, 
                                                            points= [lA_p1, new_point])

                            self.undo_stack.push(update_command)
                            line_A_new = self.commandLine({"step":3, "data":[
                                        [intersection_point.x(),intersection_point.y()],
                                        [lA_p2f.x(),lA_p2f.y()]]})
                            line_A_new = self.items_lines_models[line_A_new].getLineItem()
                            #new_point.addAnchoredLine(line_A)
                            #new_point.addAnchoredLine(line_A_new)
            
                        # Linea B
                        if new_point != lB_p1 and new_point != lB_p2:
                            update_command = UpdateCommand(current_project=self,
                                                            item = line_B,
                                                            points=  [lB_p1, new_point])

                            self.undo_stack.push(update_command)
                            line_B_new = self.commandLine({"step":3, "data":[
                                        [intersection_point.x(),intersection_point.y()],
                                        [lB_p2f.x(),lB_p2f.y()]]})
                            line_B_new = self.items_lines_models[line_B_new].getLineItem()
                            #new_point.addAnchoredLine(line_B)
                            #new_point.addAnchoredLine(line_B_new)
                        if line_A_new != None or line_B_new != None:
                            if line_A_new != None:
                                selected_items.append(line_A_new)
                            if line_B_new != None:
                                selected_items.append(line_B_new)
                            self.intersectionLinesDraw(selected_items)
                            return

    