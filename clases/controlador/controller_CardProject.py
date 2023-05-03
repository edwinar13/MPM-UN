

from clases.Vista.view_WidgetCardProject import ViewWidgetCardProjectHome
 
class ControllerCardProject():

    def __init__(self, controller_PageHome, project) -> None:

        self.controller_PageHome= controller_PageHome
        self.name, self.path, self.data, self.hour = project.getData()

        self.view_card_project = ViewWidgetCardProjectHome(
                                                           cardName=self.name, 
                                                           cardPath=self.path, 
                                                           cardDataTime=self.data, 
                                                           cardHour=self.hour)
        
        self.view_card_project.signal_open_project.connect(self.openProject)
    
    def openProject(self):
        project_path = self.path  
        self.controller_PageHome.controller_main.openProject(project_path)        

