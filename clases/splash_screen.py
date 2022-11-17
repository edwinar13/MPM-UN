""" Este módulo contiene la clase iniciar Ui_SplashScreen que es la ventana de Bienvenida"""

from PySide6.QtCore import (Qt,  QTimer)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QMainWindow, QGraphicsDropShadowEffect,QDialog)
from ui import ui_splash_screen
from clases import main_window
from clases import class_ui_dialog_msg
import sys
import os

class SplashScreen(QMainWindow):
    """Esta clase crea la ventana QMainWindow de la ventana de cargando.

    Args:
        createDataBase(CreateDataBase): Objeto para crear bases de datos.          

    Attributes:
        counter (int): Contador para tiempo.
        createDataBase(CreateDataBase): Objeto para crear bases de datos.
    
    """ 
    def __init__(self, createDataBase):
        QMainWindow.__init__(self)

        # Instancia de ui de pantalla de bienvenida
        self.ui = ui_splash_screen.Ui_SplashScreen()
        self.ui.setupUi(self)

        # Atributo
        self.__createDataBase = createDataBase
        self.counter = 0
        
        # Tiempo de espera para iniciar main window
        self.timer_splash = QTimer()
        self.timer_splash.timeout.connect(self.__progress)
        """              ███▀▀▀▀▀ CAMBIAR start a 60 seg ▀▀▀▀▀███                 """
        self.timer_splash.start(6)

        # Configura la UI
        self.__configUi()

        # Cambio de texto en etiqueta		
        QTimer.singleShot(1000, lambda: self.ui.label_info.setText("Actualizando proyectos recientes<strong> . . . </strong>"))
        QTimer.singleShot(3000, lambda: self.ui.label_info.setText("Ajustando configuración de usuario<strong> . . .</strong>"))
        QTimer.singleShot(5000, lambda: self.ui.label_info.setText("Inicializando software <strong> . . .</strong>"))

        self.show()
        
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """Configura la interface de usuario (ui) de splash screen""" 
        #Ocultar barra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Sombra de ventana
        self.shadow_splash = QGraphicsDropShadowEffect(self)
        self.shadow_splash.setBlurRadius(20)
        self.shadow_splash.setXOffset(0)
        self.shadow_splash.setYOffset(0)
        self.shadow_splash.setColor(QColor(255,255,255,60))
        self.ui.frame_background.setGraphicsEffect(self.shadow_splash)

        self.ui.label_info.setText("Cargando<strong> . . . </strong>")

    def __progress(self):
        """Contador del tiempo de espera, al finalizar tiempo inicia main window """ 
        self.counter
        self.ui.progressBar_load.setValue(self.counter)
        if self.counter > 100:
            self.timer_splash.stop()
            self.main_window = main_window.MainWindow(self.__createDataBase)
            self.main_window.show()
            self.close()                
        self.counter +=1

