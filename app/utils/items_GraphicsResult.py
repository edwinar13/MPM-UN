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
from config import config_manager
import sys
import weakref
import math



class TextNoMpItem(QGraphicsItem):

    def __init__(self, node:str, coordinatesX:float, coordinatesY:float):        
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
                
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())
        self.node = f'MP{node}:'
        self.setTextResult()
        self.coordenates = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.coordenates)
        self.font = QFont("Ubuntu")
        self.font.setWeight(QFont.Bold)
        self.font.setPointSize(12)  # Increase the font size here
        
        self.font_value = QFont("Monospace")
        self.font_value.setWeight(QFont.Normal)
        self.font_value.setPointSize(11)  # Increase the font size here
        
        self.seprate_text = 8
        
        '''
        self.font.setCapitalization(QFont.AllUppercase)
        self.font.setLetterSpacing(QFont.AbsoluteSpacing, 1)
        '''

    def signalThemeChanged(self, theme: str):   
        if theme == "dark":
            color = QColor("#fff")
        else:
            color = QColor("#000")            
        self.pen = QPen(color)
        self.update()

    def newPos(self, pos:QPointF|QPoint):
        self.coordenates = pos
        self.setPos(pos)
        
    def setTextResult(self, text:str=""):
        self.text = f'{text}'
        self.update()
        
    def setSize(self, size:int):
        self.font.setPointSize(size)
        self.font_value.setPointSize(size-2)
        self.seprate_text = int(size*2/3)
        
        self.update()
        
    def boundingRect(self) -> QRectF:
        size = 0.1
        return QRectF(-size, -size,
                             2*size, 2*size)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        painter.setPen(self.pen)    
        painter.setFont(self.font)  
        
        # Calculate the width and height of the text
        font_metrics = QFontMetrics(self.font)
        node_width = font_metrics.horizontalAdvance(self.node)
        node_height = font_metrics.height()

        # Draw the text centered
        painter.drawText(QPointF(-node_width/2, -self.seprate_text ), self.node)
        #painter.drawText(QPointF(-node_width/2, -self.seprate_text - node_height/2), self.node)

        painter.setFont(self.font_value)   

        # Calculate the width and height of the text
        font_metrics_value = QFontMetrics(self.font_value)
        text_width = font_metrics_value.horizontalAdvance(self.text)
        text_height = font_metrics_value.height()

        # Draw the text centered
        painter.drawText(QPointF(-text_width/2, self.seprate_text ), self.text)
        #painter.drawText(QPointF(-text_width/2, self.seprate_text - text_height/2), self.text)
  
        '''
        painter.setPen(self.pen)    
        painter.setFont(self.font)         
        painter.drawText(QPointF(0, -self.seprate_text), self.node)
        painter.setFont(self.font_value)   
        painter.drawText(QPointF(0, self.seprate_text), self.text)
        '''

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
        self.coor = QPointF(height/2, -height/2)
        self.coor = QPointF(-width/2, -height/2)


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

    def __init__(self, radius, color_type_default, graphic_time, data_result, result_min, result_max, text_node: TextNoMpItem):
        QGraphicsItem.__init__(self)
        
 
         
        self.text_node = text_node
        self.text_node.setVisible(False)
        self.text_node.setZValue(100)
        
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
        self.shadow_effect.setOffset(20, 20)

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
        self.text_node.setSize(size_texts)
        
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
            
            '''
            hue: 0-359 >235
            saturation: 0-255
            value: 0-255
            if self.color_style == "Rojo-Azul":
                hue = int(1+((percent/100)*235))
                saturation = 255
                value = 255
            '''
            '''
            if self.color_style == "Rojo-Azul":
                hue = int(1+((percent/100)*298))
                saturation = 255
                value = 255
            '''
            if self.color_style == "Rojo-Azul":
                hue = int((1-(percent/100))*300)
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
            
        
        self.text_node.setTextResult(str(value_text))

    
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
            stop:0.0 rgba(255, 0, 0), 
            stop:0.2 rgba(255, 255, 0), 
            stop:0.4 rgba(0, 255, 0), 
            stop:0.6 rgba(0, 255,255), 
            stop:0.8 rgba(0, 0, 255)
            stop:1.0 rgba(255, 0, 255)

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
            self.text_node.newPos(self.coor)
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

            #self.text_value.setVisible(True)
            self.text_node.setVisible(True)
        else:
            #self.text_value.setVisible(False)
            self.text_node.setVisible(False)

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
        print("max, min", max, min)
        self.texts = []
        for i in range(5):
            self.texts.append({})
            number = min + (i*(max-min)/4)
            self.texts[i]['text'] = format_number(number)
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
            gradient.setColorAt(1.0, QColor(255, 0, 0, 255)) # rojo
            gradient.setColorAt(0.8, QColor(255, 255, 0, 255)) # amarillo
            gradient.setColorAt(0.6, QColor(0, 255, 0, 255)) # verde            
            gradient.setColorAt(0.4, QColor(0, 255,255, 255)  ) # cyan
            gradient.setColorAt(0.2, QColor(0, 0, 255, 255)) # azul
            gradient.setColorAt(0.0, QColor(255, 0, 255, 255)) # magenta
                       
        elif color_type == 2:
            gradient.setColorAt(1, QColor(0, 0, 0, 255)) # 
            gradient.setColorAt(0, QColor(255, 255, 255, 255))
        
        elif color_type == 3:
            print("color_type 3")
            gradient.setColorAt(1, QColor(255, 255, 255, 255))
            gradient.setColorAt(0, color)

        if  color_type == 4:
            print("color_type 4")
            
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
                 nodes, elements):
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
        
        self.elements = []

        for id_element in elements:
            element = elements[id_element]  
            p1 = QPointF(
                nodes[element[0]]['COORDINATES'][0],
                nodes[element[0]]['COORDINATES'][1]
                )
            p2 = QPointF(nodes[element[1]]['COORDINATES'][0], nodes[element[1]]['COORDINATES'][1])
            p3 = QPointF(nodes[element[2]]['COORDINATES'][0], nodes[element[2]]['COORDINATES'][1])
            p4 = QPointF(nodes[element[3]]['COORDINATES'][0], nodes[element[3]]['COORDINATES'][1])
            rectang = QRectF(p1, p3)
            self.elements.append(rectang)


   
        
        self.pen = QPen(QColor( self.color), self.width_border, Qt.SolidLine)
        #self.pen.setCosmetic(True)
        #self.pen.setWidthF(1.5)
   

    def boundingRect(self):
        return QRectF(self.x ,self.y ,self.width ,self.height )


    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)            
        #painter.drawLines(self.lines)
        painter.drawRects(self.elements)
        
class ItemResultLabelGridMeshBack(QGraphicsItem):

    WIDTH = 0.2
    COLOR = "#888"


    def __init__(self, scene, x, y, width, height, 
                nodes,
                nodes_boundary_top,
                nodes_boundary_bottom, 
                nodes_boundary_left, 
                nodes_boundary_right  ):
        QGraphicsItem.__init__(self)
        
        self.nodes = nodes 

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
        
        num_labels = min(10, len(nodes_boundary_top))
        step = len(nodes_boundary_top) // num_labels

        for i in range(0, len(nodes_boundary_top), step):
            top = nodes_boundary_top[i]
            xi = nodes[top]['COORDINATES'][0]
            yi = nodes[top]['COORDINATES'][1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi, yi + (line_label_dxy * 1.5))
            line = QLineF(p1, p2)
            self.lines.append(line)
            
            text_label = ItemResultTextLabel(text=f"{xi:.2f}",
                                            coordinatesX=xi,
                                            coordinatesY=yi,
                                            angle_degrees=0,
                                            alignment='TOP')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)
            
        # For nodes_boundary_bottom
        num_labels = min(10, len(nodes_boundary_bottom))
        step = len(nodes_boundary_bottom) // num_labels

        for i in range(0, len(nodes_boundary_bottom), step):
            bottom = nodes_boundary_bottom[i]
            xi = nodes[bottom]['COORDINATES'][0]
            yi = nodes[bottom]['COORDINATES'][1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi, yi - (line_label_dxy * 1.5))
            line = QLineF(p1, p2)
            self.lines.append(line)
            
            text_label = ItemResultTextLabel(text=f"{xi:.2f}",
                                            coordinatesX=xi,
                                            coordinatesY=yi,
                                            angle_degrees=0,
                                            alignment='BOTTOM')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)

        # For nodes_boundary_left
        num_labels = min(10, len(nodes_boundary_left))
        step = len(nodes_boundary_left) // num_labels

        for i in range(0, len(nodes_boundary_left), step):
            left = nodes_boundary_left[i]
            xi = nodes[left]['COORDINATES'][0]
            yi = nodes[left]['COORDINATES'][1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi - (line_label_dxy * 1.5), yi)
            line = QLineF(p1, p2)
            self.lines.append(line)
            
            text_label = ItemResultTextLabel(text=f"{yi:.2f}",
                                            coordinatesX=xi,
                                            coordinatesY=yi,
                                            angle_degrees=0,
                                            alignment='LEFT')
            text_label.setScale(text_height)
            scene.addItem(text_label)
            self.labes_text.append(text_label)

        # For nodes_boundary_right
        num_labels = min(10, len(nodes_boundary_right))
        step = len(nodes_boundary_right) // num_labels

        for i in range(0, len(nodes_boundary_right), step):
            right = nodes_boundary_right[i]
            xi = nodes[right]['COORDINATES'][0]
            yi = nodes[right]['COORDINATES'][1]
            p1 = QPointF(xi, yi)
            p2 = QPointF(xi + (line_label_dxy * 1.5), yi)
            line = QLineF(p1, p2)
            self.lines.append(line)
                
            text_label = ItemResultTextLabel(text=f"{yi:.2f}",
                                            coordinatesX=xi,
                                            coordinatesY=yi,
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


