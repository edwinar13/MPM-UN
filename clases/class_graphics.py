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
import weakref
from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
from clases import class_projects
import math

contador = 0 
import datetime


class TextItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#00ff55")
    HIGT = 10
    WIDTH = 40

    def __init__(self, text:str, position:QPointF):
        QGraphicsItem.__init__(self)
        
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)

        self.item_type = self.TYPE
        self.color = self.COLOR
        self.higt = self.HIGT
        self.width = self.WIDTH
        self.text = str(text)
        self.position = position
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


    def __init__(self,id, name:str, coor:QPointF, text_id:TextItem):
        QGraphicsItem.__init__(self)
        
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable )
        '''
        self.setFlag(QGraphicsItem.ItemIgnoresTransformations)
        self.id = id
        self.name = name
        self.item_type = self.TYPE

        self.coor = coor


        self.color = self.COLOR
        self.radius = self.RADIUS

        self.text_id = text_id
        self.text_id.setVisible(False)
        self.text_id.setColor("#7E6807")

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
        self.text_id.newPos(self.coor)
          
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
            self.text_id.newPos(self.coor)
            list_lines = []
            for line in self.anchored_lines:                
                list_lines.append(line.name)
            self.text_id.text = "ID:{} - [{}]".format(self.id, list_lines)
            self.text_id.setVisible(True)
        else:
            self.text_id.setVisible(False)

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

    def __init__(self, id, name: str, start_point: PointItem, end_point: PointItem, text_id:TextItem):
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
        self.text_id = text_id
        self.text_id.setVisible(False)
        self.text_id.setColor("#1482CA")
        
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
        self.text_id.newPos(self.center())
    
      
    def getData(self):
        data = {
            "id":self.id,
            'name': self.name,
            'type': self.item_type,
            'start_point': self.start_point.name,
            'end_point': self.end_point.name
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
            self.text_id.newPos(self.center())
            self.text_id.setVisible(True)
        else:
            self.text_id.setVisible(False)

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

class RectItem2(QGraphicsItem):
    TYPE = "Rect"
    def __init__(self,  name:str, p1:QPointF, p2:QPointF):
        QGraphicsItem.__init__(self)
        '''
        self.setFlags(
            QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable)
        '''
        self.name = name
        self.item_type = self.TYPE
        self.p1 = p1
        self.p2 = p2 
        self.pen = None
        self.brush = None
        self.rect = None


        self.newPos(self.p1)           
        self.setRect(QRectF(self.p1, self.p2))

        self.isSelectedDraw = False
        self.isActive = False
        
    def __str__ (self):
        return str(self.getData())

    def newPos(self, pos:QPointF|QPoint):
        self.setPos(pos)

    def setRect(self, rect:QRectF|QRect):
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
            'type': self.item_type,
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

        if self.isSelectedDraw:
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

class AdminScene():
    def __init__(self,scene:QGraphicsScene) -> None:

                
        self.undo_stack = None
        self.__projectActual= None
        self.__scene= scene

        self.list_points = {}
        self.list_lines = {}
        self.list_rects = {}

        self.dict_points ={}
        self.dict_lines ={}
        self.dict_rects ={}

        self.no_items = 0
 
    def setUndoStack(self, undo_stack):
        self.undo_stack = undo_stack

    def addMesh(self,name, data):        
        self.updateListMesh("ADD", name, data)

    def updateMesh(self,name, data):        
        self.updateListMesh("UPDATE", name, data)

    def deleteMesh(self,name):        
        self.updateListMesh("DELETE", name, "")

    def addCommand(self,item):
        add_command = AddCommand(self, self.__scene, item)
        self.undo_stack.push(add_command) 
   

    def removeCommand(self,items):
        remove_command = RemoveCommand(self, self.__scene, items)
        self.undo_stack.push(remove_command)

    def moveCommand(self,items,dx,dy):
        move_command = MoveCommand(self, self.__scene, items, dx, dy)
        self.undo_stack.push(move_command) 

    def rotateCommand(self,items):
        rotate_command = RotateCommand(self, self.__scene, items)
        self.undo_stack.push(rotate_command) 

    def updateCommand(self,item, points):
        update_command = UpdateCommand(self, self.__scene, item, points)
        self.undo_stack.push(update_command) 
         
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

        self.no_items = data_items_draw["NOITEMS"]
        self.list_points = data_items_draw["PUNTOS"]
        self.list_lines = data_items_draw["LINEAS"]
        self.list_rects = data_items_draw["RECTANGULOS"]


    def __setDrawItems(self):
        """ Recupera información de los atributos y dibuja los items """
        self.__scene.clear()
        self.__scene.drawElementTemp()
        self.__scene.update()

         

        for point in self.list_points:
            id = self.list_points[point]["id"]
            name = self.list_points[point]["name"]
            x = self.list_points[point]["coordinates"][0]
            y = self.list_points[point]["coordinates"][1]

            
            text_id = TextItem(id, QPointF(0,0))
            self.__scene.addItem(text_id)



            p = PointItem(id, name,QPointF(x,y), text_id)  
            self.__scene.addItem(p)
            self.dict_points[name] = p

        for line in self.list_lines:            
            id = self.list_lines[line]["id"]
            name = self.list_lines[line]["name"]
            start_point = self.list_lines[line]["start_point"]
            end_point = self.list_lines[line]["end_point"]

            text_id = TextItem(id, QPointF(0,0))
            self.__scene.addItem(text_id)


            l = LineItem(id, name,self.dict_points[start_point],self.dict_points[end_point], text_id)  
            self.__scene.addItem(l)
            self.dict_lines[name] = l

            point1 = self.dict_points[start_point]
            point2 = self.dict_points[end_point]
            point1.addAnchoredLine(l)
            point2.addAnchoredLine(l)
       
            


        for rect in self.list_rects:

            id = self.list_rects[line]["id"]
            name = self.list_rects[line]["name"]
            start_point = self.list_rects[line]["start_point"]
            end_point = self.list_rects[line]["end_point"]

            r = RectItem(id, name,self.dict_points[start_point],self.dict_points[end_point])  
            r.setPen(QPen(QColor(Qt.black),0))
            self.__scene.addItem(r)
            self.dict_rects[name] = r


    
    def updateListMesh(self, type_update:str,name:str, data:dict):


        """
        type_action = type_update
        name =data["name"]
        color =data["color"]
        points= data["points"]
        triangles= data["triangles"]
        """



        """
                self.scene_draw.admin.addCommand({"name":self.__card_name_mesh,
                                          "color":self.__card_color_mesh,
                                          "points":self.__points,
                                          "triangles":self.__triangles,
                                          })
        """

        error_update = False
        if type_update == "ADD" or type_update == "UPDATE":            
            error_update = self.__projectActual.db_project.updateMeshDB(name=name, triangle_mesh=data)


            if(error_update == True):
                checkProjectChanges = self.__projectActual.checkProjectChanges() 
                
            else:
                self.signal_msn_critical.emit("Error al guardar la malla ")

        elif type_update == "DELETE" :            
            error_update = self.__projectActual.db_project.deleteMeshDB(name=name)

        else:            
            return
   
    
    def updateListItems(self, type_update:str, item:PointItem|LineItem|RectItem):

        type_item = item.getData()["type"]
        name = item.getData()["name"]


        if type_update == "DELETE":
            if  type_item == "Point":
                self.list_points.pop(name)
                self.dict_points.pop(name)

            elif  type_item == "Line":
                self.list_lines.pop(name)
                self.dict_lines.pop(name)

            elif type_item == "Rect":
                self.list_rects.pop(name)
                self.dict_rects.pop(name)

        elif type_update == "ADD":
            if  type_item == "Point":
                self.list_points[name] = item.getData()
                self.dict_points[name] = item
            elif  type_item == "Line":                
                self.list_lines[name] = item.getData()
                self.dict_lines[name] = item
            elif type_item == "Rect":
                self.list_rects[name] = item.getData()
                self.dict_rects[name] = item
                
        elif type_update == "UPDATECOORDINATES":
            coordinates = item.getData()["coordinates"]
            self.list_points[name]["coordinates"] = coordinates

        elif type_update == "UPDATESTARENDPOINT":

            start_point = item.getData()["start_point"]
            end_point = item.getData()["end_point"]
            self.list_lines[name]["start_point"] = start_point
            self.list_lines[name]["end_point"] = end_point
            
            self.dict_lines[name] = item

        else:            
            return
    

class AddCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, item:PointItem):
        super(AddCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.item = item            
        scene.update()
        self.setText("add -> {}".format(self.item.getData()["type"]))

    def undo(self):
        self.graphics_scene.removeItem(self.item)
        self.graphics_scene.removeItem(self.item.text_id)
        if isinstance(self.item, LineItem):
            point1 = self.item.start_point
            point2 = self.item.end_point
            point1.removeAnchoredLine(self.item)
            point2.removeAnchoredLine(self.item)
        self.graphics_scene.update()
        self.admin.updateListItems("DELETE",self.item)
        #self.admin.list_points.pop(self.item.getName())
      
    def redo(self):
        self.graphics_scene.addItem(self.item)
        self.graphics_scene.addItem(self.item.text_id)

        if isinstance(self.item, LineItem):
            point1 = self.item.start_point
            point2 = self.item.end_point
            point1.addAnchoredLine(self.item)
            point2.addAnchoredLine(self.item)
        
        self.graphics_scene.clearSelection()
        self.graphics_scene.update()
        self.admin.updateListItems("ADD",self.item)

        #self.admin.list_points[self.item.getName()] = self.item.__dict__

class RemoveCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, items):
        super(RemoveCommand, self).__init__()         
        self.graphics_scene = scene
        self.admin = admin
        self.items = items
        scene.update()
        self.setText("del -> {} items".format(len(self.items)))

    def redo(self):        
        for item in self.items:
            
            self.graphics_scene.removeItem(item)
            self.graphics_scene.removeItem(item.text_id)
            if isinstance(item, LineItem):
                point1 = item.start_point
                point2 = item.end_point
                point1.removeAnchoredLine(item)
                point2.removeAnchoredLine(item)
            self.graphics_scene.update()
            self.admin.updateListItems("DELETE",item)
      
    def undo(self):
        for item in self.items:            
            self.graphics_scene.addItem(item)
            self.graphics_scene.addItem(item.text_id)

            if isinstance(item, LineItem):
                point1 = item.start_point
                point2 = item.end_point
                point1.addAnchoredLine(item)
                point2.addAnchoredLine(item)
            self.graphics_scene.clearSelection()
            self.graphics_scene.update()
            self.admin.updateListItems("ADD",item)
          
class MoveCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, items:PointItem, dx, dy):
        super(MoveCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.items = items
        self.dx = dx
        self.dy = dy
        scene.update()
        self.setText("move -> {} items".format(len(self.items)))

    def redo(self):        

        for item in self.items:
            p1 =item.coor
            self.pos = QPointF(p1.x()+self.dx, p1.y()+self.dy)
            item.movePoint(self.pos)          
            self.graphics_scene.update()
            self.admin.updateListItems("UPDATECOORDINATES", item)

      
    def undo(self):
        for item in self.items:
            p1 =item.coor
            self.pos = QPointF(p1.x()-self.dx, p1.y()-self.dy)
            item.movePoint(self.pos)

            self.graphics_scene.update()
            self.admin.updateListItems("UPDATECOORDINATES", item)

class RotateCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, items:list):
        super(RotateCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.items = items
        scene.update()
        self.setText("rotate -> {} items".format(len(self.items)))
        

    def redo(self):        

        for item, xi, yi, new_x, new_y in self.items:
            self.pos = QPointF(new_x, new_y)
            item.movePoint(self.pos)

            #self.graphics_scene.removeItem(self.item)            
            self.graphics_scene.update()
            self.admin.updateListItems("UPDATECOORDINATES", item)

      
    def undo(self):
        for item, xi, yi, new_x, new_y in self.items:
            self.pos = QPointF(xi, yi)
            item.movePoint(self.pos)

            #self.graphics_scene.addItem(self.item)
            #self.graphics_scene.clearSelection()
     
            self.graphics_scene.update()
            self.admin.updateListItems("UPDATECOORDINATES", item)
            
class UpdateCommand(QUndoCommand):
    """."""
    def __init__(self,admin:AdminScene ,scene:QGraphicsScene, item, points):
        super(UpdateCommand, self).__init__() 
        self.graphics_scene = scene
        self.admin = admin
        self.item = item
        self.points = points
        scene.update()
        self.setText("update -> {} item".format(self.item.name))

        self.start_point_ant = self.item.start_point
        self.end_point_ant = self.item.end_point
        self.start_point = points[0]
        self.end_point = points[1]
        
    def redo(self):        

        self.item.start_point = self.start_point
        self.item.end_point = self.end_point
        self.admin.updateListItems("UPDATESTARENDPOINT", self.item)
        self.graphics_scene.update()
      
    def undo(self):
        self.item.start_point = self.start_point_ant
        self.item.end_point = self.end_point_ant
        self.admin.updateListItems("UPDATESTARENDPOINT", self.item)
        self.graphics_scene.update()


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


    signal_point_point = Signal(dict)
    signal_point_line = Signal(dict)
    signal_point_move = Signal(dict)
    signal_point_copy = Signal(dict)
    signal_point_rotate = Signal(dict)
    signal_point_erase = Signal(dict)
    signal_point_intersection = Signal(dict)
    signal_point_rule = Signal(dict)

    signal_mesh_select = Signal(dict)
    signal_mesh_size = Signal(dict)
          


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
        self.isDrawGeometry = False


        self.isDrawLine = False
        self.isDrawRectangle = False
        self.isDrawPoint = False
        self.isDrawPolyline = False  
        self.isDrawMove = False          
        self.isDrawCopy = False
        self.isDrawRotate = False
        self.isDrawErase = False
        self.isDrawIntersection = False
        self.isDrawRule = False
        self.isDrawSelect = False          

  

        self.isMeshSelect = False   
        self.isMeshCua = False   
        self.isMeshSize = False   




        self.p1_select = None
        self.p2_select = None
        self.selected_items = []
        self.selected_items_line = []


        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None
        self.point_init = None
        self.vertex = 0
        
        #self.isSelect = False 

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
        text = TextItem("temp", QPointF(0,0))
        self.addItem(text)
        self.point_temp = PointItem(0,"pointTemp",QPointF(0,0),text)          
        self.addItem(self.point_temp)
        self.point_temp.color= QColor("#36C9C6")
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

        self.text_temp = QGraphicsTextItem("quesote")
        #self.text_temp = QGraphicsSimpleTextItem("quesote")
        #self.text_temp.setPlainText("edwin")
        self.text_temp.setPos(QPointF(0,0))
        self.addItem(self.text_temp)
        self.text_temp.setVisible(False)



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
        self.text_temp.setVisible(True)

        if event.button() == Qt.LeftButton and not self.isPan:        

            #::::::::::::  punto  ::::::::::::::::
            if self.isDrawPoint: 
                self.signal_point_point.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
            
            elif self.isDrawLine: 
                if self.point_vertex_ant == None:
                    self.signal_point_line.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
                else:
                    self.signal_point_line.emit(
                        {"step":3,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

            elif self.isDrawSelect or self.isMeshSelect: 
                self.p1_select = event.scenePos()
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.p1_select))
                self.rect_select_temp.setVisible(True)

            #::::::::::::  mover  ::::::::::::::::    
            elif self.isDrawMove and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_move.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:                    
                    self.signal_point_move.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  copiar  ::::::::::::::::    
            elif self.isDrawCopy and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_copy.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:                    
                    self.signal_point_copy.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  malla  ::::::::::::::::    
            elif self.isMeshCua and not self.isMeshSelect:

                if self.point_vertex_ant == None:
                    return
                    self.signal_point_copy.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:         
                    return
                    self.signal_point_copy.emit(
                        {"step":5,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })

            #::::::::::::  rotar  ::::::::::::::::    
            elif self.isDrawRotate and not self.isDrawSelect:

                if self.point_vertex_ant == None:
                    self.signal_point_rotate.emit(
                        {"step":4,
                        "data":
                            [self.point_vertex.x(),self.point_vertex.y()]
                        })

                    self.point_vertex_ant=self.point_vertex
                else:      
                    
                    point = self.point_vertex
                    point_ref = self.point_vertex_ant
                    dx = point.x() - point_ref.x()
                    dy = point.y() - point_ref.y()
                    angle_ref = math.degrees(math.atan2(dy, dx))
                    if angle_ref < 0:
                        angle_ref = 360 + angle_ref


                    self.signal_point_rotate.emit(
                        {"step":5,
                        "data":
                            [[point_ref.x(),point_ref.y()],
                            angle_ref]
                        })
                    
            elif self.isDrawRule: 
                
                if self.point_vertex_ant == None:
                    self.signal_point_rule.emit({"step":2, "data": [self.point_vertex.x(),self.point_vertex.y()]})
                else:
                    self.signal_point_rule.emit(
                        {"step":3,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

            elif self.isMeshSize: 

                if self.point_vertex_ant != None:
                    self.signal_mesh_size.emit(
                        {"step":2,
                        "data":
                            [[self.point_vertex_ant.x(),self.point_vertex_ant.y()],
                            [self.point_vertex.x(),self.point_vertex.y()]]
                        })
                self.point_vertex_ant=self.point_vertex

            



        super(GraphicsSceneDraw, self).mousePressEvent(event)
    
    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        self.point_vertex = event.scenePos()
        
        self.text_temp.setPos(self.point_vertex)
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
        
        #::::::::::::  mover, copiar, rotar, borrar  ::::::::::::::::
        if self.isDrawSelect or self.isMeshSelect:
            
            #self.drawGeneral(self.point_vertex,self.point_vertex_ant)
            if self.p1_select != None:
                self.rect_select_temp.setRect(QRectF(self.p1_select,self.point_vertex))
                x1 = self.p1_select.x()
                x2 = self.point_vertex.x()
                if x1 > x2:
                    self.rect_select_temp.setBrush(self.color_select_mode1)
                else:
                    self.rect_select_temp.setBrush(self.color_select_mode2)
            return            

        
        #::::::::::::  move, copiar , rotar ::::::::::::::::
        if self.isDrawMove or self.isDrawCopy or self.isDrawRotate:   
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  punto  ::::::::::::::::
        elif self.isDrawPoint :  
            self.drawGeneral(self.point_vertex)

            
        #::::::::::::  Linea  ::::::::::::::::
        elif self.isDrawLine:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)
        
        #::::::::::::  Rectangulo  ::::::::::::::::
        elif self.isDrawRectangle:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  regla  ::::::::::::::::
        elif self.isDrawRule:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        #::::::::::::  mesh  ::::::::::::::::
        elif self.isMeshSize:
            self.drawGeneral(self.point_vertex,self.point_vertex_ant)

        super(GraphicsSceneDraw, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:  
        self.text_temp.setVisible(False)
        self.p2_select = event.scenePos()
        if event.button() == Qt.LeftButton and not self.isPan:               
            #::::::::::::  mover  ::::::::::::::::
            if  self.isDrawSelect and self.isDrawMove and self.p1_select != None:
                self.signal_point_move.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
        
            #::::::::::::  copiar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawCopy and self.p1_select != None:
                self.signal_point_copy.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
            

            #::::::::::::  rotar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawRotate and self.p1_select != None:
                self.signal_point_rotate.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                
            #::::::::::::  borrar ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawErase and self.p1_select != None:
                self.signal_point_erase.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                
            #::::::::::::  malla ::::::::::::::::
            elif  self.isMeshSelect and self.isMeshCua and self.p1_select != None:                    
                self.signal_mesh_select.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )
                


            #::::::::::::  interseccion ::::::::::::::::
            elif  self.isDrawSelect and self.isDrawIntersection and self.p1_select != None:
                self.signal_point_intersection.emit(
                    {"step":2,
                    "data":
                        [[self.p1_select.x(),self.p1_select.y()],
                        [self.p2_select.x(),self.p2_select.y()]]
                    }
                    )


            self.rect_select_temp.setRect(0,0,0,0)
            self.rect_select_temp.setVisible(False)
            self.p1_select = None
            self.p2_select = None

                 
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
        self.isDrawErase = False
        self.isDrawSelect = False          
        self.isDrawRotate = False
        self.isDrawCopy = False
        self.isDrawMove = False
        self.isDrawRule = False

        self.isMeshSelect = False
        self.isMeshCua = False
        self.isMeshSize = False


        """
        self.isDrawGeometry = False
        """

        """
        """
        
        self.point_temp.setVisible(False)
        self.line_temp.setVisible(False)
        self.rectangle_temp.setVisible(False)
        self.rect_select_temp.setVisible(False)


        #self.graphicsScene_draw.mode_crosshair = False  
        #self.signal_end_draw_geometry.emit()

        self.p1_select = None
        self.p2_select = None

        for item in self.selected_items:
            item.isSelectedDraw = False

        for  line in self.selected_items_line:
            line.isSelectedDraw = False
            
        self.selected_items = []
        self.selected_items_line = []
        
        self.point_vertex = None
        self.point_vertex_ant = None
        self.point_vertex_init = None

        if self.vertex == 1 and self.point_init != None:
            self.removeItem(self.point_init)
        self.point_init = None
        self.vertex = 0

    
    """
    def initDrawGeometry(self):
        self.isDrawGeometry = True
        #self.graphicsScene_draw.mode_crosshair =True
        #self.signal_end_draw_geometry.emit()        
        self.vertex = 0
        #self.update()
    """

    """
    def drawPointScene(self):        
        self.initDrawGeometry()
        self.isDrawPoint = True

    def drawMoveItemScene(self):
        self.isMove = True  
        return

    def drawLineScene(self):
        self.isDrawLine = True
        self.initDrawGeometry()
    
    def drawPolylineScene(self):   
        self.isDrawPolyline = True
        self.initDrawGeometry()
    
    def drawRectangleScene(self):
        self.isDrawRectangle = True
        self.initDrawGeometry()
        
    

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

    """





    def drawTransform (self, transformation=None):
        return


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

        elif self.isDrawPoint:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)

        elif self.isDrawLine or self.isDrawMove or self.isDrawCopy or self.isDrawRotate or self.isDrawRule or self.isMeshSize:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.line_temp.setVisible(True)
                self.line_temp.setLine(QLineF(p1,p2)) 

        elif self.isDrawRectangle:
            self.point_temp.setVisible(True)
            self.point_temp.setPos(p1)
            if p2 != None:
                self.rectangle_temp.setVisible(True)
                self.rectangle_temp.setRect(QRectF(p1,p2)) 

    """
    
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
    """

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
