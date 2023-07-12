from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Vista.view_WidgetDrawMenuBoundary import ViewWidgetDrawMenuBoundary
 
class ControllerMenuBoundary():

    def __init__(self) -> None:

        #Crea la vista menu Boundary
        self.view_menu_boundary = ViewWidgetDrawMenuBoundary()
        self.model_current_project = None
        
    def getView(self):
        return self.view_menu_boundary



    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project




