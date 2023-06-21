from time import strftime
from PySide6.QtCore import (QFile, QTime)
import json
import os


class ModelSettingApp:
    def __init__(self):
        self.path_db_Config="db/db_mpmun.json"
        self.setting = None
        self.loadSetting()


    
    def loadSetting(self):
        """Carga las configuraciones de la db del sofware al modelo.
  
        Returns:
            (bool): False >> si no se encontró la db del software.
            (list): lista de ajustes.  
        """

        BD = self.path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_setting = json.load(f)
                data_setting = data_setting['SETTING']  
                self.setting = data_setting
                return data_setting
        else:
            print("No se encontró la base de datos {}".format(self.path_db_Config))
            return (False)
 
    def updateSetting(self,setting_update):
        """actualiza los ajustes del app en la db del software.

        Args:
            setting_update (dict): diccionario con la configuracion a actualizar.

        Returns:
            (bool): 
                : True >> si se actualizo correctamente los ajustes
                : False >> si no se encontró la db del software.
        """  
        
        BD=self.path_db_Config    
        section, type_setting, value = setting_update["setting_data"]


        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_setting = json.load(f)
                    data_setting['SETTING'][section][type_setting]=value

                with open(BD, 'w') as f:
                    f.write(json.dumps(data_setting))
                validacion=True
                
            except:
                print("Error al actualizar ajuste en <SETTING> de la base de datos {}".format(self.path_db_Config))
                validacion=False
                
        else:  
            print("No se encontró la base de datos {}".format(self.path_db_Config))          
            validacion=False

            
                    
        return validacion
       
    def getSetting(self):
        """
        Retorna una lista de las configuraciones .
  
        Returns:
            (list): Lista con las configuraciones.
        """
        return self.setting
      