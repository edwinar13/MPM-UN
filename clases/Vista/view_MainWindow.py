""" Este módulo contiene la vista Ui_MainWindow.
es la ventana principal del programa."""

from PySide6.QtCore import ( QFile, QSize,Qt,Signal)
from PySide6.QtWidgets import (QApplication, QMainWindow,QFileDialog,
QFrame, QSizePolicy,QLabel,QPushButton,QComboBox,QToolButton,QUndoView)
from PySide6.QtGui import (QIcon,QScreen,QShortcut,QKeySequence,QKeyEvent, QUndoStack)

from ui import ui_main_window



class ViewMainWindow(QMainWindow):
    """Esta clase crea la vista de la vista QMainWindow de la ventana principal.

        Args:
            controller(ControllerMainWindow): Controlador de la vista ViewMainWindow
            
        Attributes:
            

    """ 
    
    signal_clear_recent_project = Signal()
    signal_open_project = Signal(str)
    signal_new_project = Signal(str)
    signal_action_menu_save = Signal()
    signal_action_menu_saveAs = Signal(str)
    signal_action_menu_undo = Signal()
    signal_action_menu_redo = Signal()

    signal_selected_menu_button = Signal(str)
    signal_toolButton_statusBar = Signal(list)
    signal_action_menu_viewDraw = Signal(list)
    signal_close_app = Signal()
    signal_change_theme = Signal()


    def __init__(self):
        QMainWindow.__init__(self)
       

        # inicializar los widgets
        self.ui = ui_main_window.Ui_MainWindow()        
        self.ui.setupUi(self)

        self.setting = True

        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()

     
        self.showMessageStatusBar("informative","Programa iniciado correctamente")

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 

        #::::::::::::::::::::  CONFIGURANDO MAIN WINDOW ::::::::::::::::::::
        """
        with open("css/styles_oscuro.css") as f:
            self.setStyleSheet(f.read())
        """       
        
        #self.setFixedSize(QSize(1200,700))
        self.showMaximized()

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
        
        self.ui.action_deshacer.setShortcut('Ctrl+z')
        self.ui.action_rehacer.setShortcut('Ctrl+y')        

        self.ui.action_origin.setChecked(True)
        self.ui.action_origin.setShortcut('F5')
        self.ui.action_axis.setChecked(True)
        self.ui.action_axis.setShortcut('F6')
        self.ui.action_grid.setChecked(True)
        self.ui.action_grid.setShortcut('F7')
        self.ui.action_console.setChecked(True)
        self.ui.action_console.setShortcut('F8')
        self.ui.action_label.setChecked(False)
        self.ui.action_label.setShortcut('F9')       

        self.shortcut_change_thema = QShortcut(QKeySequence('Ctrl++'), self)
        self.shortcut_change_thema.setObjectName("shortcut_change_thema")

        # ::::::::::::::::::::   WIDGET BARRA DE ESTADO ::::::::::::::::::::        
        self.label_coor = QLabel("Coor")
        self.label_coor.setStyleSheet('border: none; color:  #DDDDDD')
        self.label_coor.setMinimumSize(QSize(100, 0))
        self.label_coor.setAlignment(Qt.AlignCenter)
        self.label_coor.setVisible(False)
         
        self.toolButton_snap_grid = QToolButton()
        self.toolButton_snap_grid.setCheckable(True)
        self.toolButton_snap_grid.setStyleSheet('border-color: red; background-color: #333333 ;margin: 0px 3px ')
        self.toolButton_snap_grid.setMinimumSize(QSize(40, 0))
        self.icon_snap_grid = QIcon()
        self.icon_snap_grid.addFile(u"recursos/iconos/iconos_status_bar/snap_grid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_snap_grid.setIcon(self.icon_snap_grid)
        self.toolButton_snap_grid.setVisible(False)

        self.toolButton_ortho = QToolButton()
        self.toolButton_ortho.setCheckable(True)
        self.toolButton_ortho.setStyleSheet('border-color: red; background-color: #333333 ;margin: 0px 3px ')
        self.toolButton_ortho.setMinimumSize(QSize(40, 0))
        self.icon_ortho = QIcon()
        self.icon_ortho.addFile(u"recursos/iconos/iconos_status_bar/ortho.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_ortho.setIcon(self.icon_ortho)
        self.toolButton_ortho.setVisible(False)

        self.toolButton_osnap = QToolButton()
        self.toolButton_osnap.setCheckable(True)
        self.toolButton_osnap.setStyleSheet('border-color: red; background-color: #333333 ;margin: 0px 3px ')
        self.toolButton_osnap.setMinimumSize(QSize(40, 0))
        self.icon_osnap = QIcon()
        self.icon_osnap.addFile(u"recursos/iconos/iconos_status_bar/osnap.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_osnap.setIcon(self.icon_osnap)
        self.toolButton_osnap.setVisible(False)
      
        self.statusBar().addPermanentWidget(self.toolButton_osnap)
        self.statusBar().addPermanentWidget(self.toolButton_ortho)
        self.statusBar().addPermanentWidget(self.toolButton_snap_grid)
        self.statusBar().addPermanentWidget(self.label_coor)

        self.statusBar().reformat()
        

        # ::::::::::::::::::::   SHORTCUT Y STATUS DE MENÚ LATERAL ::::::::::::::::::::
        self.ui.toolButton_setting.setToolTip('Ajustes del programa [Ctrl+p]')
        self.ui.toolButton_setting.setShortcut('Ctrl+p')


        # ::::::::::::::::::::   CONFIGURANDO  FRAME SETTING ::::::::::::::::::::
        self.icon_config_select = QIcon()
        self.icon_config_select.addFile(u"recursos/iconos/iconos_menu_lateral/config_select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_config = QIcon()
        self.icon_config.addFile(u"recursos/iconos/iconos_menu_lateral/config.svg", QSize(), QIcon.Normal, QIcon.Off)


    
        # :::::::::::::::::::: BOTÓN Y PAGINA POR DEFECTO ::::::::::::::::::::
        self.previous_selected_button = 1
        self.viewToolButtonMenuLat(self.previous_selected_button)
        #self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
        #self.ui.frame_home.setStyleSheet("background-color: #36C9C6;")
        #self.ui.frame_homeInf.setStyleSheet("background-color: #2B2B2B;")       

        return
        
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        
        # ::::::::::::::::::::   EVENTOS  MENU SUPERIOR ::::::::::::::::::::
        self.ui.action_nuevo.triggered.connect(self.__triggeredActionNuevoProyecto)
        self.ui.action_abrir.triggered.connect(self.__triggeredActionAbrirProyecto)
        self.ui.action_guardar.triggered.connect(self.__triggeredActionSaveProject)
        self.ui.action_guardarComo.triggered.connect(self.__triggeredActionSaveAsProject)
        self.ui.action_deshacer.triggered.connect(self.__triggeredActionUndo)
        self.ui.action_rehacer.triggered.connect(self.__triggeredActionRedo)
        """
        #self.ui.action_importar.triggered.connect(self.triggeredActionXXXXXXXX)
        #self.ui.actionExportar.triggered.connect(self.triggeredActionXXXXXXXX)

        """
        self.ui.action_origin.triggered.connect(self.__triggeredActionShowHideOrigin)
        self.ui.action_axis.triggered.connect(self.__triggeredActionShowHideAxis)
        self.ui.action_grid.triggered.connect(self.__triggeredActionShowHideGrid)
        self.ui.action_console.triggered.connect(self.__triggeredActionShowHideConsole)
        self.ui.action_label.triggered.connect(self.__triggeredActionShowHideLabel)
        """
        """



        # ::::::::::::::::::::   EVENTOS MENU LATERAL ::::::::::::::::::::
        self.ui.toolButton_home.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawData.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawMesh.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawPoint.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_drawBoundary.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_viewResult.clicked.connect(self.__clickedToolButtonMenuLat)
        self.ui.toolButton_setting.clicked.connect(self.__clickedToolButtonMenuLat)

        
   
        # ::::::::::::::::::::   EVENTOS STATUS BAR ::::::::::::::::::::
        self.toolButton_snap_grid.clicked.connect(self.__clickedToolButtoSnapGrid)
        self.toolButton_ortho.clicked.connect(self.__clickedToolButtoOrtho)
        self.toolButton_osnap.clicked.connect(self.__clickedToolButtoOsnap)
        
        # ::::::::::::::::::::    EVENTOS  SHORTCUT    ::::::::::::::::::::    
        self.shortcut_change_thema.activated.connect(self.__activatedShortCutChangeTheme)
        return





    ###############################################################################
	# ::::::::::::::::::::           OTROS MÉTODOS             ::::::::::::::::::::
	###############################################################################
    def setPageWidget(self,page, view_page):  

        if page == "home":
            self.ui.verticalLayout_emptyHome.addWidget(view_page)

        elif page == "draw":
            self.ui.verticalLayout_emptyDraw.addWidget(view_page)

        elif page == "setting":
            self.ui.verticalLayout_emptySetting.addWidget(view_page)

        return

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS PARA MENSAJES        ::::::::::::::::::::
	###############################################################################
    def showMessageStatusBar(self,type_msn, message):
        """ imprime en la barra de estado un mensaje.               

        Args:
            type_msn(str): tipo de mensaje 
                critical
                satisfactory
                informative
            message(str): Mensaje  
        """

        if type_msn == "critical":
            self.ui.statusbar.setStyleSheet("color: #F94646;") 
            self.ui.statusbar.showMessage(message,6000)
            #self.frame_draw.msnConsole("Error",message)
        elif type_msn == "satisfactory":
            self.ui.statusbar.setStyleSheet("color: #36C9C6;") 
            self.ui.statusbar.showMessage(message,6000)
            #self.frame_draw.msnConsole("Running",message)

        elif type_msn == "informative":

            self.ui.statusbar.setStyleSheet("color: #DDDDDD;") 
            self.ui.statusbar.showMessage(message,6000)
            #self.frame_draw.msnConsole("Information",message)

    ###############################################################################
	# ::::::::::::::::::::::::      MÉTODOS GENERALES      ::::::::::::::::::::::
	###############################################################################
    def updateTitleWindow(self, name_project):
        self.setWindowTitle("MPM-UN    {}".format(name_project))

    ###############################################################################
	# ::::::::::::::::::::::::      MÉTODOS MENU LATERAL     ::::::::::::::::::::::
	###############################################################################
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

        self.ui.toolButton_setting.setIcon(self.icon_config)

    def viewToolButtonMenuLat(self, button):
        """ Muestra el botón seleccionado
        Args:
            button(int) numero de boton seleccionado
        """
        self.__resetToolButtonMenuLat()

        list_button = [
            [self.ui.frame_home, self.ui.frame_homeInf,self.ui.page_home],
            [self.ui.frame_drawData, self.ui.frame_drawDataInf,self.ui.page_draw],
            [self.ui.frame_drawMesh, self.ui.frame_drawMeshInf,self.ui.page_draw],
            [self.ui.frame_drawPoint, self.ui.frame_drawPointInf,self.ui.page_draw],
            [self.ui.frame_drawBoundary, self.ui.frame_drawBoundaryInf,self.ui.page_draw],
            [self.ui.frame_viewResult, self.ui.frame_viewResultInf,self.ui.page_view]
            ]
        
        
        self.label_coor.setVisible(False)
        self.toolButton_snap_grid.setVisible(False)
        self.toolButton_ortho.setVisible(False)
        self.toolButton_osnap.setVisible(False)

        if button == 1 or button == 2 or button == 3 or button == 4 or button == 5 or button == 6:

            list_button[button-1][0].setStyleSheet("background-color: #36C9C6;") 
            list_button[button-1][1].setStyleSheet("background-color: #526585;")            
            self.ui.stackedWidget_container.setCurrentWidget(list_button[button-1][2])

            self.label_coor.setVisible(True)
            self.toolButton_snap_grid.setVisible(True)
            self.toolButton_ortho.setVisible(True)
            self.toolButton_osnap.setVisible(True)

        elif button == 7:            
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)
            self.ui.toolButton_setting.setIcon(self.icon_config_select)
    
    def activateMenuLat(self):

        self.ui.toolButton_drawData.setEnabled(True)
        self.ui.toolButton_drawMesh.setEnabled(True)
        self.ui.toolButton_drawPoint.setEnabled(True)
        self.ui.toolButton_drawBoundary.setEnabled(True) 
        self.ui.toolButton_viewResult.setEnabled(True)



    def __clickedToolButtonMenuLat(self):
        """ Método para los eventos de los botones del menú lateral
        Se obtiene el botón que activo la señal y se redirecciona
        al botón correspondiente"""
        

        buttonSelected = self.sender()
        #print(buttonSelected.objectName())
        if buttonSelected != None:
            nameButton = buttonSelected.objectName()
        else:
            return
        self.signal_selected_menu_button.emit(nameButton)      



    ##############################################################################
	# :::::::::::::::::::::::    MÉTODOS MENU SUPERIOR   :::::::::::::::::::::::::
	##############################################################################
 

    def updateProjectsRecentMenuSup(self, list_projects_paths):
        self.clearProjectsRecentMenuSup()
        No_project = 1
        max_projects = 15
        for  path_project in list_projects_paths:
            if No_project <= max_projects and QFile.exists(path_project):
                self.addActionProjectsRecentMenuSup(path_project)
            No_project += 1        
        self.addSeparatorProjectsRecentMenuSup()

    def addActionProjectsRecentMenuSup(self, path):        
        self.ui.menu_recientes.addAction(path)

    def clearProjectsRecentMenuSup(self):        
        self.ui.menu_recientes.clear()

    def addSeparatorProjectsRecentMenuSup(self):        
   
        self.ui.menu_recientes.addSeparator()
        self.ui.menu_recientes.addAction('Limpiar')
        

        for accion in self.ui.menu_recientes.actions():
            if accion.text() == 'Limpiar':
                accion.triggered.connect(self.__triggeredAccionRecienteClearMenuSup)
            else:
                pass
                accion.triggered.connect(self.__triggeredAccionRecienteMenuSup)
   

    def __triggeredAccionRecienteMenuSup(self):
        """Método para los eventos del menú superior >> recientes"""
    
        file_path = self.sender().text()
        if file_path:
            self.signal_open_project.emit(file_path)
        return

    def __triggeredAccionRecienteClearMenuSup(self):
        """Borra los proyectos recientes."""
        self.signal_clear_recent_project.emit()
   
    def __triggeredActionNuevoProyecto(self):
        """ Abre cuadro de dialogo para nuevo proyecto. """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self,"Nuevo Pryecto","","Data files mpm (*.mpm)", options=options)
        if file_path:
            self.signal_new_project.emit(file_path)
   
    def __triggeredActionAbrirProyecto(self):
        """ Abre cuadro de dialogo para abrir proyecto. """
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self,"Abrir Pryecto","","Data files mpm (*.mpm)", options=options)
        if file_path:
            self.signal_open_project.emit(file_path)

    def __triggeredActionSaveProject(self):   
        """Guarda el proyecto"""     
        self.signal_action_menu_save.emit()


    def __triggeredActionSaveAsProject(self):   
        """ Guarda en ruta diferente el proyecto """

        options = QFileDialog.Options()
        new_path_file, _ = QFileDialog.getSaveFileName(self,"Guardar proyecto como","","Data files mpm (*.mpm)", options=options)
        if new_path_file:
            self.signal_action_menu_saveAs.emit(new_path_file)


    def __triggeredActionUndo(self):   
        """ """
        self.signal_action_menu_undo.emit()
  

    def __triggeredActionRedo(self):   
        """ """
        self.signal_action_menu_redo.emit()


    def __triggeredActionShowHideOrigin(self):        
        """ envia a la scena draw el modo de origen true para ver y false para ocultar"""   
        value = self.ui.action_origin.isChecked()
        self.signal_action_menu_viewDraw.emit(["ShowHideOrigin",value])
                
    def __triggeredActionShowHideAxis(self):        
        """ envia a la scena draw el modo de ejes true para ver y false para ocultar"""
        value = self.ui.action_axis.isChecked()
        self.signal_action_menu_viewDraw.emit(["ShowHideAxis",value])
                
    def __triggeredActionShowHideGrid(self):        
        """ envia a la scena draw el modo de grilla true para ver y false para ocultar"""
        value = self.ui.action_grid.isChecked()
        self.signal_action_menu_viewDraw.emit(["ShowHideGrid",value])     

    def __triggeredActionShowHideConsole(self):        
        """ envia a la scena draw el modo de consola true para ver y false para ocultar"""
        value = self.ui.action_console.isChecked()
        self.signal_action_menu_viewDraw.emit(["ShowHideConsole",value])

    def __triggeredActionShowHideLabel(self):        
        """ envia a la scena draw el modo de etiquetas true para ver y false para ocultar"""
        value = self.ui.action_label.isChecked()
        self.signal_action_menu_viewDraw.emit(["ShowHideLabel",value])


    def __activatedShortCutChangeTheme(self):
        """cambia de tema en los tres disponibles"""
        self.signal_change_theme.emit()
        

    ###############################################################################
	# ::::::::::::::::        MÉTODOS PARA BARRA DE ESTADO         ::::::::::::::::
	###############################################################################
    def __clickedToolButtoSnapGrid(self,mode):
       
       self.signal_toolButton_statusBar.emit(["SnapGrid",mode])
 
    def __clickedToolButtoOrtho(self,mode):
       self.signal_toolButton_statusBar.emit(["Ortho",mode])
       
    def __clickedToolButtoOsnap(self,mode):
       self.signal_toolButton_statusBar.emit(["Osnap",mode])


    def setTextStatusCoor(self, x, y):
        self.label_coor.setText("{:.3f}, {:.3f}".format(x,y))
    
    def modeConsoleDraw(self,state):
        self.ui.action_console.setChecked(state)

  
    def projectChanges(self, name_project, there_are_changes):
        """cambia el estado del proyecto 

        Args:
            there_are_changes(bool): 
                        True >>> si se realizó cambios en el proyecto
                        False >>> si no hay cambios en el proyecto

        """
        if there_are_changes == True:     
            self.setWindowTitle("MPM-UN    •• {} ••".format(name_project))
        else:
            self.setWindowTitle("MPM-UN    {}".format(name_project))

     
    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################
    
    def closeEvent(self, event):
        """Evento al cerrar la ventana main window"""
        event.ignore()
        self.signal_close_app.emit()