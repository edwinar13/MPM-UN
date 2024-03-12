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

from utils.general_functions import format_number

import sys
import weakref
import math



class TextResultItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#555")
    FONT_SIZE = 5

    def __init__(self, text:str, coordinatesX, coordinatesY):
        QGraphicsItem.__init__(self)
        
        #self.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        self.item_type = self.TYPE
        self.color = self.COLOR
        self.text = str(text)
        self.position = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.position)
        self.pen = QPen(self.color)
        self.font = QFont("Times", self.FONT_SIZE)
        # centrar texto
        width = self.boundingRect().width()
        height = self.boundingRect().height()
        self.coor = QPointF(-width/2, -height/2)
        self.coor = QPointF(height/2, -height/2)


    def setColor(self, color):
        self.color = QColor(color)
        self.pen = QPen(self.color)
        
    def setSize(self, size):
        self.font = QFont("Times", size)


    def newPos(self, pos:QPointF|QPoint):       
        self.position = pos 
        self.setPos(pos)
        
    def setText(self, text):
        self.text = str(text)
        self.update()

    def boundingRect(self) -> QRectF:
        font_metrics = QFontMetrics(self.font)
        text_rect = font_metrics.boundingRect(self.text)
        text_rect.setHeight(font_metrics.ascent())
        return text_rect

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        painter.setPen(self.pen)
        painter.setFont(self.font)
        painter.scale(1, -1)
        painter.drawText(self.coor, self.text)
        
        
        

        
        

class ItemResultNode(QGraphicsItem):
    """color_type 1 o 2"""
    COLOR_1A = "#e8ca7b"
    COLOR_1B = "#a8821d"

    COLOR_2A = "#a89565"
    COLOR_2B = "#594c2b"
    
    signal_time_steps_changed = Signal(int)

    def __init__(self, radius, color_type_default, graphic_time, data_result, result_min, result_max, text_value:TextResultItem):
        QGraphicsItem.__init__(self)
        
 
        self.text_value = text_value
        self.text_value.setVisible(False)
        self.text_value.setColor("#333")
        self.text_value.setZValue(100)
        
        self.showLabel = False

        
        self.color_type_default = color_type_default
        self.radius = radius   
        self._time_view = 0
        self.__hue = 0
        
        '''
        self.max_sigXX = max_min[0]
        self.min_sigXX = max_min[1]
        '''
        
        self.data_result = data_result
        
        self.times = graphic_time
        self.no_data = len(self.times)
        self.coorX = data_result['CORX']
        self.coorY = data_result['CORY']
        
        
        self.sigXX = data_result['SIGXX']
        self.sigYY = data_result['SIGYY']
        self.sigXY = data_result['SIGXY']
        self.epsXX = data_result['EPSXX']
        self.epsYY = data_result['EPSYY']
        self.epsXY = data_result['EPSXY']
        
        #maximos
        self.d_sigXX = max(self.sigXX) - min(self.sigXX)
        self.d_sigYY = max(self.sigYY) - min(self.sigYY)
        self.d_sigXY = max(self.sigXY) - min(self.sigXY)
        self.d_epsXX = max(self.epsXX) - min(self.epsXX)
        self.d_epsYY = max(self.epsYY) - min(self.epsYY)
        self.d_epsXY = max(self.epsXY) - min(self.epsXY)
        

        self.result_min = result_min   
        self.result_max = result_max
        self.type_result = 'default'
        
        
        xo = self.coorX[0]
        yo = self.coorY[0]
        
        self.coor = QPointF(xo, yo)
        self.movePoint(self.coor)
        
        # Crear una sombra difusa
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#555"))
        self.shadow_effect.setBlurRadius(25)
        self.shadow_effect.setOffset(2, 2)

        '''
        # Aplicar la sombra al item
        self.setGraphicsEffect(self.shadow_effect)
        '''

        
        
        self.gradient = QRadialGradient(self.radius / 4, self.radius / 2,
                        self.radius, self.radius / 2, self.radius / 2)
        self.pen = QPen(QColor('#55555500'), 0, Qt.SolidLine)
        #por defecto
        self.color_style = "default"
        self.updateColorPoint()
        
                
        
        
    def regressTime(self, time_view):
        self._time_view = time_view
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))
        self.updateColorPoint()
        
        
    def stopTime(self):

        self._time_view = 0
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))
        self.updateColorPoint()

        
    def advanceTime(self,time_view):
        self._time_view = time_view  
        self.movePoint(QPointF(self.coorX[self._time_view], self.coorY[self._time_view]))
        
        self.updateColorPoint()
        
        
    #:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    def setColorStyle(self, color_style, hue):
        self.color_style = color_style
        self.__hue = hue
        self.updateColorPoint()
    
    def setSizePoints(self, size_points):
        self.radius = size_points
    
    def setSizeTexts(self, size_texts):
        self.text_value.setSize(size_texts)
        
    def setTypeResult(self, type_result):
        self.type_result = type_result
        self.updateColorPoint()
        
    def setVisibleValue(self, visible):
        self.showLabel = visible
        self.update()

        
              
        
        
        
    def updateColorPoint(self):       

        if self.type_result != 'default':
            type_result = self.type_result.upper()
            min_value = self.result_min[type_result]     
            max_value = self.result_max[type_result]
            value_data = self.data_result[type_result][self._time_view]
        else:
            min_value = -1
            max_value = 1
            value_data = 0            
        
        percent = self.evaluatePercent(value_data, (min_value, max_value))
                    
        if self.color_style == "default":
            if self.color_type_default != 1:
                color_a = self.COLOR_1A
                color_b = self.COLOR_1B
            else:
                color_a = self.COLOR_2A
                color_b = self.COLOR_2B          
                      
            self.gradient.setColorAt(0, QColor(color_a))
            self.gradient.setColorAt(1, QColor(color_b))
            self.brush = QBrush(self.gradient)   
        else:
            
                        
            if self.color_style == "Rojo-Azul":
                hue = int(1+((percent/100)*235))
                saturation = 255
                value = 255
            elif self.color_style == "Escala de grises":
                hue = 0
                saturation = 0
                value = int(1+((percent/100)*253))
            elif self.color_style == "Escala color":
                hue = self.__hue
                saturation = int(1+((percent/100)*253))
                value = 255

            color = QColor.fromHsv(hue, saturation, value)
            self.brush = QBrush(color)        
        
        if self.type_result != 'default':
            value_text = format_number(value_data)
        else:
            x = self.data_result['CORX'][self._time_view]
            y = self.data_result['CORY'][self._time_view]
            value_text = f"({round(x,2)}, {round(y,2)})"            
            
        
        self.text_value.setText(str(value_text))

    
    def evaluatePercent(self, value, range):

        # Obtener los extremos del range
        min_value, max_value = sorted(range)

        # Calcular el porcentaje
        if value < min_value:
            porcentaje = 0.0
        elif value > max_value:
            porcentaje = 100.0
        else:
            range_total = max_value - min_value
            porcentaje = ((value - min_value) / range_total) * 100

        return porcentaje
        
    
    
    
    def setStyle(self, type, percent=0):
        if type == 0:
            if self.color_type_default == 1:
                color_a = self.COLOR_1A
                color_b = self.COLOR_1B
            else:
                color_a = self.COLOR_2A
                color_b = self.COLOR_2B
            
            gradient = QRadialGradient(self.radius / 4, self.radius / 2,
                                    self.radius, self.radius / 2, self.radius / 2)
            self.gradient.setColorAt(0, QColor(color_a))
            self.gradient.setColorAt(1, QColor(color_b))
            
        if type == 1:

            '''                
            stop:0 rgba(255, 0, 0), 
            stop:0.25 rgba(255, 255, 0), 
            stop:0.50 rgba(0, 255, 0), 
            stop:0.75 rgba(0, 255,255), 
            stop:1 rgba(0, 0, 255));"
            '''            
            gradient = QLinearGradient(0, 0, 0, self.radius)
            gradient.setColorAt(0, QColor(255, 0, 0, 255))
            gradient.setColorAt(1, QColor(0, 255,255, 255))
            
            

        # Establecer el gradiente como el fondo de la vista
        self.brush = QBrush(gradient)
        self.pen = QPen(QColor('#55555500'), 0, Qt.SolidLine)
    
    
    
    
    
    
    
    

    def getCurrentTime(self):
        return self._time_view


    def movePoint(self, pos:QPointF):
        try:
            self.coor = pos
            self.setPos(pos)
            self.text_value.newPos(self.coor)
        except Exception as e:
            print("-->Error movePoint", e)
        
    def boundingRect(self):
        return QRectF(-self.radius,-self.radius,self.radius*2,self.radius*2)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        # Especifica el radio de las esquinas curvas (10 en este ejemplo, pero puedes ajustarlo a tu gusto)
        radius = self.radius
        painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)
        

        if self.showLabel:  

            self.text_value.setVisible(True)
        else:
            self.text_value.setVisible(False)

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
        self.setZValue(100) 

    def boundingRect(self):
        return QRectF(self.x - (self.width ), self.y - (self.height / 10), self.width * 3, self.height / 10)

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        # Especifica el radio de las esquinas curvas (10 en este ejemplo, pero puedes ajustarlo a tu gusto)
        
        painter.drawRoundedRect(self.boundingRect(), self.corner_radius, self.corner_radius)
        
class ItemResultColorBar(QGraphicsItem):
    
    RADIUS = 50
    FONTSIZE = 10
    
    def __init__(self,  x , y, height_text=0.1, width = 0.8, height = 1.5):
        QGraphicsItem.__init__(self)
        
        #se puede mover
        self.setFlag(QGraphicsItem.ItemIsMovable)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges)
        self.setZValue(-1)

        self.x = x
        self.y = y
        self.width = width*100
        self.height = height*100
        self.corner_radius = self.RADIUS * (width/50)
                
        self.rect_color_h= 100        
        self.rect_color = QRectF(self.x, self.y, self.rect_color_h/6, self.rect_color_h)   
        self.lines = [
            QLineF(self.x , self.y + (self.rect_color_h)*1, self.x + (self.rect_color_h/4), self.y+(self.rect_color_h)*1),
            QLineF(self.x , self.y + (self.rect_color_h)*0.75, self.x + (self.rect_color_h/4), self.y+(self.rect_color_h)*0.75),
            QLineF(self.x , self.y + (self.rect_color_h)*0.50, self.x + (self.rect_color_h/4), self.y+(self.rect_color_h)*0.50),
            QLineF(self.x , self.y + (self.rect_color_h)*0.25, self.x + (self.rect_color_h/4), self.y+(self.rect_color_h)*0.25),
            QLineF(self.x , self.y + (self.rect_color_h)*0.0, self.x + (self.rect_color_h/4), self.y+(self.rect_color_h)*0.0)
        ]     
        
        self.setText(1,0)       
        self.setColorType(1)
        # Establecer el gradiente como el fondo de la vista
                
        self.pen_bar1 = QPen(QColor("#555"))
        self.font_bar1 = QFont("Times", self.FONTSIZE-3, 0)
        
        self.pen = QPen(QColor("#222"))
        self.font = QFont("Times", self.FONTSIZE, QFont.Bold)
        self.text ="sigxx"
        
        self.cardColorBar()
        
    def setText(self, max, min):
        self.texts = []
        for i in range(5):
            self.texts.append({})
            self.texts[i]['text'] = str(max - (i*(max-min)/4))
            self.texts[i]['text'] = format_number(max - (i*(max-min)/4))
            self.texts[i]['coor'] = QPointF(self.x + (self.rect_color_h/4), self.y-(self.rect_color_h)*(i/4))
            
        
    def setTypeResult(self, type_result, max, min):
        self.text = str(type_result)      
        self.setText(max, min)      
        self.update()
        
    def setScaleView(self, scale):
        self.setScale(scale)
        self.width = self.width*scale
        self.height = self.height*scale
       
    def setColorType(self, color_type, color=QColor("#2d2df2")):
        gradient = QLinearGradient(0,0,0,self.rect_color_h)
        

        if  color_type == 1:
            gradient.setColorAt(1, QColor(255, 0, 0, 255))
            gradient.setColorAt(0.75, QColor(255, 255, 0, 255))
            gradient.setColorAt(0.5, QColor(0, 255, 0, 255))
            gradient.setColorAt(0.25, QColor(0, 255,255, 255)  )
            gradient.setColorAt(0, QColor(0, 0, 255, 255))
        elif color_type == 2:
            gradient.setColorAt(1, QColor(0, 0, 0, 255))
            gradient.setColorAt(0, QColor(255, 255, 255, 255))
        
        elif color_type == 3:
            gradient.setColorAt(1, QColor(255, 255, 255, 255))
            gradient.setColorAt(0, color)

            
        self.brush_rect_color = QBrush(gradient)
        self.pen_rect_color = QPen(QColor("#555"), 0, Qt.SolidLine)
        
        #update
        self.update()
                    
    def cardColorBar(self):
        
        # Establecer el gradiente como el fondo de la vista
        self.brush_background = QBrush(QColor("#fafafa"))
        self.pen_background = QPen(QColor("#aaa"), 0, Qt.SolidLine)
        
        # Crear una sombra difusa
        self.shadow_effect = QGraphicsDropShadowEffect()
        self.shadow_effect.setColor(QColor("#aaa"))
        self.shadow_effect.setBlurRadius(20)
        self.shadow_effect.setOffset(3, 3)

        # Aplicar la sombra al item
        self.setGraphicsEffect(self.shadow_effect)
        self.setZValue(100) 
        
    def boundingRect(self):

        return QRectF(self.x-(self.width/10) , self.y-(self.height/20) , self.width , self.height )

    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen_background)
        painter.setBrush(self.brush_background)

        # Especifica el radio de las esquinas curvas (10 en este ejemplo, pero puedes ajustarlo a tu gusto)
        
        painter.drawRoundedRect(self.boundingRect(), 3, 3)
        painter.drawRect
        
        painter.setPen(self.pen_rect_color)
        painter.setBrush(self.brush_rect_color)
        painter.drawRect(self.rect_color)
        
        
        for line in self.lines:
            painter.drawLine(line)
        
        painter.scale(1, -1)
        painter.setPen(self.pen_bar1)
        painter.setFont(self.font_bar1)
        
        for text in self.texts:
            painter.drawText(text['coor'], text['text'])
        
        painter.setPen(self.pen)
        painter.setFont(self.font)
        painter.drawText(self.x, self.y-120, self.text)
 
 
 
 
 
              
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


    def __init__(self, x, y, width, height,
                 points, quadrilaterals):
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
        
        self.quadrilaterals = []

        for quadrilateral in quadrilaterals:

            p1 = QPointF(points[quadrilateral[0]-1][0], points[quadrilateral[0]-1][1])
            p2 = QPointF(points[quadrilateral[1]-1][0], points[quadrilateral[1]-1][1])
            p3 = QPointF(points[quadrilateral[2]-1][0], points[quadrilateral[2]-1][1])
            p4 = QPointF(points[quadrilateral[3]-1][0], points[quadrilateral[3]][1])
            rectang = QRectF(p1, p3)
            self.quadrilaterals.append(rectang)


   
        
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )


    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        #painter.drawLines(self.lines)
        painter.drawRects(self.quadrilaterals)
        
class ItemResultLabelGridMeshBack(QGraphicsItem):

    WIDTH = 0.2
    COLOR = "#888"


    def __init__(self, scene, x, y, width, height, 
                points_boundary_top,
                points_boundary_bottom, 
                points_boundary_left, 
                points_boundary_right  ):
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


        text_height = len_min/500
        
        self.labes_text = []
        self.lines = []
        for top in points_boundary_top:
            xi = top[0]
            yi = top[1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi, yi + (line_label_dxy*1.5))
            line = QLineF(p1, p2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(xi),
                                      coordinatesX= xi,
                                      coordinatesY= yi,
                                      angle_degrees=0,
                                      alignment='TOP')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)
            
                       

        for bottom in points_boundary_bottom:
            xi = bottom[0]
            yi = bottom[1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi, yi - (line_label_dxy*1.5))
            line = QLineF(p1, p2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(xi),
                                      coordinatesX= xi,
                                      coordinatesY= yi,
                                      angle_degrees=0,
                                      alignment='BOTTOM')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)
            
        for left in points_boundary_left:
            xi = left[0]
            yi = left[1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi - (line_label_dxy*1.5), yi)
            line = QLineF(p1, p2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(yi),
                                      coordinatesX= xi,
                                      coordinatesY= yi,
                                      angle_degrees=0,
                                      alignment='LEFT')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)
            
        
        for right in points_boundary_right:
            xi = right[0]
            yi = right[1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi + (line_label_dxy*1.5), yi)
            line = QLineF(p1, p2)
            self.lines.append(line)
            text_label = ItemResultTextLabel(text=str(yi),
                                      coordinatesX= xi,
                                      coordinatesY= yi,
                                      angle_degrees=0,
                                      alignment='RIGHT')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)
            
               
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )


    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        painter.drawLines(self.lines)
    
    #reimplemetar setVisible
    def setVisible(self, visible: bool):      
        for labe_text in self.labes_text:
            labe_text.setVisible(visible) 
        QGraphicsItem.setVisible(self, visible)
        for child in self.childItems():
            child.setVisible(visible)
        '''
        '''

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
        self.position = pos     
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
          
