"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : DiagramItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""
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



class PointItem(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1
    def __init__(self, graphWidget ):
        QGraphicsItem.__init__(self)

class RectItem(QGraphicsRectItem):
    def __init__(self,  parent=None):
        super().__init__(parent)

class LineItem(QGraphicsLineItem):
    def __init__(self,  parent=None):
        super().__init__(parent)

class GraphicsViewDraw (QGraphicsView):
    def __init__(self, SceneDraw):
        super(GraphicsViewDraw, self).__init__() 
        self.setMouseTracking(True)       
        self.graphicsScene_draw = SceneDraw
        self.setScene(self.graphicsScene_draw)

        self.scaleFactor = 1
        self.startPos = None
        """
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)

        self.scale(0.8, 0.8)
        self.setMinimumSize(400, 400)
        """



        '''

        pen= QPen(Qt.yellow)
        brush = QBrush(Qt.SolidPattern)
        self.graphicsScene_draw.addItem(self.graphicsScene_draw.addRect(
                                                50,50,
                                                -50,-50,
                                                pen,brush))

        pen_red= QPen(Qt.red)
        self.graphicsScene_draw.addItem(self.graphicsScene_draw.addLine(0,-50000,0,50000,pen_red))
        self.pen= QPen(Qt.green)

        self.line_axis_x = QGraphicsLineItem(QLineF(QPointF(-50000,0),QPointF(-50000,0)))
        self.line_axis_x.setPen(self.pen)
        self.graphicsScene_draw.addItem(self.line_axis_x )
        
        pen= QPen(Qt.yellow)
        brush = QBrush(Qt.SolidPattern)
        self.graphicsScene_draw.addItem(self.graphicsScene_draw.addRect(
                                                0,0,
                                                -50,-50,
                                                pen,brush))
        pen= QPen(Qt.black)
        self.graphicsScene_draw.addItem(self.graphicsScene_draw.addRect(
                                                0,0,
                                                100,100,
                                                pen,brush))


        self.isLine = False
        self.isDelate = False
        self.isClear = False
        self.isObject = None
        self.startX=None
        self.startY=None
        '''

        #self.setStyleSheet("background-color: #444444 ;border: none;")
        self.setStyleSheet("background-color: #888888 ;border: none;")

        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #sirve para deplzar la ventana
        #self.setDragMode(QGraphicsView.ScrollHandDrag)
    """
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
    def mousePressEvent(self, event):
        if event.button() == Qt.MiddleButton:
            self.startPos = event.pos()
            self.graphicsScene_draw.mode_crosshair_pick_box = False
            self.setCursor(Qt.OpenHandCursor)
        else:
            super(GraphicsViewDraw, self).mousePressEvent(event)
    def mouseMoveEvent(self, event):
        if self.startPos is not None:
            # funcionalidad
            #https://stackoverflow.com/questions/59239074/how-to-translate-drag-move-qgraphicsscene
            delta = self.startPos - event.pos()
            transform = self.transform()
            deltaX = delta.x() / transform.m11()
            deltaY = delta.y() / transform.m22()
            self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
            self.startPos = event.pos()
        else:
            super(GraphicsViewDraw, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.startPos = None
        self.setCursor(Qt.ArrowCursor)
        self.graphicsScene_draw.mode_crosshair_pick_box = True
        super(GraphicsViewDraw, self).mouseReleaseEvent(event)


    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        #self.scale_view(math.pow(2.0, -delta / 240.0)) # cambia el sentido del zoom        
        self.scale_view(math.pow(1.5, delta / 240.0))
    
    def scale_view(self, scaleFactor):
        factor = self.transform().scale(scaleFactor, scaleFactor).mapRect(QRectF(0, 0, 1, 1)).width()
        if factor < 0.07 or factor > 200:
            return
        self.scaleFactor = (scaleFactor)
        self.scale(scaleFactor, scaleFactor)
        #self.pen.setColor(Qt.black)        
        #self.pen= QPen(Qt.green)
        #self.graphicsScene_draw.addLine(-50000,0,50000,0,self.pen)


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
        
        # Atributos
        self.mode_axis = True
        self.mode_grid = True
        self.mode_crosshair_pick_box = True
        self.contador = 0

        self.crosshair_size = 1.0
        self.pick_box_sise = 0.07




    def drawBackground(self, painter, rect) -> None:
        """Evento para dibujar en el plano del fondo, se dibuja los ejes principales X y Y"""
        super(GraphicsSceneDraw, self).drawBackground(painter, rect)
        self.contador += 1

        space_lines_axis = 50
        print("{}  {}  max_:{}".format(
            
            (rect.top()),(rect.bottom()),

            max(abs(rect.top()),abs(rect.bottom()) )
            
            
            ))

        """"
        okkkkk
        """

        lines_axis_x_top = (int(abs(rect.top() / space_lines_axis )))+1
        lines_axis_x_bottom = (int(abs(rect.bottom() / space_lines_axis )))+1
        lines_axis_y_right = (int(abs(rect.right() / space_lines_axis )))+1
        lines_axis_y_left = (int(abs(rect.left() / space_lines_axis )))+1




        """
        lines_axis_x = (int(abs(rect.top() / space_lines_axis )))+1
        print(lines_axis_x)
        lines_axis_x = (int(abs((((rect.bottom())-(rect.top()))/2) / space_lines_axis )))+1
        print(lines_axis_x)
        lines_axis_y = (int(abs(rect.right() / space_lines_axis )))+1

        lines_axis_x = 20
        lines_axis_y = 20
        """

        if self.mode_axis == True or self.mode_grid == True:
            painter.save()

            if  self.mode_grid == True:

                pen_grid_x = QPen(QColor("#777777"))
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
                pen_axis_y = QPen(QColor("#C8CC8E"))
                pen_axis_y.setWidth(0)
                painter.setPen(pen_axis_y)
                liney = QLineF(0,rect.top(),0,rect.bottom(),)
                painter.drawLine(liney)

                # eje X
                pen_axis_x = QPen(QColor("#742427"))
                pen_axis_x.setWidth(0)
                painter.setPen(pen_axis_x)
                linex = QLineF(rect.left(),0,rect.right(),0,)
                painter.drawLine(linex)
            painter.restore()

        elif self.mode_axis == False or self.mode_grid == False:
            # deberia eliminar los ejes
            #painter.save()
            #painter.restore()
            pass


    
    def drawForeground(self, painter, rect):
        """ Evento para dibujar en el primer plano, se dibuja la
        punta de mira y la caja de selección que sigue al ratón """
        super(GraphicsSceneDraw, self).drawForeground(painter, rect)
        if not hasattr(self, "cursor_position"):
            return
        #print("SCENE ▲▼ drawForeground")    
        if self.mode_crosshair_pick_box == True:
            painter.save()

            # el pluma para el crosshair
            pen = QPen(QColor("#666666"))
            pen.setWidth(0)
            painter.setPen(pen)
            
            crosshair_size = self.crosshair_size
            if crosshair_size >=1.0:
                crosshair_size = 2.0
                
            crosshair_size_max = crosshair_size * max(abs(rect.left()), abs(rect.right()), abs(rect.top()), abs(rect.bottom()))
            crosshair_size_left = self.cursor_position.x() - crosshair_size_max
            crosshair_size_right = self.cursor_position.x() + crosshair_size_max
            crosshair_size_top = self.cursor_position.y() - crosshair_size_max
            crosshair_size_botton = self.cursor_position.y() + crosshair_size_max

            '''
            crosshair_size = 0.9
            if crosshair_size == 1.0:
                crosshair_size_left = rect.left()
                crosshair_size_right = rect.right()
                crosshair_size_top = rect.top()
                crosshair_size_botton = rect.bottom()
            elif crosshair_size < 1.0:
                crosshair_size_max = crosshair_size * max(abs(rect.left()), abs(rect.right()), abs(rect.top()), abs(rect.bottom()))
                crosshair_size_left = self.cursor_position.x() - crosshair_size_max
                crosshair_size_right = self.cursor_position.x() + crosshair_size_max
                crosshair_size_top = self.cursor_position.y() - crosshair_size_max
                crosshair_size_botton = self.cursor_position.y() + crosshair_size_max
            else:
                return       
            '''   
            

            linex = QLineF(crosshair_size_left,
                            self.cursor_position.y(),
                            crosshair_size_right,
                            self.cursor_position.y())
            liney = QLineF(self.cursor_position.x(),
                            crosshair_size_top,
                            self.cursor_position.x(),
                            crosshair_size_botton)
            for line in (linex, liney):
                painter.drawLine(line)

            # el pluma para el pick_box
            pen = QPen(QColor("#000000"))
            pen.setWidth(0)
            painter.setPen(pen)

            # se establece el porcentaje min y max del tamaño de pick_box
            pick_box_sise = self.pick_box_sise      
            if pick_box_sise > 0.2:
                pick_box_sise = 0.2
            elif pick_box_sise < 0.03:
                pick_box_sise = 0.03

            pick_box_sise_min = pick_box_sise * min(
                (rect.right()- rect.left())/2,
                (rect.bottom()- rect.top())/2
                ) 
            """
            print("{:.2f}  {:.2f}[I:{:.2f}, D:{:.2f}, T:{:.2f}, B:{:.2f}]".format(pick_box_sise_min,
                                        min(abs(rect.left()), abs(rect.right()), abs(rect.top()), abs(rect.bottom())),
                                        rect.left(), rect.right(), rect.top(), rect.bottom(),
                                        ) )
            """


            rect = QRectF(self.cursor_position.x() - (pick_box_sise_min / 2),
                            self.cursor_position.y() - (pick_box_sise_min / 2),
                            pick_box_sise_min,
                            pick_box_sise_min)
            


            
            painter.drawRect(rect)
            painter.restore()

    def mousePressEvent(self, mouseEvent):
        print("SCENE ↓↓↓ mousePressEvent")
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
        print("SCENE ↑↑↑ mouseReleaseEvent")
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

  