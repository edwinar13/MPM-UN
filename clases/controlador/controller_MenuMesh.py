from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)

from clases.Vista.view_WidgetDrawMenuMesh import ViewWidgetDrawMenuMesh
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardMesh import ControllerCardMesh
import pygmsh

class ControllerMenuMesh(QObject):

    signal_end_draw_geometry = Signal()
    '''
    signal_delete_mesh = Signal(str)
    signal_update_mesh = Signal(dict)

    '''
    signal_new_mesh= Signal() 
    signal_select_line_mesh= Signal() 
    signal_size_mesh= Signal() 
    

    def __init__(self) -> None:
        super().__init__()


        self.view_menu_mesh = ViewWidgetDrawMenuMesh()
        self.list_controller_card=[]
        '''
        self.__selected_objects=[]
        '''
        self.__initEvent()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_mesh.signal_select_line_mesh.connect(self.signalSelectLineMesh)
        self.view_menu_mesh.signal_size_mesh.connect(self.signalSizeMesh)
        self.view_menu_mesh.signal_new_mesh.connect(self.newMesh)


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################

    

    @Slot(str)
    def deleteMesh(self, id):
        self.model_current_project.deleteMeshTriangular(id)

    #FALTA DESDE ACA

    @Slot()
    def newMesh(self):

        name_mesh =self.view_menu_mesh.getName()
        color_mesh =self.view_menu_mesh.getColor()
        selected_objects = self.model_current_project.getSelectedObjects()      
        size_element_mesh = self.view_menu_mesh.getSize()
       
  
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


         
        id = self.model_current_project.createMesh(name=name_mesh ,
                                                    color=color_mesh,
                                                    points=points,
                                                    triangles = triangles)
        model_mesh = self.model_current_project.getModelsMeshs()[id]
        self.createMeshCard(model_mesh)

        self.view_menu_mesh.endMesh()
        self.endDrawMesh()
        
     
    @Slot()
    def signalSelectLineMesh(self):
        self.model_current_project.commandMeshSelectLine({"step":1, "data":None}) 

    @Slot(int)
    def selectLineMesh(self, no_lines):
        self.view_menu_mesh.setNoSelectLineMesh(no_lines)
        #self.signalEndDrawGeometry()
    '''
        print(no_lines)
        selected_objects = self.controller_graphics_draw.getSelectedObjects()
        self.controller_menu_mesh.selectLineMesh(no_lines, selected_objects)

    def selectLineMesh(self, no_lines, selected_objects):
        self.__selected_objects = selected_objects
        self.view_menu_mesh.selectLineMesh(no_lines)
    '''


    @Slot()
    def signalSizeMesh(self):
        self.model_current_project.commandMeshSize({"step":1, "data":None}) 


    @Slot(float)
    def sizeMesh(self, dist):
        self.view_menu_mesh.setSizeMesh(dist)
        self.signalEndDrawGeometry()



    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################


    def configDrawMenuMesh(self):   
        
        models_mesh = self.model_current_project.getModelsMeshs()
        for id_mesh in models_mesh:
            self.createMeshCard(models_mesh[id_mesh])

    def createMeshCard(self, model_mesh):
        controller_card_mesh = ControllerCardMesh( model_mesh = model_mesh)
        self.view_menu_mesh.addCardMesh(controller_card_mesh.view_card_mesh)
        controller_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        self.list_controller_card.append(controller_card_mesh)
        self.signal_new_mesh.emit()

    def getView(self):
        return self.view_menu_mesh

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_current_project.signal_size_mesh.connect(self.sizeMesh)
        self.model_current_project.signal_select_line_mesh.connect(self.selectLineMesh)
        

    def endDrawMesh(self):
        self.model_current_project.endMeshSelectLine()
        self.selectLineMesh(0)

    #FALTA DESDE ACA




    def setMeshs (self, meshs):
        self.meshs = meshs
        
    def addMeshs (self, mesh):
        self.meshs.append(mesh)

    def signalEndDrawGeometry(self):
        self.signal_end_draw_geometry.emit()
    
    ###############################################################################
	# ::::::::::::::::::::        OTROS MÉTODOS          ::::::::::::::::::::
	###############################################################################
    
    def is_closed_polygon(self, lines:list):

        polygon = []
        current_line = lines.pop(0)
        star_point = current_line[0]
        end_point = current_line[1]
        polygon.append(current_line)        

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





