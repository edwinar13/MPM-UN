from PySide6.QtCore import ( Slot, Signal,QObject)
from clases.Vista.view_WidgetDrawMenuData import ViewWidgetDrawMenuData
from clases.Modelo.model_Projects import ModelProjectCurrent
 
class ControllerMenuData(QObject):

    signal_paint_draw = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        #Crea la vista menu data
        self.view_menu_data = ViewWidgetDrawMenuData()
        self.current_project = None
        self.view_menu_data.signal_data_project.connect(self.updateDate)


        self.view_menu_data.signal_paint_point.connect(lambda: self.paintDraw("point"))
        self.view_menu_data.signal_paint_line.connect(lambda: self.paintDraw("line"))
        self.view_menu_data.signal_paint_move.connect(lambda: self.paintDraw("move"))
        self.view_menu_data.signal_paint_copy.connect(lambda: self.paintDraw("copy"))
        self.view_menu_data.signal_paint_rotate.connect(lambda: self.paintDraw("rotate"))
        self.view_menu_data.signal_paint_erase.connect(lambda: self.paintDraw("erase"))
        self.view_menu_data.signal_paint_import.connect(lambda: self.paintDraw("import"))
        self.view_menu_data.signal_paint_intersection.connect(lambda: self.paintDraw("intersection"))
        self.view_menu_data.signal_paint_rule.connect(lambda: self.paintDraw("rule"))


    def paintDraw(self, signal_type):
           self.signal_paint_draw.emit(signal_type)


    def getView(self):
        return self.view_menu_data    

    def setCurrentProject(self,current_project:ModelProjectCurrent):
        self.current_project = current_project
    
    def configDrawMenuData(self):
        dataInfo = self.current_project.selectInformationDB()
        dataConf = self.current_project.selectConfigDB()
        self.view_menu_data.setTextWidget(dataInfo, dataConf)
        
 

    @Slot(dict)
    def updateDate(self,date:dict):

        """ Actualiza la información recibida, en la copia de la bd del proyecto.

        Args:
            value_input (str): valor de entrada
            name_attribute (str): nombre del atributo

        """
        name_attribute = list(date.keys())[0]
        value_input = date[name_attribute]

        if name_attribute == "name_project":     
            self.current_project.updateInformationDB(name_project=value_input)
            
        elif name_attribute == "location":          
            self.current_project.updateInformationDB(location=value_input)
            
        elif name_attribute == "author":
            self.current_project.updateInformationDB(author=value_input)
            
        elif name_attribute == "description":
            self.current_project.updateInformationDB(description=value_input)
            
        elif name_attribute == "gravity":
            self.current_project.updateConfigDB(gravity=value_input)
