import sys
import json
from PySide6.QtCore import (QFile)
from PySide6.QtGui import (QFontDatabase)
from PySide6.QtWidgets import (QApplication)
from views.view_SplashScreen import SplashScreen


def newFileApp():  
    """Crea base de datos del software si no existe.""" 
    path_db_Config ="app/resources/db/Config.json"
    datos = {}    
    datos['ULTIMOSPROYECTOS'] = []
    datos['SETTING'] =  [
                            {
                                "TamañoCruzPuntero": 0,
                                "TamañoCajaPuntero": 0,
                                "Estilos de vista": 1
                            }
                        ]

    try:
        if not QFile.exists(path_db_Config):            
            with open(path_db_Config, 'w') as file:
                file.write(json.dumps(datos)) 
                print('Base de datos creada con éxito')
        else:
            print('Base de datos ya está creada')
    except Exception as e:
        print('EL ERROR ES: {}'.format(e))


def initFont():
    """Inicia las fuentes Ubuntu"""
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-Bold.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-BoldItalic.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-Italic.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-Light.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-LightItalic.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-Medium.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-MediumItalic.ttf')
    QFontDatabase.addApplicationFont('app/resources/fonts/Ubuntu-Regular.ttf')

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    initFont()
    newFileApp()
    window = SplashScreen()
    window.show()
    sys.exit(app.exec())


