""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-mesh
Es el widget card de cada malla."""
from PySide6.QtCore import ( QSize, Signal)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )
from ui import ui_widget_draw_mesh_card
from clases import general_class

class viewCardDrawMesh(QFrame, ui_widget_draw_mesh_card.Ui_FormDrawMeshCard):
    """Esta clase crea el QFrame mesh-card para agregarlo a Frame draw-menu-mesh. 

    Args:
            cardNameMesh (str):      Nombre de la malla (default = "").
            cardColorMesh (str):     Color de la malla (default = "").
            cardShowHideMesh (bool): Estado para mostrar u ocultar la malla (default = True).
            
    Attributes:
            __card_name_mesh (str):       Nombre de la malla.
            __card_color_mesh (str):      Color de la malla.
            __card_show_hide_mesh (bool): Estado para mostrar u ocultar la malla.

    """    
    signal_open_project = Signal(str)

    def __init__(self, parent = None,  cardNameMesh="", cardColorMesh="#ffffff",cardShowHideMesh=True):
        super(viewCardDrawMesh, self).__init__(parent)
        self.setupUi(self)
        
        # Atributo
        self.__card_name_mesh = cardNameMesh
        self.__card_color_mesh = cardColorMesh
        self.__card_show_hide_mesh = cardShowHideMesh

        # Configura la UI
        self._configUi()
    
        # Establece los eventos de la UI
        self.__initEventUi()

     
       
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def _configUi(self):
        """Configura la interface de usuario (ui).""" 
        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,20,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show = QIcon()
        self.icon_show.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide = QIcon()
        self.icon_hide.addFile(u"recursos/iconos/iconos_menu_draw_mesh/not_view.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # se actualiza informacion del card
        self.label_cardNameMesh.setText(u"{}".format(self.__card_name_mesh))
        self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_mesh))



    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_showHideMesh.clicked.connect(self.__clickedToolButtonShowHideMesh)
        self.toolButton_closeMesh.clicked.connect(self.__clickedToolButtonCloseMesh)

        #este es una forma de darle evento a un frame
        observer = general_class.MouseObserver(self.label_cardNameMesh)


    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonShowHideMesh(self):
        """ Muestra u oculta la malla """
        if self.__card_show_hide_mesh == True:
            
            self.__card_show_hide_mesh = False
            self.toolButton_showHideMesh.setIcon(self.icon_show)
        elif self.__card_show_hide_mesh == False:
            
            self.__card_show_hide_mesh = True
            self.toolButton_showHideMesh.setIcon(self.icon_hide)
        print("OCULTAR O MOSTRAR MALLA")
    
    def __clickedToolButtonCloseMesh(self):
        print("BORRAR MALLA")

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################


    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################
    def mousePressEvent(self, event):
        """Reimplantado el método mousePressEvent
        Args:
            event (QEvent): evento de ui
        """ 
        super().mousePressEvent(event)
        print("***** {}=  Reimplementando mousePressEvent {} *****".format(self.__card_name_mesh,event))


