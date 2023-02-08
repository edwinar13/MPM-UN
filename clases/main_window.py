""" Este módulo contiene la clase iniciar Ui_MainWindow.
es la ventana principal del programa."""
from datetime import datetime
from PySide6.QtCore import ( QFile, Slot,QSize,Qt,QTimer)
from PySide6.QtWidgets import (QApplication, QMainWindow,QFileDialog,
QFrame, QSizePolicy,QLabel,QPushButton,QComboBox,QToolButton,QUndoView)
from PySide6.QtGui import (QIcon,QScreen,QShortcut,QKeySequence,QKeyEvent, QUndoStack)
from ui import ui_main_window
from clases import class_projects
from clases import class_ui_frame_home
from clases import class_ui_frame_draw
from clases import database_class
from clases import class_ui_dialog_msg


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

        # iniciando Tiempo de autoguardado
        # = tiempo * (60seg) * (1000*miliseg)
        self.autosave = False
        self.mili_second_save = 60 * 60 * 1000 # Tiempo
        self.timer_save = QTimer()
        self.timer_save.setObjectName("timer_save")
        self.timer_save.timeout.connect(self.__save_auto)
        self.timer_save.start( self.mili_second_save)

        #Inicia el objeto db de del programa
        self.db_config_mpmun = database_class.DataBaseConfigMpmun()
        

        # Iniciando objeto proyectos 
        self.projects = class_projects.Projects(self.db_config_mpmun)        
        self.__updateProjectsRecent()

        # Recuperando ajustes de la app 
        setting = self.db_config_mpmun.selectSettingDB()
        self.__iniSetting(setting)
        self.setting = True


        self.undoStack = QUndoStack(self)
        self.createUndoView()





        


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
        self.showMaximized()
        #self.setFixedSize(QSize(1000,700))



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
        self.ui.action_origin.setShortcut('F6')
        self.ui.action_axis.setChecked(True)
        self.ui.action_axis.setShortcut('F7')
        self.ui.action_grid.setChecked(True)
        self.ui.action_grid.setShortcut('F8')
        self.ui.action_console.setChecked(True)
        self.ui.action_console.setShortcut('F9')



  

        self.shortcut_change_thema = QShortcut(QKeySequence('Ctrl++'), self)
        self.shortcut_change_thema.setObjectName("shortcut_change_thema")



        # ::::::::::::::::::::   WIDGET BARRA DE ESTADO ::::::::::::::::::::
        #-----------------------------------------------------------------------------------
        
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

        #self.statusBar().addPermanentWidget(VLine())    # <---
        
        self.statusBar().addPermanentWidget(self.toolButton_osnap)
        self.statusBar().addPermanentWidget(self.toolButton_ortho)
        self.statusBar().addPermanentWidget(self.toolButton_snap_grid)
        self.statusBar().addPermanentWidget(self.label_coor)

        self.statusBar().reformat()
        '''
        self.statusBar().setStyleSheet('border: 0; background-color: #FFF8DC;')
        self.statusBar().setStyleSheet("QStatusBar::item {border: none;}") 
        '''




        # ::::::::::::::::::::   SHORTCUT Y STATUS DE MENÚ LATERAL ::::::::::::::::::::
        self.ui.toolButton_setting.setToolTip('Ajustes del programa [Ctrl+p]')
        self.ui.toolButton_setting.setShortcut('Ctrl+p')

        # ::::::::::::::::::::   CONFIGURANDO  FRAME INICIO ::::::::::::::::::::
        self.frame_home = class_ui_frame_home.FrameHome(self)
        self.ui.verticalLayout_emptyHome.addWidget(self.frame_home)

        # ::::::::::::::::::::   CONFIGURANDO  FRAME DRAW ::::::::::::::::::::
        self.frame_draw = class_ui_frame_draw.FrameDraw(self)
        self.ui.verticalLayout_emptyDraw.addWidget(self.frame_draw)


        # ::::::::::::::::::::   CONFIGURANDO  FRAME SETTING ::::::::::::::::::::
        self.icon_config_select = QIcon()
        self.icon_config_select.addFile(u"recursos/iconos/iconos_menu_lateral/config_select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_config = QIcon()
        self.icon_config.addFile(u"recursos/iconos/iconos_menu_lateral/config.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.horizontalSlider_1.setRange(0,100)
        self.ui.spinBox_1.setRange(0,100)
        self.ui.horizontalSlider_2.setRange(5,50)



 

        # :::::::::::::::::::: BOTÓN Y PAGINA POR DEFECTO ::::::::::::::::::::
        self.previous_selected_button = 1
        self.__viewToolButtonMenuLat(self.previous_selected_button)
        #self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
        #self.ui.frame_home.setStyleSheet("background-color: #36C9C6;")
        #self.ui.frame_homeInf.setStyleSheet("background-color: #2B2B2B;")
        




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
        self.frame_draw.signal_coor_mouse.connect(self._printStatusBarCoor)
        self.frame_draw.signal_console_hise_show.connect(self._console_hise_show)

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
        self.ui.action_deshacer.triggered.connect(self.__triggeredActionUndo)
        self.ui.action_rehacer.triggered.connect(self.__triggeredActionRedo)
        #self.ui.action_importar.triggered.connect(self.triggeredActionXXXXXXXX)
        #self.ui.actionExportar.triggered.connect(self.triggeredActionXXXXXXXX)
        self.ui.action_abrir.triggered.connect(self.__triggeredActionAbrirProyecto)

        self.ui.action_origin.triggered.connect(self.__triggeredActionShowHideOrigin)
        self.ui.action_axis.triggered.connect(self.__triggeredActionShowHideAxis)
        self.ui.action_grid.triggered.connect(self.__triggeredActionShowHideGrid)
        self.ui.action_console.triggered.connect(self.__triggeredActionShowHideConsole)


        # ::::::::::::::::::::   EVENTOS STATUS BAR ::::::::::::::::::::
        self.toolButton_snap_grid.clicked.connect(self.__clickedToolButtoSnapGrid)
        self.toolButton_ortho.clicked.connect(self.__clickedToolButtoOrtho)
        self.toolButton_osnap.clicked.connect(self.__clickedToolButtoOsnap)



        # ::::::::::::::::::::    EVENTOS  SETTING    ::::::::::::::::::::    
        self.ui.horizontalSlider_1.valueChanged.connect(self.__updateSetting)
        self.ui.spinBox_1.valueChanged.connect(self.__updateSetting)
        self.ui.horizontalSlider_2.valueChanged.connect(self.__updateSetting)
        self.ui.comboBox_3.currentIndexChanged.connect(self.__updateSetting)

        self.ui.doubleSpinBox_grid_spacing.valueChanged.connect(self.__updateSetting)
        self.ui.checkBox_grid_adaptative.stateChanged.connect(self.__updateSetting)
        self.ui.doubleSpinBox_snap_grid_spacing.valueChanged.connect(self.__updateSetting)
        self.ui.checkBox_snap_grid_adaptative.stateChanged.connect(self.__updateSetting)

        self.ui.comboBox_intervalAutoSave.currentIndexChanged.connect(self.__updateSetting)
        self.ui.checkBox_autoSave.stateChanged.connect(self.__updateSetting)



        # ::::::::::::::::::::    EVENTOS  SHORTCUT    ::::::::::::::::::::    
        self.shortcut_change_thema.activated.connect(self.__activatedShortCutChangeTheme)

    ###############################################################################
	# ::::::::::::::::::::    MÉTODOS DE EVENTOS MENU LATERAL   ::::::::::::::::::::
	###############################################################################
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
        
        if nameButton==self.ui.toolButton_home.objectName() : 
            self.previous_selected_button = 1
            self.__viewToolButtonMenuLat(self.previous_selected_button)
            self.setting = True


        elif nameButton==self.ui.toolButton_drawData.objectName() :
            self.previous_selected_button = 2
            self.__viewToolButtonMenuLat(self.previous_selected_button)
            self.frame_draw.showHideDrawMenu("Data")
            self.setting = True

        elif nameButton==self.ui.toolButton_drawMesh.objectName() :
            self.previous_selected_button = 3
            self.__viewToolButtonMenuLat(self.previous_selected_button)
            self.frame_draw.showHideDrawMenu("Mesh")
            self.setting = True

        elif nameButton==self.ui.toolButton_drawPoint.objectName() :
            self.previous_selected_button = 4
            self.__viewToolButtonMenuLat(self.previous_selected_button) 
            self.frame_draw.showHideDrawMenu("Point")
            self.setting = True

        elif nameButton==self.ui.toolButton_drawBoundary.objectName() :
            self.previous_selected_button = 5
            self.__viewToolButtonMenuLat(self.previous_selected_button) 
            self.frame_draw.showHideDrawMenu("Boundary")
            self.setting = True
            

        elif nameButton==self.ui.toolButton_viewResult.objectName():
            self.previous_selected_button = 6
            self.__viewToolButtonMenuLat(self.previous_selected_button)
            self.setting = True
        
        elif nameButton==self.ui.toolButton_setting.objectName():
            if self.setting == True :
                self.__viewToolButtonMenuLat(7)
                self.setting = False
            elif self.setting == False:            
                self.__viewToolButtonMenuLat(self.previous_selected_button)
                self.setting = True
            


            
        

    ###############################################################################
	# ::::::::::::::::::::  MÉTODOS DE EVENTOS MENU SUPERIOR  ::::::::::::::::::::
	###############################################################################
        
    def __activatedShortCutChangeTheme(self):
        """cambia de tema en los tres disponibles"""
        index_theme = self.ui.comboBox_3.currentIndex()
        if index_theme ==2:
            self.ui.comboBox_3.setCurrentIndex(0)
        else:
            self.ui.comboBox_3.setCurrentIndex(index_theme+1)

      
    
    def __activatedShortCutEsc(self):
        """Al presionar ESC ejecuta aciones contenidas en la lista. """
        self.__viewToolButtonMenuLat(self.previous_selected_button)
        self.setting = True

        
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
        triggered = self.sender()
        if self.__actual_project != None :
            if self.__actual_project.checkProjectChanges():
                if triggered.objectName() == "timer_save":
                    self.__showMessageCommand("_autoSave")
                else:
                    self.__showMessageCommand("_save")
                self.__actual_project.saveData()
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
    def createUndoView(self):

        undoView = QUndoView(self.undoStack)
        undoView.setWindowTitle("Command List")
        undoView.show()
        undoView.setAttribute(Qt.WA_QuitOnClose, False)
        print("adadadad")

    def __triggeredActionUndo(self):   
        """ """
        self.frame_draw.undo()

    def __triggeredActionRedo(self):   
        """ """
        self.frame_draw.redo()
        
    
    def __triggeredActionShowHideOrigin(self):        
        """ envia a la scena draw el modo del origen true para ver y false para ocultar"""   
        self.frame_draw.mode_origin_draw(self.ui.action_origin.isChecked())
                
    def __triggeredActionShowHideAxis(self):        
        """ envia a la scena draw el modo del axis true para ver y false para ocultar"""
        self.frame_draw.mode_axis_draw(self.ui.action_axis.isChecked())
                
    def __triggeredActionShowHideGrid(self):        
        """ envia a la scena draw el modo del grilla true para ver y false para ocultar"""
        self.frame_draw.mode_grid_draw(self.ui.action_grid.isChecked())
                
    def __triggeredActionShowHideConsole(self):        
        """ envia a la scena draw el modo del grilla true para ver y false para ocultar"""
        self.frame_draw.mode_console_draw(self.ui.action_console.isChecked())

          
    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS DE EVENTOS SETTING     ::::::::::::::::::::
	###############################################################################
    def __updateSetting(self,value=0,updateAll=False):
        """Método para los eventos de los widget de setting. Se obtiene el widget
         que activo la señal y se redirecciona al widget correspondiente"""
        widgetSelected = self.sender()
        nameWidget=""
        if widgetSelected != None:        
            nameWidget = widgetSelected.objectName()

        
	    # ::::::::::::::::::::    SETTING Pantalla de dibujo    ::::::::::::::::::::
        if nameWidget==self.ui.horizontalSlider_1.objectName() or updateAll:
            self.ui.spinBox_1.setValue(self.ui.horizontalSlider_1.value())

        if nameWidget==self.ui.spinBox_1.objectName() or updateAll:
            value_crosshair_size = self.ui.spinBox_1.value()
            self.ui.horizontalSlider_1.setValue(value_crosshair_size)
            self.frame_draw.view_draw_1.crosshair_size=(value_crosshair_size)/100
            self.frame_draw.view_draw_2.crosshair_size=(value_crosshair_size)/100
            self.db_config_mpmun.updateSettingDB(0,"TamanoCruzPuntero", value_crosshair_size)

        if nameWidget==self.ui.horizontalSlider_2.objectName() or updateAll:            
            value_pick_box_size = (self.ui.horizontalSlider_2.value())
            value_Margin =18 * (1-((value_pick_box_size-5)/45))           
            self.ui.frame_4.setContentsMargins(value_Margin, value_Margin, value_Margin, value_Margin)
            self.frame_draw.view_draw_1.pick_box_size =(value_pick_box_size)
            self.frame_draw.view_draw_2.pick_box_size =(value_pick_box_size)
            self.db_config_mpmun.updateSettingDB(0,"TamanoCajaPuntero", value_pick_box_size)
            

        if nameWidget==self.ui.comboBox_3.objectName() or updateAll:
            index_style_view_scene = self.ui.comboBox_3.currentIndex()
            self.db_config_mpmun.updateSettingDB(0,"EstiloVista", index_style_view_scene)
            self.frame_draw.scene_draw.setStyleScene(index_style_view_scene)
            self.frame_draw.view_draw_1.setStyleView(index_style_view_scene)
            self.frame_draw.view_draw_2.setStyleView(index_style_view_scene)




        if nameWidget==self.ui.checkBox_grid_adaptative.objectName() or updateAll:
            check_grid_adaptative = self.ui.checkBox_grid_adaptative.isChecked() 
            grid_spacing = self.ui.doubleSpinBox_grid_spacing.value()           
            if check_grid_adaptative:
                self.ui.doubleSpinBox_grid_spacing.setEnabled(False)
                self.frame_draw.view_draw_1.grid_adaptative = True
                self.frame_draw.view_draw_2.grid_adaptative = True
            else:
                self.ui.doubleSpinBox_grid_spacing.setEnabled(True)
                self.frame_draw.view_draw_1.grid_adaptative = False
                self.frame_draw.view_draw_1.grid_spacing = grid_spacing
                self.frame_draw.view_draw_2.grid_adaptative = False
                self.frame_draw.view_draw_2.grid_spacing = grid_spacing
                self.frame_draw.scene_draw.grid_spacing = grid_spacing

            self.db_config_mpmun.updateSettingDB(0,"GrillaAdaptativa", check_grid_adaptative)
            self.db_config_mpmun.updateSettingDB(0,"EspacioGrilla", grid_spacing)

        if nameWidget==self.ui.doubleSpinBox_grid_spacing.objectName() or updateAll:
            grid_spacing = self.ui.doubleSpinBox_grid_spacing.value()           
            self.frame_draw.view_draw_1.grid_spacing = grid_spacing
            self.frame_draw.view_draw_2.grid_spacing = grid_spacing
            self.frame_draw.scene_draw.grid_spacing = grid_spacing
            self.db_config_mpmun.updateSettingDB(0,"EspacioGrilla", grid_spacing)


        if nameWidget==self.ui.checkBox_snap_grid_adaptative.objectName() or updateAll:
            check_snap_grid_adaptative = self.ui.checkBox_snap_grid_adaptative.isChecked()
            snap_grid_spacing = self.ui.doubleSpinBox_snap_grid_spacing.value() 

            if check_snap_grid_adaptative:
                self.ui.doubleSpinBox_snap_grid_spacing.setEnabled(False)
                self.frame_draw.scene_draw.snap_grid_adaptative = True
                
            else:
                self.ui.doubleSpinBox_snap_grid_spacing.setEnabled(True)
                self.frame_draw.scene_draw.snap_grid_adaptative = False
                self.frame_draw.scene_draw.snap_grid_spacing = snap_grid_spacing

            self.db_config_mpmun.updateSettingDB(0,"SnapGrillaAdaptativa", check_snap_grid_adaptative)
            self.db_config_mpmun.updateSettingDB(0,"EspacioSnapGrilla", snap_grid_spacing)


        if nameWidget==self.ui.doubleSpinBox_snap_grid_spacing.objectName() or updateAll:
            snap_grid_spacing = self.ui.doubleSpinBox_snap_grid_spacing.value() 
            self.frame_draw.scene_draw.snap_grid_spacing = snap_grid_spacing
            self.db_config_mpmun.updateSettingDB(0,"EspacioSnapGrilla", snap_grid_spacing)
        




        
        if nameWidget==self.ui.checkBox_autoSave.objectName() or updateAll:
            check_auto_save = self.ui.checkBox_autoSave.isChecked()            
            if check_auto_save:
                self.ui.comboBox_intervalAutoSave.setEnabled(True)
                self.autosave = True
            else:
                self.ui.comboBox_intervalAutoSave.setEnabled(False)
                self.autosave = False
            self.db_config_mpmun.updateSettingDB(1,"GuardadoAutomatico", check_auto_save)

        if nameWidget==self.ui.comboBox_intervalAutoSave.objectName() or updateAll:
            index = self.ui.comboBox_intervalAutoSave.currentIndex()  
            self.db_config_mpmun.updateSettingDB(1,"IntervaloAutoGuardado", index)
            if index == 0:
                self.mili_second_save = 5 * 60 * 1000
            elif index == 1:
                self.mili_second_save = 15 * 60 * 1000
            elif index == 2:
                self.mili_second_save = 30 * 60 * 1000
            elif index == 3:
                self.mili_second_save = 60 * 60 * 1000
            self.timer_save.setInterval(self.mili_second_save)
    
    def __save_auto(self):
        """Método para la señal de tiempo para auto guardado,
        debe estar activada la función para guardar """
        if self.autosave:
            self.now = datetime.now() 
            self.hour = self.now.hour
            self.minute = self.now.minute
            self.second = self.now.second
            self.microsecond = self.now.microsecond
            self.__triggeredActionSaveProject()

            print("autoSave: {}:{}:{},{}".format(
                self.hour, self.minute ,self.second, self.microsecond ))

        else:
            print("Not auto save")

    ###############################################################################
	# ::::::::::::::::::::         FUNCIONES GENERALES UI      ::::::::::::::::::::
	###############################################################################
    

    # ::::::::::::::::::::  FUNCIONES PAGE SETTING  ::::::::::::::::::::
    def __iniSetting(self, setting):
        """Actualiza las configuraciones de la app.

        Args:
            setting (list): Lista con las configuraciones.
        
        """
        # Setting Pantalla de dibujo
        TamanoCruzPuntero=(setting[0]["TamanoCruzPuntero"])
        self.ui.horizontalSlider_1.setValue(TamanoCruzPuntero)        
        TamanoCajaPuntero=(setting[0]["TamanoCajaPuntero"])
        self.ui.horizontalSlider_2.setValue(TamanoCajaPuntero)
        EstiloVista=(setting[0]["EstiloVista"])
        self.ui.comboBox_3.setCurrentIndex(EstiloVista)

        GrillaAdaptativa=(setting[0]["GrillaAdaptativa"])
        self.ui.checkBox_grid_adaptative.setChecked(GrillaAdaptativa) 
        EspacioGrilla=(setting[0]["EspacioGrilla"])
        self.ui.doubleSpinBox_grid_spacing.setValue(EspacioGrilla)   

        SnapGrillaAdaptativa=(setting[0]["SnapGrillaAdaptativa"])
        self.ui.checkBox_snap_grid_adaptative.setChecked(SnapGrillaAdaptativa)
        EspacioSnapGrilla=(setting[0]["EspacioSnapGrilla"])
        self.ui.doubleSpinBox_snap_grid_spacing.setValue(EspacioSnapGrilla) 

        GuardadoAutomatico=(setting[1]["GuardadoAutomatico"])
        self.ui.checkBox_autoSave.setChecked(GuardadoAutomatico)
        IntervaloAutoGuardado=(setting[1]["IntervaloAutoGuardado"])
        self.ui.comboBox_intervalAutoSave.setCurrentIndex(IntervaloAutoGuardado)

        self.__updateSetting(updateAll=True)

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

        self.ui.toolButton_setting.setIcon(self.icon_config)
    
    def __viewToolButtonMenuLat(self, button):
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
            list_button[button-1][1].setStyleSheet("background-color: #2B2B2B;")
            self.ui.stackedWidget_container.setCurrentWidget(list_button[button-1][2])
            if button == 2:
                self.frame_draw.showHideDrawMenu("Data")
                self.label_coor.setVisible(True)
                self.toolButton_snap_grid.setVisible(True)
                self.toolButton_ortho.setVisible(True)
                self.toolButton_osnap.setVisible(True)

            elif button == 3:
                self.frame_draw.showHideDrawMenu("Mesh")
                self.label_coor.setVisible(True)
                self.toolButton_snap_grid.setVisible(True)
                self.toolButton_ortho.setVisible(True)
                self.toolButton_osnap.setVisible(True)

            elif button == 4:
                self.frame_draw.showHideDrawMenu("Point")
                self.label_coor.setVisible(True)
                self.toolButton_snap_grid.setVisible(True)
                self.toolButton_ortho.setVisible(True)
                self.toolButton_osnap.setVisible(True)

            elif button == 5:
                self.frame_draw.showHideDrawMenu("Boundary")
                self.label_coor.setVisible(True)
                self.toolButton_snap_grid.setVisible(True)
                self.toolButton_ortho.setVisible(True)
                self.toolButton_osnap.setVisible(True)

        elif button == 7:            
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)
            self.ui.toolButton_setting.setIcon(self.icon_config_select)

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
                

                self.previous_selected_button = 2
                self.__viewToolButtonMenuLat(self.previous_selected_button)
                self.label_coor.setVisible(True)
                self.toolButton_snap_grid.setVisible(True)
                self.toolButton_ortho.setVisible(True)
                self.toolButton_osnap.setVisible(True)
                self.__showMessageInformative("Se ha abierto el proyecto: {}".format(self.__actual_project.getName()))


                """              ███▀▀▀▀▀ deberia actualizar todo ▀▀▀▀▀███                 """
                self.frame_draw.configDrawMenuData(project = self.__actual_project)
                self.frame_draw.configDrawItemsScene(project = self.__actual_project)

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
    def __showMessageCommand(self, command):
        """ imprime en la consola un comando.

        Args:
            command(str): comando  

        """
        self.frame_draw.msnConsole("Command",command)
    
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
	# ::::::::::::::::        MÉTODOS PARA BARRA DE ESTADO         ::::::::::::::::
	###############################################################################
    def __clickedToolButtoSnapGrid(self,mode):
       self.frame_draw.scene_draw.mode_snap_grid = mode
 
    def __clickedToolButtoOrtho(self,mode):
        self.frame_draw.scene_draw.mode_ortho = mode
       
    def __clickedToolButtoOsnap(self,mode):
        self.frame_draw.scene_draw.mode_osnap = mode
      

    
    @Slot(list)
    def _printStatusBarCoor(self, coor_list):
        """ imprime en la barra de estado las coordenadas del mouse al moverse por el QGraphics.

        Args:
            coor_list(list): coordenada X y Y
        """
        x = round(coor_list[0],4)
        y = round(coor_list[1],4)
        self.label_coor.setText("{:.3f}, {:.3f}".format(x,y))
      

    
    @Slot(bool)
    def _console_hise_show(self,state):
        self.ui.action_console.setChecked(state)

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



    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Evento al presionar una tecla de la A a la Z,   para escribir comando en la consola."""
        key = event.key()
        try:
            if key == 16777216:                       
                self.__activatedShortCutEsc()
            return super().keyPressEvent(event)
        except UnicodeDecodeError:
            print("no puede decodificar Ejemplo: Ñ ")