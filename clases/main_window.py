

from sqlite3 import connect
from PySide6.QtCore import ( QFile,QTime, QObject,QEvent, Signal, Slot,QSize)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QMainWindow,QFileDialog,QLabel,
                            QWidget,QMessageBox,QFrame, QGraphicsDropShadowEffect,QSizePolicy )
from time import strftime

from ui import ui_main_window
from ui import ui_frame_draw

from clases import class_projects
from clases import class_card_view
from clases import class_data_project
from clases import class_frame_home




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main_window.Ui_MainWindow()        
        self.ui.setupUi(self)

        
        #::::::::::::::::::::  CONFIGURANDO MAIN WINDOW::::::::::::::::::::
        """
        with open("css/styles_oscuro.css") as f:
            self.setStyleSheet(f.read())
        self.showMaximized()
        """
        self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
        self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
        self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")
        self.showMessageStatusBarInformative("Programa iniciado correctamente")



        # ::::::::::::::::::::   CONFIGURANDO  FRAME INICIO ::::::::::::::::::::
        self.frame_home = class_frame_home.FrameHome(self)
        self.ui.verticalLayout_empty_draw.addWidget(self.frame_home)

        self.list_view_card = []

        # ::::::::::::::::::::   CONFIGURANDO FRAME VIEW  ::::::::::::::::::::
        self.ui.splitter.setStretchFactor(0, 100)
        self.ui.splitter.setStretchFactor(1, 0)        
        self.ui.splitter.setSizes([100,100]) 

        
        # ::::::::::::::::::::   INICIANDO DATA PROJECTS ::::::::::::::::::::
        self.projects = class_projects.Projects()        
        self.functionUpdateListProjects()

        # ::::::::::::::::::::   CONFIGURANDO FRAME DATA PROJECT  ::::::::::::::::::::
        self.menuDataProject = class_data_project.DataProject()
        self.ui.horizontalLayout_draw.addWidget(self.menuDataProject)

        # ::::::::::::::::::::   EVENTOS WIDGET  MENU LATERAL ::::::::::::::::::::
        self.ui.toolButton_inicio.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_data.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_malla.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_puntos.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_contorno.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_resultados.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_config.clicked.connect(self.onClickedToolButtonMenuLat)

        # ::::::::::::::::::::   EVENTOS WIDGET FRAME INICIO ::::::::::::::::::::
        #self.cardProject.trigger.connect(self.functionOpenProject)
        self.frame_home.signal_home_open.connect(self.functionOpenProject)
        self.frame_home.signal_home_new.connect(self.onTriggeredactionNuevoProyecto)
        
        # ::::::::::::::::::::   EVENTOS WIDGET FRAME DRAW DATA PROJECT ::::::::::::::::::::
        self.menuDataProject.signal_msn_critical.connect(self.showMessageStatusBarCritical)
        self.menuDataProject.signal_msn_Satisfactory.connect(self.showMessageStatusBarSatisfactory)
        self.menuDataProject.signal_msn_Informative.connect(self.showMessageStatusBarInformative)



        # ::::::::::::::::::::   EVENTOS TECLADO Y MENU SUPERIOR ::::::::::::::::::::
        self.ui.actionNuevo.setShortcut('Ctrl+n')
        self.ui.actionNuevo.setStatusTip('Nuevo')
        self.ui.actionNuevo.triggered.connect(self.onTriggeredactionNuevoProyecto)
        self.ui.actionAbrir.setShortcut('Ctrl+o')
        self.ui.actionAbrir.setStatusTip('Abrir')
        self.ui.actionAbrir.triggered.connect(self.onTriggeredactionAbrirProyecto)

        self.ui.actionGuardar.setShortcut('Ctrl+g')
        self.ui.actionGuardar.setStatusTip('Guardar')
        #self.ui.actionGuardar.triggered.connect(self.onTriggeredactionNuevoProyecto)
        self.ui.actionGuardar_como.setShortcut('Ctrl+shift+g')
        self.ui.actionGuardar_como.setStatusTip('Guardar como')
        #self.ui.actionGuardar_como.triggered.connect(self.onTriggeredactionNuevoProyecto)
        self.ui.actionImportar.setShortcut('Ctrl+i')
        self.ui.actionImportar.setStatusTip('Importar')
        #self.ui.actionImportar.triggered.connect(self.onTriggeredactionNuevoProyecto)
        self.ui.actionExportar.setShortcut('Ctrl+e')
        self.ui.actionExportar.setStatusTip('Exportar')
        #self.ui.actionExportar.triggered.connect(self.onTriggeredactionNuevoProyecto)
        
        

        """
    @Slot(str)
    def updateLabel(self, text="algo"):
        print("Estas en main: {}".format(text))
        self.ui.label_title_1.setText(text)
        """   

    ###############################################################################
	# ::::::::::::::::::::    FUNCIONES EVENTOS MENU LATERAL   ::::::::::::::::::::
	###############################################################################
    def onClickedToolButtonViewCard(self):
        buttonSelected = self.sender()
        nameButton = buttonSelected.objectName()
        print("="*30)
        print("Nombre: {}".format(nameButton))
        print("objeto: {}".format(buttonSelected))
        print("="*30)

    def onClickedToolButtonMenuLat(self):
        self.hideToolButtonMenuLat()
        buttonSelected = self.sender()
        nameButton = buttonSelected.objectName()
        if nameButton=="toolButton_inicio":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
            self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
            self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")  

        if nameButton=="toolButton_data":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_data)
            self.ui.frame_data.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_dataInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_malla":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_mesh)
            self.ui.frame_malla.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_mallaInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_puntos":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_point)
            self.ui.frame_puntos.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_puntosInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_contorno":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            #self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_contour)
            self.ui.frame_contorno.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_contornoInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_resultados":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_view)
            self.ui.frame_resultados.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_resultadosInf.setStyleSheet("background-color: #2B2B2B;") 


        if nameButton=="toolButton_config":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)
            

    def hideToolButtonMenuLat(self):
        self.ui.frame_inicio.setStyleSheet("background-color: #333333;") 
        self.ui.frame_data.setStyleSheet("background-color: #333333;") 
        self.ui.frame_malla.setStyleSheet("background-color: #333333;") 
        self.ui.frame_puntos.setStyleSheet("background-color: #333333;") 
        self.ui.frame_contorno.setStyleSheet("background-color: #333333;") 
        self.ui.frame_resultados.setStyleSheet("background-color: #333333;") 

        self.ui.frame_resultadosInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_inicioInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_dataInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_contornoInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_puntosInf.setStyleSheet("background-color: #333333;") 
        self.ui.frame_mallaInf.setStyleSheet("background-color: #333333;") 
    

    ###############################################################################
	# ::::::::::::::::::::         FUNCIONES GENERALES UI      ::::::::::::::::::::
	###############################################################################
    #desactivar botones
    

    ###############################################################################
	# ::::::::::::::::::::  FUNCIONES Y EVENTOS MENU SUPERIOR  ::::::::::::::::::::
	###############################################################################

    # ::::::::::::::::::::  EVENTOS MENU SUPERIOR  ::::::::::::::::::::

    def onTriggeredactionNuevoProyecto(self):
        """ ABRE CUADRO DE DIALOGO PARA NUEVO PROYECTO"""
        nameCurrent = self.windowTitle()
        self.setWindowTitle("MPM-UN -- Untitled document*")
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getSaveFileName(self,"New Project","","Data files mpm (*.mpm)", options=options)
        if filePath:
            if self.projects.newFileProject(filePath):
                fileName = filePath.split('/')[-1]
                self.setWindowTitle("MPM-UN -- {}".format(fileName))
                self.showMessageStatusBarSatisfactory("Proyecto creado con éxito")
                self.functionOpenProject(filePath) 
        else:
            self.setWindowTitle(nameCurrent)

    def onTriggeredactionAbrirProyecto(self):
        """ ABRE CUADRO DE DIALOGO PARA ABRIR PROYECTO"""

        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(self,"Open Project","","Data files mpm (*.mpm)", options=options)
        if filePath:
            self.functionOpenProject(filePath)
    
    def onTriggeredaccionRecienteClear(self):
        """BORRA LOS PROYECTOS RECIENTES"""
        if self.projects.deleteProjects(self):
            self.functionUpdateListProjects()
        else:
            self.functionQMessageBox('Error función onTriggeredaccionRecienteClear')

    def onTriggeredaccionReciente(self):
        '''
        Funcion de Menu recientes
        '''
        fileName = self.sender().text()
        if fileName:
            self.functionOpenProject(fileName)

# ::::::::::::::::::::  FUNCIONES MENU SUPERIOR  ::::::::::::::::::::
    @Slot(str)
    def functionOpenProject (self, filePath):
        '''
        Project
        Funcion para abril, actualizar y leer proyectos 
        muestra canvas y habilita pestaña malla
        '''
        hour = QTime.currentTime().toString("hh:mm:ss A ")
        data = strftime("%d/%m/%y")

        file_name=filePath.split('/')[-1]
        if ( QFile.exists(filePath)):

            project_open = class_projects.Project(name_file = file_name, path = filePath,data= data,hour= hour) 
        
            if self.projects.addProject(self, project_open):

                self.setWindowTitle("MPM-UN -- {}".format(file_name))
                self.ui.toolButton_data.setEnabled(True)
                self.ui.toolButton_malla.setEnabled(True)
                self.ui.toolButton_puntos.setEnabled(True)
                self.ui.toolButton_contorno.setEnabled(True)
                self.hideToolButtonMenuLat()
                self.ui.frame_data.setStyleSheet("background-color: #36C9C6;") 
                self.ui.frame_dataInf.setStyleSheet("background-color: #2B2B2B;")
                self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
                self.showMessageStatusBarInformative("Se ha abierto el proyecto {}".format(file_name))


                self.menuDataProject.setPathProject(filePath)
                self.menuDataProject.setTextWidget()

        else:
            self.showMessageStatusBarCritical("No se ha encontrado el documento {}".format(file_name)) 
        self.functionUpdateListProjects()
    
    def functionUpdateListProjects(self):
        """ACTUALIZA PROYECTOS RECIENTES """
        view_card=None
        if len(self.list_view_card) != 0:
            for view_card in self.list_view_card:                
                self.frame_home.verticalLayout_FH_container_card.removeWidget(view_card)
                view_card.deleteLater()
            self.list_view_card=[]
        self.ui.menuRecientes.clear()

        if self.projects.getProjects():
            projects = self.projects.getProjects()	
            
            total_projects = len(projects)
            No_proyecto = 1
            max_projects = 15
            positions = [(i,j) for i in range(5) for j in range(3)]  
            for position, project in zip(positions, projects):
                #agrega cada proyecto a menu>recientes
                name=project.getData()[0]
                path=project.getData()[1]
                data=project.getData()[2]
                hour=project.getData()[3]
                
                if No_proyecto <= max_projects and QFile.exists(path):
                    self.ui.menuRecientes.addAction(path)


                    self.cardProject = class_card_view.viewCardProject(self, cardName = name,
                                         cardDataTime = data, cardPath= path, cardHour= hour)
                    #self.cardProject.setStyleSheet("background-color: #36C{}C6;".format(No_proyecto))
                    #self.frame_home.gridLayout_proyectos.addWidget(self.cardProject,*position)
                    self.frame_home.verticalLayout_FH_container_card.addWidget(self.cardProject)
                    self.list_view_card.append(self.cardProject)
                    self.cardProject.trigger.connect(self.functionOpenProject)

                    #self.cardProject.setNamesWidges(No_proyecto)

                No_proyecto += 1
            #colocar otro al final
            frame_end = QFrame()
            frame_end.setSizePolicy(QSizePolicy(QSizePolicy.Preferred,
                                                 QSizePolicy.Expanding))
            self.frame_home.verticalLayout_FH_container_card.addWidget(frame_end)
            self.list_view_card.append(frame_end)
        self.ui.menuRecientes.addSeparator()
        self.ui.menuRecientes.addAction('Limpiar')


        for accion in self.ui.menuRecientes.actions():
            if accion.text() == 'Limpiar':
                accion.triggered.connect(self.onTriggeredaccionRecienteClear)
            else:
                pass
                accion.triggered.connect(self.onTriggeredaccionReciente)

    ###############################################################################
	# ::::::::::::::::::::         FUNCIONES GENERALES         ::::::::::::::::::::
	###############################################################################
    @Slot(str)
    def showMessageStatusBarCritical(self, message):
        self.ui.statusbar.setStyleSheet("color: #F94646;") 
        self.ui.statusbar.showMessage(message,6000)
    @Slot(str)
    def showMessageStatusBarSatisfactory(self, message):
        self.ui.statusbar.setStyleSheet("color: #36C9C6;") 
        self.ui.statusbar.showMessage(message,6000)
    @Slot(str)
    def showMessageStatusBarInformative(self, message):
        self.ui.statusbar.setStyleSheet("color: #DDDDDD;") 
        self.ui.statusbar.showMessage(message,6000)
