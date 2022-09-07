import time
from tokenize import String
from PySide6.QtCore import ( QObject,QEvent, Signal, Slot,QThread)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )

from ui import ui_widget_data_project

class DataProject(QFrame, ui_widget_data_project.Ui_FormDataProject):
    trigger = Signal(str)
    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(DataProject, self).__init__(parent)
        self.setupUi(self)

        """
        self.cardName = cardName
        self.cardDataTime = cardDataTime
        self.cardHour = cardHour
        self.cardPath = cardPath


        

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,0,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)
        """
