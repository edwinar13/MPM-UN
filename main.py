
import sys
import random
from PySide6.QtCore import (Qt, Slot, QTimer)
from PySide6.QtGui import (QColor,QFontDatabase,QFont)
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QPushButton, QLabel, QHBoxLayout,QFrame,QSplitter,QVBoxLayout,QWidget, QGraphicsDropShadowEffect,QStyleFactory)


from clases import splash_screen
from config import class_config

# cuando se pase de .ui a .py
# se debe ajustar las rutas de las imagenes
# quitar ../

        
def IniciarFuentes():
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Bold.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-BoldItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Italic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Light.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-LightItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Medium.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-MediumItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Regular.ttf')


if __name__ == '__main__':
    databaseConfig = class_config.DataBaseConfig()
    databaseConfig.initApp()
    app = QApplication(sys.argv)
    IniciarFuentes()
    window = splash_screen.SplashScreen()
    window.show()
    sys.exit(app.exec())