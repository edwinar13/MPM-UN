"""Este módulo contiene las clases para interactuar con las bases de datos json.

class:
    : CreateDataBase.
    : DataBaseConfigMpmun.
    : DataBaseProject.

"""
from copy import copy
import json
import os
from PySide6.QtCore import (QFile)

'''
/*****************************************************/
Sentencias SQL para nombres de funciones de bases de datos
[exists], si existe un registro
[insert], inserta un registro
[select], recupera registro
[update], actualiza registro 
[delete], elimina registro
'''


class CreateDataBase ():    
    """Esta clase permite crear las bases de datos para la aplicación (.json), para cada proyecto (.mpm). 
    
    Attributes:
        path_db_Config (str): Ruta de la base de datos del programa.

    Method:
        : newFileApp
        : newFileProject   

    """
    def __init__(self) -> None:
        self.__path_db_Config="db/db_mpmun.json"
    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS NUEVA DB           ::::::::::::::::::::
	############################################################################### 
    def newFileApp(self):  
        """Crea base de datos del software si no existe.

        Args:
            
        Returns:
            
        """ 
        
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
            if not QFile.exists(self.__path_db_Config):            
                with open(self.__path_db_Config, 'w') as file:
                    file.write(json.dumps(datos)) 
                    print('Base de datos creada con éxito')
            else:
                print('Base de datos ya está creada')
        except Exception as e:
            print('EL ERROR ES: {}'.format(e))
  
    def newFileProject(self, filePath):       
        """crea la base de datos de cada proyecto Guardado Como o lo remplaza si ya existe.

        Args:
            filePath(str): Ruta para crear el archivo.
            data(dict): informacion de proyecto anterior 

        Returns:
            (bool): 
                : True >> si se crea correctamente el archivo de proyecto .mpm
                : False >> si hay un error

        """  
        filePath = filePath.replace('.mpm', '')
        filePath='{}.mpm'.format(filePath)
        
        data = {}	        
        data['INFORMACION'] = {
            "NOMBREPROYECTO": "",
            "LOCALIZACION": "",
            "AUTOR": "", 
            "DESCRIPCION": ""
        }
        data['CONFIGURACION'] = {
            "GRAVEDAD": 9.80
        }
        data['ITEMSDIBUJO'] = {
            "PUNTOS": {},
            "LINEAS": {},
            "RECTANGULOS": {}
        }
        data['MALLAS'] = {}
        data['PUNTOSMATERIAL'] = {}
        data['MATERIALES'] = {}
        data['RESULTADOS'] = {}
        
        try:

            with open(filePath, 'w') as file:
                file.write(json.dumps(data))  
                print('Archivo (mpm) del proyecto fue creado correctamente en: [{}]'.format(filePath))               
                validacion=True

        except Exception as e:
            print('EL ERROR ES: {}'.format(e))
            validacion=False

        return validacion

class DataBaseConfigMpmun():    
    """Esta clase permite crear el objeto que interactuara con la base de datos del programa. 

    Attributes:
        path_db_Config (str): Ruta de la base de datos del programa.
    
    Method:
        : selectProjectsDB
        : insertProjectDB
        : deleteProjectsDB

    """ 
    def __init__(self) -> None:
        self.__path_db_Config="db/db_mpmun.json"

        

    
    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB PROYECTOS         ::::::::::::::::::::
	###############################################################################   
    def selectProjectsDB(self):
        """Recupera los proyectos recientes de la db del sofware.
  
        Returns:
            (bool): False >> si no se encontró la db del software.
            (list): lista de proyectos recientes.

        """   
        BD = self.__path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects = json.load(f)
                data_projects = data_projects['ULTIMOSPROYECTOS']                
                return data_projects
        else:
            print("No se encontró la base de datos {}".format(self.__path_db_Config))
            return (False)

    def insertProjectDB(self, name_file, path, data, hour):
        """Inserta un proyecto a los proyectos recientes de la db del software.

        Args:
            name_file (str): Nombre del archivo del proyecto.
            path (str): Ruta del archivo del proyecto.
            data (str): Fecha en que se agrega el proyecto.
            hour (str): Hora en que se agrega el proyecto.

        Returns:
            (bool): 
                : True >> si se agrega correctamente el proyecto
                : False >> si no se encontró la db del software.

        """  
        BD=self.__path_db_Config
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects = json.load(f)
                    projects = data_projects['ULTIMOSPROYECTOS']
                    row = 0
                    exists = False
                    for project in projects:
                        if project["ruta"] == path:
                            exists = True
                            break
                        row += 1
                    if exists:
                        data_projects['ULTIMOSPROYECTOS'].pop(row)
                    data_projects['ULTIMOSPROYECTOS'].insert(0,{'nombreArchivo': name_file,
                                                'ruta': path,
                                                'fecha': data,
                                                'hora': hour})

                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects))
                validacion=True
            except:
                print("Error al agregar registro en <ULTIMOSPROYECTOS> de la base de datos {}".format(self.__path_db_Config))
                validacion=False
        else:  
            print("No se encontró la base de datos {}".format(self.__path_db_Config))          
            validacion=False        
        return validacion

    def deleteProjectsDB(self):
        """Elimina todos los proyectos recientes en la db del software.

        Returns:
            (bool): 
                : True >> si se eliminaron los proyectos recientes.
                : False >> si hay un error o no se encontró la db del software.

        """  
        
        BD = self.__path_db_Config
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects = json.load(f)
                    data_projects['ULTIMOSPROYECTOS']=[]
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects))
                validacion=True
            except:
                print("Error al eliminar registros de <ULTIMOSPROYECTOS> de la base de datos {}".format(self.__path_db_Config))
                validacion=False
        else:
            print("No se encontró la base de datos {}".format(self.__path_db_Config))  
            validacion=False
        return validacion

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB SETTING         ::::::::::::::::::::
	###############################################################################   

    def selectSettingDB(self):
        """Recupera los ajustes de la app de la db del sofware.
  
        Returns:
            (bool): False >> si no se encontró la db del software.
            (list): lista de ajustes.

        """   
        BD = self.__path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_setting = json.load(f)
                data_setting = data_setting['SETTING']                
                return data_setting
        else:
            print("No se encontró la base de datos {}".format(self.__path_db_Config))
            return (False)

    def updateSettingDB(self,section, type_setting, value):
        """actualiza los ajustes del app en la db del software.

        Args:
            section(int): la seccion de ajustes
            type_setting(str): ajuste para actualizar
            valu(*): valor del ajustes para actualizar

        Returns:
            (bool): 
                : True >> si se actualizo correctamente los ajustes
                : False >> si no se encontró la db del software.
        """  
        
        BD=self.__path_db_Config
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_setting = json.load(f)
                    data_setting['SETTING'][section][type_setting]=value

                with open(BD, 'w') as f:
                    f.write(json.dumps(data_setting))
                validacion=True
                
            except:
                print("Error al actualizar ajuste en <SETTING> de la base de datos {}".format(self.__path_db_Config))
                validacion=False
                
        else:  
            print("No se encontró la base de datos {}".format(self.__path_db_Config))          
            validacion=False        
        return validacion


class DataBaseProject():    
    """Esta clase permite crear el objeto que interactuara con la base de datos del proyecto. 

    Attributes:
        path_db_project (str): Ruta de la base de datos del proyecto.
        name_doc_py(str): Nombre del archivo .py donde se ejecuta esta clase. 
        original_copy_db_projec(dict):Copia original de la base de datos del proyecto
        unguarded_copy_db_project(dict):Copia sin guardar de la base de datos del proyecto
    
    Method:
        : selectInformationDB
        : updateInformationDB
        : selectConfigDB
        : updateConfigDB
        : selectItemDrawDB
        : updateItemDrawDB
        : checkProjectChanges
        : saveDataDb

    """

    def __init__(self, path) -> None:
        # Atributos
        self.__path_db_project = path
        self.__name_doc_py = os.path.basename(__file__) 
        self.__original_copy_db_project = None
        self.__unguarded_copy_db_project = None

        #inicializa las copias de la base de datos del proyecto
        self.__initDb()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initDb(self):
        """Hace una copia original de la db del proyecto y otra para almacenar los cambios."""

        BD = self.__path_db_project
        if QFile.exists(BD):            
            with open(BD, 'r') as a: 
                self.__original_copy_db_project = json.load(a)
                a.close()

            with open(BD, 'r') as b: 
                self.__unguarded_copy_db_project = json.load(b)
                b.close()
        else:            
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.__name_doc_py,BD))   

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB INFORMACION       ::::::::::::::::::::
	###############################################################################   
    def selectInformationDB(self):
        """Recupera la información básica contenida en la copia sin guardas de la db del proyecto.
        Returns:
            (dict): Diccionario con la información del proyecto.
        """   

        data_projects_information = self.__unguarded_copy_db_project['INFORMACION']
        return data_projects_information
    
    def updateInformationDB(self, name_project=None, location=None,
                                 author=None,  description=None):
        """Actualiza la información básica en la copia sin guardar de la db del proyecto.

        Args:
            name_project (str): Nombre del proyecto (default= None).
            location (str): Localización del proyecto (default= None).
            author (str): Autor del proyecto (default= None).
            description (str): Descripción del proyecto (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la información al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 

        try:  
            if name_project != None:          
                self.__unguarded_copy_db_project['INFORMACION']['NOMBREPROYECTO']=name_project
            if location != None:          
                self.__unguarded_copy_db_project['INFORMACION']['LOCALIZACION']=location
            if author != None:        
                self.__unguarded_copy_db_project['INFORMACION']['AUTOR']=author
            if description != None:          
                self.__unguarded_copy_db_project['INFORMACION']['DESCRIPCION']=description
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <INFORMACION> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS DB CONFIGURACION       ::::::::::::::::::::
	###############################################################################   
    def selectConfigDB(self):
        """Recupera la configuración básica contenida en la copia sin guardas de la db del proyecto.

        Returns:
            (dict): Diccionario con la configuración del proyecto.

        """   

        data_projects_config = self.__unguarded_copy_db_project['CONFIGURACION']
        return data_projects_config
    
    def updateConfigDB(self, gravity = None):
        """Actualiza la configuración básica en la db del proyecto.

        Args:
            gravity(str): Valor de la gravedad para el proyecto (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la configuración al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 


        try:  
            if gravity != None:          
                self.__unguarded_copy_db_project['CONFIGURACION']['GRAVEDAD']=gravity
            return True
        except BaseException as err:
            print("[Doc: {}]  Error al agregar registro en <CONFIGURACION> de la base de datos {}".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB ITEMSDIBUJO       ::::::::::::::::::::
	###############################################################################   
    def selectItemDrawDB(self):
        """Recupera los items de dibujo (puntos, lineas, rectangulos) contenidos en la copia sin guardas de la db del proyecto.
        Returns:
            (dict): Diccionario con los items de dibujo del proyecto.
        """   

        data_projects_items_draw = self.__unguarded_copy_db_project['ITEMSDIBUJO']
        return data_projects_items_draw
    
    def updateItemDrawDB(self, no_items, points=None, lines=None,  rectangles=None):
        """Actualiza los items de dibujo (puntos, lineas, rectangulos) en la copia sin guardar de la db del proyecto.

        Args:
            no_items (int): numero de items.
            points (list): lista de puntos (default= None).
            lines (list): lista de lineas (default= None).
            rectangles (list): lista de rectangulos (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente los items al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 

        try:  
            if no_items != None:          
                self.__unguarded_copy_db_project['ITEMSDIBUJO']['NOITEMS']=no_items
            if points != None:          
                self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS']=points
            if lines != None:          
                self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS']=lines
            if rectangles != None:        
                self.__unguarded_copy_db_project['ITEMSDIBUJO']['RECTANGULOS']=rectangles

            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    def checkProjectChanges(self):
        """ Verifica si hay cambios en el proyecto.

        Returns:
            (bool):
                : True >> si hay cambios en el proyecto
                : False >> si no hay cambios en el proyecto

        """
        #print("------\n{}\n{}\n------".format(self.__original_copy_db_project , self.__unguarded_copy_db_project))

        if(self.__original_copy_db_project == self.__unguarded_copy_db_project):
            return False
        else:
            return True

    def saveDataDb(self):
        """Guarda la información de la copia sin guardar en la db del proyecto.
        
        Returns:
            (bool): 
                : True >> si se guardo correctamente en la base de datos
                : False >> si no se guardo correctamente en la base de datos

        """
        BD=self.__path_db_project
        if QFile.exists(BD):		  
            try:
                # se guarda en el archivo
                with open(BD, 'w') as a:
                    a.write(json.dumps(self.__unguarded_copy_db_project)) 
                    a.close()
                            
                # se actualiza la copia original
                with open(BD, 'r') as b: 
                    self.__original_copy_db_project = json.load(b)
                    b.close()
                print("Guardo correctamente en la base de datos")   

                validacion=True
            
            except BaseException as err:
                print("[Doc: {}]  Error al agregar registro en <CONFIGURACION> de la base de datos {}".format(self.__name_doc_py,BD))
                print("[Tipo: {}, Erro: {}]".format(type(err),err))
                validacion=False
            
        else:  
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.__name_doc_py,BD))          
            validacion=False
        return validacion


    def projectSaveAs(self, new_path_file):  
        """Guarda la información de la copia sin guardar en la nueva ruta de la db del proyecto.

        Args:
            new_path_file(str): Ruta para crear el archivo.

        Returns:
            (bool): 
                : True >> si se guardo correctamente en la base de datos
                : False >> si no se guardo correctamente en la base de datos

        """

        BD=new_path_file	  
        try:
            # se guarda en el archivo
            with open(BD, 'w') as a:
                a.write(json.dumps(self.__unguarded_copy_db_project)) 
                a.close()
            print("Guardo como, correctamente en la base de datos")   

            validacion=True
        
        except BaseException as err:
            print("[Doc: {}]  Error al guardar como {}".format(self.__name_doc_py,BD))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            validacion=False
        

        return validacion





         
