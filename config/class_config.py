import json
from PySide6.QtCore import (QFile)
from PySide6.QtWidgets import (QMessageBox)

class DataBaseConfig ():    
    def __init__(self) -> None:
        self.pathDBConfig="config/database_mpmun.json"

    def initApp(self):
        """CREA BASE DE DATOS DEL SOFTWARE SI NO EXISTE"""    
        datos = {}    
        datos['ULTIMOSPROYECTOS'] = []
        try:
            if not QFile.exists('config/database_mpmun.json'):            
                with open('config/database_mpmun.json', 'w') as file:
                    file.write(json.dumps(datos)) 
                    print('Base de datos creada con exito')
            else:
                print('Base de datos ya esta creada')
        except Exception as e:
            print('EL ERROR ES: {}'.format(e))

