
""" Este módulo contiene controlador de la vista pagina home """
from PySide6.QtCore import ( QFile, Slot)
from clases.Vista.view_PageHome import  ViewPageHome
from clases.Controlador.controller_CardProject import ControllerCardProject
from clases.Modelo.model_Projects import ModelProject
import typing

 
class ControllerPageHome():

    def __init__(self, controller_main, list_projects) -> None:    

        self.controller_main = controller_main 
        self.controller_card_projects = []

        #Crea la vista ViewPageHome
        self.view_page_home = ViewPageHome()


        self.view_page_home.signal_new_project.connect(self.newProject)
        self.view_page_home.signal_open_project.connect(self.openProject)      
        
        

        self.updateProjectsCartView(list_projects)
        

    def getView(self):
        return self.view_page_home
    
    def updateProjectsCartView(self, list_projects):
        # Crea y agrega cada card de proyecto reciente
        self.view_page_home.removeCardsProjectsRecent()   
        No_project = 1
        max_projects = 15
        for project in list_projects:  
            project = typing.cast(ModelProject, project)
            if No_project <= max_projects and QFile.exists(project.getPath()):          
                controller_card_project = ControllerCardProject(self, project)
                self.view_page_home.addCardProjectsRecent(controller_card_project.view_card_project)
                self.controller_card_projects.append(controller_card_project)
                No_project += 1
        self.view_page_home.addCardEmptyProjectsRecent()


    @Slot(str)
    def openProject(self, path): 
        if path:
            self.controller_main.openProject(path)     

    @Slot(str)
    def newProject(self,path):
        if path:
            self.controller_main.newProject(path)     







 
 