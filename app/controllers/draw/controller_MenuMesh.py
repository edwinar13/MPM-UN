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
    signal_delete_all_boundary = Signal()
    
    signal_cancel_select = Signal()
    
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
        self.view_menu_mesh.signal_size_mesh.connect(self.signalSizeMesh)
        self.view_menu_mesh.signal_new_mesh.connect(self.newMesh)
        self.view_menu_mesh.signal_mesh_back_changed.connect(self.updateMeshBack)
        self.view_menu_mesh.signal_mesh_back_show.connect(self.showMeshBack)
        self.view_menu_mesh.signal_show_hide_meshs.connect(self.showHideMeshs)        
        self.view_menu_mesh.signal_show_hide_label.connect(self.showHideLabel)
        self.view_menu_mesh.signal_show_hide_label_point.connect(self.showMeshBackPoint)
        
        self.view_menu_mesh.signal_select_line_mesh.connect(self.signalSelectLineMesh)
        self.view_menu_mesh.signal_cancel_select.connect(self.signalCancelSelect)
        

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
        controller_card_mesh = ControllerCardMesh( model_mesh = model_mesh,
                                                  model_current_project=self.model_current_project
                                                  )
        self.view_menu_mesh.addCardMesh(controller_card_mesh.view_card_mesh)
        controller_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        controller_card_mesh.signal_edit_mesh.connect(self.editMesh)
        controller_card_mesh.signal_msn.connect(self.msnAlertDefault)

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
        """Oculta o muestra la malla de fondo."""
        self.model_mesh_back.showHideMesh(value)
                
    @Slot(bool)
    def showMeshBackPoint(self, value):
        self.model_mesh_back.showMeshBackPoint(value)

    @Slot()
    def updateMeshBack(self):
        """Actualiza la malla de fondo."""
        
        size_dx= self.view_menu_mesh.getMeshDx()
        size_dy= self.view_menu_mesh.getMeshDy()
        size_element= self.view_menu_mesh.getMeshBackSize()

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
        
        # Genera la malla, los nodos y elemtos devueltos van de izq a derecha y de abajo hacia arriba
        # los nodos de lso elementos se numeran en sentido antihorario
        mesh_cuad_coord, mesh_cuad_inci, mesh_cuad_nelex, error = create_uniform(size_dx,size_dy,size_element)

        
        # nodos
        nodes ={}
        index = 1
        for node in mesh_cuad_coord:
            nodes[f'NODE#{index}'] = {'COORDINATES':[node[0],node[1]]}             
            index +=1

        elements ={}
        index = 1
        for element in mesh_cuad_inci:
            elements[f'ELEMENT#{index}'] = [
                            f'NODE#{element[0]}',
                            f'NODE#{element[1]}',
                            f'NODE#{element[2]}',
                            f'NODE#{element[3]}'    
                        ]
            index +=1

        # nodos en los bordes
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
                    nodes_boundary_bottom.append("NODE#"+str(count + 1))
                if y==nnodesy-1:
                    points_boundary_top.append(coor_boundary)
                    nodes_boundary_top.append("NODE#"+str(count + 1))
                if x==0:
                    points_boundary_left.append(coor_boundary)
                    nodes_boundary_left.append("NODE#"+str(count + 1))
                if x==nnodesx-1:
                    points_boundary_right.append(coor_boundary)
                    nodes_boundary_right.append("NODE#"+str(count + 1))

                count +=1
        if error:            
            return
        self.model_mesh_back.updateMesh(size_dx=size_dx,
                                        size_dy=size_dy,
                                        size_element=size_element,
                                        nodes=nodes,
                                        elements=elements,
                                        nodes_boundary_top = nodes_boundary_top,
                                        nodes_boundary_bottom = nodes_boundary_bottom,
                                        nodes_boundary_left = nodes_boundary_left,
                                        nodes_boundary_right = nodes_boundary_right
                                        )
        self.signal_delete_all_boundary.emit()
        msn = "Malla Actualizada"
        self.view_menu_mesh.msnAlert(False, msn)
    

     
    
    @Slot()
    def signalSelectLineMesh(self):
        self.signalEndDrawGeometry()
        self.model_current_project.commandMeshSelectLine({"step":1, "data":None}) 
    
    @Slot()
    def signalCancelSelect(self):
        self.signal_cancel_select.emit()
        self.endDrawMesh()
    
    
    
    
    
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
        path_file = self.view_menu_mesh.getPathFile()
        
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
        
        
        if type_mesh == "Archivo":
            if path_file == "":                
                self.view_menu_mesh.msnAlertFile(True, "Seleciona un archivo")
                return
            else:                
                self.newMeshFile(name_mesh, color_mesh, path_file)
            
        else:
            if len(selected_objects) == 0:
                self.view_menu_mesh.msnAlertSelected(True, "Selecciona elementos para la malla")
                return
            else:
                self.view_menu_mesh.msnAlertSelected(False)
                
            if type_mesh == "Triangular":
                self.newMeshTriangular(name_mesh, color_mesh, selected_objects, size_element_mesh, type_mesh)

            elif type_mesh == "Cuadrilátera":
                self.newMeshQuadrilateral(name_mesh, color_mesh, selected_objects, size_element_mesh, type_mesh)

            elif type_mesh == "Estructurada":
                subdivision = self.view_menu_mesh.getSubdivision()
                self.newMeshAligned(name_mesh, color_mesh, selected_objects, subdivision)
        
        
    def newMeshFile(self, name_mesh, color_mesh, path_file):
        # verificamos que el archivo exista
        if path_file == None:
            self.view_menu_mesh.msnAlertFile(True, "Archivo no encontrado")
            return
            
        #verificamos qsi los datos del archivo son correctos
        with open(path_file, 'r') as file:
            lines = file.readlines()
            
            # Inicializar listas para almacenar los datos
            coord = []
            incide = []

            # Iterar sobre las líneas del archivo
            for line in lines:
                
                # Ignorar líneas vacías o comentarios
                if line.strip() == "" or line.startswith("#"):
                    continue
                
                # Separar los valores en la línea por espacios y convertirlos a números
                try:
                    valores = [float(valor) for valor in line.split()]
                except ValueError:
                    self.view_menu_mesh.msnAlertFile(True, "Error en la separación o tipo de dato")                    
                    return
                                    

                
                # Verificar a qué conjunto de datos pertenece esta línea                
                if len(valores) == 2: # coordenadas
                    coord.append(valores)
                
                elif len(valores) == 3 or len(valores) == 4: # índices triangulares o cuadriláteros
                    #pasar de float a int
                    valores = [int(valor) for valor in valores]
                    incide.append(valores)
                else:
                    self.view_menu_mesh.msnAlertFile(True, "Error en la cantidad de datos en la línea")
                    return
                
                    
            # Verificar que haya al menos 3 coordenadas y 3 índices
            if len(coord) < 3 or len(incide) < 3:
                self.view_menu_mesh.msnAlertFile(True, "Datos insuficientes en el archivo")
                return
            
            # Verificar que los índices sean válidos
            for indices in incide:
                for indice in indices:
                    if indice < 1 or indice > len(coord):
                        self.view_menu_mesh.msnAlertFile(True, "Índices incorrectos en el archivo")
                        return
            
            # nodos
            nodes ={}
            index = 1
            for node in coord:
                nodes[f'NODE#{index}'] = {'COORDINATES':[node[0],node[1]]}             
                index +=1
            
            # elementos
            elements ={}
            index = 1
            for element in incide:
                elements[f'ELEMENT#{index}'] = [
                                f'NODE#{element[0]}',
                                f'NODE#{element[1]}',
                                f'NODE#{element[2]}'
                            ]
                if len(element) == 4:
                    elements[f'ELEMENT#{index}'].append(f'NODE#{element[3]}')
                index +=1
                
            if len(element) == 3:
                id = self.model_current_project.createMeshTriangular(name=name_mesh ,
                                                    color=color_mesh,
                                                    nodes=nodes,
                                                    elements= elements)
                model_mesh = self.model_current_project.getModelsMeshsTriangular()[id]
            
            elif len(element) == 4:
                id = self.model_current_project.createMeshQuadrilateral(name=name_mesh ,
                                                    color=color_mesh,
                                                    nodes=nodes,
                                                    elements= elements)
                model_mesh = self.model_current_project.getModelsMeshsQuadrilaterals()[id]
                
            self.createMeshCard(model_mesh)
            self.view_menu_mesh.endMesh()
            self.endDrawMesh()
            
            self.view_menu_mesh.msnAlertFile(False, "Archivo cargado correctamente")

    
    def newMeshTriangular(self, name_mesh, color_mesh, selected_objects, size_element_mesh, type_mesh):         
            

        if len(selected_objects) < 3 and type_mesh == "Triangular":
            self.view_menu_mesh.msnAlertSelected(True, "Para triangular, Selecciona más de 3 elementos")
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
        nodes = { }
        index = 1
        for node in _points:
            nodes[f'NODE#{index}'] = {'COORDINATES':[node[0],node[1]]}
            index +=1

        _triangles = mesh.cells_dict["triangle"]

        elements = { }
        index = 1
        for element in _triangles:
            elements[f'ELEMENT#{index}'] = [
                            f'NODE#{int(element[0]+1)}',
                            f'NODE#{int(element[1]+1)}',
                            f'NODE#{int(element[2]+1)}'
                        ]            
            index +=1
            
        id = self.model_current_project.createMeshTriangular(name=name_mesh ,
                                                    color=color_mesh,
                                                    nodes=nodes,
                                                    elements= elements)
        model_mesh = self.model_current_project.getModelsMeshsTriangular()[id]
        self.createMeshCard(model_mesh)

        self.view_menu_mesh.endMesh()
        self.endDrawMesh()


    def newMeshQuadrilateral(self, name_mesh, color_mesh, selected_objects, size_element_mesh, type_mesh):
        
        
        if type_mesh == "Cuadrilátera" and not len(selected_objects) == 4 :
            self.view_menu_mesh.msnAlertSelected(True, "Para Cuadrilátera selecciona únicamente 4 líneas ")
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


        # nodos
        nodes ={}
        index = 1
        for node in points:
            nodes[f'NODE#{index}'] = {'COORDINATES':[node[0],node[1]]}             
            index +=1



        elements ={}
        index = 1
        for element in quadrilaterals:
            elements[f'ELEMENT#{index}'] = [
                            f'NODE#{element[0]+1}',
                            f'NODE#{element[1]+1}',
                            f'NODE#{element[2]+1}',
                            f'NODE#{element[3]+1}'    
                        ]
            index +=1

   

        id = self.model_current_project.createMeshQuadrilateral(name=name_mesh ,
                                                    color=color_mesh,
                                                    nodes=nodes,
                                                    elements = elements,)

        model_mesh = self.model_current_project.getModelsMeshsQuadrilaterals()[id]
        self.createMeshCard(model_mesh)

        self.view_menu_mesh.endMesh()
        self.endDrawMesh()


    def newMeshAligned(self, name_mesh, color_mesh, selected_objects, subdivision):
        """Genera una malla cuadrilátera alineada a la malla de fondo.
        Subdivide cada celda de la malla de fondo en NxN subceldas (subdivision = N*N)
        y solo conserva las subceldas cuyo centro cae dentro del polígono seleccionado.
        """
        # 1) Validar malla de fondo
        model_mesh_back = self.model_current_project.getModelMeshBack()
        if model_mesh_back is None or not model_mesh_back.getNodes():
            self.view_menu_mesh.msnAlertSelected(True, "Requiere malla de fondo definida")
            return

        # 2) Validar polígono cerrado (mínimo 3 líneas, reusa helpers existentes)
        if len(selected_objects) < 3:
            self.view_menu_mesh.msnAlertSelected(True, "Para Estructurada, selecciona al menos 3 líneas")
            return

        lines = []
        for line in selected_objects:
            lines.append(
                ((line.start_point.pos().x(), line.start_point.pos().y()),
                 (line.end_point.pos().x(),   line.end_point.pos().y()))
            )

        polygon = self.is_closed_polygon(lines)
        if not polygon:
            self.view_menu_mesh.msnAlertSelected(True, "Selección no es un polígono cerrado")
            return
        self.view_menu_mesh.msnAlertSelected(False)

        if self.line_Intersection(polygon):
            self.view_menu_mesh.msnAlertSelected(True, "Dos líneas se interceptan")
            return
        self.view_menu_mesh.msnAlertSelected(False)

        # 3) Vértices del polígono en orden
        vertices = [line[0] for line in polygon]

        # 4) Tamaño de subcelda derivado de la malla de fondo
        ele_size = model_mesh_back.getSizeElement()
        n_per_axis = int(round(math.sqrt(subdivision)))
        sub_size = ele_size / n_per_axis

        # 5) Bounding box del polígono
        xs = [v[0] for v in vertices]
        ys = [v[1] for v in vertices]
        x_min, x_max = min(xs), max(xs)
        y_min, y_max = min(ys), max(ys)

        # 6) Recorrer subceldas en el bounding box y filtrar por containment
        nodes_dict = {}
        elements_dict = {}
        node_pos_to_id = {}
        next_node_id = 1
        next_elem_id = 1

        i_start = math.floor(x_min / sub_size)
        i_end   = math.ceil(x_max / sub_size)
        j_start = math.floor(y_min / sub_size)
        j_end   = math.ceil(y_max / sub_size)

        for i in range(i_start, i_end):
            for j in range(j_start, j_end):
                cx = (i + 0.5) * sub_size
                cy = (j + 0.5) * sub_size
                if not self._point_in_polygon(cx, cy, vertices):
                    continue
                corners = [
                    (i*sub_size,     j*sub_size),
                    ((i+1)*sub_size, j*sub_size),
                    ((i+1)*sub_size, (j+1)*sub_size),
                    (i*sub_size,     (j+1)*sub_size),
                ]
                corner_ids = []
                for (cx_n, cy_n) in corners:
                    key = (round(cx_n, 9), round(cy_n, 9))
                    if key not in node_pos_to_id:
                        nid = f"NODE#{next_node_id}"
                        nodes_dict[nid] = {"COORDINATES": [cx_n, cy_n]}
                        node_pos_to_id[key] = nid
                        next_node_id += 1
                    corner_ids.append(node_pos_to_id[key])
                elements_dict[f"ELEMENT#{next_elem_id}"] = corner_ids
                next_elem_id += 1

        if not elements_dict:
            self.view_menu_mesh.msnAlertSelected(True, "Ninguna subcelda cae dentro del polígono")
            return

        # 7) Guardar como malla cuadrilátera estándar (reusa flujo existente)
        id_mesh = self.model_current_project.createMeshQuadrilateral(
            name=name_mesh,
            color=color_mesh,
            nodes=nodes_dict,
            elements=elements_dict,
        )

        model_mesh = self.model_current_project.getModelsMeshsQuadrilaterals()[id_mesh]
        self.createMeshCard(model_mesh)

        self.view_menu_mesh.endMesh()
        self.endDrawMesh()


    def _point_in_polygon(self, x, y, vertices):
        """Ray casting algorithm. vertices: lista [(x,y), ...]"""
        inside = False
        n = len(vertices)
        j = n - 1
        for i in range(n):
            xi, yi = vertices[i]
            xj, yj = vertices[j]
            if ((yi > y) != (yj > y)) and \
               (x < (xj - xi) * (y - yi) / (yj - yi + 1e-15) + xi):
                inside = not inside
            j = i
        return inside


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
            
        for controller in self.list_controller_card:
            if controller.id == id:
                self.list_controller_card.remove(controller)
                break
        self.signal_delete_mesh.emit()
        
    @Slot()
    def editMesh(self):
        self.signal_edit_mesh.emit()
        
    @Slot(str)
    def msnAlertDefault(self, msn):
        self.view_menu_mesh.msnAlertDefault( msn=msn)
	




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


