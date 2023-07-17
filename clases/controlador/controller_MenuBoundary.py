from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from clases.Vista.view_WidgetDrawMenuBoundary import ViewWidgetDrawMenuBoundary
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardBoundary import ControllerCardBoundary

class ControllerMenuBoundary(QObject):

    signal_end_draw_geometry = Signal()

    def __init__(self) -> None:
        super().__init__()
        #Crea la vista menu Boundary
        self.view_menu_boundary = ViewWidgetDrawMenuBoundary()
        self.model_current_project = None
        self.list_controller_card=[]

        self.__initEvent()
        self.showHideBoundaries(False)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################


    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_boundary.signal_select_point_mesh.connect(self.signalSelectPointMesh)
        self.view_menu_boundary.signal_new_boundary_automatic.connect(self.newBoundaryAutomatic)
        self.view_menu_boundary.signal_new_boundary_manual.connect(self.newBoundaryManual)
        self.view_menu_boundary.signal_show_hide_boundaries.connect(self.showHideBoundaries)        
        self.view_menu_boundary.signal_show_hide_labels.connect(self.showHideLabels)
        

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project        
        self.model_current_project.signal_select_point_back.connect(self.selectPointMesh)

        

    def configDrawMenuBoundary(self):
        
        self.view_menu_boundary.removeCardBoundary()
        self.list_controller_card=[]

        models_boundaries = self.model_current_project.getModelsBoundaries()
        for id_boundary in models_boundaries:
            self.createBoundaryCard(models_boundaries[id_boundary])

        
    def getView(self):
        return self.view_menu_boundary


    def createBoundaryCard(self, model_boundary):
        controller_card_boundary = ControllerCardBoundary( model_boundary = model_boundary)
        self.view_menu_boundary.addCardBoundary(controller_card_boundary.view_card_boundary)
        controller_card_boundary.signal_delete_boundary.connect(self.deleteBoundary)
        self.list_controller_card.append(controller_card_boundary)




    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::

      
    @Slot(bool)
    def showHideBoundaries(self, show_boundaries):

        for controller in self.list_controller_card:
            controller.showHideBoundary(show_boundaries)
        
        	
    @Slot(bool)
    def showHideLabels(self, show_label):     
        for controller in self.list_controller_card:
            controller.showHideLabels(show_label)

    @Slot()
    def signalSelectPointMesh(self):
        self.signalEndDrawGeometry()
        self.model_current_project.commandMeshSelectLine({"step":1, "data":None}) 
        self.model_current_project.commandBoundarySelectPoint({"step":1, "data":None}) 

  

    @Slot()
    def newBoundaryAutomatic(self):
        restriction_automatic = self.view_menu_boundary.getTxTyAutomatic()

        restriction_automatic_top = restriction_automatic["Top"]
        restriction_automatic_bottom = restriction_automatic["Bottom"]
        restriction_automatic_left = restriction_automatic["Left"]
        restriction_automatic_right = restriction_automatic["Right"]       

        points_top, points_bottom ,points_left ,points_right = self.model_current_project.getBoundaryMeshBack()

        if  restriction_automatic_top[0] or restriction_automatic_top[1]:        
            id_top= self.model_current_project.createBoundary(
                                                        name ="boundary_top",
                                                        points = points_top,
                                                        restrictionX = restriction_automatic_top[0],
                                                        restrictionY = restriction_automatic_top[1]                                                    
                                                        )
            model_boundary_top = self.model_current_project.getModelsBoundaries()[id_top]
            self.createBoundaryCard(model_boundary_top)
            

        if  restriction_automatic_bottom[0] or restriction_automatic_bottom[1]:
            id_bottom = self.model_current_project.createBoundary(
                                                        name ="boundary_bottom",
                                                        points = points_bottom,
                                                        restrictionX = restriction_automatic_bottom[0],
                                                        restrictionY = restriction_automatic_bottom[1]                                                    
                                                        )
            model_boundary_bottom = self.model_current_project.getModelsBoundaries()[id_bottom]
            self.createBoundaryCard(model_boundary_bottom)

        if  restriction_automatic_left[0] or restriction_automatic_left[1]:
            id_left = self.model_current_project.createBoundary(
                                                        name ="boundary_left",
                                                        points = points_left,
                                                        restrictionX = restriction_automatic_left[0],
                                                        restrictionY = restriction_automatic_left[1]                                                    
                                                        )
            model_boundary_left = self.model_current_project.getModelsBoundaries()[id_left]
            self.createBoundaryCard(model_boundary_left)
                        
        if  restriction_automatic_right[0] or  restriction_automatic_right[1]:
            id_right = self.model_current_project.createBoundary(
                                                        name ="boundary_right",
                                                        points = points_right,
                                                        restrictionX = restriction_automatic_right[0],
                                                        restrictionY = restriction_automatic_right[1]                                                    
                                                        )
            

            model_boundary_right = self.model_current_project.getModelsBoundaries()[id_right]
            self.createBoundaryCard(model_boundary_right)

        self.view_menu_boundary.endBoundary1()
        self.endDrawBoudary()


    @Slot()
    def newBoundaryManual(self):
        return

        name_mesh =self.view_menu_mesh.getName()
        color_mesh =self.view_menu_mesh.getColor()
        selected_objects = self.model_current_project.getSelectedObjects()      
        size_element_mesh = self.view_menu_mesh.getSize()
        type_mesh = self.view_menu_mesh.getType()
         
        if name_mesh == "":
            self.view_menu_mesh.msnAlertName(True, "Revisa el nombre  de la malla")
            return     
        else:
            self.view_menu_mesh.msnAlertName(False)

        if color_mesh == None:
            self.view_menu_mesh.msnAlertColor(True, "Revisa el color de la malla")
            return               
        else:
            self.view_menu_mesh.msnAlertColor(False)
            

        if len(selected_objects) < 3 :
            self.view_menu_mesh.msnAlertSelected(True, "Selecciona más de 3 elementos")
            return
        else:
            self.view_menu_mesh.msnAlertSelected(False)

        # Validación de las líneas seleccionadas
        lines = []
        for line in selected_objects:
            lines.append(
            ((line.start_point.pos().x(), line.start_point.pos().y()),
            (line.end_point.pos().x(), line.end_point.pos().y()))
            )

        polygon = self.is_closed_polygon(lines)
        if not polygon:
            self.view_menu_mesh.msnAlertSelected(True, "Selección no es un polígono cerrado")
            return
        else:
            self.view_menu_mesh.msnAlertSelected(False)

        isIntercepted = self.line_Intersection(polygon)
        if isIntercepted:
            self.view_menu_mesh.msnAlertSelected(True, "Dos líneas se interceptan")
            return
        else:
            self.view_menu_mesh.msnAlertSelected(False)



        
        if type_mesh == "Cuadrilátera" and not len(selected_objects) == 4 :
            self.view_menu_mesh.msnAlertSelected(True, "Para Cuadrilátera únicamente 4 líneas ")
            return
        else:
            self.view_menu_mesh.msnAlertSelected(False)
        


        if type_mesh == "Cuadrilátera":
 
            points, quadrilaterals, n_element = self.generate_mesh_quadrilateral(
                polygon= polygon,
                mesh_size=size_element_mesh
                )

            mesh_points =[]
            for point in points:
                mesh_points.append([point[0],point[1]]) 
  
            mesh_quadrilaterals =[] 

            for quadrilaterals in quadrilaterals:
                mesh_quadrilaterals.append([int(quadrilaterals[0]),int(quadrilaterals[1]),int(quadrilaterals[2]),int(quadrilaterals[3])])


            id = self.model_current_project.createMeshQuadrilateral(name=name_mesh ,
                                                        color=color_mesh,
                                                        points=mesh_points,
                                                        quadrilaterals = mesh_quadrilaterals)
            model_mesh = self.model_current_project.getModelsMeshsQuadrilaterals()[id]
            self.createMeshCard(model_mesh)

            self.view_menu_mesh.endMesh()
            self.endDrawMesh()
            

        elif type_mesh == "Triangular":
             
            vertices = []
            for line in polygon:
                vertices.append(line[0])    

            #METODO PYGMSH
            with pygmsh.geo.Geometry() as geom:
                geom.add_polygon(
                    vertices,
                    mesh_size=size_element_mesh,
                )
                mesh = geom.generate_mesh()
        
            _points = mesh.points  
            points =[]
            for point in _points:
                points.append([point[0],point[1]])  
    
            _triangles = mesh.cells_dict["triangle"]
            triangles =[] 
            for triangle in _triangles:
                triangles.append([int(triangle[0]),int(triangle[1]),int(triangle[2])])
                
               
            id = self.model_current_project.createMeshTriangular(name=name_mesh ,
                                                        color=color_mesh,
                                                        points=points,
                                                        triangles = triangles)
            model_mesh = self.model_current_project.getModelsMeshsTriangular()[id]
            self.createMeshCard(model_mesh)

            self.view_menu_mesh.endMesh()
            self.endDrawMesh()

    # ::::::::::::::::::::         MÉTODOS  CURRENT        ::::::::::::::::::::
	
    @Slot(int)
    def selectPointMesh(self, no_points):
        self.view_menu_boundary.setNoSelectPointsMesh(no_points)

    

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(str)
    def deleteBoundary(self, id):
        self.model_current_project.deleteBoundary(id)
        


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################



    def endDrawBoudary(self):
        self.model_current_project.endBoundarySelectPoint()
        self.selectPointMesh(0)


    def signalEndDrawGeometry(self):
            self.signal_end_draw_geometry.emit()