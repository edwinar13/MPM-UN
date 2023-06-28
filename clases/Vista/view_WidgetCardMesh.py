""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-mesh
Es el widget card de cada malla."""
from PySide6.QtCore import ( QSize, Signal)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)

from ui.ui_widget_draw_mesh_card import Ui_FormDrawMeshCard
from clases import class_ui_dialog_msg


 

class viewCardDrawMesh(QFrame, Ui_FormDrawMeshCard):
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
    signal_update_mesh = Signal()
    
 
    def __init__(self,controller_CardMesh):
        super(viewCardDrawMesh, self).__init__()
        self.setupUi(self)
        
        # esto solo para que sirva Slot-Signal
        self.controller_CardMesh = controller_CardMesh

        self.__card_show_hide_mesh = True
        self.__card_color_mesh = None
        self.__card_name_mesh = None
        self.card_color_mesh_prev = None




        # Configura la UI
        self.__configUi()
        self.__initEventUi()


 
       
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
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
        
        '''
        # se actualiza informacion del card
        self.label_cardNameMesh.setText(u"{}".format(self.__card_name_mesh))
        self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_mesh))
        '''
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

        self.lineEdit_nameMesh.setText(self.label_cardNameMesh.text())
        self.lineEdit_nameMesh.setFocus()
        self.card_color_mesh_prev = self.__card_color_mesh

    def __clickedToolButtonColorMesh(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__card_color_mesh=color.name()
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
        self.signal_update_mesh.emit()

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
                                "¿Quieres eliminar la malla {} ?".format(self.getName()), 
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
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.__card_name_mesh

    def getColor(self):
        return self.__card_color_mesh


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
 
    def showData(self, name, color):        
        self.label_cardNameMesh.setText(u"{}".format(name))
        self.__card_color_mesh = color
        self.frame_color.setStyleSheet('background-color : {}'.format(color))



