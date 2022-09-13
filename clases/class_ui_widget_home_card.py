""" Este módulo contiene la clase Ui_FormHomeCard, para incluirla en frame home
Es el widget card de cada proyecto reciente."""
from PySide6.QtCore import ( QObject,QEvent, Signal)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )
from ui import ui_widget_home_card
from clases import general_class

class viewCardProject(QFrame, ui_widget_home_card.Ui_FormHomeCard):
    """Esta clase crea el QFrame home-card para agregarlo a Frame Home. 

    Args:
            cardName (str):     Nombre del archivo del proyecto (default = "").
            cardDataTime (str): Fecha en la que se abrió por última vez el proyecto (default = "").
            cardHour (str):     Hora en la que se abrió por última vez el proyect (default = "").
            cardPath (str):     Ruta del archivo del proyect (default = "").

    Attributes:
            cardName (str):     Nombre del archivo del proyecto.
            cardDataTime (str): Fecha en la que se abrió por última vez el proyecto.
            cardHour (str):     Hora en la que se abrió por última vez el proyecto.
            cardPath (str):     Ruta del archivo del proyecto.
    """    
    signal_open_project = Signal(str)

    def __init__(self, parent = None,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(viewCardProject, self).__init__(parent)
        self.setupUi(self)
        
        # Atributo
        self.__cardName = cardName
        self.__cardDataTime = cardDataTime
        self.__cardHour = cardHour
        self.__cardPath = cardPath

        # Configura la UI
        self._configUi()
      
        #se colocan los atributos en las etiquetas
        self.setTextLabel()

        #este es una forma de darle evento a un frame
        observer = general_class.MouseObserver(self.label_cardName)
                

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def _configUi(self):
        """Configura la interface de usuario (ui).""" 
        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,0,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    def setTextLabel(self):
        """ Recupera información de los atributos y la coloca en las etiquetas de cada card de los proyectos recientes"""
        self.label_cardName.setText(u"{}".format(self.__cardName))
        self.label_cardDataTime.setText(u"{} {}".format(self.__cardDataTime,self.__cardHour))
        self.label_cardPath.setText(u"{}".format(self.__cardPath))        
        self.frame_card.setToolTip(u"{}".format(self.__cardPath))

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################
    def mousePressEvent(self, event):
        """Reimplantado el método mousePressEvent
        Args:
            event (QEvent): evento de ui
        """ 
        super().mousePressEvent(event)
        print("***** con  Reimplementando mousePressEvent {} *****".format(event))
        self.signal_open_project.emit(self.__cardPath)

