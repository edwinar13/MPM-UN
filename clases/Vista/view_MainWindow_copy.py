""" Este módulo contiene la clase iniciar Ui_MainWindow.
es la ventana principal del programa."""

from PySide6.QtCore import ( QFile, Slot,QSize,Qt,QTimer)
from PySide6.QtWidgets import (QApplication, QMainWindow,QFileDialog,
QFrame, QSizePolicy,QLabel,QPushButton,QComboBox,QToolButton,QUndoView)
from PySide6.QtGui import (QIcon,QScreen,QShortcut,QKeySequence,QKeyEvent, QUndoStack)
from ui import ui_main_window
from clases import class_projects
from clases.Vista import view_PageHome
from clases.Vista import view_PageDraw
from clases import class_database
from clases import class_ui_dialog_msg


class MainWindow(QMainWindow):
    """Esta clase crea la ventana QMainWindow de la ventana principal.

        Args:
            createDataBase(CreateDataBase): Objeto para crear bases de datos.
            
        Attributes:
            createDataBase(CreateDataBase): Objeto para crear bases de datos.
            actual_project(Project): Contiene el proyecto actual.

    """ 
    
        
    def __init__(self,controller,  createDataBase):
        QMainWindow.__init__(self)
        self.ui = ui_main_window.Ui_MainWindow()        
        self.ui.setupUi(self)

        

    ###############################################################################
	# ::::::::::::::::::::  MÉTODOS DE EVENTOS MENU SUPERIOR  ::::::::::::::::::::
	###############################################################################
        
          
    def __activatedShortCutEsc(self):
        """Al presionar ESC ejecuta aciones contenidas en la lista. """
        self.__viewToolButtonMenuLat(self.previous_selected_button)
        self.setting = True


    



    

    # ::::::::::::::::::::  FUNCIONES MENU SUPERIOR  ::::::::::::::::::::
    @Slot(str)
    def __openProject (self, file_path):
        """ Abre un proyecto y configura la UI para este nuevo proyecto. 

        Attributes:
            file_path (str): Ruta del proyecto.
                        
        """
        event_changes= "accept"      
        if self.__actual_project != None:
            checkProjectChanges = self.__actual_project.checkProjectChanges()      
            if checkProjectChanges: 
                dialoMsg = class_ui_dialog_msg.DialogMsg(self, 1, 
                                        "¿Quiere guardar los cambios de este proyecto?", 
                                        "has realizado cambios")
                dialoMsg.setTypeIcon(0)
                dialoMsg.setTextDescription("Has realizado cambios en el archivo {}".format(self.__actual_project.getName()))
                dialoMsg.setModal(True)
                dialoMsg.exec()
                result = dialoMsg.getButtonSelected()
                #Guardar
                if result == "save":
                    print("# Guardar = {}".format(self.__actual_project.saveData()))
                    event_changes= "accept"
                # No Guardar
                elif result == "not save":
                    print("# No Guardar")
                    event_changes= "accept"
                elif result == "cancel" or result == "exit":
                    print("# Cancelar")
                    event_changes= "ignore"
            else:                
                event_changes= "accept"
 

        if ( QFile.exists(file_path) and event_changes=="accept"):
            project_open = class_projects.Project(path = file_path) 
            file_name =project_open.getName()
        
            if self.projects.addProject(self, project_open):
                
                # Configura la UI
                self.__actual_project = project_open




                """              ███▀▀▀▀▀ deberia actualizar todo ▀▀▀▀▀███                 """
                self.frame_draw.configDrawMenuData(project = self.__actual_project)
                self.frame_draw.configDrawItemsScene(project = self.__actual_project)
                self.frame_draw.configDrawMenuMesh(project = self.__actual_project)

        elif ( QFile.exists(file_path) and event_changes=="ignore"):
            pass
        self.__updateProjectsRecent()
    
































   