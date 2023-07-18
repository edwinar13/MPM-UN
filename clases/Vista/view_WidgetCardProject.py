"""
Este módulo contiene la implementación de un widget para la página de inicio, 
que muestra información resumida de los proyectos recientes. La clase
ViewWidgetCardProjectHome es la encargada de crear el widget y se utiliza
como plantilla de diseño la definida en el archivo ui_widget_home_card.py.
"""

from PySide6.QtCore import ( QObject,QEvent, Signal)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect )
from ui import ui_widget_home_card
#from clases import class_general

class ViewWidgetCardProjectHome(QFrame, ui_widget_home_card.Ui_FormHomeCard):


    """

    La clase ViewWidgetCardProjectHome es una vista que crea un widget de tipo tarjeta (card)
    para almacenar información de un proyecto reciente, con el propósito de ser incluido en la 
    vista de la página home. Esta clase hereda de la clase QFrame de Qt y utiliza la plantilla de 
    diseño definida en el archivo ui_widget_home_card.py para construir su interfaz de usuario.

    El constructor de la clase recibe como argumentos el nombre del archivo del proyecto, la fecha
    y hora en que se abrió por última vez, y su ruta en el sistema de archivos. Estos valores se
    almacenan en los atributos privados de la clase (__cardName, __cardDataTime, __cardHour, y __cardPath)
    y se utilizan para actualizar el texto de las etiquetas dentro del widget.

    La clase ViewWidgetCardProjectHome también define una señal signal_open_project, que se emite 
    cuando el usuario hace clic en el widget de la tarjeta. El controlador asociado con esta vista debe 
    conectarse a esta señal para poder procesar el evento.

    Args:

        cardName (str): Nombre del archivo del proyecto (default = "").
        cardDataTime (str): Fecha en la que se abrió por última vez el proyecto (default = "").
        cardHour (str): Hora en la que se abrió por última vez el proyecto (default = "").
        cardPath (str): Ruta del archivo del proyecto (default = "").

    Attributes:
        __cardName (str): Nombre del archivo del proyecto.
        __cardDataTime (str): Fecha en la que se abrió por última vez el proyecto.
        __cardHour (str): Hora en la que se abrió por última vez el proyecto.
        __cardPath (str): Ruta del archivo del proyecto.

    Signals:
        signal_open_project: Señal emitida al hacer clic en el widget.

    """


    signal_open_project = Signal()

    def __init__(self,  cardName="", 
                        cardDataTime="", cardPath="",cardHour=""):
        super(ViewWidgetCardProjectHome, self).__init__()
        self.setupUi(self)
   
        
        # Atributo
        self.__cardName = cardName
        self.__cardDataTime = cardDataTime
        self.__cardHour = cardHour
        self.__cardPath = cardPath

        # Configura la UI
        self._configUi()
      
        #se colocan los atributos en las etiquetas
        self.setTextCard()
                

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def _configUi(self):
        """
        Configura la interface de usuario (ui).
        """
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
    def setTextCard(self):
        """
        Recupera información de los atributos y la coloca en las etiquetas de cada card de los proyectos recientes
        """
        self.label_cardName.setText(u"{}".format(self.__cardName))
        self.label_cardDataTime.setText(u"{} {}".format(self.__cardDataTime,self.__cardHour))
        self.label_cardPath.setText(u"{}".format(self.__cardPath))        
        self.frame_card.setToolTip(u"{}".format(self.__cardPath))

    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################
    
    def mousePressEvent(self, event):
        """
        Reimplantado el método mousePressEvent
        Args:
            event (QEvent): evento de ui
        """ 
        super().mousePressEvent(event)
        self.signal_open_project.emit()

    

