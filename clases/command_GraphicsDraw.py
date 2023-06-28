from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*

contador = 0 


from clases.items_GraphicsDraw import LineItem, PointItem


class AddPointCommand(QUndoCommand):
    """."""
    def __init__(self,current_project, data:list):
        super(AddPointCommand, self).__init__() 

        self.current_project = current_project
        self.id_point = data[0]
        self.name = data[1]     
        self.coordinates = data[2]   
        self.setText("add -> Point")

    def undo(self):
        self.current_project.deleteItemPoint(self.id_point)

    def redo(self):
        
        self.current_project.createItemPoint(
            id_point = self.id_point,
            name=self.name,
            coordinates=self.coordinates
        )  

    def getId(self):
        return self.id_point      

class AddLineCommand(QUndoCommand):
    """."""
    def __init__(self,current_project, data:list):
        super(AddLineCommand, self).__init__() 

        self.current_project = current_project
        self.id_line = data[0]
        self.name = data[1]     
        self.id_start_point = data[2]     
        self.id_end_point = data[3]    

        self.setText("add -> Line")

    def undo(self):
        self.current_project.deleteItemLine(self.id_line)

    def redo(self):
         self.current_project.createItemLine(
            id_line= self.id_line,
            name=self.name,
            id_start_point=self.id_start_point,
            id_end_point=self.id_end_point
        )        
    def getId(self):
        return self.id_line
class MoveCommand(QUndoCommand):
    """."""
    def __init__(self, current_project, items:PointItem, dx, dy):
        super(MoveCommand, self).__init__() 
        self.current_project = current_project
        self.items = items
        self.dx = dx
        self.dy = dy
        #scene.update()
        self.setText("move -> {} items".format(len(self.items)))

    def redo(self):        

        for item in self.items:
            p1 =item.coor
            self.pos = QPointF(p1.x()+self.dx, p1.y()+self.dy)
            item.movePoint(self.pos)          
            self.current_project.updateItemPoint( id_point= item.getId(),
                coordinates=[self.pos.x(), self.pos.y()])



      
    def undo(self):
        for item in self.items:
            p1 =item.coor
            self.pos = QPointF(p1.x()-self.dx, p1.y()-self.dy)
            item.movePoint(self.pos)
            self.current_project.updateItemPoint( id_point= item.getId(),
                coordinates=[self.pos.x(), self.pos.y()])

class RotateCommand(QUndoCommand):
    """."""
    def __init__(self, current_project, items:list):
        super(RotateCommand, self).__init__() 
        self.current_project = current_project
        self.items = items
        #scene.update()
        self.setText("rotate -> {} items".format(len(self.items)))
        

    def redo(self):        

        for item, xi, yi, new_x, new_y in self.items:
            self.pos = QPointF(new_x, new_y)
            item.movePoint(self.pos)
            self.current_project.updateItemPoint( id_point= item.getId(),
                coordinates=[new_x, new_y])
            #self.graphics_scene.removeItem(self.item)            
            #self.graphics_scene.update()
            #self.admin.updateListItems("UPDATECOORDINATES", item)

      
    def undo(self):
        for item, xi, yi, new_x, new_y in self.items:
            self.pos = QPointF(xi, yi)
            item.movePoint(self.pos)
            self.current_project.updateItemPoint( id_point= item.getId(),
                coordinates=[xi, yi])
            #self.graphics_scene.addItem(self.item)
            #self.graphics_scene.clearSelection()
            #self.graphics_scene.update()
            #self.admin.updateListItems("UPDATECOORDINATES", item)

class RemoveCommand(QUndoCommand):
    """."""
    def __init__(self, current_project, items):
        super(RemoveCommand, self).__init__()         
        self.current_project = current_project
        self.items = items
        #scene.update()
        self.setText("del -> {} items".format(len(self.items)))
        
    def redo(self):        

        for item in self.items:    
            if isinstance(item, LineItem):
                id_item = item.getId()   
                self.current_project.deleteItemLine(id_item)

        for item in self.items:    
            if isinstance(item, PointItem):
                id_item = item.getId()
                self.current_project.deleteItemPoint(id_item)




            '''
            self.graphics_scene.removeItem(item)
            self.graphics_scene.removeItem(item.text_id)
            if isinstance(item, LineItem):
                point1 = item.start_point
                point2 = item.end_point
                point1.removeAnchoredLine(item)
                point2.removeAnchoredLine(item)
            #self.graphics_scene.update()
            #self.admin.updateListItems("DELETE",item)
            '''
      
    def undo(self):  



        for item in self.items:    
            if isinstance(item, PointItem):
                data = item.getData()   
                self.current_project.createItemPoint(
                    id_point = data["id"],
                    name=data["name"],
                    coordinates=data["coordinates"]
                ) 

        for item in self.items:    
            if isinstance(item, LineItem ):
                data = item.getData()
                print(data)
                self.current_project.createItemLine(
                    id_line= data["id"],
                    name=data["name"],
                    id_start_point=data["start_point"],
                    id_end_point=data["end_point"]
                )   


            '''
            self.graphics_scene.addItem(item)
            self.graphics_scene.addItem(item.text_id)

            if isinstance(item, LineItem):
                point1 = item.start_point
                point2 = item.end_point
                point1.addAnchoredLine(item)
                point2.addAnchoredLine(item)
            #self.graphics_scene.clearSelection()
            #self.graphics_scene.update()
            #self.admin.updateListItems("ADD",item)
            '''

     
class UpdateCommand(QUndoCommand):
    """."""
    def __init__(self,current_project, item, points):
        super(UpdateCommand, self).__init__() 
        self.current_project = current_project
        self.item = item
        self.points = points
        #scene.update()
        self.setText("update -> {} item".format(self.item.name))

        self.start_point_ant = self.item.start_point
        self.end_point_ant = self.item.end_point
        self.start_point = points[0]
        self.end_point = points[1]
        
    def redo(self):        

        self.item.start_point = self.start_point
        self.item.end_point = self.end_point

        self.current_project.updateItemLine(
            id_line= self.item.getId(),
            id_start_point = self.start_point.getId(), 
            id_end_point = self.end_point.getId()
             )
        #self.admin.updateListItems("UPDATESTARENDPOINT", self.item)
        #self.graphics_scene.update()
      
    def undo(self):
        self.item.start_point = self.start_point_ant
        self.item.end_point = self.end_point_ant
        self.current_project.updateItemLine(
            id_line= self.item.getId(),
            id_start_point = self.start_point_ant.getId(), 
            id_end_point = self.end_point_ant.getId()
            )
        #self.admin.updateListItems("UPDATESTARENDPOINT", self.item)
        #self.graphics_scene.update()

'''


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

'''
