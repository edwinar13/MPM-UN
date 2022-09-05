import json
from PySide6.QtCore import (QFile)
from PySide6.QtWidgets import (QMessageBox)


class DataBaseProjects ():    
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







class Projects ():    
    def __init__(self) -> None:
        self.list_projects= []
        
        # se lee los proyectos de db y se almacenan como objetos en list_projects
        self.db_projects = DataBaseProjects()
        for project in self.db_projects.getProjectsDB():
            name = project['nombreArchivo']
            path = project['ruta']
            data = project['fecha']
            hour = project['hora']
            self.list_projects.append(Project(name_file=name, path=path, data=data, hour=hour))

    def getProjects(self):
        """DEVUELVE LOS PROYECTOS RECIENTES 
        Devuelve >>> 
            lista de proyectos recientes"""

        return self.list_projects

    def addProject(self, objeto, project_to_open):
        """AGREGA UN NUEVO PROYECTO A LOS PROYECTOS RECIENTES DE LA DB
        Recibe >>
            objeto: QWidget
            nombreArchivo, fecha, hora, ruta
        devuelve >>
            True: si se agrega correctamente el proyecto
            False: si hay un error o no se encontro la DB"""
        try:
            name_file, path, data, hour = project_to_open.getData()        
            self.db_projects.addProjectDB(name_file=name_file, path=path, data=data, hour=hour)   
            row = 0
            for project in self.list_projects:
                if project.path == path:
                    self.list_projects.pop(row)
                    break
                row += 1
            self.list_projects.insert(0,project_to_open)
            validacion = True

    

        except:
                QMessageBox.critical(objeto, "MPM-UN", "Error class_projects addProjects",
                                    QMessageBox.Ok)
                validacion=False

        return validacion
     
    def deleteProjects(self,objeto):
        """ELIMINA LA LISTA DE PROYECTOS RECINETES EN LA DB
        Recibe >>
            objeto: QWidget
        devuelve >>
            True: si se eliminaron los proyectos recientes
            False: si hay un error o no se encontro la DB"""
        
        try:
            self.list_projects=[]
            self.db_projects.deleteProjectsDB()
            validacion=True
        except:
            QMessageBox.critical(objeto, "MPM-UN", "Error deleteProjects",
                                QMessageBox.Ok)
            validacion=False
        return validacion
    
    def newFileProject(self, fileName):
        """CREA LA BASE DER DATOS DE CADA PROYECTO NUEVO"""

        fileName = fileName.replace('.mpm', '')
        fileName='{}.mpm'.format(fileName)
        datos = {}	        
        datos['INFORMACION'] = {}
        datos['CONFIGURACION'] = {}
        datos['MALLAS'] = {}
        datos['PUNTOSMATERIAL'] = {}
        datos['MATERIALES'] = {}
        datos['RESULTADOS'] = {}
        try:

            with open(fileName, 'w') as file:
                file.write(json.dumps(datos))                 
                validacion=True

        except Exception as e:
            print('EL ERROR ES: {}'.format(e))
            validacion=False

        return validacion

    def openProject(self):
        pass


class Project():
    """ devuelve 
    name_file, path, data, hour"""
    def __init__(self,name_file, path, data, hour) -> None:
        self.name_file = name_file
        self.path = path
        self.data = data
        self.hour = hour        
    def getData(self):
        """  devuelve datos del proyecto 
        name_file, path, data, hour"""
        return[self.name_file, self.path, self.data, self.hour]
