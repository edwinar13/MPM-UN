import time
from tokenize import String
from PySide6.QtCore import ( QObject,QEvent, Signal, Slot,QThread)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )

from ui import ui_widget_card

class Communicate(QObject):
    sig = Signal(str) 

class Worker(QThread):

    def __init__(self, parent=None, communicate=Communicate()):
        super(Worker, self).__init__(parent)
        self.communicate = communicate
        # self.count = 0
        self.loop = loop(communicate= self.communicate)

    def run(self):

        self.loop.methodA()

        ## Original code without being in class loop and method loopA
        # while True:
        #     time.sleep(1)
        #     self.count += 1
        #     if (self.count % 1 == 0):
        #         self.sig.emit(f"Timer: {self.count} s")

# Newly added class with method "methodA"
class loop(object):

    def __init__(self, communicate=Communicate()):
        self.count = 0
        self.communicate = communicate

    def methodA(self):

        while True:
            time.sleep(1)
            self.count += 1
            if (self.count % 1 == 0):
                self.communicate.sig.emit(f"Timer: {self.count} s")


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
            print("****************  MouseObserver **************")
            #print(event)
            print(self.widget.objectName())
            
            #print(self.widget.cardPath)
            print("****************  MouseObserver **************")
            
        return super().eventFilter(obj, event)

class viewCardProject(QFrame, ui_widget_card.Ui_Form):
    trigger = Signal(str)
    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(viewCardProject, self).__init__(parent)
        self.setupUi(self)
        self.cardName = cardName
        self.cardDataTime = cardDataTime
        self.cardHour = cardHour
        self.cardPath = cardPath
        self.selected=False

        
        
        # este sirve para observar el evento del mause en el frame
        observer = MouseObserver(self)
        # tambien se realizao el de reimplemetacion


        # este metodo con parent ejecuta la funcion del padre Ejem QMainWindow
        #self.toolButton.clicked.connect(self.parent().functionOpenProject)
        self.toolButton.clicked.connect(self.toolButtonClicked)
        # Connect the trigger signal to a slot.
        #self.trigger.connect(self.parent().updateLabel)
        # Emit the signal.
        #self.trigger.emit()
   
        
        # tambien funciona self.cardProject.pushButton.clicked.connect(self.onClickedToolButtonMenuLat)
        # cando se crea el viewCard
        #self.pushButton.clicked.connect(self.parent().algo)


        

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(20)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(255,255,255,60))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        self.pushButton.clicked.connect(self.onClickedCard)
                
        self.setTextLabel()

    def toolButtonClicked(self):    
        # Emit the signal.
        self.trigger.emit(self.cardPath)



    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        print("****************  Reimplementando mousePressEvent **************")
        print(event)
        print(self.cardPath)
        self.trigger.connect(self.handle_trigger)
        self.trigger.emit()

        print("****************  Reimplementando mousePressEvent **************")
        self.selected=True
    
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

        
    def onClickedCard(self):
        print("ok button")

