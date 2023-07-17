""" Este módulo contiene la clase Ui_FormDrawBoundaryCard, para incluirla en frame draw-menu-boundary
Es el widget card de cada malla."""
from PySide6.QtCore import ( QSize, Signal)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)

from ui.ui_widget_draw_boundary_card import Ui_FormDrawBoundaryCard
from clases import class_ui_dialog_msg


class viewCardDrawBoundary(QFrame, Ui_FormDrawBoundaryCard):
    """Esta clase crea el QFrame boundary-card para agregarlo a Frame draw-menu-boundary. 
    Args:
            cardNameBoundary (str):      Nombre de la malla (default = "").
            cardColorBoundary (str):     Color de la malla (default = "").
            cardShowHideBoundary (bool): Estado para mostrar u ocultar la malla (default = True).
    Attributes:
            __card_name_boundary (str):       Nombre de la malla.
            __card_color_boundary (str):      Color de la malla.
            __card_show_hide_boundary (bool): Estado para mostrar u ocultar la malla.
    """    
    signal_hide_show_boundary = Signal(bool)
    signal_delete_boundary = Signal()
    signal_update_boundary = Signal()
        
    def __init__(self,controller_CardBoundary):
        super(viewCardDrawBoundary, self).__init__()
        self.setupUi(self)
        
        # esto solo para que sirva Slot-Signal
        self.controller_CardBoundary = controller_CardBoundary

        self.__card_show_hide_boundary = True
        self.__card_name_boundary = None
        

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
        
        self.lineEdit_nameBoundary.setVisible(False)
        self.toolButton_okBoundary.setVisible(False)
        self.toolButton_exitBoundary.setVisible(False)
     
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_showHideBoundary.clicked.connect(self.__clickedToolButtonShowHideBoundary)
        self.toolButton_closeBoundary.clicked.connect(self.__clickedToolButtonCloseBoundary)
        self.toolButton_editBoundary.clicked.connect(self.__clickedToolButtonEditBoundary)
        self.toolButton_okBoundary.clicked.connect(self.__clickedToolButtonOkBoundary)
        self.toolButton_exitBoundary.clicked.connect(self.__clickedToolButtonExitBoundary)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonExitBoundary(self):
 
        self.lineEdit_nameBoundary.setVisible(False)
        self.toolButton_okBoundary.setVisible(False)
        self.toolButton_exitBoundary.setVisible(False)
        self.toolButton_closeBoundary.setVisible(True)
        self.toolButton_editBoundary.setVisible(True)
        self.toolButton_showHideBoundary.setVisible(True)
        self.label_cardNameBoundary.setVisible(True)


    def __clickedToolButtonEditBoundary(self):
        self.lineEdit_nameBoundary.setVisible(True)
        self.toolButton_okBoundary.setVisible(True)
        self.toolButton_exitBoundary.setVisible(True)

        self.toolButton_closeBoundary.setVisible(False)
        self.toolButton_editBoundary.setVisible(False)
        self.toolButton_showHideBoundary.setVisible(False)
        self.label_cardNameBoundary.setVisible(False)

        self.lineEdit_nameBoundary.setText(self.label_cardNameBoundary.text())
        self.lineEdit_nameBoundary.setFocus()


    def __clickedToolButtonOkBoundary(self):
       
        self.lineEdit_nameBoundary.setVisible(False)
        self.toolButton_okBoundary.setVisible(False)
        self.toolButton_exitBoundary.setVisible(False)
        self.toolButton_closeBoundary.setVisible(True)
        self.toolButton_editBoundary.setVisible(True)
        self.toolButton_showHideBoundary.setVisible(True)
        self.label_cardNameBoundary.setVisible(True)

        self.__card_name_boundary = self.lineEdit_nameBoundary.text()
        self.lineEdit_nameBoundary.setText("")
        self.label_cardNameBoundary.setText(self.__card_name_boundary)
 
        self.signal_update_boundary.emit()

    def __clickedToolButtonShowHideBoundary(self):
        """ Muestra u oculta la malla """

        if self.__card_show_hide_boundary:            
            self.signal_hide_show_boundary.emit(False)
            
        else :            
            self.signal_hide_show_boundary.emit(True)
      
        
    def __clickedToolButtonCloseBoundary(self):
        

        dialoMsg = class_ui_dialog_msg.DialogMsg(self, 3, 
                                "¿Quieres eliminar el contorno {} ?".format(self.getName()), 
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
            
        self.signal_delete_boundary.emit()

        # Elimina la tarjeta
        self.deleteLater()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.__card_name_boundary


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
 
    def showData(self, name, Tx, Ty):        
        self.label_cardNameBoundary.setText(u"{}".format(name))
        style = "QFrameStyle_"
        if Tx:
            self.setPropertyStyle(self.frame_Tx, style, 2)
        else:
            self.setPropertyStyle(self.frame_Tx, style, 1)

        if Ty:
            self.setPropertyStyle(self.frame_Ty, style, 2)
        else:            
            self.setPropertyStyle(self.frame_Ty,style, 1)



    def setPropertyStyle(self, widget, style, property: int):
        widget.setProperty(style, property)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

        

    def showHideBoundary(self, value):
        """ Muestra u oculta la malla """
        self.__card_show_hide_boundary = value        
        if self.__card_show_hide_boundary:            
            self.toolButton_showHideBoundary.setIcon(self.icon_show)    
        else :                   
            self.toolButton_showHideBoundary.setIcon(self.icon_hide)

