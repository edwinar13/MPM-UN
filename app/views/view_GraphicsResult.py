"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : PointItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

#from cmath import rect
#from ctypes import pointer
#from ast import Return, type_ignore
#from re import X
from typing import Union
import weakref
from PySide6.QtCore import*
import PySide6.QtCore
from PySide6.QtGui import*
import PySide6.QtGui
from PySide6.QtWidgets import*

from utils.items_GraphicsResult import Node, Edge
from utils.items_GraphicsDraw import LineItem, PointItem, TextItem, RectItem, PointMeshBackItem


import math
import uuid
contador = 0 
import datetime



def random(boundary):
    return QRandomGenerator.global_().bounded(boundary)



class ViewGraphicsSceneResult(QGraphicsScene):
    def __init__(self):
        super().__init__()  
        #self.setSceneRect(QRectF(-20, -20, 40, 40))
    
    #rectangulo en el rect de la scena
    def drawBackground(self, painter: QPainter, rect: QRectF|QRect) -> None:
        painter.setPen(QPen(Qt.black, 1))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawRect(rect)
        return super(ViewGraphicsSceneResult, self).drawBackground(painter, rect)






class ViewGraphicsViewResult(QGraphicsView):
    signal_coor_mouse = Signal(list)
    def __init__(self):
        super().__init__()     
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.adjust_view_on_resize = False 
        self.adjust_view_on_show = 3 
        
        self.isModeColorBar = True
        self.gradient = QLinearGradient()

        self.scale(1, -1)
        self.setStyleView()

    def setStyleView(self, index=0):       
        """ Establece el estilo de la vista.
        
        args:
            index(int): index del estilo

        """

        if index == 0:
            # Crear un gradiente lineal vertical
            gradient = QLinearGradient(0, 0, 0, self.viewport().height())
            gradient.setColorAt(0, QColor("#ffffff"))
            gradient.setColorAt(1, QColor("#fafafa"))
        
        elif index == 1:
            gradient = QRadialGradient(self.viewport().width() / 4, self.viewport().height() / 2,
                                    self.viewport().width(), self.viewport().width() / 2, self.viewport().height() / 2)
            gradient.setColorAt(0, QColor("#DDDDDD"))
            gradient.setColorAt(1, QColor("#aaaaaa"))



        brush = QBrush(gradient)
        self.setBackgroundBrush(brush)
        self.setStyleSheet(f"border-radius: 8px; border: 2px solid #333;padding: 5px;")
        
    def resetView(self):
        '''
        rect = self.scene().itemsBoundingRect()
        self.resetTransform()
        self.setSceneRect(rect)
        self.fitInView(rect, Qt.KeepAspectRatio)
        self.scale(1, -1)
        '''
        self.adjust_view_on_resize = True
        self.adjust_view_on_show = 1
    
        self.updateView()
    

    def updateView(self):
        scene = self.scene()
        r = scene.sceneRect()
        self.fitInView(r, Qt.KeepAspectRatio)

    def resizeEvent(self, event):  
        if self.adjust_view_on_resize <=3:
            self.updateView()
            self.adjust_view_on_resize +=1
        else:
            factor = 1.25
            self.scale(factor, factor)  
            factor = 0.8
            self.scale(factor, factor)  

    def showEvent(self, event):
        if not event.spontaneous():            
            if self.adjust_view_on_show:
                self.updateView()
            self.adjust_view_on_show = False




    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	############################################################################### 
    
    def wheelEvent(self, event):
        #Zoom max
        if self.transform().m11() <0.005 and event.angleDelta().y() < 0:
            return
        #Zoom min
        if self.transform().m11()>250000 and event.angleDelta().y() > 0:
            return
        if event.angleDelta().y() > 0:
            factor = 1.25
        else:
            factor = 0.8
        self.isModeCrosshairPickbox = False
        self.scale(factor, factor)        
        self.isModeCrosshairPickbox = True

        # para actulizar cursor al realizar zoom
        point_view = event.position()
        point_view = QPoint(int(point_view.x()),int(point_view.y()))
        self.point_scene = self.mapToScene(point_view) 
        self.signal_coor_mouse.emit([self.point_scene.x(),self.point_scene.y()])
        
        self.scene().update()

    def mousePressEvent(self, event: QMouseEvent) -> None:
            
        #mover la escena
        if event.button() == Qt.MiddleButton:

            self.scene().isPan = True
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            #self.viewport().setCursor(Qt.ClosedHandCursor)
            self.original_event = event
            handmade_event = QMouseEvent(
                QEvent.MouseButtonPress,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifiers(),
            )
            QGraphicsView.mousePressEvent(self, handmade_event)
            self.scene().isPan = False

        super(ViewGraphicsViewResult, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Evento al mover el ratón, se emite una señal con
        las coordenadas de ratón  para ser mostradas en statusBar
        """
        # Emite señal para mostrar coordenada
        point_view = event.pos()
        self.point_scene = self.mapToScene(point_view) 
        self.signal_coor_mouse.emit([self.point_scene.x(),self.point_scene.y()])

        self.scene().update()
        super(ViewGraphicsViewResult, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:      
        if event.button() == Qt.MiddleButton:
            self.setDragMode(QGraphicsView.NoDrag)
            #self.viewport().setCursor(Qt.BlankCursor)
        
  

        super(ViewGraphicsViewResult, self).mouseReleaseEvent(event)



class GraphWidget(QGraphicsView):
    def __init__(self):
        super().__init__()

        self._timer_id = 0

        scene = QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(-200, -200, 400, 400)
        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        node1 = Node(self)
        node2 = Node(self)
        node3 = Node(self)
        node4 = Node(self)
        self._center_node = Node(self)
        node6 = Node(self)
        node7 = Node(self)
        node8 = Node(self)
        node9 = Node(self)
        scene.addItem(node1)
        scene.addItem(node2)
        scene.addItem(node3)
        scene.addItem(node4)
        scene.addItem(self._center_node)
        scene.addItem(node6)
        scene.addItem(node7)
        scene.addItem(node8)
        scene.addItem(node9)
        scene.addItem(Edge(node1, node2))
        scene.addItem(Edge(node2, node3))
        scene.addItem(Edge(node2, self._center_node))
        scene.addItem(Edge(node3, node6))
        scene.addItem(Edge(node4, node1))
        scene.addItem(Edge(node4, self._center_node))
        scene.addItem(Edge(self._center_node, node6))
        scene.addItem(Edge(self._center_node, node8))
        scene.addItem(Edge(node6, node9))
        scene.addItem(Edge(node7, node4))
        scene.addItem(Edge(node8, node7))
        scene.addItem(Edge(node9, node8))

        node1.setPos(-50, -50)
        node2.setPos(0, -50)
        node3.setPos(50, -50)
        node4.setPos(-50, 0)
        self._center_node.setPos(0, 0)
        node6.setPos(50, 0)
        node7.setPos(-50, 50)
        node8.setPos(0, 50)
        node9.setPos(50, 50)

        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        self.setWindowTitle(self.tr("Elastic Nodes"))

    def item_moved(self):
        if not self._timer_id:
            self._timer_id = self.startTimer(1000 / 25)

    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Up:
            self._center_node.moveBy(0, -20)
        elif key == Qt.Key_Down:
            self._center_node.moveBy(0, 20)
        elif key == Qt.Key_Left:
            self._center_node.moveBy(-20, 0)
        elif key == Qt.Key_Right:
            self._center_node.moveBy(20, 0)
        elif key == Qt.Key_Plus:
            self.scale_view(1.2)
        elif key == Qt.Key_Minus:
            self.scale_view(1 / 1.2)
        elif key == Qt.Key_Space or key == Qt.Key_Enter:
            for item in self.scene().items():
                if isinstance(item, Node):
                    item.setPos(-150 + random(300), -150 + random(300))
        else:
            QGraphicsView.keyPressEvent(self, event)

    def timerEvent(self, event):
        nodes = [item for item in self.scene().items() if isinstance(item, Node)]

        for node in nodes:
            node.calculate_forces()

        items_moved = False
        for node in nodes:
            if node.advance():
                items_moved = True

        if not items_moved:
            self.killTimer(self._timer_id)
            self._timer_id = 0

    def wheelEvent(self, event):
        delta = event.angleDelta().y()
        self.scale_view(math.pow(2.0, -delta / 240.0))

    def draw_background(self, painter, rect):
        # Shadow.
        scene_rect = self.sceneRect()
        right_shadow = QRectF(scene_rect.right(), scene_rect.top() + 5,
                              5, scene_rect.height())
        bottom_shadow = QRectF(scene_rect.left() + 5, scene_rect.bottom(),
                               scene_rect.width(), 5)
        if right_shadow.intersects(rect) or right_shadow.contains(rect):
                painter.fillRect(right_shadow, Qt.darkGray)
        if bottom_shadow.intersects(rect) or bottom_shadow.contains(rect):
                painter.fillRect(bottom_shadow, Qt.darkGray)

        # Fill.
        gradient = QLinearGradient(scene_rect.topLeft(), scene_rect.bottomRight())
        gradient.setColorAt(0, Qt.white)
        gradient.setColorAt(1, Qt.lightGray)
        painter.fillRect(rect.intersected(scene_rect), QBrush(gradient))
        painter.setBrush(Qt.NoBrush)
        painter.drawRect(scene_rect)

        # Text.
        text_rect = QRectF(scene_rect.left() + 4, scene_rect.top() + 4,
                                 scene_rect.width() - 4, scene_rect.height() - 4)
        message = self.tr("Click and drag the nodes around, and zoom with the "
                          "mouse wheel or the '+' and '-' keys")

        font = painter.font()
        font.setBold(True)
        font.setPointSize(14)
        painter.setFont(font)
        painter.setPen(Qt.lightGray)
        painter.drawText(text_rect.translated(2, 2), message)
        painter.setPen(Qt.black)
        painter.drawText(text_rect, message)

    def scale_view(self, scaleFactor):
        factor = self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()

        if factor < 0.07 or factor > 100:
            return

        self.scale(scaleFactor, scaleFactor)






# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►


class ViewGraphicsViewResult000 (QGraphicsView):
    signal_coor_mouse = Signal(list)
    signal_main_view = Signal(str)
    signal_end_draw_geometry = Signal()
    


    def __init__(self):
        super(ViewGraphicsViewResult, self).__init__() 

        #self.setCursor(Qt.BlankCursor)
        #print(self.cursor())
        
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)   # este se ve mejor las lineas probar    
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse) # este realiza zoom en el mause solo cuando hay barras de dezplazamiento
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate )


        #self.setMouseTracking(True) 
                
        # ajusta el eje vertical como positivo arriba
        self.scale(1, -1)

        #obtiene la pantalla principal y su tamaño
        self.screen_primary = QApplication.primaryScreen()
        self.screen_height = self.screen_primary.size().height()
        self.screen_width = self.screen_primary.size().width()
        self.isMainView = False

        #Atributos
        self.point_scene = None
        self.isModeOrigin = True
        self.isModeAxis = True
        self.isModeGrid = True
        self.isModeCrosshairPickbox = True
        self.isModeCrosshair = False
        self.isModePickbox= False


        self.isZoomWindow = False
        self.p1_zoom_window = None
        self.p2_zoom_window = None


        self.crosshair_size = 1.0
        self.pick_box_size = 0.005
        self.grid_adaptative = False
        self.grid_spacing = 50

        # pluma para grilla, eje y eje x
        self.pen_grid_x = QPen()        
        self.pen_grid_x.setWidth(0)
        self.pen_axis_y = QPen()
        self.pen_axis_y.setWidth(0)
        self.pen_axis_x = QPen()
        self.pen_axis_x.setWidth(0)

        # plumas para pick_box, crosshair y mode_crosshair
        self.pen_pick_box = QPen()
        self.pen_pick_box.setWidth(0)
        self.pen_crosshair = QPen()
        self.pen_crosshair.setWidth(0)
        self.pen_crosshair_draw = QPen()
        self.pen_crosshair_draw.setWidth(0)

        # Para mover la escena
        self.start_pos = None

    ###############################################################################
	# :::::::::::::::::::::          OTROS MÉTODOS           ::::::::::::::::::::::
	############################################################################### 
    def setStyleView(self, index):       
        """ Establece el estilo de la vista.
        
        args:
            index(int): index del estilo

        """

        if index == 0:
            color_background = "#ffffff"
            self.color_grid="#EEEEEE"
            self.color_axis_x="#B18284"
            self.color_axis_y="#A9CE92"
            self.color_crosshair_draw="#000000"
            self.color_crosshair="#888888"
            self.color_pick_box ="#888888"
            
        elif index == 1:
            color_background = "#333333"    
            self.color_grid="#3f3f3f"
            self.color_axis_x="#742427"
            self.color_axis_y="#6A6C48"
            self.color_crosshair_draw="#FFFFFF"
            self.color_crosshair="#AAAAAA"
            self.color_pick_box ="#AAAAAA"

        elif index == None:
            color_background = "#888888"
            self.color_grid="#777777"
            self.color_axis_x="#742427"
            self.color_axis_y="#C8CC8E"
            self.color_crosshair_draw="#000000"
            self.color_crosshair="#555555"
            self.color_pick_box ="#555555"

        self.setStyleSheet("background-color: {} ;border: 2px solid #444444;".format(color_background))
        self.pen_grid_x.setColor(QColor(self.color_grid))
        self.pen_axis_y.setColor(QColor(self.color_axis_y))
        self.pen_axis_x.setColor(QColor(self.color_axis_x))
        self.pen_crosshair_draw.setColor(QColor(self.color_crosshair_draw))
        self.pen_crosshair.setColor(self.color_crosshair)
        self.pen_pick_box.setColor(self.color_pick_box)
    
    def reset_view(self):
        """Reinicia la vista, colocando el rectángulo de la escena al tamaño de la vista scale=1."""
        rect = self.scene().itemsBoundingRect()
        self.resetTransform()
        self.setSceneRect(rect)
        self.fitInView(rect, Qt.KeepAspectRatio)
        self.scale(1, -1)

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	############################################################################### 
    
    def wheelEvent(self, event):


        #Zoom max
        if self.transform().m11() <0.005 and event.angleDelta().y() < 0:
            return
        #Zoom min
        if self.transform().m11()>250000 and event.angleDelta().y() > 0:
            return

        if event.angleDelta().y() > 0:
            factor = 1.25
        else:
            factor = 0.8
        self.isModeCrosshairPickbox = False
        self.scale(factor, factor)
        self.isModeCrosshairPickbox = True

        # para actulizar cursor al realizar zoom
        point_view = event.position()
        point_view = QPoint(int(point_view.x()),int(point_view.y()))
        self.point_scene = self.mapToScene(point_view) 
        self.signal_coor_mouse.emit([self.point_scene.x(),self.point_scene.y()])
        
        self.scene().update()
       
    def mousePressEvent(self, event: QMouseEvent) -> None:

        if event.button() == Qt.LeftButton and self.isZoomWindow:
            self.setDragMode(self.RubberBandDrag)
            self.p1_zoom_window = event.pos()
            
        #mover la escena
        elif event.button() == Qt.MiddleButton:

            self.scene().isPan = True
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            self.viewport().setCursor(Qt.ClosedHandCursor)
            self.original_event = event
            handmade_event = QMouseEvent(
                QEvent.MouseButtonPress,
                QPointF(event.pos()),
                Qt.LeftButton,
                event.buttons(),
                Qt.KeyboardModifiers(),
            )
            QGraphicsView.mousePressEvent(self, handmade_event)
            self.scene().isPan = False

        super(ViewGraphicsViewResult, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Evento al mover el ratón, se emite una señal con
        las coordenadas de ratón  para ser mostradas en statusBar
        """
        # Emite señal para mostrar coordenada
        point_view = event.pos()
        self.point_scene = self.mapToScene(point_view) 
        self.signal_coor_mouse.emit([self.point_scene.x(),self.point_scene.y()])

        #Emite la señal para seleccionar view como principal
        self.signal_main_view.emit(self.objectName())
        self.scene().update()
        super(ViewGraphicsViewResult, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        #mover la escena
        if event.button() == Qt.LeftButton and self.isZoomWindow:            
            self.zoomWindow(False)

            # aca realiza el zoom
            self.p2_zoom_window = event.pos()
            delta = self.p1_zoom_window - self.p2_zoom_window 
            try:
                scale_w = self.rect().width()/ abs(delta.x())
                scale_h = self.rect().height() /abs(delta.y())
            except ZeroDivisionError:
                return
            center = (self.p1_zoom_window + self.p2_zoom_window) /2
            center =self.mapToScene(center)

            if scale_w <= scale_h:
                self.scale(scale_w,scale_w) 
            else:                
                self.scale(scale_h,scale_h) 

            self.centerOn(center)

            self.signal_end_draw_geometry.emit()
            

        if event.button() == Qt.MiddleButton:
            self.setDragMode(QGraphicsView.NoDrag)
            self.viewport().setCursor(Qt.BlankCursor)

  

        super(ViewGraphicsViewResult, self).mouseReleaseEvent(event)

    def drawBackground(self, painter: QPainter, rect: QRectF|QRect) -> None:
        
        if self.isModeAxis == True or self.isModeGrid == True:
            scale_view = self.transform().m11()

            if self.grid_adaptative == True:

                spacing_temp = 50/(scale_view)
                #ajusta a la escala los espacios de la grilla
                if spacing_temp < 0.001:
                    self.grid_spacing = 0.001
                elif spacing_temp < 0.01:
                    self.grid_spacing = round(spacing_temp,3)
                elif spacing_temp < 0.1:
                    self.grid_spacing = round(spacing_temp,2)
                elif spacing_temp < 1:
                    self.grid_spacing = round(spacing_temp,1)
                elif spacing_temp < 10:
                    self.grid_spacing = int(spacing_temp)
                elif spacing_temp < 100:
                    self.grid_spacing = 10*(int((spacing_temp/10)))
                elif spacing_temp < 1000:
                    self.grid_spacing = 100*(int((spacing_temp/100)))
                elif spacing_temp < 10000:
                    self.grid_spacing = 1000*(int((spacing_temp/1000)))
                else:
                    self.grid_spacing = 10000
                grid_spacing = self.grid_spacing
            else:
                grid_spacing = self.grid_spacing
            
            if  self.isMainView == True:
                self.scene().grid_spacing = self.grid_spacing
                #print(self.objectName(),grid_spacing ,self.hasFocus(),self.transform())
                
                


            isShow = True
            if int((rect.bottom()-rect.top())/grid_spacing) > 100:
                isShow = False
           
            painter.save()
            if  self.isModeGrid == True and isShow:

                painter.setPen(self.pen_grid_x)

                # lineas grilla horizontal > positivo 
                if rect.bottom() >0:
                    lines_axis_x_bottom = (int(abs(rect.bottom() / grid_spacing )))+1                    
                    for i  in range(lines_axis_x_bottom):
                        yi = (i) * grid_spacing
                        if rect.top()<yi:
                            linex_positive = QLineF(rect.left(), yi,
                                        rect.right(), yi)
                            painter.drawLine(linex_positive)

                # lineas grilla horizontal > negativo
                if rect.top()< 0:
                    lines_axis_x_top = (int(abs(rect.top() / grid_spacing )))+1
                    for i  in range(lines_axis_x_top):
                        yi= -((i) * (grid_spacing))
                        if rect.bottom()>yi:
                            linex_negative = QLineF(rect.left(), yi,
                                        rect.right(), yi)
                            painter.drawLine(linex_negative)


                # lineas grilla vertical > positivo
                if rect.right() > 0:
                    lines_axis_y_right = (int(abs(rect.right() / grid_spacing )))+1
                    for i  in range(lines_axis_y_right):
                        xi = (i) * grid_spacing
                        if rect.left()<xi:
                            linex_positive = QLineF(xi, rect.top(),
                                        xi, rect.bottom())
                            painter.drawLine(linex_positive)
 
                # lineas grilla vertical > negativo
                if rect.left()<0:
                    lines_axis_y_left = (int(abs(rect.left() / grid_spacing )))+1
                    for i  in range(lines_axis_y_left):
                        xi = -((i) * (grid_spacing))
                        if rect.right()>xi:
                            linex_negative = QLineF( xi, rect.top(),
                                        xi, rect.bottom())
                            painter.drawLine(linex_negative)

            if self.isModeAxis == True :

                # eje Y
                painter.setPen(self.pen_axis_y)
                liney = QLineF(0,rect.top(),0,rect.bottom(),)
                painter.drawLine(liney)

                # eje X
                painter.setPen(self.pen_axis_x)
                linex = QLineF(rect.left(),0,rect.right(),0,)
                painter.drawLine(linex)
            painter.restore()
        
        return super(ViewGraphicsViewResult, self).drawBackground(painter, rect)

    def drawForeground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        """ Evento para dibujar en el primer plano, se dibuja las fechas
        del origen, punta de mira y la caja de selección que sigue al ratón """
        scale_view = self.transform().m11()

        if  self.isMainView == True:
            x_scene = (self.rect().x()) 
            y_scene = (self.rect().y()) 
            w_scene = (self.rect().width())-4 # no se ha podido identificar por que se requiere
            h_scene = (self.rect().height())-4

            rect_scene = self.mapToScene(QRect(x_scene,y_scene,w_scene,h_scene)) 
            painter.save()  
            scale_Width = 2 * (1/scale_view)
            pen = QPen(QColor(254,233,183,255))                
            pen.setWidthF(scale_Width)
            painter.setPen(pen)
            painter.drawPolygon(rect_scene)
            painter.restore()            

        
        if  self.isModeOrigin == True and self.isMainView == True:
            point_view = QPoint(self.rect().x(),self.rect().height()-3)  
            point_scene = self.mapToScene(point_view) 
            painter.save()             
            xo=point_scene.x()
            yo=point_scene.y()
            scale_arrow = 2.1 * (1/scale_view)

            #Origen Y
            pen = QPen(QColor("#C8CC8E"))
            pen.setWidth(0)
            brush = QBrush(Qt.SolidPattern)
            brush.setColor(QColor("#C8CC8E"))
            painter.setBrush(brush)
            painter.setPen(pen)

            coord_arrow_y=[
            [xo + (4.5 * scale_arrow)  , yo + ( 5.5 * scale_arrow)],
            [xo + (6.5 * scale_arrow)  , yo + ( 5.5 * scale_arrow)],
            [xo + (6.5 * scale_arrow)  , yo + (19.5 * scale_arrow)],
            [xo + (9.0 * scale_arrow)  , yo + (19.5 * scale_arrow)],
            [xo + (5.5 * scale_arrow)  , yo + (25.5 * scale_arrow)],
            [xo + (2.0 * scale_arrow)  , yo + (19.5 * scale_arrow)],
            [xo + (4.5 * scale_arrow)  , yo + (19.5 * scale_arrow)]]                

            arrow_y = QPolygonF()
            for i in coord_arrow_y:
                arrow_y.append(QPointF(i[0], i[1]))
            painter.drawPolygon(arrow_y)

            #Origen X
            pen = QPen(QColor("#742427"))
            pen.setWidth(0)
            brush = QBrush(Qt.SolidPattern)
            brush.setColor(QColor("#742427"))
            painter.setBrush(brush)
            painter.setPen(pen)

            coord_arrow_x=[
            [xo + ( 5.5 * scale_arrow), yo + (6.5 * scale_arrow)],
            [xo + ( 5.5 * scale_arrow), yo + (4.5 * scale_arrow)],
            [xo + (19.5 * scale_arrow), yo + (4.5 * scale_arrow)],
            [xo + (19.5 * scale_arrow), yo + (2.0 * scale_arrow)],
            [xo + (25.5 * scale_arrow), yo + (5.5 * scale_arrow)],
            [xo + (19.5 * scale_arrow), yo + (9.0 * scale_arrow)],
            [xo + (19.5 * scale_arrow), yo + (6.5 * scale_arrow)]]           

            arrow_x = QPolygonF()
            for i in coord_arrow_x:
                arrow_x.append(QPointF(i[0], i[1]))
            painter.drawPolygon(arrow_x)

            pen = QPen(QColor("#aaaaaa"))                
            pen.setWidth(0)
            painter.setPen(pen)
            brush= QBrush(Qt.SolidPattern)
            brush.setColor(QColor("#bbbbbb"))
            painter.setBrush(brush)

            painter.drawEllipse(QPointF(xo + (5.5*scale_arrow),yo + (5.5*scale_arrow)), 2*scale_arrow, 2*scale_arrow)

            painter.restore()
        
        if self.isModeCrosshairPickbox == True and self.isMainView == True :
            #self.viewport().setCursor(Qt.BlankCursor)
            point_scene = self.point_scene

            if point_scene == None:
                return
            cursor_x = point_scene.x()
            cursor_y = point_scene.y()
            painter.save()

            #:::::::::::::::::  pick_box   :::::::::::::::::
            painter.setPen(self.pen_pick_box)

            # se establece el porcentaje min y max del tamaño de pick_box
            pick_box_size = self.pick_box_size      
            if pick_box_size < 5:
                pick_box_size = 5
            elif pick_box_size > 50:
                pick_box_size = 50

            if self.isModeCrosshair :
                pick_box_size_min = 0                
            else:
                pick_box_size_min = pick_box_size * (1/scale_view)

            rectangle = QRectF(cursor_x - (pick_box_size_min / 2),
                            cursor_y - (pick_box_size_min / 2),
                            pick_box_size_min,
                            pick_box_size_min)
            if not self.isModeCrosshair:            
                painter.drawRect(rectangle)

            self.scene().rect_pick_box = rectangle

            #:::::::::::::::::  crosshair   :::::::::::::::::
            if self.isModeCrosshair :
                painter.setPen(self.pen_crosshair_draw)      
            else:
                painter.setPen(self.pen_crosshair)
            
            crosshair_size = self.crosshair_size
            if crosshair_size >=1.0:
                crosshair_size = 2.0

            crosshair_size_max = crosshair_size * (self.screen_width/2)* (1/(scale_view))

            crosshair_size_left = cursor_x + crosshair_size_max
            crosshair_size_right = cursor_x - crosshair_size_max
            crosshair_size_top = cursor_y + crosshair_size_max
            crosshair_size_botton = cursor_y - crosshair_size_max

            linex_left = QLineF(crosshair_size_left,
                            cursor_y,
                            cursor_x+(pick_box_size_min/2),
                            cursor_y)
            
            linex_right = QLineF(cursor_x-(pick_box_size_min/2),
                            cursor_y,
                            crosshair_size_right,
                            cursor_y)

            liney_top = QLineF(cursor_x,
                            crosshair_size_top,
                            cursor_x,
                            cursor_y+(pick_box_size_min/2))

            liney_botton = QLineF(cursor_x,
                            cursor_y-(pick_box_size_min/2),
                            cursor_x,
                            crosshair_size_botton)
            if not self.isModePickbox:
                for line in (linex_left,linex_right,liney_top,liney_botton):
                    painter.drawLine(line)

            painter.restore()
        
        super(ViewGraphicsViewResult, self).drawForeground(painter, rect)

    def zoomWindow(self, state):
        if state == True:
            self.isZoomWindow = True  
            self.viewport().setCursor(Qt.UpArrowCursor)
            self.isModeCrosshairPickbox = False 
        else:
            
            self.setDragMode(QGraphicsView.NoDrag)
            self.isZoomWindow = False  
            self.viewport().setCursor(Qt.BlankCursor)
            self.isModeCrosshairPickbox = True
            self.update()

    def selectElement(self, state):
        
        if state == True:            
            self.isModePickbox = True
            #self.setDragMode(self.RubberBandDrag)
        else:
            self.isModePickbox = False
            #self.setDragMode(self.NoDrag)


    def endDrawGeometry(self):        
        self.zoomWindow(False)
        self.selectElement(False)
        self.update()
        
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►


class ViewGraphicsSceneResult000 (QGraphicsScene): 
    signal_next_point = Signal(int)


    signal_point_point = Signal(dict)
    signal_point_line = Signal(dict)
    signal_point_move = Signal(dict)
    signal_point_copy = Signal(dict)
    signal_point_rotate = Signal(dict)
    signal_point_erase = Signal(dict)
    signal_point_intersection = Signal(dict)
    signal_point_rule = Signal(dict)

    signal_mesh_select = Signal(dict)
    signal_point_back_select = Signal(dict)
    signal_mesh_size = Signal(dict)
          


    def __init__(self):
        super(ViewGraphicsSceneResult, self).__init__()
        # Atributos
        self.grid_spacing = 50
        

        #Atributos para ayudas de dibujo
        self.mode_ortho = False
        self.mode_osnap  = False
        self.rect_pick_box = None
        self.mode_snap_grid = False
        self.snap_grid_adaptative  = False
        self.snap_grid_spacing = 10
        
        #Atributos para dibujo
        self.isDrawGeometry = False


        self.isDrawLine = False
        self.isDrawRectangle = False
        self.isDrawPoint = False
        self.isDrawPolyline = False  
        self.isDrawMove = False          
        self.isDrawCopy = False
        self.isDrawRotate = False
        self.isDrawErase = False
        self.isDrawIntersection = False
        self.isDrawRule = False
        self.isDrawSelect = False          

  

        self.isPointBackSelect = False   
        self.isMeshSelect = False   
        self.isMeshCua = False   
        self.isMeshSize = False   




        self.p1_select = None
        self.p2_select = None
        self.selected_items = []
        self.selected_items_line = []


        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None
        self.point_init = None
        self.vertex = 0
        
        #self.isSelect = False 

        self.isPan = False
        self.theme = 0
        self.drawElementTemp()

    def setAdmin(self,admin):
        self.admin = admin

    ###############################################################################
	# :::::::::::::::::::::          OTROS MÉTODOS           ::::::::::::::::::::::
	############################################################################### 

    def getPointVertex(self):
        return self.point_vertex
    
    def setPointVertex(self, point):
        self.point_vertex = point

        

    def getPointVertexAnt(self):
        return self.point_vertex_ant
    
    def setPointVertexAnt(self, point):
        self.point_vertex_ant = point
    
    def getSelectedItems(self):
        return self.selected_items

    def addSelectedItems(self,item):
         self.selected_items.append(item)

    def removeSelectedItems(self,item):
         self.selected_items.remove(item)


    def drawElementTemp(self):
        #elementos temporales
        text = TextItem("temp", 0,0)
        self.addItem(text)
        self.point_temp = PointItem(0,"pointTemp",0,0,text)          
        self.addItem(self.point_temp)
        self.point_temp.color= QColor("#36C9C6")
        self.point_temp.setVisible(False)
        
        self.line_temp = QGraphicsLineItem(QLineF(0,0,0,0)) 
        self.addItem(self.line_temp)
        self.line_temp.setVisible(False)
        self.color_element_temp="#555555"
        self.line_temp.setPen(QPen(QColor(self.color_element_temp),0,Qt.DashLine, Qt.RoundCap, Qt.RoundJoin))

        self.rectangle_temp = QGraphicsRectItem(QRectF(0,0,0,0))                
        self.rectangle_temp.setPen(QPen(QColor(self.color_element_temp),0,Qt.DashLine, Qt.RoundCap, Qt.RoundJoin))
        self.addItem(self.rectangle_temp)
        self.rectangle_temp.setVisible(False)

        self.color_select_mode1 = QColor("#96be25")
        self.color_select_mode1.setAlphaF(0.2)
        self.color_select_mode2 = QColor("#2596be")
        self.color_select_mode2.setAlphaF(0.2)

        self.rect_select_temp = RectItem("rectTemp",QPoint(0,0),QPoint(0,0))                
        self.rect_select_temp.setPen(QPen(QColor(self.color_element_temp),0,Qt.DashDotDotLine, Qt.RoundCap, Qt.RoundJoin))
        self.rect_select_temp.setBrush(self.color_select_mode1)
        self.addItem(self.rect_select_temp)
        self.rect_select_temp.setVisible(False)
        '''
        self.text_temp = QGraphicsTextItem("Mesh")
        #self.text_temp = QGraphicsSimpleTextItem("quesote")
        #self.text_temp.setPlainText("edwin")
        self.text_temp.setPos(QPointF(0,0))
        self.addItem(self.text_temp)
        self.text_temp.setVisible(False)
        '''



    def setStyleScene(self, index):    
        """Establece el estilo de la escena.

        args:
            index(int): index del estilo

        """  
        self.theme =index

    def getTheme(self ):  
        return self.theme

    def setUndoStackToAdmin(self, undo_stack ):
        self.admin.setUndoStack(undo_stack)

    def redo(self):
        self.admin.redo()
        #print(self.admin.getActions())

    def undo(self):
        self.admin.undo()
        
    
    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	############################################################################### 

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None: 
        self.text_temp.setVisible(False)

        if event.button() == Qt.LeftButton and not self.isPan:        

            #::::::::::::  punto  ::::::::::::::::
            if self.isDrawPoint: 
                self.signal_point_point.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
            
            elif self.isDrawLine: 
                if self.point_vertex_ant == None:
                    self.signal_point_line.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
                else:
                    self.signal_point_line.emit(
                        {"step":3,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

            elif self.isDrawSelect or self.isMeshSelect or self.isPointBackSelect: 
                self.p1_select = event.scenePos()
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.p1_select))
                self.rect_select_temp.setVisible(True)

            #::::::::::::  mover  ::::::::::::::::    
            elif self.isDrawMove and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_move.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:                    
                    self.signal_point_move.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  copiar  ::::::::::::::::    
            elif self.isDrawCopy and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_copy.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:                    
                    self.signal_point_copy.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  malla  ::::::::::::::::    
            elif self.isMeshCua and not self.isMeshSelect:

                if self.point_vertex_ant == None:
                    return
                    self.signal_point_copy.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:         
                    return
                    self.signal_point_copy.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  rotar  ::::::::::::::::    
            elif self.isDrawRotate and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_rotate.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:      
                    
                    point = self.point_vertex
                    point_ref = self.point_vertex_ant
                    dx = point.x() - point_ref.x()
                    dy = point.y() - point_ref.y()
                    angle_ref = math.degrees(math.atan2(dy, dx))
                    if angle_ref < 0:
                        angle_ref = 360 + angle_ref


                    self.signal_point_rotate.emit(
                        {"step":5,
                        "data":
                            [[point_ref.x(),point_ref.y()],
                            angle_ref]
                        })
                    
            elif self.isDrawRule: 
                
                if self.point_vertex_ant == None:
                    self.signal_point_rule.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
                else:
                    self.signal_point_rule.emit(
                        {"step":3,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

            elif self.isMeshSize: 

                if self.point_vertex_ant != None:
                    self.signal_mesh_size.emit(
                        {"step":2,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

    

        super(ViewGraphicsSceneResult, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        self.point_vertex = event.scenePos()    
        #print(type(self.text_temp))    
        self.text_temp.setPos(self.point_vertex)
        # MODO OSNAP 
        if self.mode_osnap:        
            point_osnap = self.pointInCursor(self.point_vertex,self.rect_pick_box)
            
            if point_osnap != None:
                self.point_vertex = point_osnap.pos()
                point_osnap.draw_rect_osnap = True

        # MODO SNAP GRID
        if self.mode_snap_grid:
            if self.snap_grid_adaptative == True:
                spacing = self.grid_spacing
            else:
                spacing = self.snap_grid_spacing
            self.point_vertex = self.pointSnapGrid(spacing, self.point_vertex)

        # MODO ORTHO 
        if self.mode_ortho == True and self.point_vertex_ant != None and not self.isDrawRectangle:
            point_a = self.point_vertex_ant
            point_b = self.point_vertex
            delta_cursor = point_b - point_a
            try:
                validator = delta_cursor.x()/delta_cursor.y()
            except ZeroDivisionError:
                validator=100

            if -1 <= validator <= 1:
                point_b.setX(point_a.x())
            else:
                point_b.setY(point_a.y())
            self.point_vertex = point_b
        
        #::::::::::::  mover, copiar, rotar, borrar  ::::::::::::::::
        if self.isDrawSelect or self.isMeshSelect or self.isPointBackSelect:
            
            #self.drawGeneral(self.point_vertex,self.point_vertex_ant)
            if self.p1_select != None:
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.point_vertex))
                x1 = self.p1_select.x()
                x2 = self.point_vertex.x()
                if x1 > x2:
                    self.rect_select_temp.setBrush(self.color_select_mode1)
                else:
                    self.rect_select_temp.setBrush(self.color_select_mode2)
            return            

        
        #::::::::::::  move, copiar , rotar ::::::::::::::::
        if self.isDrawMove or self.isDrawCopy or self.isDrawRotate:   
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  punto  ::::::::::::::::
        elif self.isDrawPoint :  
            self.drawGeneral(self.point_vertex)

            
        #::::::::::::  Linea  ::::::::::::::::
        elif self.isDrawLine:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)
        
        #::::::::::::  Rectangulo  ::::::::::::::::
        elif self.isDrawRectangle:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  regla  ::::::::::::::::
        elif self.isDrawRule:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  mesh  ::::::::::::::::
        elif self.isMeshSize:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        super(ViewGraphicsSceneResult, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:  
        self.text_temp.setVisible(False)
        self.p2_select = event.scenePos()
        if event.button() == Qt.LeftButton and not self.isPan:               
            #::::::::::::  mover  ::::::::::::::::
            if  self.isDrawSelect and self.isDrawMove and self.p1_select != None:
                self.signal_point_move.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
        
            #::::::::::::  copiar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawCopy and self.p1_select != None:
                self.signal_point_copy.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
            

            #::::::::::::  rotar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawRotate and self.p1_select != None:
                self.signal_point_rotate.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                
            #::::::::::::  borrar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawErase and self.p1_select != None:
                self.signal_point_erase.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                
            #::::::::::::  malla ::::::::::::::::
            elif  self.isMeshSelect and self.isMeshCua and self.p1_select != None:    
                self.signal_mesh_select.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                
            #::::::::::::  malla back point ::::::::::::::::
            elif  self.isPointBackSelect and self.p1_select != None:    
                self.signal_point_back_select.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                


            #::::::::::::  interseccion ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawIntersection and self.p1_select != None:
                self.signal_point_intersection.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )


            self.rect_select_temp.setRect(0,0,0,0)
            self.rect_select_temp.setVisible(False)
            self.p1_select = None
            self.p2_select = None

                 
        super(ViewGraphicsSceneResult, self).mouseReleaseEvent(event)

    def drawBackground(self, painter: QPainter, rect: QRectF| QRect) -> None:

        pen = QPen()
        pen.setWidth(0)
        pen.setColor("#56fdb6")
        pen.setStyle(Qt.DashLine)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(255, 255, 255, 50))        
        painter.save()
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawRect(self.sceneRect())
        painter.restore()
        
        super(ViewGraphicsSceneResult, self).drawBackground(painter, rect)

    def drawForeground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        """ Evento para dibujar en el primer plano, se dibuja las fechas
        del origen, punta de mira y la caja de selección que sigue al ratón """
        super(ViewGraphicsSceneResult, self).drawForeground(painter, rect)
    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS PARA DIBUJO     ::::::::::::::::::::
	############################################################################### 
    def endDrawGeometry(self):
        self.isDrawPoint = False
        self.isDrawLine = False
        self.isDrawPolyline = False
        self.isDrawRectangle = False
        self.isDrawErase = False
        self.isDrawSelect = False          
        self.isDrawRotate = False
        self.isDrawCopy = False
        self.isDrawMove = False
        self.isDrawRule = False

        self.isPointBackSelect = False
        self.isMeshSelect = False
        self.isMeshCua = False
        self.isMeshSize = False


        self.point_temp.setVisible(False)
        self.line_temp.setVisible(False)
        self.rectangle_temp.setVisible(False)
        self.rect_select_temp.setVisible(False)    
        self.p1_select = None
        self.p2_select = None
        for item in self.selected_items:
            item.isSelectedDraw = False
            if isinstance(item, PointMeshBackItem):
                item.isSelectedPointBlack = False

        for  line in self.selected_items_line:
            line.isSelectedDraw = False
            line.isSelectedMesh = False

            line.isSelectedPointBlack = False
        
        
            
        self.selected_items = []
        self.selected_items_line = []
        
        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None

        if self.vertex == 1 and self.point_init != None:
            self.removeItem(self.point_init)
        self.point_init = None
        self.vertex = 0
        self.update()

    def drawGeneral(self, p1=None, p2=None):  
        if p1 == None:
            return

        elif self.isDrawPoint:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)

        elif self.isDrawLine or self.isDrawMove or self.isDrawCopy or self.isDrawRotate or self.isDrawRule or self.isMeshSize:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.line_temp.setVisible(True)
                self.line_temp.setLine(QLineF(p1,p2)) 

        elif self.isDrawRectangle:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.rectangle_temp.setVisible(True)
                self.rectangle_temp.setRect(QRectF(p1,p2)) 

  
    def pointSnapGrid(self, spacing, point_base):

        piX = (point_base.x()//spacing)*spacing
        piY = (point_base.y()//spacing)*spacing
        pfX = piX + spacing
        pfY = piY + spacing

        point_snap_1 = QPointF(piX,piY)
        point_snap_2 = QPointF(piX,pfY)
        point_snap_3 = QPointF(pfX,pfY)
        point_snap_4 = QPointF(pfX,piY)

        delta_point_snap_1 = QPointF(point_base-point_snap_1)
        delta_point_snap_2 = QPointF(point_base-point_snap_2)
        delta_point_snap_3 = QPointF(point_base-point_snap_3)
        delta_point_snap_4 = QPointF(point_base-point_snap_4)

        list_deltas = [delta_point_snap_1, delta_point_snap_2, delta_point_snap_3,delta_point_snap_4]
        list_areas = []
        for delta in list_deltas:
            dx = delta.x()
            dy = delta.y()
            if dx ==0:
                dx=0.000001
            if dy ==0:
                dy=0.000001            
            list_areas.append(abs(dx*dy))

        index = list_areas.index(min(list_areas))

        if index == 0:
            return point_snap_1
        elif index == 1:
            return point_snap_2
        elif index == 2:
            return point_snap_3
        elif index == 3:
            return point_snap_4
        else:
            return point_base
    
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
        '''
        '''
        return val

    def pointInCursor(self,point_center:QPointF, rect:QRectF) -> PointItem:
        point = None
        len_point_min = 10000000
        items = self.items(rect)

        for item in items:
            if type(item) == PointItem:
                if item.getData()["name"] != "pointTemp":
                    delta = item.pos()-point_center
                    dx = abs(delta.x())
                    dy = abs(delta.y())
                    len_point = (dx + dy)**0.5
                    if len_point < len_point_min:
                        point = item
                        len_point_min = len_point
        return point

            