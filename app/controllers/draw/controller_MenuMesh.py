from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from views.draw.view_WidgetDrawMenuMesh import ViewWidgetDrawMenuMesh
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMesh import ControllerCardMesh
from utils.analysis.generate_mesh import MeshGenerator, ModelPolygon
from motorMPM.mesh import create_uniform
import pygmsh
import math
import time

meshg = MeshGenerator()

class ControllerMenuMesh(QObject):

    signal_new_mesh= Signal() 
    signal_edit_mesh= Signal() 
    signal_delete_mesh= Signal() 
    signal_end_draw_geometry = Signal()
    
    def __init__(self) -> None:
        super().__init__()
        

        self.view_menu_mesh = ViewWidgetDrawMenuMesh()
        self.model_current_project = None
        self.model_mesh_back = None
        self.list_controller_card=[]
        self.__config()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __config(self):
        self.setListTypeView()
        self.setTypeView()

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_mesh.signal_select_line_mesh.connect(self.signalSelectLineMesh)
        self.view_menu_mesh.signal_size_mesh.connect(self.signalSizeMesh)
        self.view_menu_mesh.signal_new_mesh.connect(self.newMesh)
        self.view_menu_mesh.signal_mesh_back_changed.connect(self.updateMeshBack)
        self.view_menu_mesh.signal_mesh_back_show.connect(self.showMeshBack)
        self.view_menu_mesh.signal_show_hide_meshs.connect(self.showHideMeshs)        
        self.view_menu_mesh.signal_show_hide_label.connect(self.showHideLabel)
        
        

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_current_project.signal_size_mesh.connect(self.sizeMesh)
        self.model_current_project.signal_select_line_mesh.connect(self.selectLineMesh)
        self.model_mesh_back = self.model_current_project.getModelMeshBack()

        
    def configDrawMenuMesh(self):
        
        data = self.model_mesh_back.getData()
        self.view_menu_mesh.setTextWidgetMeshBack(data=data)

        self.view_menu_mesh.removeCardMesh()
        self.list_controller_card=[]

        models_mesh = self.model_current_project.getModelsMeshsTriangular()
        for id_mesh in models_mesh:
            self.createMeshCard(models_mesh[id_mesh])

        models_mesh = self.model_current_project.getModelsMeshsQuadrilaterals()
        for id_mesh in models_mesh:
            self.createMeshCard(models_mesh[id_mesh])



    def getView(self):
        return self.view_menu_mesh

    def createMeshCard(self, model_mesh):
        controller_card_mesh = ControllerCardMesh( model_mesh = model_mesh)
        self.view_menu_mesh.addCardMesh(controller_card_mesh.view_card_mesh)
        controller_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        controller_card_mesh.signal_edit_mesh.connect(self.editMesh)

        self.list_controller_card.append(controller_card_mesh)
        self.signal_new_mesh.emit()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::
        
    @Slot(bool)
    def showHideMeshs(self, show_meshs):

        for controller in self.list_controller_card:
            controller.showHideMesh(show_meshs)
        
        	
    @Slot(bool)
    def showHideLabel(self, show_label):     
        for controller in self.list_controller_card:
            controller.showHideLabel(show_label)
        
        

    @Slot(bool)
    def showMeshBack(self, value):
        self.model_mesh_back.showHideMesh(value)

    @Slot(bool)
    def showMeshBackPoint(self, value):
        self.model_mesh_back.showMeshBackPoint(value)

    @Slot()
    def updateMeshBack(self):
        
        size_dx= self.view_menu_mesh.getMeshDx()
        size_dy= self.view_menu_mesh.getMeshDy()
        size_element= self.view_menu_mesh.getMeshBackSize()
        color= self.view_menu_mesh.getColor()

        resul_x = abs(size_dx/size_element - round(size_dx/size_element)) 
        resul_y = abs(size_dy/size_element - round(size_dy/size_element)) 
        
        if resul_x > 1e-11:
            msn = "No elementos no se ajusta en X"
            self.view_menu_mesh.msnAlert(True, msn)
            return 
        if resul_y > 1e-11:
            msn = "No elementos no se ajusta en Y"
            self.view_menu_mesh.msnAlert(True, msn)
            return 
        
        
        


        '''
            def create_uniform(dimx, dimy, ele_size):
        """ Funcion que crea una malla regular uniforme de ancho dimx por dimy
            Elementos cuadrilaterals bilineales
            dimx = ancho en x 
            dimy = ancho en y
            ele_size = Tamano de los elementos"""   
        #======= Instrucciones para el calculo de tabla de coordenadas ========

        coord = None
        inci = None
        nelex = None
        error = False

        nelex = int(round(dimx / ele_size)) ; neley = int(round(dimy / ele_size))

        if abs(dimx/ele_size - round(dimx/ele_size)) > 1e-11:
            print("El numero de elementos no se ajusta en la direccion x")
            error= True
            return coord ,inci ,nelex, error
        if abs(dimy/ele_size - round(dimy/ele_size)) > 1e-11:
            print("El numero de elementos no se ajusta en la direccion y")
            error= True
            return coord ,inci ,nelex, error

        assert (abs(dimx/ele_size - round(dimx/ele_size)) < 1e-11), "El numero de elementos no se ajusta en la direccion x"
        assert (abs(dimy/ele_size - round(dimy/ele_size))< 1e-11), "El numero de elementos no se ajusta en la direccion y"
            
        '''


        mesh_cuad_coord, mesh_cuad_inci, mesh_cuad_nelex, error = create_uniform(size_dx,size_dy,size_element)


        

        nnodesx = int(mesh_cuad_nelex + 1)
        nnodesy = int(len(mesh_cuad_coord) / nnodesx)
        count=0
        points_boundary_top = []
        points_boundary_bottom = []        
        points_boundary_left = []
        points_boundary_right = []        
        nodes_boundary_top = []
        nodes_boundary_bottom = []        
        nodes_boundary_left = []
        nodes_boundary_right = []

        for y in range(nnodesy):
            for x in range(nnodesx):
                coor_boundary = mesh_cuad_coord[count].tolist()
                if y==0:
                    points_boundary_bottom.append(coor_boundary)
                    nodes_boundary_bottom.append(count + 1)
                if y==nnodesy-1:
                    points_boundary_top.append(coor_boundary)
                    nodes_boundary_top.append(count + 1)
                if x==0:
                    points_boundary_left.append(coor_boundary)
                    nodes_boundary_left.append(count + 1)
                if x==nnodesx-1:
                    points_boundary_right.append(coor_boundary)
                    nodes_boundary_right.append(count + 1)

                count +=1
                

        if error:            
            return

        points =[]
        for point in mesh_cuad_coord:
            points.append([point[0],point[1]])  

        quadrilaterals =[] 
        for triangle in mesh_cuad_inci:
            quadrilaterals.append([int(triangle[0]),int(triangle[1]),int(triangle[2]),int(triangle[3])])
        
        

        self.model_mesh_back.updateMesh(size_dx=size_dx,
                                        size_dy=size_dy,
                                        size_element=size_element,
                                        color=color,
                                        points=points,
                                        quadrilaterals=quadrilaterals,
                                        points_boundary_top = points_boundary_top,
                                        points_boundary_bottom = points_boundary_bottom,
                                        points_boundary_left = points_boundary_left,
                                        points_boundary_right = points_boundary_right,
                                        nodes_boundary_top = nodes_boundary_top,
                                        nodes_boundary_bottom = nodes_boundary_bottom,
                                        nodes_boundary_left = nodes_boundary_left,
                                        nodes_boundary_right = nodes_boundary_right
                                        )
        
        msn = "Malla Actualizada"
        self.view_menu_mesh.msnAlert(False, msn)
    

     
    
    @Slot()
    def signalSelectLineMesh(self):
        self.signalEndDrawGeometry()
        self.model_current_project.commandMeshSelectLine({"step":1, "data":None}) 
    
    @Slot()
    def signalSizeMesh(self):
        self.signalEndDrawGeometry()
        self.model_current_project.commandMeshSize({"step":1, "data":None}) 

    @Slot()
    def newMesh(self):

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
            """             
            points, quadrilaterals, n_element = self.generate_mesh_quadrilateral(
                polygon= polygon,
                mesh_size=size_element_mesh
                )
            """            
            
            meshg.add_polygon(
                polygon= ModelPolygon(points=polygon, mesh_size=size_element_mesh)
            )
            points, quadrilaterals, n_element = meshg.generate_mesh_quadrilateral()

    


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
    def selectLineMesh(self, no_lines):
        self.view_menu_mesh.setNoSelectLineMesh(no_lines)

    @Slot(float)
    def sizeMesh(self, dist):
        self.view_menu_mesh.setSizeMesh(dist)
        self.signalEndDrawGeometry()

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(list)
    def deleteMesh(self, data):
        type_mesh =data[0]
        id =data[1]

        if type_mesh == "TRIANGLE":
            self.model_current_project.deleteMeshTriangular(id)
            
        elif type_mesh == "QUADRILATERAL":
            self.model_current_project.deleteMeshQuadrilaterals(id)
        
        self.signal_delete_mesh.emit()
        
    @Slot()
    def editMesh(self):
        self.signal_edit_mesh.emit()
	




    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def endDrawMesh(self):
        self.model_current_project.endMeshSelectLine()
        self.selectLineMesh(0)
        self.view_menu_mesh.setPropertyStyle(self.view_menu_mesh.toolButton_cardMeshDrawSize, 1)

    def signalEndDrawGeometry(self):
        self.signal_end_draw_geometry.emit()

    def setListTypeView(self):  
        self.view_menu_mesh.setListTypes()
    
    def setTypeView(self, index=0):        
        self.view_menu_mesh.setType(index=index)

    ###############################################################################
	# ::::::::::::::::::::           OTROS MÉTODOS             ::::::::::::::::::::
	###############################################################################
    
    def is_closed_polygon(self, lines:list):
        "devuelve poligono cerrado anti horario"

        polygon = []
        current_line = lines.pop(0)
        
        star_point = current_line[0]
        end_point = current_line[1]
        polygon.append(tuple(current_line))        

        while True:

            if len(lines) <= 0:
                break

            index = 0
            joined_lines = False

            for line in lines:
                p1 = line[0]
                p2 = line[1]
             
                if p1 == end_point:
                    current_line = line
                    lines.pop(index)
                    star_point = p1
                    end_point = p2
                    polygon.append((star_point,end_point))
                    joined_lines = True
                    break
            
                elif  p2 == end_point:
                    current_line = line
                    lines.pop(index)
                    star_point = p2
                    end_point = p1
                    polygon.append((star_point,end_point))
                    joined_lines = True
                    break
                index += 1

            if not joined_lines:
                return False
        
        polygon_star_point = polygon[0][0]
        polygon_end_point = polygon[-1][-1]

        if polygon_star_point ==polygon_end_point:
            return polygon
        else:
            return False
        

    def line_Intersection(self, polygon):
        len_lines = len(polygon)
        linesF = []
        for line in polygon:
            p1=QPointF(line[0][0], line[0][1])
            p2=QPointF(line[1][0], line[1][1])
            linesF.append(QLineF(p1, p2 ))
            
        new_list_line=[]
        while True:
            line_ref = linesF[-1]
            linesF.pop(-1)   
            for line in linesF:
                intersection_type, intersection_point = line_ref.intersects(line)
                #print("TIpo:",intersection_type, intersection_point)               
                if intersection_type == QLineF.IntersectionType.BoundedIntersection:
                    if line_ref.p1()!=intersection_point and line_ref.p2()!=intersection_point and  line.p1()!=intersection_point and line.p2()!=intersection_point:
                    
                        return True
            new_list_line.append(line_ref)
            if len(linesF)==0:
                return False


    def generate_mesh_quadrilateral(self, polygon, mesh_size):     
       
        line_A = polygon[0]
        line_B = polygon[1]
        line_AA = polygon[2]
        line_BB = polygon[3]

        # puntos lineas A
        pA1 = line_A[0]
        pA2 = line_A[1]
        dist_A = math.sqrt((pA2[0] - pA1[0])**2 + (pA2[1] - pA1[1])**2)

        pAA1 = line_AA[0]
        pAA2 = line_AA[1]
        dist_AA = math.sqrt((pAA2[0] - pAA1[0])**2 + (pAA2[1] - pAA1[1])**2)

        if dist_A >= dist_AA:
            dist_A_max = dist_A
        else:
            dist_A_max = dist_AA
        parts_A = int(dist_A_max/mesh_size)


        # puntos lineas B
        pB1 = line_B[0]
        pB2 = line_B[1]
        dist_B = math.sqrt((pB2[0] - pB1[0])**2 + (pB2[1] - pB1[1])**2)

        pBB1 = line_BB[0]
        pBB2 = line_BB[1]
        dist_BB = math.sqrt((pBB2[0] - pBB1[0])**2 + (pBB2[1] - pBB1[1])**2)

        if dist_B >= dist_BB:
            dist_B_max = dist_B
        else:
            dist_B_max = dist_BB
            
        parts_B = int(dist_B_max/mesh_size)

     

        result_A = self.divide_line(line_A, parts_A)
        result_B = self.divide_line(line_B, parts_B)
        result_AA = self.divide_line(line_AA, parts_A)
        result_BB = self.divide_line(line_BB, parts_B)

        result_AA.reverse()
        result_BB.reverse()



        # genera la lista de puntos 
        points = []
        print("len: ",len(result_A), len(result_B), len(result_AA), len(result_BB))
        #len:  5 4 5 4
        for i in range(0, len(result_B)):            
            result_A_i = self.divide_line([result_BB[i],result_B[i]], parts_A)

            for point in result_A_i:
                points.append(point)


        quadrilaterals = []
        na = parts_A
        nb = parts_B
        for b in range(0, nb): #3
            sum_row = (na +1 ) * b
            for a in range(0, na): #1      
                vertex_1 = (a)          + sum_row
                vertex_2 = (a + 1)      + sum_row
                vertex_3 = (a + 1)      + sum_row   + (na+1)
                vertex_4 = (a)          + sum_row   + (na+1)

                quadrilaterals.append([vertex_1,vertex_2,vertex_3,vertex_4])
        
        n_element = len(quadrilaterals)
        return points, quadrilaterals, n_element
    
    
    

    def divide_line(self, line, parts):
        x1, y1 = line[0]
        x2, y2 = line[1]
        
        # Calcula la distancia entre los puntos
        dx = (x2 - x1) / parts
        dy = (y2 - y1) / parts
        
        # Calcula las coordenadas de la división
        coordinates = []
        for i in range(parts + 1):
            x = x1 + dx * i
            y = y1 + dy * i
            coordinates.append([x, y])
        
        return coordinates


