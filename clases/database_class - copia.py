"""
Este módulo contiene las clases para interactuar con las bases de datos json.

class:
    : CreateDataBase.
    : DataBaseConfigMpmun.
    : DataBaseProject.
"""
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

    Args:
        
    Attributes:

    Method:
        : newFileApp
        : newFileProject
    """

    def newFileApp(self):  
        """Crea base de datos del software si no existe.

        Args:
            
        Returns:
            
        """ 
        path_db_Config="db/db_mpmun.json"
        datos = {}    
        datos['ULTIMOSPROYECTOS'] = []
        try:
            if not QFile.exists( path_db_Config):            
                with open( path_db_Config, 'w') as file:
                    file.write(json.dumps(datos)) 
                    print('Base de datos creada con éxito')
            else:
                print('Base de datos ya está creada')
        except Exception as e:
            print('EL ERROR ES: {}'.format(e))
  
    def newFileProject(self, filePath):       
        """crea la base de datos de cada proyecto nuevo o lo remplaza si ya existe.

        Args:
            filePath(str): Ruta para crear el archivo.

        Returns:
            (bool): 
                : True >> si se crea correctamente el archivo de proyecto .mpm
                : False >> si hay un error
        """  
        filePath = filePath.replace('.mpm', '')
        filePath='{}.mpm'.format(filePath)
        datos = {}	        
        datos['INFORMACION'] = {"NOMBREPROYECTO": "",
                                "LOCALIZACION": "",
                                "AUTOR": "", 
                                "DESCRIPCION": ""
                                }
        datos['CONFIGURACION'] = {
                                "GRAVEDAD": 9.80
                                }
        datos['MALLAS'] = {}
        datos['PUNTOSMATERIAL'] = {}
        datos['MATERIALES'] = {}
        datos['RESULTADOS'] = {}
        try:

            with open(filePath, 'w') as file:
                file.write(json.dumps(datos))  
                print('Archivo (mpm) del proyecto fue creado correctamente en: [{}]'.format(filePath))               
                validacion=True

        except Exception as e:
            print('EL ERROR ES: {}'.format(e))
            validacion=False

        return validacion

class DataBaseConfigMpmun():    
    """Esta clase permite crear el objeto que interactuara con la base de datos del programa. 

    Args:
        
    Attributes:
        path_db_Config (str): Ruta de la base de datos del programa.
    
    Method:
        : selectProjectsDB
        : insertProjectDB
        : deleteProjectsDB

    """ 
    def __init__(self) -> None:
        self.path_db_Config="db/db_mpmun.json"
    
  
    def selectProjectsDB(self):
        """Devuelve los proyectos recientes de la db del sofware.

        Args:
            
        Returns:
            (bool): False >> si no se encontró la db del software.
            (list): lista de proyectos recientes.
        """   
        BD = self.path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects = json.load(f)
                data_projects = data_projects['ULTIMOSPROYECTOS']                
                return data_projects
        else:
            print("No se encontró la base de datos {}".format(self.path_db_Config))
            return (False)

    def insertProjectDB(self, name_file, path, data, hour):
        """Agrega un proyecto a los proyectos recientes de la db del software.

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
        BD=self.path_db_Config
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
                print("Error al agregar registro en <ULTIMOSPROYECTOS> de la base de datos {}".format(self.path_db_Config))
                validacion=False
        else:  
            print("No se encontró la base de datos {}".format(self.path_db_Config))          
            validacion=False        
        return validacion

    def deleteProjectsDB(self):
        """Elimina todos los proyectos recientes en la db del software.

        Args:

        Returns:
            (bool): 
                : True >> si se eliminaron los proyectos recientes.
                : False >> si hay un error o no se encontró la db del software.
        """  
        
        BD = self.path_db_Config
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects = json.load(f)
                    data_projects['ULTIMOSPROYECTOS']=[]
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects))
                validacion=True
            except:
                print("Error al eliminar registros de <ULTIMOSPROYECTOS> de la base de datos {}".format(self.path_db_Config))
                validacion=False
        else:
            print("No se encontró la base de datos {}".format(self.path_db_Config))  
            validacion=False
        return validacion

class DataBaseProject ():    
    """Esta clase permite crear el objeto que interactuara con la base de datos del proyecto. 

    Args:
        
    Attributes:
        path_db_project (str): Ruta de la base de datos del proyecto.
        name_doc_py(str): Nombre del archivo .py donde se ejecuta esta clase. 
    
    Method:
        : selectInformationDB
        : insertInformationDB
        : selectConfigDB
        : insertConfigDB
    """

    def __init__(self, path) -> None:
        self.path_db_project = path
        self.name_doc_py = os.path.basename(__file__) 



    ###############################################################################
	# ::::::::::::::::::::             INFORMACION             ::::::::::::::::::::
	###############################################################################   

    def selectInformationDB(self):
        """Devuelve la información básica contenida en la db del proyecto.

        Args:
            
        Returns:
            (bool): False >> si no se encontró la db del proyecto.
            (dict): Diccionario con la información del proyecto.
        """   


        BD = self.path_db_project
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects_information = json.load(f)
                data_projects_information = data_projects_information['INFORMACION']
                return data_projects_information
        else:            
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.name_doc_py,BD))   
            return (False)
    
    def insertInformationDB(self, name_project, location, author,  description):
        """Agrega la información básica en la db del proyecto.

        Args:
            name_project (str): Nombre del proyecto.
            location (str): Localización del proyecto.
            author (str): Autor del proyecto.
            description (str): Descripción del proyecto.

        Returns:
            (bool): 
                : True >> si se agrega correctamente la información al proyecto
                : False >> si no se encontró la db del proyecto.
        """ 
        BD=self.path_db_project
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects_information = json.load(f)
                    data_projects_information['INFORMACION']['NOMBREPROYECTO']=name_project
                    data_projects_information['INFORMACION']['LOCALIZACION']=location
                    data_projects_information['INFORMACION']['AUTOR']=author
                    data_projects_information['INFORMACION']['DESCRIPCION']=description

                    '''
                    row = 0
                    exists = False
                    for project in projects:
                        if project["ruta"] == path:
                            exists = True
                            break
                        row += 1
                    if exists:
                        data_projects_information['ULTIMOSPROYECTOS'].pop(row)
                    data_projects_information['ULTIMOSPROYECTOS'].insert(0,{'nombreArchivo': name_file,
                                                'ruta': path,
                                                'fecha': data,
                                                'hora': hour})
                    '''
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects_information))
                
                validacion=True
            except BaseException as err:
                print("[Doc: {}] Error al agregar registro en <INFORMACION> de la base de datos {}".format(self.name_doc_py,BD))
                print("[Tipo: {}, Erro: {}]".format(type(err),err))
                validacion=False
        else:  
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.name_doc_py,BD))            
            validacion=False
        return validacion

    ###############################################################################
	# ::::::::::::::::::::             CONFIGURACION             ::::::::::::::::::::
	###############################################################################   

    def selectConfigDB(self):
        """Devuelve la configuración básica contenida en la db del proyecto.

        Args:
            
        Returns:
            (bool): False >> si no se encontró la db del proyecto.
            (dict): Diccionario con la configuración del proyecto.
        """   
        BD = self.path_db_project
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects_config = json.load(f)
                data_projects_config = data_projects_config['CONFIGURACION']
                return data_projects_config
        else:            
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.name_doc_py,BD))   
            return (False)
    
    def insertConfigDB(self, gravity):
        """Agrega la configuración básica en la db del proyecto.

        Args:
            gravity(str): Valor de la gravedad para el proyecto.

        Returns:
            (bool): 
                : True >> si se agrega correctamente la configuración al proyecto
                : False >> si no se encontró la db del proyecto.
        """ 

        BD=self.path_db_project
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects_config = json.load(f)                    
                    data_projects_config['CONFIGURACION']['GRAVEDAD']=gravity
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects_config))
                
                validacion=True
            except BaseException as err:
                print("[Doc: {}]  Error al agregar registro en <CONFIGURACION> de la base de datos {}".format(self.name_doc_py,BD))
                print("[Tipo: {}, Erro: {}]".format(type(err),err))
                validacion=False
        else:  
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.name_doc_py,BD))          
            validacion=False
        return validacion



    '''
    def addProjectDB(self, name_file, path, data, hour, ):
        """
        AGREGA UN NUEVO PROYECTO A LOS PROYECTOS RECIENTES DE LA DB
        Recibe >>
            name_file, data, hour, path
        devuelve >>
            True: si se agrega correctamente el protecto
            False: si hay un error o no se encontro la DB
        """

        BD=self.path_db_Config
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
                print("Error al agregar registro en <ULTIMOSPROYECTOS>")
                validacion=False
        else:  
            print("No se encontro la base de datos de MPM-UN")          
            validacion=False
        return validacion

    def deleteProjectsDB(self):
        """ELIMINA TODOS LOS PROYECTOS RECIENTES EN LA DB
        devuelve >>
            True: si se eliminaron los proyectos recientes
            False: si hay un error o no se encontro la DB"""
        BD = self.path_db_Config
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects = json.load(f)
                    data_projects['ULTIMOSPROYECTOS']=[]
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects))
                validacion=True
            except:
                print("Error al eliminar registros de <ULTIMOSPROYECTOS>")
                validacion=False
        else:
            print("No se encontro la base de datos de MPM-UN") 
            validacion=False
        return validacion



    '''


