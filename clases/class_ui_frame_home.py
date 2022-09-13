""" Este módulo contiene la clase Ui_FormHome, para incluirla en main window
es el frame que contiene la parte del inicio."""
import os
from PySide6.QtCore import (Signal)
from PySide6.QtWidgets import ( QFrame,QSizePolicy)
from ui import ui_frame_home
from clases import class_ui_widget_home_card

class FrameHome(QFrame, ui_frame_home.Ui_FormHome):
    """Esta clase crea el QFrame home para agregarlo a main window. 

    Attributes:
            list_view_card (lits): Lista con widget card de cada proyecto.
            pathApp (str): Ruta de donde se ejecuta este archivo.
    Method:
        : removeCardsProjectsRecent
        : addCardProjectsRecent
        : addCardEmptyProjectsRecent

    """
    signal_home_open = Signal(str)
    signal_home_new = Signal()
    def __init__(self, parent = None):
        super(FrameHome, self).__init__(parent)
        self.setupUi(self)

        # Atributo
        self.__list_view_card = []
        self.__pathApp = os.path.abspath(os.getcwd())
        #print(os.path.dirname(os.path.abspath(__file__)))

        # Configura la UI
        self.configUi()

        # Establece los eventos de la UI
        self.initEventUi()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def configUi(self):
        """ Configura la interface de usuario (ui) """ 
        # Deshabilita el desplazamiento vertical del scroll área 1
        self.scrollArea_1.verticalScrollBar().setEnabled(False)
    
    def initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS FRAME HOME     ::::::::::::::::::::
        self.toolButton_cardNew1.clicked.connect(self.__clickedToolButtonNewProject)
        self.toolButton_cardNew2.clicked.connect(self.__clickedToolButtonOpenProject_2)
        self.toolButton_cardNew3.clicked.connect(self.__clickedToolButtonOpenProject_3)
        self.toolButton_cardNew4.clicked.connect(self.__clickedToolButtonOpenProject_4)
        self.toolButton_cardNew5.clicked.connect(self.__clickedToolButtonOpenProject_5)
   
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    """ Métodos para los eventos de los botones y widget """
    
    def __clickedToolButtonNewProject(self):
        """Emite una señal para crear nuevo proyecto""" 
        self.signal_home_new.emit()
    
    def __clickedToolButtonOpenProject_2(self):        
        """ Emite señal para abrir ejemplo barra empotrada """
        path=r"{}\recursos\ejemplos\Ejemplo vibracion barra empotrada.mpm".format(self.__pathApp)
        self.__emitSignalOpen(path=path)

    def __clickedToolButtonOpenProject_3(self):
        """ Emite señal para abrir ejemplo capacidad portante """
        path=r"{}\recursos\ejemplos\Ejemplo capacidad portante.mpm".format(self.__pathApp)
        self.__emitSignalOpen(path=path)

    def __clickedToolButtonOpenProject_4(self):
        """ Emite señal para abrir ejemplo disco en plano inclinado """
        path=r"{}\recursos\ejemplos\Ejemplo disco deslizando en plano inclinado.mpm".format(self.__pathApp)
        self.__emitSignalOpen(path=path)

    def __clickedToolButtonOpenProject_5(self):
        """ Emite señal para abrir ejemplo talud elastoplastico """
        path=r"{}\recursos\ejemplos\Ejemplo falla de talud elastoplastico.mpm".format(self.__pathApp)
        self.__emitSignalOpen(path=path) 

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES   UI     ::::::::::::::::::::
	###############################################################################
    def __emitSignalOpen(self, path):
        """Emite una señal para abrir nuevo proyecto.

        Args:
            path (str): cadena con la ruta del proyecto para abrir

        """ 
        path = path.replace('\\','/')
        self.signal_home_open.emit(path)
    
    def removeCardsProjectsRecent(self):
        """ Elimina las tarjetas de los proyectos si existen. """
        view_card=None
        if len(self.__list_view_card) != 0:
            for view_card in self.__list_view_card: 
                self.verticalLayout_containerCard.removeWidget(view_card)
                view_card.deleteLater()
            self.__list_view_card=[]
    
    def addCardProjectsRecent(self,  name, path, data, hour):
        """ Agrega una tarjeta de proyecto a recientes. 
        
        Args:
            name (str): Nombre del archivo del proyecto.
            path (str): Ruta del archivo del proyecto.
            data (str): Fecha en la que se abrió por última vez el proyecto.
            hour (str): Hora en la que se abrió por última vez el proyecto.

        """
        cardProject = class_ui_widget_home_card.viewCardProject(self, cardName = name,
                                cardDataTime = data, cardPath= path, cardHour= hour)
        #self.cardProject.setStyleSheet("background-color: #36C{}C6;".format(No_proyecto))
        #self.cardProject.setNamesWidges(No_proyecto)

        '''  
        Forma de agregar a un grid layout
        #projects = self.projects.getProjects()
        #positions = [(i,j) for i in range(5) for j in range(3)]
        #   for position, project in zip(positions, projects):
        #self.frame_home.gridLayout_proyectos.addWidget(self.cardProject,*position)
        '''
        self.verticalLayout_containerCard.addWidget(cardProject)
        self.__list_view_card.append(cardProject)
        cardProject.signal_open_project.connect(self.__emitSignalOpen)

    def addCardEmptyProjectsRecent(self):
        """ Agrega una tarjeta vacia proyectos a recientes."""
        frame_end = QFrame()
        frame_end.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                 QSizePolicy.Expanding))
        self.verticalLayout_containerCard.addWidget(frame_end) 
        self.__list_view_card.append(frame_end)