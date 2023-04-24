"""Este módulo contiene las clases para objetos relacionados con proyectos.

class:
    : Projects
    : Project

"""
from time import strftime
from PySide6.QtCore import (QTime)
from PySide6.QtWidgets import (QMessageBox)
from clases import class_database


class Projects():
    """Esta clase crear el objeto proyectos. 

    Args:
        dataBaseConfigMpmun(DataBaseConfigMpmun):Objeto para interactuar con la base de datos del programa
        
    Attributes:
        db_config_mpmun(DataBaseConfigMpmun):Objeto para interactuar con la base de datos del programa
        list_projects (list): Lista de objetos de proyectos recientes.
    
    Method:
        : getProjects
        : addProject
        : deleteProjects
        : newFileProject

    """ 
    def __init__(self, dataBaseConfigMpmun:class_database.DataBaseConfigMpmun) -> None:

        # Atributos
        self.__list_projects = []
        self.__db_config_mpmun = dataBaseConfigMpmun

        # Establece list_projects
        self.setProjects()


    ###############################################################################
	# ::::::::::::::::::::           GETTERS Y SETTERS         ::::::::::::::::::::
	###############################################################################
    def setProjects(self):
        """Establece los proyectos recientes de la db."""
        list_projects = self.__db_config_mpmun.selectProjectsDB()
        #if  type(list_projects) == list:
        for project in list_projects:
            name = project['nombreArchivo']
            path = project['ruta']
            data = project['fecha']
            hour = project['hora']
            self.__list_projects.append(Project(name_file=name, path=path, data=data, hour=hour))

    def getProjects(self):
        """Obtiene los proyectos recientes.
    
        Returns:
            (list): lista de objetos de proyectos recientes.

        """ 
        return self.__list_projects


    ###############################################################################
	# ::::::::::::::::::::           MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    def addProject(self, objeto, project_to_open):
        """Agrega objeto de proyecto a la lista de proyectos y a la db del sofware.

        Args:
            project_to_open(Project): Objeto tipo proyecto.

        Returns:
            (bool): 
                : True >> si se agrega correctamente el proyecto
                : False >> si hay un error o no se encontró la db del proyecto.

        """ 
        try:
            name_file, path, data, hour = project_to_open.getData() 
            self.__db_config_mpmun.insertProjectDB(name_file=name_file, path=path, data=data, hour=hour)   
            row = 0
            for project in self.__list_projects:
                if project.getPath() == path:
                    self.__list_projects.pop(row)
                    break
                row += 1
            self.__list_projects.insert(0,project_to_open)
            validacion = True            
        except:
#-------------------------------------------------------------------------------------------------------
            QMessageBox.critical(objeto, "MPM-UN", "Error class_projects addProjects",
                                QMessageBox.Ok)
#-------------------------------------------------------------------------------------------------------
            validacion=False
            
        return validacion
     
    def deleteProjects(self):
        """Elimina todos los proyectos recientes de la lista de proyectos y de la db del sofware.

        Returns:
            (bool): 
                : True >> si se elimina correctamente el proyecto
                : False >> si hay un error o no se encontró la db del proyecto.

        """         
        try:
            self.__list_projects=[]
            self.__db_config_mpmun.deleteProjectsDB()
            validacion=True
        except BaseException as err:     
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            validacion=False
        return validacion
    
    def newFileProject(self, filePath):       
        """Crea nueva base de datos de un proyecto.

        Args:
            filePath(str): Ruta para crear el archivo.

        Returns:
            (bool): 
                : True >> si se crea correctamente el archivo de proyecto .mpm
                : False >> si hay un error

        """ 
        createDataBaseProject =class_database.CreateDataBase()
        return createDataBaseProject.newFileProject(filePath)

class Project():
    """Esta clase crear el objeto proyecto. 

    Args:
        name_file (str): Nombre del archivo del proyecto (default = None).
        path (str): Ruta del archivo del proyecto (default = None).
        data (str): Fecha en la que se abrió por última vez el proyecto (default = None).
        hour (str): Hora en la que se abrió por última vez el proyecto (default = None).
        
    Attributes:
        name_file (str): Nombre del archivo del proyecto.
        path (str): Ruta del archivo del proyecto.
        data (str): Fecha en la que se abrió por última vez el proyecto.
        hour (str): Hora en la que se abrió por última vez el proyecto.
        db_project(DataBaseProject): Instancia a la base de datos del proyecto

    Method:
        : getName
        : setData
        : getData
        : saveData
        : checkProjectChanges

    """ 
    def __init__(self, path, name_file=None, data=None, hour=None) -> None:
        self.__name_file = name_file
        self.__path = path
        self.__data = data
        self.__hour = hour
        self.db_project= None

        # Actualiza argumentos vacíos
        self.__initProject()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initProject(self):
        """Actualiza argumentos vacíos (none)"""
        if self.__data == None or self.__hour == None or self.__name_file == None :
            self.setData(self.__path)
            self.__instanceDbProject(self.__path)

    ###############################################################################
	# ::::::::::::::::::::           GETTERS Y SETTERS         ::::::::::::::::::::
	###############################################################################
    def getName(self):
        """Obtiene el nombre del proyecto.

        Returns:
            name_file (str): Nombre del archivo del proyecto.

        """
        return self.__name_file
    
    def getPath(self):
        """Obtiene la ruta del proyecto.

        Returns:
            path (str): Ruta del archivo del proyecto.

        """
        return self.__path

    def setData(self, filePath):
        """Establece los argumentos: nombre, fecha (actual) y hora (actual).

        Args:
            filePath(str): ruta del proyecto

        """ 
        self.__hour = QTime.currentTime().toString("hh:mm:ss A ")
        self.__data = strftime("%d/%m/%y")
        self.__name_file = filePath.split('/')[-1]

    def getData(self):
        """Obtiene todos los argumentos del proyecto.

        Returns:
            (list): lista de los argumentos del proyecto
                    name_file, path, data, hour

        """ 
        return[self.__name_file, self.__path, self.__data, self.__hour]
       

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    def saveData(self):
        """ Guarda toda la información en la base de datos del proyecto.
  
        Returns:
            (bool):
                : True >> si se guardo correctamente en la base de datos
                : False >> si no se guardo correctamente en la base de datos

        """ 
        return self.db_project.saveDataDb()

    def projectSaveAs(self, new_path_file):       
        """Guarda como, el proyecto actual en la nueva ruta.

        Args:
            new_path_file(str): Ruta para crear el archivo.

        Returns:
            (bool): 
                : True >> si se crea correctamente el archivo de proyecto .mpm
                : False >> si hay un error

        """    
        return self.db_project.projectSaveAs(new_path_file)
        
    def checkProjectChanges(self):
        """ Verifica si hay cambios en el proyecto.

        Returns:
            (bool):
                : True >> si hay cambios en el proyecto
                : False >> si no hay cambios en el proyecto

        """         
        return self.db_project.checkProjectChanges()

    def __instanceDbProject(self, path):
        """Crea una instancia de la base de datos del proyecto.

        Args:
            filePath(str): Ruta del proyecto

        """
        self.db_project = class_database.DataBaseProject(path=path)

