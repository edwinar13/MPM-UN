from PySide6.QtCore import ( Slot, Signal,QObject)
from clases.Vista.view_WidgetDrawMenuData import ViewWidgetDrawMenuData
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
 
class ControllerMenuData(QObject):

    signal_paint_draw = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        #Crea la vista menu data
        self.view_menu_data = ViewWidgetDrawMenuData()
        self.current_project = None
        self.view_menu_data.signal_data_project.connect(self.updateDate)


        self.view_menu_data.signal_paint_point.connect(lambda: self.paintDrawCommand("point"))
        self.view_menu_data.signal_paint_line.connect(lambda: self.paintDrawCommand("line"))
        self.view_menu_data.signal_paint_move.connect(lambda: self.paintDrawCommand("move"))
        self.view_menu_data.signal_paint_copy.connect(lambda: self.paintDrawCommand("copy"))
        self.view_menu_data.signal_paint_rotate.connect(lambda: self.paintDrawCommand("rotate"))
        self.view_menu_data.signal_paint_erase.connect(lambda: self.paintDrawCommand("erase"))
        self.view_menu_data.signal_paint_import.connect(lambda: self.paintDrawCommand("import"))
        self.view_menu_data.signal_paint_intersection.connect(lambda: self.paintDrawCommand("intersection"))
        self.view_menu_data.signal_paint_rule.connect(lambda: self.paintDrawCommand("rule"))


    def paintDrawCommand(self, command):           
        if command == "point" :
            self.current_project.commandPoint({"step":1, "data":None})                

        elif command == "line" :
            self.current_project.commandLine({"step":1, "data":None})    

        elif command == "move" :
            self.current_project.commandMove({"step":1, "data":None})    

        elif command == "copy" :
            self.current_project.commandCopy({"step":1, "data":None})    

        elif command == "rotate" :
            self.current_project.commandRotate({"step":1, "data":None})    
            
        elif command == "erase" :
            self.current_project.commandErase({"step":1, "data":None})    

        elif command == "import" :
            self.current_project.commandImport({"step":1, "data":None})    

        elif command == "intersection" :
            self.current_project.commandIntersection({"step":1, "data":None})   

        elif command == "rule" :
           self.current_project.commandRule({"step":1, "data":None})  


    def getView(self):
        return self.view_menu_data    

    def setCurrentProject(self,current_project:ModelProjectCurrent):
        self.current_project = current_project
    
    def configDrawMenuData(self):
        dataInfo = self.current_project.getDataInfo()
        dataConf = self.current_project.getDataConfig()
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
            self.current_project.updateInformation(name_project=value_input)
            
        elif name_attribute == "location":          
            self.current_project.updateInformation(location=value_input)
            
        elif name_attribute == "author":
            self.current_project.updateInformation(author=value_input)
            
        elif name_attribute == "description":
            self.current_project.updateInformation(description=value_input)
            
        elif name_attribute == "gravity":
            self.current_project.updateConfig(gravity=value_input)
