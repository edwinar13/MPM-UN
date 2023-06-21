""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-mesh
Es el widget card de cada malla."""
from PySide6.QtCore import ( QSize, Signal, QPointF)
from PySide6.QtGui import (QColor,QIcon, QPolygonF, QPen)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QGraphicsItemGroup, QGraphicsPolygonItem, QColorDialog)

from ui import ui_widget_draw_mesh_card
from clases import class_general
from clases import class_ui_dialog_msg


 

class viewCardDrawMesh(QFrame, ui_widget_draw_mesh_card.Ui_FormDrawMeshCard):
    """Esta clase crea el QFrame mesh-card para agregarlo a Frame draw-menu-mesh. 

    Args:
            cardNameMesh (str):      Nombre de la malla (default = "").
            cardColorMesh (str):     Color de la malla (default = "").
            cardShowHideMesh (bool): Estado para mostrar u ocultar la malla (default = True).
            
    Attributes:
            __card_name_mesh (str):       Nombre de la malla.
            __card_color_mesh (str):      Color de la malla.
            __card_show_hide_mesh (bool): Estado para mostrar u ocultar la malla.

    """    
    signal_hide_show_mesh = Signal(bool)
    signal_delete_mesh = Signal()
    signal_update_mesh = Signal(dict)
    


    ##def __init__(self, parent, scene_draw, points, triangles, cardNameMesh="", cardColorMesh="#ffffff",cardShowHideMesh=True):
    def __init__(self,controller_CardMesh, points, triangles, cardNameMesh="", cardColorMesh="#ffffff"):
        #super(viewCardDrawMesh, self).__init__(parent)
        super(viewCardDrawMesh, self).__init__()
        self.setupUi(self)
        
        # Atributo
        ##self.__parent = parent
        self.controller_CardMesh = controller_CardMesh
        self.__card_name_mesh = cardNameMesh
        self.__card_color_mesh = cardColorMesh
        self.__card_show_hide_mesh = True

        self.__points = points
        self.__triangles = triangles


        # Configura la UI
        self._configUi()
    
        # Establece los eventos de la UI
        self.__initEventUi()


        self.setPointsTriangles()
        #self.drawTriangles()


        data={"name":self.__card_name_mesh,
            "color":self.__card_color_mesh,
            "points":self.__points,
            "triangles":self.__triangles,
            }
      
        ##self.scene_draw.admin.addMesh(name=self.__card_name_mesh,data=data)

   
    def setPointsTriangles(self):
        points = self.__points[:]
        triangles = self.__triangles[:]
        self.__points =[]
        self.__triangles =[]
        for point in points:
            self.__points.append([point[0],point[1]])
        for triangle in triangles:
            self.__triangles.append([int(triangle[0]),int(triangle[1]),int(triangle[2])])




       
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def _configUi(self):
        """Configura la interface de usuario (ui).""" 
        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,20,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show = QIcon()
        self.icon_show.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide = QIcon()
        self.icon_hide.addFile(u"recursos/iconos/iconos_menu_draw_mesh/not_view.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # se actualiza informacion del card
        self.label_cardNameMesh.setText(u"{}".format(self.__card_name_mesh))
        self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_mesh))


        self.lineEdit_nameMesh.setVisible(False)
        self.toolButton_colorMesh.setVisible(False)
        self.toolButton_okMesh.setVisible(False)
        self.toolButton_exitMesh.setVisible(False)
     



    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_showHideMesh.clicked.connect(self.__clickedToolButtonShowHideMesh)
        self.toolButton_closeMesh.clicked.connect(self.__clickedToolButtonCloseMesh)
        self.toolButton_editMesh.clicked.connect(self.__clickedToolButtonEditMesh)
        self.toolButton_colorMesh.clicked.connect(self.__clickedToolButtonColorMesh)
        self.toolButton_okMesh.clicked.connect(self.__clickedToolButtonOkMesh)
        self.toolButton_exitMesh.clicked.connect(self.__clickedToolButtonExitMesh)

        
     
        '''
        #este es una forma de darle evento a un frame
        observer = class_general.MouseObserver(self.label_cardNameMesh)
        '''


    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################




    def __clickedToolButtonExitMesh(self):

 
        self.lineEdit_nameMesh.setVisible(False)
        self.toolButton_colorMesh.setVisible(False)
        self.toolButton_okMesh.setVisible(False)
        self.toolButton_exitMesh.setVisible(False)
        self.frame_color.setFixedWidth(10)
        self.toolButton_closeMesh.setVisible(True)
        self.toolButton_editMesh.setVisible(True)
        self.toolButton_showHideMesh.setVisible(True)
        self.label_cardNameMesh.setVisible(True)

        self.__card_color_mesh=self.card_color_mesh_prev
        self.card_color_mesh_prev = None
        self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_mesh))

 


    def __clickedToolButtonOkMesh(self):

        name_prev =self.label_cardNameMesh.text()

        self.lineEdit_nameMesh.setVisible(False)
        self.toolButton_colorMesh.setVisible(False)
        self.toolButton_okMesh.setVisible(False)
        self.toolButton_exitMesh.setVisible(False)
        self.frame_color.setFixedWidth(10)
        self.toolButton_closeMesh.setVisible(True)
        self.toolButton_editMesh.setVisible(True)
        self.toolButton_showHideMesh.setVisible(True)
        self.label_cardNameMesh.setVisible(True)


        self.__card_name_mesh = self.lineEdit_nameMesh.text()
        self.lineEdit_nameMesh.setText("")
        self.label_cardNameMesh.setText(self.__card_name_mesh)


        self.card_color_mesh_prev = None

        data={"name_prev":name_prev,
            "name":self.__card_name_mesh,
            "color":self.__card_color_mesh,
            "points":self.__points,
            "triangles":self.__triangles,
            }        
        self.signal_update_mesh.emit(data)




    def __clickedToolButtonEditMesh(self):
        self.lineEdit_nameMesh.setVisible(True)
        self.toolButton_colorMesh.setVisible(True)
        self.toolButton_okMesh.setVisible(True)
        self.toolButton_exitMesh.setVisible(True)

        self.toolButton_closeMesh.setVisible(False)
        self.toolButton_editMesh.setVisible(False)
        self.toolButton_showHideMesh.setVisible(False)
        self.label_cardNameMesh.setVisible(False)
        self.frame_color.setFixedWidth(20)

        self.lineEdit_nameMesh.setText(self.__card_name_mesh)
        self.lineEdit_nameMesh.setFocus()
        self.card_color_mesh_prev = self.__card_color_mesh


    def __clickedToolButtonColorMesh(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__card_color_mesh=color.name()
            self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_mesh))


    def __clickedToolButtonShowHideMesh(self):
        """ Muestra u oculta la malla """

        if self.__card_show_hide_mesh:            
            self.__card_show_hide_mesh = False
            self.toolButton_showHideMesh.setIcon(self.icon_hide)
            
        else :            
            self.__card_show_hide_mesh = True
            self.toolButton_showHideMesh.setIcon(self.icon_show)    
      
        self.signal_hide_show_mesh.emit(self.__card_show_hide_mesh)


        
    def __clickedToolButtonCloseMesh(self):
        

        dialoMsg = class_ui_dialog_msg.DialogMsg(self, 3, 
                                "¿Quieres eliminar la malla {} ?".format(self.__card_name_mesh), 
                                "")
        dialoMsg.setTypeIcon(1)
        dialoMsg.setTextDescription("")
        dialoMsg.setModal(True)
        dialoMsg.exec()
        result = dialoMsg.getButtonSelected()

        #Guardar
        if result == "yes":
            print("# Guardar = {}".format(2))
            
        # No Guardar
        elif result == "not":
            print("# No Guardar")
            return

        elif result == "cancel" or result == "exit":
            print("# Cancelar")
            return
            
        self.signal_delete_mesh.emit()

        # Elimina la tarjeta
        self.deleteLater()





    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

 

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################

    '''
    def mousePressEvent(self, event):
        """Reimplantado el método mousePressEvent
        Args:
            event (QEvent): evento de ui
        """ 
        super().mousePressEvent(event)
        print("***** {}=  Reimplementando mousePressEvent {} *****".format(self.__card_name_mesh,event))
    '''


