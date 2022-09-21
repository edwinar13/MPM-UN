""" Este módulo contiene la clase Ui_FormDraw, para incluirla en main window, es el frame que contiene la parte del dibujo."""


from PySide6.QtCore import (Signal,QRectF,Qt,QPointF)
from PySide6.QtWidgets import (QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu)
from PySide6.QtGui import (QPen,QBrush,
                            QPainter,QPixmap,QPolygonF,QPainterPath,QFont)
from ui import ui_frame_draw
from clases import class_ui_widget_draw_menu_data
from clases import class_ui_widget_draw_menu_mesh
from clases import class_projects
from clases import class_graphics

import math
class FrameDraw(QFrame, ui_frame_draw.Ui_FormDraw):
    """Esta clase crea el QFrame draw para agregarlo a main window. """ 
    signal_home_open = Signal(str)
    signal_home_new = Signal()

    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str) 

    signal_project_save_state = Signal(bool)


    signal_coor_mouse = Signal(list)

    def __init__(self, parent = None, ):
        super(FrameDraw, self).__init__(parent)
        self.setupUi(self)

        # Configura la UI
        self.__configUi()
        
        # Establece los eventos de la UI
        self.__initEventUi()


    """
    def resizeEvent(self, event):
        #print("Tamaño: {}".format(self.viewport().rect()))
        #self.graphicsView_draw.setSceneRect(QRectF(0,0,1000,1000))
        pass
    """
 
   

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
    ###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 

        # ::::::::::   AJUSTA EL SPLITTER PARA LA ALTURA DE LA CONSOLA  ::::::::::::
        self.splitter.setStretchFactor(0, 1)      
        self.splitter.setSizes([100,1]) 
        

        # ::::::::::::::::::   INICIANDO  DRAW  QGraphics  ::::::::::::::::::

        self.scene_draw = class_graphics.GraphicsSceneDraw()
        self.scene_draw.setSceneRect(QRectF(-200, -200, 400, 400))
        self.view_draw = class_graphics.GraphicsViewDraw(self.scene_draw)       
        self.horizontalLayout_graphics.addWidget(self.view_draw)
        
        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-DATA  ::::::::::::::::::
        self.drawMenuData = class_ui_widget_draw_menu_data.WidgetDrawMenuData()        
        self.horizontalLayout_draw.addWidget(self.drawMenuData)

        # ::::::::::::::::::   INICIANDO FRAME DRAW-MENU-MESH  ::::::::::::::::::
        self.drawMenuMesh = class_ui_widget_draw_menu_mesh.WidgetDrawMenuMesh()        
        self.horizontalLayout_draw.addWidget(self.drawMenuMesh)

        # ::::::::::::::::::   AJUSTES ADICIONALES  ::::::::::::::::::
        self.label_console.setVisible(False)
        self.showHideDrawMenu("Data")


    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-DATA :::::::::::::::::
        self.drawMenuData.signal_msn_critical.connect(self.showMessageStatusBarCritical)
        self.drawMenuData.signal_msn_satisfactory.connect(self.showMessageStatusBarSatisfactory)
        self.drawMenuData.signal_msn_informative.connect(self.showMessageStatusBarInformative)
        self.drawMenuData.signal_project_save_state.connect(self.__projectSaveState)

        # ::::::::::::::::::   SEÑAL>>RANURA FRAME-DRAW-MENU-MESH :::::::::::::::::
        self.drawMenuMesh.signal_paint_line.connect(self.__clickedToolButtonDrawPaintLine)
        self.drawMenuMesh.signal_paint_polyline.connect(self.__clickedToolButtonDrawPaintPolyline)
        self.drawMenuMesh.signal_paint_rectangle.connect(self.__clickedToolButtonDrawPaintRectangle)

        self.drawMenuMesh.signal_paint_move.connect(self.__clickedToolButtonDrawPaintMove)
        self.drawMenuMesh.signal_paint_rotate.connect(self.__clickedToolButtonDrawPaintRotate)
        self.drawMenuMesh.signal_paint_copy.connect(self.__clickedToolButtonDrawPaintCopy)
        self.drawMenuMesh.signal_paint_erase.connect(self.__clickedToolButtonDrawPaintErase)

        # ::::::::::::::::::   SEÑAL>>RANURA SCENE DRAW :::::::::::::::::        
        self.scene_draw.coor_mouse.connect(self.coor_mouse)
        '''        
        self.scene_draw.item_inserted.connect(self.item_inserted)
        self.scene_draw.text_inserted.connect(self.text_inserted)
        self.scene_draw.item_selected.connect(self.item_selected)
        self.scene_draw.item_selected.connect(self.item_selected)
        '''

        # ::::::::::::::::::::      EVENTOS FRAME DRAW     ::::::::::::::::::::
        self.toolButton_closeConsole.clicked.connect(self.__clickedToolButtonCloseConsole)



    ###############################################################################
    # ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
    ###############################################################################
    """ Métodos para los eventos de los botones y widget """
    def __clickedToolButtonCloseConsole(self):
        self.splitter.setSizes([1,0]) 

    def __clickedToolButtonDrawPaintLine(self):
        pass
        '''
        self.graphicsView_draw.isObject = 0
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        self.msnConsole("Command","_Line")
        self.msnLabelConsole("LINEA [Primer punto]: ")
        '''

    def __clickedToolButtonDrawPaintPolyline(self):
        pass
        '''
        self.graphicsView_draw.isObject = 1
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        '''

    def __clickedToolButtonDrawPaintRectangle(self):
        pass
        '''
        self.graphicsView_draw.isObject = 2
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        '''

    def __clickedToolButtonDrawPaintMove(self):
        pass

    def __clickedToolButtonDrawPaintRotate(self):
        pass
        '''
        if self.graphicsView_draw.isClear == False:
            self.graphicsView_draw.isClear = True
        else:
            self.graphicsView_draw.isClear = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.graphicsScene_draw.clear()
        '''

    def __clickedToolButtonDrawPaintCopy(self):
        pass
        '''
        if self.graphicsView_draw.isLine == False:
            self.graphicsView_draw.isLine = True
        else:
            self.graphicsView_draw.isLine = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isDelate = False
        self.graphicsView_draw.isClear = False
        '''

    def __clickedToolButtonDrawPaintErase(self):
        pass
        '''
        if self.graphicsView_draw.isDelate == False:
            self.graphicsView_draw.isDelate = True
        else:
            self.graphicsView_draw.isDelate = False

        self.graphicsView_draw.isObject = None
        self.graphicsView_draw.isLine = False
        self.graphicsView_draw.isClear = False
        '''

    def showHideDrawMenu(self,name_menu_view):
        """Muestra el menú seleccionado.

        Args:
            name_menu_view(str): nombre del meú a mostrar
                                : "Data"
                                : "Mesh"

        """
        self.drawMenuData.setVisible(False)
        self.drawMenuMesh.setVisible(False)
        if name_menu_view == "Data":
            self.drawMenuData.setVisible(True)
        elif name_menu_view == "Mesh":
            self.drawMenuMesh.setVisible(True)
        elif name_menu_view == "Point":
            pass
            #self.drawMenuPoint.setVisible(True)
        elif name_menu_view == "Boundary":
            pass
            #self.drawMenuBoundary.setVisible(True)

    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
    ###############################################################################
    def configDrawMenuData(self,project:class_projects.Project):
        """Configura el menú data de la vista draw.

        Args:
            project(Project): Objeto del proyecto actual

        """ 
        
        self.drawMenuData.initDrawMenuDataProject(project)

    def __projectSaveState(self, there_are_changes):
        """Recibe la señal del estado del guardado del proyecto y remite la misma, señal a main window.

        Args:
            there_are_changes(bool): True >>> si se realizó cambios en el proyecto

        """
        self.signal_project_save_state.emit(there_are_changes)

    def mode_origin_draw(self,mode):
        self.scene_draw.mode_axis=mode
        self.view_draw.scale_view(math.pow(1.1, +0.5))
        self.view_draw.scale_view(math.pow(1.1, -0.5))

    def mode_grid_draw(self,mode):
        self.scene_draw.mode_grid=mode
        self.view_draw.scale_view(math.pow(1.1, +0.5))
        self.view_draw.scale_view(math.pow(1.1, -0.5))



    ###############################################################################
    # ::::::::::::::::::::        MÉTODOS PARA MENSAJES        ::::::::::::::::::::
    ############################################################################### 
    def showMessageStatusBarCritical(self,msn):
        """Recibe la señal de mensaje crítico y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje critico

        """
        self.msnConsole("Error",msn)
        self.signal_msn_critical.emit(msn)

    def showMessageStatusBarSatisfactory(self,msn):
        """Recibe la señal de mensaje satisfactorio y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje satisfactorio

        """ 
        self.msnConsole("Running",msn)
        self.signal_msn_satisfactory.emit(msn)

    def showMessageStatusBarInformative(self,msn):
        """Recibe la señal de mensaje informativo y remite la misma, señal a main window para imprimir en barra de estado.

        Args:
            msn(str): Mensaje informativo

        """ 
        self.msnConsole("Command",msn)
        self.signal_msn_informative.emit(msn)

    def msnConsole(self, type_msn, msn):
        """Imprime mensaje en la consola.

        Args:
            type_msn(str): tipo de mensaje a mostrar
                    : Error
                    : Warning
                    : Running
                    : Command
                    : Information
            msn(str): Mensaje a mostrar

        """ 
        if type_msn == "Error":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f94646;">Error:       </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)

        elif type_msn == "Warning":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#c8cc8e;">Warning:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Running":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#36c9c6;">Running:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Command":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#f28123;">Command:     </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        elif type_msn == "Information":
            text_to_add = u'<a><span style="font-family:Ubuntu; font-size:8pt; color:#999999;">information: </span> <span style="font-family:Ubuntu; font-size:8pt; font-style:italic;"> {} </span> </a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        else:
            text_to_add = u'<a> <span>Command:</span><span> {} </span></a>'.format(msn)
            self.textBrowser_2.append(text_to_add)
        self.textBrowser_2.verticalScrollBar().maximum()

    def msnLabelConsole(self, msn):
        """Imprime mensaje en el label la consola.

        Args:

            msn(str): Mensaje a mostrar

        """ 
        self.label_console.setText(msn)
        self.label_console.setVisible(True)
        self.lineEdit_console.setFocus()

    def coor_mouse(self,coor_list):
        self.signal_coor_mouse.emit(coor_list)
