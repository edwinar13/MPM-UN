"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : PointItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*

contador = 0 

class TextItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#00ff55")
    HIGT = 0
    WIDTH = 0

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
        
    def __str__ (self):
        return "text: {}".format(self.text)

    def setColor(self, color):
        self.color = QColor(color)
        self.pen = QPen(self.color)


    def newPos(self, pos:QPointF|QPoint):
        self.coor = pos
        self.setPos(pos)

    def boundingRect(self) -> QRectF:
        h = self.higt
        w = self.width        
        return QRectF(-w/2, -h/2, w, h)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:

        if self.text != "temp":
            painter.setPen(self.pen)
            painter.drawText(QPointF(0, 0), self.text)
            

class TextFrameItem(TextItem):
    HIGT = 20
    def __init__(self, text: str, coordinatesX, coordinatesY):
        super().__init__(text, coordinatesX, coordinatesY)

        self.frame_pen = QPen(QColor("#333333"))
        self.frame_radius = 3
        self.gradient_start_color = QColor("#DDDDDD")
        self.gradient_end_color = QColor("#FFFFFF")
        self.gradient_start_color.setAlpha(200)  # Establecer transparencia al 50%
        self.gradient_end_color.setAlpha(200)  # Establecer transparencia al 50%
        
        self.extra_width = 1  # Ancho adicional del marco
        self.font = QFont("Arial", 12)  # Define la fuente del texto
        self.higt = self.HIGT
    
    def rectText(self):
        h= self.higt + 2
        font_metrics = QFontMetrics(self.font)
        text_width = font_metrics.horizontalAdvance(self.text)  # Ancho del texto
        w = text_width + 3 * self.extra_width  # Ancho ajustado
        return QRectF(-w/2, -h/2, w, h + 3)

    def boundingRect(self) -> QRectF:
        return QRectF(-1, -1, 2, 2)



    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        # Dibujar marco con esquinas curvas
        frame_rect = self.rectText()
        
        # Dibujar fondo degradado
        gradient = QLinearGradient(frame_rect.topLeft(), frame_rect.bottomLeft())
        gradient.setColorAt(0, self.gradient_start_color)
        gradient.setColorAt(1, self.gradient_end_color)
        painter.setBrush(QBrush(gradient))
        painter.drawRoundedRect(frame_rect.adjusted(1, 1, -1, -1), self.frame_radius - 1, self.frame_radius - 1)

        # Dibujar texto centrado
        #text_rect = self.boundingRect().adjusted(self.extra_width, 0, -self.extra_width, 0)
        text_rect = self.rectText().adjusted(self.extra_width, 0, -self.extra_width, 0)
        painter.setPen(self.pen)
        painter.drawText(text_rect, Qt.AlignCenter, self.text)


        

class PointItem(QGraphicsItem):
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
    RADIUS = 2.0
    COLOR = Qt.black


    def __init__(self,id, name:str, coordinatesX, coordinatesY, text_name:TextItem):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
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
            

      
        

class PointMeshBackItem(QGraphicsItem):


    SIZE = 3
    COLOR = QColor("#57cfcf")


    def __init__(self, name:str, coordinatesX, coordinatesY ):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
       

        self.name = name
        self.coor = QPointF(coordinatesX, coordinatesY)


        self.color = self.COLOR
        self.size = self.SIZE
        self.setPos(self.coor)
        self.isSelectedPointBlack = False

        
        self.pen = QPen(self.color, 0)

        self.pen_selected = QPen(QColor("#960b0f"), 0, Qt.SolidLine)
        self.pen_selected.setCosmetic(True)
        self.pen_selected.setWidthF(0.5)


        self.rect_view =QRectF(-self.size/2, -self.size/2, self.size, self.size)

    def __str__ (self):
        return "nodo: {}".format(self.name)


    def getPoint(self):
        return self.coor
    
    def getNode(self):
        return int(self.name)



    def boundingRect(self) -> QRectF:
        size = 0.01
        return QRectF(-size, -size,
                             2*size, 2*size)
    


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.isSelectedPointBlack:
            self.pen_selected.setWidthF(1 / painter.transform().m11()) # m11()
            painter.setPen(self.pen_selected)
            painter.drawRect(-3, -3, 6, 6)
            painter.setBrush(QBrush(QColor(Qt.red)))

            painter.drawRect(self.boundingRect())

        else:
            painter.setPen(self.pen)
            painter.drawRect(self.rect_view)
        return

class PointBoundaryTxItem(QGraphicsItem):


    SIZE = 6
    COLOR = QColor("#ff0000")


    def __init__(self, id:str, name:str, coordinatesX=1, coordinatesY=1, Tx=True, Ty = True ):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.id = id
        self.name = name
        self.coor = QPointF(coordinatesX, coordinatesY)
        
        self.Tx=Tx
        self.Ty=Ty



        self.color = self.COLOR
        self.size = self.SIZE
        self.setPos(self.coor)
        self.isSelected = False
        self.isSelectedBoundary = False

        
        self.pen = QPen(self.color, 0)
        self.brush = QBrush(QColor(self.color))
        self.pen_selected = QPen(QColor("#0ccc45"), 0, Qt.DashLine)
        self.brush_selected = QBrush(QColor("#0ccc45"))
        self.pen_selected.setCosmetic(True)
        self.pen_selected.setWidthF(0.5)

        pointsTx =[
            QPointF(0, 0),
            QPointF(0-(self.size), 0-(self.size/2)),
            QPointF(0-(self.size), 0+(self.size/2))
        ]

        pointsTy =[
            QPointF(0, 0),
            QPointF(0+(self.size/2), 0+(self.size)),
            QPointF(0-(self.size/2), 0+(self.size))
        ]

        self.pathTx = QPainterPath()
        self.pathTx.addPolygon(QPolygonF(pointsTx))
        self.pathTy = QPainterPath()
        self.pathTy.addPolygon(QPolygonF(pointsTy))
 

    def __str__ (self):
        return "boundary: {}".format(self.name)


    def getPoint(self):
        return self.coor


    def boundingRect(self) -> QRectF:
        size = 0.2
        return QRectF(-size, -size,
                             2*size, 2*size)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.isSelected or self.isSelectedBoundary:
            self.pen_selected.setWidthF(1 / painter.transform().m11()) # m11()
            pen = self.pen_selected
            brush=self.brush_selected
        else:
            pen = self.pen
            brush=self.brush
        painter.setBrush(brush)
        painter.setPen(pen)

        if self.Tx:
            painter.drawPath(self.pathTx)
        if self.Ty:
            painter.drawPath(self.pathTy)


    
    


class LineItem(QGraphicsItem):
    """
    LineItem es una clase que hereda de QGraphicsItem y representa una línea en una escena.
    
    Atributos:
        id (int): Numero único del elemento 
        name (str): Nombre de la línea.
        start_point (PointItem): Punto de inicio de la línea.
        end_point (PointItem): Punto final de la línea.
        type (str): Tipo de elemento gráfico (en este caso, siempre es "Line").
        color (Qt): Color con el que se dibujará la línea.        
        width (float): Ancho con el que se dibujará la línea.
        
        isSelectedDraw (bool): Indica si la línea está seleccionada en el momento.
        isSelectedMesh (bool): Indica si la línea está seleccionada para mallado.
        isActive (bool): Indica si la línea está activa en el momento.
        
    """
    TYPE = "Line"
    WIDTH = 5
    COLOR = Qt.black

    def __init__(self, id, name: str, start_point: PointItem, end_point: PointItem, text_name:TextItem):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        #self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges, True)
        self.id = id
        self.name = name
        self.item_type = self.TYPE
        self.start_point = start_point
        self.end_point = end_point
        self.text_name = text_name
        self.text_name.setVisible(False)
        self.text_name.setColor("#1482CA")
        
        self.color = self.COLOR
        self.width = self.WIDTH
        self.isSelectedDraw = False
        self.isSelectedMesh = False
        self.showLabel = False


    def __str__ (self):
        return self.name
    
    def center(self):
        return QPointF((self.start_point.x() + self.end_point.x()) / 2, (self.start_point.y() + self.end_point.y()) / 2)


    def shape(self):
        # Calcula la forma de la línea
        path = QPainterPath()
        path.moveTo(self.start_point.pos())
        path.lineTo(self.end_point.pos())
        # Crea un área de selección más grande que la línea para que sea más fácil de seleccionar
        stroker = QPainterPathStroker()
        stroker.setWidth(1) # Ajusta el ancho del área de selección
        return stroker.createStroke(path)

   

    def movePoint(self, pos:QPointF):
        self.coor = pos
        self.setPos(pos)
        self.text_name.newPos(self.center())
    
    def getId(self):
        return self.id
    
    def getData(self):
        data = {
            "id":self.id,
            'name': self.name,
            'type': self.item_type,
            'start_point': self.start_point.id,
            'end_point': self.end_point.id
            }
        return data
    
    def getPoints(self):
        return self.start_point, self.end_point 

    def boundingRect(self) -> QRectF:
        p1 = QPointF(self.start_point.pos().x(),self.start_point.pos().y())
        p2 = QPointF(self.end_point.pos().x(),self.end_point.pos().y())
        return QRectF(p1, p2)



    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:

        if self.isSelectedDraw:          
            painter.setPen(QPen(QColor("#960b0f"), 0, Qt.DashLine))

        elif self.isSelectedMesh:          
            painter.setPen(QPen(QColor("#1482CA"), 0, Qt.DashDotDotLine))

        else:            
            painter.setPen(QPen(self.color, 0))
       
        painter.drawLine(self.start_point.coor, self.end_point.coor)
        #painter.drawRect(self.boundingRect())


        if self.name != "lineTemp" and self.showLabel:   
            self.text_name.newPos(self.center())
            self.text_name.setVisible(True)
        else:
            self.text_name.setVisible(False)


class TriangleMeshItem(QGraphicsItem):
    """
    TriangleMeshItem es una clase que hereda de QGraphicsItem y representa un triangulo de malla en una escena.

    Atributos:
        id (int): Número único del elemento
        name (str): Nombre de la malla.
        color (Qt): Color con el que se dibujará la malla.        
        triangles (list): Lista de triángulos que componen la malla.
        width (float): Ancho con el que se dibujará la malla.
        isSelected (bool): Indica si la malla está seleccionada en el momento.
        isActive (bool): Indica si la malla está activa en el momento.

    """
    WIDTH = 0


    def __init__(self,id, name:str, color:str, coordinates:list):
        QGraphicsItem.__init__(self)
        self.id = id
        self.name = name
        self.color = color
        self.coordinates = coordinates
        self.width = self.WIDTH
        self.isSelected = False
        self.isActive = False
                

        self.pen = QPen()
        self.pen.setCosmetic(True)
        self.pen.setWidthF(1.5)
        self.brush = QBrush()

        self.generatePath()
        self.setColor(self.color)
    
    def generatePath(self):
        self.path = QPainterPath()
        points = []
        for point in self.coordinates:
            point = QPointF(point[0], point[1])
            points.append(point)        

        self.path.addPolygon(QPolygonF(points))

    def setColor(self, color):
        self.color = color
        color_q  = QColor(color)
        color_darker = color_q.darker(100)
        self.pen.setColor(color_darker)

        color_transparente = color_q
        color_transparente.setAlpha(200)#(0-255)
        self.brush = QBrush(color_transparente)
        self.update()


    def boundingRect(self):
        rect = self._triangleBoundingRect(self.coordinates)
        return rect



    def _triangleBoundingRect(self, points):
        # Calcula el rectángulo que envuelve un triángulo
        left = min(point[0] for point in points)
        top = min(point[1] for point in points)
        right = max(point[0] for point in points)
        bottom = max(point[1] for point in points)
        return QRectF(left, top, right - left, bottom - top)

    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)  
        painter.setBrush(self.brush) 
        painter.drawPath(self.path) 



class QuadrilateraLMeshItem(QGraphicsItem):
    """
    TriangleMeshItem es una clase que hereda de QGraphicsItem y representa un triangulo de malla en una escena.

    Atributos:
        id (int): Número único del elemento
        name (str): Nombre de la malla.
        color (Qt): Color con el que se dibujará la malla.        
        triangles (list): Lista de triángulos que componen la malla.
        width (float): Ancho con el que se dibujará la malla.
        isSelected (bool): Indica si la malla está seleccionada en el momento.
        isActive (bool): Indica si la malla está activa en el momento.

    """
    WIDTH = 0


    def __init__(self,id, name:str, color:str, coordinates:list):
        QGraphicsItem.__init__(self)
        self.id = id
        self.name = name
        self.color = color
        self.coordinates = coordinates

        self.width = self.WIDTH
        self.isSelected = False
        self.isActive = False
        

        
        self.pen = QPen()
        self.pen.setCosmetic(True)
        self.pen.setWidthF(1.5)
        self.brush = QBrush()

        self.generatePath()
        self.setColor(self.color)


        '''
        self.pen = QPen(QColor(self.color), self.width, Qt.DashLine)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(1.5)

        color_transparente = QColor(self.color)
        color_transparente.setAlpha(100)#(0-255)
        self.brush = QBrush(color_transparente)
        '''
    
    def generatePath(self):
        self.path = QPainterPath()
        points = []

        for point in self.coordinates:
            point = QPointF(point[0], point[1])
            points.append(point)
        points.append(QPointF(self.coordinates[0][0], self.coordinates[0][1]))
        self.path.addPolygon(QPolygonF(points))


    def setColor(self, color):        
        self.color = color
        color_q  = QColor(color)
        color_darker = color_q.darker(100)
        self.pen.setColor(color_darker)

        color_transparente = color_q
        color_transparente.setAlpha(200)#(0-255)
        self.brush = QBrush(color_transparente)
        self.update()



    def boundingRect(self):
        rect = self._triangleBoundingRect(self.coordinates)
        return rect



    def _triangleBoundingRect(self, points):
        # Calcula el rectángulo que envuelve un triángulo
        left = min(point[0] for point in points)
        top = min(point[1] for point in points)
        right = max(point[0] for point in points)
        bottom = max(point[1] for point in points)
        return QRectF(left, top, right - left, bottom - top)

    def paint(self, painter, option, widget):
        
        painter.setBrush(self.brush)        
        painter.setPen(self.pen)        
        painter.drawPath(self.path)   


class QuadrilateraLMeshBackItem(QGraphicsItem):
    """
    TriangleMeshItem es una clase que hereda de QGraphicsItem y representa un triangulo de malla en una escena.

    Atributos:
        id (int): Número único del elemento
        name (str): Nombre de la malla.
        color (Qt): Color con el que se dibujará la malla.        
        triangles (list): Lista de triángulos que componen la malla.
        width (float): Ancho con el que se dibujará la malla.
        isSelected (bool): Indica si la malla está seleccionada en el momento.
        isActive (bool): Indica si la malla está activa en el momento.

    """
    WIDTH = 0
    #COLOR0 = "#DDDDDD"
    #COLOR1 = "#555555"
    COLOR0 = "#a6ccff"
    COLOR1 = "#817e61"


    def __init__(self, color_style:int, coordinates:list, p1:PointMeshBackItem ,
                 p2:PointMeshBackItem, p3:PointMeshBackItem, p4:PointMeshBackItem ):
        QGraphicsItem.__init__(self)

        self.color_0 = self.COLOR0
        self.color_1 = self.COLOR1
        
        self.coordinates = coordinates
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4


        self.width = self.WIDTH
        self.isSelected = False
        self.isActive = False
        
        self.generatePath()
        

        ##ACA DEBERIA RECIBIR EL COLOR PERO DEL TEMA
        if color_style==1: 
            color_ =self.color_1
        else:
            color_ =self.color_0

        self.pen = QPen(QColor( color_), self.width, Qt.SolidLine)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(1.5)
    
    def generatePath(self):
        self.path = QPainterPath()
        points = [] 
        points.append(self.p1.getPoint())
        points.append(self.p2.getPoint())
        points.append(self.p3.getPoint())
        points.append(self.p4.getPoint())
        points.append(self.p1.getPoint())
        self.path.addPolygon(QPolygonF(points))

    def setColor(self, color_style):        
        if color_style==0:
            self.pen.setColor(QColor(self.color_0))
        elif color_style==1:
            self.pen.setColor(QColor(self.color_1))
        self.update()



    def boundingRect(self):
        rect = self._triangleBoundingRect(self.coordinates)
        return rect

    def _triangleBoundingRect(self, points):
        # Calcula el rectángulo que envuelve un triángulo
        left = min(point[0] for point in points)
        top = min(point[1] for point in points)
        right = max(point[0] for point in points)
        bottom = max(point[1] for point in points)
        return QRectF(left, top, right - left, bottom - top)

    def paint(self, painter, option, widget):
        
        painter.setPen(self.pen)        
        painter.drawPath(self.path)   
        
 




class RectMeshBackItem(QGraphicsRectItem):
 
    def __init__(self,  name:str, p1:QPointF, p2:QPointF):
        super(RectItem, self).__init__()
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''
        self.name = name
        self.p1 = p1
        self.p2 = p2        
       
        self.setRect(QRectF(self.p1, self.p2))
        self.isSelected = False


    
    def __str__ (self):
        return str(self.getData())

    def getName(self):
        return self.name

    
    def newPos(self, dx, dy):
        self.p1 = QPointF(self.p1.x()+dx, self.p1.y()+dy)
        self.p2 = QPointF(self.p2.x()+dx, self.p2.y()+dy)

    def getData(self):
        data = {
            'name': self.name,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return data
        


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        self.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))  

        if self.isSelected == True:
            self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))


        return super().paint(painter, option, widget)




class PointMaterialItem(QGraphicsItem):
   
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


class RectItem(QGraphicsRectItem):
    TYPE = "Rect"
    def __init__(self,  name:str, p1:QPointF, p2:QPointF):
        super(RectItem, self).__init__()
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''
        self.name = name
        self.item_type = self.TYPE
        self.p1 = p1
        self.p2 = p2        
       
        self.setRect(QRectF(self.p1, self.p2))
        self.isSelectedDraw = False
        self.isActive = False

    
    def __str__ (self):
        return str(self.getData())

    def getName(self):
        return self.name

    def getType(self):
        return self.TYPE
    
    def newPos(self, dx, dy):
        self.p1 = QPointF(self.p1.x()+dx, self.p1.y()+dy)
        self.p2 = QPointF(self.p2.x()+dx, self.p2.y()+dy)

    def getData(self):
        data = {
            'name': self.name,
            'type': self.item_type,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return data
        


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        self.setPen(QPen(QColor("#000000"), 0, Qt.SolidLine))                
        if self.isSelectedDraw == True:
            self.setPen(QPen(QColor("#AAAAAA"), 0, Qt.SolidLine))

  
        if self.isActive :
            painter.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))
            painter.drawRect(QRectF(self.p1, self.p2))
            #self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))
            self.isActive = False    
            

        return super().paint(painter, option, widget)

