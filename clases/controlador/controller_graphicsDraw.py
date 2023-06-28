
""" Este módulo contiene controlador de la vista pagina home """
'''
from PySide6.QtCore import ( QFile, Slot)
from clases.Vista.view_PageDraw import  ViewPageDraw
from clases.Modelo.model_Projects import ModelProjectCurrent

from clases.Controlador.controller_MenuData import ControllerMenuData
from clases.Controlador.controller_MenuMesh import ControllerMenuMesh
from clases.Controlador.controller_MenuPointMaterial import ControllerMenuPointMaterial
from clases.Controlador.controller_MenuBoundary import ControllerMenuBoundary
'''

from importlib import import_module
from queue import Empty
from random import seed
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF, QLineF,QSize,QEvent,Slot,QObject)
from PySide6.QtWidgets import (QUndoView,QGraphicsRectItem, QGraphicsLineItem, QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu,QSplitter,QDockWidget, QGraphicsItemGroup, QFileDialog)
from PySide6.QtGui import (QColor, QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,
                            QPainterPath,QFont,
                            QKeyEvent,QShortcut, QKeySequence,
                            QFocusEvent,QIcon,QUndoStack,QAction,QUndoCommand,QTransform)
from ui import ui_frame_draw


from clases.Vista import view_WidgetDrawMenuData
from clases.Vista import view_WidgetDrawMenuMesh
from clases import class_projects
#from clases.Vista.view_GraphicsDraw import PointItem,LineItem,TextItem,MeshItem
from clases import class_general
from clases.general_functions import isNumber
from clases import class_ui_dialog_msg
import math
import ezdxf



from clases.Vista.view_GraphicsDraw import ViewGraphicsSceneDraw, ViewGraphicsViewDraw

class ControllerGraphicsDraw(QObject):

    signal_coor_mouse = Signal(list)
    
    signal_msn_console = Signal(list)
    signal_msn_label_console = Signal(list)
    signal_end_draw_geometry = Signal(bool)

   


    def __init__(self) -> None:  
        super().__init__()

        print("*"*60)
        print("Toca evisar el tema del zoom y el pan ")
        print("tiene comportamientos raros  ")
        print(" ControllerGraphicsDraw >>>>  def zoomDraw(self,type_zoom):")
        print("*"*60)

        self.current_project = None

       

        self.scene_draw = ViewGraphicsSceneDraw()
        self.scene_draw.setSceneRect(QRectF(-10000, -10000, 20000, 20000))
        
        self.view_draw_1 = ViewGraphicsViewDraw() 
        self.view_draw_1.setScene(self.scene_draw) 
        self.view_draw_1.setObjectName("ViewDraw1")  
        self.view_draw_1.setFocus()
        self.view_draw_1.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphicsView 2 ::::::::::::::::::        
        self.view_draw_2 = ViewGraphicsViewDraw()       
        self.view_draw_2.setScene(self.scene_draw)       
        self.view_draw_2.setObjectName("ViewDraw2")
        self.view_draw_2.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)


        
        self.modeLabelDraw(False)


        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE DRAW :::::::::::::::::    
        #     
      

        
        self.view_draw_2.signal_end_draw_geometry.connect(self.signalEndDrawGeometry)
        self.view_draw_1.signal_end_draw_geometry.connect(self.signalEndDrawGeometry)

        self.view_draw_1.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_2.signal_coor_mouse.connect(self.coor_mouse)
        self.view_draw_1.signal_main_view.connect(self.main_view)
        self.view_draw_2.signal_main_view.connect(self.main_view)

        '''
        self.scene_draw.signal_next_point.connect(self.nextPoint)
        '''

        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE MESH :::::::::::::::::   
        '''
        self.scene_draw.signal_point_point.connect(self.commandPoint)
        self.scene_draw.signal_point_line.connect(self.commandLine)
        self.scene_draw.signal_point_move.connect(self.commandMove)
        self.scene_draw.signal_point_copy.connect(self.commandCopy)
        self.scene_draw.signal_point_rotate.connect(self.commandRotate)
        self.scene_draw.signal_point_erase.connect(self.commandErase)
        self.scene_draw.signal_point_intersection.connect(self.commandIntersection)
        self.scene_draw.signal_point_rule.connect(self.commandRule)
        '''


    '''

    def setCurrentProject(self,current_project:ModelProjectCurrent):
        self.current_project = current_project
    '''


        



    def modeButtonStatusBar(self, ToolButton_mode):
        name_button = ToolButton_mode[0]
        mode = ToolButton_mode[1]
        if name_button == "SnapGrid":            
            self.scene_draw.mode_snap_grid = mode
            
        elif name_button == "Ortho":
            self.scene_draw.mode_ortho = mode

        elif name_button == "Osnap":    
            self.scene_draw.mode_osnap = mode

    def modeOriginDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar el origen.

        Args:
            mode(bool): modo de los ejes
                        False: origen Oculto
                        False: origen visible
        """ 
        self.view_draw_1.isModeOrigin=mode
        self.view_draw_2.isModeOrigin=mode
        self.scene_draw.update()

    def modeAxisDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar los ejes principales.

        Args:
            mode(bool): modo de los ejes
                        False: ejes Oculta
                        False: ejes visible
        """ 
        self.view_draw_1.isModeAxis=mode
        self.view_draw_2.isModeAxis=mode
        self.scene_draw.update()
        
    def modeGridDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar la grilla.

        Args:
            mode(bool): modo de la grilla
                        False: grilla Oculta
                        False: grilla visible
        """ 
        self.view_draw_1.isModeGrid=mode
        self.view_draw_2.isModeGrid=mode
        self.scene_draw.update()
        
    def main_view(self, main_view):
        """Recibe la señal de la vista que tiene el foco del ratón y la coloca como vista principal.

        Args:
            main_view(tr): nombre de la vista que tiene le foco.

        """ 
        if self.view_draw_1.objectName() == main_view:
            self.view_draw_1.isMainView = True
            self.view_draw_2.isMainView = False
        elif self.view_draw_2.objectName() == main_view:
            self.view_draw_2.isMainView = True
            self.view_draw_1.isMainView = False

    def getPointVertex(self):
        return self.scene_draw.getPointVertex()



    def getPointVertexAnt(self):
        return self.scene_draw.getPointVertexAnt()




    def removeSelectedItems(self, item):   
         self.scene_draw.removeSelectedItems(item)


        
    @Slot(list)
    def coor_mouse(self,coor_list):
        """Recibe la señal de coordenada del ratón y remite la misma, señal a main window para imprimir en barra de estado..

        Args:
            coor_list(list): coordenadas del raton.

        """ 
        self.signal_coor_mouse.emit(coor_list)
        
    def settingDraw(self,setting_update):

        if setting_update["setting"] == "style_view_scene":
            index_style_view_scene = setting_update["setting_data"][2]
            self.scene_draw.setStyleScene(index_style_view_scene)
            self.view_draw_1.setStyleView(index_style_view_scene)
            self.view_draw_2.setStyleView(index_style_view_scene)
            
        if setting_update["setting"] == "crosshair_size":
            value_crosshair_size = setting_update["setting_data"][2]               
            self.view_draw_1.crosshair_size=(value_crosshair_size)/100
            self.view_draw_2.crosshair_size=(value_crosshair_size)/100            

        if setting_update["setting"] == "pick_box_size":
            value_pick_box_size = setting_update["setting_data"][2]      
            self.view_draw_1.pick_box_size =(value_pick_box_size)
            self.view_draw_2.pick_box_size =(value_pick_box_size) 


        if setting_update["setting"] == "grid_adaptative":
            check_grid_adaptative = setting_update["setting_data"][2]
            if check_grid_adaptative:
                self.view_draw_1.grid_adaptative = True
                self.view_draw_2.grid_adaptative = True
            else:
                self.view_draw_1.grid_adaptative = False
                self.view_draw_2.grid_adaptative = False

        if setting_update["setting"] == "grid_spacing":
            grid_spacing = setting_update["setting_data"][2]      
            self.view_draw_1.grid_spacing = grid_spacing
            self.view_draw_2.grid_spacing = grid_spacing
            self.scene_draw.grid_spacing = grid_spacing

        if setting_update["setting"] == "snap_grid_adaptative":
            check_snap_grid_adaptative = setting_update["setting_data"][2]   

            if check_snap_grid_adaptative: 
                self.scene_draw.snap_grid_adaptative = True
 
            else:
                self.scene_draw.snap_grid_adaptative = False



        if setting_update["setting"] == "snap_grid_spacing":
            snap_grid_spacing = setting_update["setting_data"][2]      
            self.scene_draw.snap_grid_spacing = snap_grid_spacing




    def zoomDraw(self,type_zoom):

        if type_zoom == "ZoomExtend":
            self.view_draw_1.reset_view()
            self.view_draw_2.reset_view()
        elif type_zoom == "ZoomWindow":
            self.view_draw_1.zoomWindow(True)
            self.view_draw_2.zoomWindow(True)






   
    def getView1(self):
        return self.view_draw_1    
   
    def getView2(self):
        return self.view_draw_2
    

    
    def modeLabelDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar las etiquetas de los elemetos.

        Args:
            mode(bool): modo de las etiquetas
                        False: etiquetas Ocultas
                        False: etiquetas visibles
        """ 
        self.mode_label_draw = mode
        items = self.scene_draw.items()
        for item in items:
            item.showLabel = mode
        self.scene_draw.update()            

    
    def endDrawGeometry(self):
        self.scene_draw.endDrawGeometry()
        self.view_draw_1.endDrawGeometry()
        self.view_draw_2.endDrawGeometry()
        

    
    def signalEndDrawGeometry(self,show_msn=True):
        self.scene_draw.endDrawGeometry()
        self.signal_end_draw_geometry.emit(show_msn)

 




    def deleteMesh(self, name):

        for mesh in self.scene_draw.items():
            if isinstance(mesh, MeshItem) and name == mesh.getName():
                self.scene_draw.removeItem(mesh)
        self.scene_draw.update()
        self.current_project.deleteMeshDB(name=name)
        #self.scene_draw.admin.deleteMesh(name=name)



    def updateMesh(self, data):
        

        name_prev = data["name_prev"]
        name = data["name"]
        color = data["color"]
        for mesh in self.scene_draw.items():
            if isinstance(mesh, MeshItem) and name_prev == mesh.getName():
                mesh.setColor(color)
                mesh.setName(name)
        self.scene_draw.update()
        data.pop("name_prev")
        self.current_project.updateMeshDB(name_prev=name_prev,name=name, triangle_mesh=data)


        
        


    def msnConsole(self, type_msn, msn):
        self.signal_msn_console.emit([type_msn, msn])

    def msnLabelConsole(self,command, msn):
        self.signal_msn_label_console.emit([command, msn])
    '''
    def commandPoint(self, input:dict):        
        
        step = input["step"]
        coordinate = input["data"]
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo punto
            self.scene_draw.isDrawPoint = True  
            #esto toca que se envie a la vista de draw          
            self.initToolGeometry("point","Ingrese un punto [Exit]:")
            
        elif step == 2:
            point_vertex = QPointF(coordinate[0],coordinate[1])
            items = self.scene_draw.items(point_vertex)
            cancel_point = False

            # verifica si el punto esta por fuera de los limites
            if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):
                cancel_point = True
                self.msnConsole(
                    "Warning",
                    "Posición fuera del límite del dibujo."
                    )
                return cancel_point

            #verifica si hay puntos existentes
            for item in items:
                if type(item) == PointItem:
                    name = item.getData()["name"]
                    if name != "pointTemp":                        
                        self.msnConsole(
                            "Warning",
                            "En esta posición ya existe el punto {}".format(name)
                            )
                        return item

            #::::::::::::  punto  ::::::::::::::::
            items = self.scene_draw.items()
            points = self.scene_draw.admin.list_points
            id_max = 0
            for point in points:
                id = int(points[point]["id"])                
                if id > id_max:
                    id_max = id
            no_id = id_max+1
            text_id = TextItem(no_id, QPointF(0,0))
            #self.scene_draw.addItem(text_id)
            new_point = PointItem(no_id, f"POINT#{no_id}",point_vertex, text_id)
            new_point.showLabel = self.mode_label_draw
            self.scene_draw.admin.addCommand(new_point)
            self.msnConsole("Command","Se ha creado el punto {}".format(new_point.id))
            return new_point
     
    def commandLine(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        

        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo linea
            self.scene_draw.isDrawLine = True            
            self.initToolGeometry("line","Ingrese el primer punto [Exit]:")
            
        elif step == 2:
            #self.point1 = self.commandPoint({"step":2, "data": [data[0],data[1]]}) 
            point=data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertexAnt(point_vertex)
            self.msnLabelConsole("line","Ingrese el siguiente punto [Exit]:")
  
        elif step == 3:
            self.point1 = self.commandPoint({"step":2, "data": [data[0][0],data[0][1]]}) 
            self.point2 = self.commandPoint({"step":2, "data": [data[1][0],data[1][1]]}) 

            if  self.point1.name==self.point2.name:
                return

            #::::::::::::  linea  ::::::::::::::::
            lines = self.scene_draw.admin.list_lines
            id_max = 0
            for line in lines:
                id = int(lines[line]["id"])                
                if id > id_max:
                    id_max = id
            no_id = id_max + 1

            text_id = TextItem(no_id, QPointF(0,0))
            #self.scene_draw.addItem(text_id)
            new_line = LineItem(no_id, f"LINE#{no_id}",self.point1,self.point2, text_id)

            #new_line.setPen(QPen(QColor(Qt.red),0))
            new_line.showLabel = self.mode_label_draw
            self.scene_draw.admin.addCommand(new_line)



            self.point1 = self.point2
            self.msnConsole("Command","Se ha creado la linea  {}".format(new_line.id))
            point=data[1]
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertexAnt(point_vertex)
            return new_line

    def commandMove(self, input:dict):
                
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo mover
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawMove= True            
            self.initToolGeometry("move","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
                #verificar cuales lineas si toca
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
              
            count = 0
            for item in items:    

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelectedDraw = True
                    if not (item in self.getSelectedItems()):
                        count += 1
                        self.addSelectedItems(item)


                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelectedDraw = True
                    point_B.isSelectedDraw = True
                    item.isSelectedDraw = True

                    if not (point_A in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_A)
                        
                    if not (point_B in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_B)

                    if not (item in self.getSelectedItems()) :
                        count += 1
                        self.scene_draw.selected_items_line.append(item)

                self.scene_draw.update()

                #    if item.getData()["name"] != "rectTemp":


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ))
                

        #Inicio de mover
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("move", "Ingrese el primer punto [Exit]:")
        
        # Se recibe el primer punto
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)
            self.msnConsole("Command","Punto inicial = {}".format(data))
            self.msnLabelConsole("move", "Ingrese el segundo punto [Exit]:")


        # Se recibe el segundo punto
        elif step == 5:
           
            items = self.getSelectedItems()
  
 
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_vertex=QPointF(xi+dx, yi+dy)

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):                    
                    self.msnConsole(
                        "Warning",
                        "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"])
                        )
                    return 
                
                items_in_new_pos = self.scene_draw.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.msnConsole(
                                "Error",
                                "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name)
                                )
                            return 

            self.scene_draw.admin.moveCommand(items, dx=dx,dy=dy)
            self.msnConsole("Command","Punto Final = {}".format(data[1]))
            self.msnConsole("Command","Se ha movido los elementos seleccionados".format())
            self.signalEndDrawGeometry()

    def commandCopy(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        # 1) Inicio, selección de elementos
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo copiar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawCopy = True            
            self.initToolGeometry("copy","Seleccione un elemento [Exit]:")  
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:       




                item.isSelectedDraw = True
                if not (item in self.getSelectedItems()) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.addSelectedItems(item)




            if count > 0:
                self.msnConsole(
                    "Command",
                    "Copiar Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ))
        #Inicio de copiar
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("copy", "Ingrese el primer punto [Exit]:")
        
        # Se recibe el primer punto
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)
            self.msnConsole("Command","Punto inicial = {}".format(data))
            self.msnLabelConsole("copy", "Ingrese el segundo punto [Exit]:")
            

        # Se recibe el segundo punto
        elif step == 5:           

            items = self.getSelectedItems()
            
            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )

            for item in items:
                if isinstance(item, PointItem):
                    xi = item.getData()["coordinates"][0]
                    yi =item.getData()["coordinates"][1]
                    self.commandPoint({"step":2, "data": [xi+dx,yi+dy]})
                if isinstance(item, LineItem):


                    x_start_point = (item.start_point.getData()["coordinates"][0])+ dx
                    y_start_point = (item.start_point.getData()["coordinates"][1]) + dy
                    x_end_point =   (item.end_point.getData()["coordinates"][0]) + dx
                    y_end_point =   (item.end_point.getData()["coordinates"][1]) + dy

                   
                    
                    #self.commandLine({"step":2, "data":[data[0][0], data[0][1]]})
                    self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})
            self.msnConsole("Command","Punto final = {}".format(data[1]))

    def commandRotate(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo rotar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawRotate= True            
            self.initToolGeometry("rotate","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)
              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelectedDraw  = True
                    if not (item in self.getSelectedItems()):
                        count += 1
                        self.addSelectedItems(item)
                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point
                    point_A.isSelectedDraw  = True
                    point_B.isSelectedDraw  = True
                    item.isSelectedDraw  = True

                    if not (point_A in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_A)
                        
                    if not (point_B in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(point_B)

                    if not (item in self.scene_draw.selected_items_line) :
                        count += 1
                        self.scene_draw.selected_items_line.append(item)

                """
                item.isSelectedDraw  = True
                if not (item in self.scene_draw.selected_items) and not isinstance(item, TextItem):
                    if item.getData()["name"] != "rectTemp":
                        count += 1
                        self.addSelectedItems(item)
                """


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ))
        #Inicio de rotar
        elif step == 3:
            selected_items = len(self.getSelectedItems())
            self.view_draw_1.selectElement(False)
            self.view_draw_2.selectElement(False)                
            self.scene_draw.update()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items))
            self.msnLabelConsole("rotate", "Ingrese el punto base [Exit]:")        

        
        # Se recibe el punto centro para rotar
        elif step == 4:
            point = data
            point_vertex =QPointF(point[0],point[1])
            self.setPointVertex(point_vertex)
            self.setPointVertexAnt(point_vertex)
            self.msnConsole("Command","Punto base = {}".format(data))
            self.msnLabelConsole("rotate", "Ingrese el ángulo [Exit]:")

        # Se recibe el segundo punto
        elif step == 5:



            items = self.getSelectedItems()
            x_ref, y_ref = data[0][0], data[0][1]
            point_ref = QPointF(x_ref, y_ref)
            angle_ref = data[1]

            """
            group_selected = QGraphicsItemGroup()
            for item_i in items_i:                
                group_selected.addToGroup(item_i)
            self.scene_draw.addItem(group_selected)
            transform = QTransform().translate(pivot.x(), pivot.y()).rotate(angle_ref).translate(-pivot.x(), -pivot.y())
            group_selected.setTransform(transform, combine=False)

            elements = group_selected.childItems()
            self.scene_draw.removeItem(group_selected)
            """
            list_items_new_pos =[]

 
            for item in items:
                xi = item.getData()["coordinates"][0]
                yi =item.getData()["coordinates"][1]
                point_to_rotate =  QPointF(xi,yi)
                angle_rad_ref = math.radians(angle_ref)     
                dx = point_to_rotate.x() - point_ref.x()
                dy = point_to_rotate.y() - point_ref.y()
                dist = math.sqrt(dx*dx + dy*dy)
                angle_point = math.atan2(dy, dx)
                if angle_point < 0:
                    angle_point = (2*math.pi) + angle_point

                angle_new = angle_point + angle_rad_ref

                # Calcular la nueva posición del punto después de la rotación
                new_x = point_ref.x() + dist * math.cos(angle_new)
                new_y = point_ref.y() + dist * math.sin(angle_new)              
                
                point_vertex=QPointF(new_x, new_y)            

                # verifica si los punto se mueven por fuera de los limites
                if not self.pointInRect(point_vertex,self.scene_draw.sceneRect()):                    
                    self.msnConsole(
                        "Warning",
                        "Nueva posición del elemento {} fuera del límite del dibujo.".format(item.getData()["name"])
                        )
                    return 
                
                items_in_new_pos = self.scene_draw.items(point_vertex)

                #verifica si hay puntos existentes
                for item_in_new_pos in items_in_new_pos:
                    if type(item_in_new_pos) == PointItem:
                        name = item_in_new_pos.getData()["name"]
                        name_iten_to_move = item.getData()["name"]
                        if name != "pointTemp" and item_in_new_pos not in items: 
                            self.msnConsole(
                                "Error",
                                "En la nueva posición del elemento {} ya existe el punto {}.".format(name_iten_to_move,name)
                                )
                            return 
                
                list_items_new_pos.append([item, xi, yi, new_x, new_y])


            self.scene_draw.admin.rotateCommand(items= list_items_new_pos)
            self.msnConsole("Command","ángulo = {}".format(data[1]))
            self.msnConsole("Command","Se ha rotado los elementos seleccionados".format())
            self.signalEndDrawGeometry()

    def commandErase(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo borrar
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawErase= True            
            self.initToolGeometry("erase","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        

                if isinstance(item, TextItem):                    
                    continue    

                elif isinstance(item,PointItem):
                    item.isSelectedDraw  = True
                    if not (item in self.getSelectedItems()):
                        if len(item.anchored_lines) != 0:
                            self.msnConsole("Command","No se puede eliminar {}, esta anclado a mas de dos lienas ".format(item.name))
                            item.isSelectedDraw =False
                        else:
                            count += 1
                            self.addSelectedItems(item)
          
                elif isinstance(item, LineItem):
                    point_A = item.start_point
                    point_B = item.end_point



                    if not (point_A in self.getSelectedItems()) :
                        count += 1
                        if item in point_A.anchored_lines and len(point_A.anchored_lines) == 1:
                            self.addSelectedItems(point_A)
                            point_A.isSelectedDraw  = True


                        
                    if not (point_B in self.getSelectedItems()) :
                        count += 1
                        if item in point_B.anchored_lines and len(point_B.anchored_lines) == 1:
                            self.addSelectedItems(point_B)
                            point_B.isSelectedDraw  = True

                    if not (item in self.getSelectedItems()) :
                        count += 1
                        self.addSelectedItems(item)
                        item.isSelectedDraw  = True


            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ))
                
        #Inicio de borrar
        elif step == 3:
            selected_items = len(self.getSelectedItems())         
            self.msnConsole("Command","{} Elementos seleccionados".format(selected_items)) 
            self.msnConsole("Command","Se ha eliminado los elementos seleccionados".format())
            self.scene_draw.admin.removeCommand(self.getSelectedItems())  
            self.signalEndDrawGeometry()

    def commandImport(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
 
        # 1) Inicio, selección de elementos
        if step == 1:
            options = QFileDialog.Options()
            dxf_file_path, _ = QFileDialog.getOpenFileName(self.view_draw_2,"Importar DXF","","Data files dxf (*.dxf)", options=options)

            if dxf_file_path:
                doc = ezdxf.readfile(dxf_file_path)            
                msp = doc.modelspace()

                for entity in msp:
                    if entity.dxftype() == "POINT":
                        xi = entity.dxf.location[0]
                        yi = entity.dxf.location[1]

                        self.commandPoint({"step":2, "data": [xi,yi]})

                    elif entity.dxftype() == "LINE":
                        start_point = entity.dxf.start
                        end_point = entity.dxf.end

                        x_start_point =start_point[0]
                        y_start_point =start_point[1]
                        x_end_point =end_point[0]
                        y_end_point =end_point[1]
                        self.commandLine({"step":3, "data":[[x_start_point, y_start_point],[x_end_point, y_end_point]]})


                        
                    elif entity.dxftype() == "LWPOLYLINE":
                        points = [(vertex[0], vertex[1]) for vertex in entity.get_points()]
                        for i in range(len(points) - 1):
                            start_point = points[i]
                            end_point = points[i+1]
                            x_start_point, y_start_point = start_point
                            x_end_point, y_end_point = end_point
                            self.commandLine({"step": 3, "data": [[x_start_point, y_start_point], [x_end_point, y_end_point]]})

    def commandIntersection(self, input:dict):
        
        step = input["step"]
        data = input["data"]
        
        
        # 1) Inicio, selección de elementos
        if step == 1:
            self.signalEndDrawGeometry(False)
            # se activa modo Interseccion
            self.scene_draw.isDrawSelect = True            
            self.scene_draw.isDrawIntersection= True            
            self.initToolGeometry("intersection","Seleccione un elemento [Exit]:")
            self.view_draw_1.selectElement(True)
            self.view_draw_2.selectElement(True)

              
        #Se recibe dos puntos para el área de selección
        elif step == 2:  
            
            coordinates = data
            p1_select = QPointF(coordinates[0][0],coordinates[0][1])
            p2_select = QPointF(coordinates[1][0],coordinates[1][1])
            x1 = p1_select.x()
            x2 = p2_select.x()

            if p1_select==p2_select:
                items = self.scene_draw.items(self.scene_draw.rect_pick_box,mode=Qt.IntersectsItemShape)
            elif x1 > x2:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.IntersectsItemShape)
            else:
                items = self.scene_draw.items(QRectF(p1_select, p2_select),mode=Qt.ContainsItemShape)
            count = 0
            for item in items:        
                
                if isinstance(item, TextItem):                    
                    continue    

                elif isinstance(item,PointItem):
                    continue

                elif isinstance(item, LineItem):

                    if (not self.deselect_draw_geometry) and (not (item in self.getSelectedItems())) :
                        count += 1
                        self.addSelectedItems(item)
                        item.isSelectedDraw  = True

                    elif self.deselect_draw_geometry and (item in self.getSelectedItems()):
                        item.isSelectedDraw  = False
                        self.removeSelectedItems(item)



            if count > 0:
                self.msnConsole(
                    "Command",
                    "Se ha seleccionado en total {} elementos (nuevos +{}) ".format(
                        len(self.getSelectedItems()),
                        count
                        ))
    
        #Inicio de interseccion a
        elif step == 3:

            
            selected_items = self.getSelectedItems()
            self.scene_draw.isDrawSelect = False
            self.msnConsole("Command","{} Elementos seleccionados".format(len(selected_items))) 


            self.intersectionLinesDraw(selected_items)


            self.msnConsole("Command","Se ha creado la intersección ".format())
            self.signalEndDrawGeometry()

    def commandRule(self, input:dict):

        
        step = input["step"]
        data = input["data"]

        if step == 1:   
            self.signalEndDrawGeometry(False)      
            self.scene_draw.isDrawRule = True            
            self.initToolGeometry("rule", "Ingrese el primer punto [Exit]:")

        if step == 2:                  
            self.initToolGeometry("rule", "Ingrese el segundo punto [Exit]:")

        elif step == 3:  
            x1, y1 = data[0][0],data[0][1]
            x2, y2 = data[1][0],data[1][1]

            dx = (data[1][0] -data[0][0] )
            dy = (data[1][1] -data[0][1] )
            dist = (((dx)**2)+((dy)**2))**0.5
            if dx != 0:
                angle = math.degrees(math.atan(dy/dx))
            else:
                angle = math.degrees(math.atan(dy/0.000000001))
            
            self.msnConsole("Command","Punto Inicial: [{},{}] Punto Final: [{}, {}]".format(x1,y1,x2,y2))
            self.msnConsole("Command","dx:{} dy:{}".format(dx,dy))
            self.msnConsole("Command","Distancia: {}".format(dist))
            self.msnConsole("Command","Ángulo: {}".format(angle))

            self.signalEndDrawGeometry()


            """

    def intersectionLinesDraw(self, selected_items):

            len_selected_items= len(selected_items)

            print("DATOS: {} \nCANTIDAD: {}".format(selected_items,len_selected_items))

     
            line_A= selected_items[0]
            line_B= selected_items[1]

            # Obtener los puntos finales de cada línea
            lA_p1, lA_p2 = line_A.getPoints()
            lB_p1, lB_p2 = line_B.getPoints()
            
            lA_p1f, lA_p2f  = lA_p1.getCoordinates(), lA_p2.getCoordinates()
            lB_p1f, lB_p2f = lB_p1.getCoordinates(), lB_p2.getCoordinates()

            line_Af = QLineF(lA_p1f, lA_p2f )
            line_Bf = QLineF(lB_p1f, lB_p2f)

           
            # Calcular la intersección entre las dos líneas
            intersection_type, intersection_point = line_Af.intersects(line_Bf)
            print(" A:[{}] B:[{}]  >>>>   interse type:[{}] ".format(
                                    line_A.getData()["name"],line_B.getData()["name"],
                                    intersection_type))
            # Verificar si las líneas se intersectan
            if intersection_type == QLineF.IntersectionType.BoundedIntersection or intersection_type == QLineF.IntersectionType.UnboundedIntersection:

                new_point = self.commandPoint({"step":2, "data": [intersection_point.x(),intersection_point.y()]})

                # Linea A
                if new_point != lA_p1 and new_point != lA_p2:

                    self.scene_draw.admin.updateCommand(line_A, [lA_p1, new_point])
                    line_A_new = self.commandLine({"step":3, "data":[
                                [intersection_point.x(),intersection_point.y()],
                                [lA_p2f.x(),lA_p2f.y()]]})
                    new_point.addAnchoredLine(line_A)
                    new_point.addAnchoredLine(line_A_new)
       
                # Linea B
                if new_point != lB_p1 and new_point != lB_p2:
                    self.scene_draw.admin.updateCommand(line_B, [lB_p1, new_point])
                    line_B_new = self.commandLine({"step":3, "data":[
                                [intersection_point.x(),intersection_point.y()],
                                [lB_p2f.x(),lB_p2f.y()]]})
                    new_point.addAnchoredLine(line_B)
                    new_point.addAnchoredLine(line_B_new)

            """

    '''

    def getSelectedObjects (self):
        return self.__selected_objects
               
        



