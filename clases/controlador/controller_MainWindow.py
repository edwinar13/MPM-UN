
""" Este módulo contiene controlador de la vista Ui_MainWindow"""
from PySide6.QtCore import ( Slot, QFile)
import typing
from clases.Vista.view_MainWindow import ViewMainWindow
from clases.Modelo.model_Projects import ModelProjects, ModelProject
from clases.controlador.controller_PageHome import ControllerPageHome
from clases.controlador.controller_PageDraw import ControllerPageDraw

 
class ControllerMainWindow():

    def __init__(self) -> None:

        self.current_project =None

        # cargar proyectos recientes
        self.model_projects = ModelProjects()

        #Crea la vista MainWindow        
        self.view_main_window = ViewMainWindow()
        self.view_main_window.show()
        self.view_main_window.updateProjectsRecentMenuSup(self.getProjectPaths())

        # crea el controlador de las page
        self.controller_page_home = ControllerPageHome(self, self.getProjects())
        self.controller_page_draw = ControllerPageDraw(self)

        # se agrega las vistas page a la vista main
        self.view_main_window.setPageWidget("home",self.controller_page_home.getView())
        self.view_main_window.setPageWidget("draw",self.controller_page_draw.getView())
        
        self.view_main_window.signal_new_project.connect(self.newProject)
        self.view_main_window.signal_open_project.connect(self.openProject)       

    def getProjectPaths(self):
        list_path_projects = []
        for project in  self.getProjects():
            project = typing.cast(ModelProject, project)
            list_path_projects.append(project.getPath())
        return list_path_projects   
    
    def getProjects(self):
        return self.model_projects.getProjects()


    @Slot(str)
    def openProject(self, path_project):

        if self.current_project and self.current_project.getPath() == path_project:
            return        
        if not QFile.exists(path_project):
            return    
        self.current_project = self.model_projects.selectProject(path_project)
        if self.current_project:
            self.model_projects.updateProjectsList(self.current_project)
            self.view_main_window.updateProjectsRecentMenuSup(self.getProjectPaths())
            self.controller_page_home.updateProjectsCartView(self.getProjects())
            self.view_main_window.updateTitleWindow(self.current_project.getName())

            #inicializar el proyecto ...

            self.view_main_window.showMessageStatusBar("satisfactory","Proyecto <<{}>> abierto con éxito".format(self.current_project.getName().replace(".mpm","")))


    @Slot(str)
    def newProject(self, path_project):
        if  self.model_projects.createProjectFile(path_project):  
            if self.model_projects.newProject(path_project):
                self.openProject(path_project)
