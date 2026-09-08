"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : PointItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
from config import config_manager
import math



class TextMeshBackItem(QGraphicsItem):

    def __init__(self, text:str, coordinatesX:float, coordinatesY:float):        
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
                
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())

        self.text = text
        self.coordenates = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.coordenates)
        
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
    
    def boundingRect(self) -> QRectF:
        size = 0.001
        return QRectF(-size, -size,
                             2*size, 2*size)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:

        if self.text != "temp":
            painter.setPen(self.pen)
            painter.drawText(QPointF(0, 0), self.text)

class NodeMeshBackItem(QGraphicsItem):

    SIZE = 10
    
    #thema 1 > dark
    COLOR_T1 = QColor("#333")
    COLORBORDER_T1 = QColor("#817e61")
    
    #thema 2 > light    
    COLOR_T2 = QColor("#555")
    COLORBORDER_T2 = QColor("#a6ccff")

    def __init__(self, id:str, coordinatesX, coordinatesY ):
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())
       
        self.name = id
        self.coordenates = QPointF(coordinatesX, coordinatesY)
        self.newPos(self.coordenates)

        self.isSelectedPointBlack = False
        
        self.pen_selected = QPen(QColor("#960b0f"), 0, Qt.SolidLine)
        self.pen_selected.setCosmetic(True)
        self.pen_selected.setWidthF(0.5)
        self.brush_selected = QBrush(QColor(Qt.red))

    def getIdNode(self):
        return self.name
    
    def getCoodenates(self):
        return self.coordenates
        
    def newPos(self, pos:QPointF|QPoint):
        self.coordenates = pos
        self.setPos(pos)

    def signalThemeChanged(self, theme:str):
        if theme == "dark":
            color = QColor(self.COLOR_T1)
            color_border = QColor(self.COLORBORDER_T1)
        else:
            color = QColor(self.COLOR_T2)
            color_border = QColor(self.COLORBORDER_T2)            
        self.pen = QPen(color_border, 0)
        self.brush = QBrush(QColor(color))
        self.update()

    def boundingRect(self) -> QRectF:
        size = 0.01
        return QRectF(-size, -size,
                             2*size, 2*size)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        
        if self.isSelectedPointBlack:
            self.pen_selected.setWidthF(1 / painter.transform().m11()) # m11()
            painter.setPen(self.pen_selected)
            painter.setBrush(self.brush_selected)
            painter.drawRect(-self.SIZE/2, -self.SIZE/2, self.SIZE, self.SIZE)
        else:
            painter.setPen(self.pen)
            painter.setBrush(self.brush)
            painter.drawRect(-self.SIZE/2, -self.SIZE/2, self.SIZE, self.SIZE)
        
class ElementMeshBackItem(QGraphicsItem):

    WIDTH = 1
    
    #thema 1 > dark
    COLOR_T1 = "#a6ccff"
    
    # theme 2 > light
    COLOR_T2 = "#817e61"

    def __init__(self,
                 node1:NodeMeshBackItem,node2:NodeMeshBackItem,
                 node3:NodeMeshBackItem, node4:NodeMeshBackItem ):
        QGraphicsItem.__init__(self)
        
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())

        self.node1 = node1
        self.node2 = node2
        self.node3 = node3
        self.node4 = node4
                
        self.nodes_coordenates = [
            self.node1.getCoodenates(),
            self.node2.getCoodenates(),
            self.node3.getCoodenates(),
            self.node4.getCoodenates(),
            self.node1.getCoodenates()
        ]

        self.isSelected = False
        self.isActive = False

        self.generatePath()
        xs = [c.x() for c in self.nodes_coordenates]
        ys = [c.y() for c in self.nodes_coordenates]
        self._bounding_rect = QRectF(min(xs), min(ys), max(xs) - min(xs), max(ys) - min(ys))

    def signalThemeChanged(self, theme:str):
        if theme == "dark":
            color = QColor(self.COLOR_T1)
        else:
            color = QColor(self.COLOR_T2)            
        self.pen = QPen(color, 0)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(self.WIDTH)
        self.update()
            
    def generatePath(self):
        self.path = QPainterPath()
        self.path.addPolygon(QPolygonF(self.nodes_coordenates))

    def boundingRect(self):
        return self._bounding_rect

    def paint(self, painter, option, widget):
        painter.setPen(self.pen)
        painter.drawPath(self.path)

class TextFrameItem(QGraphicsItem):
    HIGT = 20
    def __init__(self, text: str, coordinatesX, coordinatesY):
        super().__init__()
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        self.frame_pen = QPen(QColor("#333333"))
        self.frame_radius = 3
        self.gradient_start_color = QColor("#DDDDDD")
        self.gradient_end_color = QColor("#FFFFFF")
        self.gradient_start_color.setAlpha(200)  # Establecer transparencia al 50%
        self.gradient_end_color.setAlpha(200)  # Establecer transparencia al 50%
        
        self.extra_width = 1  # Ancho adicional del marco
        self.font = QFont("Arial", 12)  # Define la fuente del texto
        self.higt = self.HIGT
        
        self.text = str(text)
        self.position = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.position)
    
    def rectText(self):
        h= self.higt + 2
        font_metrics = QFontMetrics(self.font)
        text_width = font_metrics.horizontalAdvance(self.text)  # Ancho del texto
        w = text_width + 3 * self.extra_width  # Ancho ajustado
        return QRectF(-w/2, -h/2, w, h + 3)
    
    def setColor(self, color):
        self.color = QColor(color)
        self.pen = QPen(self.color)

    def newPos(self, pos:QPointF|QPoint):
        self.position = pos
        self.setPos(pos)
        
    def boundingRect(self) -> QRectF:
        return QRectF(-0.01, -0.01, 0.02, 0.02)

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
        
class TriangleMeshItem(QGraphicsItem):

    WIDTH = 1.8

    def __init__(self,id, name:str, color:str, coordinates:list):
        QGraphicsItem.__init__(self)
        
        self.id = id
        self.name = name
        self.color = color
        self.coordinates = coordinates
        
        self.width =         self.isSelected = False
        self.isActive = False

        self.pen = QPen()
        self.pen.setCosmetic(True)
        self.pen.setWidthF(self.WIDTH)
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
        self._bounding_rect = self._triangleBoundingRect(self.coordinates)

    def setColor(self, color):
        self.color = color
        color_q  = QColor(color)
        color_darker = color_q.darker(150)
        self.pen.setColor(color_darker)

        color_transparente = color_q
        color_transparente.setAlpha(150)#(0-255)
        self.brush = QBrush(color_transparente)
        self.update()

    def boundingRect(self):
        return self._bounding_rect

    def _triangleBoundingRect(self, points):
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

    WIDTH = 1.8


    def __init__(self,id, name:str, color:str, coordinates:list):
        QGraphicsItem.__init__(self)
        self.id = id
        self.name = name
        self.color = color
        self.coordinates = coordinates

        self.isSelected = False
        self.isActive = False   
        
        self.pen = QPen()
        self.pen.setCosmetic(True)
        self.pen.setWidthF(self.WIDTH)
        self.brush = QBrush()

        self.generatePath()
        self.setColor(self.color)

   
    def generatePath(self):
        self.path = QPainterPath()
        points = []
        for point in self.coordinates:
            point = QPointF(point[0], point[1])
            points.append(point)
        points.append(QPointF(self.coordinates[0][0], self.coordinates[0][1]))
        self.path.addPolygon(QPolygonF(points))
        self._bounding_rect = self._triangleBoundingRect(self.coordinates)

    def setColor(self, color):
        self.color = color
        color_q = QColor(color)
        color_darker = color_q.darker(150)
        self.pen.setColor(color_darker)
        color_transparente = color_q
        color_transparente.setAlpha(150)
        self.brush = QBrush(color_transparente)
        self.update()

    def boundingRect(self):
        return self._bounding_rect

    def _triangleBoundingRect(self, points):
        left = min(point[0] for point in points)
        top = min(point[1] for point in points)
        right = max(point[0] for point in points)
        bottom = max(point[1] for point in points)
        return QRectF(left, top, right - left, bottom - top)

    def paint(self, painter, option, widget):
        painter.setBrush(self.brush)
        painter.setPen(self.pen)
        painter.drawPath(self.path)



class TextMptem(QGraphicsItem):

    def __init__(self, text:str, coordinatesX:float, coordinatesY:float):        
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
                
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())

        self.text = text
        self.coordenates = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.coordenates)

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
    
    def boundingRect(self) -> QRectF:
        size = 0.001
        return QRectF(-size, -size,
                             2*size, 2*size)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        painter.setPen(self.pen)
        painter.drawText(QPointF(0, 0), self.text)

class PointBoundaryTxItem(QGraphicsItem):

    SIZE = 0.15  # fallback en unidades de escena

    def __init__(self, node_id: str, name: str, coordinatesX=1, coordinatesY=1,
                 Tx=True, Ty=True, size: float = 0.0,
                 dir_x: float = 0.0, dir_y: float = -1.0):
        QGraphicsItem.__init__(self)

        self.node_id = node_id
        self.name = name
        self.coor = QPointF(coordinatesX, coordinatesY)
        self.Tx = Tx
        self.Ty = Ty

        s = size if size > 0 else self.SIZE
        self.size = s
        self.setPos(self.coor)
        self.isSelected = False
        self.isSelectedBoundary = False

        # Desplazamiento en dirección alejada del centroide
        ox = dir_x * s
        oy = dir_y * s
        self.off_x = ox
        self.off_y = oy

        self.pen = QPen(QColor("#FF0000"), 0)
        self.pen.setCosmetic(True)
        self.pen_selected = QPen(QColor("#FF6600"), 0)
        self.pen_selected.setCosmetic(True)

        r = s * 0.5
        if Tx and Ty:
            # Triángulo que apunta al nodo (0,0)
            # La dirección (dir_x, dir_y) es hacia afuera del nodo.
            # El triángulo se dibuja desde el apex (0,0) hacia afuera.
            
            # Vector perpendicular para el ancho de la base
            p_dx, p_dy = -dir_y, dir_x
            
            # Base del triángulo desplazada una distancia 's' en dirección (dir_x, dir_y)
            base_mid_x = dir_x * s
            base_mid_y = dir_y * s
            
            # Esquinas de la base
            bx1, by1 = base_mid_x + p_dx * s * 0.5, base_mid_y + p_dy * s * 0.5
            bx2, by2 = base_mid_x - p_dx * s * 0.5, base_mid_y - p_dy * s * 0.5
            
            pts = [
                QPointF(0, 0),   # Apex en el nodo
                QPointF(bx1, by1),
                QPointF(bx2, by2),
                QPointF(0, 0),
            ]
            self.path_main = QPainterPath()
            self.path_main.addPolygon(QPolygonF(pts))
            
            # Línea de sombreado (un poco más lejos de la base)
            line_ext = s * 1.2
            lx1, ly1 = base_mid_x * 1.15 + p_dx * s * 0.7, base_mid_y * 1.15 + p_dy * s * 0.7
            lx2, ly2 = base_mid_x * 1.15 - p_dx * s * 0.7, base_mid_y * 1.15 - p_dy * s * 0.7
            self.line_p1 = QPointF(lx1, ly1)
            self.line_p2 = QPointF(lx2, ly2)

        else:
            # Círculo: pegado al nodo (0,0) y se extiende en dirección (dir_x, dir_y)
            r = s * 0.4 
            cx, cy = dir_x * r, dir_y * r
            self.circle_rect = QRectF(cx - r, cy - r, r*2, r*2)
            
            ext = s * 0.7  # semilongitud de la línea de restricción
            
            if Tx:
                # Restricción en X -> Línea VERTICAL
                # Si estamos en un lateral, la ponemos en el borde exterior, si no, al borde derecho
                lx = dir_x * (r * 2) if dir_x != 0 else cx + r
                ly = cy
                self.line_p1 = QPointF(lx, ly - ext)
                self.line_p2 = QPointF(lx, ly + ext)
            else:
                # Restricción en Y (Ty) -> Línea HORIZONTAL
                # Si estamos arriba/abajo, al borde exterior, si no, al borde superior (como pidió el user)
                lx = cx
                ly = dir_y * (r * 2) if dir_y != 0 else cy - r
                self.line_p1 = QPointF(lx - ext, ly)
                self.line_p2 = QPointF(lx + ext, ly)

    def getNameGroup(self):
        return self.name

    def getIdNode(self):
        return self.node_id

    def boundingRect(self) -> QRectF:
        margin = self.size * 2.0
        return QRectF(self.off_x - margin, self.off_y - margin, margin * 2, margin * 2)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        pen = self.pen_selected if (self.isSelected or self.isSelectedBoundary) else self.pen
        painter.setPen(pen)
        painter.setBrush(Qt.BrushStyle.NoBrush)

        if self.Tx and self.Ty:
            painter.drawPath(self.path_main)
            painter.drawLine(self.line_p1, self.line_p2)
        else:
            painter.drawEllipse(self.circle_rect)
            painter.drawLine(self.line_p1, self.line_p2)

class PointForceItem(QGraphicsItem):

    SIZE = 10
    COLOR = QColor("#FF0000")
    
    #theme 1 > dark
    COLORBORDER_T1 = QColor("#c8e3d0")
    
    #theme 2 > light
    COLORBORDER_T2 = QColor("#706b53")


    def __init__(self, id_mp:str, id_group:str, coordinatesX, coordinatesY, Fx:float, Fy:float):
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())

        self.id_mp = id_mp
        self.id_group = id_group
        self.coor = QPointF(coordinatesX, coordinatesY)
            
            
        self.color = self.COLOR  
              
        self.size = self.SIZE
        self.setForce(Fx, Fy)
        
        self.setPos(self.coor)
        self.isSelected = False
        self.isSelectedBoundary = False
        
        self.pen = QPen(self.color_border, 0)
        self.brush = QBrush(QColor(self.color))
        

    
    def setForce(self, Fx, Fy):
        self.Fox = Fx
        self.Foy = Fy
        self.flag_Fo = True
        if Fx == 0.0 and Fy == 0.0:
            self.flag_Fo = False
            return
        
        size = self.size
        pointsFoR =[
            QPointF(0, 0),
            QPointF(size, (size/2)),
            QPointF(size, (size/2)*(1/3)),
            QPointF((size*2), (size/2)*(1/3)),
            
            QPointF((size*2), -(size/2)*(1/3)),
            QPointF(size, -(size/2)*(1/3)),
            QPointF(size, -(size/2)),
            QPointF(0, 0)
        ]
        
        # cambiar direcion del eje y
        Fy = -Fy
        
        # Calcular dirección de la resultante R
        R_direccion = math.degrees(math.atan2(Fy, Fx))
        
        # Rotar el polígono de la resultante R
        pointsFoR = [QPointF(point.x() * math.cos(math.radians(R_direccion)) - point.y() * math.sin(math.radians(R_direccion)),
                           point.x() * math.sin(math.radians(R_direccion)) + point.y() * math.cos(math.radians(R_direccion))) for point in pointsFoR]
        
        self.pathFoR = QPainterPath()
        self.pathFoR.addPolygon(QPolygonF(pointsFoR))
        

        self.update()
    
        
    def signalThemeChanged(self, theme):     
        if theme == "dark":
            self.color_border = self.COLORBORDER_T1
        else:
            self.color_border = self.COLORBORDER_T2
        self.pen = QPen(self.color_border, 0)
   
    
    def boundingRect(self) -> QRectF:
        s = self.size * 2 + 2
        return QRectF(-s, -s, 2*s, 2*s)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        self.pen.setWidthF(1 / painter.transform().m11()) # m11()
        painter.setPen(self.pen)
        painter.setBrush(self.brush)

        if self.flag_Fo:
            painter.drawPath(self.pathFoR)
             
class PointVelocityItem(QGraphicsItem):

    SIZE = 10
    COLOR = QColor("#0000FF")
    
    #theme 1 > dark
    COLORBORDER_T1 = QColor("#c8e3d0")
    
    #theme 2 > light
    COLORBORDER_T2 = QColor("#706b53")


    def __init__(self, id_mp:str, id_group:str, coordinatesX, coordinatesY, Vx:float, Vy:float ):
        QGraphicsItem.__init__(self)
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        
        # Configura el color del texto según el tema
        config_manager.signalThemeChanged.connect(self.signalThemeChanged)
        self.signalThemeChanged(config_manager.getTheme())

        self.id_mp = id_mp
        self.id_group = id_group
        self.coor = QPointF(coordinatesX, coordinatesY)
            

        self.color = self.COLOR        
        self.size = self.SIZE
        
        self.setPos(self.coor)
        self.isSelected = False
        self.isSelectedBoundary = False
        
        self.setVelocity(Vx, Vy)        
        self.pen = QPen(self.color_border, 0)
        self.brush = QBrush(QColor(self.color))
    
    def setVelocity(self, Vx, Vy):
        self.Vox = Vx
        self.Voy = Vy
        self.flag_Vo = True
        if Vx == 0.0 and Vy == 0.0:
            self.flag_Vo = False            
            return       
             
        size = self.size
        
        pointsVoR =[
            QPointF((size*2), 0),
            QPointF(size, (size/2)),
            QPointF(size, (size/2)*(1/3)),
            QPointF(0, (size/2)*(1/3)),
            
            QPointF(0, -(size/2)*(1/3)),
            QPointF(size, -(size/2)*(1/3)),
            QPointF(size, -(size/2)),
            QPointF((size*2), 0)
        ]

        #cambiar direcion del eje y
        Vy = -Vy
        
        # Calcular dirección de la resultante R
        R_direccion = math.degrees(math.atan2(Vy, Vx))  # Ángulo en grados
        
        # Rotar el polígono de la resultante R
        pointsVoR = [QPointF(point.x() * math.cos(math.radians(R_direccion)) - point.y() * math.sin(math.radians(R_direccion)),
                           point.x() * math.sin(math.radians(R_direccion)) + point.y() * math.cos(math.radians(R_direccion))) for point in pointsVoR]
        
        self.pathVoR = QPainterPath()
        self.pathVoR.addPolygon(QPolygonF(pointsVoR))
        
        self.update()
        
    def signalThemeChanged(self, theme):     
        if theme == "dark":
            self.color_border = self.COLORBORDER_T1
        else:
            self.color_border = self.COLORBORDER_T2
        self.pen = QPen(self.color_border, 0)
   
    
    def boundingRect(self) -> QRectF:
        s = self.size * 2 + 2
        return QRectF(-s, -s, 2*s, 2*s)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        self.pen.setWidthF(1 / painter.transform().m11()) # m11()
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        if self.flag_Vo:
            painter.drawPath(self.pathVoR)

class PointMaterialItem(QGraphicsItem):
   
    RADIUS = 0.1

    def __init__(self,pm_id, group_id:str, color:str, coor:list, volume:float,
                 force:PointForceItem, velocity:PointVelocityItem):
        QGraphicsItem.__init__(self)      


        self.pm_id = pm_id
        self.group_id = group_id
        self.color = color
        self.coor = QPointF(coor[0],coor[1])
        self.movePoint(self.coor)        
        self.force = force
        self.velocity = velocity

        self.radius = self.RADIUS
        
        area =volume # es area por unidad de longitud
        # optener radio del circulo
        self.radius = (math.sqrt(area/math.pi))/2

   
        self.pen = QPen(QColor(self.color), 0)
        self.pen.setCosmetic(True)
        self.pen.setWidthF(0.5)

        self.brush = QBrush(QColor(self.color))
        self.brush_selected = QBrush(QColor("#33333300"))

        self.pen_selected_dash  = QPen(QColor("#ff0000"), 0, Qt.DashLine)
        self.pen_selected_solid = QPen(QColor("#000000"), 0, Qt.SolidLine)

        self.isSelectedPointMaterial = False
        
    def setColor(self, color):
        self.color = color
        self.pen.setColor(QColor(self.color))
        self.brush.setColor(QColor(self.color))
        self.update()
        
    def getIdNode(self):
        return self.pm_id
    
    def getIdGroup(self):
        return self.group_id
    
    def setRadius(self, percentage_radius):   
        self.radius = self.RADIUS*(percentage_radius/100)
        self.update()

    def movePoint(self, pos:QPointF):
        self.coor = pos
        self.setPos(pos)          
  
    def boundingRect(self) -> QRectF:
        radius = self.radius
        return QRectF(-radius, -radius,
                             2*radius, 2*radius)

    def paint(self, painter: QPainter, option: QStyleOptionGraphicsItem, widget: QWidget = ...) -> None:
        if self.isSelectedPointMaterial:
            painter.setPen(self.pen_selected_dash)
            painter.setPen(self.pen_selected_solid)
            painter.drawRect(self.boundingRect())
        else:
            painter.setBrush(self.brush)
            painter.setPen(self.pen)
        painter.drawEllipse(QPointF(0, 0), self.radius, self.radius)


#⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
#⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
    

class TextItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#00ff55")
    HIGT = 0
    WIDTH = 0

    def __init__(self, text:str, coordinatesX, coordinatesY, isColorDefaultTheme = False):
        QGraphicsItem.__init__(self)
        if isColorDefaultTheme:
            self.isDefaultTextColorTheme = isColorDefaultTheme
            config_manager.signalThemeChanged.connect(self.signalThemeChanged)
            self.signalThemeChanged(config_manager.getTheme())
        else:
            self.isDefaultTextColorTheme = False
            self.color = self.COLOR
            self.pen = QPen(self.color)
        
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        self.item_type = self.TYPE
        self.higt = self.HIGT
        self.width = self.WIDTH
        self.text = str(text)
        self.position = QPointF(coordinatesX,coordinatesY)
        self.newPos(self.position)
        
    def __str__ (self):
        return "text: {}".format(self.text)
    

    def signalThemeChanged(self, theme):        
        if self.isDefaultTextColorTheme:
            if theme == "dark":
                self.color = QColor("#fff")
            else:
                self.color = QColor("#000")
                
            self.pen = QPen(self.color)
            self.update()
    
    
        
            


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
            self.text_name.setVisible(True)
        else:
            self.text_name.setVisible(False)
            
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
    WIDTHDRAW = 3
    
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
        
        self.pen_select_draw = QPen(QColor("#ff0000"), 0, Qt.SolidLine)
        self.pen_select_draw.setCosmetic(True)
        self.pen_select_draw.setWidthF(self.WIDTHDRAW)
        
        self.pen_select_mesh = QPen(QColor("#ff0000"), 0, Qt.DotLine)
        self.pen_select_mesh.setCosmetic(True)
        self.pen_select_mesh.setWidthF(self.WIDTH)


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
            painter.setPen(self.pen_select_draw)
            painter.drawLine(self.start_point.coor, self.end_point.coor)

        elif self.isSelectedMesh:          
            painter.setPen(self.pen_select_mesh)
            painter.drawLine(self.start_point.coor, self.end_point.coor)


        painter.setPen(QPen(self.color, 0))       
        painter.drawLine(self.start_point.coor, self.end_point.coor)
        #painter.drawRect(self.boundingRect())


        if self.name != "lineTemp" and self.showLabel:   
            self.text_name.newPos(self.center())
            self.text_name.setVisible(True)
        else:
            self.text_name.setVisible(False)

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

