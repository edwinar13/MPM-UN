""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize,QTimer,QRectF,QLineF,QPointF, Qt, )
from PySide6.QtGui import (QIcon, QFont,QTransform, QPen, QBrush, QPolygonF, QColor)
from PySide6.QtWidgets import ( QLabel,QFrame, QSpacerItem, QSizePolicy,QColorDialog,QGraphicsScene,QGraphicsView, QGraphicsPolygonItem)
from ui import ui_widget_draw_menu_mesh
from clases import general_functions
from clases import class_general
from clases.Vista import view_WidgetCardMesh
#from clases.Vista.view_GraphicsDraw import PointItem,LineItem,TextItem, GraphicsSceneDraw, GraphicsViewDraw
from clases.Vista.view_GraphicsDraw import PointItem,LineItem,TextItem
import math
import numpy as np
import meshpy.triangle as triangle
from scipy.spatial import Delaunay
import scipy
print("scipy.__version__",scipy.__version__)

from clases import class_projects



class Mesh:
    def __init__(self, points, triangles, name="", color="black", size=1.0):
        self.points = points
        self.triangles = triangles
        self.name = name
        self.color = color
        self.size = size
        
    def __str__(self):
        return f"Mesh '{self.name}' with {len(self.points)} points and {len(self.triangles)} triangles"



class ViewWidgetDrawMenuMesh(QFrame, ui_widget_draw_menu_mesh.Ui_FormDrawMenuMesh):
    """Esta clase crea el QFrame draw-menu-mesh para agregarlo a Frame Draw.

    Args:
            scene (QGraphicsScene): es la escena actual para draw
            view (QGraphicsView): es la vista actual para draw

    Attributes:
            name_mesh (str): 
            color_mesh (str):
            size_element_mesh (str):
            selected_objects (str):
            gravity (str):
            projectActual (Project): Objeto del proyecto actual.
            graphicsScene (QGraphicsScene): es la escena actual para draw
            graphicsView (QGraphicsView): es la vista actual para draw

            hide_show_frame_data_1 (bool): Estado hide-Show de draw-menu-mesh Dibujo.
            hide_show_frame_data_2 (bool): Estado hide-Show de draw-menu-mesh Malla Regular cuadrilátero.
            hide_show_frame_data_3 (bool): Estado hide-Show de draw-menu-mesh lista de mallas.
            hide_show_frame_data (bool): Esatdo hide-Show draw-menu-mesh.
            
    Method:
            :

    """ 
    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str)  
    signal_deleted_card_mesh = Signal(bool) 
    signal_end_draw_geometry = Signal() 

    signal_select_line_mesh= Signal() 
    signal_size_mesh= Signal() 
    signal_new_mesh= Signal() 
    
    
    #def __init__(self, scene:GraphicsSceneDraw, view1:GraphicsViewDraw, view2:GraphicsViewDraw):
    def __init__(self):

        super(ViewWidgetDrawMenuMesh, self).__init__()
        self.setupUi(self)

        '''
        self.scene_draw = scene
        self.view_draw_1 = view1
        self.view_draw_2 = view2
        '''

        self.scene_draw = None
        self.view_draw_1 = None
        self.view_draw_2 = None

        # Atributo
        """
        self.__name_mesh = None
        self.__size_element_mesh = None
        """
        self.__color_mesh = None
        self.__selected_objects=[]

 
        self.__hide_show_frame_mesh_2=True
        self.__hide_show_frame_mesh_3=True
        self.__hide_show_frame_mesh=True

        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()

        self.contador=0

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('MALLADO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)


    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        


        # ::::::::::::::::::::      EVENTOS MENU MESH  Malla Regular cuadrilátero.   ::::::::::::::::::::
        self.lineEdit_textMesh1.editingFinished.connect(self.__editingFinishedLineEditMesh1)
        self.toolButton_cardMeshDraw5.clicked.connect(self.__clickedToolButtonSizeMesh)  
        self.toolButton_cardMeshDraw6.clicked.connect(self.__clickedToolButtonSelectLine)  
        self.toolButton_cardMeshDraw7.clicked.connect(self.__clickedToolButtonColorPicker)        
        self.toolButton_mesh.clicked.connect(self.__clickedToolButton_mesh)
        self.doubleSpinBoxl_textMesh4.valueChanged.connect(self.__valueChangedDoubleSpinBoxlSizeMesh)
        
        # :::::::::::::::::::::::            EVENTOS MENU MESH             :::::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardMeshSubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_cardMeshSubTitle3.clicked.connect(self.__clickedToolButtonCardMeshSubTitle3)




    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    """ Métodos para los eventos de los botones y widget """

    def addCardMesh(self, card_mesh):                   

        self.verticalLayout_containerCardMesh.addWidget(card_mesh)
        last_index = self.verticalLayout_containerCardMesh.count() - 1
        self.verticalLayout_containerCardMesh.insertWidget(last_index, self.frame_empty)
    

    def __editingFinishedLineEditMesh1(self):
        #self.__name_mesh = self.lineEdit_textMesh1.text()
        self.lineEdit_textMesh1.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 
          

    def __clickedToolButtonColorPicker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__color_mesh=color.name()
            self.lineEdit_textMesh2.setStyleSheet('background-color : {}'.format(self.__color_mesh))

    
    def __valueChangedDoubleSpinBoxlSizeMesh(self):
        self.__size_element_mesh = self.doubleSpinBoxl_textMesh4.value()


    def __clickedToolButtonSelectLine(self):
        self.signal_end_draw_geometry.emit()
        self.signal_select_line_mesh.emit()
        self.hideShowSelectedObjects(False) 
        self.lineEdit_textMesh5.setText("{} Elementos".format(0)) 

    def __clickedToolButtonSizeMesh(self):
        self.signal_end_draw_geometry.emit()
        self.signal_size_mesh.emit()

    def selectLineMesh(self, no_lines):
        self.lineEdit_textMesh5.setText("{} Elementos".format(no_lines))   


    def sizeMesh(self, dist):
        self.__size_element_mesh = dist
        self.doubleSpinBoxl_textMesh4.setValue(self.__size_element_mesh)



    def hideShowSelectedObjects(self, state):     

        """
        Cambia el estado de selección de los objetos seleccionados.

        Args:
            state (bool): Estado de selección a asignar a los objetos seleccionados.

        Attributes:
            __selected_objects (list): Lista de objetos seleccionados.

        Returns:
            None
        """
        for object_selected in self.__selected_objects:
            object_selected.isSelectedMesh = state
        #### #self.scene_draw.update()

    def getNameNewMesh (self):
        name_mesh = self.lineEdit_textMesh1.text()
        return name_mesh
    
    def getcolorNewMesh (self):        
        return self.__color_mesh
    
    def getSizeNewMesh (self):    
        size_element_mesh = self.doubleSpinBoxl_textMesh4.value()    
        return size_element_mesh
        
    


    def msnAlertName(self, error, msn=""):
        if not error:
            # self.lineEdit_textMesh2.setStyleSheet("border-color: #444444;background-color: {};".format(self.__color_mesh))
            self.lineEdit_textMesh1.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMesh1.setFocus()
            self.lineEdit_textMesh1.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertColor(self, error, msn=""):
        if not error:
            self.lineEdit_textMesh2.setStyleSheet("border-color: #444444;background-color: {};".format(self.__color_mesh))
            #self.lineEdit_textMesh2.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMesh2.setFocus()
            self.lineEdit_textMesh2.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertSelected(self, error, msn=""):
        if not error:
            self.lineEdit_textMesh5.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMesh5.setFocus()
            self.lineEdit_textMesh5.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))


    def __clickedToolButton_mesh(self):

        self.signal_new_mesh.emit()
        return

        name_mesh = self.lineEdit_textMesh1.text()
        color_mesh = self.__color_mesh
        selected_objects = self.__selected_objects
        size_element_mesh = self.doubleSpinBoxl_textMesh4.value()
         


        
        # Validación de las líneas seleccionadas
        lines = []
        for line in selected_objects:
            lines.append(
            ((line.start_point.pos().x(), line.start_point.pos().y()),
            (line.end_point.pos().x(), line.end_point.pos().y()))
            )

        polygon = self.is_closed_polygon(lines)
        if not polygon:
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Selección no es un polígono cerrado")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
            return
        
        #falta verfivccar si el poligono no forma un 8
        isIntercepted = self.line_Intersection(polygon)
        if isIntercepted:
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Dos líneas se interceptan")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
            return
              
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


    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """

        if self.__hide_show_frame_mesh == True:
            self.frame_mesh.setVisible(False)
            self.__hide_show_frame_mesh = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_mesh == False:
            self.frame_mesh.setVisible(True)
            self.__hide_show_frame_mesh = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)
    
    '''
    def __clickedToolButtonCardMeshSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  datos del proyecto  """
        if self.__hide_show_frame_mesh_1 == True:
            self.frame_mesh1.setVisible(False)
            self.__hide_show_frame_mesh_1 = False
            self.toolButton_cardMeshSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_mesh_1 == False:
            self.frame_mesh1.setVisible(True)
            self.__hide_show_frame_mesh_1 = True
            self.toolButton_cardMeshSubTitle1.setIcon(self.icon_minimize)
    '''

    def __clickedToolButtonCardMeshSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_mesh_2 == True:
            self.frame_mesh2.setVisible(False)
            self.__hide_show_frame_mesh_2 = False
            self.toolButton_cardMeshSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_mesh_2 == False:
            self.frame_mesh2.setVisible(True)
            self.__hide_show_frame_mesh_2 = True
            self.toolButton_cardMeshSubTitle2.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle3(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_mesh_3 == True:
            self.frame_mesh3.setVisible(False)
            self.__hide_show_frame_mesh_3 = False
            self.toolButton_cardMeshSubTitle3.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_mesh_3 == False:
            self.frame_mesh3.setVisible(True)
            self.__hide_show_frame_mesh_3 = True
            self.toolButton_cardMeshSubTitle3.setIcon(self.icon_minimize)



    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################



    
    
