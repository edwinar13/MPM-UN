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

        self.anchored_lines =[]

        self.movePoint(self.coor)
        self.draw_rect_osnap = False
        self.isSelectedDraw = False
        self.showLabel = False


        self.pen_selected = QPen(QColor("#960b0f"), 0, Qt.DashLine)
        self.pen_selected.setCosmetic(True)
        self.pen_selected.setWidthF(0.5)

    def __str__ (self):
        return self.name
        return str(self.getData())
    
    def addAnchoredLine(self, line):
        """
        Agrega una línea a la lista de líneas ancladas.
        
        Args:
            line (LineItem): Objeto que representa la línea a agregar.
        """
        self.anchored_lines.append(line)
        self.anchored_lines=list(set(self.anchored_lines))

    def removeAnchoredLine(self, line):
        """
        Elimina una línea de la lista de líneas ancladas.
        
        Args:
            line (LineItem): Objeto que representa la línea a eliminar.
        """
        if line in self.anchored_lines:
            self.anchored_lines.remove(line)

    def movePoint(self, pos:QPointF):
        self.coor = pos
        self.setPos(pos)
        self.text_name.newPos(self.coor)
    def getId(self):
        return self.id
          
    def getData(self):

        anchored_lines_names = [linea.name for linea in self.anchored_lines]
        data = {
            "id":self.id,
            'name': self.name,
            'type': self.item_type,
            'coordinates': [self.coor.x(), self.coor.y()],
            'lines':anchored_lines_names
            }
        return data
    
    def getCoordinates(self):
        return self.coor

    def boundingRect(self) -> QRectF:
        radius = self.radius - 1.499
        return QRectF(-radius, -radius,
                             2*radius, 2*radius)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.draw_rect_osnap:
            painter.setPen(QPen(QColor("#34c3eb"), 0, Qt.SolidLine))
            painter.drawRect(-5,-5,10,10)
            self.draw_rect_osnap = False            

        if self.isSelectedDraw:
            self.pen_selected.setWidthF(1 / painter.transform().m11()) # m11()
            painter.setPen(self.pen_selected)
            painter.drawEllipse(-5, -5, 10, 10)

        else:
            painter.setPen(QPen(self.color, 0))
            painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)

        if self.name != "pointTemp" and self.showLabel:   
            self.text_name.newPos(self.coor)
            list_lines = []
            for line in self.anchored_lines:                
                list_lines.append(line.name)
            #self.text_name.text = ":{} - [{}]".format(self.id,)
            self.text_name.setVisible(True)
        else:
            self.text_name.setVisible(False)

        return

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
    WIDTH = 2
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
        
        #self.id_text = TextItem(str(self.id), self.center())
        #self.point_text = PointItem(1,"self.id", self.center())

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

        #shape__ = self.shape()
        #painter.drawPath(shape__)
        #return

class TriangleItem (QGraphicsItem):
    """
    TriangleItem es una clase que hereda de QGraphicsItem y representa un triángulo en una escena.

    Atributos:
        id (int): Numero del triángulo 
        points (list): Lista de puntos que forman el triángulo.
        type (str): Tipo de elemento gráfico (en este caso, siempre es "Triangle").
        color (Qt): Color con el que se dibujará el triángulo.        
        width (float): Ancho con el que se dibujará el triángulo.
    """
    TYPE = "Triangle"
    WIDTH = 2
    COLOR = Qt.black

       
    def __init__(self, id:int, points:list):
        QGraphicsItem.__init__(self)        
        self.id = id
        self.points = points
        self.item_type = self.TYPE
        self.color = self.COLOR
        self.width = self.WIDTH



    def __str__ (self):
        return "Triángulo No:{} puntos:{}  ".format(self.id, self.points)
    
    def center(self):
        # Calcula el centro del triángulo
        center_x = (self.points[0].x() + self.points[1].x() + self.points[2].x()) / 3
        center_y = (self.points[0].y() + self.points[1].y() + self.points[2].y()) / 3
        return QPointF(center_x, center_y)
    
    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        
        points = self.points
        path = QPainterPath()
        path.moveTo(points[0])
        path.lineTo(points[1])
        path.lineTo(points[2])
        path.lineTo(points[0])
        painter.drawPath(path)

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
        
        self.generatePath()
        
        self.pen = QPen(QColor(self.color), self.width, Qt.DashLine)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(0.5)
    
    def generatePath(self):
        self.path = QPainterPath()
        points = []
        
        for point in self.coordinates:
            point = QPointF(point[0], point[1])
            points.append(point)
        self.path.addPolygon(QPolygonF(points))

    def setColor(self, color):
        self.color = color
        self.pen.setColor(QColor(self.color))
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
    '''
    def __str__ (self):
        return self.name
    '''
    
    def setColor(self, color):
        self.color = color
        self.pen.setColor(QColor(self.color))
        self.brush.setColor(QColor(self.color))
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






