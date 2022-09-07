import time
from tokenize import String
from PySide6.QtCore import ( QObject,QEvent, Signal, Slot,QThread)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )

from ui import ui_widget_card


class MouseObserver(QObject):
    def __init__(self, widget):
        super().__init__(widget)
        self._widget = widget
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self._widget

    def eventFilter(self, obj, event):
        if obj is self.widget and event.type() == QEvent.MouseButtonPress:
            print(">>>> con MouseObserver {} <<<<<".format(self.widget.objectName()))
           
        return super().eventFilter(obj, event)

class viewCardProject(QFrame, ui_widget_card.Ui_FormCard):
    trigger = Signal(str)
    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(viewCardProject, self).__init__(parent)
        self.setupUi(self)
        self.cardName = cardName
        self.cardDataTime = cardDataTime
        self.cardHour = cardHour
        self.cardPath = cardPath

    

        """
        Para button encontre dos formas mas faciles de conectar pero no pude mandar argumentos
        1) cunado se crea el objeto en el main window
                self.cardProject.pushButton.clicked.connect(self.onClickedToolButtonMenuLat)
        2) dentro de la clase
            self.pushButton.clicked.connect(self.parent().algo)
        """


        

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,0,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        observer = MouseObserver(self.label_cardName)
                
        self.setTextLabel()



    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("***** con  Reimplementando mousePressEvent {} *****".format(event))
        self.trigger.emit(self.cardPath)

    
    def handle_trigger(self):
        print ("trigger signal received")

    def setTextLabel(self):
        self.label_cardName.setText(u"{}".format(self.cardName))
        self.label_cardDataTime.setText(u"{}".format(self.cardDataTime))
        self.label_cardPath.setText(u"{}".format(self.cardHour))
        self.frame_card.setToolTip(u"{}".format(self.cardPath))

    def setNamesWidges (self,numberProject):
        self.frame_card.setObjectName(u"frame_card_{}".format(numberProject))
        self.label_img.setObjectName(u"label_img_{}".format(numberProject))
        self.label_cardName.setObjectName(u"label_cardName_{}".format(numberProject))
        self.label_cardDataTime.setObjectName(u"label_cardDataTime_{}".format(numberProject))
        self.label_cardPath.setObjectName(u"label_cardPath_{}".format(numberProject))
        self.pushButton.setObjectName(u"pushButton_{}".format(numberProject))
        self.setObjectName(u"card_{}".format(numberProject))

    def printNamesWidges (self):
        print(self.frame_card.objectName)
        print(self.label_img.objectName)
        print(self.label_cardName.objectName)
        print(self.label_cardDataTime.objectName)
        print(self.label_cardPath.objectName)

