""" Este módulo contiene la clase Ui_DialogMsg, mostar mensajes."""
from PySide6.QtCore import (Signal,Qt,QSize)
from PySide6.QtGui import (QColor,QPixmap)
from PySide6.QtWidgets import ( QDialog, QGraphicsDropShadowEffect )
from ui import ui_dialog_loanding

class DialogLoanding(QDialog, ui_dialog_loanding.Ui_DialogLoanding):
 
    def __init__(self, parent = None):
        super(DialogLoanding, self).__init__(parent)
        self.setupUi(self)
        
        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()

    def showEvent(self, event):
        # Llamamos al showEvent de la clase base para asegurarnos de que se ejecuten las operaciones normales
        super().showEvent(event)


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """Configura la interface de usuario (ui).""" 

        #Ocultar barra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,0,100))
        self.frame_content.setGraphicsEffect(self.shadow_card)

        self.shadow_dialog = QGraphicsDropShadowEffect(self)
        self.shadow_dialog.setBlurRadius(15)
        self.shadow_dialog.setXOffset(0)
        self.shadow_dialog.setYOffset(0)
        self.shadow_dialog.setColor(QColor(255,255,255,100))
        self.frame_dialog.setGraphicsEffect(self.shadow_dialog)

        #ocultar botones
        self.pushButton_accept.setVisible(True)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal).""" 

        # ::::::::::::::::::::      EVENTOS DRAW MENU DATA     ::::::::::::::::::::
        self.pushButton_accept.clicked.connect(self.__clickedPushButtonAccept)


    ###############################################################################
	# ::::::::::::::::::::           GETTERS Y SETTERS         ::::::::::::::::::::
	###############################################################################


    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    ''' Métodos para los eventos de los botones '''

    def __clickedPushButtonAccept(self):
        """ Establece como botón deseleccionado accept.""" 
        self.__button_selected = "accept"
        self.accept()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    
