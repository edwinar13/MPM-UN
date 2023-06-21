""" Este módulo contiene la vista Ui_FormHome, para incluirla en la vista main window"""


import os
from PySide6.QtCore import (Signal)
from PySide6.QtWidgets import ( QFrame,QSizePolicy, QFileDialog)
from ui import ui_frame_home
from clases.Vista.view_WidgetCardProject import ViewWidgetCardProjectHome

class ViewPageHome(QFrame, ui_frame_home.Ui_FormHome):
    
    """Esta clase crea la vista  QFrame home para agregarlo a main window. 

    Attributes:
            controller(ControllerMainWindow): Controlador de la vista ViewMainWindow
            list_view_card (lits): Lista con widget card de cada proyecto.
            pathApp (str): Ruta de donde se ejecuta este archivo.
    Method:
        : removeCardsProjectsRecent
        : addCardProjectsRecent
        : addCardEmptyProjectsRecent

    """
    signal_open_project = Signal(str)
    signal_new_project = Signal(str)


    def __init__(self ):
        super(ViewPageHome, self).__init__()
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
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self,"Nuevo Pryecto","","Data files mpm (*.mpm)", options=options)
        if file_path:
            self.signal_new_project.emit(file_path)
    
    def __clickedToolButtonOpenProject_2(self):        
        """ Emite señal para abrir ejemplo barra empotrada """
        path=r"{}\recursos\ejemplos\Ejemplo vibracion barra empotrada.mpm".format(self.__pathApp)
        self.openReferenceProject(path=path)

    def __clickedToolButtonOpenProject_3(self):
        """ Emite señal para abrir ejemplo capacidad portante """
        path=r"{}\recursos\ejemplos\Ejemplo capacidad portante.mpm".format(self.__pathApp)
        self.openReferenceProject(path=path)

    def __clickedToolButtonOpenProject_4(self):
        """ Emite señal para abrir ejemplo disco en plano inclinado """
        path=r"{}\recursos\ejemplos\Ejemplo disco deslizando en plano inclinado.mpm".format(self.__pathApp)
        self.openReferenceProject(path=path)

    def __clickedToolButtonOpenProject_5(self):
        """ Emite señal para abrir ejemplo talud elastoplastico """
        path=r"{}\recursos\ejemplos\Ejemplo falla de talud elastoplastico.mpm".format(self.__pathApp)
        self.openReferenceProject(path=path) 

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES   UI     ::::::::::::::::::::
	###############################################################################
    def openReferenceProject(self, path):
        """Emite una señal para abrir nuevo proyecto.

        Args:
            path (str): cadena con la ruta del proyecto para abrir

        """ 
        path = path.replace('\\','/')
        self.signal_open_project.emit(path)
    
    def removeCardsProjectsRecent(self):
        """ Elimina las tarjetas de los proyectos si existen. """
        view_card=None
        if len(self.__list_view_card) != 0:
            for view_card in self.__list_view_card: 
                self.verticalLayout_containerCard.removeWidget(view_card)
                view_card.deleteLater()
            self.__list_view_card=[]
    
    def addCardProjectsRecent(self,  cardProject:ViewWidgetCardProjectHome):
        """ Agrega una tarjeta de proyecto a recientes. 
        
        Args:
            cardProject (ViewWidgetCardProjectHome): Objeto tarjeta de proyecto

        """

        self.verticalLayout_containerCard.addWidget(cardProject)
        self.__list_view_card.append(cardProject)       

    def addCardEmptyProjectsRecent(self):
        """ Agrega una tarjeta vacia proyectos a recientes."""
        frame_end = QFrame()
        frame_end.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                 QSizePolicy.Expanding))
        self.verticalLayout_containerCard.addWidget(frame_end) 
        self.__list_view_card.append(frame_end)






