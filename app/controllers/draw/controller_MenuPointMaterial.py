from PySide6.QtCore import (Slot, Signal, QObject)
from views.draw.view_WidgetDrawMenuPointMaterial import ViewWidgetDrawMenuPointMaterial
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMaterialPoint import ControllerCardMaterialPoint
from utils.items_GraphicsDraw import PointMaterialItem

class ControllerMenuPointMaterial(QObject):

    signal_new_points_material = Signal(str)
    signal_delete_points_material= Signal() 
    signal_edit_points_material= Signal() 
    
    signal_cancel_select = Signal()
    
    def __init__(self) -> None:
        super().__init__()

        self.view_menu_pointMaterial = ViewWidgetDrawMenuPointMaterial()
        self.model_current_project = None
        self.list_controller_card=[]

        self.__config()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __config(self):
        self.setListNoPointsView()
        self.setNoPointsView()
        self.setBaseMeshView()

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_pointMaterial.signal_new_points_material.connect(self.newPointsMaterial)
        self.view_menu_pointMaterial.signal_show_hide_points_materials.connect(self.showHidePointsMaterials)
        self.view_menu_pointMaterial.signal_show_hide_label.connect(self.showHideLabel)
        self.view_menu_pointMaterial.signal_change_size_point.connect(self.ChangeSizePoint)
        self.view_menu_pointMaterial.signal_select_points_material.connect(self.signalSelectPointsMaterial)
        self.view_menu_pointMaterial.signal_cancel_select.connect(self.signalCancelSelect)
        self.view_menu_pointMaterial.signal_assing_points_material.connect(self.assignDataPointsMaterial)

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project
        self.model_current_project.signal_select_point_material.connect(self.selectPointMaterial)


        
    def configDrawMenuPointMaterial(self):

        self.view_menu_pointMaterial.removeCardMaterialPoint()
        self.view_menu_pointMaterial.clearListProperties()
        self.list_controller_card =[]
        
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        for id_point_material in models_points_materials:
            self.createPointsMaterialsCard(models_points_materials[id_point_material])        
        self.setListBaseMeshView()

    def getView(self):
        return self.view_menu_pointMaterial

    def createPointsMaterialsCard(self, model_point_material):
        controller_card_material_point = ControllerCardMaterialPoint( model_project_current=self.model_current_project,
                                                model_point_material=model_point_material
                                                )
        self.view_menu_pointMaterial.addCardMaterialPoint(controller_card_material_point.view_card_material_point)
        controller_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)
        controller_card_material_point.signal_edit_material_point.connect(self.editMaterialPoint)   
        self.list_controller_card.append(controller_card_material_point)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::
    @Slot(bool)
    def showHidePointsMaterials(self, show_points_materials):
        for controller in self.list_controller_card:
            controller.showHideMaterialPoint(show_points_materials)



    @Slot(bool)
    def showHideLabel(self, show_label):        
        for controller in self.list_controller_card:
            controller.showHideLabelTitle(show_label)

    @Slot()
    def ChangeSizePoint(self):
        value = self.view_menu_pointMaterial.getSizePoint()
        for controller in self.list_controller_card:
            controller.ChangeSizePoint(value)
    
    @Slot()
    def signalSelectPointsMaterial(self):
        self.model_current_project.commandAssignSelectPointMaterial({"step":1, "data":None}) 
    
    @Slot()
    def signalCancelSelect(self):
        self.signal_cancel_select.emit()
        self.endDrawPointMaterial()
        
        
    
    @Slot()
    def assignDataPointsMaterial(self):        

        selected_objects = self.model_current_project.getSelectedObjects() 
        vox, voy = self.view_menu_pointMaterial.getVoxVoy()
        fx, fy = self.view_menu_pointMaterial.getFxFy()
        
        if len(selected_objects) <= 0:
            self.view_menu_pointMaterial.msnAlertSelect(True, "Selecciona los puntos materiales")
        
        for point_material in selected_objects:
            if isinstance(point_material, PointMaterialItem):
                id_group = point_material.getIdGroup()
                id_node = point_material.getIdNode()
                response = self.model_current_project.updateVectorQuantityPointsMaterial(id_MP=id_group, id_node=id_node, 
                                                                               vox=vox, voy=voy, fx=fx, fy=fy)
        self.view_menu_pointMaterial.endVectorQuantity()
        self.model_current_project.endVectorQuantityPointsMaterial()

        
        
           
    @Slot()
    def newPointsMaterial(self):


        point_material_name = self.view_menu_pointMaterial.getName()
        point_material_id_base_mesh, point_material_base_mesh, point_material_base_mesh_type = self.view_menu_pointMaterial.getBaseMesh()
        point_material_id_property, point_material_name_property = self.view_menu_pointMaterial.getProperty()
        point_material_no_points = self.view_menu_pointMaterial.getNoPoints()
        
        if point_material_name == "":
            self.view_menu_pointMaterial.msnAlertName(True, "Revisa el nombre de los puntos materiales")
            return     
        else:
            self.view_menu_pointMaterial.msnAlertName(False)

        if point_material_base_mesh == "":
            self.view_menu_pointMaterial.msnAlertBaseMesh(True, "Selecciona una malla base")
            
            return     
        else:
            self.view_menu_pointMaterial.msnAlertBaseMesh(False)
        

        if point_material_name_property == "":
            self.view_menu_pointMaterial.msnAlertBaseMesh(True, "Selecciona un material")
            
            return     
        else:
            self.view_menu_pointMaterial.msnAlertBaseMesh(False)
        
    
        
        if point_material_no_points == "":
            self.view_menu_pointMaterial.msnAlertNoPoints(True, "Selecciona la cantidad de puntos por elemento")
            return     
        else:
            self.view_menu_pointMaterial.msnAlertNoPoints(False)
        



        id_property = self.model_current_project.getModelsProperties()[point_material_id_property].getId()
        
        if point_material_base_mesh_type == "QUADRILATERAL":

            base_mesh =self.model_current_project.getModelsMeshsQuadrilaterals()[point_material_id_base_mesh]
        
            coordenates_quadrilaterals= base_mesh.getNodes()
            quadrilaterals= base_mesh.getElements()

            point_material_points =[]
            point_material_volumes =[]

            for quadrilateral in quadrilaterals:
                node_a = quadrilaterals[quadrilateral][0]
                node_b = quadrilaterals[quadrilateral][1]
                node_c = quadrilaterals[quadrilateral][2]
                node_d = quadrilaterals[quadrilateral][3]                
                
                point1  = coordenates_quadrilaterals[node_a]['COORDINATES']
                point2  = coordenates_quadrilaterals[node_b]['COORDINATES']
                point3  = coordenates_quadrilaterals[node_c]['COORDINATES']
                point4  = coordenates_quadrilaterals[node_d]['COORDINATES']
                
                # volumen del elemeto quadrilateral 
                volume_element = abs((point1[0]*(point2[1]-point3[1]) + point2[0]*(point3[1]-point1[1]) + point3[0]*(point1[1]-point2[1]))/2) + abs((point1[0]*(point3[1]-point4[1]) + point3[0]*(point4[1]-point1[1]) + point4[0]*(point1[1]-point3[1]))/2)

                center_x = (point1[0] + point2[0] + point3[0] + point4[0]) / 4
                center_y = (point1[1] + point2[1] + point3[1] + point4[1]) / 4
                center_point = [center_x, center_y]

                if point_material_no_points == "1x": # 1 punto
                    point_material_points.append(center_point)  
                    point_material_volumes.append(volume_element)

                elif point_material_no_points == "2x": # 4 puntos
                    center_x = (point1[0] + center_point[0]) / 2
                    center_y = (point1[1] + center_point[1]) / 2
                    center_point_1 = [center_x, center_y]
                    point_material_points.append(center_point_1)  
                    point_material_volumes.append(volume_element/4)


                    center_x = (point2[0] + center_point[0]) / 2
                    center_y = (point2[1] + center_point[1]) / 2
                    center_point_2 = [center_x, center_y]
                    point_material_points.append(center_point_2)  
                    point_material_volumes.append(volume_element/4)

                    
                    center_x = (point3[0] + center_point[0]) / 2
                    center_y = (point3[1] + center_point[1]) / 2
                    center_point_3 = [center_x, center_y]
                    point_material_points.append(center_point_3) 
                    point_material_volumes.append(volume_element/4)

                    
                    center_x = (point4[0] + center_point[0]) / 2
                    center_y = (point4[1] + center_point[1]) / 2
                    center_point_4 = [center_x, center_y]
                    point_material_points.append(center_point_4)  
                    point_material_volumes.append(volume_element/4)
                    
                    
        


        elif point_material_base_mesh_type == "TRIANGULAR":
            
            
            base_mesh =self.model_current_project.getModelsMeshsTriangular()[point_material_id_base_mesh]
            coordenates_triangles= base_mesh.getNodes()
            triangles= base_mesh.getElements()

            point_material_points =[]
            point_material_volumes =[]
            for triangle in triangles:
                node_a = triangles[triangle][0]
                node_b = triangles[triangle][1]
                node_c = triangles[triangle][2]
                
                point1  = coordenates_triangles[node_a]['COORDINATES']
                point2  = coordenates_triangles[node_b]['COORDINATES']
                point3  = coordenates_triangles[node_c]['COORDINATES']    

                
                volume_element = abs((point1[0]*(point2[1]-point3[1]) + point2[0]*(point3[1]-point1[1]) + point3[0]*(point1[1]-point2[1]))/2)

                center_x = (point1[0] + point2[0] + point3[0]) / 3
                center_y = (point1[1] + point2[1] + point3[1]) / 3
                center_point = [center_x, center_y]

                if point_material_no_points == "1x":
                    
                    point_material_points.append(center_point)  
                    point_material_volumes.append(volume_element)                    

                elif point_material_no_points == "2x":
                    center_x = (point1[0] + (center_point[0]*2)) / 3
                    center_y = (point1[1] + (center_point[1]*2)) / 3
                    center_point_1 = [center_x, center_y]
                    point_material_points.append(center_point_1)  
                    point_material_volumes.append(volume_element/3)
                    
                    center_x = (point2[0] + (center_point[0]*2)) / 3
                    center_y = (point2[1] + (center_point[1]*2)) / 3
                    center_point_2 = [center_x, center_y]
                    point_material_points.append(center_point_2)  
                    point_material_volumes.append(volume_element/3)
                    
                    center_x = (point3[0] + (center_point[0]*2)) / 3
                    center_y = (point3[1] + (center_point[1]*2)) / 3
                    center_point_3 = [center_x, center_y]
                    
                    point_material_points.append(center_point_3)  
                    point_material_volumes.append(volume_element/3)

        points_materials = {}
        index = 1

        if point_material_base_mesh_type == "Archivo":
            # Rama de carga por archivo de texto
            path_file = self.view_menu_pointMaterial.getPathFile()
            if not path_file:
                self.view_menu_pointMaterial.msnAlertBaseMesh(True, "Selecciona un archivo .txt con las coordenadas")
                return

            point_material_points = []
            point_material_volumes = []
            try:
                with open(path_file, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                            continue
                        # Reemplazamos ; y , por espacios y luego split() maneja cualquier cantidad de espacios
                        parts = line.replace(";", " ").replace(",", " ").split()
                        # garantizar que el archivo tenga al menos 3 columnas
                        if len(parts) >= 3:
                            x = float(parts[0].strip())
                            y = float(parts[1].strip())
                            vol = float(parts[2].strip())
                            point_material_points.append([x, y])
                            point_material_volumes.append(vol)
            except Exception as e:
                self.view_menu_pointMaterial.msnAlertBaseMesh(True, f"Error leyendo archivo: {e}")
                return

            if not point_material_points:
                self.view_menu_pointMaterial.msnAlertBaseMesh(True, "El archivo no contiene coordenadas válidas")
                return

            for center_point, volume_element in zip(point_material_points, point_material_volumes):
                points_materials[f'POINT#{index}'] = {
                    "COORDINATES": center_point,
                    "VOLUME": volume_element,
                    "VELOCITY": {"X": 0.0, "Y": 0.0},
                    "FORCE": {"X": 0.0, "Y": 0.0},
                }
                index += 1

        else:
            for center_point, volume_element in zip(point_material_points, point_material_volumes):
                points_materials[f'POINT#{index}'] = {
                    "COORDINATES": center_point,
                    "VOLUME": volume_element,
                    "VELOCITY": {"X": 0.0,"Y": 0.0},
                    "FORCE": {"X": 0.0,"Y": 0.0},
                }
                index += 1

        id = self.model_current_project.createMaterialPoint(name=point_material_name ,
                                                    points=points_materials,
                                                    id_property = id_property,
                                                    id_mesh_base=point_material_id_base_mesh                                                   
                                                    )
        model_point_material = self.model_current_project.getModelsPointsMaterials()[id]
        self.createPointsMaterialsCard(model_point_material)        
        self.setListPropertiesViews()

        self.view_menu_pointMaterial.endPointMaterial()
        
        self.signal_new_points_material.emit(id)

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(str)
    def deleteMaterialPoint(self, id):
        self.model_current_project.deleteMaterialPoint(id)
        for  controlled_card in self.list_controller_card:
            if controlled_card.id == id:
                self.list_controller_card.remove(controlled_card)            
                self.signal_delete_points_material.emit()
                break
        
        
    @Slot()
    def editMaterialPoint(self):
        self.signal_edit_points_material.emit()
        
    # ::::::::::::::::::::         MÉTODOS  CURRENT        ::::::::::::::::::::
	
    @Slot(int)
    def selectPointMaterial(self, no_points):
        self.view_menu_pointMaterial.setNoSelectPointsMaterial(no_points)


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def endDrawPointMaterial(self):
        
        self.model_current_project.endVectorQuantityPointsMaterial()
        self.selectPointMaterial(0)

 
   
    def setListBaseMeshView(self):  
        mesh_data = []   

        meshs = self.model_current_project.getModelsMeshsTriangular()
        for id_mesh in meshs:
            name = meshs[id_mesh].getName()
            color = meshs[id_mesh].getColor()
            type_mesh = meshs[id_mesh].getType()
            mesh_data.append([id_mesh, name, color, type_mesh])
        meshs = self.model_current_project.getModelsMeshsQuadrilaterals()
        for id_mesh in meshs:
            name = meshs[id_mesh].getName()
            color = meshs[id_mesh].getColor()
            type_mesh = meshs[id_mesh].getType()
            mesh_data.append([id_mesh, name, color, type_mesh])
        self.view_menu_pointMaterial.setListBaseMesh(mesh_data=mesh_data)
        
        for controller_card in self.list_controller_card:
            controller_card.setListBaseMeshViews()
            



    def setListPropertiesViews(self): 
        properties_data = []   
        property = self.model_current_project.getModelsProperties()
        for id_property in property:
            name = property[id_property].getName()
            color = property[id_property].getColor()
            properties_data.append([id_property, name, color])
        self.view_menu_pointMaterial.setListProperties(properties_data=properties_data)
        
        for controller_card in self.list_controller_card:
            controller_card.setListPropertiesViews(properties_data=properties_data)
            controller_card.setColor()

    
    def setBaseMeshView(self, index=0):        
        self.view_menu_pointMaterial.setBaseMesh(index=index)
    
    def setListNoPointsView(self):  
        self.view_menu_pointMaterial.setListNoPoints()
    
    def setNoPointsView(self, index=0):        
        self.view_menu_pointMaterial.setNoPoints(index=index)
    
