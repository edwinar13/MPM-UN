"""Este módulo contiene las clases para interactuar con las bases de datos json.

class:
    : CreateDataBase.
    : DataBaseConfigMpmun.
    : DataBaseProject.

"""

from time import strftime
from PySide6.QtCore import (QFile, QTime,Signal, QObject)
import json
import os
from clases.Modelo.model_Mesh import ModelMesh

class ModelProject:



    def __init__(self, path, name=None, date=None, hour=None) -> None:
        self.__name = name
        self.__path = path
        self.__date = date
        self.__hour = hour    


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################


    def getName(self):
        """Obtiene el nombre del proyecto.

        Returns:
            name_file (str): Nombre del archivo del proyecto.

        """
        return self.__name
    
    def getPath(self):
        """Obtiene la ruta del proyecto.

        Returns:
            path (str): Ruta del archivo del proyecto.

        """
        return self.__path

    def getDate(self):
        """Obtiene la fecha del proyecto.

        Returns:
            date (str): fecha de la ultima vez que se abrio el proyecto.

        """
        return self.__date

    def getHour(self):
        """Obtiene la hora del proyecto.

        Returns:
            hour (str): hora de la ultima vez que se abrio el proyecto.

        """
        return self.__hour
    
    def getData(self):
        """Obtiene todos los argumentos del proyecto.

        Returns:
            (list): lista de los argumentos del proyecto
                    name_file, path, data, hour

        """ 
        return[self.__name, self.__path, self.__date, self.__hour]
       
    def setData(self, filePath):
        """Establece los argumentos: nombre, fecha (actual) y hora (actual).

        Args:
            filePath(str): ruta del proyecto

        """ 
        self.__hour = QTime.currentTime().toString("hh:mm:ss A ")
        self.__date = strftime("%d/%m/%y")
        self.__name = filePath.split('/')[-1]
        #self.__path = filePath


class ModelProjectCurrent(QObject):
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

    signal_project_changes= Signal(list)
    print("REVISAR :::: el modelo no debe generar una señal mas bien retornalr ")
    print("linea 112, model_Projets.py")
    

    def __init__(self, path_project_current) -> None:
        super().__init__()

        self.__path_db_project = path_project_current
        self.__name_project = self.__path_db_project.split('/')[-1]
        self.__original_copy_db_project = None
        self.__unguarded_copy_db_project = None
        self.__name_doc_py = os.path.basename(__file__) 

        self.meshs=[]


        #inicializa las copias de la base de datos del proyecto
        self.__initDb()
        self.__initMesh()


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
    
    def __initMesh(self):
        meshs = self.selectMeshDB()["TRIANGULARES"]
        for mesh_name in meshs:
            name = meshs[mesh_name]["name"]
            color = meshs[mesh_name]["color"]
            points = meshs[mesh_name]["points"]
            triangles = meshs[mesh_name]["triangles"]

            model_mesh = ModelMesh(name=name, color=color, points=points, triangles=triangles)
            self.meshs.append(model_mesh)


    def getPath(self):
        """Obtiene la ruta del proyecto.

        Returns:
            path (str): Ruta del archivo del proyecto.

        """
        return self.__path_db_project
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

        #try:  
        if name_project != None:          
            self.__unguarded_copy_db_project['INFORMACION']['NOMBREPROYECTO']=name_project
        if location != None:          
            self.__unguarded_copy_db_project['INFORMACION']['LOCALIZACION']=location
        if author != None:        
            self.__unguarded_copy_db_project['INFORMACION']['AUTOR']=author
        if description != None:          
            self.__unguarded_copy_db_project['INFORMACION']['DESCRIPCION']=description
        self.projectSaveState()
        return True
        '''
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <INFORMACION> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
        '''
    

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
            self.projectSaveState()
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
            self.projectSaveState()
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
    
    def deleteItemDrawDB(self, name=None):
        """elimina el item de dibujo (puntos, lineas) de la copia sin guardar de la db del proyecto.

        Args:
            name (dic): Nombre del item a eliminar (default= None).


        Returns:
            (bool): 
                : True >> si se agrega correctamente los items al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 


        try:  
            if  name in self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS']:
                del self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][name]
   
            elif  name in self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS']:
                del self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][name]
            self.projectSaveState()
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

  ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB MALLA       ::::::::::::::::::::
	###############################################################################   
    def selectMeshDB(self):
        """Recupera las mallas contenidas en la copia sin guardas de la db del proyecto.
        Returns:
            (dict): Diccionario con las mallas del proyecto.
        """   

        data_projects_information = self.__unguarded_copy_db_project['MALLAS']
        return data_projects_information
    
    def addMeshDB(self, triangle_mesh=None,name=None, rectangular_mesh=None):
        
        #######################################falta reivar esto
        ########### aca la cla¿ve de la malla no deberia ser el nombre sino el ID
        try:  
            if triangle_mesh != None:    
                print()
                self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][ name]=triangle_mesh
            if rectangular_mesh != None:  
       
                self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][name]=rectangular_mesh
            self.projectSaveState()
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def updateMeshDB(self,name_prev=None, triangle_mesh=None,name=None, rectangular_mesh=None):
        """Actualiza las mallas en la copia sin guardar de la db del proyecto.

        Args:
            triangle_mesh (list): Puntos de la malla (default= None).
            rectangular_mesh (list): Elementos de la malla (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la malla al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 
        try:  
            if triangle_mesh != None:   

                self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'].pop(name_prev)
                self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][name]=triangle_mesh

            if rectangular_mesh != None:  
       
                self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][name]=rectangular_mesh
            self.projectSaveState()
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def deleteMeshDB(self, name=None):
        """Elimina la malla en la copia sin guardar de la db del proyecto.

        Args:
            name (str): Nombre de la malla a eliminar (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la malla al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 
        
 
        try:  

            if name in self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES']:
                del self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][name]

            elif name in self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES']:
                del self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][name]
            self.projectSaveState()
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
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
            #try:
                # se guarda en el archivo
                with open(BD, 'w') as a:
                    a.write(json.dumps(self.__unguarded_copy_db_project)) 
                    a.close()
                            
                # se actualiza la copia original
                with open(BD, 'r') as b: 
                    self.__original_copy_db_project = json.load(b)
                    b.close()
                print("Guardo correctamente en la base de datos")   
                self.projectSaveState()
                validacion=True
            
            #except BaseException as err:
            #    print("[Doc: {}]  Error al agregar registro en <CONFIGURACION> de la base de datos {}".format(self.__name_doc_py,BD))
            #    print("[Tipo: {}, Erro: {}]".format(type(err),err))
            #    validacion=False
            
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
            self.projectSaveState()
            validacion=True
        
        except BaseException as err:
            print("[Doc: {}]  Error al guardar como {}".format(self.__name_doc_py,BD))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            validacion=False
        
        return validacion

    def projectSaveState(self):
        state = self.checkProjectChanges()        
        self.signal_project_changes.emit([self.__name_project, state])

class ModelProjects:
    print("?"*100,"actualizar esta documentacion view_MainWind.. LINE78")
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


    def __init__(self):
        self.path_db_Config="db/db_mpmun.json"
        self.projects = []
        self.loadProjects()
    
    def loadProjects(self):
        """Carga los proyectos de la db del sofware al modelo.
  
        Returns:
            (bool): 
                : True >> si se cargo correctamente los proyectos
                : False >> si no se encontró la db del software.
        """   


        BD = self.path_db_Config
        if QFile.exists(BD):
            with open(BD, 'r') as f: 
                data_projects = json.load(f)
                data_projects = data_projects['ULTIMOSPROYECTOS']  
        else:
            print("No se encontró la base de datos {}".format(self.path_db_Config))
            return False
        
        
        for project in data_projects:
            name = project['nombreArchivo']
            path = project['ruta']
            date = project['fecha']
            hour = project['hora']
            project = ModelProject(path=path, name=name, date=date, hour=hour)
            self.projects.append(project)

        return True
    
    def updateProjectsList(self, selected_project):
        """
        Actualiza la lista de proyectos en el modelo, colocando el proyecto
        seleccionado al principio de la lista y actualizando la base de datos.

        Args:
            selected_project (ModelProject): El proyecto que fue seleccionado.
  
        Returns:
            None
        """
        #actualiza la informacion del proyecto selecionado
        selected_project.setData(selected_project.getPath())

        # actualizar la lista de proyectos con el proyecto seleccionado al inicio
        self.projects.remove(selected_project)
        self.projects.insert(0, selected_project)
        

        # actualizar la nueva lista de proyectos
        data_projects = []
        for project in self.projects:
            data_projects.append({
                'nombreArchivo': project.getName(),
                'ruta': project.getPath(),
                'fecha': project.getDate(),
                'hora': project.getHour()
            })

        BD=self.path_db_Config  
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_setting = json.load(f)
                    data_setting['ULTIMOSPROYECTOS']=data_projects

                with open(BD, 'w') as f:
                    f.write(json.dumps(data_setting))
                validacion=True
                
            except Exception as e:
                print("Error al actualizar los ultimos proyectos en <ULTIMOSPROYECTOS> de la base de datos {}".format(self.path_db_Config))
                print(e)
                validacion=False
                
        else:  
            print("No se encontró la base de datos {}".format(self.path_db_Config))          
            validacion=False

            
                    
        return validacion

    def selectProject(self, path_project):            
        """
        Devuelve el proyecto correspondiente al path especificado.
    
        Args:
            path_project (str): El path del proyecto a seleccionar.
            
        Returns:
            (ModelProject): El proyecto correspondiente al path especificado.
            Si no se encuentra el proyecto, crea y devuelve un nuevo proyecto.
        """
        for project in self.projects:
            if project.getPath() == path_project:
                return project
            
        # Si el proyecto no está en la lista, se crea
        new_project = self.newProject(path_project)
        if new_project:
            return self.selectProject(path_project)  # Llamada recursiva para obtener el proyecto recién creado
        else:
            return None

    def getProjects(self):
        """
        Obtiene una lista de los proyectos del modelo.
  
        Returns:
            (list): Lista de objetos ModelProject que representan los proyectos.
        """
        return self.projects

    def newProject(self, path_project):

        """
        Crea un nuevo proyecto y lo agrega al modelo y a la db de la app.

        Args:
            path_project (str): la ruta del nuevo proyecto.

        Returns:
            (bool): 
                : True >> si el proyecto se creó y agregó correctamente.
                : False >> si el proyecto no se pudo crear o agregar.
        """


        for project in self.projects:
            if project.getPath() == path_project:
                print(f"Proyecto ya existe")
                return False

        # crear un nuevo proyecto
        project = ModelProject(path=path_project)
        project.setData(project.getPath())

        # agregar el proyecto al modelo
        self.projects.insert(0, project)

        # actualizar la nueva lista de proyectos
        data_projects = []
        for project in self.projects:
            data_projects.append({
                'nombreArchivo': project.getName(),
                'ruta': project.getPath(),
                'fecha': project.getDate(),
                'hora': project.getHour()
            })





        BD=self.path_db_Config  
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    data_setting = json.load(f)
                    data_setting['ULTIMOSPROYECTOS']=data_projects

                with open(BD, 'w') as f:
                    f.write(json.dumps(data_setting))
                validacion=True
                
            except Exception as e:
                print("Error al actualizar los ultimos proyectos en <ULTIMOSPROYECTOS> de la base de datos {}".format(self.path_db_Config))
                print(e)
                validacion=False
                
        else:  
            print("No se encontró la base de datos {}".format(self.path_db_Config))          
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
            self.projects = []
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
                    print("Error al eliminar registros de <ULTIMOSPROYECTOS> de la base de datos {}".format(self.__path_db_Config))
                    validacion=False
            else:
                print("No se encontró la base de datos {}".format(self.__path_db_Config))  
                validacion=False
            return validacion


        except BaseException as err:     
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            validacion=False
        return validacion
    
    def createProjectFile(self, path_project):
        """
        Crea un nuevo archivo .mpm en la ruta especificada.

        Args:
            path_project (str): la ruta del nuevo archivo .mpm.

        Returns:
            (bool): 
                : True >> si el archivo se creó correctamente.
                : False >> si el archivo no se pudo crear.
        """


        try:
            filePath = os.path.splitext(path_project)[0] + '.mpm'
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
                "NOITEMS":0,
                "PUNTOS": {},
                "LINEAS": {},
            }
            data['MALLAS'] = {
                "TRIANGULARES": {},
                "RECTANGULARES": {}
            }
            data['PUNTOSMATERIAL'] = {}
            data['MATERIALES'] = {}
            data['RESULTADOS'] = {}

            with open(filePath, 'w') as file:
                file.write(json.dumps(data))
                print('Archivo (mpm) del proyecto fue creado correctamente en: [{}]'.format(filePath))
            
            return True
        except Exception as e:
            print(f"No se pudo crear el archivo del proyecto: {e}")
            return False
    




        """
        def deleteProject(self, project):
            self.projects.remove(project)
            # aca va la lógica eliminar un proyecto específico de la base de datos
    
        def updateProject(self, project):
            # Lógica para actualizar el proyecto en la base de datos
            pass
            
            QMessageBox.critical(objeto, "MPM-UN", "Error class_projects addProjects",
                                QMessageBox.Ok)
        """