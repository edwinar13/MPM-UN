""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-mesh
Es el widget card de cada malla."""
from PySide6.QtCore import ( QSize, Signal, QEvent)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)
from ui.ui_widget_result_card_point import Ui_FormResultCardPoint
from clases import class_ui_dialog_msg
from clases.class_general import MouseObserver


class viewResultCardPoint(QFrame, Ui_FormResultCardPoint):

    signal_hide_show_point = Signal(bool)
    signal_delete_point = Signal()
    signal_update_color_point = Signal()
        
    def __init__(self,controller_Cardpoint):
        super(viewResultCardPoint, self).__init__()
        self.setupUi(self)
        
        # esto solo para que sirva Slot-Signal
        self.controller_Cardpoint = controller_Cardpoint

        self.__card_show_hide_point = True
        self.__card_color_point = None

        self.frame_mouse_observer = MouseObserver(self.frame_color)

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

        # Se agrega los dos iconos 
        self.icon_show = QIcon()
        self.icon_show.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide = QIcon()
        self.icon_hide.addFile(u"recursos/iconos/iconos_menu_draw_mesh/not_view.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        

     
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        self.toolButton_showHidePoint.clicked.connect(self.__clickedToolButtonShowHidePoint)
        self.toolButton_closePoint.clicked.connect(self.__clickedToolButtonClosePoint)
        #self.frame_color.clicked.connect(self.__clickedToolButtonColorPoint)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonShowHidePoint(self):
        """ Muestra u oculta la malla """

        if self.__card_show_hide_point:            
            self.signal_hide_show_point.emit(False)
            
        else :                  
            self.signal_hide_show_point.emit(True)
        
    def __clickedToolButtonClosePoint(self):                    
        self.signal_delete_point.emit()
        # Elimina la tarjeta
        self.deleteLater()

    
    def __clickedToolButtonColorPoint(self):
        color = QColorDialog.getColor(initial=QColor(self.__card_color_point))
        if color.isValid():
            self.__card_color_point=color.name()
            self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_point))
            self.signal_update_color_point.emit()




    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.label_cardNamePoint.text()

    def getColor(self):
        return self.__card_color_point

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
 
    def showData(self, name, color):        
        self.label_cardNamePoint.setText(u"{}".format(name))
        self.__card_color_point = color
        self.frame_color.setStyleSheet('background-color : {}'.format(color))



    def ShowHidePoint(self, value):
        """ Muestra u oculta la malla """
        self.__card_show_hide_point = value
        if self.__card_show_hide_point:            
            self.toolButton_showHidePoint.setIcon(self.icon_show)   
        else :            
            self.toolButton_showHidePoint.setIcon(self.icon_hide)            



    def event(self, event):        
        if event.type() == QEvent.Type.MouseButtonPress:
            clicked_widget = self.childAt(event.pos())
            if clicked_widget is not None and clicked_widget == self.frame_color:
                self.__clickedToolButtonColorPoint()
        return super().event(event)