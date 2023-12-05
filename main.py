
import sys
import json
from PySide6.QtCore import (QFile)
from PySide6.QtGui import (QFontDatabase)
from PySide6.QtWidgets import (QApplication)
from clases.Vista import view_SplashScreen



def newFileApp():  
    """Crea base de datos del software si no existe.""" 
    path_db_Config ="db/db_mpmun.json"
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
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Bold.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-BoldItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Italic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Light.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-LightItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Medium.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-MediumItalic.ttf')
    QFontDatabase.addApplicationFont('recursos/fuentes/Ubuntu-Regular.ttf')

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    initFont()
    newFileApp()
    window = view_SplashScreen.SplashScreen()
    window.show()
    sys.exit(app.exec())




