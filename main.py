
import sys
import random
from PySide6.QtCore import (Qt, Slot, QTimer)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import (QApplication, QMainWindow,
								QPushButton, QLabel, QHBoxLayout,QFrame,QSplitter,QVBoxLayout,QWidget, QGraphicsDropShadowEffect,QStyleFactory)

from UI.ui_splash_screen import Ui_SplashScreen
#from UI.ui_main_window import Ui_MainWindow

counter=0
class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_MainWindow()		
		self.ui.setupUi(self)
		self.ui.splitter.setStretchFactor(0, 100)
		self.ui.splitter.setStretchFactor(1, 0)        
		self.ui.splitter.setSizes([100,100]) 



class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_SplashScreen()
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
		self.timer_splash.start(60)

		# Etiqueta de texto cambiando
		self.ui.label_load.setText("Cargando<strong> . . . </strong>")
		QTimer.singleShot(2000, lambda: self.ui.label_load.setText("Actualizando proyectos recientes<strong> . . . </strong>"))
		QTimer.singleShot(4000, lambda: self.ui.label_load.setText("Ajustando configuración de usuario<strong> . . .</strong>"))
		QTimer.singleShot(5000, lambda: self.ui.label_load.setText("Inicializando programa <strong> . . .</strong>"))

		self.show()

	def progress(self):
		global counter
		self.ui.progressBar.setValue(counter)
		if counter > 100:
			self.timer_splash.stop()
			#self.main_window = MainWindow()
			#self.main_window.show()
			self.close()
		counter +=1

		



if __name__ == '__main__':
	#database.newApp()
	app = QApplication(sys.argv)
	window = SplashScreen()
	#window.show()
	sys.exit(app.exec())