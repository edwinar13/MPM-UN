

from clases.Vista.view_WidgetDrawMenuBoundary import ViewWidgetDrawMenuBoundary
 
class ControllerMenuBoundary():

    def __init__(self) -> None:

        #Crea la vista menu Boundary
        self.view_menu_boundary = ViewWidgetDrawMenuBoundary()
        
    def getView(self):
        return self.view_menu_boundary



