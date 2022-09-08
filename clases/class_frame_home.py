from cgitb import enable
import time
from tokenize import String
from PySide6.QtCore import (Qt, QObject,QEvent, Signal, Slot,QThread)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )

from ui import ui_frame_inicio_2
import os




class FrameHome(QFrame, ui_frame_inicio_2.Ui_FormHome):
    signal_home_open = Signal(str)
    signal_home_new = Signal()
    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(FrameHome, self).__init__(parent)
        self.setupUi(self)

        self.pathApp=os.path.abspath(os.getcwd())
        #print(os.path.dirname(os.path.abspath(__file__)))

        self.scrollArea_1.verticalScrollBar().setEnabled(False)

        # ::::::::::::::::::::   EVENTOS WIDGET FRAME INICIO ::::::::::::::::::::
        self.toolButton_FH_cardNew_1.clicked.connect(self.clickedToolButtonNewProject)
        self.toolButton_FH_cardNew_2.clicked.connect(self.clickedToolButtonOpenProject_2)
        self.toolButton_FH_cardNew_3.clicked.connect(self.clickedToolButtonOpenProject_3)
        self.toolButton_FH_cardNew_4.clicked.connect(self.clickedToolButtonOpenProject_4)
        self.toolButton_FH_cardNew_5.clicked.connect(self.clickedToolButtonOpenProject_5)

    def clickedToolButtonOpenProject_2(self):        
        path=r"{}\recursos\ejemplos\Ejemplo vibracion barra empotrada.mpm".format(self.pathApp)
        self.emitSignalOpen(path=path)

    def clickedToolButtonOpenProject_3(self):
        path=r"{}\recursos\ejemplos\Ejemplo capacidad portante.mpm".format(self.pathApp)
        self.emitSignalOpen(path=path)

    def clickedToolButtonOpenProject_4(self):
        path=r"{}\recursos\ejemplos\Ejemplo disco deslizando en plano inclinado.mpm".format(self.pathApp)
        self.emitSignalOpen(path=path)

    def clickedToolButtonOpenProject_5(self):
        path=r"{}\recursos\ejemplos\Ejemplo falla de talud elastoplastico.mpm".format(self.pathApp)
        self.emitSignalOpen(path=path)

    def emitSignalOpen(self, path):
        path = path.replace('\\','/')
        self.signal_home_open.emit(path)




    def clickedToolButtonNewProject(self):
        self.signal_home_new.emit()
    
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("***** con  Reimplementando mousePressEvent {} *****".format(event))


