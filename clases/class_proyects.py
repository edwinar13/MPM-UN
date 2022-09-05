import json
from PySide6.QtCore import (QFile)
from PySide6.QtWidgets import (QMessageBox)

class Projects ():    
    def __init__(self) -> None:
        self.pathDBConfig="config/database_mpmun.json"
        self.datos = {}  
        self.list_projects= []
        self.datos_proyectos = {}

    def getListProjects(self, objeto):
        """CONSULTA LOS PROYECTOS RECIENTES EN LA DB
        Recibe >>
            objeto: QWidget
        Devuelve >>> 
            lista de proyectos recientes"""
        BD = self.pathDBConfig
        if QFile.exists(BD):		  
            #try:
                with open(BD, 'r') as f: 
                    self.datos_proyectos = json.load(f)
                    for proyecto in self.datos_proyectos['ULTIMOSPROYECTOS']:
                        name=proyecto['nombreArchivo']
                        path=proyecto['ruta']
                        data=proyecto['fecha']
                        hour=proyecto['hora']
                        Project(name,path,data,hour)
                        self.list_projects.append(Project(name,path,data,hour))
            #except:
            #    QMessageBox.critical(objeto, "MPM-UN", "Error getListProjects ",
            #                        QMessageBox.Ok)
        else:
            QMessageBox.critical(objeto, "MPM-UN", "No se encontro la base de datos de MPM-UN", QMessageBox.Ok)
        #print(self.list_projects)
        return self.list_projects

    def deleteListProjects(self,objeto):
        """ELIMINA LA LISTA DE PROYECTOS RECINETES EN LA DB
        Recibe >>
            objeto: QWidget
        devuelve >>
            True: si se eliminaron los proyectos recientes
            False: si hay un error o no se encontro la DB"""
        BD = self.pathDBConfig
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    self.datos_proyectos = json.load(f)
                    self.datos_proyectos['ULTIMOSPROYECTOS']=[]
                    self.list_projects=[]
                
                with open(BD, 'w') as f:
                    f.write(json.dumps(self.datos_proyectos))
                validacion=True
            except:
                QMessageBox.critical(objeto, "MPM-UN", "Error deleteListProjects",
                                    QMessageBox.Ok)
                validacion=False
        else:
            QMessageBox.critical(objeto, "MPM-UN", "No se encontro la base de datos de MPM-UN"
                                "   ", QMessageBox.Ok)
            validacion=False
        return validacion

    def addProjectToProjects(self, objeto, nombreArchivo, fecha, hora, ruta):
        """AGREGA UN NUEVO PROYECTO A LOS PROYECTOS RECIENTES DE LA DB
        Recibe >>
            objeto: QWidget
            nombreArchivo, fecha, hora, ruta
        devuelve >>
            True: si se eliminaron los proyectos recientes
            False: si hay un error o no se encontro la DB"""

        BD=self.pathDBConfig
        if QFile.exists(BD):		  
            try:
                with open(BD, 'r') as f: 
                    #self.datos_proyectos = json.load(f)
                    #projects = self.datos_proyectos['ULTIMOSPROYECTOS']
                    fila = 0
                    existe = False
                    for project in self.list_projects:
                        if project.ruta == ruta:
                            existe = True
                            break
                        fila += 1
                    if existe:
                        self.datos_proyectos['ULTIMOSPROYECTOS'].pop(fila)
                        self.list_projects.pop(fila)
                    self.datos_proyectos['ULTIMOSPROYECTOS'].insert(0,{'nombreArchivo': nombreArchivo,
                                                'ruta': ruta,
                                                'fecha': fecha,
                                                'hora': hora})
                    self.list_projects.insert(0,Project(nombreArchivo, ruta, fecha, hora))


                with open(BD, 'w') as f:
                    f.write(json.dumps(self.datos_proyectos))
                validacion=True
            except:
                QMessageBox.critical(objeto, "MPM-UN", "Error addListProjects",
                                    QMessageBox.Ok)
                validacion=False
        else:
            QMessageBox.critical(objeto, "MPM-UN", "No se encontro la base de datos de MPM-UN"
                                "   ", QMessageBox.Ok)
            validacion=False
        return validacion

    def printProjects(self):
        """ IMPRIME EN CONSOLA LOS PROYECTOS RECIENTES EN LA DB"""
        print(self.datos)
    
    def newProject(self, fileName):
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

    def opeProject(objeto, fileName):
        if QFile.exists(fileName):		  
            #try:
                with open(fileName, 'r') as f: 
                    datos = json.load(f)
                    datosDevueltos_1 = datos['MALLA']['COORDENADAS_CONTORNO']
                    datosDevueltos_2 = datos['MALLA']['COORDENADAS_MALLA']
                    datosDevueltos_3 = datos['MALLA']['INI_MALLA']
                    datosDevueltos_4 = datos['MALLA']['NLEX_MALLA']
                    datosDevueltos_5 = datos['PUNTOMATERIAL']
            
            #except:
            #	QMessageBox.critical(objeto, "MPMGeo", "Error opeProject ",
            #						 QMessageBox.Ok)
                
        else:
            QMessageBox.critical(objeto, "MPMGeo", "No se encontro la base de datos de MPMGeo"
                                "   ", QMessageBox.Ok)
        return datosDevueltos_1, datosDevueltos_2, datosDevueltos_3, datosDevueltos_4, datosDevueltos_5
"""
    def addProject(self, object):
        self.list_projects.append(object)

"""
class Project():
    def __init__(self,nombreArchivo,ruta,fecha,hora) -> None:
        self.nombreArchivo = nombreArchivo
        self.ruta = ruta
        self.fecha = fecha
        self.hora = hora
    def getData(self):
        return[self.nombreArchivo, self.ruta, self.fecha, self.hora]

"""
        for proyecto in self.dataProjects['ULTIMOSPROYECTOS']:
            name=proyecto['nombreArchivo']
            path=proyecto['ruta']
            data=proyecto['fecha']
            hour=proyecto['hora']
            Project(name,path,data,hour)
            self.projects.addProject(Project(name,path,data,hour))
        print("--------------------------------------------------------------")
        print(self.projects.list_projects)
        print("--------------------------------------------------------------")

"""