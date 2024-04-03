"""Este módulo contiene las clases para objetos relacionados con graphics view, scene e item.

class:
    : PointItem
    : GraphicsViewDraw
    : GraphicsSceneDraw

"""

from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*

class ViewGraphicsSceneResult(QGraphicsScene):
    def __init__(self):
        super().__init__()  
        #self.setSceneRect(QRectF(-20, -20, 40, 40))
    
    #rectangulo en el rect de la scena
    def drawBackground(self, painter: QPainter, rect: QRectF|QRect) -> None:
        painter.setPen(QPen(Qt.blue, 1))
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.drawRect(rect)
        return super(ViewGraphicsSceneResult, self).drawBackground(painter, rect)
    
    '''
    NOTA:
        esto es para verificar los rectangulos de los items
        si bien tengo un problema con el rectangulo del item bar_color
        se debaja asi ya que no alteral el funcionamiento de la aplicacion
    
    
    def drawBoundingRects(self):
        print("*"*50)
        items = self.items()
        for item in items:
            bounding_rect = item.boundingRect()
            print(f"colordendas {bounding_rect} >>>  item {item}")

            
    def drawForeground(self, painter: PySide6.QtGui.QPainter, rect: QRectF | QRect) -> None:
        items = self.items()
        for item in items:
            
            bounding_rect = item.boundingRect()
            painter.setPen(QPen(Qt.red, 0))
            #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
            painter.drawRect(bounding_rect)
            
        
        return super().drawForeground(painter, rect)

    '''

class ViewGraphicsViewResult(QGraphicsView):
    signal_coor_mouse = Signal(list)
    def __init__(self):
        super().__init__()     
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.adjust_view_on_resize = False 
        self.adjust_view_on_show = 3 
        
        self.isModeColorBar = True
        self.gradient = QLinearGradient()

        self.scale(1, -1)
        self.setStyleView()

    def setStyleView(self, index=0):       
        """ Establece el estilo de la vista.
        
        args:
            index(int): index del estilo

        """

        if index == 0:
            # Crear un gradiente lineal vertical
            gradient = QLinearGradient(0, 0, 0, self.viewport().height())
            gradient.setColorAt(0, QColor("#ffffff"))
            gradient.setColorAt(1, QColor("#fafafa"))
        
        elif index == 1:
            gradient = QRadialGradient(self.viewport().width() / 4, self.viewport().height() / 2,
                                    self.viewport().width(), self.viewport().width() / 2, self.viewport().height() / 2)
            gradient.setColorAt(0, QColor("#DDDDDD"))
            gradient.setColorAt(1, QColor("#aaaaaa"))



        brush = QBrush(gradient)
        self.setBackgroundBrush(brush)
        self.setStyleSheet(f"border-radius: 8px; border: 2px solid #333;padding: 5px;")
        
    def resetView(self):
        '''
        rect = self.scene().itemsBoundingRect()
        self.resetTransform()
        self.setSceneRect(rect)
        self.fitInView(rect, Qt.KeepAspectRatio)
        self.scale(1, -1)
        '''
        self.adjust_view_on_resize = True
        self.adjust_view_on_show = 1
    
        self.updateView()
    

    def updateView(self):
        scene = self.scene()
        r = scene.sceneRect()
        self.fitInView(r, Qt.KeepAspectRatio)

    def resizeEvent(self, event):  
        if self.adjust_view_on_resize <=3:
            self.updateView()
            self.adjust_view_on_resize +=1
        else:
            factor = 1.25
            self.scale(factor, factor)  
            factor = 0.8
            self.scale(factor, factor)  

    def showEvent(self, event):
        if not event.spontaneous():            
            if self.adjust_view_on_show:
                self.updateView()
            self.adjust_view_on_show = False




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
            
        #mover la escena
        if event.button() == Qt.MiddleButton:

            self.scene().isPan = True
            self.setDragMode(QGraphicsView.ScrollHandDrag)
            #self.viewport().setCursor(Qt.ClosedHandCursor)
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

        super(ViewGraphicsViewResult, self).mousePressEvent(event)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """Evento al mover el ratón, se emite una señal con
        las coordenadas de ratón  para ser mostradas en statusBar
        """
        # Emite señal para mostrar coordenada
        point_view = event.pos()
        self.point_scene = self.mapToScene(point_view) 
        self.signal_coor_mouse.emit([self.point_scene.x(),self.point_scene.y()])

        self.scene().update()
        super(ViewGraphicsViewResult, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:      
        if event.button() == Qt.MiddleButton:
            self.setDragMode(QGraphicsView.NoDrag)
            #self.viewport().setCursor(Qt.BlankCursor)
        
  

        super(ViewGraphicsViewResult, self).mouseReleaseEvent(event)

