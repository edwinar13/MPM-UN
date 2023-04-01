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
from clases import class_ui_widget_draw_menu_data
from clases import class_ui_widget_draw_menu_mesh
from clases import class_projects
from clases.class_graphics import PointItem,LineItem,TextItem, GraphicsSceneDraw, GraphicsViewDraw
from clases import general_class
from clases.general_functions import isNumber
from clases import class_ui_dialog_msg
import math
import ezdxf



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
        self.modeConsoleDraw(True)
        self.signal_console_hise_show.emit(True)


        

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsScene  ::::::::::::::::::
        self.scene_draw = GraphicsSceneDraw()
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
        self.view_draw_1 = GraphicsViewDraw(self) 
        self.view_draw_1.setScene(self.scene_draw) 
        self.view_draw_1.setObjectName("ViewDraw1")  
        self.view_draw_1.setFocus()
        #self.horizontalLayout_graphics.addWidget(self.view_draw_1)
        self.splitter_view.addWidget(self.view_draw_1)
        self.view_draw_1.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)


        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 2 ::::::::::::::::::        
        self.view_draw_2 = GraphicsViewDraw(self)       
        self.view_draw_2.setScene(self.scene_draw)       
        self.view_draw_2.setObjectName("ViewDraw2---------------->>")
        #self.horizontalLayout_graphics.addWidget(self.view_draw_2)
        #self.view_draw_2.setMaximumSize(QSize(500, 16777215))
        self.splitter_view.addWidget(self.view_draw_2)
        self.view_draw_2.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

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
        self.mode_label_draw = False
        self.modeLabelDraw(False)


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
        self.drawMenuMesh.signal_paint_copy.connect(self.__clickedToolButtonDrawPaintCopy)
        self.toolButton_cardMeshDrawCopy.clicked.connect(self.__clickedToolButtonDrawPaintCopy)
        self.drawMenuMesh.signal_paint_rotate.connect(self.__clickedToolButtonDrawPaintRotate)
        self.toolButton_cardMeshDrawRotate.clicked.connect(self.__clickedToolButtonDrawPaintRotate)
        self.drawMenuMesh.signal_paint_erase.connect(self.__clickedToolButtonDrawPaintErase)
        self.toolButton_cardMeshDrawErase.clicked.connect(self.__clickedToolButtonDrawPaintErase)
        
        self.toolButton_cardMeshDrawImport.clicked.connect(self.__clickedToolButtonDrawPaintImport)
        self.toolButton_cardMeshDrawIntersection.clicked.connect(self.__clickedToolButtonDrawPaintIntersection)
        self.toolButton_cardMeshDrawRule.clicked.connect(self.__clickedToolButtonDrawPaintRule)


        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE DRAW :::::::::::::::::    
        #     
        self.view_draw_1.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_2.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_1.signal_main_view.connect(self.main_view)
        self.view_draw_2.signal_main_view.connect(self.main_view)
        self.view_draw_1.signal_end_draw_geometry.connect(self.end_draw_geometry)
        self.view_draw_2.signal_end_draw_geometry.connect(self.end_draw_geometry)

        self.scene_draw.signal_next_point.connect(self.nextPoint)


        self.scene_draw.signal_point_point.connect(self.commandPoint)
        self.scene_draw.signal_point_line.connect(self.commandLine)
        self.scene_draw.signal_point_move.connect(self.commandMove)
        self.scene_draw.signal_point_copy.connect(self.commandCopy)
        self.scene_draw.signal_point_rotate.connect(self.commandRotate)
        self.scene_draw.signal_point_erase.connect(self.commandErase)
        self.scene_draw.signal_point_intersection.connect(self.commandIntersection)
        self.scene_draw.signal_point_rule.connect(self.commandRule)


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
        
        commands =     ["point", "line", "pline", "rectang", "erase", "move", "copy", "rotate", "zoom", "views", "import", "intersection"]
        commands_min = ["p",     "l",    "pl",    "rec",     "er",   "mo",   "co",    "ro",      "z",    "v", "im", "in"]
        
        #se ejecuta si la entrada es un comando
        if ((data_consola in commands) or (data_consola in commands_min)) and current_command == "" :
            if data_consola in commands:
                index = commands.index(data_consola)
            elif  data_consola in commands_min:
                index = commands_min.index(data_consola)

            command = commands[index]
            print("comando: {}".format(command))

            if command == "point" :
                self.commandPoint({"step":1, "data":None})                

            elif command == "line" :
                self.commandLine({"step":1, "data":None})    

            elif command == "move" :
                self.commandMove({"step":1, "data":None})    

            elif command == "copy" :
                self.commandCopy({"step":1, "data":None})    

            elif command == "rotate" :
                self.commandRotate({"step":1, "data":None})    
                
            elif command == "erase" :
                self.commandErase({"step":1, "data":None})    

            elif command == "import" :
                self.commandImport({"step":1, "data":None})    

            elif command == "intersection" :
                self.commandIntersection({"step":1, "data":None})    

            elif command == "rectang" :
                self.scene_draw.drawRectangleScene()
                self.init_tool_geometry(command,"Ingrese el primer punto [Exit]:")

            elif command == "pline" :
                self.scene_draw.drawPolylineScene()
                self.init_tool_geometry(command,"Ingrese el primer punto [Exit]:")

            elif command == "zoom" :
                self.init_tool_geometry(command,"[Extents Window] <E>:")

            elif command == "views" :
                self.init_tool_geometry(command,"[1 2] <1>:")
        
        #se ejecuta si ya hay un comando activo
        elif current_command in commands:

            #exit: salir de la edición de objeto
            if (data_consola.lower() == "e" or data_consola.lower() == "exit") and "Exit" in descrip_command:
                self.msnConsole("Command","_cancel")
                self.end_draw_geometry()                
                self.scene_draw.endDrawGeometry()
                self.view_draw_1.selectElement(False)
                self.view_draw_2.selectElement(False)                
                self.scene_draw.update()
            
            #se ejecuta si la entrada es una opcion de zoom
            elif current_command == "zoom" and descrip_command == "[Extents Window] <E>:":
                
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

            #se ejecuta si la entrada es una opcion de vistas
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

            #se ejecuta si la entrada es una opcion de mover
            elif current_command == "move":

                selected_items = len(self.scene_draw.selected_items)
                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.commandMove({"step":3, "data":None})
                  

                elif descrip_command == "Ingrese el primer punto [Exit]:" and selected_items > 0:
                    
                    point_vertex_ant = self.scene_draw.point_vertex_ant
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_vertex_ant)
                    if point == None:
                        return
                    self.commandMove({"step":4, "data":point})

                    point_vertex =QPointF(point[0],point[1])
                    self.scene_draw.point_vertex = point_vertex
                    self.scene_draw.point_vertex_ant = point_vertex
                    

                elif descrip_command == "Ingrese el segundo punto [Exit]:" and selected_items > 0:
                    point_ant = self.scene_draw.point_vertex_ant  
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_ant)
                    if point == None:
                        return
                    self.commandMove({"step":5, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                    
                else:
                    return

            #se ejecuta si la entrada es una opcion de copiar
            elif current_command == "copy":                              
                
                selected_items = len(self.scene_draw.selected_items)                
                point_ant = self.scene_draw.point_vertex_ant
                input_point = data_consola.split(",")
                point  = self.pointFromConsole(input_point, point_ant)

                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.commandCopy({"step":3, "data":None})

                elif descrip_command == "Ingrese el primer punto [Exit]:" and selected_items > 0:
                    if point == None:
                        return
                    self.commandCopy({"step":4, "data":point})
                    point_vertex =QPointF(point[0],point[1])
                    self.scene_draw.point_vertex = point_vertex
                    self.scene_draw.point_vertex_ant = point_vertex                    

                elif descrip_command == "Ingrese el segundo punto [Exit]:" and selected_items > 0:
                    if point == None:
                        return
                    self.commandCopy({"step":5, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                    self.lineEdit_console.setText("")
                    
                else:
                    return
                    
            #se ejecuta si la entrada es una opcion de rotar
            elif current_command == "rotate":

                selected_items = len(self.scene_draw.selected_items)
                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.commandRotate({"step":3, "data":None})
                  

                elif descrip_command == "Ingrese el punto base [Exit]:" and selected_items > 0:
                    
                    point_vertex_ant = self.scene_draw.point_vertex_ant
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_vertex_ant)
                    if point == None:
                        return
                    self.commandRotate({"step":4, "data":point})
                    point_vertex =QPointF(point[0],point[1])
                    self.scene_draw.point_vertex = point_vertex
                    self.scene_draw.point_vertex_ant = point_vertex
                    

                elif descrip_command == "Ingrese el ángulo [Exit]:" and selected_items > 0:
                    point_ant = self.scene_draw.point_vertex_ant  
                    input_angle = data_consola
   
                    if not isNumber(input_angle):
                        return
                    input_angle = float(input_angle)



                    self.commandRotate({"step":5, "data":
                                            [[point_ant.x(),point_ant.y()],
                                                        input_angle]
                                        })
                    
                else:
                    return

            #se ejecuta si la entrada es una opcion de borrar
            elif current_command == "erase":

                selected_items = len(self.scene_draw.selected_items)                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.commandErase({"step":3, "data":None})

            #se ejecuta si la entrada es una opcion de interseccion
            elif current_command == "intersection":
                selected_items = len(self.scene_draw.selected_items)   
                            
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items == 2:                                    
                    self.commandIntersection({"step":3, "data":None})
                else:
                    self.msnConsole("Error","Selecciona dos líneas")



            #se ejecuta si la entrada es una opcion de punto
            elif current_command == "point":
                input_point = data_consola.split(",")
                point_ant = self.scene_draw.point_vertex_ant
                point  = self.pointFromConsole(input_point, point_ant)
                point_ant = self.scene_draw.point_vertex_ant
                if point == None:
                    return
                self.commandPoint({"step":2, "data": point})
                self.lineEdit_console.setText("")

            #se ejecuta si la entrada es una opcion de linea
            elif current_command == "line":
                input_point = data_consola.split(",")
                point_ant = self.scene_draw.point_vertex_ant
                point  = self.pointFromConsole(input_point, point_ant)
                if point == None:
                    return
                
                point_vertex =QPointF(point[0],point[1])

                if descrip_command == "Ingrese el primer punto [Exit]:" and point_ant == None:
                    if point == None:
                        return
                    self.commandLine({"step":2, "data":point})
                    self.scene_draw.point_vertex_ant = point_vertex     

                elif descrip_command == "Ingrese el siguiente punto [Exit]:" and point_ant != None:
                    if point == None:
                        return
                    self.commandLine({"step":3, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                    self.scene_draw.point_vertex_ant = point_vertex                    
                    self.lineEdit_console.setText("")
                    
                else:
                    return

            else:
                return


        else:
            print("demas opciones")

            return

            if current_command == "point" or current_command == "rectang" or current_command == "line":
                

                """
                # close: cerrar un poligono  
                elif data_consola.lower() == "c" and "Close" in descrip_command:
                    point_vertex_init = self.scene_draw.point_vertex_init
                    point_vertex_ant = self.scene_draw.point_vertex_ant
                    self.scene_draw.drawGeometry(point_vertex_init, point_vertex_ant)
                    self.scene_draw.endDrawGeometry()
                    self.end_draw_geometry()                
                    self.msnConsole("Command","_line close")
                    return

                #se ejecuta si la entrada es un punto nuevo
                elif current_command == "rectang":

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
                """



    def pointInRect(self, point:QPointF, rec:QRectF):
        val = True
        x = point.x()
        y = point.y()

        xi = rec.x()
        yi = rec.y()
        xf = rec.x()+rec.width()
        yf = rec.y()+rec.height()

        if xi <= x <= xf:
            if yi <= y <=yf:
                pass
            else:
                val = False
        else:
            val = False
        return val

    def commandPoint(self, input:dict):        
        step = input["step"]
        coordinate = input["data"]
        if step == 1:
            # se activa modo punto
            self.scene_draw.isDrawPoint = True            
            self.init_tool_geometry("point","Ingrese un punto [Exit]:")
            
        elif step == 2:
            point_vertex = QPointF(coordinate[0],coordinate[1])
            items = self.scene_draw.items(point_vertex)
            cancel_point = False

            # verifica si el punto esta por fuera de los limites
            if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):
                cancel_point = True
                self.msnConsole(
                    "Warning",
                    "Posición fuera del límite del dibujo."
                    )
                return cancel_point

            #verifica si hay puntos existentes
            for item in items:
                if type(item) == PointItem:
                    name = item.getData()["name"]
                    if name != "pointTemp":                        
                        self.msnConsole(
                            "Warning",
                            "En esta posición ya existe el punto {}".format(name)
                            )
                        return item

            #::::::::::::  punto  ::::::::::::::::
            items = self.scene_draw.items()
            points = self.scene_draw.admin.list_points
            id_max = 0
            for point in points:
                id = int(points[point]["id"])                
                if id > id_max:
                    id_max = id
            no_id = id_max+1
            text_id = TextItem(no_id, QPointF(0,0))
            #self.scene_draw.addItem(text_id)
            new_point = PointItem(no_id, f"POINT#{no_id}",point_vertex, text_id)
            new_point.showLabel = self.mode_label_draw
            self.scene_draw.admin.addCommand(new_point)
            self.msnConsole("Command","Se ha creado el punto {}".format(new_point.id))
            return new_point
            
    def commandLine(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        

        if step == 1:
            # se activa modo linea
            self.scene_draw.isDrawLine = True            
            self.init_tool_geometry("line","Ingrese el primer punto [Exit]:")
            
        elif step == 2:
            #self.point1 = self.commandPoint({"step":2, "data": [data[0],data[1]]}) 
            self.msnLabelConsole("line","Ingrese el siguiente punto [Exit]:")
  
        elif step == 3:
            self.point1 = self.commandPoint({"step":2, "data": [data[0][0],data[0][1]]}) 
            self.point2 = self.commandPoint({"step":2, "data": [data[1][0],data[1][1]]}) 

            if  self.point1.name==self.point2.name:
                return

            #::::::::::::  linea  ::::::::::::::::
            lines = self.scene_draw.admin.list_lines
            id_max = 0
            for line in lines:
                id = int(lines[line]["id"])                
                if id > id_max:
                    id_max = id
            no_id = id_max + 1

            text_id = TextItem(no_id, QPointF(0,0))
            #self.scene_draw.addItem(text_id)
            new_line = LineItem(no_id, f"LINE#{no_id}",self.point1,self.point2, text_id)

            #new_line.setPen(QPen(QColor(Qt.red),0))
            new_line.showLabel = self.mode_label_draw
            self.scene_draw.admin.addCommand(new_line)


            '''
            print("\n",self.point1.getData()['name'])
            lineas = self.point1.anchored_lines
            for line in lineas:
                print(line.getData()['name'])

            print("\n",self.point2.getData()['name'])
            lineas = self.point2.anchored_lines
            for line in lineas:
                print(line.name)
            '''

            self.point1 = self.point2
            self.msnConsole("Command","Se ha creado la linea  {}".format(new_line.id))
            return new_line

    def commandMove(self, input:dict):

        
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            # se activa modo mover
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawMove= True            
            self.init_tool_geometry("move","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
                #verificar cuales lineas si toca
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
              
            count = 0
            for item in items:    

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelected = True
                    if not (item in self.scene_draw.selected_items):
                        count += 1
                        self.scene_draw.selected_items.append(item)

                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelected = True
                    point_B.isSelected = True
                    item.isSelected = True

                    if not (point_A in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(point_A)
                        
                    if not (point_B in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(point_B)

                    if not (item in self.scene_draw.selected_items_line) :
                        count += 1
                        self.scene_draw.selected_items_line.append(item)

                self.scene_draw.update()

                #    if item.getData()["name"] != "rectTemp":


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.scene_draw.selected_items),
                        count
                        ))
                

        #Inicio de mover
        elif step == 3:
            selected_items = len(self.scene_draw.selected_items)
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("move", "Ingrese el primer punto [Exit]:")
        
        # Se recibe el primer punto
        elif step == 4:
            self.msnConsole("Command","Punto inicial = {}".format(data))
            self.msnLabelConsole("move", "Ingrese el segundo punto [Exit]:")

        # Se recibe el segundo punto
        elif step == 5:
           
            items = self.scene_draw.selected_items
  
 
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_vertex=QPointF(xi+dx, yi+dy)

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):                    
                    self.msnConsole(
                        "Warning",
                        "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"])
                        )
                    return 
                
                items_in_new_pos = self.scene_draw.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.msnConsole(
                                "Error",
                                "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name)
                                )
                            return 

            self.scene_draw.admin.moveCommand(items, dx=dx,dy=dy)
            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()
            self.msnConsole("Command","Punto Final = {}".format(data[1]))
            self.msnConsole("Command","Se ha movido los elementos seleccionados".format())

    def commandCopy(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        

        # 1) Inicio, selección de elementos
        if step == 1:
            # se activa modo copiar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawCopy = True            
            self.init_tool_geometry("copy","Seleccione un elemento [Exit]:")  
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:       




                item.isSelected = True
                if not (item in self.scene_draw.selected_items) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.scene_draw.selected_items.append(item)



            if count > 0:
                self.msnConsole(
                    "Command",
                    "Copiar Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.scene_draw.selected_items),
                        count
                        ))
        #Inicio de copiar
        elif step == 3:
            selected_items = len(self.scene_draw.selected_items)
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("copy", "Ingrese el primer punto [Exit]:")
        
        # Se recibe el primer punto
        elif step == 4:
            self.msnConsole("Command","Punto inicial = {}".format(data))
            self.msnLabelConsole("copy", "Ingrese el segundo punto [Exit]:")
            

        # Se recibe el segundo punto
        elif step == 5:           

            items = self.scene_draw.selected_items
            
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                if isinstance(item, PointItem):
                    xi = item.getData()["coordinates"][0]
                    yi =item.getData()["coordinates"][1]
                    self.commandPoint({"step":2, "data": [xi+dx,yi+dy]})
                if isinstance(item, LineItem):


                    x_start_point = (item.start_point.getData()["coordinates"][0])+ dx
                    y_start_point = (item.start_point.getData()["coordinates"][1]) + dy
                    x_end_point =   (item.end_point.getData()["coordinates"][0]) + dx
                    y_end_point =   (item.end_point.getData()["coordinates"][1]) + dy

                   
                    
                    #self.commandLine({"step":2, "data":[data[0][0], data[0][1]]})
                    self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})

    def commandRotate(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            # se activa modo rotar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawRotate= True            
            self.init_tool_geometry("rotate","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelected = True
                    if not (item in self.scene_draw.selected_items):
                        count += 1
                        self.scene_draw.selected_items.append(item)
                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelected = True
                    point_B.isSelected = True
                    item.isSelected = True

                    if not (point_A in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(point_A)
                        
                    if not (point_B in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(point_B)

                    if not (item in self.scene_draw.selected_items_line) :
                        count += 1
                        self.scene_draw.selected_items_line.append(item)

                '''
                item.isSelected = True
                if not (item in self.scene_draw.selected_items) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.scene_draw.selected_items.append(item)
                '''


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.scene_draw.selected_items),
                        count
                        ))
        #Inicio de rotar
        elif step == 3:
            selected_items = len(self.scene_draw.selected_items)
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("rotate", "Ingrese el punto base [Exit]:")        

        
        # Se recibe el punto centro para rotar
        elif step == 4:
            self.msnConsole("Command","Punto base = {}".format(data))
            self.msnLabelConsole("rotate", "Ingrese el ángulo [Exit]:")

        # Se recibe el segundo punto
        elif step == 5:



            items = self.scene_draw.selected_items
            x_ref, y_ref = data[0][0], data[0][1]
            point_ref = QPointF(x_ref, y_ref)
            angle_ref = data[1]

            """
            group_selected = QGraphicsItemGroup()
            for item_i in items_i:                
                group_selected.addToGroup(item_i)
            self.scene_draw.addItem(group_selected)
            transform = QTransform().translate(pivot.x(), pivot.y()).rotate(angle_ref).translate(-pivot.x(), -pivot.y())
            group_selected.setTransform(transform, combine=False)

            elements = group_selected.childItems()
            self.scene_draw.removeItem(group_selected)
            """
            list_items_new_pos =[]

 
            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_to_rotate =  QPointF(xi,yi)
                angle_rad_ref = math.radians(angle_ref)     
                dx = point_to_rotate.x() - point_ref.x()
                dy = point_to_rotate.y() - point_ref.y()
                dist = math.sqrt(dx*dx + dy*dy)
                angle_point = math.atan2(dy, dx)
                if angle_point < 0:
                    angle_point = (2*math.pi) + angle_point

                angle_new = angle_point + angle_rad_ref

                # Calcular la nueva posición del punto después de la rotación
                new_x = point_ref.x() + dist * math.cos(angle_new)
                new_y = point_ref.y() + dist * math.sin(angle_new)              
                
                point_vertex=QPointF(new_x, new_y)            

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):                    
                    self.msnConsole(
                        "Warning",
                        "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"])
                        )
                    return 
                
                items_in_new_pos = self.scene_draw.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.msnConsole(
                                "Error",
                                "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name)
                                )
                            return 
                
                list_items_new_pos.append([item, xi, yi, new_x, new_y])


            self.scene_draw.admin.rotateCommand(items= list_items_new_pos)
            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()
            self.msnConsole("Command","ángulo = {}".format(data[1]))
            self.msnConsole("Command","Se ha rotado los elementos seleccionados".format())

    def commandErase(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            # se activa modo borrar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawErase= True            
            self.init_tool_geometry("erase","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):                    
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelected = True
                    if not (item in self.scene_draw.selected_items):
                        if len(item.anchored_lines) != 0:
                            self.msnConsole("Command","No se puede eliminar {}, esta anclado a mas de dos lienas ".format(item.name))
                            item.isSelected=False
                        else:
                            count += 1
                            self.scene_draw.selected_items.append(item)
          
                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point



                    if not (point_A in self.scene_draw.selected_items) :
                        count += 1
                        if item in point_A.anchored_lines and len(point_A.anchored_lines) == 1:
                            self.scene_draw.selected_items.append(point_A)
                            point_A.isSelected = True


                        
                    if not (point_B in self.scene_draw.selected_items) :
                        count += 1
                        if item in point_B.anchored_lines and len(point_B.anchored_lines) == 1:

                            self.scene_draw.selected_items.append(point_B)
                            point_B.isSelected = True

                    if not (item in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(item)
                        item.isSelected = True


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.scene_draw.selected_items),
                        count
                        ))
                
        #Inicio de borrar
        elif step == 3:
            selected_items = len(self.scene_draw.selected_items)
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items)) 

            self.scene_draw.admin.removeCommand(items= self.scene_draw.selected_items)
            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()

            self.msnConsole("Command","Se ha eliminado los elementos seleccionados".format())

    def commandImport(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            options = QFileDialog.Options()
            dxf_file_path, _ = QFileDialog.getOpenFileName(self,"Importar DXF","","Data files dxf (*.dxf)", options=options)

            if dxf_file_path:
                doc = ezdxf.readfile(dxf_file_path)            
                msp = doc.modelspace()

                for entity in msp:
                    if entity.dxftype() == "POINT":
                        xi = entity.dxf.location[0]
                        yi = entity.dxf.location[1]

                        self.commandPoint({"step":2, "data": [xi,yi]})

                    elif entity.dxftype() == "LINE":
                        start_point = entity.dxf.start
                        end_point = entity.dxf.end

                        x_start_point =start_point[0]
                        y_start_point =start_point[1]
                        x_end_point =end_point[0]
                        y_end_point =end_point[1]
                        self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})


                        
                    elif entity.dxftype() == "LWPOLYLINE":
                        points = [(vertex[0], vertex[1]) for vertex in entity.get_points()]
                        for i in range(len(points) - 1):
                            start_point = points[i]
                            end_point = points[i+1]
                            x_start_point, y_start_point = start_point
                            x_end_point, y_end_point = end_point
                            self.commandLine({"step": 3, "data": [[x_start_point, y_start_point], [x_end_point, y_end_point]]})

    def commandIntersection(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
        # 1) Inicio, selección de elementos
        if step == 1:
            # se activa modo Interseccion
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawIntersection= True            
            self.init_tool_geometry("intersection","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):                    
                    continue    

                elif isinstance(item,PointItem):
                    continue

                elif isinstance(item, LineItem):

                    if not (item in self.scene_draw.selected_items) :
                        count += 1
                        self.scene_draw.selected_items.append(item)
                        item.isSelected = True


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.scene_draw.selected_items),
                        count
                        ))
    
        #Inicio de interseccion
        elif step == 3:
            selected_items = len(self.scene_draw.selected_items)    
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items)) 

            line_A= self.scene_draw.selected_items[0]
            line_B= self.scene_draw.selected_items[1]

            # Obtener los puntos finales de cada línea
            lA_p1, lA_p2 = line_A.getPoints()
            lB_p1, lB_p2 = line_B.getPoints()
            
            lA_p1f, lA_p2f  = lA_p1.getCoordinates(), lA_p2.getCoordinates()
            lB_p1f, lB_p2f = lB_p1.getCoordinates(), lB_p2.getCoordinates()

            line_Af = QLineF(lA_p1f, lA_p2f )
            line_Bf = QLineF(lB_p1f, lB_p2f)

            '''
            print("Datos:",p_1f,p_2f,p_3f,p_4f,line_1f,line_2f)
            Datos:
            PySide6.QtCore.QPointF(0.000000, 15.230280)
            PySide6.QtCore.QPointF(14.769720, 15.230280)
            PySide6.QtCore.QPointF(10.000000, 20.000000)
            PySide6.QtCore.QPointF(20.000000, 10.000000)
            PySide6.QtCore.QLineF(0.000000, 15.230280, 14.769720, 15.230280) 
            PySide6.QtCore.QLineF(10.000000, 20.000000, 20.000000, 10.000000)
            '''

            #tengo un problema cuando un estremo se intresdetcva
            #con la linea ya que se general solo tre slineas y no cuatro
           
            # Calcular la intersección entre las dos líneas
            intersection_type, intersection_point = line_Af.intersects(line_Bf)
            print("TIpo:",intersection_type)

            # Verificar si las líneas se intersectan
            if intersection_type == QLineF.IntersectionType.BoundedIntersection or intersection_type == QLineF.IntersectionType.UnboundedIntersection:

                new_point = self.commandPoint({"step":2, "data": [intersection_point.x(),intersection_point.y()]})

                '''
                print(new_point)
                d1 = (((lA_p1f.x()-intersection_point.x())**2) + ((lA_p1f.y()-intersection_point.y())**2))**0.5
                d2 = (((lA_p2f.x()-intersection_point.x())**2) + ((lA_p2f.y()-intersection_point.y())**2))**0.5
                d3 = (((lB_p1f.x()-intersection_point.x())**2) + ((lB_p1f.y()-intersection_point.y())**2))**0.5
                d4 = (((lB_p2f.x()-intersection_point.x())**2) + ((lB_p2f.y()-intersection_point.y())**2))**0.5
                print("{:.2f}::{:.2f}::{:.2f}::{:.2f}".format(d1,d2,d3,d4))
                '''

                # Linea A
                if new_point != lA_p1 and new_point != lA_p2:

                    self.scene_draw.admin.updateCommand(line_A, [lA_p1, new_point])
                    line_A_new = self.commandLine({"step":3, "data":[
                                [intersection_point.x(),intersection_point.y()],
                                [lA_p2f.x(),lA_p2f.y()]]})
                    new_point.addAnchoredLine(line_A)
                    new_point.addAnchoredLine(line_A_new)
                '''
                    print("A >>>> ok")

                else:
                    print("AA>> [{} {}] el punto ya exite: {}".format(lA_p1, lA_p2, new_point))
                '''

                # Linea B
                if new_point != lB_p1 and new_point != lB_p2:
                    self.scene_draw.admin.updateCommand(line_B, [lB_p1, new_point])
                    line_B_new = self.commandLine({"step":3, "data":[
                                [intersection_point.x(),intersection_point.y()],
                                [lB_p2f.x(),lB_p2f.y()]]})
                    new_point.addAnchoredLine(line_B)
                    new_point.addAnchoredLine(line_B_new)
                '''
                    print("B >>>> ok")
                else:
                    print("BB>> [{} {}] el punto ya exite: {}".format(lB_p1, lB_p2, new_point))
                '''

            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()
            self.msnConsole("Command","Se ha creado la intersección ".format())
        """
        elif step == 5:           

            items = self.scene_draw.selected_items
            
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
            
            
                if isinstance(item, PointItem):
                    xi = item.getData()["coordinates"][0]
                    yi =item.getData()["coordinates"][1]
                    self.commandPoint({"step":2, "data": [xi+dx,yi+dy]})
                if isinstance(item, LineItem):


                    x_start_point = (item.start_point.getData()["coordinates"][0])+ dx
                    y_start_point = (item.start_point.getData()["coordinates"][1]) + dy
                    x_end_point =   (item.end_point.getData()["coordinates"][0]) + dx
                    y_end_point =   (item.end_point.getData()["coordinates"][1]) + dy

                   
                    
                    #self.commandLine({"step":2, "data":[data[0][0], data[0][1]]})
                    self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})

        """


    def commandRule(self, input:dict):

        
        step = input["step"]
        data = input["data"]

        if step == 1:         
            self.scene_draw.isDrawRule = True            
            self.init_tool_geometry("rule", "Ingrese el primer punto [Exit]:")

        if step == 2:                  
            self.init_tool_geometry("rule", "Ingrese el segundo punto [Exit]:")


        elif step == 3:  
            x1, y1 = data[0][0],data[0][1]
            x2, y2 = data[1][0],data[1][1]

            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )
            dist = (((dx)**2)+((dy)**2))**0.5
            if dx != 0:
                angle = math.degrees(math.atan(dy/dx))
            else:
                angle = math.degrees(math.atan(dy/0.000000001))


            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()
            
            self.msnConsole("Command","Punto Inicial: [{},{}] Punto Final: [{}, {}]".format(x1,y1,x2,y2))
            self.msnConsole("Command","dx:{} dy:{}".format(dx,dy))
            self.msnConsole("Command","Distancia: {}".format(dist))
            self.msnConsole("Command","Ángulo: {}".format(angle))

            #self.msnConsole("Command","nose: {}".format(point_d))



   
        # Se recibe el segundo punto
        elif step == 5:
            return
           
            items = self.scene_draw.selected_items
  
 
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_vertex=QPointF(xi+dx, yi+dy)

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):                    
                    self.msnConsole(
                        "Warning",
                        "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"])
                        )
                    return 
                
                items_in_new_pos = self.scene_draw.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.msnConsole(
                                "Error",
                                "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name)
                                )
                            return 

            self.scene_draw.admin.moveCommand(items, dx=dx,dy=dy)
            self.scene_draw.endDrawGeometry()
            self.end_draw_geometry()
            self.msnConsole("Command","Punto Final = {}".format(data[1]))
            self.msnConsole("Command","Se ha movido los elementos seleccionados".format())



    def __clickedToolButtonDrawPaintMove(self):
        self.scene_draw.endDrawGeometry()
        self.commandMove({"step":1, "data":None})

    def __clickedToolButtonDrawPaintCopy(self):
        self.scene_draw.endDrawGeometry()
        self.commandCopy({"step":1, "data":None})  

    def __clickedToolButtonDrawPaintRotate(self):
        self.scene_draw.endDrawGeometry()
        self.commandRotate({"step":1, "data":None})  

    def __clickedToolButtonDrawPaintErase(self):
        self.scene_draw.endDrawGeometry()
        self.commandErase({"step":1, "data":None})  

    def __clickedToolButtonDrawPaintImport(self):
        self.scene_draw.endDrawGeometry()
        self.commandImport({"step":1, "data":None})       
 
    def __clickedToolButtonDrawPaintIntersection(self):       
        self.scene_draw.endDrawGeometry()
        self.commandIntersection({"step":1, "data":None})  

    def __clickedToolButtonDrawPaintRule(self):       
        self.scene_draw.endDrawGeometry()
        self.commandRule({"step":1, "data":None})  
       
        


    def __clickedToolButtonDrawPaintPoint(self):
        self.scene_draw.endDrawGeometry()
        self.commandPoint({"step":1, "data":None})     



    def __clickedToolButtonDrawPaintLine(self):
        self.scene_draw.endDrawGeometry()
        self.commandLine({"step":1, "data":None})     

    def __clickedToolButtonDrawPaintRectangle(self):
        self.scene_draw.endDrawGeometry()
        self.scene_draw.drawRectangleScene()
        self.init_tool_geometry("rectang","Ingrese el primer punto [Exit]:")
      
    def __clickedToolButtonDrawPaintPolyline(self):
        return
        self.init_draw_geometry("pline")
        self.scene_draw.drawPolylineScene()




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

    def pointFromConsole(self, input, point_prev):
        """
        Esta función toma una entrada `input` de consola, procesa su tipo y devuelve una nueva coordenada `point`
        en función de la entrada y la coordenada anterior `point_prev`.

        Args:
            input (list): una lista que contiene una o más entradas de consola en función del tipo de entrada.
                Puede contener coordenadas, distancias, ángulos, dx-dy, etc.
            point_prev (list): una lista que contiene una coordenada previa que se utilizará como referencia para
                calcular la siguiente coordenada.

        Returns:
            list: una lista que contiene dos valores: `x` e `y`, que representan la nueva coordenada calculada.


        Ejemplos:
            # Calcular una coordenada para una distancia y un ángulo con respecto a una coordenada previa (10, 10).
            >>> pfc = pointFromConsole(["@45", "5"], [10, 10])
            >>> print(pfc)
            [13.535898384862247, 13.535898384862247]

            # Calcular una coordenada para una distancia X y una distancia Y con respecto a una coordenada previa (10, 10).
            >>> pfc = pointFromConsole(["#3", "4"], [10, 10])
            >>> print(pfc)
            [13.0, 14.0]

            # Calcular una coordenada para una sola coordenada.
            >>> pfc = pointFromConsole(["7"], None)
            >>> print(pfc)
            [7.0, 7.0]
        """


        # Si es el primer punto y se recibe un solo valor input=x=y
        
        if len(input) == 1 and point_prev == None:
            x = input[0]
            if isNumber(x):
                x = float(x)
                y = x
            else:
                return None

        # Si es el segundo punto y se recibe un solo valor input=dist
        elif len(input) == 1 and point_prev!= None:
            dist = input[0]
            if isNumber(dist):
                point_vertex = self.scene_draw.point_vertex
                x, y = self.pointInLine(point_prev, point_vertex,float(dist))
                

            else:
                return None
    
        # Si es el segundo punto y se recibe angulo y distancia input=@angulo,dist
        elif len(input) == 2 and input[0][0] == "@" and point_prev!= None:
            angle = input[0][1:]
            dist = input[1]
            if isNumber(angle) and isNumber(dist):
                angle = float(angle)
                dist = float(dist)
                dx = dist * math.cos(math.radians(angle))
                dy = dist * math.sin(math.radians(angle))
                x = point_prev.x() + dx
                y = point_prev.y() + dy                        
            else:
                return None

        # Si es el segundo punto y se recibe distancia X y distancia Y input=#dx,dy
        elif len(input) == 2 and input[0][0] == "#" and point_prev!= None:
            dx = input[0][1:]
            dy = input[1]
            if isNumber(dx) and isNumber(dy):
                x = point_prev.x() + float(dx)
                y = point_prev.y() + float(dy)                        
            else:
                return None
                
        # Si es el segundo punto y se recibe coordenada input=x,y
        elif len(input) == 2:
            x = input[0]
            y = input[1]
            if isNumber(x) and isNumber(y):
                x = float(x)
                y = float(y) 
            else: 
                return None

        # en los demas casos ejem: texto
        else:
            return None

        point=[x,y]
        return point


    def pointInLine(self, p1:QPointF, p2:QPointF,dist_i):
        """
        Devuelve las coordenadas de un punto en la línea que va desde p1 hasta p2,
        a una distancia determinada desde p1.

        Args:
            p1: QPointF. Punto de inicio de la línea.
            p2: QPointF. Punto final de la línea.
            dist_i: float. Distancia desde p1 hasta el punto que se quiere calcular.

        Returns:
            Tuple[float, float]: Coordenadas del punto en la línea, como una tupla de dos floats (x, y).

        Raises:
            ValueError: Si p1 y p2 son el mismo punto o dist_i es menor o igual a cero.

        Example:
            --------
            >>> p1 = QPointF(1, 1)
            >>> p2 = QPointF(5, 5)
            >>> dist_i = 2.89
            >>> self.pointInLine(p1, p2, dist_i)
            (3.00111219075793, 3.00111219075793)

        """
        
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

    def modeOriginDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar el origen.

        Args:
            mode(bool): modo de los ejes
                        False: origen Oculto
                        False: origen visible
        """ 
        self.view_draw_1.isModeOrigin=mode
        self.view_draw_2.isModeOrigin=mode
        self.scene_draw.update()

    def modeAxisDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar los ejes principales.

        Args:
            mode(bool): modo de los ejes
                        False: ejes Oculta
                        False: ejes visible
        """ 
        self.view_draw_1.isModeAxis=mode
        self.view_draw_2.isModeAxis=mode
        self.scene_draw.update()
        
    def modeGridDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar la grilla.

        Args:
            mode(bool): modo de la grilla
                        False: grilla Oculta
                        False: grilla visible
        """ 
        self.view_draw_1.isModeGrid=mode
        self.view_draw_2.isModeGrid=mode
        self.scene_draw.update()
        
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

    def modeLabelDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar las etiquetas de los elemetos.

        Args:
            mode(bool): modo de las etiquetas
                        False: etiquetas Ocultas
                        False: etiquetas visibles
        """ 
        self.mode_label_draw = mode
        items = self.scene_draw.items()
        for item in items:
            item.showLabel = mode
        self.scene_draw.update()
            
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
        #try:
            #Presiono tecla de A-Z
            #print()dejar tabien numero, punto coma y espacoipn- 

        if key >= 40 and key <= 90:                
            self.__keyPressViewConsole(event.text())

        elif key == Qt.Key_Enter or key == 16777220:
            self.lineEdit_console.setFocus()
            #self.__returnPressedLineEditConsole()

        elif key == Qt.Key_Enter or key == 16777216:
            print("funcionalidad escapar")
            self.end_draw_geometry()                
            self.msnConsole("Command","_cancel")
            self.scene_draw.endDrawGeometry()
            self.view_draw_1.zoomWindow(False)
            self.view_draw_2.zoomWindow(False)
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)

        return super().keyPressEvent(event)
        #except UnicodeDecodeError:
            #print("no puede decodificar Ejemplo: Ñ ")


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


