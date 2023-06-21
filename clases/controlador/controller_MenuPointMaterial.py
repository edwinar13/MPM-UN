

from clases.Vista.view_WidgetDrawMenuPointMaterial import ViewWidgetDrawMenuPointMaterial
 
class ControllerMenuPointMaterial():

    def __init__(self) -> None:

        #Crea la vista menu PointMaterial
        self.view_menu_pointMaterial = ViewWidgetDrawMenuPointMaterial()

        self.setListBaseMeshView()
        self.setBaseMeshView()

        self.setListNoPointsView()
        self.setNoPointsView()


        self.view_menu_pointMaterial.signal_new_points_material.connect(self.newPointsMaterial)


        
    def getView(self):
        return self.view_menu_pointMaterial
    
    def setListBaseMeshView(self):        
        mesh_name = ["malla 1","malla 2","malla 3"]
        mesh_color = ["#236596","#968698","#ff5865"]
        self.view_menu_pointMaterial.setListBaseMesh(mesh_name=mesh_name, mesh_color=mesh_color)
    
    def setBaseMeshView(self, index=-1):        
        self.view_menu_pointMaterial.setBaseMesh(index=index)
    

    def setListNoPointsView(self):  
        self.view_menu_pointMaterial.setListNoPoints()

    
    def setNoPointsView(self, index=-1):        
        self.view_menu_pointMaterial.setNoPoints(index=index)
    

    def newPointsMaterial(self):
        point_material_name = self.view_menu_pointMaterial.getName()
        point_material_color = self.view_menu_pointMaterial.getColor()
        point_material_base_mesh = self.view_menu_pointMaterial.getBaseMesh()
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



        # se agrega la card



        self.view_menu_pointMaterial.endPointMaterial()