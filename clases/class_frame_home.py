import time
from tokenize import String
from PySide6.QtCore import ( QObject,QEvent, Signal, Slot,QThread)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )

from ui import ui_frame_inicio_1

class FrameHome(QFrame, ui_frame_inicio_1.Ui_FormHome):
    signal_home_open = Signal()
    signal_home_new = Signal()
    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(FrameHome, self).__init__(parent)
        self.setupUi(self)

        # ::::::::::::::::::::   EVENTOS WIDGET FRAME INICIO ::::::::::::::::::::
        self.toolButton_abrirProyecto.clicked.connect(self.clickedToolButtonOpenProject)
        self.toolButton_nuevoProyecto.clicked.connect(self.clickedToolButtonNewProject)

    def clickedToolButtonOpenProject(self):
        self.signal_home_open.emit()
    def clickedToolButtonNewProject(self):
        self.signal_home_new.emit()


