from PySide6.QtCore import (Slot)
from clases.Vista.view_WidgetDrawMenuPointMaterial import ViewWidgetDrawMenuPointMaterial
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardMaterialPoint import ControllerCardMaterialPoint


class ControllerMenuPointMaterial():

    def __init__(self) -> None:

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

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project

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
            controller.showHideLabel(show_label)

    @Slot()
    def ChangeSizePoint(self):
        value = self.view_menu_pointMaterial.getSizePoint()
        for controller in self.list_controller_card:
            controller.ChangeSizePoint(value)
    
        

        
    @Slot()
    def newPointsMaterial(self):

        point_material_name = self.view_menu_pointMaterial.getName()
        point_material_color = self.view_menu_pointMaterial.getColor()
        point_material_id_base_mesh, point_material_base_mesh, point_material_base_mesh_type = self.view_menu_pointMaterial.getBaseMesh()
        point_material_id_property, point_material_name_property = self.view_menu_pointMaterial.getProperty()
        point_material_no_points = self.view_menu_pointMaterial.getNoPoints()
        
        if point_material_name == "":
            self.view_menu_pointMaterial.msnAlertName(True, "Revisa el nombre de los puntos materiales")
            return     
        else:
            self.view_menu_pointMaterial.msnAlertName(False)

        

        if point_material_color == None:
            self.view_menu_pointMaterial.msnAlertColor(True, "Revisa el color de los puntos materiales")
            return     
        else:
            self.view_menu_pointMaterial.msnAlertColor(False)
        
        
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
        
            coordenates_quadrilaterals= base_mesh.getPoints()
            quadrilaterals= base_mesh.getQuadrilaterals()

            point_material_points =[]

            for quadrilateral in quadrilaterals:
                point1  = coordenates_quadrilaterals[quadrilateral[0]]
                point2  = coordenates_quadrilaterals[quadrilateral[1]]
                point3  = coordenates_quadrilaterals[quadrilateral[2]]
                point4  = coordenates_quadrilaterals[quadrilateral[3]]

                center_x = (point1[0] + point2[0] + point3[0] + point4[0]) / 4
                center_y = (point1[1] + point2[1] + point3[1] + point4[1]) / 4
                center_point = (center_x, center_y)

                if point_material_no_points == "1x":
                    point_material_points.append(center_point)  

                elif point_material_no_points == "2x":
                    center_x = (point1[0] + center_point[0]) / 2
                    center_y = (point1[1] + center_point[1]) / 2
                    center_point_1 = (center_x, center_y)
                    point_material_points.append(center_point_1)  


                    center_x = (point2[0] + center_point[0]) / 2
                    center_y = (point2[1] + center_point[1]) / 2
                    center_point_2 = (center_x, center_y)
                    point_material_points.append(center_point_2)  

                    
                    center_x = (point3[0] + center_point[0]) / 2
                    center_y = (point3[1] + center_point[1]) / 2
                    center_point_3 = (center_x, center_y)
                    point_material_points.append(center_point_3)  

                    
                    center_x = (point4[0] + center_point[0]) / 2
                    center_y = (point4[1] + center_point[1]) / 2
                    center_point_4 = (center_x, center_y)
                    point_material_points.append(center_point_4)  
        


        elif point_material_base_mesh_type == "TRIANGULAR":
            
            
            base_mesh =self.model_current_project.getModelsMeshsTriangular()[point_material_id_base_mesh]
        
            coordenates_triangles= base_mesh.getPoints()
            triangles= base_mesh.getTriangles()

            point_material_points =[]

            for triangle in triangles:
                point1  = coordenates_triangles[triangle[0]]
                point2  = coordenates_triangles[triangle[1]]
                point3  = coordenates_triangles[triangle[2]]

                center_x = (point1[0] + point2[0] + point3[0]) / 3
                center_y = (point1[1] + point2[1] + point3[1]) / 3
                center_point = (center_x, center_y)

                if point_material_no_points == "1x":
                    point_material_points.append(center_point)  

                elif point_material_no_points == "2x":
                    center_x = (point1[0] + (center_point[0]*2)) / 3
                    center_y = (point1[1] + (center_point[1]*2)) / 3
                    center_point_1 = (center_x, center_y)
                    point_material_points.append(center_point_1)  
                    center_x = (point2[0] + (center_point[0]*2)) / 3
                    center_y = (point2[1] + (center_point[1]*2)) / 3
                    center_point_2 = (center_x, center_y)
                    point_material_points.append(center_point_2)  
                    center_x = (point3[0] + (center_point[0]*2)) / 3
                    center_y = (point3[1] + (center_point[1]*2)) / 3
                    center_point_3 = (center_x, center_y)
                    point_material_points.append(center_point_3)  


                '''
                elif point_material_no_points == "2x":
                    center_x = (point1[0] + point2[0] + center_point[0]) / 3
                    center_y = (point1[1] + point2[1] + center_point[1]) / 3
                    center_point_1 = (center_x, center_y)
                    point_material_points.append(center_point_1)  
                    center_x = (point2[0] + point3[0] + center_point[0]) / 3
                    center_y = (point2[1] + point3[1] + center_point[1]) / 3
                    center_point_2 = (center_x, center_y)
                    point_material_points.append(center_point_2)  
                    center_x = (point3[0] + point1[0] + center_point[0]) / 3
                    center_y = (point3[1] + point1[1] + center_point[1]) / 3
                    center_point_3 = (center_x, center_y)
                    point_material_points.append(center_point_3)  
                '''



        
        id = self.model_current_project.createMaterialPoint(name=point_material_name ,
                                                    color=point_material_color,
                                                    points=point_material_points,
                                                    id_property = id_property
                                                    )
        model_point_material = self.model_current_project.getModelsPointsMaterials()[id]
        self.createPointsMaterialsCard(model_point_material)        
        self.setListPropertiesViews()

        self.view_menu_pointMaterial.endPointMaterial()

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(str)
    def deleteMaterialPoint(self, id):
        self.model_current_project.deleteMaterialPoint(id)
        for  controlled_card in self.list_controller_card:
            if controlled_card.id == id:
                self.list_controller_card.remove(controlled_card)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
   
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



    def setListPropertiesViews(self): 
        properties_data = []   
        property = self.model_current_project.getModelsProperties()
        for id_property in property:
            name = property[id_property].getName()
            properties_data.append([id_property, name])
        self.view_menu_pointMaterial.setListProperties(properties_data=properties_data)
        for controller_card in self.list_controller_card:
            controller_card.setListPropertiesViews(properties_data=properties_data)

    
    def setBaseMeshView(self, index=0):        
        self.view_menu_pointMaterial.setBaseMesh(index=index)
    
    def setListNoPointsView(self):  
        self.view_menu_pointMaterial.setListNoPoints()
    
    def setNoPointsView(self, index=0):        
        self.view_menu_pointMaterial.setNoPoints(index=index)
    
