""" Este módulo contiene la clase Ui_FormDraw, para incluirla en main window, es el frame que contiene la parte del dibujo."""

from asyncio import events
from hashlib import new
import math
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF)
from PySide6.QtWidgets import ( QFrame,QGraphicsScene,QGraphicsView)
from PySide6.QtGui import (QTransform ,QPen,QBrush)
from ui import ui_frame_draw
from clases import class_ui_widget_draw_menu_data
from clases import class_ui_widget_draw_menu_mesh
from clases import class_projects


class GraphicsViewDraw (QGraphicsView):
    def __init__(self, parent=None):
        super(GraphicsViewDraw, self).__init__(parent)

        #self.setSceneRect(QRectF(self.viewport().rect()))
        self.setSceneRect(QRectF(0,0,100,100))
        
        self.graphicsScene_draw = GraphicsSceneDraw()


        self.isLine = False
        self.isDelate = False
        self.isClear = False
        self.isObject = None
        self.startX=None
        self.startY=None

        self.setStyleSheet("background-color: #444444 ;border: none;")
        #self.setStyleSheet("background-color: #444444 ;border: none;")

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
    def getGraphicsScene(self):
        return  self.graphicsScene_draw

    def tools (self, a):
        if self.isLine == True:
            pen= QPen(Qt.red)
            brush = QBrush(Qt.SolidPattern)
            self.graphicsScene_draw.addItem(self.graphicsScene_draw.addEllipse(a.x(),a.y(),30,30,pen,brush))
            self.setScene(self.graphicsScene_draw)
            
            self.show()
        if self.isDelate == True:
            items = self.items(a.x(),a.y())
            for item in items:
                self.graphicsScene_draw.removeItem(item)

    def paintObject(self,b):
        if self.isObject != None:
            object = self.isObject

            if object == 0:#line
                pen= QPen(Qt.black)
                self.graphicsScene_draw.addItem(self.graphicsScene_draw.addLine(self.startX,self.startY,b.x(),b.y(),pen))
                self.setScene(self.graphicsScene_draw)                
            if object == 1:#rect
                pen= QPen(Qt.yellow)
                brush = QBrush(Qt.SolidPattern)
                self.graphicsScene_draw.addItem(self.graphicsScene_draw.addRect(
                                                        self.startX,
                                                        self.startY,
                                                        b.x()-self.startX,
                                                        b.y()-self.startY,
                                                        pen,brush))
                self.setScene(self.graphicsScene_draw)   
            if object == 2:#Eli
                pen= QPen(Qt.green)
                brush = QBrush(Qt.SolidPattern)
                self.graphicsScene_draw.addItem(self.graphicsScene_draw.addEllipse(
                                                        self.startX,
                                                        self.startY,
                                                        b.x()-self.startX,
                                                        b.y()-self.startY,
                                                        pen,brush))
                self.setScene(self.graphicsScene_draw)

    def mousePressEvent(self, mouseEvent):
        if (mouseEvent.button() != Qt.LeftButton):
            return
        e = QPointF(self.mapToScene(mouseEvent.pos()))
        print("---PRESS----     {}    ------------".format(e))
        self.tools(e)

        self.startX=e.x()
        self.startY=e.y()
        
    def mouseMoveEvent(self, mouseEvent):

        e = QPointF(self.mapToScene(mouseEvent.pos()))
        print("---MOVE----     {}    ------------".format(e))
        self.tools(e)
        #print("-- mouseMoveEvent")

    def mouseReleaseEvent(self, mouseEvent):
        e = QPointF(self.mapToScene(mouseEvent.pos()))
        print("---Release----     {}    ------------".format(e))
        self.paintObject(e)
    
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Plus:
            self.scale_view(1.2)
        elif key == Qt.Key_Minus:
            self.scale_view(1 / 1.2)
        '''
        elif key == Qt.Key_Space or key == Qt.Key_Enter:
            for item in self.scene().items():
                if isinstance(item, Node):
                    item.setPos(-150 + random(300), -150 + random(300))
        else:
            QGraphicsView.keyPressEvent(self, event)
        '''
        """
    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        self.scale_view(math.pow(2.0, -delta / 240.0))
        """
    
    def scale_view(self, scaleFactor):
        factor = self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

        if factor < 0.07 or factor > 100:
            return

        self.scale(scaleFactor, scaleFactor)
    
class GraphicsSceneDraw (QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsSceneDraw, self).__init__(parent)

    def mousePressEvent(self, mouseEvent):

        '''
        MiddleButton: boton rueda raton
        LeftButton: boton izq raton
        RightButton: boton der raton
        '''
        if (mouseEvent.button() != Qt.LeftButton):
            return
        '''

        if self._my_mode == self.InsertItem:
            item = DiagramItem(self._my_item_type, self._my_item_menu)
            item.setBrush(self._my_item_color)
            self.addItem(item)
            item.setPos(mouseEvent.scenePos())
            self.item_inserted.emit(item)
        elif self._my_mode == self.InsertLine:
            self.line = QGraphicsLineItem(QLineF(mouseEvent.scenePos(),
                                        mouseEvent.scenePos()))
            self.line.setPen(QPen(self._my_line_color, 2))
            self.addItem(self.line)
        elif self._my_mode == self.InsertText:
            text_item = DiagramTextItem()
            text_item.setFont(self._my_font)
            text_item.setTextInteractionFlags(Qt.TextEditorInteraction)
            text_item.setZValue(1000.0)
            text_item.lost_focus.connect(self.editor_lost_focus)
            text_item.selected_change.connect(self.item_selected)
            self.addItem(text_item)
            text_item.setDefaultTextColor(self._my_text_color)
            text_item.setPos(mouseEvent.scenePos())
            self.text_inserted.emit(text_item)

        super(DiagramScene, self).mousePressEvent(mouseEvent)
        '''

    def mouseMoveEvent(self, mouseEvent):
        #print("-- mouseMoveEvent")
        '''
        if self._my_mode == self.InsertLine and self.line:
            new_line = QLineF(self.line.line().p1(), mouseEvent.scenePos())
            self.line.setLine(new_line)
        elif self._my_mode == self.MoveItem:
            super(DiagramScene, self).mouseMoveEvent(mouseEvent)
        '''

    def mouseReleaseEvent(self, mouseEvent):
        #print("--- mouseReleaseEvent")
        '''
        if self.line and self._my_mode == self.InsertLine:
            start_items = self.items(self.line.line().p1())
            if len(start_items) and start_items[0] == self.line:
                start_items.pop(0)
            end_items = self.items(self.line.line().p2())
            if len(end_items) and end_items[0] == self.line:
                end_items.pop(0)

            self.removeItem(self.line)
            self.line = None

            if (len(start_items) and len(end_items) and
                    isinstance(start_items[0], DiagramItem) and
                    isinstance(end_items[0], DiagramItem) and
                    start_items[0] != end_items[0]):
                start_item = start_items[0]
                end_item = end_items[0]
                arrow = Arrow(start_item, end_item)
                arrow.set_color(self._my_line_color)
                start_item.add_arrow(arrow)
                end_item.add_arrow(arrow)
                arrow.setZValue(-1000.0)
                self.addItem(arrow)
                arrow.update_position()

        self.line = None
        super(DiagramScene, self).mouseReleaseEvent(mouseEvent)
        '''

class FrameDraw(QFrame, ui_frame_draw.Ui_FormDraw):
    """Esta clase crea el QFrame draw para agregarlo a main window. """ 
    signal_home_open = Signal(str)
    signal_home_new = Signal()

    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str) 

    signal_project_save_state = Signal(bool)

    def __init__(self, parent = None, ):
        super(FrameDraw, self).__init__(parent)
        self.setupUi(self)

        # Configura la UI
        self.__configUi()
        
        # Establece los eventos de la UI
        self.__initEventUi()

    def resizeEvent(self, event):
        #print("Tamaño: {}".format(self.viewport().rect()))
        #self.graphicsView_draw.setSceneRect(QRectF(0,0,1000,1000))
        pass
 

    

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
    ###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 

        # ::::::::::   AJUSTA EL SPLITTER PARA LA ALTURA DE LA CONSOLA  ::::::::::::
        self.splitter.setStretchFactor(0, 1)
        #self.splitter.setStretchFactor(100, 0)        
        self.splitter.setSizes([100,1]) 

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphics  ::::::::::::::::::
        self.graphicsView_draw = GraphicsViewDraw()
        self.graphicsScene_draw = self.graphicsView_draw.getGraphicsScene()
        self.horizontalLayout_graphics.addWidget(self.graphicsView_draw)
        self.graphicsView_draw.show()       
        

        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-DATA  ::::::::::::::::::
        self.drawMenuData = class_ui_widget_draw_menu_data.WidgetDrawMenuData()        
        self.horizontalLayout_draw.addWidget(self.drawMenuData)

        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-MESH  ::::::::::::::::::
        self.drawMenuMesh = class_ui_widget_draw_menu_mesh.WidgetDrawMenuMesh(self.graphicsScene_draw,self.graphicsView_draw)        
        self.horizontalLayout_draw.addWidget(self.drawMenuMesh)

        self.label_console.setVisible(False)
    

        self.showHideDrawMenu("Data")

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-DATA :::::::::::::::::
        self.drawMenuData.signal_msn_critical.connect(self.showMessageStatusBarCritical)
        self.drawMenuData.signal_msn_satisfactory.connect(self.showMessageStatusBarSatisfactory)
        self.drawMenuData.signal_msn_informative.connect(self.showMessageStatusBarInformative)
        self.drawMenuData.signal_project_save_state.connect(self.__projectSaveState)

        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-MESH :::::::::::::::::
        self.drawMenuMesh.signal_paint_line.connect(self.__clickedToolButtonDrawPaintLine)
        self.drawMenuMesh.signal_paint_polyline.connect(self.__clickedToolButtonDrawPaintPolyline)
        self.drawMenuMesh.signal_paint_rectangle.connect(self.__clickedToolButtonDrawPaintRectangle)

        self.drawMenuMesh.signal_paint_move.connect(self.__clickedToolButtonDrawPaintMove)
        self.drawMenuMesh.signal_paint_rotate.connect(self.__clickedToolButtonDrawPaintRotate)
        self.drawMenuMesh.signal_paint_copy.connect(self.__clickedToolButtonDrawPaintCopy)
        self.drawMenuMesh.signal_paint_erase.connect(self.__clickedToolButtonDrawPaintErase)

        # ::::::::::::::::::::      EVENTOS FRAME DRAW     ::::::::::::::::::::
        self.toolButton_closeConsole.clicked.connect(self.__clickedToolButtonCloseConsole)


    ###############################################################################
    # ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
    ###############################################################################
    """ Métodos para los eventos de los botones y widget """
    def __clickedToolButtonCloseConsole(self):
        self.splitter.setSizes([1,0]) 

    def __clickedToolButtonDrawPaintLine(self):
        self.graphicsView_draw.isObject = 0
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        self.msnConsole("Command","_Line")
        self.msnLabelConsole("LINEA [Primer punto]: ")




    def __clickedToolButtonDrawPaintPolyline(self):
        self.graphicsView_draw.isObject = 1
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False

    def __clickedToolButtonDrawPaintRectangle(self):
        self.graphicsView_draw.isObject = 2
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False

    def __clickedToolButtonDrawPaintMove(self):
        pass

    def __clickedToolButtonDrawPaintRotate(self):
        if self.graphicsView_draw.isClear == False:
            self.graphicsView_draw.isClear = True
        else:
            self.graphicsView_draw.isClear = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.graphicsScene_draw.clear()
    def __clickedToolButtonDrawPaintCopy(self):
        if self.graphicsView_draw.isLine == False:
            self.graphicsView_draw.isLine = True
        else:
            self.graphicsView_draw.isLine = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
    def __clickedToolButtonDrawPaintErase(self):
        if self.graphicsView_draw.isDelate == False:
            self.graphicsView_draw.isDelate = True
        else:
            self.graphicsView_draw.isDelate = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isClear = False


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

    def __projectSaveState(self, there_are_changes):
        """Recibe la señal del estado del guardado del proyecto y remite la misma, señal a main window.

        Args:
            there_are_changes(bool): True >>> si se realizó cambios en el proyecto

        """
        self.signal_project_save_state.emit(there_are_changes)

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
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f94646;">Error:       </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)

        elif type_msn == "Warning":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#c8cc8e;">Warning:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Running":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#36c9c6;">Running:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Command":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f28123;">Command:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Information":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#999999;">information: </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        else:
            text_to_add = u'<a> <span>Command:</span><span> {} </span></a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        self.textBrowser_2.verticalScrollBar().maximum()


    def msnLabelConsole(self, msn):
        """Imprime mensaje en el label la consola.

        Args:

            msn(str): Mensaje a mostrar

        """ 
        self.label_console.setText(msn)
        self.label_console.setVisible(True)
        self.lineEdit_console.setFocus()



