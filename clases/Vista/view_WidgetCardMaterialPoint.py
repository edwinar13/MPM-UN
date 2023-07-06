""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-materialPoint
Es el widget card de cada materialPoint."""
from PySide6.QtCore import ( QSize, Signal)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)

from ui.ui_widget_draw_material_point_card import Ui_FormDrawMaterialPointCard
from clases import class_ui_dialog_msg

 
class viewCardDrawMaterialPoint(QFrame, Ui_FormDrawMaterialPointCard):
    """Esta clase crea el QFrame materialPoint-card para agregarlo a Frame draw-menu-materialPoint. 

    Args:
            cardNameMesh (str):      Nombre de la malla (default = "").
            cardColorMesh (str):     Color de la malla (default = "").
            cardShowHideMesh (bool): Estado para mostrar u ocultar la malla (default = True).
            
    Attributes:
            __card_name_materialPoint (str):       Nombre de la malla.
            __card_color_material_point (str):      Color de la malla.
            __card_show_hide_material_point (bool): Estado para mostrar u ocultar la malla.

    """    
    signal_hide_show_material_point = Signal(bool)
    signal_delete_material_point = Signal()
    signal_update_material_point = Signal()
    
    def __init__(self, controller_CardMesh):
        super(viewCardDrawMaterialPoint, self).__init__()
        self.setupUi(self)

        # esto solo para que sirva Slot-Signal
        self.controller_CardMesh = controller_CardMesh

        self.__card_show_hide_material_point = True
        self.__card_color_material_point = None
        self.__card_name_material_point = None
        self.card_color_material_point_prev = None
        
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
        
        self.lineEdit_nameMaterialPoint.setVisible(False)
        self.toolButton_colorMaterialPoint.setVisible(False)
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)
     
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_showHideMaterialPoint.clicked.connect(self.__clickedToolButtonShowHideMaterialPoint)
        self.toolButton_closeMaterialPoint.clicked.connect(self.__clickedToolButtonCloseMaterialPoint)
        self.toolButton_editMaterialPoint.clicked.connect(self.__clickedToolButtonEditMaterialPoint)
        self.toolButton_colorMaterialPoint.clicked.connect(self.__clickedToolButtonColorMaterialPoint)
        self.toolButton_okMaterialPoint.clicked.connect(self.__clickedToolButtonOkMaterialPoint)
        self.toolButton_exitMaterialPoint.clicked.connect(self.__clickedToolButtonExitMaterialPoint)
    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonExitMaterialPoint(self): 
        self.lineEdit_nameMaterialPoint.setVisible(False)
        self.toolButton_colorMaterialPoint.setVisible(False)
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)
        self.frame_color.setFixedWidth(10)
        self.toolButton_closeMaterialPoint.setVisible(True)
        self.toolButton_editMaterialPoint.setVisible(True)
        self.toolButton_showHideMaterialPoint.setVisible(True)
        self.label_cardNameMaterialPoint.setVisible(True)

        self.__card_color_material_point=self.card_color_material_point_prev
        self.card_color_material_point_prev = None
        self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_material_point))
 
    def __clickedToolButtonEditMaterialPoint(self):
        self.lineEdit_nameMaterialPoint.setVisible(True)
        self.toolButton_colorMaterialPoint.setVisible(True)
        self.toolButton_okMaterialPoint.setVisible(True)
        self.toolButton_exitMaterialPoint.setVisible(True)

        self.toolButton_closeMaterialPoint.setVisible(False)
        self.toolButton_editMaterialPoint.setVisible(False)
        self.toolButton_showHideMaterialPoint.setVisible(False)
        self.label_cardNameMaterialPoint.setVisible(False)
        self.frame_color.setFixedWidth(20)

        self.lineEdit_nameMaterialPoint.setText(self.label_cardNameMaterialPoint.text())
        self.lineEdit_nameMaterialPoint.setFocus()
        self.card_color_material_point_prev = self.__card_color_material_point

    def __clickedToolButtonColorMaterialPoint(self):
        color = QColorDialog.getColor(initial=QColor(200,200,200))
        if color.isValid():
            self.__card_color_material_point=color.name()
            self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_material_point))

    def __clickedToolButtonOkMaterialPoint(self):

        self.lineEdit_nameMaterialPoint.setVisible(False)
        self.toolButton_colorMaterialPoint.setVisible(False)
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)
        self.frame_color.setFixedWidth(10)
        self.toolButton_closeMaterialPoint.setVisible(True)
        self.toolButton_editMaterialPoint.setVisible(True)
        self.toolButton_showHideMaterialPoint.setVisible(True)
        self.label_cardNameMaterialPoint.setVisible(True)

        self.__card_name_material_point = self.lineEdit_nameMaterialPoint.text()
        self.lineEdit_nameMaterialPoint.setText("")
        self.label_cardNameMaterialPoint.setText(self.__card_name_material_point)

        self.card_color_material_point_prev = None
        self.signal_update_material_point.emit()
        
    def __clickedToolButtonShowHideMaterialPoint(self):
        """ Muestra u oculta la malla """

        if self.__card_show_hide_material_point:            
            self.__card_show_hide_material_point = False
            self.toolButton_showHideMaterialPoint.setIcon(self.icon_hide)
            
        else :            
            self.__card_show_hide_material_point = True
            self.toolButton_showHideMaterialPoint.setIcon(self.icon_show)    
      
        self.signal_hide_show_material_point.emit(self.__card_show_hide_material_point)
         
    def __clickedToolButtonCloseMaterialPoint(self):       
        dialoMsg = class_ui_dialog_msg.DialogMsg(self, 3, 
                                "¿Quieres eliminar los puntos materiales {} ?".format(self.getName()), 
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
            
        self.signal_delete_material_point.emit()

        # Elimina la tarjeta
        self.deleteLater()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        self.__card_name_material_point = self.label_cardNameMaterialPoint.text()
        return self.__card_name_material_point

    def getColor(self):
        return self.__card_color_material_point

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def showData(self, name, color):        
        self.label_cardNameMaterialPoint.setText(u"{}".format(name))
        self.__card_color_material_point = color
        self.frame_color.setStyleSheet('background-color : {}'.format(color))





















       
