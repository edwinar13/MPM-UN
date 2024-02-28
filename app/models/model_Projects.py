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

class ModelProjects:
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
        self.path_db_Config="app/resources/db/db_mpmun.json"
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
                "GRAVEDAD": 9.80,
                "DAMPFAC": 0.00
            }
            data['ITEMSDIBUJO'] = {
                "NOITEMS":0,
                "PUNTOS": {},
                "LINEAS": {},
            }
            data['MALLAS'] = {
                "MALLAFONDO":{
                    "SIZEDX": 3.0,
                    "SIZEDY": 3.0,
                    "SIZEELEMENT": 0.5,
                    "COLOR": "#555696",
                    "POINTS": [
                [
                    0.0,
                    0.0
                ],
                [
                    0.5,
                    0.0
                ],
                [
                    1.0,
                    0.0
                ],
                [
                    1.5,
                    0.0
                ],
                [
                    2.0,
                    0.0
                ],
                [
                    2.5,
                    0.0
                ],
                [
                    3.0,
                    0.0
                ],
                [
                    0.0,
                    0.5
                ],
                [
                    0.5,
                    0.5
                ],
                [
                    1.0,
                    0.5
                ],
                [
                    1.5,
                    0.5
                ],
                [
                    2.0,
                    0.5
                ],
                [
                    2.5,
                    0.5
                ],
                [
                    3.0,
                    0.5
                ],
                [
                    0.0,
                    1.0
                ],
                [
                    0.5,
                    1.0
                ],
                [
                    1.0,
                    1.0
                ],
                [
                    1.5,
                    1.0
                ],
                [
                    2.0,
                    1.0
                ],
                [
                    2.5,
                    1.0
                ],
                [
                    3.0,
                    1.0
                ],
                [
                    0.0,
                    1.5
                ],
                [
                    0.5,
                    1.5
                ],
                [
                    1.0,
                    1.5
                ],
                [
                    1.5,
                    1.5
                ],
                [
                    2.0,
                    1.5
                ],
                [
                    2.5,
                    1.5
                ],
                [
                    3.0,
                    1.5
                ],
                [
                    0.0,
                    2.0
                ],
                [
                    0.5,
                    2.0
                ],
                [
                    1.0,
                    2.0
                ],
                [
                    1.5,
                    2.0
                ],
                [
                    2.0,
                    2.0
                ],
                [
                    2.5,
                    2.0
                ],
                [
                    3.0,
                    2.0
                ],
                [
                    0.0,
                    2.5
                ],
                [
                    0.5,
                    2.5
                ],
                [
                    1.0,
                    2.5
                ],
                [
                    1.5,
                    2.5
                ],
                [
                    2.0,
                    2.5
                ],
                [
                    2.5,
                    2.5
                ],
                [
                    3.0,
                    2.5
                ],
                [
                    0.0,
                    3.0
                ],
                [
                    0.5,
                    3.0
                ],
                [
                    1.0,
                    3.0
                ],
                [
                    1.5,
                    3.0
                ],
                [
                    2.0,
                    3.0
                ],
                [
                    2.5,
                    3.0
                ],
                [
                    3.0,
                    3.0
                ]
            ],
                    "QUADRILATERALS": [
                        [
                            1,
                            2,
                            9,
                            8
                        ],
                        [
                            2,
                            3,
                            10,
                            9
                        ],
                        [
                            3,
                            4,
                            11,
                            10
                        ],
                        [
                            4,
                            5,
                            12,
                            11
                        ],
                        [
                            5,
                            6,
                            13,
                            12
                        ],
                        [
                            6,
                            7,
                            14,
                            13
                        ],
                        [
                            8,
                            9,
                            16,
                            15
                        ],
                        [
                            9,
                            10,
                            17,
                            16
                        ],
                        [
                            10,
                            11,
                            18,
                            17
                        ],
                        [
                            11,
                            12,
                            19,
                            18
                        ],
                        [
                            12,
                            13,
                            20,
                            19
                        ],
                        [
                            13,
                            14,
                            21,
                            20
                        ],
                        [
                            15,
                            16,
                            23,
                            22
                        ],
                        [
                            16,
                            17,
                            24,
                            23
                        ],
                        [
                            17,
                            18,
                            25,
                            24
                        ],
                        [
                            18,
                            19,
                            26,
                            25
                        ],
                        [
                            19,
                            20,
                            27,
                            26
                        ],
                        [
                            20,
                            21,
                            28,
                            27
                        ],
                        [
                            22,
                            23,
                            30,
                            29
                        ],
                        [
                            23,
                            24,
                            31,
                            30
                        ],
                        [
                            24,
                            25,
                            32,
                            31
                        ],
                        [
                            25,
                            26,
                            33,
                            32
                        ],
                        [
                            26,
                            27,
                            34,
                            33
                        ],
                        [
                            27,
                            28,
                            35,
                            34
                        ],
                        [
                            29,
                            30,
                            37,
                            36
                        ],
                        [
                            30,
                            31,
                            38,
                            37
                        ],
                        [
                            31,
                            32,
                            39,
                            38
                        ],
                        [
                            32,
                            33,
                            40,
                            39
                        ],
                        [
                            33,
                            34,
                            41,
                            40
                        ],
                        [
                            34,
                            35,
                            42,
                            41
                        ],
                        [
                            36,
                            37,
                            44,
                            43
                        ],
                        [
                            37,
                            38,
                            45,
                            44
                        ],
                        [
                            38,
                            39,
                            46,
                            45
                        ],
                        [
                            39,
                            40,
                            47,
                            46
                        ],
                        [
                            40,
                            41,
                            48,
                            47
                        ],
                        [
                            41,
                            42,
                            49,
                            48
                        ]
                    ],
                    "POINTSBOUNDARYTOP": [
                        [
                            0.0,
                            3.0
                        ],
                        [
                            0.5,
                            3.0
                        ],
                        [
                            1.0,
                            3.0
                        ],
                        [
                            1.5,
                            3.0
                        ],
                        [
                            2.0,
                            3.0
                        ],
                        [
                            2.5,
                            3.0
                        ],
                        [
                            3.0,
                            3.0
                        ]
                    ],
                    "POINTSBOUNDARYBOTTOM": [
                        [
                            0.0,
                            0.0
                        ],
                        [
                            0.5,
                            0.0
                        ],
                        [
                            1.0,
                            0.0
                        ],
                        [
                            1.5,
                            0.0
                        ],
                        [
                            2.0,
                            0.0
                        ],
                        [
                            2.5,
                            0.0
                        ],
                        [
                            3.0,
                            0.0
                        ]
                    ],
                    "POINTSBOUNDARYLEFT": [
                        [
                            0.0,
                            0.0
                        ],
                        [
                            0.0,
                            0.5
                        ],
                        [
                            0.0,
                            1.0
                        ],
                        [
                            0.0,
                            1.5
                        ],
                        [
                            0.0,
                            2.0
                        ],
                        [
                            0.0,
                            2.5
                        ],
                        [
                            0.0,
                            3.0
                        ]
                    ],
                    "POINTSBOUNDARYRIGHT": [
                        [
                            3.0,
                            0.0
                        ],
                        [
                            3.0,
                            0.5
                        ],
                        [
                            3.0,
                            1.0
                        ],
                        [
                            3.0,
                            1.5
                        ],
                        [
                            3.0,
                            2.0
                        ],
                        [
                            3.0,
                            2.5
                        ],
                        [
                            3.0,
                            3.0
                        ]
                    ],
                    "NODESBOUNDARYTOP": [
                        43,
                        44,
                        45,
                        46,
                        47,
                        48,
                        49
                    ],
                    "NODESBOUNDARYBOTTOM": [
                        1,
                        2,
                        3,
                        4,
                        5,
                        6,
                        7
                    ],
                    "NODESBOUNDARYLEFT": [
                        1,
                        8,
                        15,
                        22,
                        29,
                        36,
                        43
                    ],
                    "NODESBOUNDARYRIGHT": [
                        7,
                        14,
                        21,
                        28,
                        35,
                        42,
                        49
                    ]
                    },
                "TRIANGULARES": {},
                "CUADRILATEROS": {}
                }
            data['PUNTOSMATERIAL'] = {}
            data['MATERIALES'] = {}
            data['CONTORNOS'] = {}
            
            data['RESULTADOS'] = {
                "DATOSBASE": {},
                "MATERIALES" :{},
                "PUNTOSMATERIAL":{},
                "MALLAFONDO":{},
                "CONTORNOS":{},
                "DATOSTIEMPOS":{},        
                "TIEMPOSANALISIS" :[],
                "TIEMPOSGRAFICAR" :[],
                "MINIMOSRESULTADOS": {},
                "MAXIMOSRESULTADOS": {},
                "RESULTADOSNODOS" :{}
            }

            with open(filePath, 'w') as file:
                file.write(json.dumps(data))
                print('Archivo (mpm) del proyecto fue creado correctamente en: [{}]'.format(filePath))
            
            return True
        except Exception as e:
            print(f"No se pudo crear el archivo del proyecto: {e}")
            return False
    

