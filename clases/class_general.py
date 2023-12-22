""" Este módulo contiene las clases generales para Qt

class:
    : QLabelVertical.
    : MouseObserver.

"""
from PySide6.QtCore import (QEvent, QSize,QObject)
from PySide6.QtGui import (QPainter,QFontMetrics,Qt)
from PySide6.QtWidgets import ( QLabel)


class QLabelVertical(QLabel):
    """Crear un QLabel en formato vertical.

    Args:
        (str): cadena con el texto a mostrar.
        *args: Argumentos de QLabel

    Attributes:
        Atributos de QLabel.
    
    Method:
        : paintEvent
        : minimumSizeHint
        : sizeHint
        : *Métodos de QLabel

    """        
    def __init__(self, *args):
        QLabel.__init__(self, *args)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        
        fm = QFontMetrics(painter.font())
        xoffset = int(fm.boundingRect(self.text()).width()/2)
        yoffset = int(fm.boundingRect(self.text()).height()/2)
        x = int(self.width()/2) + yoffset
        y = int(self.height()/2) - xoffset
        
        painter.drawText(y, x, self.text())
        painter.end()
        
    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())

class MouseObserver(QObject):
    """Crear un observador para los eventos del ratón, en especial para los frame que no tiene ese evento por defecto.

    Args:
        widget(QtWidgets): Widget al que se le agregara el observador.

    Attributes:
        widget(QtWidgets): Widget al que se le agregara el observador.
    
    Method:
        : eventFilter.

    """     
    def __init__(self, widget):
        super().__init__(widget)
        self.__widget = widget
        self.widget.installEventFilter(self)

    @property
    def widget(self):
        return self.__widget

    def eventFilter(self, obj, event):
        """método para filtrar el tipo de widget que activo la señal
        Returns:
            (bool): 
        """
        
        if obj is self.widget and event.type() == QEvent.MouseButtonPress:
            print(">>>> con MouseObserver {} <<<<<".format(self.widget.objectName()))        
        return super().eventFilter(obj, event)
    
 