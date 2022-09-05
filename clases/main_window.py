
from PySide6.QtCore import ( QFile,QTime,SIGNAL, QObject,QEvent)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QMainWindow,QFileDialog,
                            QWidget,QMessageBox,QFrame, QGraphicsDropShadowEffect )
from time import strftime
from ui import ui_main_window
from ui import ui_widget_card
from ui import ui_frame_inicio
from ui import ui_frame_draw
from clases import class_proyects


class MouseObserver(QObject):
    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, obj, event):
        if obj is self.widget and event.type() == QEvent.MouseButtonPress:
            print(event)
        return super().eventFilter(obj, event)

class viewCardProject(QFrame, ui_widget_card.Ui_Form):
    def __init__(self, cardName, cardDataTime, cardPath,cardHour):
        super(viewCardProject, self).__init__()
        self.setupUi(self)
        self.cardName = cardName
        self.cardDataTime = cardDataTime
        self.cardHour = cardHour
        self.cardPath = cardPath
        self.selected=False

        observer = MouseObserver(self.frame_11)

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(20)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(255,255,255,60))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        self.pushButton.clicked.connect(self.onClickedCard)
                

        
        
        self.setTextLabel()

    def setTextLabel(self):
        self.label_cardName.setText(u"{}".format(self.cardName))
        self.label_cardDataTime.setText(u"{}".format(self.cardDataTime))
        self.label_cardPath.setText(u"{}".format(self.cardHour))
        self.frame_card.setToolTip(u"{}".format(self.cardPath))

    def setNamesWidges (self,numberProject):
        self.frame_card.setObjectName(u"frame_card_{}".format(numberProject))
        self.label_img.setObjectName(u"label_img_{}".format(numberProject))
        self.label_cardName.setObjectName(u"label_cardName_{}".format(numberProject))
        self.label_cardDataTime.setObjectName(u"label_cardDataTime_{}".format(numberProject))
        self.label_cardPath.setObjectName(u"label_cardPath_{}".format(numberProject))
        self.pushButton.setObjectName(u"pushButton_{}".format(numberProject))

    def printNamesWidges (self):
        print(self.frame_card.objectName)
        print(self.label_img.objectName)
        print(self.label_cardName.objectName)
        print(self.label_cardDataTime.objectName)
        print(self.label_cardPath.objectName)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        #print(event)
        self.selected=True
        
    def onClickedCard(self):
        print("ok button")



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_main_window.Ui_MainWindow()        
        self.ui.setupUi(self)

        
        #::::::::::::::::::::  CONFIGURANDO MAIN WINDOW::::::::::::::::::::
        """
        with open("css/styles_oscuro.css") as f:
            self.setStyleSheet(f.read())
        """
        #self.showMaximized()
        self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
        self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
        self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")
        self.showMessageStatusBarInformative("Programa iniciado correctamente")


        # ::::::::::::::::::::   INICIANDO DATA PROJECTS ::::::::::::::::::::
        self.projects = class_proyects.Projects()
        self.dataProjects = self.projects.getListProjects(self)
        self.functionUpdateListProjects(self.dataProjects)


            #listProjects
        '''
        self.card1 = viewCardProject()
        self.frame = QWidget()	
        self.subFrame = ui_widget_card.Ui_Form()	
        self.subFrame.setupUi(self.frame)
        self.ui.verticalLayout_17.addWidget((self.frame))
        self.ui.verticalLayout_17.addWidget((self.card1))
        self.card1.printNamesWidges()
        self.card1.setNamesWidges(1)
        self.card1.printNamesWidges()
        '''

        
        #self.contador = 1
        #self.proyecto = self.projects.addProjectToProjects(self,"algo{}".format(self.contador),"01-1-01","20:25",r"C:")
        #self.proyecto = self.projects.addProjectToProjects(self,"algo2{}".format(self.contador),"01-1-01","20:25",r"C:\Program Files (x86)\Google\Update\Download\{65E60E95-0DE9-43FF-9F3F-4F7D2DFF04B5}\7.3.4.8642")
        #self.proyecto = self.projects.addProjectToProjects(self,"algo3{}".format(self.contador),"01-1-01","20:25",r"C:\Users")
        #self.proyecto = self.projects.addProjectToProjects(self,"algo44{}".format(self.contador),"01-1-01","20:25", r"C:\Users\Edwin Arevalo\Desktop\Geotecnia ARGEO")
        #self.projects.printData()


        # ::::::::::::::::::::   CONFIGURANDO FRAME VIEW  ::::::::::::::::::::
        self.ui.splitter.setStretchFactor(0, 100)
        self.ui.splitter.setStretchFactor(1, 0)        
        self.ui.splitter.setSizes([100,100]) 
        
        # ::::::::::::::::::::   EVENTOS WIDGET  MENU LATERAL ::::::::::::::::::::
        self.ui.toolButton_inicio.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_data.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_malla.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_puntos.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_contorno.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_resultados.clicked.connect(self.onClickedToolButtonMenuLat)
        self.ui.toolButton_config.clicked.connect(self.onClickedToolButtonMenuLat)

        # ::::::::::::::::::::   EVENTOS WIDGET FRAME INICIO ::::::::::::::::::::
        self.ui.toolButton_abrirProyecto.clicked.connect(self.onTriggeredactionAbrirProyecto)
        self.ui.toolButton_nuevoProyecto.clicked.connect(self.onTriggeredactionNuevoProyecto)

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


    ###############################################################################
	# ::::::::::::::::::::    FUNCIONES EVENTOS MENU LATERAL   ::::::::::::::::::::
	###############################################################################
 

    def onClickedToolButtonMenuLat(self):
        self.hideToolButtonMenuLat()
        buttonSelected = self.sender()
        nameButton = buttonSelected.objectName()
        print("Nombre: {}".format(nameButton))
        print("objeto: {}".format(buttonSelected))
        if nameButton=="toolButton_inicio":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
            self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
            self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")  

        if nameButton=="toolButton_data":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_data)
            self.ui.frame_data.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_dataInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_malla":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_mesh)
            self.ui.frame_malla.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_mallaInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_puntos":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_point)
            self.ui.frame_puntos.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_puntosInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_contorno":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
            self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_contour)
            self.ui.frame_contorno.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_contornoInf.setStyleSheet("background-color: #2B2B2B;") 

        if nameButton=="toolButton_resultados":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_view)
            self.ui.frame_resultados.setStyleSheet("background-color: #36C9C6;") 
            self.ui.frame_resultadosInf.setStyleSheet("background-color: #2B2B2B;") 


        if nameButton=="toolButton_config":
            self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)
            
            
        '''
        Azules #36C9C6 #00BDB9 #77ACA2
        rojos #910D3F #C70039 #F94646
        naranjas #D34E24 #F28123 #F7F052
        '''

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
            if self.projects.newProject(filePath):
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
        if self.projects.deleteListProjects(self):
            self.functionUpdateListProjects(self.projects.getListProjects(self))
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

    def functionOpenProject (self, filePath):
        '''
        Project
        Funcion para abril, actualizar y leer proyectos 
        muestra canvas y habilita pestaña malla
        '''
        hora = QTime.currentTime().toString("hh:mm:ss A ")
        fecha = strftime("%d/%m/%y")
        fileName=filePath.split('/')[-1]
        #toca volver a validar que si exista el archivo
        if ( QFile.exists(filePath)):
            print(" Existe {}".format(fileName))
        
            if self.projects.addProjectToProjects(self,fileName,fecha,hora,filePath):
                self.setWindowTitle("MPM-UN -- {}".format(fileName))
                self.ui.toolButton_data.setEnabled(True)
                self.ui.toolButton_malla.setEnabled(True)
                self.ui.toolButton_puntos.setEnabled(True)
                self.ui.toolButton_contorno.setEnabled(True)
                self.hideToolButtonMenuLat()
                self.ui.frame_data.setStyleSheet("background-color: #36C9C6;") 
                self.ui.frame_dataInf.setStyleSheet("background-color: #2B2B2B;")
                self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
                self.showMessageStatusBarInformative("Se ha abierto el proyecto {}".format(fileName))

                """
                self.functionStyleButtonPanel(1)
                self.functionUpdateDataProject(filePath)
                self.tabWidget.setTabEnabled(0,True)	
                """
        else:
            self.showMessageStatusBarCritical("No se ha encontrado el documento {}".format(fileName))
        print(self.projects.getListProjects(self))
        self.functionUpdateListProjects(self.projects.getListProjects(self))
        print(self.projects.getListProjects(self))
    
    def functionUpdateListProjects(self,dataProjects):
        """ACTUALIZA PROYECTOS RECIENTES
        Recibe >>
            dataProjects: lista de proyectos"""
        self.ui.menuRecientes.clear()
        print(dataProjects)

        if dataProjects:
            proyectos = dataProjects		
            total_proyectos = len(proyectos)
            No_proyecto = 1
            max_proyectos = 10
            positions = [(i,j) for i in range(5) for j in range(3)]  
            for position, proyecto in zip(positions, proyectos):
                #agrega cada proyecto a menu>recientes
                name=proyecto.getData()[0]
                path=proyecto.getData()[1]
                data=proyecto.getData()[2]
                hour=proyecto.getData()[3]
                if No_proyecto >= total_proyectos-max_proyectos and QFile.exists(path):
                    self.ui.menuRecientes.addAction(path)

                #crear las tarjetas
                self.cardProject = viewCardProject(name,data, path,hour)
                self.ui.gridLayout_proyectos.addWidget(self.cardProject,*position)
                self.cardProject.pushButton.clicked.connect(self.onClickedToolButtonMenuLat)
                self.cardProject.frame_card.connect(SIGNAL("mousePressed()"),self.onClickedToolButtonMenuLat)
                self.cardProject.setNamesWidges(No_proyecto)

                No_proyecto += 1


        self.ui.menuRecientes.addSeparator()
        self.ui.menuRecientes.addAction('Limpiar')
        """
        print("##############################################")    
        print(self.ui.gridLayout_proyectos.rowCount())
        print(self.ui.gridLayout_proyectos.columnCount())
        print(self.ui.gridLayout_proyectos.itemAtPosition(0,0))
        """



        for accion in self.ui.menuRecientes.actions():
            if accion.text() == 'Limpiar':
                accion.triggered.connect(self.onTriggeredaccionRecienteClear)
            else:
                pass
                accion.triggered.connect(self.onTriggeredaccionReciente)
    
    ###############################################################################
	# ::::::::::::::::::::         FUNCIONES GENERALES         ::::::::::::::::::::
	###############################################################################

    def showMessageStatusBarCritical(self, message):
        self.ui.statusbar.setStyleSheet("color: #F94646;") 
        self.ui.statusbar.showMessage(message,6000)
    def showMessageStatusBarSatisfactory(self, message):
        self.ui.statusbar.setStyleSheet("color: #36C9C6;") 
        self.ui.statusbar.showMessage(message,6000)
    def showMessageStatusBarInformative(self, message):
        self.ui.statusbar.setStyleSheet("color: #DDDDDD;") 
        self.ui.statusbar.showMessage(message,6000)
