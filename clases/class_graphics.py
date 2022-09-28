"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : DiagramItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""
from ast import Pass
from cmath import rect
from ctypes import pointer
import math
"""
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF,QLineF,QEvent,QLineF,qAbs,QSizeF)
from PySide6.QtWidgets import ( QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QGraphicsLineItem,QGraphicsPixmapItem,
                            QStyle)
from PySide6.QtGui import (QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,QPainterPath,QFont,
                            QTransform,QColor,QRadialGradient)
"""

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
from clases import general_class
import weakref

pointsCoord = [
[   0.0000 ,  0.0000],
[   0.0010 ,  0.0010],
[   0.0100 ,  0.0000],
[ 100.0000 ,  0.0000],
[ 100.0000 , 60.9283],
[  68.4604 , 49.7303],
[  63.3560 , 35.7021],
[  54.9338 , 34.4268],
[  48.2981 , 34.9369],
[  41.4071 , 31.1111],
[  36.5580 , 28.3054],
[  28.3910 , 27.7953],
[  22.5209 , 22.6941],
[  15.1196 , 19.3784],
[   0.0000 , 19.2158]
]

class PointItem(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1
    def __init__(self, graphWidget ):
        QGraphicsItem.__init__(self)
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)


    def boundingRect(self) -> QRectF:
        return QRectF(-10, -10, 20, 20)


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:

        gradient = QRadialGradient(-3, -3, 10)
        if option.state & QStyle.State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            gradient.setColorAt(1, QColor(Qt.gray).lighter(120))
            gradient.setColorAt(0, QColor(Qt.darkGray).lighter(120))
        else:
            gradient.setColorAt(0, Qt.gray)
            gradient.setColorAt(1, Qt.darkGray)

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(Qt.black, 0))
        painter.drawEllipse(-1, -1, 2, 2)
        if self.isSelected():
            painter.setPen(QPen(QColor("#00ff00"), 1, Qt.DashLine))
            painter.drawEllipse(-2, -2, 2, 2)



    def type(self):
        return PointItem.Type

class Node(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1

    def __init__(self, graphWidget):
        QGraphicsItem.__init__(self)

        self.graph = weakref.ref(graphWidget)
        print(self.graph,">>>>",graphWidget)
        self.edgeList = []
        self.newPos = QPointF()
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(self.DeviceCoordinateCache)
        self.setZValue(-1)

    def type(self):
        return Node.Type

    def addEdge(self, edge):
        self.edgeList.append(weakref.ref(edge))
        edge.adjust()

    def edges(self):
        return self.edgeList

    def calculateForces(self):
        if not self.scene() or self.scene().mouseGrabberItem() is self:
            self.newPos = self.pos()
            return

        # Sum up all forces pushing this item away.
        xvel = 0.0
        yvel = 0.0
        for item in self.scene().items():
            if not isinstance(item, Node):
                continue

            line = QLineF(self.mapFromItem(item, 0, 0), QPointF(0, 0))
            dx = line.dx()
            dy = line.dy()
            l = 2.0 * (dx * dx + dy * dy)
            if l > 0:
                xvel += (dx * 150.0) / l
                yvel += (dy * 150.0) / l

        # Now subtract all forces pulling items together.
        weight = (len(self.edgeList) + 1) * 10.0
        for edge in self.edgeList:
            if edge().sourceNode() is self:
                pos = self.mapFromItem(edge().destNode(), 0, 0)
            else:
                pos = self.mapFromItem(edge().sourceNode(), 0, 0)
            xvel += pos.x() / weight
            yvel += pos.y() / weight

        if qAbs(xvel) < 0.1 and qAbs(yvel) < 0.1:
            xvel = yvel = 0.0

        sceneRect = self.scene().sceneRect()
        self.newPos = self.pos() + QPointF(xvel, yvel)
        self.newPos.setX(min(max(self.newPos.x(), sceneRect.left() + 10), sceneRect.right() - 10))
        self.newPos.setY(min(max(self.newPos.y(), sceneRect.top() + 10), sceneRect.bottom() - 10))

    def advance(self):
        if self.newPos == self.pos():
            return False

        self.setPos(self.newPos)
        return True

    def boundingRect(self):
        adjust = 2.0
        return QRectF(-10 - adjust, -10 - adjust,
                             23 + adjust, 23 + adjust)

    def shape(self):
        path = QPainterPath()
        path.addEllipse(-10, -10, 20, 20)
        return path

    def paint(self, painter, option, widget):
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.darkGray)
        painter.drawEllipse(-7, -7, 20, 20)

        gradient = QRadialGradient(-3, -3, 10)
        if option.state & QStyle.State_Sunken:
            gradient.setCenter(3, 3)
            gradient.setFocalPoint(3, 3)
            gradient.setColorAt(1, QColor(Qt.yellow).lighter(120))
            gradient.setColorAt(0, QColor(Qt.darkYellow).lighter(120))
        else:
            gradient.setColorAt(0, Qt.yellow)
            gradient.setColorAt(1, Qt.darkYellow)

        painter.setBrush(QBrush(gradient))
        painter.setPen(QPen(Qt.black, 0))
        painter.drawEllipse(-10, -10, 20, 20)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for edge in self.edgeList:
                edge().adjust()
            #self.graph().itemMoved()

        return QGraphicsItem.itemChange(self, change, value)

    def mousePressEvent(self, event):
        self.update()
        QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.update()
        QGraphicsItem.mouseReleaseEvent(self, event)

class RectItem(QGraphicsRectItem):
    def __init__(self,  parent=None):
        super().__init__(parent)

class LineItem(QGraphicsLineItem):
    def __init__(self):
        super().__init__()
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)

    def boundingRect(self):
        return QRectF(-200, -200, 400, 400)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget:QWidget):
        intersect_point = QPointF(0,0)
        self.setLine(QLineF(intersect_point, QPointF(500,500)))
        line = self.line()
        painter.drawLine(line)
        if self.isSelected():
            painter.setPen(QPen(QColor("#00ff00"), 1, Qt.DashLine))
            my_line = QLineF(line)
            my_line.translate(0, 4.0)
            painter.drawLine(my_line)
            my_line.translate(0, -8.0)
            painter.drawLine(my_line)

class GraphicsViewDraw (QGraphicsView):
    zoom_view = Signal(float)

    def __init__(self, SceneDraw:QGraphicsScene):
        super(GraphicsViewDraw, self).__init__() 

        #se le agrega la escena a la vista
        self.graphicsScene_draw = SceneDraw
        self.setScene(self.graphicsScene_draw)
        
        # para rastrear el raton en tiempo real
        self.setMouseTracking(True) 
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        """
        OTRAS PROPIEDADES
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setRenderHint(QPainter.Antialiasing)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setMinimumSize(400, 400)
        """

        #Atributos
        self.percent_zoom_view = 100
        self.zoom_scale = 1 
        self.scaleFactor = 1
        self.startPos = None
        self.mousePos = None
        self.mode_origin = True
        self.scale_view = 1
        
        # Configuracion para cursor
        self.cursor_position_view = QPoint(0,0)
        self.setCursor(Qt.BlankCursor)

        #Obtenemos tamaño de la pantalla para escalado de paint
        self.screen = QApplication.primaryScreen()
        self.size_screen = self.screen.size()
        self.scale_screen = self.size_screen.height()

        #******************************************
        # Figura inicial de prueba
        trianglePolygon = QPolygonF()
        for i in pointsCoord:
            trianglePolygon.append(QPointF(i[0], i[1]))
        
        pen= QPen(Qt.yellow)
        pen.setWidth(0)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor("#400509"))
        self.graphicsScene_draw.addPolygon(trianglePolygon,pen,brush)
        #******************************************

        #coloca un fondo por defecto en el view
        self.setStyleBackgroundView(0)


        #Atributos para dibujo
        self.vertex = 0
        self.draw_line = False
        self.line = None

        self.point_temp = False
        self.line_temp = False
        self.isDelate = False
        self.isClear = False
        self.isObject = None
        self.startX=None
        self.startY=None





    def setStyleBackgroundView(self, index):       
        
        if index == 0:
            color = "#aaaaaa"
        elif index == 1:
            color = "#888888"
        if index == 2:
            color = "#333333"
            
        self.setStyleSheet("background-color: {} ;border: 2px solid #444444;".format(color))
        self.graphicsScene_draw.setStyleGridScene(index)
   

    ###############################################################################
	# ::::::::::::::::    MÉTODOS PARA TRANSFORMACION DE VIEW    ::::::::::::::::::
	############################################################################### 
    def view_scale_changed(self, scale):
        """Cambia la escala de la vista 
        args:
            scale(str): Porcentaje de escalado en formato "X%" ejem: "200%"

        """
        #hacer zoom
        self.percent_zoom_view = float(scale[:-1])
        new_scale = self.percent_zoom_view / 100.0    
        old_matrix = self.transform()
        self.resetTransform()
        self.translate(old_matrix.dx(), old_matrix.dy())

        self.scale(new_scale, new_scale)
        self.zoom_view.emit(new_scale)
        self.graphicsScene_draw.scale_view=new_scale
        self.scale_view=new_scale

        new_point_cursor_scene = self.mapToScene(self.cursor_position_view)
        self.graphicsScene_draw.cursor_position=new_point_cursor_scene

    def move_view(self, deltaX, deltaY):

        #mover vista         
        transform = self.transform() 
        print("ESC H:",transform.m11())          
        deltaX =   deltaX/transform.m11()# m11 escala horizontal
        deltaY =  deltaY/transform.m22()# m22 escala vertical
        self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
        
    def scale_view(self, scaleFactor,scale_reverse):
        
        factor = self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()
        if factor < 0.05 or factor > 100000:
            return

        
        self.graphicsScene_draw.setScaledScreenSize(scale_reverse)
        self.scaleFactor = scaleFactor
        self.scale(scaleFactor, scaleFactor)
        '''
        self.screen = QApplication.primaryScreen()
        self.size_screen = self.screen.size()
        self.scale_screen = self.size_screen.height()
        self.zoom_scale = 1
        '''
        self.scale_screen = self.scale_screen * scale_reverse
        self.zoom_scale = self.size_screen.height()/self.scale_screen
        self.zoom_view.emit(self.zoom_scale)
       

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################    
    def mousePressEvent(self, mouseEvent):
        # activa el modo desplazamiento de la escena
        if mouseEvent.button() == Qt.MiddleButton:
            self.startPos = mouseEvent.pos()
            self.graphicsScene_draw.mode_crosshair_pick_box = False
            self.setCursor(Qt.OpenHandCursor)
        #se establece el punto inicial para dibujo 
        if mouseEvent.button() == Qt.LeftButton:   

            point_a = QPointF(self.mapToScene(mouseEvent.pos()))     

            if self.draw_line and self.vertex == 0:
                self.startX = point_a.x()
                self.startY = point_a.y()
                self.vertex  += 1



                
                self.line = QGraphicsLineItem(QLineF(point_a,point_a))
                self.line.setPen(QPen(QColor("#333333"),0))
                self.graphicsScene_draw.addItem(self.line)

                point1=PointItem(self)
                point1.setPos(point_a.x(),point_a.y())
                self.graphicsScene_draw.addItem(point1)
                print("@@",point1.type())

                #point1 = PointItem(self)
                #point1.setPos(self.startX,self.startY)
                #self.graphicsScene_draw.addItem(point1)

            elif self.draw_line and self.vertex == 1:

                point2=PointItem(self)
                point2.setPos(point_a.x(),point_a.y())
                self.graphicsScene_draw.addItem(point2)

                #self.graphicsScene_draw.addItem(LineItem(point1,point2))



                self.draw_line = False
                self.graphicsScene_draw.mode_crosshair = False
                self.vertex = 0

                '''
                print("P1.1")
                start_items = self.graphicsScene_draw.items(self.line.line().p1())
                print("start_items:",start_items)
                if len(start_items) and start_items[0] == self.line:
                    start_items.pop(0)

                end_items = self.graphicsScene_draw.items(self.line.line().p2())
                print("end_items:",end_items)
                if len(end_items) and end_items[0] == self.line:
                    end_items.pop(0)

                self.graphicsScene_draw.removeItem(self.line)
                self.line = None

                if (len(start_items) and len(end_items) and
                        start_items[0] != end_items[0]):
                    #line = LineItem(start_item, end_item)
                    #self.addItem(line)
                    pass

                print("P2  self.vertex : ", self.vertex)
                #self.paintObject(point_a)
                print("P3  self.vertex : ", self.vertex)
                '''

            #se dibuja punto
            if self.point_temp:
                self.draw_general(point_a)
                super(GraphicsViewDraw, self).mousePressEvent(mouseEvent)
        else:
            super(GraphicsViewDraw, self).mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        self.mousePos=mouseEvent.pos()

        # desplaza la escena view
        if self.startPos is not None:
            self.setCursor(Qt.ClosedHandCursor)
            # funcionalidad de :
            '''https://stackoverflow.com/questions/59239074/how-to-translate-drag-move-qgraphicsscene'''
            
            delta = self.startPos - mouseEvent.pos()            
            transform = self.transform()            
            deltaX = delta.x() / transform.m11()# m11 escala horizontal
            deltaY = delta.y() / transform.m22()# m22 escala vertical
            self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
            self.startPos = mouseEvent.pos()

        elif self.draw_line and self.vertex == 1 :

            point_b = QPointF(self.mapToScene(self.mousePos))  
            point_a = QPointF(0,0)
            point_a = self.line.line().p1()
            new_line = QLineF(point_a, point_b)




            #agigna la linea a la ya creada 
            self.line.setLine(new_line)


        elif self.line_temp == True:
            print("self.line_temp = True")
            super(GraphicsViewDraw, self).mouseMoveEvent(mouseEvent)
        else:
            self.setCursor(Qt.BlankCursor)
            super(GraphicsViewDraw, self).mouseMoveEvent(mouseEvent)

        self.cursor_position_view = QPoint(mouseEvent.x(),mouseEvent.y())
        '''
           
    def mouseMoveEvent(self, mouseEvent):

        e = QPointF(self.mapToScene(mouseEvent.pos()))
        self.tools(e)
        #print("-- mouseMoveEvent")



    '''
    
    def mouseReleaseEvent(self, mouseEvent):        
        # activa el modo desplazamiento de  view
        self.startPos = None
        
        self.setCursor(Qt.BlankCursor)
        self.graphicsScene_draw.mode_crosshair_pick_box = True
        self.update()

        #e = QPointF(self.mapToScene(mouseEvent.pos()))
        #self.paintObject(e)

        self.line_temp == False

        super(GraphicsViewDraw, self).mouseReleaseEvent(mouseEvent)

    def wheelEvent(self, event):
        angle_mouse = event.angleDelta().y()    
        scale = math.pow(1.5, angle_mouse / 240.0)
        '''
        star_pos_scene = self.graphicsScene_draw.mouse_pos_scene
        star_pos_view = self.mousePos
        # '''
        #anchor = self.transformationAnchor()
        #self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.prev_percent_zoom_view= self.percent_zoom_view
        self.percent_zoom_view = self.percent_zoom_view * scale
        
        if self.percent_zoom_view < 2:
            self.percent_zoom_view = 2
            return
        elif self.percent_zoom_view > 500000:
            self.percent_zoom_view = 500000
            return
        
        self.view_scale_changed("{:.1f}%".format(self.percent_zoom_view))
        
        #self.setTransformationAnchor(anchor)

        '''
        end_pos_mouse = self.graphicsScene_draw.mouse_pos_scene
        delta_pos = star_pos_mouse -end_pos_mouse
        print(delta_pos,star_pos_mouse, end_pos_mouse)
        self.move_view( delta_pos.x(), delta_pos.y())
        '''



        
        '''
        def wheel____Event(self, event):
            
            factor = 1.1
            if event.angleDelta().y() < 0:
                factor = 0.9
            print("\n")
            view_pos = self.mousePos
            print("View: ",view_pos)
            scene_pos = self.mapToScene(view_pos)
            print("Scene: ",scene_pos)
            self.centerOn(scene_pos)
            self.scale(factor, factor)
            delta = scene_pos - self.mapToScene(self.viewport().rect().center())
            print("delta: ",delta)
            self.centerOn(scene_pos - delta)
            self.centerOn()
        
            

        def wheelEvent(self, event):

            numDegrees = event.angleDelta().y() / 8
            numSteps = numDegrees / 15
            self.numScheduledScalings += numSteps
            print(numDegrees,numSteps,self.numScheduledScalings)
            if self.numScheduledScalings * numSteps < 0:
                self.numScheduledScalings = numSteps
                print(numDegrees,numSteps,self.numScheduledScalings)

            timeLine = QTimeLine(350, self)
            timeLine.setUpdateInterval(20)
            timeLine.valueChanged.connect(self.scalingTime)
            timeLine.finished.connect(self.animFinished())
            timeLine.start()
        '''

    '''
    def keyPressEvent(self, event: QKeyEvent) -> None:
        try:
            #print(event,event.type(),event.key())
            if event.key() >= 65 and event.key() <= 90:
                print("Presiono tecla de A-Z: {}".format(event.text()))
                self.key_press.emit(event.text())
            return super().keyPressEvent(event)
        except UnicodeDecodeError:
            print("no puede decodificar Ejemplo: Ñ ")
    
    def keyPressEvent(self, event):
        key = event.key()

        if key == Qt.Key_Plus:
            self.scale_view(1.2)
        elif key == Qt.Key_Minus:
            self.scale_view(1 / 1.2)
        
        elif key == Qt.Key_Space or key == Qt.Key_Enter:
            for item in self.scene().items():
                if isinstance(item, Node):
                    item.setPos(-150 + random(300), -150 + random(300))
        else:
            QGraphicsView.keyPressEvent(self, event)
    '''
    
    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS PARA DIBUJO          ::::::::::::::::::::
	############################################################################### 
    def drawPointScene(self):
        self.isObject = None
        self.point_temp = True
        self.isDelate = False
        self.isClear = False 
        self.graphicsScene_draw.mode_crosshair =True

    def drawLineScene(self):
        self.isObject = 0
        self.draw_line = True
        #self.isDelate = False
        #self.isClear = False
        self.graphicsScene_draw.mode_crosshair = True

    def draw_general(self, point):

        if self.point_temp == True:  
            point1=PointItem(self)
            point1.setPos(point.x(),point.y())
            print(9)
            self.graphicsScene_draw.addItem(point1)
            '''
            '''
            print(10)
            

            '''
            pen= QPen(Qt.gray)
            pen.setWidth(0)
            brush = QBrush(Qt.SolidPattern)
            brush.setColor(QColor("#000000"))
            diameter = 1
            self.graphicsScene_draw.addItem(self.graphicsScene_draw.addEllipse(
                                                                            point.x()-(diameter/2),
                                                                            point.y()-(diameter/2),
                                                                            diameter,
                                                                            diameter,
                                                                            pen,brush))
            print("revisar: QGraphicsScene::addItem: item has already been added to this scene")
            '''          

            self.point_temp = False
            self.graphicsScene_draw.mode_crosshair = False
            
            self.setScene(self.graphicsScene_draw)                
            self.show()
        if self.line_temp == True:
            pen= QPen(Qt.gray)
            pen.setWidth(0)
            self.graphicsScene_draw.addItem(self.graphicsScene_draw.addLine(self.startX,
                                                                            self.startY,
                                                                            point.x(),
                                                                            point.y(),
                                                                            pen))
            print("revisar: QGraphicsScene::addItem: item has already been added to this scene")

            self.point_temp = False
            self.graphicsScene_draw.mode_crosshair = False
            
            self.setScene(self.graphicsScene_draw)                
            self.show()
        if self.isDelate == True:
            items = self.items(point.x(),point.y())
            for item in items:
                self.graphicsScene_draw.removeItem(item)

    def paintObject(self,b):
        if self.isObject != None:
            object = self.isObject

            if object == 0:#line
                pen= QPen(Qt.black)
                pen.setWidth(0)

                self.graphicsScene_draw.addItem(self.graphicsScene_draw.addLine(self.startX,self.startY,b.x(),b.y(),pen))
                
                self.setScene(self.graphicsScene_draw) 
                self.draw_line = False
                self.graphicsScene_draw.mode_crosshair = False 
                self.vertex = 0              
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

    def drawForeground(self, painter: QPainter, rect: QRectF| QRect) -> None:

        """ Evento para dibujar en el primer plano, se dibuja la
        punta de mira y la caja de selección que sigue al ratself.scale_viewón """
        super(GraphicsViewDraw, self).drawForeground(painter, rect)
        if not hasattr(self, "sceneRect"):
            return
        point_view = QPoint(self.rect().x(),self.rect().y())        
        point_scene = self.mapToScene(point_view)

        #print("VIEW ▲▼ drawForeground")

        
        if  self.mode_origin == True :
            painter.save()
  
            
            xo=point_scene.x()
            yo=point_scene.y()
           

            scale_arrow = 2.1 * (1/self.scale_view)

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
            [xo + (4.5 * scale_arrow)  , yo + (19.5 * scale_arrow)]
            ]                

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
            [xo + (19.5 * scale_arrow), yo + (6.5 * scale_arrow)]
            ]           

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
    

class GraphicsSceneDraw (QGraphicsScene):
    
    InsertPoint, InsertRect, InsertLine, InsertText, MoveItem = range(5)
    point_inserted = Signal(PointItem)
    rect_inserted = Signal(RectItem)
    line_inserted = Signal(LineItem)
    text_inserted = Signal(QGraphicsTextItem)
    item_selected = Signal(QGraphicsItem)
    coor_mouse = Signal(list)
    
    

    def __init__(self, parent=None):
        super(GraphicsSceneDraw, self).__init__(parent)

        

        self.screen = QApplication.primaryScreen()
        self.size_screen = self.screen.size()
        self.scaled_screen_size = self.size_screen.height()

        # Atributos
        self.mode_axis = True
        self.mode_grid = True
        self.mode_crosshair_pick_box = True
        self.mode_crosshair = False

        self.mouse_pos_scene = None
        self.draw_line = False
        

        self.crosshair_size = 1.0
        self.pick_box_size = 0.005
        self.zoom_scale_general = 1
        self.setStyleGridScene(1)
        self.setScaledScreenSize(1)


        self.scale_view =1

    def setStyleGridScene(self, index):       
        
        if index == 0:
            self.color_grid="#bbbbbb"
            self.color_axis_x="#742427"
            self.color_axis_y="#C8CC8E"
        elif index == 1:
            self.color_grid="#777777"
            self.color_axis_x="#742427"
            self.color_axis_y="#C8CC8E"
        if index == 2:
            self.color_grid="#313A39"
            self.color_axis_x="#742427"
            self.color_axis_y="#6A6C48"
      
    def setScaledScreenSize(self, zoom_scale):

        self.scaled_screen_size = self.scaled_screen_size * zoom_scale
        self.zoom_scale_general = self.size_screen.height()/self.scaled_screen_size
    
    def drawBackground(self, painter, rect) -> None:
        """Evento para dibujar en el plano del fondo, se dibuja los ejes principales X y Y"""
        
        super(GraphicsSceneDraw, self).drawBackground(painter, rect)

        space_lines_axis = 50
        '''
        if min(abs(rect.top() ),        abs(rect.bottom() ),        abs(rect.right() ),        abs(rect.left() ))<50:
            space_lines_axis = 0.5
        elif min(abs(rect.top() ),        abs(rect.bottom() ),        abs(rect.right() ),        abs(rect.left() ))<5:
            space_lines_axis = 0.05
        '''

        

        lines_axis_x_top = (int(abs(rect.top() / space_lines_axis )))+1
        lines_axis_x_bottom = (int(abs(rect.bottom() / space_lines_axis )))+1
        lines_axis_y_right = (int(abs(rect.right() / space_lines_axis )))+1
        lines_axis_y_left = (int(abs(rect.left() / space_lines_axis )))+1


        if self.mode_axis == True or self.mode_grid == True:
            painter.save()

            if  self.mode_grid == True:

                pen_grid_x = QPen(QColor(self.color_grid))
                pen_grid_x.setWidth(0)
                painter.setPen(pen_grid_x)

                # lineas grilla X > positivo
                for i  in range(lines_axis_x_bottom):
                    linex_positive = QLineF(rect.left(), (i) * space_lines_axis,
                                rect.right(), (i) * space_lines_axis)
                    painter.drawLine(linex_positive)

                # lineas grilla X > negativo
                for i  in range(lines_axis_x_top):
                    linex_negative = QLineF(rect.left(), (i) * (-space_lines_axis),
                                rect.right(), (i) * (-space_lines_axis))
                    painter.drawLine(linex_negative)

                # lineas grilla Y positivo
                for i  in range(lines_axis_y_left):
                    linex_positive = QLineF((i) * space_lines_axis, rect.top(),
                                (i) * space_lines_axis, rect.bottom())
                    painter.drawLine(linex_positive)
                    linex_negative = QLineF( (i) * (-space_lines_axis),rect.top(),
                                (i) * (-space_lines_axis),rect.bottom())
                    painter.drawLine(linex_negative)

                # lineas grilla Y negativo
                for i  in range(lines_axis_y_right):
                    linex_positive = QLineF((i) * space_lines_axis, rect.top(),
                                (i) * space_lines_axis, rect.bottom())
                    painter.drawLine(linex_positive)
                    linex_negative = QLineF( (i) * (-space_lines_axis),rect.top(),
                                (i) * (-space_lines_axis),rect.bottom())
                    painter.drawLine(linex_negative)

            if self.mode_axis == True :

                # eje Y
                pen_axis_y = QPen(QColor(self.color_axis_y))
                pen_axis_y.setWidth(0)
                painter.setPen(pen_axis_y)
                liney = QLineF(0,rect.top(),0,rect.bottom(),)
                painter.drawLine(liney)

                # eje X
                pen_axis_x = QPen(QColor(self.color_axis_x))
                pen_axis_x.setWidth(0)
                painter.setPen(pen_axis_x)
                linex = QLineF(rect.left(),0,rect.right(),0,)
                painter.drawLine(linex)
            painter.restore()
  
    def drawForeground(self, painter: QPainter, rect: QRectF| QRect) -> None:

        """ Evento para dibujar en el primer plano, se dibuja la
        punta de mira y la caja de selección que sigue al ratón """
        super(GraphicsSceneDraw, self).drawForeground(painter, rect)
        if not hasattr(self, "cursor_position"):
            return
        #print("SCENE ▲▼ drawForeground")   
        #  
        if self.draw_line == True:
            return
        
        if self.mode_crosshair_pick_box == True :
            painter.save()
            # el pluma para el pick_box
            pen = QPen(QColor("#000000"))
            pen.setWidth(0)
            painter.setPen(pen)

            # se establece el porcentaje min y max del tamaño de pick_box
            pick_box_size = self.pick_box_size      
            if pick_box_size < 5:
                pick_box_size = 5
            elif pick_box_size > 50:
                pick_box_size = 50


            if self.mode_crosshair == True:
                pick_box_size_min = 0
            else:
                pick_box_size_min = pick_box_size * (1/self.scale_view)

            rectangle = QRectF(self.cursor_position.x() - (pick_box_size_min / 2),
                            self.cursor_position.y() - (pick_box_size_min / 2),
                            pick_box_size_min,
                            pick_box_size_min)
            
            
            painter.drawRect(rectangle)


            # el pluma para el crosshair
            pen = QPen(QColor("#000000"))
            pen.setWidth(0)
            painter.setPen(pen)
            
            crosshair_size = self.crosshair_size
            if crosshair_size >=1.0:
                crosshair_size = 2.0


            crosshair_size_max = crosshair_size * (self.size_screen.width()/2)* (1/self.scale_view)

            crosshair_size_left = self.cursor_position.x() + crosshair_size_max
            crosshair_size_right = self.cursor_position.x() - crosshair_size_max
            crosshair_size_top = self.cursor_position.y() + crosshair_size_max
            crosshair_size_botton = self.cursor_position.y() - crosshair_size_max

            linex_left = QLineF(crosshair_size_left,
                            self.cursor_position.y(),
                            self.cursor_position.x()+(pick_box_size_min/2),
                            self.cursor_position.y())
            
            linex_right = QLineF(self.cursor_position.x()-(pick_box_size_min/2),
                            self.cursor_position.y(),
                            crosshair_size_right,
                            self.cursor_position.y())

            liney_top = QLineF(self.cursor_position.x(),
                            crosshair_size_top,
                            self.cursor_position.x(),
                            self.cursor_position.y()+(pick_box_size_min/2))

            liney_botton = QLineF(self.cursor_position.x(),
                            self.cursor_position.y()-(pick_box_size_min/2),
                            self.cursor_position.x(),
                            crosshair_size_botton)

            for line in (linex_left,linex_right,liney_top,liney_botton):
                painter.drawLine(line)


            painter.restore()
    
    def mousePressEvent(self, mouseEvent):
        #print("SCENE ↓↓↓ mousePressEvent")


        '''
        MiddleButton: boton rueda raton
        LeftButton: boton izq raton
        RightButton: boton der raton
        '''
        '''
        print("@@@@ ",mouseEvent.scenePos())
        if (mouseEvent.button() != Qt.LeftButton):
            return

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
        """Evento al mover el ratón, se emite una señal con
        las coordenadas de ratón  para ser mostradas en statusBar
        """
        #print("SCENE →← mouseMoveEvent")

        self.cursor_position = mouseEvent.scenePos()
        self.coor_mouse.emit([self.cursor_position.x(),self.cursor_position.y()]) 
        self.mouse_pos_scene = self.cursor_position   
        self.update()

        super(GraphicsSceneDraw, self).mouseMoveEvent(mouseEvent)


        '''
        if self._my_mode == self.InsertLine and self.line:
            new_line = QLineF(self.line.line().p1(), mouseEvent.scenePos())
            self.line.setLine(new_line)
        elif self._my_mode == self.MoveItem:
            super(DiagramScene, self).mouseMoveEvent(mouseEvent)
        '''

    def mouseReleaseEvent(self, mouseEvent):
        #print("SCENE ↑↑↑ mouseReleaseEvent")
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

  















    '''
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""                       """""""""""""""""""""""""""
    """"""""""""""""""""          VIEW         """""""""""""""""""""""""""
    """"""""""""""""""""                       """""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    self.numScheduledScalings=0

    def scalingTime(self):
        factor = 1.0 + self.numScheduledScalings / 300.0
        self.scale(factor, factor)
    def animFinished(self):
        if self.numScheduledScalings > 0:
            self.numScheduledScalings -= 1
        else:
    self.numScheduledScalings += 1
        def getGraphicsScene(self):
        return  self.graphicsScene_draw

    '''