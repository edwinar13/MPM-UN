""" Este módulo contiene la clase iniciar Ui_MainWindow.
es la ventana principal del programa."""

from PySide6.QtCore import ( QFile, Slot)
from PySide6.QtWidgets import ( QMainWindow,QFileDialog,QFrame, QSizePolicy,QLabel,QPushButton )
from ui import ui_main_window
from clases import class_projects
from clases import class_ui_frame_home
from clases import class_ui_frame_draw
from clases import database_class
from clases import class_ui_dialog_msg

'''
class VLine(QFrame):
    # a simple VLine, like the one you get from designer
    def __init__(self):
        super(VLine, self).__init__()
        self.setFrameShape(self.VLine)
'''

class MainWindow(QMainWindow):
    """Esta clase crea la ventana QMainWindow de la ventana principal.

        Args:
            createDataBase(CreateDataBase): Objeto para crear bases de datos.
            
        Attributes:
            createDataBase(CreateDataBase): Objeto para crear bases de datos.
            actual_project(Project): Contiene el proyecto actual.

    """ 
    
        
    def __init__(self, createDataBase):
        QMainWindow.__init__(self)
        self.ui = ui_main_window.Ui_MainWindow()        
        self.ui.setupUi(self)

        # Atributo
        self.__createDataBase = createDataBase
        self.__actual_project = None
     

        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()

        #Inicia el objeto db de del programa
        self.db_config_mpmun = database_class.DataBaseConfigMpmun()

        # Iniciando objeto proyectos 
        self.projects = class_projects.Projects(self.db_config_mpmun)        
        self.__updateProjectsRecent()

        '''
#-----------------------------------------------------------------------------------
        #self.ui.statusbar().showMessage("bla-bla bla")
        self.statusBar().showMessage("bla-bla bla")
        self.lbl1 = QLabel("Label: ")
        self.lbl1.setStyleSheet('border: 0; color:  blue;')
        self.lbl2 = QLabel("Data : ")
        self.lbl2.setStyleSheet('border: 0; color:  red;')
        ed = QPushButton('StatusBar text')
        ed.setStyleSheet('background-color: #FFF8DC; color:  red;')


        self.statusBar().reformat()
        self.statusBar().setStyleSheet('border: 0; background-color: #FFF8DC;')
        self.statusBar().setStyleSheet("QStatusBar::item {border: none;}") 
        
        #self.statusBar().addPermanentWidget(VLine())    # <---
        self.statusBar().addPermanentWidget(self.lbl1)
        #self.statusBar().addPermanentWidget(VLine())    # <---
        self.statusBar().addPermanentWidget(self.lbl2)
        #self.statusBar().addPermanentWidget(VLine())    # <---
        self.statusBar().addPermanentWidget(ed)
        #self.statusBar().addPermanentWidget(VLine())    # <---
        
        self.lbl1.setText("Label: Hello")
        self.lbl2.setText("Data : 15-09-2019")

        ed.clicked.connect(lambda: self.statusBar().showMessage("Hello "))
#-----------------------------------------------------------------------------------

        '''


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 

        #::::::::::::::::::::  CONFIGURANDO MAIN WINDOW ::::::::::::::::::::
        """
        with open("css/styles_oscuro.css") as f:
            self.setStyleSheet(f.read())
        self.showMaximized()
        """
        # :::::::::::::::::::: BOTÓN Y PAGINA POR DEFECTO ::::::::::::::::::::
        self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
        self.ui.frame_home.setStyleSheet("background-color: #36C9C6;")
        self.ui.frame_homeInf.setStyleSheet("background-color: #2B2B2B;")
        

        # ::::::::::::::::::::   SHORTCUT Y STATUS DE MENÚ SUPERIOR ::::::::::::::::::::
        self.ui.action_nuevo.setShortcut('Ctrl+n')
        self.ui.action_nuevo.setStatusTip('Nuevo')
        self.ui.action_abrir.setShortcut('Ctrl+o')
        self.ui.action_abrir.setStatusTip('Abrir')
        self.ui.action_guardar.setShortcut('Ctrl+s')
        self.ui.action_guardar.setStatusTip('Guardar')
        self.ui.action_guardarComo.setShortcut('Ctrl+shift+s')
        self.ui.action_guardarComo.setStatusTip('Guardar como')
        self.ui.action_importar.setShortcut('Ctrl+i')
        self.ui.action_importar.setStatusTip('Importar')
        self.ui.action_exportar.setShortcut('Ctrl+e')
        self.ui.action_exportar.setStatusTip('Exportar')

        # ::::::::::::::::::::   CONFIGURANDO  FRAME INICIO ::::::::::::::::::::
        self.frame_home = class_ui_frame_home.FrameHome(self)
        self.ui.verticalLayout_emptyHome.addWidget(self.frame_home)

        # ::::::::::::::::::::   CONFIGURANDO  FRAME DRAW ::::::::::::::::::::
        self.frame_draw = class_ui_frame_draw.FrameDraw(self)
        self.ui.verticalLayout_emptyDraw.addWidget(self.frame_draw)


        self.__showMessageInformative("Programa iniciado correctamente")
        
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        
        # ::::::::::::::::::::   EVENTOS DE WIDGET FRAME INICIO ::::::::::::::::::::
        self.frame_home.signal_home_open.connect(self.__openProject)
        self.frame_home.signal_home_new.connect(self.__triggeredActionNuevoProyecto)
        
        # ::::::::::::::::::::   EVENTOS DE WIDGET FRAME DRAW  ::::::::::::::::::::
        self.frame_draw.signal_msn_critical.connect(self.__showMessageCritical)
        self.frame_draw.signal_msn_satisfactory.connect(self.__showMessageSatisfactory)
        self.frame_draw.signal_msn_informative.connect(self.__showMessageInformative)
        self.frame_draw.signal_msn_informative.connect(self.__showMessageInformative)
        self.frame_draw.signal_project_save_state.connect(self.__projectSaveState)

        # ::::::::::::::::::::   EVENTOS MENU LATERAL ::::::::::::::::::::
        self.ui.toolButton_home.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawData.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawMesh.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawPoint.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawBoundary.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_viewResult.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_setting.clicked.connect(self.__clickedToolButtonMenuLat)

        
        # ::::::::::::::::::::   EVENTOS  MENU SUPERIOR ::::::::::::::::::::
        self.ui.action_nuevo.triggered.connect(self.__triggeredActionNuevoProyecto)
        self.ui.action_guardar.triggered.connect(self.__triggeredActionSaveProject)
        self.ui.action_guardarComo.triggered.connect(self.__triggeredActionSaveAsProject)
        #self.ui.action_importar.triggered.connect(self.triggeredActionXXXXXXXX)
        #self.ui.actionExportar.triggered.connect(self.triggeredActionXXXXXXXX)
        self.ui.action_abrir.triggered.connect(self.__triggeredActionAbrirProyecto)

    ###############################################################################
	# ::::::::::::::::::::    MÉTODOS DE EVENTOS MENU LATERAL   ::::::::::::::::::::
	###############################################################################
    def __clickedToolButtonMenuLat(self):
        """ Método para los eventos de los botones del menú lateral
        Se obtiene el botón que activo la señal y se redirecciona
        al botón correspondiente"""

        self.__resetToolButtonMenuLat()
        buttonSelected = self.sender()
        nameButton = buttonSelected.objectName()

        if nameButton==self.ui.toolButton_home.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
            self.ui.frame_home.setStyleSheet("background-color: #36C9C6;")
            self.ui.frame_homeInf.setStyleSheet("background-color: #2B2B2B;")  

        if nameButton==self.ui.toolButton_drawData.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_data)
            self.ui.frame_drawData.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_drawDataInf.setStyleSheet("background-color: #2B2B2B;")
            self.frame_draw.showHideDrawMenu("Data")

        if nameButton==self.ui.toolButton_drawMesh.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_mesh)
            self.ui.frame_drawMesh.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_drawMeshInf.setStyleSheet("background-color: #2B2B2B;") 
            self.frame_draw.showHideDrawMenu("Mesh")

        if nameButton==self.ui.toolButton_drawPoint.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_point)
            self.ui.frame_drawPoint.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_drawPointInf.setStyleSheet("background-color: #2B2B2B;") 
            self.frame_draw.showHideDrawMenu("Point")

        if nameButton==self.ui.toolButton_drawBoundary.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_contour)
            self.ui.frame_drawBoundary.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_drawBoundaryInf.setStyleSheet("background-color: #2B2B2B;") 
            self.frame_draw.showHideDrawMenu("Boundary")

        if nameButton==self.ui.toolButton_viewResult.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_view)
            self.ui.frame_viewResult.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_viewResultInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton==self.ui.toolButton_setting.objectName():
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)

    ###############################################################################
	# ::::::::::::::::::::  MÉTODOS DE EVENTOS MENU SUPERIOR  ::::::::::::::::::::
	###############################################################################
    def __triggeredActionNuevoProyecto(self):
        """ Abre cuadro de dialogo para nuevo proyecto. """
        nameCurrent = self.windowTitle()
        self.setWindowTitle("MPM-UN    Untitled document*")
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self,"Nuevo Pryecto","","Data files mpm (*.mpm)", options=options)
        if file_path:
            if self.projects.newFileProject(file_path):
                fileName = file_path.split('/')[-1]
                self.setWindowTitle("MPM-UN    {}".format(fileName))
                self.__showMessageInformative("Proyecto creado con éxito")
                self.__openProject(file_path) 
        else:
            self.setWindowTitle(nameCurrent)

    def __triggeredActionAbrirProyecto(self):
        """ Abre cuadro de dialogo para abrir proyecto. """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self,"Abrir Pryecto","","Data files mpm (*.mpm)", options=options)
        if file_path:
            self.__openProject(file_path)
    
    def __triggeredaccionRecienteClear(self):
        """Borra los proyectos recientes."""
        if self.projects.deleteProjects():
            self.__updateProjectsRecent()
        else:
            pass

    def __triggeredaccionReciente(self):
        """Método para los eventos del menú superior >> recientes"""
        file_path = self.sender().text()
        if file_path:
            self.__openProject(file_path)

    def __triggeredActionSaveProject(self):   
        """Guarda el proyecto"""     
        if self.__actual_project != None :
            if self.__actual_project.checkProjectChanges():
                self.__actual_project.saveData()
                self.__showMessageInformative("Se ha guardado el proyecto")
                self.__projectSaveState(False)
                
    def __triggeredActionSaveAsProject(self):   
        """ Guarda en ruta diferente el proyecto """
        if self.__actual_project != None :
            nameCurrent = self.windowTitle()
            options = QFileDialog.Options()
            new_path_file, _ = QFileDialog.getSaveFileName(self,"Guardar proyecto como","","Data files mpm (*.mpm)", options=options)
            if new_path_file:
                if self.__actual_project.projectSaveAs(new_path_file):
                    fileName = new_path_file.split('/')[-1]
                    self.setWindowTitle("MPM-UN    {}".format(fileName))

                    self.__showMessageInformative("Proyecto fue guardado como {}")
                    self.__openProject(new_path_file) 
            else:
                self.setWindowTitle(nameCurrent)

    ###############################################################################
	# ::::::::::::::::::::         FUNCIONES GENERALES UI      ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::  FUNCIONES MENU LATERAL  ::::::::::::::::::::
    def __resetToolButtonMenuLat(self):
        """ Reinicializa el estado de los botones del menú lateral  """
        self.ui.frame_home.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawData.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawMesh.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawPoint.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawBoundary.setStyleSheet("background-color: #333333;") 
        self.ui.frame_viewResult.setStyleSheet("background-color: #333333;") 

        self.ui.frame_viewResultInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_homeInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawDataInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawBoundaryInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawPointInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_drawMeshInf.setStyleSheet("background-color: #333333;")

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
                self.setWindowTitle("MPM-UN    {}".format(self.__actual_project.getName()))
                self.ui.toolButton_drawData.setEnabled(True)
                self.ui.toolButton_drawMesh.setEnabled(True)
                self.ui.toolButton_drawPoint.setEnabled(True)
                self.ui.toolButton_drawBoundary.setEnabled(True)
                self.__resetToolButtonMenuLat()
                self.ui.frame_drawData.setStyleSheet("background-color: #36C9C6;") 
                self.ui.frame_drawDataInf.setStyleSheet("background-color: #2B2B2B;")
                self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
                self.__showMessageInformative("Se ha abierto el proyecto: {}".format(self.__actual_project.getName()))


                """              ███▀▀▀▀▀ deberia actualizar todo ▀▀▀▀▀███                 """
                self.frame_draw.configDrawMenuData(project = self.__actual_project)

        elif ( QFile.exists(file_path) and event_changes=="ignore"):
            pass
        else:
            self.__showMessageCritical("No se ha encontrado el documento {}".format(file_name)) 
        self.__updateProjectsRecent()
    
    def __updateProjectsRecent(self):
        """ Actualiza los proyectos recientes. """
        self.frame_home.removeCardsProjectsRecent()
        self.ui.menu_recientes.clear()

        if self.projects.getProjects():
            projects = self.projects.getProjects()
            No_proyecto = 1
            max_projects = 15

            for  project in projects:
                #agrega cada proyecto a menu>recientes  
                name, path, data, hour = project.getData()
                if No_proyecto <= max_projects and QFile.exists(path):
                    self.frame_home.addCardProjectsRecent(name, path, data, hour)
                    self.ui.menu_recientes.addAction(path)
                No_proyecto += 1
            
            #colocar una tarjeta vacía otro al final proyectos recientes
            self.frame_home.addCardEmptyProjectsRecent()
            
        self.ui.menu_recientes.addSeparator()
        self.ui.menu_recientes.addAction('Limpiar')

        for accion in self.ui.menu_recientes.actions():
            if accion.text() == 'Limpiar':
                accion.triggered.connect(self.__triggeredaccionRecienteClear)
            else:
                pass
                accion.triggered.connect(self.__triggeredaccionReciente)
    
    @Slot(bool)
    def __projectSaveState(self,there_are_changes):
        """Recibe la señal del estado del guardado del proyecto.

        Args:
            there_are_changes(bool): 
                        True >>> si se realizó cambios en el proyecto
                        False >>> si no hay cambios en el proyecto

        """
        if there_are_changes == True:     
            self.setWindowTitle("MPM-UN    •• {} ••".format(self.__actual_project.getName()))
        else:
            self.setWindowTitle("MPM-UN    {}".format(self.__actual_project.getName()))

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS PARA MENSAJES        ::::::::::::::::::::
	###############################################################################
    @Slot(str)
    def __showMessageCritical(self, message):
        """ imprime en la barra de estado un mensaje critico.

        Args:
            message(str): Mensaje critico 
        """
        self.ui.statusbar.setStyleSheet("color: #F94646;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Error",message)
    
    @Slot(str)
    def __showMessageSatisfactory(self, message):
        """ imprime en la barra de estado un mensaje satisfactorio.

        Args:
            message(str): Mensaje satisfactorio 
        """
        self.ui.statusbar.setStyleSheet("color: #36C9C6;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Running",message)
    
    @Slot(str)
    def __showMessageInformative(self, message):
        """ imprime en la barra de estado un mensaje informativo.

        Args:
            message(str): Mensaje informativo 
        """
        self.ui.statusbar.setStyleSheet("color: #DDDDDD;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Information",message)

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################
    def closeEvent(self, event):
        """Evento al cerrar la ventana main window, se valida si hay proyecto actual y hay cambio,
         en ese caso se abre cuadro de dialogo para confirmar si guarda o no."""
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
                    event.accept()
                # No Guardar
                elif result == "not save":
                    print("# No Guardar")
                    event.accept()

                elif result == "cancel" or result == "exit":
                    print("# Cancelar")
                    event.ignore()
            else:
                event.accept()
        else:
            event.accept()
