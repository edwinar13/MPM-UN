""" Este módulo contiene la vista Ui_FormHome, para incluirla en la vista main window"""


import os
import shutil
from PySide6.QtCore import (Signal)
from PySide6.QtWidgets import ( QFrame,QSizePolicy, QFileDialog, QMessageBox)
from config import RESOURCES_DIR
from ui import ui_frame_home
from views.cards.view_WidgetCardProject import ViewWidgetCardProjectHome

class ViewPageHome(QFrame, ui_frame_home.Ui_FormHome):
    
    """Esta clase crea la vista  QFrame home para agregarlo a main window. 

    Attributes:
            controller(ControllerMainWindow): Controlador de la vista ViewMainWindow
            list_view_card (lits): Lista con widget card de cada proyecto.
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
        file_path, _ = QFileDialog.getSaveFileName(self,"Nuevo Proyecto","","Data files json (*.json) ;; Data files mpm (*.mpm)", options=options)
        if file_path:
            self.signal_new_project.emit(file_path)
    
    def __clickedToolButtonOpenProject_2(self):
        self.openExampleProject("Ejemplo 1 - Viga en voladizo.json")

    def __clickedToolButtonOpenProject_3(self):
        self.openExampleProject("Ejemplo 2 - Capacidad portante.json")

    def __clickedToolButtonOpenProject_4(self):
        self.openExampleProject("Ejemplo 3 - Falla de talud.json")

    def __clickedToolButtonOpenProject_5(self):
        self.openExampleProject("Ejemplo 4 - Consolidación 2D.json")

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES   UI     ::::::::::::::::::::
	###############################################################################
    def openExampleProject(self, file_name):
        """Copia un ejemplo (solo datos de entrada, sin resultados) a la ruta
        que elija el usuario y lo abre. El original no se modifica.

        Args:
            file_name (str): nombre del archivo en resources/ejemplos

        """
        source = os.path.join(RESOURCES_DIR, "ejemplos", file_name)
        if not os.path.exists(source):
            QMessageBox.critical(self, "Ejemplo", "No se encontró el ejemplo:\n{}".format(source))
            return
        default = os.path.join(os.path.expanduser("~"), "Documents", file_name)
        file_path, _ = QFileDialog.getSaveFileName(self, "Guardar ejemplo como", default,
                                                   "Data files json (*.json)")
        if not file_path:
            return
        if os.path.splitext(file_path)[1].lower() != ".json":
            file_path += ".json"
        try:
            shutil.copyfile(source, file_path)
        except OSError as e:
            QMessageBox.critical(self, "Ejemplo", "No se pudo guardar el ejemplo:\n{}".format(e))
            return
        self.signal_open_project.emit(file_path.replace('\\', '/'))
    
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






