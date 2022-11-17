""" Este módulo contiene la clase Ui_FormDraw, para incluirla en main window, es el frame que contiene la parte del dibujo."""


from importlib import import_module
from queue import Empty
from random import seed
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF,QSize,QEvent,Slot)
from PySide6.QtWidgets import (QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu,QSplitter,QDockWidget)
from PySide6.QtGui import (QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,
                            QPainterPath,QFont,
                            QKeyEvent,QShortcut, QKeySequence,
                            QFocusEvent,QIcon,QUndoStack,QAction,QUndoCommand)
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

    signal_console_hise_show = Signal(bool)

    def __init__(self, parent = None, ):
        super(FrameDraw, self).__init__(parent)
        self.setupUi(self)

        self.lineEdit_console.installEventFilter(self)


        # Configura la UI
        self.__configUi()
        
        # Establece los eventos de la UI
        self.__initEventUi()

        #Atributos
        self.isTwoViewsVisible = False
        self.__clickedToolButtonViews()
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
        self.scene_draw.setSceneRect(QRectF(-10000, -10000, 20000, 20000))
        

        self.splitter_view = QSplitter()
        self.splitter_view.setObjectName(u"splitter_view")
        self.splitter_view.setOrientation(Qt.Horizontal)
        self.splitter_view.setHandleWidth(0)
        self.icon_view_one = QIcon()
        self.icon_view_one.addFile(u"recursos/iconos/iconos_consola/view_one.svg", QSize(), QIcon.Normal, QIcon.Off)        
        self.icon_view_two = QIcon()
        self.icon_view_two.addFile(u"recursos/iconos/iconos_consola/view_two.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        


        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 1 ::::::::::::::::::
        self.view_draw_1 = class_graphics.GraphicsViewDraw(self) 
        self.view_draw_1.setScene(self.scene_draw) 
        self.view_draw_1.setObjectName("ViewDraw1")  
        self.view_draw_1.setFocus()
        #self.horizontalLayout_graphics.addWidget(self.view_draw_1)
        self.splitter_view.addWidget(self.view_draw_1)

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 2 ::::::::::::::::::        
        self.view_draw_2 = class_graphics.GraphicsViewDraw(self)       
        self.view_draw_2.setScene(self.scene_draw)       
        self.view_draw_2.setObjectName("ViewDraw2---------------->>")
        #self.horizontalLayout_graphics.addWidget(self.view_draw_2)
        #self.view_draw_2.setMaximumSize(QSize(500, 16777215))
        self.splitter_view.addWidget(self.view_draw_2)

        self.horizontalLayout_graphics.addWidget(self.splitter_view)
  


        
        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-DATA  ::::::::::::::::::
        self.drawMenuData = class_ui_widget_draw_menu_data.WidgetDrawMenuData()        
        self.horizontalLayout_draw.addWidget(self.drawMenuData)
        
        self.undoStack = QUndoStack(self)
        self.undoView_draw.setStack(self.undoStack)
        self.scene_draw.setUndoStackToAdmin(self.undoStack)


        '''
        #self.undoView.setWindowTitle(QDockWidget.tr("Lista de comandos"))
        #self.undoView.show()
        #self.undoView.setAttribute(Qt.WA_QuitOnClose, False)
        self.deleteAction = QAction(("Delete Item"), self)
        self.deleteAction.setShortcut(QKeySequence.Delete)
        #self.deleteAction.triggered.connect(self.deleteItem)
        self.undoAction = self.undoStack.createUndoAction(self, ("Undo"))
        self.undoAction.setShortcuts(QKeySequence.Undo)
        self.redoAction = self.undoStack.createRedoAction(self, ("Redo"))
        self.redoAction.setShortcuts(QKeySequence.Redo)
        addCommand = QUndoCommand()
        self.undoStack.push(addCommand)
        '''



        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-MESH  ::::::::::::::::::
        self.drawMenuMesh = class_ui_widget_draw_menu_mesh.WidgetDrawMenuMesh()        
        self.horizontalLayout_draw.addWidget(self.drawMenuMesh)

        # ::::::::::::::::::   AJUSTES ADICIONALES  ::::::::::::::::::
        self.label_console_command.setVisible(False)
        self.label_console_descrip.setVisible(False)
        self.comboBox_console.setEditable(True)
        self.showHideDrawMenu("Data")
        #self.splitter_view.setSizes([1,0])


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
        self.toolButton_cardMeshDrawPoint.clicked.connect(self.__clickedToolButtonDrawPaintPoint)
        self.drawMenuMesh.signal_paint_line.connect(self.__clickedToolButtonDrawPaintLine)
        self.toolButton_cardMeshDrawLine.clicked.connect(self.__clickedToolButtonDrawPaintLine)
        self.drawMenuMesh.signal_paint_rectangle.connect(self.__clickedToolButtonDrawPaintRectangle)
        self.toolButton_cardMeshDrawRect.clicked.connect(self.__clickedToolButtonDrawPaintRectangle)
        self.drawMenuMesh.signal_paint_polyline.connect(self.__clickedToolButtonDrawPaintPolyline)

        self.drawMenuMesh.signal_paint_move.connect(self.__clickedToolButtonDrawPaintMove)
        self.toolButton_cardMeshDrawMove.clicked.connect(self.__clickedToolButtonDrawPaintMove)
        self.drawMenuMesh.signal_paint_rotate.connect(self.__clickedToolButtonDrawPaintRotate)
        self.drawMenuMesh.signal_paint_copy.connect(self.__clickedToolButtonDrawPaintCopy)
        self.toolButton_cardMeshDrawCopy.clicked.connect(self.__clickedToolButtonDrawPaintCopy)
        self.drawMenuMesh.signal_paint_erase.connect(self.__clickedToolButtonDrawPaintErase)
        self.toolButton_cardMeshDrawErase.clicked.connect(self.__clickedToolButtonDrawPaintErase)

        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE DRAW :::::::::::::::::    
        #     
        self.view_draw_1.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_2.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_1.signal_main_view.connect(self.main_view)
        self.view_draw_2.signal_main_view.connect(self.main_view)
        self.view_draw_1.signal_end_draw_geometry.connect(self.end_draw_geometry)
        self.view_draw_2.signal_end_draw_geometry.connect(self.end_draw_geometry)

        self.scene_draw.signal_next_point.connect(self.nextPoint)



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
            self.signal_console_hise_show.emit(False)
        else:
            self.signal_console_hise_show.emit(True)          

    def __clickedToolButtonCloseConsole(self):
        """Oculta la consola."""
        self.mode_console_draw(False)
        self.signal_console_hise_show.emit(False)
        return

    def __clickedToolButtonZoomExtend(self):
        """Realiza zoom extendido"""
        self.view_draw_1.reset_view()
        self.view_draw_2.reset_view()
        return
    
    def __clickedToolButtonZoomWindow(self):
        """Realiza zoom ventana"""
        self.view_draw_1.zoomWindow(True)
        self.view_draw_2.zoomWindow(True)
        return
        
    def __clickedToolButtonViews(self):
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
        
        commands =     ["point", "line", "pline", "rectang", "erase", "zoom", "views"]
        commands_min = ["p",     "l",    "pl",    "rec",     "era",   "z",    "v"]

        #se ejecuta si la entrada es un comando
        if (data_consola in commands) or (data_consola in commands_min):
            if data_consola in commands:
                index = commands.index(data_consola)
            elif  data_consola in commands_min:
                index = commands_min.index(data_consola)

            command = commands[index]

            if command == "point" :
                self.scene_draw.drawPointScene()
                self.init_tool_geometry(command,"Ingrese un punto [Exit]:")

            elif command == "line" :
                self.scene_draw.drawLineScene()
                self.init_tool_geometry(command,"Ingrese el primer punto [Exit]:")

            elif command == "rectang" :
                self.scene_draw.drawRectangleScene()
                self.init_tool_geometry(command,"Ingrese el primer punto [Exit]:")

            elif command == "pline" :
                self.scene_draw.drawPolylineScene()
                self.init_tool_geometry(command,"Ingrese el primer punto [Exit]:")

                
            elif command == "erase" :
                self.scene_draw.drawEraseItemScene()
                self.init_tool_geometry(command,"Selecione un elemento  [Exit]:")

            elif command == "zoom" :
                self.init_tool_geometry(command,"[Extents Window] <E>:")

            elif command == "views" :
                self.init_tool_geometry(command,"[1 2] <1>:")
            return
            self.init_draw_geometry(command)
        

        #se ejecuta si la entrada una opcion de zoom
        if current_command == "zoom" and descrip_command == "[Extents Window] <E>:":
            
            if data_consola == "" or data_consola.lower() == "e":
                self.__clickedToolButtonZoomExtend()             
            elif data_consola == "w":
                self.__clickedToolButtonZoomWindow()
                self.msnConsole("Command","_zoomWindow")
                self.init_tool_geometry("zoom","Window")
                return
            else:
                return
            self.msnConsole("Command","_end")
            self.end_draw_geometry() 
            return

        #se ejecuta si la entrada una opcion de vistas
        elif current_command == "views" and descrip_command == "[1 2] <1>:":
            
            if data_consola == "" or data_consola == "1":
                self.isTwoViewsVisible = False                
            elif data_consola == "2":
                self.isTwoViewsVisible = True
            else:
                return

            self.__clickedToolButtonViews()
            self.msnConsole("Command","_end")
            self.end_draw_geometry() 
            return
        
        if current_command == "rectang" or current_command == "line" or current_command == "point":
            
            #exit: salir del dibujo de objeto
            if data_consola.lower() == "e" and "Exit" in descrip_command:
                self.end_draw_geometry()                
                self.msnConsole("Command","_cancel")
                self.scene_draw.endDrawGeometry()
                return

            # close: cerrar un poligono  
            elif data_consola.lower() == "c" and "Close" in descrip_command:
                point_vertex_init = self.scene_draw.point_vertex_init
                point_vertex_ant = self.scene_draw.point_vertex_ant
                self.scene_draw.drawGeometry(point_vertex_init, point_vertex_ant)
                self.scene_draw.endDrawGeometry()
                self.end_draw_geometry()                
                self.msnConsole("Command","_line close")
                return


            if data_consola != "":

                input_point = data_consola.split(",")
                point_vertex_ant = self.scene_draw.point_vertex_ant
                
                # Si es el primer punto y se recibe un solo valor input=x=y
                if len(input_point) == 1 and point_vertex_ant == None:
                    x = input_point[0]
                    if isNumber(x):
                        x = float(x)
                        y = x
                    else:
                        return

                # Si es el segundo punto y se recibe un solo valor input=dist
                elif len(input_point) == 1 and point_vertex_ant!= None:
                        dist = input_point[0]
                        if isNumber(dist):
                            point_vertex = self.scene_draw.point_vertex
                            x, y = self.pointInLine(point_vertex_ant, point_vertex,float(dist))
                        else:
                            return
            
                # Si es el segundo punto y se recibe angulo y distancia input=@angulo,dist
                elif len(input_point) == 2 and input_point[0][0] == "@" and point_vertex_ant!= None:
                    angle = input_point[0][1:]
                    dist = input_point[1]
                    if isNumber(angle) and isNumber(dist):
                        angle = float(angle)
                        dist = float(dist)
                        dx = dist * math.cos(math.radians(angle))
                        dy = dist * math.sin(math.radians(angle))
                        x = point_vertex_ant.x() + dx
                        y = point_vertex_ant.y() + dy                        
                    else:
                        return

                # Si es el segundo punto y se recibe distancia X y distancia Y input=#dx,dy
                elif len(input_point) == 2 and input_point[0][0] == "#" and point_vertex_ant!= None:
                    dx = input_point[0][1:]
                    dy = input_point[1]
                    if isNumber(dx) and isNumber(dy):
                        x = point_vertex_ant.x() + float(dx)
                        y = point_vertex_ant.y() + float(dy)                        
                    else:
                        return
                        
                # Si es el segundo punto y se recibe coordenada input=x,y
                elif len(input_point) == 2:
                    x = input_point[0]
                    y = input_point[1]
                    if isNumber(x) and isNumber(y):
                        x = float(x)
                        y = float(y) 
                    else: 
                        return

                # en los demas casos ejem: texto
                else: 
                    return

            else:

                self.end_draw_geometry()                
                self.msnConsole("Command","_end")
                self.scene_draw.endDrawGeometry()
                return

            #se ejecuta si la entrada es un punto nuevo
            if current_command == "rectang":

                point_vertex = QPointF(x,y)




                if point_vertex_ant == None:
                    cancel_point = self.scene_draw.drawGeometry(point_vertex)  
                    if not cancel_point: 
                        self.scene_draw.point_vertex_ant = point_vertex
                        #self.scene_draw.drawGeneral(point_vertex, point_vertex_ant)
                        #self.scene_draw.rectangle_temp.setVisible(True)
                        #self.scene_draw.update()

                else:
                    cancel_point = self.scene_draw.drawGeometry(point_vertex, point_vertex_ant)
                    if not cancel_point:
                        self.scene_draw.point_vertex_ant = None
                        self.scene_draw.point_vertex = None
                        self.scene_draw.rectangle_temp.setVisible(False)
                        self.scene_draw.update()

            #se ejecuta si la entrada es un punto nuevo
            elif current_command == "line":

                point_vertex = QPointF(x,y)
                cancel_point = self.scene_draw.drawGeometry(point_vertex, point_vertex_ant)  
                if not cancel_point: 
                    self.scene_draw.point_vertex_ant = point_vertex
                    self.scene_draw.drawGeneral(self.scene_draw.point_vertex, self.scene_draw.point_vertex_ant)


            #se ejecuta si la entrada es un punto nuevo
            elif current_command == "point":
                
                point_vertex = QPointF(x,y)
                self.scene_draw.drawGeometry(point_vertex)
                self.lineEdit_console.setText("")
                self.msnConsole("Command",f"Ingrese un punto:{x},{y}")



    def __clickedToolButtonDrawPaintPoint(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawPointScene()
        self.init_tool_geometry("point","Ingrese un punto [Exit]:")

    def __clickedToolButtonDrawPaintLine(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawLineScene()
        self.init_tool_geometry("line","Ingrese el primer punto [Exit]:")

    def __clickedToolButtonDrawPaintRectangle(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawRectangleScene()
        self.init_tool_geometry("rectang","Ingrese el primer punto [Exit]:")
      
    def __clickedToolButtonDrawPaintPolyline(self):
        return
        self.init_draw_geometry("pline")
        self.scene_draw.drawPolylineScene()

    def __clickedToolButtonDrawPaintMove(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawMoveItemScene()
        self.init_tool_geometry("move","Seleccione un objeto[Exit]:")

    def __clickedToolButtonDrawPaintRotate(self):
        pass

    def __clickedToolButtonDrawPaintCopy(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawCopyItemScene()
        self.init_tool_geometry("copy","Seleccione un objeto[Exit]:")


    def __clickedToolButtonDrawPaintErase(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawEraseItemScene()
        self.init_tool_geometry("erase","Seleccione un objeto[Exit]:")


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
    def undo(self):
        self.undoStack.undo()

    def redo(self):
        self.undoStack.redo()
    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
    ###############################################################################

    def pointInLine(self, p1:QPointF, p2:QPointF,dist_i):
        x = None
        y = None
        dx = p2.x() - p1.x()  
        dy = p2.y() - p1.y()
        if dx >= 0: 
            signX = 1
        else:
            signX = -1
        if dy >= 0: 
            signY = 1
        else:
            signY = -1  
        try: 
            theta = math.atan(dx/dy) 
        except ZeroDivisionError:
            theta = math.radians(90)
        
        dxi = abs(dist_i * math.sin(theta)) * signX
        dyi = abs(dist_i * math.cos(theta)) * signY
        x = p1.x() + dxi
        y = p1.y() + dyi
        return (x, y)




    def configDrawMenuData(self,project:class_projects.Project):
        """Configura el menú data de la vista draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.drawMenuData.initDrawMenuDataProject(project)

    def configDrawItemsScene(self,project:class_projects.Project):
        """Configura la escena de draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.scene_draw.admin.initDrawItemsSceneProject(project)

    def mode_origin_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar el origen.

        Args:
            mode(bool): modo de los ejes
                        False: origen Oculto
                        False: origen visible
        """ 
        self.view_draw_1.isModeOrigin=mode
        self.view_draw_2.isModeOrigin=mode
        self.scene_draw.update()

    def mode_axis_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar los ejes principales.

        Args:
            mode(bool): modo de los ejes
                        False: ejes Oculta
                        False: ejes visible
        """ 
        self.view_draw_1.isModeAxis=mode
        self.view_draw_2.isModeAxis=mode
        self.scene_draw.update()
        
    def mode_grid_draw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar la grilla.

        Args:
            mode(bool): modo de la grilla
                        False: grilla Oculta
                        False: grilla visible
        """ 
        self.view_draw_1.isModeGrid=mode
        self.view_draw_2.isModeGrid=mode
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
              
        #self.msnConsole("Command","_cancel")
    @Slot(int)
    def nextPoint(self, vertex):
        """Recibe la señal que ha finalizado el dibujo de geometria.""" 

        current_command = self.label_console_command.text()
        if vertex == 0 or vertex == 1:
            self.init_tool_geometry(current_command,"Ingrese el siguiente punto [Exit]:")
        elif vertex >= 1:
            self.init_tool_geometry(current_command,"Ingrese el siguiente punto [Exit Close]:")

    

    def init_draw_geometry888888888888888888888 (self,command):
        return
        """Recibe la señal que ha iniciado eujna utilidad como zoom.
        
        args:
            command(str): comando de la utilidad
        
        """         
        self.msnConsole("Command","_{}".format(command))
        self.msnLabelConsole(command,"Ingrese un punto:")

    def init_tool_geometry(self,command,input):
        """Recibe la señal que ha iniciado el dibujo de geometria.
        
        args:
            command(str): comando de la geometria a dibujar
            input(str): mensaje de consola para entrada
        
        """         
        self.msnConsole("Command","_{}".format(command))
        self.msnLabelConsole(command, input)

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

    
    def main_view(self, main_view):
        """Recibe la señal de la vista que tiene el foco del ratón y la coloca como vista principal.

        Args:
            main_view(tr): nombre de la vista que tiene le foco.

        """ 
        if self.view_draw_1.objectName() == main_view:
            self.view_draw_1.isMainView = True
            self.view_draw_2.isMainView = False
        elif self.view_draw_2.objectName() == main_view:
            self.view_draw_2.isMainView = True
            self.view_draw_1.isMainView = False
        
     
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
                print("funcionalidad escapar")
                self.end_draw_geometry()                
                self.msnConsole("Command","_cancel")
                self.scene_draw.endDrawGeometry()
                self.view_draw_1.zoomWindow(False)
                self.view_draw_2.zoomWindow(False)

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
                self.view_draw_1.endDrawGeometry()


        return super().eventFilter(obj, event)

    '''