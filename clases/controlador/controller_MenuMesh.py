
from PySide6.QtCore import (Slot, Signal, QObject,QPointF,QLineF)

from clases.Vista.view_WidgetDrawMenuMesh import ViewWidgetDrawMenuMesh
from clases.Modelo.model_Projects import ModelProjectCurrent
from clases.Controlador.controller_CardMesh import ControllerCardMesh
import pygmsh

class ControllerMenuMesh(QObject):

    signal_end_draw_geometry = Signal()
    signal_delete_mesh = Signal(str)
    signal_update_mesh = Signal(dict)

    signal_select_line_mesh= Signal() 
    signal_size_mesh= Signal() 
    signal_new_mesh= Signal(list) 
    

    def __init__(self) -> None:
        super().__init__()
        self.current_project = None
        self.meshs = []
        self.__selected_objects=[]
        #Crea la vista menu mesh
        self.view_menu_mesh = ViewWidgetDrawMenuMesh()

        self.view_menu_mesh.signal_end_draw_geometry.connect(self.signalEndDrawGeometry)
        self.view_menu_mesh.signal_select_line_mesh.connect(self.signalSelectLineMesh)
        self.view_menu_mesh.signal_size_mesh.connect(self.signalSizeMesh)
        self.view_menu_mesh.signal_new_mesh.connect(self.newMesh)


        return

        self.controller_PageDraw= controller_PageDraw
        self.name, self.path, self.data, self.hour = project.getData()

        self.view_card_project = ViewWidgetCardProjectHome(
                                                           cardName=self.name, 
                                                           cardPath=self.path, 
                                                           cardDataTime=self.data, 
                                                           cardHour=self.hour)
        
        self.view_card_project.signal_open_project.connect(self.openProject)
    
    
    
    def newMesh(self):

        name_mesh =self.view_menu_mesh.getNameNewMesh()
        color_mesh =self.view_menu_mesh.getcolorNewMesh()
        selected_objects = self.__selected_objects
        size_element_mesh = self.view_menu_mesh.getSizeNewMesh()
       

        # Validación de los datos de entrada
        print("&"*10000, "\n falalreviar el nom,bre quer no se repita")
        

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


        """
        #crea un area
        trianglePolygon = QPolygonF()
        for i in vertices:
            trianglePolygon.append(QPointF(i[0], i[1]))    
        pen= QPen(Qt.black)
        pen.setWidth(0)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(color_mesh))
        self.scene_draw.addPolygon(trianglePolygon,pen,brush)
        """



        # METODO MESHPY
        """
        # Define la geometría del dominio a mallar
        points = np.array([
            [30, 0],
            [32, 0],
            [32, 2],
            [30, 2]
        ])

        # Define las fronteras o límites del dominio
        facets = np.array([
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0]
        ])

        # Crea un objeto de mallado
        info = triangle.MeshInfo()

        # Define la geometría y las fronteras en el objeto de mallado
        info.set_points(points)
        info.set_facets(facets)   

        # Genera el mallado
        mesh = triangle.build(info, max_volume=0.25)

        # Accede a los resultados del mallado
        vertices = np.array(mesh.points)
        triangles = np.array(mesh.elements)


        print(vertices)
        print(triangles)


        trianglePolygon = QPolygonF()
        pen= QPen(color_mesh)

        for triangle_mesh in triangles:
            trianglePolygon.clear()
            vertex_1 = vertices[triangle_mesh[0]]
            vertex_2 = vertices[triangle_mesh[1]]
            vertex_3 = vertices[triangle_mesh[2]] 
            trianglePolygon.append( QPointF(vertex_1[0], vertex_1[1]))
            trianglePolygon.append(QPointF(vertex_2[0], vertex_2[1]))
            trianglePolygon.append(QPointF(vertex_3[0], vertex_3[1]))  
            pen.setWidth(0)
            self.scene_draw.addPolygon(trianglePolygon,pen)

        """
        #METODO PYGMSH
        with pygmsh.geo.Geometry() as geom:
            geom.add_polygon(
                vertices,
                mesh_size=size_element_mesh,
            )
            mesh = geom.generate_mesh()
 
        """

        triangleLine = QLineF()
        pen= QPen(Qt.yellow)
        for triangle_mesh in mesh.cells_dict["line"]:
            vertex_1 = mesh.points[triangle_mesh[0]]
            vertex_2 = mesh.points[triangle_mesh[1]] 
            triangleLine.setP1((QPointF(vertex_1[0], vertex_1[1])))
            triangleLine.setP2((QPointF(vertex_2[0], vertex_2[1])))
            pen.setWidth(0)
            self.scene_draw.addLine(triangleLine,pen)


        trianglePolygon = QPolygonF()
        pen= QPen(color_mesh)
        for triangle_mesh in mesh.cells_dict["triangle"]:
            trianglePolygon.clear()
            vertex_1 = mesh.points[triangle_mesh[0]]
            vertex_2 = mesh.points[triangle_mesh[1]]
            vertex_3 = mesh.points[triangle_mesh[2]] 
            trianglePolygon.append( QPointF(vertex_1[0], vertex_1[1]))
            trianglePolygon.append(QPointF(vertex_2[0], vertex_2[1]))
            trianglePolygon.append(QPointF(vertex_3[0], vertex_3[1]))  
            pen.setWidth(0)
            self.scene_draw.addPolygon(trianglePolygon,pen)


        """

        #METODO SCIPY
        """

        pen= QPen(Qt.red)
        # lista de vértices del polígono
        vertices_Scipy = [      
            
            [20, 0],
            [22, 0],
            [22, 2],
            [20, 2]
            ] 

        # calcular la triangulación de Delaunay
        tri = Delaunay(vertices_Scipy)


        # obtener los triángulos generados por la triangulación de Delaunay

        triangulos = tri.simplices
        points = tri.points
        print("MESH")
        print(points)
        print(triangulos)

        for triangle_mesh in triangulos:
            trianglePolygon.clear()
            vertex_1 = points[triangle_mesh[0]]
            vertex_2 = points[triangle_mesh[1]]
            vertex_3 = points[triangle_mesh[2]] 
            trianglePolygon.append( QPointF(vertex_1[0], vertex_1[1]))
            trianglePolygon.append(QPointF(vertex_2[0], vertex_2[1]))
            trianglePolygon.append(QPointF(vertex_3[0], vertex_3[1]))    


            pen.setWidth(0)
            self.scene_draw.addPolygon(trianglePolygon,pen)
        """       

        '''

        def configDrawMenuMesh(self):       

        for mesh in self.current_project.meshs:
            controller_card_mesh = ControllerCardMesh( mesh=mesh)
            self.view_menu_mesh.addCardMesh(controller_card_mesh.view_card_mesh)
            controller_card_mesh.signal_hide_show_mesh.connect(self.showHideMesh)
            controller_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
            controller_card_mesh.signal_update_mesh.connect(self.updateMesh)
        '''


        self.signal_new_mesh.emit([name_mesh, color_mesh, mesh.points, mesh.cells_dict["triangle"]])
        return
        card_mesh = view_WidgetCardMesh.viewCardDrawMesh(
                                            parent=self,
                                            scene_draw=self.scene_draw,
                                            points = mesh.points,
                                            triangles=mesh.cells_dict["triangle"],
                                            cardNameMesh="Mesh: {}".format(name_mesh),
                                            cardColorMesh = color_mesh,
                                            cardShowHideMesh = True)
        
        self.verticalLayout_containerCardMesh.addWidget(card_mesh)

        last_index = self.verticalLayout_containerCardMesh.count() - 1
        self.verticalLayout_containerCardMesh.insertWidget(last_index, self.frame_empty)

        self.lineEdit_textMesh1.setText("")
        self.lineEdit_textMesh2.setStyleSheet('background-color : #333333')
        self.lineEdit_textMesh5.setText("")
        self.doubleSpinBoxl_textMesh4.setValue(1)
        for item in self.__selected_objects:
            item.isSelectedMesh = False
        self.__selected_objects = []

        '''  
        Forma de agregar a un grid layout
        #projects = self.projects.getProjects()
        #positions = [(i,j) for i in range(5) for j in range(3)]
        #   for position, project in zip(positions, projects):
        #self.frame_home.gridLayout_proyectos.addWidget(self.cardProject,*position)
        '''
        
        """
        self.verticalLayout_containerCard.addWidget(cardProject)
        self.__list_view_card.append(cardProject)
        cardProject.signal_open_project.connect(self.__emitSignalOpen)
        """
        self.contador += 1
    
    
    
    def getView(self):
        return self.view_menu_mesh


    def setCurrentProject(self,current_project:ModelProjectCurrent):
        self.current_project = current_project


    def configDrawMenuMesh(self):      
        for mesh in self.current_project.meshs:
            self.createMeshCard(mesh)


    def createMeshCard(self, mesh):

        controller_card_mesh = ControllerCardMesh( mesh=mesh)
        self.view_menu_mesh.addCardMesh(controller_card_mesh.view_card_mesh)
        controller_card_mesh.signal_hide_show_mesh.connect(self.showHideMesh)
        controller_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        controller_card_mesh.signal_update_mesh.connect(self.updateMesh)


    @Slot()
    def signalSelectLineMesh(self):
        self.signal_select_line_mesh.emit()

    def selectLineMesh(self, no_lines, selected_objects):
        self.__selected_objects = selected_objects
        self.view_menu_mesh.selectLineMesh(no_lines)

    @Slot()
    def signalSizeMesh(self):
        self.signal_size_mesh.emit()

    def sizeMesh(self, dist):
        self.view_menu_mesh.sizeMesh(dist)

    @Slot(list)
    def showHideMesh(self, data):
       name_mesh = data[0]
       value = data[1]
       for mesh in self.meshs:
           
           if name_mesh == mesh.getName():
               mesh.setVisible(value)   


    @Slot(str)
    def deleteMesh(self, name):
        self.signal_delete_mesh.emit(name)

          
    @Slot(dict)
    def updateMesh(self, data):
        self.signal_update_mesh.emit(data)


    def setMeshs (self, meshs):
        self.meshs = meshs
        

    def addMeshs (self, mesh):
        self.meshs.append(mesh)


    def signalEndDrawGeometry(self):
        self.signal_end_draw_geometry.emit()

    
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
        
    ###############################################################################
	# ::::::::::::::::::::        OTROS MÉTODOS          ::::::::::::::::::::
	###############################################################################

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
