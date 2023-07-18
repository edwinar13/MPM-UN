
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

 




        
        


    def msnConsole(self, type_msn, msn):
        self.signal_msn_console.emit([type_msn, msn])

    def msnLabelConsole(self,command, msn):
        self.signal_msn_label_console.emit([command, msn])

    def getSelectedObjects (self):
        return self.__selected_objects
               
        



