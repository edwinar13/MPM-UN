
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


from views.draw import view_WidgetDrawMenuData
from views.draw import view_WidgetDrawMenuMesh

from utils import class_general, class_ui_dialog_msg
from utils.general_functions import isNumber
import math
import ezdxf



from views.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult


class ControllerGraphicsResult(QObject):

    signal_coor_mouse = Signal(list)
    
    signal_msn_console = Signal(list)
    signal_msn_label_console = Signal(list)
    signal_end_draw_geometry = Signal(bool)

   


    def __init__(self) -> None:  
        super().__init__()

        self.current_project = None

       
        self.scene_result = ViewGraphicsSceneResult()
        #self.scene_result.setSceneRect(QRectF(-20, -20, 40, 40))
        
        self.view_result = ViewGraphicsViewResult()
        self.view_result.setScene(self.scene_result) 
        self.view_result.setObjectName("ViewResult")  
        self.view_result.setFocus()
        self.view_result.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)


        #bounding_rect = self.scene_result.itemsBoundingRect()
        #self.view_result.setScene(self.scene_result)
        #self.view_result.fitInView(bounding_rect, Qt.KeepAspectRatio)

        #self.scene_result.setSceneRect(QRectF(x,y,w,h))
        
        self.modeLabelDraw(False)


        # ::::::::::::::::::   SEÑAL>>RANURA VIEW Y SCENE DRAW :::::::::::::::::    
        #     
      


        #self.view_result.signal_end_draw_geometry.connect(self.signalEndDrawGeometry)

        self.view_result.signal_coor_mouse.connect(self.coor_mouse)


    def animation(self):
        self.view_result.updateView()
        print(1155455)
        return
        text_item = TextResultItem(text="1",
                                   coordinatesX=0,
                                   coordinatesY=0)
        point_item = PointResultItem(id="dfgsdgdfg",
                                     name="Punto prueba",
                                     coordinatesX=0,
                                     coordinatesY=0,
                                     text_name=text_item)
        self.scene_result.addItem(text_item)
        self.scene_result.addItem(point_item)

        time_list =[0,1000,2000,3000]
        x_list = [0,100,300,200]
        y_list = [0,130,30,500]
        animation = PointAnimation(point_item, time_list, x_list, y_list)
        animation.startAnimation()




    def modeButtonStatusBar(self, ToolButton_mode):
        name_button = ToolButton_mode[0]
        mode = ToolButton_mode[1]
        if name_button == "SnapGrid":            
            self.scene_result.mode_snap_grid = mode
            
        elif name_button == "Ortho":
            self.scene_result.mode_ortho = mode

        elif name_button == "Osnap":    
            self.scene_result.mode_osnap = mode

    def modeOriginDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar el origen.

        Args:
            mode(bool): modo de los ejes
                        False: origen Oculto
                        False: origen visible
        """ 
        self.view_result.isModeOrigin=mode
        self.scene_result.update()

    def modeAxisDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar los ejes principales.

        Args:
            mode(bool): modo de los ejes
                        False: ejes Oculta
                        False: ejes visible
        """ 
        self.view_result.isModeAxis=mode
        self.scene_result.update()
        
    def modeGridDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar la grilla.

        Args:
            mode(bool): modo de la grilla
                        False: grilla Oculta
                        False: grilla visible
        """ 
        self.view_result.isModeGrid=mode
        self.scene_result.update()
        

    def getPointVertex(self):
        return self.scene_result.getPointVertex()


    def getPointVertexAnt(self):
        return self.scene_result.getPointVertexAnt()


    def removeSelectedItems(self, item):   
         self.scene_result.removeSelectedItems(item)


        
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
            self.scene_result.setStyleScene(index_style_view_scene)
            self.view_result.setStyleView(index_style_view_scene)
            
        if setting_update["setting"] == "crosshair_size":
            value_crosshair_size = setting_update["setting_data"][2]               
            self.view_result.crosshair_size=(value_crosshair_size)/100          

        if setting_update["setting"] == "pick_box_size":
            value_pick_box_size = setting_update["setting_data"][2]      
            self.view_result.pick_box_size =(value_pick_box_size)


        if setting_update["setting"] == "grid_adaptative":
            check_grid_adaptative = setting_update["setting_data"][2]
            if check_grid_adaptative:
                self.view_result.grid_adaptative = True
            else:
                self.view_result.grid_adaptative = False

        if setting_update["setting"] == "grid_spacing":
            grid_spacing = setting_update["setting_data"][2]      
            self.view_result.grid_spacing = grid_spacing
            self.scene_result.grid_spacing = grid_spacing

        if setting_update["setting"] == "snap_grid_adaptative":
            check_snap_grid_adaptative = setting_update["setting_data"][2]   

            if check_snap_grid_adaptative: 
                self.scene_result.snap_grid_adaptative = True
 
            else:
                self.scene_result.snap_grid_adaptative = False



        if setting_update["setting"] == "snap_grid_spacing":
            snap_grid_spacing = setting_update["setting_data"][2]      
            self.scene_result.snap_grid_spacing = snap_grid_spacing




    def zoomDraw(self,type_zoom):

        if type_zoom == "ZoomExtend":
            self.view_result.reset_view()
        elif type_zoom == "ZoomWindow":
            self.view_result.zoomWindow(True)


   
    def getView(self):
        return self.view_result    
        return self.view_result_animation    
   

    
    def modeLabelDraw(self,mode:bool):
        """Establece el modo en la escena para ocultar o mostrar las etiquetas de los elemetos.

        Args:
            mode(bool): modo de las etiquetas
                        False: etiquetas Ocultas
                        False: etiquetas visibles
        """ 
        self.mode_label_draw = mode
        items = self.scene_result.items()
        for item in items:
            item.showLabel = mode
        self.scene_result.update()            

    
    def endDrawGeometry(self):        
        self.scene_result.endDrawGeometry()
        self.view_result.endDrawGeometry()
        
    
    def signalEndDrawGeometry(self,show_msn=True):
        self.scene_result.endDrawGeometry()
        self.signal_end_draw_geometry.emit(show_msn)

 




        
        


    def msnConsole(self, type_msn, msn):
        self.signal_msn_console.emit([type_msn, msn])

    def msnLabelConsole(self,command, msn):
        self.signal_msn_label_console.emit([command, msn])

    def getSelectedObjects (self):
        return self.__selected_objects
               
        



