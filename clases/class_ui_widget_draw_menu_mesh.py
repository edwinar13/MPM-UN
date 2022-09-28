""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize,QTimer,QRectF,QLineF)
from PySide6.QtGui import (QIcon, QFont,QTransform)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy,QColorDialog,QGraphicsScene,QGraphicsView)
from ui import ui_widget_draw_menu_mesh
from clases import general_functions
from clases import general_class
from clases import class_ui_widget_draw_mesh_card

class WidgetDrawMenuMesh(QFrame, ui_widget_draw_menu_mesh.Ui_FormDrawMenuMesh):
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
    signal_project_save_state = Signal(bool) 
    
    signal_paint_point = Signal() 
    signal_paint_line = Signal() 
    signal_paint_polyline = Signal() 
    signal_paint_rectangle = Signal() 
    signal_paint_rotate = Signal() 
    signal_paint_move = Signal() 
    signal_paint_copy = Signal() 
    signal_paint_erase = Signal() 

    
    def __init__(self):
        super(WidgetDrawMenuMesh, self).__init__()
        self.setupUi(self)

        # Atributo
        self.__name_mesh=""
        self.__color_mesh=""
        self.__size_element_mesh=""
        self.__selected_objects=""

        self.__projectActual= None

        self.__hide_show_frame_mesh_1=True
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
        self.label_lat = general_class.QLabelVertical('MALLADO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)


    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        
        # :::::::::::::::::::::::            EVENTOS DRAW MENU MESH  DIBUJO            :::::::::::::::::::::::
        self.toolButton_cardMeshDraw4.clicked.connect(self.__clickedToolButtonCardMeshDrawPoint)
        self.toolButton_cardMeshDraw1.clicked.connect(self.__clickedToolButtonCardMeshDrawLine)
        self.toolButton_cardMeshDraw2.clicked.connect(self.__clickedToolButtonCardMeshDrawPolyline)
        self.toolButton_cardMeshDraw3.clicked.connect(self.__clickedToolButtonCardMeshDrawRectangle)
        self.toolButton_cardMeshDraw8.clicked.connect(self.__clickedToolButtonCardMeshDrawMove)
        self.toolButton_cardMeshDraw9.clicked.connect(self.__clickedToolButtonCardMeshDrawRotate)
        self.toolButton_cardMeshDraw10.clicked.connect(self.__clickedToolButtonCardMeshDrawCopy)
        self.toolButton_cardMeshDraw11.clicked.connect(self.__clickedToolButtonCardMeshDrawErase)

        # ::::::::::::::::::::      EVENTOS DRAW MENU MESH  Malla Regular cuadrilátero.   ::::::::::::::::::::
        self.toolButton_cardMeshDraw7.clicked.connect(self.__clickedToolButtonColorPicker)        
        self.toolButton_mesh.clicked.connect(self.__clickedToolButton_mesh)
        
        # :::::::::::::::::::::::            EVENTOS DRAW MENU MESH             :::::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardMeshSubTitle1.clicked.connect(self.__clickedToolButtonCardMeshSubTitle1)
        self.toolButton_cardMeshSubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_cardMeshSubTitle3.clicked.connect(self.__clickedToolButtonCardMeshSubTitle3)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    """ Métodos para los eventos de los botones y widget """
    def __clickedToolButtonCardMeshDrawPoint(self):
        self.signal_paint_point.emit()

    def __clickedToolButtonCardMeshDrawLine(self):
        self.signal_paint_line.emit()
    
    def __clickedToolButtonCardMeshDrawPolyline(self):
        self.signal_paint_polyline.emit()
        pass
        '''
        rect = self.__graphicsScene.addRect(QRectF(50, 50, 100, 100))
        item = self.__graphicsScene.itemAt(5, 5, QTransform())
        self.__graphicsView.show()
        '''
    
    def __clickedToolButtonCardMeshDrawRectangle(self):
        self.signal_paint_rectangle.emit()
        pass
        '''
        rect = self.__graphicsScene.addLine(QLineF(0, 0, 100, 100))
        item = self.__graphicsScene.itemAt(50, 50, QTransform())
        self.__graphicsView.setScene(self.__graphicsScene)
        '''

    
        #self.__graphicsView.show()

    def __clickedToolButtonCardMeshDrawMove(self):
        self.signal_paint_move.emit()
    def __clickedToolButtonCardMeshDrawRotate(self):
        self.signal_paint_rotate.emit()
    def __clickedToolButtonCardMeshDrawCopy(self):
        self.signal_paint_copy.emit()
    def __clickedToolButtonCardMeshDrawErase(self):
        self.signal_paint_erase.emit()





    def __clickedToolButtonColorPicker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__color_mesh=color.name()
            self.lineEdit_textMesh2_3.setStyleSheet('background-color : {}'.format(self.__color_mesh))

    def __clickedToolButton_mesh(self):

        card_mesh = class_ui_widget_draw_mesh_card.viewCardDrawMesh(self)
        card_mesh = class_ui_widget_draw_mesh_card.viewCardDrawMesh(self,"Mesh {}".format(self.contador),"#ff559a",False)
        self.contador += 1


    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """
        print(123)
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
