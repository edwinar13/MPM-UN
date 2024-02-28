from PySide6.QtCore import ( Slot, Signal,QObject)
from views.draw.view_WidgetDrawMenuData import ViewWidgetDrawMenuData
from models.model_ProjectCurrent import ModelProjectCurrent
 


class ControllerMenuData(QObject):

    signal_paint_draw = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.view_menu_data = ViewWidgetDrawMenuData()
        self.model_current_project = None
        
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
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
        self.view_menu_data.signal_show_hide_items.connect(self.showHideItems)
        self.view_menu_data.signal_show_hide_label.connect(self.showHideLabel)

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
    
    def configDrawMenuData(self):
        dataInfo = self.model_current_project.getDataInfo()
        dataConf = self.model_current_project.getDataConfig()
        self.view_menu_data.setTextWidget(dataInfo, dataConf)

    def getView(self):
        return self.view_menu_data    

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    @Slot(bool)
    def showHideItems(self, show_items):
        self.model_current_project.showHideItems(show_items)


    @Slot(bool)
    def showHideLabel(self, show_label):
        self.model_current_project.showHideLabel(show_label)


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
            self.model_current_project.updateInformation(name_project=value_input)
            
        elif name_attribute == "location":          
            self.model_current_project.updateInformation(location=value_input)
            
        elif name_attribute == "author":
            self.model_current_project.updateInformation(author=value_input)
            
        elif name_attribute == "description":
            self.model_current_project.updateInformation(description=value_input)
            
        elif name_attribute == "gravity":
            self.model_current_project.updateConfig(gravity=value_input)
            
        elif name_attribute == "dampfac":
            self.model_current_project.updateConfig(dampfac=value_input)
    
    @Slot(str)
    def paintDrawCommand(self, command:str):           
        if command == "point" :
            self.model_current_project.commandPoint({"step":1, "data":None})                

        elif command == "line" :
            self.model_current_project.commandLine({"step":1, "data":None})    

        elif command == "move" :
            self.model_current_project.commandMove({"step":1, "data":None})    

        elif command == "copy" :
            self.model_current_project.commandCopy({"step":1, "data":None})    

        elif command == "rotate" :
            self.model_current_project.commandRotate({"step":1, "data":None})    
            
        elif command == "erase" :
            self.model_current_project.commandErase({"step":1, "data":None})    

        elif command == "import" :
            self.model_current_project.commandImport({"step":1, "data":None})    

        elif command == "intersection" :
            self.model_current_project.commandIntersection({"step":1, "data":None})   

        elif command == "rule" :
           self.model_current_project.commandRule({"step":1, "data":None})  


