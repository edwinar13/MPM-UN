import json
from PySide6.QtCore import (QFile)
from PySide6.QtWidgets import (QMessageBox)



class DataBaseConfigMpmun ():    
    def __init__(self) -> None:
        self.path_db_Config="config/database_mpmun.json"

    def getProjectsDB(self):
        """
        CONSULTA LOS PROYECTOS RECIENTES EN LA DB
        Devuelve >>> 
            lista de proyectos recientes
            o False: si hay un error o no se encontro la DB
        """
        BD = self.path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects = json.load(f)
                data_projects = data_projects['ULTIMOSPROYECTOS']
                return data_projects
        else:
            print("No se encontro la base de datos de MPM-UN")
            return (False)

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


class DataBaseProject ():    
    def __init__(self, path) -> None:
        self.path_db_project = path


    ###############################################################################
	# ::::::::::::::::::::             INFORMACION             ::::::::::::::::::::
	###############################################################################   

    def getInformationDB(self):
        """
        CONSULTA LA INFORMACION EN LA DB DEL PROYECTO
        Devuelve >>> 
            diccinario de informacion 
            o False: si hay un error o no se encontro la DB
        """
        BD = self.path_db_project
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects_information = json.load(f)
                data_projects_information = data_projects_information['INFORMACION']
                return data_projects_information
        else:
            print("No se encontro la base de datos de {}".format(BD))
            return (False)

    def addInformationDB(self, name_project, location, author,  description):
        """
        AGREGA LA INFORMACION DE LA DB DEL PROYECTO
        Recibe >>
            name_project, location, author,  description
        devuelve >>
            True: si se agrega correctamente el protecto
            False: si hay un error o no se encontro la DB
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
            except:
                print("Error al agregar registro en <INFORMACION>")
                validacion=False
        else:  
            print("No se encontro la base de datos de {}".format(BD))          
            validacion=False
        return validacion

    ###############################################################################
	# ::::::::::::::::::::             CONFIGURACION             ::::::::::::::::::::
	###############################################################################   

    def getConfigDB(self):
        """
        CONSULTA LA CONFIGURACION EN LA DB DEL PROYECTO
        Devuelve >>> 
            diccinario de informacion 
            o False: si hay un error o no se encontro la DB
        """
        BD = self.path_db_project
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects_config = json.load(f)
                data_projects_config = data_projects_config['CONFIGURACION']
                return data_projects_config
        else:
            print("No se encontro la base de datos de {}".format(BD))
            return (False)
    def addConfigDB(self, gravity):
        """
        AGREGA LA CONFIGURACION  EN LA DB DEL PROYECTO
        Recibe >>
            gravity
        devuelve >>
            True: si se agrega correctamente el protecto
            False: si hay un error o no se encontro la DB
        """

        BD=self.path_db_project
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_projects_config = json.load(f)                    
                    config = data_projects_config['CONFIGURACION']['GRAVEDAD']=gravity
                    #config['GRAVEDAD']=gravity
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(data_projects_config))
                
                validacion=True
            except:
                print("Error al agregar registro en <CONFIGURACION>")
                validacion=False
        else:  
            print("No se encontro la base de datos de {}".format(BD))          
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