from PySide6.QtCore import (Slot)
from clases.Vista.view_WidgetDrawMenuPointMaterial import ViewWidgetDrawMenuPointMaterial
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardMaterialPoint import ControllerCardMaterialPoint

class ControllerMenuPointMaterial():

    def __init__(self) -> None:

        self.view_menu_pointMaterial = ViewWidgetDrawMenuPointMaterial()
        self.list_controller_card=[]

        self.__config()
        self.__initEvent()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __config(self):
        '''
        self.setListBaseMeshView()
        self.setBaseMeshView()
        '''
        self.setListNoPointsView()
        self.setNoPointsView()

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_pointMaterial.signal_new_points_material.connect(self.newPointsMaterial)


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
   

    @Slot(str)
    def deleteMaterialPoint(self, id):
        self.model_current_project.deleteMaterialPoint(id)

    @Slot()
    def newPointsMaterial(self):

        point_material_name = self.view_menu_pointMaterial.getName()
        point_material_color = self.view_menu_pointMaterial.getColor()
        point_material_id_base_mesh, point_material_base_mesh = self.view_menu_pointMaterial.getBaseMesh()
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
        
    
        
        if point_material_no_points == "":
            self.view_menu_pointMaterial.msnAlertNoPoints(True, "Selecciona la cantidad de puntos por elemento")
            return     
        else:
            self.view_menu_pointMaterial.msnAlertNoPoints(False)
        

        base_mesh =self.model_current_project.getModelsMeshs()[point_material_id_base_mesh]

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

      

        point_material_name 
        point_material_color 
        point_material_base_mesh 
        point_material_no_points 
        point_material_points


        print("#SE CREAR LOS MODELOS DE PUNTOS EN EL MODELO DE PROYECTO ACTUAL,")
        print("# LUEDO SE PASA POR EL ADMIN QUIN CARGA A LA SCENE y LA BD")

        # 1) Se le dice al ProjectCurrent que debe crear una MP y se le pasa los cuatro datos
        #        el modelo intanaciado lo guarda en una lista
        # 2) el crea un Modelo de pointMaterial,
        #           se guarda la info como argumentos,
        #           se debe guardar la infor en la bd
        #           se crea el itemQGRAPHICS y se agrega a la scena
        #card?
        #admin?
        # 3) el modelo de MP 








        id = self.model_current_project.createMaterialPoint(name=point_material_name ,
                                                    color=point_material_color,
                                                    points=point_material_points)
        model_point_material = self.model_current_project.getModelsPointsMaterials()[id]
        self.createPointsMaterialsCard(model_point_material)

        self.view_menu_pointMaterial.endPointMaterial()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    
    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project

    def configDrawMenuPointMaterial(self):
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        for id_point_material in models_points_materials:
            self.createPointsMaterialsCard(models_points_materials[id_point_material])        
        self.setListBaseMeshView()




        

    def createPointsMaterialsCard(self, model_point_material):
        controller_card_material_point = ControllerCardMaterialPoint( model_point_material=model_point_material)
        self.view_menu_pointMaterial.addCardMaterialPoint(controller_card_material_point.view_card_material_point)
        controller_card_material_point.signal_delete_material_point.connect(self.deleteMaterialPoint)

        self.list_controller_card.append(controller_card_material_point)

    def getView(self):
        return self.view_menu_pointMaterial


    def setListBaseMeshView(self):  
        mesh_data = []   
        meshs = self.model_current_project.getModelsMeshs()
        for id_mesh in meshs:
            name = meshs[id_mesh].getName()
            color = meshs[id_mesh].getColor()
            mesh_data.append([id_mesh, name, color])
        self.view_menu_pointMaterial.setListBaseMesh(mesh_data=mesh_data)
    
    def setBaseMeshView(self, index=-1):        
        self.view_menu_pointMaterial.setBaseMesh(index=index)
    
    def setListNoPointsView(self):  
        self.view_menu_pointMaterial.setListNoPoints()
    
    def setNoPointsView(self, index=-1):        
        self.view_menu_pointMaterial.setNoPoints(index=index)
    
