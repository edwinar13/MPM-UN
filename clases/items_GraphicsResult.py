"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : PointItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

from typing import Optional
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*

import sys
import weakref
import math

contador = 0 



class ItemResultNode(QGraphicsItem):
    """color_type 1 o 2"""
    COLOR_1A = "#e8ca7b"
    COLOR_1B = "#a8821d"
    COLOR_1C = "#a8821d"

    COLOR_2A = "#a89565"
    COLOR_2B = "#594c2b"
    COLOR_2C = "#594c2b"
    
    signal_time_steps_changed = Signal(int)

    def __init__(self, radius, color_type, data_result):
        QGraphicsItem.__init__(self)
        if color_type == 1:
            self.color_a = self.COLOR_1A
            self.color_b = self.COLOR_1B
            self.color_c = self.COLOR_1C
        else:
            self.color_a = self.COLOR_2A
            self.color_b = self.COLOR_2B
            self.color_c = self.COLOR_2C


        self.radius = radius
        

        self._time_view = 0
        self.no_data = len(data_result['TIEMPOS'])
        self.times = data_result['TIEMPOS']
        self.coorX = data_result['CORX']
        self.coorY = data_result['CORY']
        self.sigXX = data_result['SIGXX']
        self.sigYY = data_result['SIGYY']
        self.sigXY = data_result['SIGXY']
        self.epsXX = data_result['EPSXX']
        self.epsYY = data_result['EPSYY']
        self.epsXY = data_result['EPSXY']
        
        #maximo
        self.max_sigXX = max(self.sigXX)
        self.min_sigXX = min(self.sigXX)
        self.d_sigXX = self.max_sigXX - self.min_sigXX

        
        xo = self.coorX[0]
        yo = self.coorY[0]
        
        self.coor = QPointF(xo, yo)
        self.movePoint(self.coor)
        


        gradient = QRadialGradient(self.radius / 4, self.radius / 2,
                                self.radius, self.radius / 2, self.radius / 2)
        gradient.setColorAt(0, QColor(self.color_a))
        gradient.setColorAt(1, QColor(self.color_b))

        # Establecer el gradiente como el fondo de la vista
        self.brush = QBrush(gradient)
        self.pen = QPen(QColor(self.color_c), 0, Qt.SolidLine)

        # Crear una sombra difusa
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#555"))
        self.shadow_effect.setBlurRadius(25)
        self.shadow_effect.setOffset(2, 2)

        # Aplicar la sombra al item
        self.setGraphicsEffect(self.shadow_effect)
        
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.advanceTime)
        
    def getCurrentTime(self):
        return self._time_view

    def advanceTime(self):
        self._time_view += 10
        if self._time_view >= self.no_data:
            self.playPauseTime(False)
            self._time_view = self.no_data - 1
        elif self._time_view < 0:
            self._time_view = 0
        #
        # 
        # 
        # 
        # self.signal_time_steps_changed.emit(self._time_view) 
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))
    
        #cambiar color
        percent = self.sigXX[self._time_view]/self.d_sigXX
        r =255  
        '''
        if round((self.sigXX[self._time_view]/self.max_sigXX)*255,0) >255:
            g = 255
        else:
            g = round((self.sigXX[self._time_view]/self.max_sigXX)*255,0) 
        '''
        g = round(1-(percent*255),0) 
        if g < 0:
            g = 0
        elif g > 255:
            g = 255
        
        b =0 
        #print(f" {g}---->>> color {(1- (self.sigXX[self._time_view]/self.max_sigXX))*255} data {self.sigXX[self._time_view]}")
        self.color_a = QColor(r,g,b)
        self.brush = QBrush(QColor(self.color_a))
    def stopTime(self):
        self.timer.stop() 
        self._time_view = 0
        #
        # 
        # 
        # 
        # 
        # 
        # self.signal_time_steps_changed.emit(self._time_view) 
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))
        
    def playPauseTime(self, scene_is_play, velocity=100):  
        if not scene_is_play:
            self.timer.stop()
        else:      
            self.timer.start(1000 / velocity) # intervalo en milisegundos
    
    
    def regressTime(self):
        self._time_view -= 1        
        if self._time_view >= self.no_data:
            self._time_view = self.no_data - 1
        elif self._time_view < 0:
            self._time_view = 0
        #
        # 
        # 
        # 
        # 
        # 
        # 
        # 
        # self.signal_time_steps_changed.emit(self._time_view) 
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))



    def movePoint(self, pos:QPointF):
        print(f"{self._time_view}")
        self.coor = pos
        self.setPos(pos)

    def boundingRect(self):
        return QRectF(-self.radius,-self.radius,self.radius*2,self.radius*2)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        # Especifica el radio de las esquinas curvas (10 en este ejemplo, pero puedes ajustarlo a tu gusto)
        radius = self.radius
        painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)

class ItemResultBaseMeshBack(QGraphicsItem):
    COLOR_A = "#bbb"
    COLOR_B = "#666"
    COLOR_C = "#aaa"
    RADIUS = 1
    def __init__(self, x, y, width, height):
        QGraphicsItem.__init__(self)

        self.color_a = self.COLOR_A
        self.color_b = self.COLOR_B
        self.color_c = self.COLOR_C
        self.corner_radius = self.RADIUS * (width/50)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        gradient = QLinearGradient(0, 0, 0, self.height)
        gradient.setColorAt(0, QColor(self.color_a))
        gradient.setColorAt(1, QColor(self.color_b))

        # Establecer el gradiente como el fondo de la vista
        self.brush = QBrush(gradient)
        self.pen = QPen(QColor(self.color_c), 0, Qt.SolidLine)

        # Crear una sombra difusa
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#999"))
        self.shadow_effect.setBlurRadius(40)
        self.shadow_effect.setOffset(3, 3)

        # Aplicar la sombra al item
        self.setGraphicsEffect(self.shadow_effect)

    def boundingRect(self):
        return QRectF(self.x - (self.width ), self.y - (self.height / 10), self.width * 3, self.height / 10)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        # Especifica el radio de las esquinas curvas (10 en este ejemplo, pero puedes ajustarlo a tu gusto)
        
        painter.drawRoundedRect(self.boundingRect(), self.corner_radius, self.corner_radius)

class ItemResultAxisMeshBack(QGraphicsItem):

    WIDTH = 0.05
    COLOR = "#222222"


    def __init__(self, x, y, width, height ):
        QGraphicsItem.__init__(self)

        self.color = self.COLOR
        self.width_border = self.WIDTH*(width/50)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        
        self.path = QPainterPath()
        points = [] 
        points.append(QPointF(x, y))
        points.append(QPointF(x + width, y))
        points.append(QPointF(x + width,y + height))
        points.append(QPointF(x, y + height))
        points.append(QPointF(x,y))

        self.path.addPolygon(QPolygonF(points))

   
        
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )



    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        painter.drawRect(self.boundingRect())

class ItemResultGridMeshBack(QGraphicsItem):

    WIDTH = 0
    COLOR = "#aaa"


    def __init__(self, x, y, width, height ):
        QGraphicsItem.__init__(self)

        self.color = self.COLOR
        self.width_border = self.WIDTH

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        len_min = min(self.width, self.height)
        dxy = len_min/10
        no_lines_x = math.ceil(self.width / dxy)
        no_lines_y = math.ceil(self.height / dxy)
        
        
        self.lines = []

        for i in range(no_lines_x):
            x1=x + (i*dxy)
            x2=x + (i*dxy)
            y1=y
            y2=y+height
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)

        for i in range(no_lines_y):
            x1=x 
            x2=x + width
            y1=y + (i*dxy)
            y2=y + (i*dxy)
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)


   
        
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )


    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        painter.drawLines(self.lines)
        
class ItemResultLabelGridMeshBack(QGraphicsItem):

    WIDTH = 0.2
    COLOR = "#888"


    def __init__(self, scene, x, y, width, height ):
        QGraphicsItem.__init__(self)

        self.color = self.COLOR
        self.width_border = self.WIDTH *(width/50)

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        len_min = min(self.width, self.height)
        dxy = len_min/10
        line_label_dxy = dxy/10
        no_lines_x = math.ceil(self.width / dxy)
        no_lines_y = math.ceil(self.height / dxy)
        

        self.lines = []
        for i in range(no_lines_x):
            # Inferior
            x1=x + (i*dxy)
            x2=x + (i*dxy)
            y1=y - line_label_dxy
            y2=y + line_label_dxy
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(round(x + (i*dxy),1)),
                                      coordinatesX= x + (i*dxy),
                                      coordinatesY= y - (0*line_label_dxy),
                                      angle_degrees=90,
                                      alignment='BOTTOM')
            text_label.setScale(0.01)
            scene.addItem(text_label)

            # superior
            x1=x + (i*dxy)
            x2=x + (i*dxy)
            y1=y + height - line_label_dxy
            y2=y + height + line_label_dxy
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(round(x + (i*dxy),1)),
                            coordinatesX= x + (i*dxy),
                            coordinatesY= y + height + (0*line_label_dxy),
                            angle_degrees=-90,
                            alignment='TOP')
            text_label.setScale(0.01)
            scene.addItem(text_label)

        for i in range(no_lines_y):

            # izquierda
            x1=x - line_label_dxy
            x2=x + line_label_dxy
            y1=y + (i*dxy)
            y2=y + (i*dxy)
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(round(y + i*dxy,1)),
                                      coordinatesX= x - (0*line_label_dxy),
                                      coordinatesY= y + (i*dxy),
                                      angle_degrees=0,
                                      alignment='LEFT')            
            text_label.setScale(0.01)
            scene.addItem(text_label)
            

            #derecha
            x1=x + width - line_label_dxy
            x2=x + width + line_label_dxy
            y1=y + (i*dxy)
            y2=y + (i*dxy)
            line = QLineF(x1,y1,x2,y2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(round(y + i*dxy,1)),
                                      coordinatesX= x + width + (0*line_label_dxy),
                                      coordinatesY= y + (i*dxy),
                                      angle_degrees=0,
                                      alignment='RIGHT')  
            text_label.setScale(0.01)          
                      
            scene.addItem(text_label)


   
        
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )


    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        painter.drawLines(self.lines)

class ItemResultTextLabel(QGraphicsItem):
    """ alignment >> TOP, BOTTOM, LEFT, RIGHT"""

    COLOR = "#222"
    FONT_SIZE = 10

    def __init__(self, text: str, coordinatesX, coordinatesY, angle_degrees=0, alignment="RIGHT"):
        QGraphicsItem.__init__(self)

        self.color = self.COLOR
        self.angle_degrees = angle_degrees        
        self.text = "{}".format(text)      
        self.position = QPointF(coordinatesX, coordinatesY)
        self.newPos(self.position)
        self.pen = QPen(QColor(self.color))

        self.font = QFont("Times", self.FONT_SIZE)

        width = self.boundingRect().width()
        height = self.boundingRect().height()
        self.coor = QPointF(0, 0)
        if alignment=="TOP":
            self.coor = QPointF(-width/2, -height)
        elif alignment=="BOTTOM":
            self.coor = QPointF(-width/2,  (height*2))
        elif alignment=="LEFT":
            self.coor = QPointF((-width*2), height/2)
        elif alignment=="RIGHT":
            self.coor = QPointF(width,  height/2)
        
    def newPos(self, pos:QPointF|QPoint):        
        self.setPos(pos)

    def boundingRect(self) -> QRectF:
        font_metrics = QFontMetrics(self.font)
        text_rect = font_metrics.boundingRect(self.text)
        text_rect.setHeight(font_metrics.ascent())
        return text_rect

    def paint(self, painter: QPainter, option, widget=None):
        painter.setPen(self.pen)
        painter.setFont(self.font)
        painter.scale(1, -1)

        painter.drawText(self.coor, self.text)


class ItemResultTextLabel000(QGraphicsItem):
    """
    ItemResultTextLabel es una clase que hereda de QGraphicsItem y representa un texto con posibilidad de rotación
    en una escena.

    Atributos:
        text (str): Texto a mostrar.
        coordinatesX (int): Coordenada X del punto de origen del texto.
        coordinatesY (int): Coordenada Y del punto de origen del texto.
        angle_degrees (float): Ángulo de rotación del texto en grados (0 por defecto, sin rotación).
        alignment (Qt.AlignmentFlag): Alineación del texto dentro de su área delimitadora (Qt.AlignCenter por defecto).
        color (Qt.GlobalColor): Color con el que se dibujará el texto (Qt.black por defecto).
        font (QFont): Fuente utilizada para el texto (QFont por defecto).

    Aparte de Qt.AlignCenter, hay varios otros valores que puedes usar para controlar la alineación del texto en el método paint. Algunos de los valores más comunes son:

    - Qt.AlignLeft: Alinea el texto a la izquierda.
    - Qt.AlignRight: Alinea el texto a la derecha.
    - Qt.AlignTop: Alinea el texto en la parte superior.
    - Qt.AlignBottom: Alinea el texto en la parte inferior.
    - Qt.AlignTop | Qt.AlignRight: Alinea el texto en la esquina superior derecha.
    - Qt.AlignBottom | Qt.AlignLeft: Alinea el texto en la esquina inferior izquierda.

    Puedes combinar estos valores usando el operador | (bitwise OR) para obtener la alineación deseada. Por ejemplo, si deseas alinear el texto en la esquina inferior derecha, puedes usar:
        alignment = Qt.AlignBottom | Qt.AlignRight
    Estos valores te permiten controlar dónde se posiciona el texto dentro del rectángulo delimitador y cómo se alinea con respecto a ese rectángulo. Experimenta con diferentes combinaciones para lograr el resultado deseado en tu aplicación.
    """

    COLOR = "#222"
    FONT_SIZE = 10

    def __init__(self, text: str, coordinatesX, coordinatesY, angle_degrees=0):
        QGraphicsItem.__init__(self)
        
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        self.color = self.COLOR
        self.angle_degrees = angle_degrees        
        self.text = text      
        self.position = QPointF(coordinatesX, coordinatesY)
        self.newPos(self.position)
        self.pen = QPen(QColor(self.color))

        self.font = QFont()
        self.font.setPointSize(self.FONT_SIZE)

    def newPos(self, pos:QPointF|QPoint):
        self.coor = pos
        self.setPos(pos)

    def boundingRect(self) -> QRectF:
        # Obtener el rectángulo delimitador del texto utilizando QFontMetricsF
        font_metrics = QFontMetricsF(self.font)
        text_rect = font_metrics.boundingRect(QRectF(), Qt.AlignCenter, self.text)

        # Ajustar el rectángulo devuelto para que contenga todo el texto
        bounding_rect = text_rect

        return bounding_rect

    def paint(self, painter: QPainter, option, widget=None):
        painter.setPen(self.pen)
        painter.save()
        painter.translate(QPointF(0, 0))
        painter.rotate(self.angle_degrees)
        painter.drawText(QPointF(0, 0), self.text)
        painter.restore()




class Edge(QGraphicsItem):

    item_type = QGraphicsItem.UserType + 2

    def __init__(self, sourceNode, destNode):
        super().__init__()

        print(self.item_type())

        self._arrow_size = 10.0
        self._source_point = QPointF()
        self._dest_point = QPointF()
        self.setAcceptedMouseButtons(Qt.NoButton)
        self.source = weakref.ref(sourceNode)
        self.dest = weakref.ref(destNode)
        self.source().add_edge(self)
        self.dest().add_edge(self)
        self.adjust()

    def item_type(self):
        return Edge.item_type

    def source_node(self):
        return self.source()

    def set_source_node(self, node):
        self.source = weakref.ref(node)
        self.adjust()

    def dest_node(self):
        return self.dest()

    def set_dest_node(self, node):
        self.dest = weakref.ref(node)
        self.adjust()

    def adjust(self):
        if not self.source() or not self.dest():
            return

        line = QLineF(self.mapFromItem(self.source(), 0, 0),
                      self.mapFromItem(self.dest(), 0, 0))
        length = line.length()

        if length == 0.0:
            return

        edge_offset = QPointF((line.dx() * 10) / length, (line.dy() * 10) / length)

        self.prepareGeometryChange()
        self._source_point = line.p1() + edge_offset
        self._dest_point = line.p2() - edge_offset

    def boundingRect(self):
        if not self.source() or not self.dest():
            return QRectF()

        pen_width = 1
        extra = (pen_width + self._arrow_size) / 2.0

        width = self._dest_point.x() - self._source_point.x()
        height = self._dest_point.y() - self._source_point.y()
        rect = QRectF(self._source_point, QSizeF(width, height))
        return rect.normalized().adjusted(-extra, -extra, extra, extra)

    def paint(self, painter, option, widget):
        if not self.source() or not self.dest():
            return

        # Draw the line itself.
        line = QLineF(self._source_point, self._dest_point)

        if line.length() == 0.0:
            return

        painter.setPen(QPen(Qt.black, 1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        painter.drawLine(line)

        # Draw the arrows if there's enough room.
        angle = math.acos(line.dx() / line.length())
        if line.dy() >= 0:
            angle = 2 * math.pi - angle

        arrow_head1 = QPointF(math.sin(angle + math.pi / 3) * self._arrow_size,
                              math.cos(angle + math.pi / 3) * self._arrow_size)
        source_arrow_p1 = self._source_point + arrow_head1
        arrow_head2 = QPointF(math.sin(angle + math.pi - math.pi / 3) * self._arrow_size,
                              math.cos(angle + math.pi - math.pi / 3) * self._arrow_size)
        source_arrow_p2 = self._source_point + arrow_head2

        arrow_head1 = QPointF(math.sin(angle - math.pi / 3) * self._arrow_size,
                              math.cos(angle - math.pi / 3) * self._arrow_size)
        dest_arrow_p1 = self._dest_point + arrow_head1
        arrow_head2 = QPointF(math.sin(angle - math.pi + math.pi / 3) * self._arrow_size,
                              math.cos(angle - math.pi + math.pi / 3) * self._arrow_size)
        dest_arrow_p2 = self._dest_point + arrow_head2

        painter.setBrush(Qt.black)
        painter.drawPolygon(QPolygonF([line.p1(), source_arrow_p1, source_arrow_p2]))
        painter.drawPolygon(QPolygonF([line.p2(), dest_arrow_p1, dest_arrow_p2]))


class Node(QGraphicsItem):
    item_type = QGraphicsItem.UserType + 1

    def __init__(self, graphWidget):
        super().__init__()

        self.graph = weakref.ref(graphWidget)
        self._edge_list = []
        self._new_pos = QPointF()
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setCacheMode(self.DeviceCoordinateCache)
        self.setZValue(-1)

    def item_type(self):
        return Node.item_type

    def add_edge(self, edge):
        self._edge_list.append(weakref.ref(edge))
        edge.adjust()

    def edges(self):
        return self._edge_list

    def calculate_forces(self):
        if not self.scene() or self.scene().mouseGrabberItem() is self:
            self._new_pos = self.pos()
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
        weight = (len(self._edge_list) + 1) * 10.0
        for edge in self._edge_list:
            if edge().source_node() is self:
                pos = self.mapFromItem(edge().dest_node(), 0, 0)
            else:
                pos = self.mapFromItem(edge().source_node(), 0, 0)
            xvel += pos.x() / weight
            yvel += pos.y() / weight

        if qAbs(xvel) < 0.1 and qAbs(yvel) < 0.1:
            xvel = yvel = 0.0

        scene_rect = self.scene().sceneRect()
        self._new_pos = self.pos() + QPointF(xvel, yvel)
        self._new_pos.setX(min(max(self._new_pos.x(), scene_rect.left() + 10),
                               scene_rect.right() - 10))
        self._new_pos.setY(min(max(self._new_pos.y(), scene_rect.top() + 10),
                               scene_rect.bottom() - 10))

    def advance(self):
        if self._new_pos == self.pos():
            return False

        self.setPos(self._new_pos)
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
            for edge in self._edge_list:
                edge().adjust()
            self.graph().item_moved()

        return QGraphicsItem.itemChange(self, change, value)

    def mousePressEvent(self, event):
        self.update()
        QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        self.update()
        QGraphicsItem.mouseReleaseEvent(self, event)





class PointAnimation (QObject):
    def __init__(self, point_item, time_list, x_list, y_list):
        super(PointAnimation, self).__init__()
        self.point_item = point_item
        self.time_list = time_list
        self.x_list = x_list
        self.y_list = y_list
        self.animation = QPropertyAnimation(self, b"pos")

    def startAnimation(self):
        self.animation.setDuration(self.time_list[-1])
        self.animation.setKeyValueAt(0.0, self.point_item.pos())
        for t, x in zip(self.time_list, self.x_list):
            pos = QPointF(x,0)
            self.animation.setKeyValueAt(t/self.time_list[-1], pos)
        self.animation.start()

class TextResultItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#00ff55")
    HIGT = 10
    WIDTH = 40

    def __init__(self, text:str, coordinatesX, coordinatesY):
        QGraphicsItem.__init__(self)
        
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        self.item_type = self.TYPE
        self.color = self.COLOR
        self.higt = self.HIGT
        self.width = self.WIDTH
        self.text = str(text)
        self.position = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.position)
        self.pen = QPen(self.color)


    def setColor(self, color):
        self.color = QColor(color)
        self.pen = QPen(self.color)


    def newPos(self, pos:QPointF|QPoint):
        self.coor = pos
        self.setPos(pos)

    def boundingRect(self) -> QRectF:
        h = self.higt
        w = self.width        
        return QRectF(-0.1, -h,
                             w, h+3)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        painter.setPen(self.pen)
        painter.drawText(QPointF(0, 0), self.text)


class PointResultItem(QGraphicsItem):
    """
    PointItem es una clase que hereda de QGraphicsItem y representa un punto en una escena.
    
    Atributos:
        id (int): Numero único del elemento 
        name (str): Nombre del punto.
        coor (QPointF): Coordenadas del punto.
        type (str): Tipo de elemento gráfico (en este caso, siempre es "Point").
        color (Qt): Color con el que se dibujará el punto.        
        radius (float): Radio con el que se dibujará el punto.
        draw_rect_osnap (bool): Indica si se debe dibujar un rectángulo para facilitar la selección del punto.

        isSelectedDraw (bool): Indica si el punto está seleccionado en el momento.
        isActive (bool): Indica si el punto está activo en el momento.
        
    """
    
    TYPE = "Point"
    RADIUS = 1
    COLOR = Qt.black


    def __init__(self,id, name:str, coordinatesX, coordinatesY, text_name:TextResultItem):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        #self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.id = id
        self.name = name
        self.item_type = self.TYPE
        self.coor = QPointF(coordinatesX, coordinatesY)
        self.color = self.COLOR
        self.radius = self.RADIUS

        self.text_name = text_name
        self.text_name.setVisible(False)
        self.text_name.setColor("#7E6807")

     
        self.movePoint(self.coor)
        self.draw_rect_osnap = False
        self.isSelectedDraw = False
        self.showLabel = False

        self.pen = QPen(self.color, 0)
        self.pen_osnap =QPen(QColor("#34c3eb"), 0, Qt.SolidLine)
        self.pen_selected = QPen(QColor("#960b0f"), 0, Qt.DashLine)
        self.pen_selected.setCosmetic(True)
        self.pen_selected.setWidthF(0.5)

        self.brush = QBrush(QColor("#960b0f"))


    def getId(self):
        return self.id
          
    def getData(self):
        
        data = {
            "id":self.id,
            'name': self.name,
            'type': self.item_type,
            'coordinates': [self.coor.x(), self.coor.y()]
            }
        return data
    
    def getCoordinates(self):
        return self.coor


    def movePoint(self, pos:QPointF):
        self.coor = pos
        self.setPos(pos)
        self.text_name.newPos(self.coor)

    def boundingRect(self) -> QRectF:
        radius = self.radius - 1.99
        return QRectF(-radius, -radius,
                             2*radius, 2*radius)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.draw_rect_osnap:
            painter.setPen(self.pen_osnap)
            painter.drawRect(-5,-5,10,10)
            self.draw_rect_osnap = False            

        if self.isSelectedDraw:
            self.pen_selected.setWidthF(1 / painter.transform().m11()) # m11()
            painter.setPen(self.pen_selected)
            painter.drawEllipse(-5,-5,10,10)

        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)

        if self.name != "pointTemp" and self.showLabel:  
            '''
            self.text_name.newPos(self.coor)
            list_lines = []
            for line in self.anchored_lines:                
                list_lines.append(line.name)
            ''' 
            self.text_name.setVisible(True)
        else:
            self.text_name.setVisible(False)

class PointMaterialResultItem(QGraphicsItem):
   
    RADIUS = 0.1

    def __init__(self,id, name:str, color:str, coor:list ):
        QGraphicsItem.__init__(self)        

        #self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.id = id
        self.name = name
        self.color = color
        self.coor = QPointF(coor[0],coor[1])

        self.radius = self.RADIUS
   

        self.movePoint(self.coor)


        self.pen = QPen(QColor(self.color), 0, Qt.DashLine)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(0.5)

        self.brush = QBrush(QColor(self.color))

    
    def setColor(self, color):
        self.color = color
        self.pen.setColor(QColor(self.color))
        self.brush.setColor(QColor(self.color))
        self.update()
        
    
    def setRadius(self, percentage_radius):
   
        self.radius = self.RADIUS*(percentage_radius/100)
        self.update()


    def movePoint(self, pos:QPointF):
        self.coor = pos
        self.setPos(pos)
          
  
    def boundingRect(self) -> QRectF:
        radius = self.radius - 1.499
        return QRectF(-radius, -radius,
                             2*radius, 2*radius)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
         
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)
          
