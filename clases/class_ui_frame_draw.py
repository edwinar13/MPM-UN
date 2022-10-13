""" Este módulo contiene la clase Ui_FormDraw, para incluirla en main window, es el frame que contiene la parte del dibujo."""


from queue import Empty
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF,QSize,QEvent)
from PySide6.QtWidgets import (QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu,QSplitter)
from PySide6.QtGui import (QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,QPainterPath,QFont,QKeyEvent,QShortcut, QKeySequence)
from ui import ui_frame_draw
from clases import class_ui_widget_draw_menu_data
from clases import class_ui_widget_draw_menu_mesh
from clases import class_projects
from clases import class_graphics
from clases import general_class
from clases.general_functions import isNumber

import math
class FrameDraw(QFrame, ui_frame_draw.Ui_FormDraw):
    """Esta clase crea el QFrame draw para agregarlo a main window. """ 
    signal_home_open = Signal(str)
    signal_home_new = Signal()

    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str) 

    signal_project_save_state = Signal(bool)


    signal_coor_mouse = Signal(list)
    signal_zoom = Signal(float)

    signal_console_hise_show = Signal(bool)

    def __init__(self, parent = None, ):
        super(FrameDraw, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit_console.installEventFilter(self)


        # Configura la UI
        self.__configUi()
        
        # Establece los eventos de la UI
        self.__initEventUi()
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
        self.mode_console_draw(True)
        self.signal_console_hise_show.emit(True)


        

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsScene  ::::::::::::::::::
        self.scene_draw = class_graphics.GraphicsSceneDraw()
        #self.scene_draw.setSceneRect(QRectF(-100, -100, 100, 100))
        


        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 1 ::::::::::::::::::
        self.view_draw = class_graphics.GraphicsViewDraw(self.scene_draw)       
        self.horizontalLayout_graphics.addWidget(self.view_draw)

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 2 ::::::::::::::::::        
        self.view_draw2 = class_graphics.GraphicsViewDraw(self.scene_draw)       
        self.horizontalLayout_graphics.addWidget(self.view_draw2)
        self.view_draw2.setMaximumSize(QSize(500, 16777215))
  


        
        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-DATA  ::::::::::::::::::
        self.drawMenuData = class_ui_widget_draw_menu_data.WidgetDrawMenuData()        
        self.horizontalLayout_draw.addWidget(self.drawMenuData)

        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-MESH  ::::::::::::::::::
        self.drawMenuMesh = class_ui_widget_draw_menu_mesh.WidgetDrawMenuMesh()        
        self.horizontalLayout_draw.addWidget(self.drawMenuMesh)

        # ::::::::::::::::::   AJUSTES ADICIONALES  ::::::::::::::::::
        self.label_console_command.setVisible(False)
        self.label_console_descrip.setVisible(False)
        self.comboBox_console.setEditable(True)
        self.showHideDrawMenu("Data")


        self.shortcut_select_items = QShortcut(QKeySequence('Ctrl+a'), self)
        self.shortcut_select_items.activated.connect(self.__activatedShortCutSelectItems)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-DATA :::::::::::::::::
        self.drawMenuData.signal_msn_critical.connect(self.showMessageStatusBarCritical)
        self.drawMenuData.signal_msn_satisfactory.connect(self.showMessageStatusBarSatisfactory)
        self.drawMenuData.signal_msn_informative.connect(self.showMessageStatusBarInformative)
        self.drawMenuData.signal_project_save_state.connect(self.__projectSaveState)

        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-MESH :::::::::::::::::
        self.drawMenuMesh.signal_paint_point.connect(self.__clickedToolButtonDrawPaintPoint)
        self.drawMenuMesh.signal_paint_line.connect(self.__clickedToolButtonDrawPaintLine)
        self.drawMenuMesh.signal_paint_polyline.connect(self.__clickedToolButtonDrawPaintPolyline)
        self.drawMenuMesh.signal_paint_rectangle.connect(self.__clickedToolButtonDrawPaintRectangle)

        self.drawMenuMesh.signal_paint_move.connect(self.__clickedToolButtonDrawPaintMove)
        self.drawMenuMesh.signal_paint_rotate.connect(self.__clickedToolButtonDrawPaintRotate)
        self.drawMenuMesh.signal_paint_copy.connect(self.__clickedToolButtonDrawPaintCopy)
        self.drawMenuMesh.signal_paint_erase.connect(self.__clickedToolButtonDrawPaintErase)

        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE DRAW :::::::::::::::::        
        self.scene_draw.coor_mouse.connect(self.coor_mouse)
        self.view_draw.signal_zoom_view.connect(self.zoom_view)
        self.view_draw.signal_end_draw_geometry.connect(self.end_draw_geometry)
        #self.view_draw2.zoom_view.connect(self.zoom_view)
        '''        
        self.scene_draw.item_inserted.connect(self.item_inserted)
        self.scene_draw.text_inserted.connect(self.text_inserted)
        self.scene_draw.item_selected.connect(self.item_selected)
        self.scene_draw.item_selected.connect(self.item_selected)
        '''

        # ::::::::::::::::::::      EVENTOS FRAME DRAW     ::::::::::::::::::::
        self.toolButton_closeConsole.clicked.connect(self.__clickedToolButtonCloseConsole)
        # para que se aga un clik en un boton desde codigo
        #self.lineEdit_console.returnPressed.connect(self.toolButton_closeConsole.click)
        self.lineEdit_console.returnPressed.connect(self.__returnPressedLineEditConsole)
        self.splitter.splitterMoved.connect(self.__splitterMovedSplitter)

    ###############################################################################
    # ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
    ###############################################################################
    """ Métodos para los eventos de los botones y widget """
    def __activatedShortCutSelectItems(self):
        items = self.scene_draw.items()
        print("@"*20)
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
            self.signal_console_hise_show.emit(False)
        else:
            self.signal_console_hise_show.emit(True)
           
        #self.mode_console_draw(False)
        #self.signal_console_hise_show.emit(False)

    def __clickedToolButtonCloseConsole(self):
        """Oculta la consola."""
        self.mode_console_draw(False)
        self.signal_console_hise_show.emit(False)

    def __returnPressedLineEditConsole(self):
        """Método presionar enter en el line edit de la consola para ejecutar el comando."""

        data_consola = self.lineEdit_console.text().lower()
        current_command = self.label_console_command.text()
        descrip_command = self.label_console_descrip.text()

        
        commands = ["point", "line", "pline", "rectang", "erase"]
        commands_min = ["p",     "l",    "pl",    "rec",     "era"]

        #se ejecuta si la entrada es un comando
        if (data_consola in commands) or (data_consola in commands_min):
            if data_consola in commands:
                index = commands.index(data_consola)
            elif  data_consola in commands_min:
                index = commands_min.index(data_consola)

            command = commands[index]

            if command == "point" :
                self.view_draw.drawPointScene()

            elif command == "line" :
                self.view_draw.drawLineScene()

            elif command == "pline" :
                self.view_draw.drawPolylineScene()

            elif command == "rectang" :
                self.view_draw.drawRectangleScene()
                
            elif command == "erase" :
                self.view_draw.drawEraseItemScene()

            self.init_draw_geometry(command)
            return
        
        #se ejecuta si la entrada es un punto
        if (current_command in commands) and descrip_command == "Ingrese un punto:":
            
            if data_consola != "":
                input_point = data_consola.split(",")
                if len(input_point) == 1:
                    x = input_point[0]
                    y = x
                elif len(input_point) == 2:
                    x = input_point[0]
                    y = input_point[1]
                else: 
                    return
                
                if isNumber(x) and isNumber(y):
                    x = float(x)
                    y = float(y)
                    self.view_draw.drawGeometry(QPointF(x,y))
                    self.lineEdit_console.setText("")
                    self.msnConsole("Command",f"Ingrese un punto:{x},{y}")
                else:
                    return
            else:
                print("1-Comando[{}]  descrip[{}]  consola[{}]]".format(current_command, descrip_command, data_consola ))
                self.end_draw_geometry()                
                self.msnConsole("Command","_end")
                self.view_draw.endDrawGeometry()
                return


        
    def __clickedToolButtonDrawPaintPoint(self):
        self.init_draw_geometry("point")
        self.view_draw.drawPointScene()
        
    def __clickedToolButtonDrawPaintLine(self):
        self.view_draw.drawLineScene()
        self.init_draw_geometry("line")
        self.view_draw.setSceneRect(self.view_draw.sceneRect().translated(10, 10))
      

    def __clickedToolButtonDrawPaintPolyline(self):
        self.init_draw_geometry("pline")
        self.view_draw.drawPolylineScene()

    def __clickedToolButtonDrawPaintRectangle(self):
        self.init_draw_geometry("rectang")
        self.view_draw.drawRectangleScene()

    def __clickedToolButtonDrawPaintMove(self):
        pass

    def __clickedToolButtonDrawPaintRotate(self):
        pass
        '''
        if self.graphicsView_draw.isClear == False:
            self.graphicsView_draw.isClear = True
        else:
            self.graphicsView_draw.isClear = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.line_temp = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.graphicsScene_draw.clear()
        '''

    def __clickedToolButtonDrawPaintCopy(self):
        pass
        '''
        if self.graphicsView_draw.line_temp == False:
            self.graphicsView_draw.line_temp = True
        else:
            self.graphicsView_draw.line_temp = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        '''

    def __clickedToolButtonDrawPaintErase(self):
        self.init_draw_geometry("erase")
        self.view_draw.drawEraseItemScene()
        '''
        if self.graphicsView_draw.isDelate == False:
            self.graphicsView_draw.isDelate = True
        else:
            self.graphicsView_draw.isDelate = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.line_temp = False
        self.graphicsView_draw.isClear = False
        '''

    def showHideDrawMenu(self,name_menu_view):
        """Muestra el menú seleccionado.

        Args:
            name_menu_view(str): nombre del meú a mostrar
                                : "Data"
                                : "Mesh"

        """
        self.drawMenuData.setVisible(False)
        self.drawMenuMesh.setVisible(False)
        if name_menu_view == "Data":
            self.drawMenuData.setVisible(True)
        elif name_menu_view == "Mesh":
            self.drawMenuMesh.setVisible(True)
        elif name_menu_view == "Point":
            pass
            #self.drawMenuPoint.setVisible(True)
        elif name_menu_view == "Boundary":
            pass
            #self.drawMenuBoundary.setVisible(True)

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
    ###############################################################################
    def configDrawMenuData(self,project:class_projects.Project):
        """Configura el menú data de la vista draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.drawMenuData.initDrawMenuDataProject(project)

    def mode_origin_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar el origen.

        Args:
            mode(bool): modo de los ejes
                        False: origen Oculto
                        False: origen visible
        """ 
        self.view_draw.mode_origin=mode
        self.scene_draw.update()

    def mode_axis_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar los ejes principales.

        Args:
            mode(bool): modo de los ejes
                        False: ejes Oculta
                        False: ejes visible
        """ 
        self.scene_draw.mode_axis=mode
        self.scene_draw.update()
        
    def mode_grid_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar la grilla.

        Args:
            mode(bool): modo de la grilla
                        False: grilla Oculta
                        False: grilla visible
        """ 
        self.scene_draw.mode_grid=mode
        self.scene_draw.update()
        
    def mode_console_draw(self,isVisible:bool):
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
            
    def __projectSaveState(self, there_are_changes):
        """Recibe la señal del estado del guardado del proyecto y remite la misma, señal a main window.

        Args:
            there_are_changes(bool): True >>> si se realizó cambios en el proyecto

        """
        self.signal_project_save_state.emit(there_are_changes)

    def end_draw_geometry(self):
        """Recibe la señal que ha finalizado el dibujo de geometria.""" 
        
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
        self.view_draw.setFocus()        
        #self.msnConsole("Command","_cancel")

    def init_draw_geometry(self,command):
        """Recibe la señal que ha iniciado el dibujo de geometria.
        
        args:
            command(str): comando de la geometria a dibujar
        
        """ 
        
        self.msnConsole("Command","_{}".format(command))
        self.msnLabelConsole(command,"Ingrese un punto:")

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
        self.textBrowser_2.verticalScrollBar().maximum()
    
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
    
    def coor_mouse(self,coor_list):
        """Recibe la señal de coordenada del ratón y remite la misma, señal a main window para imprimir en barra de estado..

        Args:
            coor_list(list): coordenadas del raton.

        """ 
        self.signal_coor_mouse.emit(coor_list)

    def zoom_view(self,zoom):
        """Recibe la señal con el zoom del view y remite la misma, señal a main window para imprimir en barra de estado..

        Args:
            zoom(floar): procentaje de zoom

        """ 
        self.signal_zoom.emit(zoom)

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################    
    def keyPressEvent(self, event: QKeyEvent) -> None:
        """Evento al presionar una tecla de la A a la Z,   para escribir comando en la consola."""
        key = event.key()
        try:
            #Presiono tecla de A-Z
            #print()dejar tabien numero, punto coma y espacoipn- 

            if key >= 40 and key <= 90:                
                self.__keyPressViewConsole(event.text())

            elif key == Qt.Key_Enter or key == 16777220:
                self.lineEdit_console.setFocus()

            elif key == Qt.Key_Enter or key == 16777216:
                print("funcionalidas escapar")
                self.end_draw_geometry()                
                self.msnConsole("Command","_cancel")
                self.view_draw.endDrawGeometry()

            return super().keyPressEvent(event)
        except UnicodeDecodeError:
            print("no puede decodificar Ejemplo: Ñ ")
    '''
    def eventFilter(self, obj, event):
        """método para filtrar el tipo de widget que activo la señal."""
        #Si key es esc en el line edit consola 
        if event.type() == QEvent.ShortcutOverride or event.type() == QEvent.KeyRelease:
            if event.key() == Qt.Key_Escape:

                self.end_draw_geometry()                
                self.msnConsole("Command","_cancel")
                self.view_draw.endDrawGeometry()


        return super().eventFilter(obj, event)

    '''