
from PySide6.QtCore import (Qt,  QTimer, QFile, QIODevice)
from PySide6.QtGui import (QColor,QFontDatabase,QFont)
from PySide6.QtWidgets import ( QMainWindow, QGraphicsDropShadowEffect)

from ui import ui_splash_screen
from clases import main_window



counter=0
class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = ui_splash_screen.Ui_SplashScreen()
		self.ui.setupUi(self)

		#Ocultar barra ventana
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground)

		#Sombra de ventana
		self.shadow_splash = QGraphicsDropShadowEffect(self)
		self.shadow_splash.setBlurRadius(20)
		self.shadow_splash.setXOffset(0)
		self.shadow_splash.setYOffset(0)
		self.shadow_splash.setColor(QColor(255,255,255,60))
		self.ui.fondoFrame.setGraphicsEffect(self.shadow_splash)


		#Tiempo de espera
		self.timer_splash = QTimer()
		self.timer_splash.timeout.connect(self.progress)


		############################################
		#########   CAMBIAR a 60 seg ###############
		self.timer_splash.start(6)
		############################################

		# Etiqueta de texto cambiando
		self.ui.label_informacion.setText("Cargando<strong> . . . </strong>")
		QTimer.singleShot(1000, lambda: self.ui.label_informacion.setText("Actualizando proyectos recientes<strong> . . . </strong>"))
		QTimer.singleShot(3000, lambda: self.ui.label_informacion.setText("Ajustando configuración de usuario<strong> . . .</strong>"))
		QTimer.singleShot(5000, lambda: self.ui.label_informacion.setText("Inicializando software <strong> . . .</strong>"))

		self.show()

	def progress(self):
		global counter
		self.ui.progressBar_splash.setValue(counter)
		if counter > 100:
			self.timer_splash.stop()
			self.main_window = main_window.MainWindow()
			self.main_window.show()
			self.close()
		counter +=1

