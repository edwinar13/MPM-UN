"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : DiagramItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

import weakref
import math
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*




class PointItem(QGraphicsItem):
    Type = QGraphicsItem.UserType + 1
    def __init__(self, name:str, point:QPointF):
        QGraphicsItem.__init__(self, )
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |QGraphicsItem.ItemIgnoresTransformations)

        self.newPos(point)
        self.name =name
        self.color = Qt.black
        self.radius = 1.5

        #para dejar de escalar en cierta parte del zoom
        '''
        print(graphWidget)
        print(type(self.scene()))
        print(self.scene()==None)
        if type(self.scene()) == None:
            print("1-",self.scene().transform())
        '''
    def newPos(self, pos):
        self.setPos(pos)
    
    def setRadius(self, r):
        self.radius = r
    
    def getName(self):
        return self.name
    


    def boundingRect(self) -> QRectF:
        adjust = 0
        return QRectF(-0.01 - adjust, -0.01 - adjust,
                             0.02 + adjust, 0.02 + adjust)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.isSelected():
            painter.setPen(QPen(QColor("#ff0000"), 0, Qt.DashLine))
            painter.setBrush(QBrush("#ff0000"))
            painter.drawEllipse(-2, -2, 4, 4)
        else:
            painter.setBrush(QBrush(self.color))
            painter.setPen(QPen(self.color, 0))
            painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)


        



    def type(self):
        return PointItem.Type

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
    signal_zoom_view = Signal(float)
    signal_end_draw_geometry = Signal()

    def __init__(self, SceneDraw:QGraphicsScene):
        super(GraphicsViewDraw, self).__init__() 

        #se le agrega la escena a la vista
        self.graphicsScene_draw = SceneDraw
        self.setScene(self.graphicsScene_draw)
       
        
        #OTRAS PROPIEDADES
        self.setMouseTracking(True) 
        '''
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setFrameShape(QFrame.NoFrame)
        '''
        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(self.NoDrag)


        #Atributos
        self.mode_origin = True
        self.scale_view = 1
        self.percent_zoom_view = 100

        # Para mover la escena
        self.start_pos = None

        #Atributos para ayudas de dibujo
        self.mode_ortho = False
        self.mode_osnap  = False
        self.mode_snap_grid = False
        self.snap_grid_adaptative  = False
        self.snap_grid_spacing = 10


        #Atributos para dibujo
        self.isDrawLine = False
        self.isDrawRectangle = False
        self.isDrawPoint = False
        self.isDrawPolyline = False  
        self.isDelate = False
        self.vertex = 0
        self.point_vertex = None

        #elementos temporales
        '''
        self.point_temp = PointItem("pointTemp",QPoint(0,0))          
        self.point_temp.setRadius(2)
        self.graphicsScene_draw.addItem(self.point_temp)
        self.point_temp.setVisible(False)
        print("+++++")
        '''

        self.is_line_temp = False
        self.line_temp = QGraphicsLineItem(QLineF(0,0,0,0))        
        self.graphicsScene_draw.addItem(self.line_temp)
        self.line_temp.setVisible(False)

        #coloca el tema claro por defecto
        self.setStyleViewScene(0)

        # ajusta el eje vertical como positivo arriba
        self.scale(1, -1)

        self.cursor_position_view = QPoint(0,0)
        self.mousePos = None        

        #Atributos para dibujo
        self.isDrawGeometry = False
        self.line = None        
        self.rectangle = None        
        self.point = None        





        self.figura_inicial_borrar()



    ###############################################################################
	# :::::::::::::::::::::          OTROS MÉTODOS           ::::::::::::::::::::::
	###############################################################################  
    def setStyleViewScene(self, index):       
        """ Establece el estilo de la escena.Primero el fondo luego, grilla selector ETC. """
        if index == 0:
            self.color_element="#000000"
            self.color_element_temp="#555555"
            color_background = "#ffffff"
        elif index == 1:
            self.color_element="#222222"
            self.color_element_temp="#555555"
            color_background = "#888888"
        if index == 2:
            self.color_element="#DDDDDD"
            self.color_element_temp="#555555"
            color_background = "#333333"            
        self.setStyleSheet("background-color: {} ;border: 2px solid #444444;".format(color_background))
        self.graphicsScene_draw.setStyleScene(index)

        self.line_temp.setPen(QPen(QColor(self.color_element_temp),0,Qt.DashLine, Qt.RoundCap, Qt.RoundJoin))
 
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
        self.scale(1, -1)

        self.signal_zoom_view.emit(new_scale)

        self.graphicsScene_draw.scale_view=new_scale        
        self.scale_view=new_scale

        new_point_cursor_scene = self.mapToScene(self.cursor_position_view)
        self.graphicsScene_draw.mouse_pos_scene=new_point_cursor_scene
       
    def move_view(self, deltaX, deltaY):
               
        transform = self.transform() 
        deltaX =   deltaX/transform.m11()# m11 escala horizontal
        deltaY =  deltaY/transform.m22()# m22 escala vertical
        self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################    

    def mousePressEvent(self, mouseEvent):
        # activa el modo desplazamiento de la escena        
        if mouseEvent.button() == Qt.MiddleButton:
            
            self.start_pos = mouseEvent.pos()
            self.graphicsScene_draw.mode_crosshair_pick_box = False
            self.setCursor(Qt.OpenHandCursor)


        #se establece el punto inicial para dibujo 
        elif mouseEvent.button() == Qt.LeftButton:   
            point_a = QPointF(self.mapToScene(mouseEvent.pos()))

            #::::::::::::  Eliminar  ::::::::::::::::
            if self.isDelate:
                self.draw_general(point_a)

            #::::::::::::  punto  ::::::::::::::::
            if self.isDrawPoint: 
                self.drawGeometry(self.point_vertex)
                #self.endDrawGeometry()






            #::::::::::::  rectangulo  ::::::::::::::::
            
            if self.isDrawRectangle and self.vertex == 0:
                
                self.vertex  += 1
                self.rectangle = QGraphicsRectItem(QRectF(point_a,point_a))                
                self.rectangle.setPen(QPen(QColor(self.color_element),0))
                self.graphicsScene_draw.addItem(self.rectangle)

                point1=PointItem(self)
                point1.setPos(point_a.x(),point_a.y())
                self.graphicsScene_draw.addItem(point1)
            
            elif self.isDrawRectangle and self.vertex == 1:

                point2=PointItem(self)
                point2.setPos(point_a.x(),point_a.y())
                self.graphicsScene_draw.addItem(point2)

                self.endDrawGeometry()

            #:::::::::::: linea ::::::::::::
            if self.isDrawLine and self.vertex == 0:

                self.vertex  += 1

                self.line = QGraphicsLineItem(QLineF(point_a,point_a))
                self.line.setPen(QPen(QColor(self.color_element),0))
                self.graphicsScene_draw.addItem(self.line)

                point1=PointItem(self)
                point1.setPos(point_a.x(),point_a.y())
                self.graphicsScene_draw.addItem(point1)

                self.point2=PointItem(self)
                self.point2.setPos(point_a.x()+10,point_a.y()+10)
                self.graphicsScene_draw.addItem(self.point2)
            
            elif self.isDrawLine and self.vertex == 1:
                self.endDrawGeometry()
                
            #:::::::::::: polilinea ::::::::::::
            if self.isDrawPolyline and self.vertex == 0:

                self.path = QPainterPath()
                self.path.moveTo(point_a.x(),point_a.y())
                self.path_pline = self.graphicsScene_draw.addPath(self.path)
                
                self.is_line_temp = True 
                self.draw_general(point_a, point_a)
                self.vertex += 1

            elif self.isDrawPolyline and self.vertex >= 1:
                self.path.lineTo(point_a.x(),point_a.y())
                self.path_pline.setPath(self.path)
                self.path_pline.setPen(QPen(QColor(self.color_element),0))

                self.draw_general(point_a, point_a)
                self.vertex += 1
                #self.painter_path.closeSubpath()

        else:
            super(GraphicsViewDraw, self).mousePressEvent(mouseEvent)

    def mouseMoveEvent(self, mouseEvent):
        self.mousePos=mouseEvent.pos()
        point_b = QPointF(self.mapToScene(self.mousePos)) 
        self.point_vertex = QPointF(self.mapToScene(self.mousePos)) 

        #:::::::::::: desplaza la escena ::::::::::::
        if self.start_pos is not None:
            self.setCursor(Qt.ClosedHandCursor)
            delta = self.start_pos - mouseEvent.pos()            
            transform = self.transform()            
            deltaX = delta.x() / transform.m11()# m11 escala horizontal
            deltaY = delta.y() / transform.m22()# m22 escala vertical
            self.setSceneRect(self.sceneRect().translated(deltaX, deltaY))
            self.start_pos = mouseEvent.pos()

        #::::::::::::  punto  ::::::::::::::::
        elif self.isDrawPoint:  

            if self.snap_grid_adaptative == True:
                spacing = self.graphicsScene_draw.grid_spacing
            else:
                spacing = self.snap_grid_spacing            

            if self.mode_snap_grid:
                self.point_vertex = self.pointSnapGrid(spacing, self.point_vertex) 
            self.draw_general(self.point_vertex)



        #:::::::::::: linea ::::::::::::
        elif self.isDrawLine and self.vertex == 1 :
            point_a = QPointF(0,0)
            point_a = self.line.line().p1()

            if self.mode_ortho == True:
                delta_cursor = point_b - point_a
                try:
                    validator = delta_cursor.x()/delta_cursor.y()
                except ZeroDivisionError:
                    validator=100                

                if -1 <= validator <= 1:
                    point_b.setX(point_a.x())
                else:
                    point_b.setY(point_a.y())

            new_line = QLineF(point_a, point_b)

            #agigna la linea a la ya creada 
            self.line.setLine(new_line)
            self.point2.setPos(point_b.x(),point_b.y())

        #::::::::::::  polilinea  ::::::::::::
        elif self.isDrawPolyline and self.is_line_temp:
            

            point_a = self.line_temp.line().p1()

            if self.mode_ortho == True:
                delta_cursor = point_b - point_a
                try:
                    validator = delta_cursor.x()/delta_cursor.y()
                except ZeroDivisionError:
                    validator=100

                if -1 <= validator <= 1:
                    point_b.setX(point_a.x())
                else:
                    point_b.setY(point_a.y())

            self.draw_general(point_a, point_b)

          
        #::::::::::::  rectangulo  ::::::::::::::::
        elif self.isDrawRectangle and self.vertex == 1 :
            point_b = QPointF(self.mapToScene(self.mousePos))  
            point_a = QPointF(self.rectangle.rect().x(),self.rectangle.rect().y())

            new_rectangle = QRectF(point_a, point_b)

            #asigna el rectangulo al ya creado 
            self.rectangle.setRect(new_rectangle)

        elif self.line_temp == True:            
            super(GraphicsViewDraw, self).mouseMoveEvent(mouseEvent)
        
        else:
            self.setCursor(Qt.BlankCursor)
            super(GraphicsViewDraw, self).mouseMoveEvent(mouseEvent)


        self.cursor_position_view = QPoint(mouseEvent.x(),mouseEvent.y())
        new_point_cursor_scene = self.mapToScene(self.cursor_position_view)
        if self.vertex >= 1 or self.isDrawPoint:
            self.graphicsScene_draw.mouse_pos_scene=new_point_cursor_scene
            self.graphicsScene_draw.coor_mouse.emit([new_point_cursor_scene.x(),new_point_cursor_scene.y()])    
            self.graphicsScene_draw.update()

    def mouseReleaseEvent(self, mouseEvent):        
        # activa el modo desplazamiento de  view
        self.start_pos = None
        
        self.setCursor(Qt.BlankCursor)
        self.graphicsScene_draw.mode_crosshair_pick_box = True
        self.update()

        #e = QPointF(self.mapToScene(mouseEvent.pos()))
        #self.paintObject(e)
        super(GraphicsViewDraw, self).mouseReleaseEvent(mouseEvent)

    def wheelEvent(self, event):
        angle_mouse = event.angleDelta().y()    
        scale = math.pow(1.5, angle_mouse / 240.0)

        self.prev_percent_zoom_view = self.percent_zoom_view
        self.percent_zoom_view = self.percent_zoom_view * scale
        
        if self.percent_zoom_view < 1:
            self.percent_zoom_view = 1
            return
        elif self.percent_zoom_view > 500000:
            self.percent_zoom_view = 500000
            return
        
        self.view_scale_changed("{:.1f}%".format(self.percent_zoom_view))
        
    def drawForeground(self, painter: QPainter, rect: QRectF| QRect) -> None:
        """ Evento para dibujar en el primer plano, se dibuja las fechas del origen """
        super(GraphicsViewDraw, self).drawForeground(painter, rect)
        if not hasattr(self, "sceneRect"):
            return

        point_view = QPoint(self.rect().x(),self.rect().height())  
        point_scene = self.mapToScene(point_view) 
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

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS PARA DIBUJO          ::::::::::::::::::::
	############################################################################### 
    def endDrawGeometry(self):
        self.isDrawPoint = False                    
        self.isDrawLine = False
        self.isDrawPolyline = False
        self.isDrawRectangle = False
        self.isDelate = False
        self.isDrawGeometry = False

        self.scene().point_temp.setVisible(False)

        self.graphicsScene_draw.mode_crosshair = False  
        self.signal_end_draw_geometry.emit()
        self.vertex = 0

    def initDrawGeometry(self):
        self.isDrawGeometry = True
        self.graphicsScene_draw.mode_crosshair =True
        #self.signal_end_draw_geometry.emit()        
        self.vertex = 0
        self.update()

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
    
    def drawEraseItemScene(self):
        self.isDelate = True
   

    def drawGeometry(self, p1=None, p2=None):

        if self.isDrawPoint:  
            print("⌡"*50)

            items = self.scene().items(self.point_vertex)
            for item in items:
                if type(item) == PointItem:
                    if item.getName() != "pointTemp":
                        return

            no_items = (len(self.scene().items()))-2
            
            if  self.isDrawGeometry == True:

                
                new_point = PointItem(f"POINT#{no_items}",p1)
                self.graphicsScene_draw.addItem(new_point)

    def draw_general(self, p1=None, p2=None):
        
        if self.isDrawPoint:
            self.scene().point_temp.setVisible(True)
            self.scene().point_temp.setPos(p1)

        if self.is_line_temp:
            self.line_temp.setLine(QLineF(p1,p2))  

        if self.isDelate == True:  
            items = self.graphicsScene_draw.items(p1)
            print(f"(items): {items}")
            for item in items:
                self.graphicsScene_draw.removeItem(item)
        




    def figura_inicial_borrar(self):
        return
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

        area_point_snap_1 = abs(delta_point_snap_1.x()*delta_point_snap_1.y())
        area_point_snap_2 = abs(delta_point_snap_2.x()*delta_point_snap_2.y())
        area_point_snap_3 = abs(delta_point_snap_3.x()*delta_point_snap_3.y())
        area_point_snap_4 = abs(delta_point_snap_4.x()*delta_point_snap_4.y())

        list_areas = [area_point_snap_1, area_point_snap_2, area_point_snap_3, area_point_snap_4]


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





















##################################################################################
##############################################################################
##########################################################################
#######################################################################
###################################################################
##############################################################
##########################################################
####################################################
################################################
############################################
########################################
####################################
################################
############################
########################
###################
###############
###########
######
##










                                                                            ###
                                                                        #######
                                                                    ###########
                                                                ###############
                                                            ###################
                                                        #######################
                                                    ###########################
                                                ###############################
                                            ###################################
                                        #######################################
                                    ###########################################
                                ###############################################
                            ###################################################
                        #######################################################
                    ###########################################################
                ###############################################################
            ###################################################################
        #######################################################################
    ###########################################################################
###############################################################################



















































class GraphicsSceneDraw (QGraphicsScene):
    
    
    point_inserted = Signal(PointItem)
    rect_inserted = Signal(RectItem)
    line_inserted = Signal(LineItem)
    text_inserted = Signal(QGraphicsTextItem)
    item_selected = Signal(QGraphicsItem)
    coor_mouse = Signal(list)
    
    def __init__(self, parent=None):
        super(GraphicsSceneDraw, self).__init__(parent)

        #obtiene la pantalla principal y su tamaño
        self.screen_primary = QApplication.primaryScreen()
        self.screen_height = self.screen_primary.size().height()
        self.screen_width = self.screen_primary.size().width()
        #self.scaled_screen_size = self.screen_height

        # Atributos
        self.mode_axis = True
        self.mode_grid = True
        self.mode_crosshair_pick_box = True
        self.mode_crosshair = False
        self.crosshair_size = 1.0
        self.pick_box_size = 0.005
        self.mouse_pos_scene = None
        self.scale_view = 1

        self.grid_adaptative = False
        self.grid_spacing = 50


        
        # plumas para pick_box, crosshair y mode_crosshair
        self.pen_pick_box = QPen()
        self.pen_pick_box.setWidth(0)
        self.pen_crosshair = QPen()
        self.pen_crosshair.setWidth(0)
        self.pen_crosshair_draw = QPen()
        self.pen_crosshair_draw.setWidth(0)

        # pluma para grilla, eje y eje x
        self.pen_grid_x = QPen()        
        self.pen_grid_x.setWidth(0)
        self.pen_axis_y = QPen()
        self.pen_axis_y.setWidth(0)
        self.pen_axis_x = QPen()
        self.pen_axis_x.setWidth(0)


        #elementos temporales
        self.point_temp = PointItem("pointTemp",QPoint(0,0))          
        self.point_temp.setRadius(2)
        self.addItem(self.point_temp)
        self.point_temp.setVisible(False)
        print("+++++")

        self.setStyleScene(1)

    ###############################################################################
	# :::::::::::::::::::::          OTROS MÉTODOS           ::::::::::::::::::::::
	###############################################################################       
    def setStyleScene(self, index):    
        """Establece el estilo de la escena."""    
        if index == 0:
            self.color_grid="#EEEEEE"
            self.color_axis_x="#B18284"
            self.color_axis_y="#A9CE92"
            self.color_crosshair_draw="#000000"
            self.color_crosshair="#888888"
            self.color_pick_box ="#888888"
            self.color_point_temp ="#00ddff"

        elif index == 1:
            self.color_grid="#777777"
            self.color_axis_x="#742427"
            self.color_axis_y="#C8CC8E"
            self.color_crosshair_draw="#000000"
            self.color_crosshair="#555555"
            self.color_pick_box ="#555555"
            self.color_point_temp ="#ffdd00"
            
        elif index == 2:
            self.color_grid="#313A39"
            self.color_axis_x="#742427"
            self.color_axis_y="#6A6C48"
            self.color_crosshair_draw="#FFFFFF"
            self.color_crosshair="#AAAAAA"
            self.color_pick_box ="#AAAAAA"
            self.color_point_temp ="#ffdd00"


        self.pen_grid_x.setColor(QColor(self.color_grid))
        self.pen_axis_y.setColor(QColor(self.color_axis_y))
        self.pen_axis_x.setColor(QColor(self.color_axis_x))
        self.pen_crosshair_draw.setColor(QColor(self.color_crosshair_draw))
        self.pen_crosshair.setColor(self.color_crosshair)
        self.pen_pick_box.setColor(self.color_pick_box)

        self.point_temp.color = QColor(self.color_point_temp)
    
    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################  
 
    def drawBackground(self, painter, rect) -> None:
        """Evento para dibujar en el plano del fondo, se dibuja los ejes principales X, Y y la grilla """        
        super(GraphicsSceneDraw, self).drawBackground(painter, rect)
        
        #self.grid_adaptative = False
        #self.grid_spacing = 50
        
        if self.grid_adaptative == True:

            #ajusta a la escala los espacios de la grilla
            if 50/(self.scale_view) < 0.5:
                grid_spacing= 0.1
            elif 0.5 <= 50/(self.scale_view)< 1:
                self.grid_spacing= 0.5
            elif 1 <= 50/(self.scale_view)< 5:
                self.grid_spacing= 1
            elif 5 <= 50/(self.scale_view)< 10:
                self.grid_spacing= 5
            elif 10 <= 50/(self.scale_view)< 20:
                self.grid_spacing= 10
            elif 20 <= 50/(self.scale_view)< 50:
                self.grid_spacing= 20
            elif 50 <= 50/(self.scale_view)< 100:
                self.grid_spacing= 50
            elif 100 <= 50/(self.scale_view)< 500:
                self.grid_spacing= 100
            elif 500 <= 50/(self.scale_view)<= 1000:
                self.grid_spacing= 500
            elif 1000 < 50/(self.scale_view):
                self.grid_spacing= 1000
            else:
                self.grid_spacing = self.grid_spacing
            grid_spacing = self.grid_spacing
        else:
            grid_spacing = self.grid_spacing

        print("self.grid_adaptative:",self.grid_adaptative,"   grid_spacing:",self.grid_spacing)

        lines_axis_x_top = (int(abs(rect.top() / grid_spacing )))+1
        lines_axis_x_bottom = (int(abs(rect.bottom() / grid_spacing )))+1
        lines_axis_y_right = (int(abs(rect.right() / grid_spacing )))+1
        lines_axis_y_left = (int(abs(rect.left() / grid_spacing )))+1
        print(lines_axis_x_top,lines_axis_x_bottom,lines_axis_y_right,lines_axis_y_left)

        if max(lines_axis_x_top,lines_axis_x_bottom,lines_axis_y_right,lines_axis_y_left) >= 50:
            lines_axis_x_top, lines_axis_x_bottom, lines_axis_y_right, lines_axis_y_left = 0,0,0,0
            print("********",lines_axis_x_top,lines_axis_x_bottom,lines_axis_y_right,lines_axis_y_left)

        if self.mode_axis == True or self.mode_grid == True:
            painter.save()
            if  self.mode_grid == True:
                painter.setPen(self.pen_grid_x)

                # lineas grilla X > positivo
                for i  in range(lines_axis_x_bottom):
                    linex_positive = QLineF(rect.left(), (i) * grid_spacing,
                                rect.right(), (i) * grid_spacing)
                    painter.drawLine(linex_positive)

                # lineas grilla X > negativo
                for i  in range(lines_axis_x_top):
                    linex_negative = QLineF(rect.left(), (i) * (-grid_spacing),
                                rect.right(), (i) * (-grid_spacing))
                    painter.drawLine(linex_negative)

                # lineas grilla Y positivo
                for i  in range(lines_axis_y_left):
                    linex_positive = QLineF((i) * grid_spacing, rect.top(),
                                (i) * grid_spacing, rect.bottom())
                    painter.drawLine(linex_positive)
                    linex_negative = QLineF( (i) * (-grid_spacing),rect.top(),
                                (i) * (-grid_spacing),rect.bottom())
                    painter.drawLine(linex_negative)

                # lineas grilla Y negativo
                for i  in range(lines_axis_y_right):
                    linex_positive = QLineF((i) * grid_spacing, rect.top(),
                                (i) * grid_spacing, rect.bottom())
                    painter.drawLine(linex_positive)
                    linex_negative = QLineF( (i) * (-grid_spacing),rect.top(),
                                (i) * (-grid_spacing),rect.bottom())
                    painter.drawLine(linex_negative)

            if self.mode_axis == True :

                # eje Y
                painter.setPen(self.pen_axis_y)
                liney = QLineF(0,rect.top(),0,rect.bottom(),)
                painter.drawLine(liney)

                # eje X
                painter.setPen(self.pen_axis_x)
                linex = QLineF(rect.left(),0,rect.right(),0,)
                painter.drawLine(linex)
            painter.restore()
  
    def drawForeground(self, painter: QPainter, rect: QRectF| QRect) -> None:
        """ Evento para dibujar en el primer plano, se dibuja la
        punta de mira y la caja de selección que sigue al ratón """
        super(GraphicsSceneDraw, self).drawForeground(painter, rect)
        if not hasattr(self, "mouse_pos_scene"):
            return
        
        if self.mode_crosshair_pick_box == True :
            if self.mouse_pos_scene == None:
                return
            cursor_y = self.mouse_pos_scene.y()
            cursor_x = self.mouse_pos_scene.x()

            painter.save()

            #:::::::::::::::::  pick_box   :::::::::::::::::
            painter.setPen(self.pen_pick_box)

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

            rectangle = QRectF(cursor_x - (pick_box_size_min / 2),
                            cursor_y - (pick_box_size_min / 2),
                            pick_box_size_min,
                            pick_box_size_min)
            painter.drawRect(rectangle)

            #:::::::::::::::::  crosshair   :::::::::::::::::
            if self.mode_crosshair == True:
                painter.setPen(self.pen_crosshair_draw)      
            else:
                painter.setPen(self.pen_crosshair)
            
            crosshair_size = self.crosshair_size
            if crosshair_size >=1.0:
                crosshair_size = 2.0

            crosshair_size_max = crosshair_size * (self.screen_width/2)* (1/self.scale_view)

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

            for line in (linex_left,linex_right,liney_top,liney_botton):
                painter.drawLine(line)

            painter.restore()

    def mouseMoveEvent(self, mouseEvent):
        """Evento al mover el ratón, se emite una señal con
        las coordenadas de ratón  para ser mostradas en statusBar
        """
        self.mouse_pos_scene = mouseEvent.scenePos()
        self.coor_mouse.emit([self.mouse_pos_scene.x(),self.mouse_pos_scene.y()])         
        self.update()
        super(GraphicsSceneDraw, self).mouseMoveEvent(mouseEvent)
