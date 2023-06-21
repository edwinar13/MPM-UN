""" Este módulo contiene la clase Ui_FormDraw, para incluirla en main window, es el frame que contiene la parte del dibujo."""


from importlib import import_module
from queue import Empty
from random import seed
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF, QLineF,QSize,QEvent,Slot)
from PySide6.QtWidgets import (QGraphicsRectItem, QGraphicsLineItem, QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu,QSplitter,QDockWidget, QGraphicsItemGroup, QFileDialog)
from PySide6.QtGui import (QColor, QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,
                            QPainterPath,QFont,
                            QKeyEvent,QShortcut, QKeySequence,
                            QFocusEvent,QIcon,QUndoStack,QAction,QUndoCommand,QTransform)
from ui import ui_frame_draw
from clases.Vista import view_WidgetDrawMenuData
from clases.Vista import view_WidgetDrawMenuMesh
from clases import class_projects
from clases.Vista.view_GraphicsDraw import PointItem,LineItem,TextItem
from clases import class_general
from clases.general_functions import isNumber
from clases import class_ui_dialog_msg
import math
import ezdxf

class ViewPageDraw(QFrame, ui_frame_draw.Ui_FormDraw):
    """Esta clase crea el QFrame draw para agregarlo a main window. """ 


    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str) 

    signal_hide_show_draw = Signal(list)
    signal_zoom_draw = Signal(str)
    signal_command_console = Signal(list)


    signal_end_draw_geometry = Signal()
    signal_end_draw_mesh = Signal()
    
    signal_deselect_draw_geometry = Signal(bool)
    




 
    def __init__(self, parent = None, ):
        super(ViewPageDraw, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit_console.installEventFilter(self)


        # Configura la UI
        self.__configUi()
        
        # Establece los eventos de la UI
        self.__initEventUi()

        #Atributos
        self.isTwoViewsVisible = False   
    """
    def resizeEvent(self, event):
        #print("Tamaño: {}".format(self.viewport().rect()))
        #self.graphicsView_draw.setSceneRect(QRectF(0,0,1000,1000))
        pass
    """

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
    ###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 

        # ::::::::::   AJUSTA EL SPLITTER PARA LA ALTURA DE LA CONSOLA  ::::::::::::
        self.signal_hide_show_draw.emit(["ShowHideConsole",True])
        self.modeConsoleDraw(True)
      
        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsScene  ::::::::::::::::::


        self.splitter_view = QSplitter()
        self.splitter_view.setObjectName(u"splitter_view")
        self.splitter_view.setOrientation(Qt.Horizontal)
        self.splitter_view.setHandleWidth(0)
        self.icon_view_one = QIcon()
        self.icon_view_one.addFile(u"recursos/iconos/iconos_consola/view_one.svg", QSize(), QIcon.Normal, QIcon.Off)        
        self.icon_view_two = QIcon()
        self.icon_view_two.addFile(u"recursos/iconos/iconos_consola/view_two.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        
        self.horizontalLayout_graphics.addWidget(self.splitter_view)
  
        
         

        # ::::::::::::::::::   AJUSTES ADICIONALES  ::::::::::::::::::
        self.label_console_command.setVisible(False)
        self.label_console_descrip.setVisible(False)
        self.comboBox_console.setEditable(True)
        
        #self.splitter_view.setSizes([1,0])
        self.mode_label_draw = False



        self.shortcut_select_items = QShortcut(QKeySequence('Ctrl+a'), self)
        self.shortcut_select_items.activated.connect(self.__activatedShortCutSelectItems)



    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   


        #### #
        '''
        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-DATA :::::::::::::::::
        self.drawMenuData.signal_msn_critical.connect(self.showMessageStatusBarCritical)
        self.drawMenuData.signal_msn_satisfactory.connect(self.showMessageStatusBarSatisfactory)
        self.drawMenuData.signal_msn_informative.connect(self.showMessageStatusBarInformative)
  

        '''



        # ::::::::::::::::::::      EVENTOS FRAME DRAW     ::::::::::::::::::::
        self.toolButton_closeConsole.clicked.connect(self.__clickedToolButtonCloseConsole)
        self.toolButton_zoomExtend.clicked.connect(self.__clickedToolButtonZoomExtend)
        self.toolButton_zoomWindow.clicked.connect(self.__clickedToolButtonZoomWindow)
        self.toolButton_views.clicked.connect(self.__clickedToolButtonViews)
        # para que se aga un clik en un boton desde codigo
        # ejemplo ==> self.lineEdit_console.returnPressed.connect(self.toolButton_closeConsole.click)
        self.lineEdit_console.returnPressed.connect(self.__returnPressedLineEditConsole)
        self.splitter.splitterMoved.connect(self.__splitterMovedSplitter)

	###############################################################################
    def setMenuWidget(self,menu, view_menu):  

        if menu == "data":
            self.drawMenuData = view_menu
            self.horizontalLayout_draw.addWidget(self.drawMenuData)

        elif menu == "mesh":
            self.drawMenuMesh = view_menu
            self.horizontalLayout_draw.addWidget(self.drawMenuMesh)

        elif menu == "pointMaterial":
            self.drawMenuPointMaterial = view_menu
            self.horizontalLayout_draw.addWidget(self.drawMenuPointMaterial)
            
        elif menu == "boundary":
            self.drawMenuBoundary = view_menu
            self.horizontalLayout_draw.addWidget(self.drawMenuBoundary)
            

        return
    
    def setViewGraphicsWidget(self, view_graphics): 
        self.splitter_view.addWidget(view_graphics)


    def setUndoStack(self, undoStack):
        self.undoView_draw.setStack(undoStack)
  

    ###############################################################################
    # ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
    ###############################################################################
    """ Métodos para los eventos de los botones y widget """
    def __activatedShortCutSelectItems(self):
        items = self.scene_draw.items()
        print("@"*50)
        for item in items:
            print(item)
            try:
                print(item.getName())
            except:
                pass

    def __keyPressViewConsole(self,key):
        """Método al presionar una tecla de la A a la Z,
         para escribir comando en la consola."""
        self.lineEdit_console.setText(key)
        self.lineEdit_console.setFocus()
        
    def __splitterMovedSplitter(self,pos,index):
        """Oculta la consola."""
        min, max = self.splitter.getRange(1)
        if pos == max:
            self.signal_hide_show_draw.emit(["ShowHideConsole",False])
        else:
            self.signal_hide_show_draw.emit(["ShowHideConsole",True])       

    def __clickedToolButtonCloseConsole(self):
        """Oculta la consola."""
       
        self.modeConsoleDraw(False)
        self.signal_hide_show_draw.emit(["ShowHideConsole",False])
        
    def __clickedToolButtonZoomExtend(self):
        """Realiza zoom extendido"""
        self.signal_zoom_draw.emit("ZoomExtend")
        

    
    def __clickedToolButtonZoomWindow(self):
        """Realiza zoom ventana"""
        self.signal_zoom_draw.emit("ZoomWindow")
        

        
    def __clickedToolButtonViews(self):
        """muestra o oculta la segunda vista"""
        self.viewsTwo()

    def viewsTwo(self):
        """muestra o oculta la segunda vista"""

        if self.isTwoViewsVisible:
            #self.splitter_view.setStretchFactor(0, 1)      
            self.toolButton_views.setIcon(self.icon_view_one)
            self.splitter_view.setSizes([1,1]) 
            self.isTwoViewsVisible = False
        else:
            self.toolButton_views.setIcon(self.icon_view_two)
            self.splitter_view.setSizes([1,0])
            self.isTwoViewsVisible = True
        return

    def __returnPressedLineEditConsole(self):
        """Método presionar enter en el line edit de la consola para ejecutar el comando."""


        data_consola = self.lineEdit_console.text().lower()
        current_command = self.label_console_command.text()
        descrip_command = self.label_console_descrip.text()

        self.signal_command_console.emit([data_consola, current_command, descrip_command])
    
        """
        falta areglar esto
        y despues revisar que si funcione cada boton
        """


        

    def showHideDrawMenu(self,name_menu_view):
        """Muestra el menú seleccionado.

        Args:
            name_menu_view(str): nombre del meú a mostrar
                                : "Data"
                                : "Mesh"

        """

        self.signal_end_draw_geometry.emit()
        self.signal_end_draw_mesh.emit()

        
        self.drawMenuData.setVisible(False)
        self.drawMenuMesh.setVisible(False)
        self.drawMenuPointMaterial.setVisible(False)
        self.drawMenuBoundary.setVisible(False)

        if name_menu_view == "data":
            self.drawMenuData.setVisible(True)
            self.drawMenuMesh.hideShowSelectedObjects(False)
            
        elif name_menu_view == "mesh":
            self.drawMenuMesh.setVisible(True)
            self.drawMenuMesh.hideShowSelectedObjects(True)

        elif name_menu_view == "pointMaterial":
            self.drawMenuPointMaterial.setVisible(True)
            #self.drawMenuPointMaterial.hideShowSelectedObjects(True)

        elif name_menu_view == "boundary":
            self.drawMenuBoundary.setVisible(True)
            #self.drawMenuBoundary.hideShowSelectedObjects(True)
    

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
    ###############################################################################


    def configDrawMenuData(self,project:class_projects.Project):
        """Configura el menú data de la vista draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.drawMenuData.initDrawMenuDataProject(project)

    def configDrawMenuMesh(self,project:class_projects.Project):
        """Configura el menú mesh de la vista draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        self.drawMenuMesh.initDrawMenuDataProject(project)

    def configDrawItemsScene(self,project:class_projects.Project):
        """Configura la escena de draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.scene_draw.admin.initDrawItemsSceneProject(project)


    def modeConsoleDraw(self,isVisible:bool):
        """Oculta o muestra la consola.

        Args:
            mode(bool): modo de vista de la consola
                        False: consola oculta
                        False: consola visible
        """         
        if isVisible:
            self.splitter.setStretchFactor(0, 1)      
            self.splitter.setSizes([100,1]) 
        else:
            self.splitter.setSizes([1,0])

           

    
    def endDrawGeometry(self, show_msn):
        
        self.label_console_command.setText("")
        self.label_console_command.setVisible(False)
        self.label_console_descrip.setText("")
        self.label_console_descrip.setVisible(False)
        self.lineEdit_console.setText("")
        self.lineEdit_console.setPlaceholderText("Ingrese comando")
        self.lineEdit_console.setStyleSheet(u"\n"
            "border: none;\n"
            "border-top-left-radius: 5px;\n"
            "border-bottom-left-radius: 5px ;")     
        if show_msn:         
            self.msnConsole("Information","_end")
        else:         
            self.msnConsole("Information","_init")
    '''
    def end_draw_mesh(self):
        """Recibe la señal que ha finalizado el dibujo de la malla.""" 
    '''
        

    ###############################################################################
    # ::::::::::::::::::::        MÉTODOS PARA MENSAJES        ::::::::::::::::::::
    ############################################################################### 
    def showMessageStatusBarCritical(self,msn):
        """Recibe la señal de mensaje crítico y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje critico

        """
        self.msnConsole("Error",msn)
        self.signal_msn_critical.emit(msn)

    def showMessageStatusBarSatisfactory(self,msn):
        """Recibe la señal de mensaje satisfactorio y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje satisfactorio

        """ 
        self.msnConsole("Running",msn)
        self.signal_msn_satisfactory.emit(msn)

    def showMessageStatusBarInformative(self,msn):
        """Recibe la señal de mensaje informativo y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje informativo

        """ 
        self.msnConsole("Command",msn)
        self.signal_msn_informative.emit(msn)




    def msnConsole(self, type_msn, msn):
        """Imprime mensaje en la consola.

        Args:
            type_msn(str): tipo de mensaje a mostrar
                    : Error
                    : Warning
                    : Running
                    : Command
                    : Information
            msn(str): Mensaje a mostrar

        """ 

        if type_msn == "Error":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f94646;">Error:       </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;">   {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)

        elif type_msn == "Warning":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#c8cc8e;">Warning:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;">   {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Running":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#36c9c6;">Running:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;">   {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Command":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f28123;">Command: </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {}{} </span> </a>'.format(" ",msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Information":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#999999;">information: </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;">   {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        else:
            text_to_add = u'<a> <span>Command:</span><span>   {} </span></a>'.format(msn)
            self.textBrowser_2.append(text_to_add)

        scrollbar = self.textBrowser_2.verticalScrollBar()
        scrollbar.setValue(scrollbar.maximum())  


    
    def msnLabelConsole(self,command: str, msn:str):
        """Imprime mensaje en el label la consola.

        Args:

            msn(str): Mensaje a mostrar

        """ 


        self.label_console_command.setText(command)
        self.label_console_command.setVisible(True)
        self.label_console_descrip.setText(msn)
        self.label_console_descrip.setVisible(True)

        self.lineEdit_console.setText("")
        self.lineEdit_console.setPlaceholderText("")
        self.lineEdit_console.setStyleSheet(u"\n"
            "border-top: 1px solid rgb(254, 255, 198);\n"
            "border-bottom: 1px solid rgb(254, 255, 198);\n"
            "border-right: 1px solid rgb(254, 255, 198);\n"
            "border-top-left-radius: 0px;\n"
            "border-bottom-left-radius: 0px ;")
        self.lineEdit_console.setFocus()
    

   
  
     
    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Evento al presionar una tecla de la A a la Z,   para escribir comando en la consola."""
        key = event.key()
        #try:
            #Presiono tecla de A-Z
            #print()dejar tabien numero, punto coma y espacoipn- 

        if key >= 40 and key <= 90:                
            self.__keyPressViewConsole(event.text())

        elif key == Qt.Key_Enter or key == 16777220:
            self.lineEdit_console.setFocus()
            #self.__returnPressedLineEditConsole()

        elif key == Qt.Key_Enter or key == 16777216:
            self.signal_end_draw_geometry.emit()
            self.signal_end_draw_mesh.emit()
            return  
        elif key == Qt.Key_Shift or key == 16777216:
            self.signal_deselect_draw_geometry.emit(True)
            return  

        return super().keyPressEvent(event)
        #except UnicodeDecodeError:
            #print("no puede decodificar Ejemplo: Ñ ")


    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_Shift:
            self.signal_deselect_draw_geometry.emit(False)
