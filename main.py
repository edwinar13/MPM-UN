import sys
from PySide6.QtGui import (QFontDatabase)
from PySide6.QtWidgets import (QApplication)
from clases import splash_screen
from clases import database_class
       
def initFont():
    """Inicia las fuentes Ubuntu"""
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Bold.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-BoldItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Italic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Light.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-LightItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Medium.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-MediumItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Regular.ttf')

if __name__ == '__main__':
    createDataBase = database_class.CreateDataBase()
    createDataBase.newFileApp()
    app = QApplication(sys.argv)
    initFont()
    window = splash_screen.SplashScreen(createDataBase)
    window.show()
    sys.exit(app.exec())