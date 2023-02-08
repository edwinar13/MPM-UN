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
#import math
import weakref
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
from clases import class_projects




class PointItem(QGraphicsItem):
    """
    PointItem es una clase que hereda de QGraphicsItem y representa un punto en una escena.
    
    Atributos:
        name (str): Nombre del punto.
        p1 (QPointF): Coordenadas del punto.
        type (str): Tipo de elemento gráfico (en este caso, siempre es "Point").
        color (Qt): Color con el que se dibujará el punto.        
        radius (float): Radio con el que se dibujará el punto.
        draw_rect_osnap (bool): Indica si se debe dibujar un rectángulo para facilitar la selección del punto.

        isSelected (bool): Indica si el punto está seleccionado en el momento.
        isActive (bool): Indica si el punto está activo en el momento.
        
    """
    TYPE = "Point"
    RADIUS = 1.5
    COLOR = Qt.black

    def __init__(self, name:str, p1:QPointF):
        QGraphicsItem.__init__(self)
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        self.name = name
        self.type = self.TYPE
        self.p1 = p1

        self.color = self.COLOR
        self.radius = self.RADIUS

        self.movePoint(self.p1)
        self.draw_rect_osnap = False
        self.isSelected = False

    def __str__ (self):
        return str(self.getData())
        
    def movePoint(self, pos:QPointF|QPoint):
        self.p1 = pos
        self.setPos(pos)
    
    '''
    def getName(self):
        return self.name

    def getType(self):
        return self.TYPE
    '''
        
    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()]
            }
        return data


    def boundingRect(self) -> QRectF:        
        return QRectF(-self.radius, -self.radius,
                             2*self.radius, 2*self.radius)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.draw_rect_osnap:
            painter.setPen(QPen(QColor("#34c3eb"), 0, Qt.SolidLine))
            painter.drawRect(-5,-5,10,10)
            self.draw_rect_osnap = False
            

        if self.isSelected:
            #painter.setBrush(QBrush("#AAAAAA"))
            painter.setPen(QPen(QColor("#AAAAAA"), 0, Qt.DashLine))
            painter.drawEllipse(-2, -2, 4, 4)

        else:
            #painter.setBrush(QBrush(self.color))
            painter.setPen(QPen(self.color, 0))
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
        self.type = self.TYPE
        self.p1 = p1
        self.p2 = p2        
       
        self.setRect(QRectF(self.p1, self.p2))
        self.isSelected = False
        self.isActive = False
    def __str__ (self):
        return str(self.getData())

    def getName(self):
        return self.name

    def getType(self):
        return self.TYPE
    def newPos(self, dx, dy):
        print("2 dx:dy ", self.p1, self.p1)
        self.p1 = QPointF(self.p1.x()+dx, self.p1.y()+dy)
        self.p2 = QPointF(self.p2.x()+dx, self.p2.y()+dy)
        print("1 dx:dy ", self.p1, self.p1)

    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return data
        


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        self.setPen(QPen(QColor("#000000"), 0, Qt.SolidLine))                
        if self.isSelected == True:
            self.setPen(QPen(QColor("#AAAAAA"), 0, Qt.SolidLine))

  
        if self.isActive :
            painter.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))
            painter.drawRect(QRectF(self.p1, self.p2))
            #self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))
            self.isActive = False    
    
        return super().paint(painter, option, widget)

class RectItem2(QGraphicsItem):
    TYPE = "Rect"
    def __init__(self,  name:str, p1:QPointF, p2:QPointF):
        QGraphicsItem.__init__(self)
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''
        self.name = name
        self.type = self.TYPE
        self.p1 = p1
        self.p2 = p2 
        self.pen = None
        self.brush = None
        self.rect = None


        self.newPos(self.p1)           
        self.setRect(QRectF(self.p1, self.p2))

        self.isSelected = False
        self.isActive = False
        
    def __str__ (self):
        return str(self.getData())

    def newPos(self, pos:QPointF|QPoint):
        self.setPos(pos)

    def setRect(self, rect:QRectF|QRect):
        print(rect, rect.size(), rect.x())
        rect.width()


        self.rect =QRectF(0,0,rect.width(),rect.height())



    def setPen(self, pen:QPen):
        self.pen=pen

    def setBrush(self, brush:QBrush):
        self.brush = brush
        
    def getName(self):
        return self.name

    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return 
        
    def getType(self):
        return self.TYPE
    
    def boundingRect(self) -> QRectF:
        return QRectF(self.p1, self.p2)


    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:

        #self.setPen(QPen(QColor("#000000"), 0, Qt.SolidLine))

        if self.isSelected:
            painter.setPen(QPen(QColor("#AAAAAA"), 0, Qt.DashLine))
            painter.setBrush(QBrush("#AAAAAA"))
            painter.drawRect(self.rect)
        else: 
            painter.setPen(self.pen)
            painter.drawRect(self.rect)

  
        if self.isActive :

            painter.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))
            painter.drawRect(QRectF(self.p1, self.p2))
            #self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))
            self.isActive = False
      
        #return super().paint(painter, option, widget)


class LineItem(QGraphicsLineItem):
    TYPE = "Line"
    def __init__(self, name:str, p1:QPointF, p2:QPointF):
        super(LineItem, self).__init__()
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''        
        self.name = name
        self.type = self.TYPE
        self.p1 = p1
        self.p2 = p2

        self.setLine(QLineF(self.p1, self.p2))
        self.isSelected = False
        self.isActive = False

    def __str__ (self):
        return str(self.getData()) 

    def getName(self):
        return self.name

    def getType(self):
        return self.TYPE

    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return data
    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        self.setPen(QPen(QColor("#000000"), 0, Qt.SolidLine))
        
        if self.isSelected:
            self.setPen(QPen(QColor("#AAAAAA"), 0, Qt.SolidLine))

        if self.isActive :
            painter.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))
            painter.drawLine(QLineF(self.p1, self.p2))
            #self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))
            self.isActive = False 
            
        
        return super().paint(painter, option, widget)

class PointItem1(QGraphicsItem):
    TYPE = "Point"
    RADIUS = 1.5
    def __init__(self, name:str, p1:QPointF):
        QGraphicsItem.__init__(self)
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        self.name = name
        self.type = self.TYPE
        self.p1 = p1
        self.newPos(self.p1)

        self.color = Qt.black
        self.draw_rect_osnap = False
        self.radius = self.RADIUS

        self.isSelected = False
        self.isActive = False

    def __str__ (self):
        return str(self.getData())
        
    def newPos(self, pos:QPointF|QPoint):
        self.p1 = pos
        self.setPos(pos)
    
    def setRadius(self, r):
        self.radius = r
    
    def getName(self):
        return self.name
        
    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()]
            }
        return data

    def getType(self):
        return self.TYPE

    def boundingRect(self) -> QRectF:
        adjust = 0
        return QRectF(-0.0009 - adjust, -0.0009 - adjust,
                             0.0019 + adjust, 0.0019 + adjust)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.draw_rect_osnap:
            painter.setPen(QPen(QColor("#34c3eb"), 0, Qt.SolidLine))
            painter.drawRect(-5,-5,10,10)
            self.draw_rect_osnap = False
        '''
        '''
        if self.isSelected:
            #painter.setBrush(QBrush("#AAAAAA"))
            painter.setPen(QPen(QColor("#AAAAAA"), 0, Qt.DashLine))
            painter.drawEllipse(-2, -2, 4, 4)

        else:
            #painter.setBrush(QBrush(self.color))
            painter.setPen(QPen(self.color, 0))
            painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)
    '''
    def type(self):
        return PointItem.Type
    '''

class LineItem2(PointItem):



    TYPE = "Line"

    def __init__(self, name:str, p1:QPointF, p2:QPointF):
        super(LineItem, self).__init__()
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''        
        self.name = name
        self.type = self.TYPE
        self.p1 = p1
        self.p2 = p2

        self.setLine(QLineF(self.p1, self.p2))
        self.isSelected = False
        self.isActive = False

    def __str__ (self):
        return str(self.getData()) 

    def getName(self):
        return self.name

    def getType(self):
        return self.TYPE

    def getData(self):
        data = {
            'name': self.name,
            'type': self.type,
            'p1': [self.p1.x(), self.p1.y()],
            'p2': [self.p2.x(), self.p2.y()]
            }
        return data

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        self.setPen(QPen(QColor("#000000"), 0, Qt.SolidLine))
        
        if self.isSelected:
            self.setPen(QPen(QColor("#AAAAAA"), 0, Qt.SolidLine))

        if self.isActive :
            painter.setPen(QPen(QColor("#ebdd21"), 0, Qt.SolidLine))
            painter.drawLine(QLineF(self.p1, self.p2))
            #self.setPen(QPen(QColor("#3AA3AA"), 0, Qt.SolidLine))
            self.isActive = False 
            
        
        return super().paint(painter, option, widget)

class Node(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1

    def __init__(self, graphWidget):
        QGraphicsItem.__init__(self)

        self.graph = weakref.ref(graphWidget)
        # print(self.graph,">>>>",graphWidget)
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
            
        if qAbs(xvel) < 0.1 and qAbs(yvepathl) < 0.1:
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

class AdminScene():
    def __init__(self,scene:QGraphicsScene) -> None:

                
        self.undo_stack = None
        self.__projectActual= None
        self.__scene= scene

        self.list_points = {}
        self.list_lines = {}
        self.list_rects = {}
        self.no_items = 0
 
    def setUndoStack(self, undo_stack):
        self.undo_stack = undo_stack

    def addCommand(self,item):
        add_command = AddCommand(self, self.__scene, item)
        self.undo_stack.push(add_command) 

    def removeCommand(self,item):
        remove_command = RemoveCommand(self, self.__scene, item)
        self.undo_stack.push(remove_command)

    def moveCommand(self,item,dx,dy):
        move_command = MoveCommand(self, self.__scene, item, dx, dy)
        self.undo_stack.push(move_command) 
         
    def initDrawItemsSceneProject(self, project:class_projects.Project):
        """Asigna el proyecto actual a admin y actualiza los items del proyecto en la escena.

        Args:
            project(Project): Objeto de tipo del proyecto actual
        """ 
        self.__projectActual = project  
        self.__setDbAttributes()
        self.__setDrawItems()
    
    def __setDbAttributes(self):
        """ Recupera información de la base de datos del proyecto y los asigna a los atributos
        
        Args:
            project(Project): Objeto de tipo del proyecto actual
        """ 
        
        # Obtiene los datos db del proyecto actual
        db_project = self.__projectActual.db_project
        data_items_draw = db_project.selectItemDrawDB()

        self.no_items=data_items_draw["NOITEMS"]
        self.list_points=data_items_draw["PUNTOS"]
        self.list_lines=data_items_draw["LINEAS"]
        self.list_rects=data_items_draw["RECTANGULOS"]


    def __setDrawItems(self):
        """ Recupera información de los atributos y dibuja los items """
        self.__scene.clear()
        self.__scene.drawElementTemp()
        self.__scene.update()

        for point in self.list_points:
            name = self.list_points[point]["name"]
            x = self.list_points[point]["p1"][0]
            y = self.list_points[point]["p1"][1]
            p = PointItem(name,QPoint(x,y))  
            self.__scene.addItem(p)

        for line in self.list_lines:
            name = self.list_lines[line]["name"]
            x1 = self.list_lines[line]["p1"][0]
            y1 = self.list_lines[line]["p1"][1]
            x2 = self.list_lines[line]["p2"][0]
            y2 = self.list_lines[line]["p2"][1]
            p = LineItem(name,QPoint(x1,y1),QPoint(x2,y2))  
            p.setPen(QPen(QColor(Qt.black),0))
            self.__scene.addItem(p)

        for rect in self.list_rects:
            name = self.list_rects[rect]["name"]
            x1 = self.list_rects[rect]["p1"][0]
            y1 = self.list_rects[rect]["p1"][1]
            x2 = self.list_rects[rect]["p2"][0]
            y2 = self.list_rects[rect]["p2"][1]
            p = RectItem(name,QPoint(x1,y1),QPoint(x2,y2))  
            p.setPen(QPen(QColor(Qt.black),0))
            self.__scene.addItem(p)


    
    def updateListItems(self, type_update:str, item:PointItem|LineItem|RectItem):

        type_item = item.getData()["type"]
        if type_update == "DELETE":
            if  type_item == "Point":
                self.list_points.pop(item.getData()["name"])
            elif  type_item == "Line":
                self.list_lines.pop(item.getData()["name"])
            elif type_item == "Rect":
                self.list_rects.pop(item.getData()["name"])

        elif type_update == "ADD":
            if  type_item == "Point":
                self.list_points[item.getData()["name"]] = item.getData()
            elif  type_item == "Line":
                self.list_lines[item.getData()["name"]] = item.getData()
            elif type_item == "Rect":
                self.list_rects[item.getData()["name"]] = item.getData()
                
        else:            
            return
        
        #actualizar db
        '''
        self.__projectActual.db_project.updateItemDrawDB(
            self.no_items,
             self.list_points, 
             self.list_lines,
             self.list_rects)
        '''
    
class AddCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, item:PointItem):
        super(AddCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.item = item
        print(item)
        scene.update()
        self.setText("add -> {}".format(self.item.getData()["type"]))

    def undo(self):
        self.graphics_scene.removeItem(self.item)
        self.graphics_scene.update()
        self.admin.updateListItems("DELETE",self.item)
        #self.admin.list_points.pop(self.item.getName())
      
    def redo(self):
        self.graphics_scene.addItem(self.item)
        self.graphics_scene.clearSelection()
        self.graphics_scene.update()
        self.admin.updateListItems("ADD",self.item)
        #self.admin.list_points[self.item.getName()] = self.item.__dict__

class RemoveCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, item:PointItem):
        super(RemoveCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.item = item
        scene.update()
        self.setText("del -> {}".format(self.item.getData()["name"]))

    def redo(self):
        self.graphics_scene.removeItem(self.item)
        self.graphics_scene.update()
        self.admin.updateListItems("DELETE",self.item)
        #self.admin.list_points.pop(self.item.getName())
      
    def undo(self):
        self.graphics_scene.addItem(self.item)
        self.graphics_scene.clearSelection()
        self.graphics_scene.update()
        self.admin.updateListItems("ADD",self.item)
        #self.admin.list_points[self.item.getName()] = self.item.__dict__

class MoveCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, item:PointItem, dx, dy):
        super(MoveCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.item = item
        self.dx = dx
        self.dy = dy
        scene.update()
        self.setText("move -> {}".format(self.item.getData()["type"]))

    def redo(self):
        

        p1 =self.item.p1
        self.pos = QPointF(p1.x()+self.dx, p1.y()+self.dy)
        self.item.movePoint(self.pos)

        #self.graphics_scene.removeItem(self.item)
        self.graphics_scene.update()
        #self.admin.updateListItems("DELETE",self.item)
        print()
      
    def undo(self):

        #self.graphics_scene.addItem(self.item)
        #self.graphics_scene.clearSelection()
        p1 =self.item.p1
        self.pos = QPointF(p1.x()-self.dx, p1.y()-self.dy)
        self.item.movePoint(self.pos)

        self.graphics_scene.update()
        #self.admin.updateListItems("ADD",self.item)


















# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►




















class GraphicsViewDraw (QGraphicsView):
    signal_coor_mouse = Signal(list)
    signal_main_view = Signal(str)
    signal_end_draw_geometry = Signal()
    


    def __init__(self,parent):
        super(GraphicsViewDraw, self).__init__(parent) 

        #self.setCursor(Qt.BlankCursor)
        #print(self.cursor())
        
        self.setRenderHints(QPainter.Antialiasing | QPainter.SmoothPixmapTransform)   # este se ve mejor las lineas probar    
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse) # este realiza zoom en el mause solo cuando hay barras de dezplazamiento
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
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
            color_background = "#888888"
            self.color_grid="#777777"
            self.color_axis_x="#742427"
            self.color_axis_y="#C8CC8E"
            self.color_crosshair_draw="#000000"
            self.color_crosshair="#555555"
            self.color_pick_box ="#555555"
            
        elif index == 2:
            color_background = "#333333"    
            self.color_grid="#313A39"
            self.color_axis_x="#742427"
            self.color_axis_y="#6A6C48"
            self.color_crosshair_draw="#FFFFFF"
            self.color_crosshair="#AAAAAA"
            self.color_pick_box ="#AAAAAA"

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
            self.setDragMode(self.ScrollHandDrag)
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

        super(GraphicsViewDraw, self).mousePressEvent(event)

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
        super(GraphicsViewDraw, self).mouseMoveEvent(event)

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
            self.update()

        if event.button() == Qt.MiddleButton:
            self.setDragMode(self.NoDrag)
            self.viewport().setCursor(Qt.BlankCursor)

        '''
        #:::::::::::: Forma 2 cuando se ve toda la escena ::::::::::::
        self.start_pos = None        
        self.setCursor(Qt.BlankCursor)
        self.scene().mode_crosshair_pick_box = True
        self.update()
        '''

        super(GraphicsViewDraw, self).mouseReleaseEvent(event)

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
        
        return super(GraphicsViewDraw, self).drawBackground(painter, rect)

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
        
        super(GraphicsViewDraw, self).drawForeground(painter, rect)

    def zoomWindow(self, state):
        if state == True:
            self.isZoomWindow = True  
            self.viewport().setCursor(Qt.UpArrowCursor)
            self.isModeCrosshairPickbox = False 
        else:
            self.signal_end_draw_geometry.emit()
            self.setDragMode(self.NoDrag)
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



















# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►
# ☼  ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►► ►►►

















class GraphicsSceneDraw (QGraphicsScene): 
    signal_next_point = Signal(int)
    def __init__(self):
        super(GraphicsSceneDraw, self).__init__()
        # Atributos
        self.grid_spacing = 50

        self.admin = AdminScene(self)

        #Atributos para ayudas de dibujo
        self.mode_ortho = False
        self.mode_osnap  = False
        self.rect_pick_box = None
        self.mode_snap_grid = False
        self.snap_grid_adaptative  = False
        self.snap_grid_spacing = 10
        
        #Atributos para dibujo
        self.isDrawLine = False
        self.isDrawRectangle = False
        self.isDrawPoint = False
        self.isDrawPolyline = False  

        self.isErase = False
        self.isMove = False          
        self.isCopy = False
        self.isRotate = False
        self.p1_select = None
        self.p2_select = None
        self.selected_items = []


        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None
        self.point_init = None
        self.vertex = 0
        
        self.isSelect = False 

        self.isPan = False

        #***************************************************** 
        self.figura_inicial_borrar()
        #*****************************************************
        self.drawElementTemp()

    ###############################################################################
	# :::::::::::::::::::::          OTROS MÉTODOS           ::::::::::::::::::::::
	############################################################################### 

    def drawElementTemp(self):
        #elementos temporales
        self.point_temp = PointItem("pointTemp",QPoint(0,0))          
        #self.point_temp.setRadius(2)
        self.addItem(self.point_temp)
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



    def setStyleScene(self, index):    
        """Establece el estilo de la escena.

        args:
            index(int): index del estilo

        """  
        #*************************************************************************
        #self.line_temp.setPen(QPen(QColor(self.color_element_temp),0,Qt.DashLine, Qt.RoundCap, Qt.RoundJoin))
        #print(self.sceneRect())
        #self.rect_scene.setRect(self.sceneRect())
        #*************************************************************************
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
    
        if  self.isMove or self.isCopy or self.isErase or self.isRotate:
            if self.isSelect: 
                '''establece el punto inicial para selección de área'''
                self.p1_select = event.scenePos()
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.p1_select))
                self.rect_select_temp.setVisible(True)
                print("Es isSelect")

            else:

                if self.point_vertex_ant == None:
                    pass
                    self.isDrawLine=True
                    cancel_point = self.drawGeometry(self.point_vertex)

                else:
                    pass
                    #self.isDrawLine=True
                    #cancel_point = self.drawGeometry(self.point_vertex, self.point_vertex_ant)
                    
                #if not cancel_point:
                #    self.point_vertex_ant = self.point_vertex

                #self.p1_select = event.scenePos()
                print(self.point_vertex)
                print(self.point_vertex_init)
                print("NO es isSelect")


        #se establece el punto inicial para dibujo 
        elif event.button() == Qt.LeftButton and not self.isPan:   
            #::::::::::::  punto  ::::::::::::::::
            if self.isDrawPoint: 
                self.drawGeometry(self.point_vertex)  

            #::::::::::::  linea  ::::::::::::::::
            if self.isDrawLine: 
                if self.point_vertex_ant == None:
                    cancel_point = self.drawGeometry(self.point_vertex)

                else:
                    cancel_point = self.drawGeometry(self.point_vertex, self.point_vertex_ant)

                if not cancel_point:
                    self.point_vertex_ant = self.point_vertex

            #::::::::::::  rectangulo  ::::::::::::::::
            if self.isDrawRectangle: 
                if self.point_vertex_ant == None:

                    cancel_point = self.drawGeometry(self.point_vertex)
                    
                    if not cancel_point:
                        self.point_vertex_ant = self.point_vertex
                else:
                    cancel_point = self.drawGeometry(self.point_vertex, self.point_vertex_ant)
                    if not cancel_point:
                        self.point_vertex_ant = None
                        self.point_vertex = None
                        self.rectangle_temp.setVisible(False)



        super(GraphicsSceneDraw, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        self.point_vertex = event.scenePos()


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
        

        if self.isMove or self.isCopy or self.isErase or self.isRotate:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)
            if self.p1_select != None:
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.point_vertex))
                x1 = self.p1_select.x()
                x2 = self.point_vertex.x()
                if x1 > x2:
                    self.rect_select_temp.setBrush(self.color_select_mode1)
                    #items_ = self.items(QRectF(self.p1_select, self.point_vertex),mode=Qt.IntersectsItemShape)
                else:
                    self.rect_select_temp.setBrush(self.color_select_mode2)
                    #items_ = self.items(QRectF(self.p1_select, self.point_vertex),mode=Qt.ContainsItemShape)
                return

                if self.rect_select_temp in items_:
                    items_.remove(self.rect_select_temp)                    

                if len(items_) > 0:
                    for item in items_:
                        item.isActive = True

            return            
        

        #::::::::::::  punto  ::::::::::::::::
        if self.isDrawPoint:  
            self.drawGeneral(self.point_vertex)

        #::::::::::::  Linea  ::::::::::::::::
        if self.isDrawLine:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)
        
        #::::::::::::  Rectangulo  ::::::::::::::::
        if self.isDrawRectangle:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)


        super(GraphicsSceneDraw, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:   
        if  (self.isMove or self.isCopy or self.isErase or self.isRotate) and self.p1_select != None:
            self.p2_select = event.scenePos()
            
            x1 = self.p1_select.x()
            x2 = self.p2_select.x()

            if self.p1_select==self.p2_select:
                items = self.items(self.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.items(QRectF(self.p1_select, self.p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.items(QRectF(self.p1_select, self.p2_select),mode=Qt.ContainsItemShape)

            self.rect_select_temp.setRect(0,0,0,0)
            self.rect_select_temp.setVisible(False)

            for item in items:                
                item.isSelected = True
                if not (item in self.selected_items):
                    self.selected_items.append(item)

            self.p1_select = None
            self.p2_select = None
        return                  
        super(GraphicsSceneDraw, self).mouseReleaseEvent(event)

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
        
        super(GraphicsSceneDraw, self).drawBackground(painter, rect)

    def drawForeground(self, painter: QPainter, rect: QRectF | QRect) -> None:
        """ Evento para dibujar en el primer plano, se dibuja las fechas
        del origen, punta de mira y la caja de selección que sigue al ratón """
        super(GraphicsSceneDraw, self).drawForeground(painter, rect)
    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS PARA DIBUJO     ::::::::::::::::::::
	############################################################################### 
    def endDrawGeometry(self):
        self.isDrawPoint = False                    
        self.isDrawLine = False
        self.isDrawPolyline = False
        self.isDrawRectangle = False
        self.isErase = False
        self.isMove = False          
        self.isCopy = False
        self.isRotate = False
        self.isDrawGeometry = False

        self.point_temp.setVisible(False)
        self.line_temp.setVisible(False)
        self.rectangle_temp.setVisible(False)
        self.rect_select_temp.setVisible(False)


        #self.graphicsScene_draw.mode_crosshair = False  
        #self.signal_end_draw_geometry.emit()

        self.p1_select = None
        self.p2_select = None
        for item in self.selected_items:
            item.isSelected = False
        self.selected_items = []
        
        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None

        if self.vertex == 1 and self.point_init != None:
            self.removeItem(self.point_init)
        self.point_init = None
        self.vertex = 0

    
    def initDrawGeometry(self):
        self.isDrawGeometry = True
        #self.graphicsScene_draw.mode_crosshair =True
        #self.signal_end_draw_geometry.emit()        
        self.vertex = 0
        #self.update()

    def drawPointScene(self):        
        self.initDrawGeometry()
        self.isDrawPoint = True

    def drawLineScene(self):
        self.isDrawLine = True
        self.initDrawGeometry()
    
    def drawPolylineScene(self):   
        self.isDrawPolyline = True
        self.initDrawGeometry()
    
    def drawRectangleScene(self):
        self.isDrawRectangle = True
        self.initDrawGeometry()
        
    

    def drawMoveItemScene(self):
        self.isMove = True  
        return
        print("Move:", self.admin.list_points)

    def drawCopyItemScene(self):
        self.isCopy = True  
        return
        print("copy:", self.admin.undo_stack.id)

    def drawRotateItemScene(self):
        self.isRotate = True  
        return

    def drawEraseItemScene(self):
        self.isErase = True
        return
        self.initDrawGeometry()


    def drawTransform (self, transformation=None):



        if transformation == None:
            return
        elif transformation == "erase":
            for selected_item in self.selected_items:
                #self.removeItem(selected_item)                
                self.admin.removeCommand(selected_item)
            
            #self.endDrawGeometry()
        elif transformation == "move":

            dx=10
            dy=10

            for selected_item in self.selected_items:
                self.admin.moveCommand(selected_item, dx,dy)
                

        elif transformation == "copy":
            return
        

    def drawGeneral(self, p1=None, p2=None):
        if p1 == None:
            return

        if self.isDrawPoint:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)

        if self.isDrawLine or self.isMove:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.line_temp.setVisible(True)
                self.line_temp.setLine(QLineF(p1,p2)) 

        if self.isDrawRectangle:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.rectangle_temp.setVisible(True)
                self.rectangle_temp.setRect(QRectF(p1,p2)) 


    def drawGeometry(self, p1:QPointF, p2=None) -> bool:
        if p1 == None:
            return

        items = self.items(p1)
        cancel_point = False

        # verifica si el punto esta por fuera de los limites
        if not self.pointInRect(p1,self.sceneRect()):
            cancel_point = True
            return cancel_point

        #verifica si hay puntos existentes
        existin_point = None
        for item in items:
            if type(item) == PointItem:

                if item.getData()["name"] != "pointTemp":
                    existin_point = item

        #Verifica si los dos puntos forman un rectangulo
        if self.isDrawRectangle and p2 != None:
            if p1.x() == p2.x() or p1.y() == p2.y():
                cancel_point = True
                return cancel_point

        #print("<<>>>",item.getName())        
        
        #::::::::::::  punto  ::::::::::::::::
        if self.isDrawPoint :  
            no_items = (len(self.items()))-2    
            if  existin_point != None:
                cancel_point = True
                return cancel_point
            elif  self.isDrawGeometry == True:                
                new_point = PointItem(f"POINT#{no_items}",p1)
                #self.addItem(new_point)
                self.admin.addCommand(new_point)
                return cancel_point

        #::::::::::::  linea  ::::::::::::::::
        if self.isDrawLine: 
            if self.vertex==0:
                self.point_vertex_init = QPointF(p1)
                self.signal_next_point.emit(self.vertex)
                self.vertex += 1

            no_items = (len(self.items()))-2
            if  self.isDrawGeometry == True and existin_point == None:                
                new_point = PointItem(f"POINT#{no_items}",p1)
                #self.addItem(new_point)
                self.admin.addCommand(new_point)
                self.point_init = new_point
                #print(new_point.getName())
            
            if p2 != None and not p1==p2:
                new_line = LineItem(f"LINE#{no_items}",p2,p1)
                new_line.setPen(QPen(QColor(Qt.black),0))
                #self.addItem(new_line)
                self.admin.addCommand(new_line)
                #print(new_line.getName())
                self.signal_next_point.emit(self.vertex)
                self.vertex += 1

            return cancel_point

        #::::::::::::  rectangulo  ::::::::::::::::
        if self.isDrawRectangle: 


            if self.vertex==0:
                self.point_vertex_init = QPointF(p1)
                self.signal_next_point.emit(self.vertex)
                self.vertex += 1

            no_items = (len(self.items()))-2

            if  self.isDrawGeometry == True and existin_point == None:                
                new_point = PointItem(f"POINT#{no_items}",p1)
                #self.addItem(new_point)
                self.admin.addCommand(new_point)
                self.point_init = new_point
                #print(new_point.getName())
            
            if p2 != None and not p1==p2:
                new_rect = RectItem(f"RECT#{no_items}",p2,p1)
                new_rect.setPen(QPen(QColor(Qt.black),0))
                #self.addItem(new_rect)
                self.admin.addCommand(new_rect)
                #print(new_rect.getName())
                self.signal_next_point.emit(self.vertex)
                self.vertex = 0

            return cancel_point


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

            
    #*************************************************************************
    def figura_inicial_borrar(self):
        #return

        pointsCoord = [
        [   0.0000 ,  0.0000],
        [   0.0010 ,  0.0010],
        [   0.0100 ,  0.0000],
        [ 100.0000 ,  0.0000],
        [ 100.0000 , 50.000],
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

        # Figura inicial de prueba
        trianglePolygon = QPolygonF()
        for i in pointsCoord:
            trianglePolygon.append(QPointF(i[0], i[1]))        
        pen= QPen(Qt.black)
        pen.setWidth(0)
        brush = QBrush(Qt.SolidPattern)
        brush.setColor(QColor(168, 246, 218, 100))
        self.addPolygon(trianglePolygon,pen,brush)
        return
        self.addLine(-1000,-1000,1000,1000,pen)
    #*************************************************************************
