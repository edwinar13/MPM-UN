
import sys
from PySide6.QtCore import (Qt,  QTimer, QFile, QIODevice, QMetaObject, QCoreApplication)
from PySide6.QtGui import (QColor,QFontDatabase,QFont)
from PySide6.QtWidgets import ( QMainWindow,QToolButton,
QFrame, QGraphicsDropShadowEffect, QPushButton, QLabel, 
QVBoxLayout,QHBoxLayout,QGridLayout)
from PySide6.QtUiTools import QUiLoader
from pathlib import Path
from ui import ui_main_window
from ui import ui_frame_inicio
from ui import ui_frame_draw


class Project():
	pass


class MainWindow(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = ui_main_window.Ui_MainWindow()		
		self.ui.setupUi(self)
		self.showMaximized()


		#self.frame_inicio = ui_frame_inicio.Ui_frame_inicio_container()
		#self.frame_draw = ui_frame_draw.Ui_Frame()
		#self.frame_resultado= ui_frame_resultado.Ui_FrameResultado()
	

		#self.ui.verticalLayout_contenedor.addWidget(self.frame_inicio)
		#self.ui.verticalLayout_contenedor.addWidget(self.frame_draw)
		#self.ui.verticalLayout_contenedor.addWidget(self.frame_resultado)
		#self.frame_inicio.setupUi(self)
		#self.frame_resultado.setupUi(self)
		#self.frame_draw.setupUi(self)
		#self.frame_resultado.setStyleSheet("background-color: green;") 
		#self.frame_draw.setStyleSheet("background-color: red;") 

		
		############   CONFIGURANDO VENTANA DE INICIO #####################
		self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
		self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
		self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")
		self.ui.splitter.setStretchFactor(0, 100)
		self.ui.splitter.setStretchFactor(1, 0)		
		self.ui.splitter.setSizes([100,100]) 
		self.ui.statusbar.showMessage("Programa iniciado correctamente ",6000)
		self.ui.statusbar.setStyleSheet("color: #DDDDDD;")



		'''
		self.button = QLabel("Click me!")
		self.text = QLabel("Hello World", alignment=Qt.AlignCenter)
		self.frames = Ui_FrameResultado()
		

		#self.layout = QVBoxLayout(self)
		self.window.verticalLayout_contenedor.addWidget(self.text)
		self.window.verticalLayout_contenedor.addWidget(self.frames)

		self.button.setStyleSheet("background-color: yellow;") 
		self.text.setStyleSheet("background-color: red;") 
		self.frames.setStyleSheet("background-color: white;") 

		self.window.verticalLayout_contenedor.addWidget(self.button)

		'''

		'''
		'''
		
		# ::::::::::::::::::::::::::::::   EVENTOS WIDGET  ::::::::::::::::::::::::::::::
		self.ui.toolButton_inicio.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_data.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_malla.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_puntos.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_contorno.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_resultados.clicked.connect(self.onClickedToolButtonMenuLat)
		self.ui.toolButton_config.clicked.connect(self.onClickedToolButtonMenuLat)

		# ::::::::::::::::::::::::::::::   EVENTOS TECLADO ::::::::::::::::::::::::::::::
		self.ui.actionNuevo.setShortcut('Ctrl+n')
		self.ui.actionNuevo.setStatusTip('Nuevo')
		#self.ui.actionNuevo.triggered.connect(self.onTriggeredactionNuevo)




		

	def onClickedToolButtonMenuLat(self):
		self.hideFrameToolButton()
		buttonSelected = self.sender()
		nameButton = buttonSelected.objectName()
		print(nameButton)
		if nameButton=="toolButton_inicio":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_home)
			self.ui.frame_inicio.setStyleSheet("background-color: #36C9C6;")
			self.ui.frame_inicioInf.setStyleSheet("background-color: #2B2B2B;")  

		if nameButton=="toolButton_data":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
			self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_data)
			self.ui.frame_data.setStyleSheet("background-color: #36C9C6;") 
			self.ui.frame_dataInf.setStyleSheet("background-color: #2B2B2B;") 

		if nameButton=="toolButton_malla":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
			self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_mesh)
			self.ui.frame_malla.setStyleSheet("background-color: #36C9C6;") 
			self.ui.frame_mallaInf.setStyleSheet("background-color: #2B2B2B;") 

		if nameButton=="toolButton_puntos":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
			self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_point)
			self.ui.frame_puntos.setStyleSheet("background-color: #36C9C6;") 
			self.ui.frame_puntosInf.setStyleSheet("background-color: #2B2B2B;") 

		if nameButton=="toolButton_contorno":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_draw)
			self.ui.stackedWidget_subMenu.setCurrentWidget(self.ui.page_contour)
			self.ui.frame_contorno.setStyleSheet("background-color: #36C9C6;") 
			self.ui.frame_contornoInf.setStyleSheet("background-color: #2B2B2B;") 

		if nameButton=="toolButton_resultados":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_view)
			self.ui.frame_resultados.setStyleSheet("background-color: #36C9C6;") 
			self.ui.frame_resultadosInf.setStyleSheet("background-color: #2B2B2B;") 

		if nameButton=="toolButton_config":
			self.ui.stackedWidget_container.setCurrentWidget(self.ui.page_config)
		'''
		Azules #36C9C6 #00BDB9 #77ACA2
		rojos #910D3F #C70039 #F94646
		naranjas #D34E24 #F28123 #F7F052
		'''

	def hideFrameToolButton(self):
		self.ui.frame_inicio.setStyleSheet("background-color: #333333;") 
		self.ui.frame_data.setStyleSheet("background-color: #333333;") 
		self.ui.frame_malla.setStyleSheet("background-color: #333333;") 
		self.ui.frame_puntos.setStyleSheet("background-color: #333333;") 
		self.ui.frame_contorno.setStyleSheet("background-color: #333333;") 
		self.ui.frame_resultados.setStyleSheet("background-color: #333333;") 

		self.ui.frame_resultadosInf.setStyleSheet("background-color: #333333;") 
		self.ui.frame_inicioInf.setStyleSheet("background-color: #333333;") 
		self.ui.frame_dataInf.setStyleSheet("background-color: #333333;") 
		self.ui.frame_contornoInf.setStyleSheet("background-color: #333333;") 
		self.ui.frame_puntosInf.setStyleSheet("background-color: #333333;") 
		self.ui.frame_mallaInf.setStyleSheet("background-color: #333333;") 
		