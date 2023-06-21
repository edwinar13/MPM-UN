
""" Este módulo contiene controlador de la vista Ui_MainWindow"""
from PySide6.QtCore import ( Slot, QFile,QTimer)
import typing
from datetime import datetime
from clases.Vista.view_MainWindow import ViewMainWindow
from clases.Modelo.model_Projects import ModelProjects, ModelProject, ModelProjectCurrent
from clases.Controlador.controller_PageHome import ControllerPageHome
from clases.Controlador.controller_PageDraw import ControllerPageDraw
from clases.Controlador.controller_PageSetting import ControllerPageSetting
from clases.class_ui_dialog_msg import DialogMsg


 
class ControllerMainWindow():

    def __init__(self) -> None:

        self.current_project = None

        # cargar proyectos recientes
        self.model_projects = ModelProjects()

        #Crea la vista MainWindow        
        self.view_main_window = ViewMainWindow()
        self.view_main_window.show()
        self.view_main_window.updateProjectsRecentMenuSup(self.getProjectPaths())

        # ::::::::::::::::::::   SEÑALES   ::::::::::::::::::::
        self.view_main_window.signal_new_project.connect(self.newProject)
        self.view_main_window.signal_open_project.connect(self.openProject)   
        self.view_main_window.signal_clear_recent_project.connect(self.clearRecentProject)   
        self.view_main_window.signal_selected_menu_button.connect(self.selectedMenuSide)
        self.view_main_window.signal_toolButton_statusBar.connect(self.buttonStatusBar)
        self.view_main_window.signal_close_app.connect(self.closeApp)
        self.view_main_window.signal_action_menu_save.connect(self.saveData)
        self.view_main_window.signal_action_menu_saveAs.connect(self.saveAsData)
        self.view_main_window.signal_change_theme.connect(self.changeTheme)
        self.view_main_window.signal_action_menu_undo.connect(self.undo)
        self.view_main_window.signal_action_menu_redo.connect(self.redo)




        # iniciando Tiempo de autoguardado
        # = tiempo * (60seg) * (1000*miliseg)
        self.autosave = False
        self.mili_second_save = 60 * 60 * 1000 # Tiempo
        self.timer_save = QTimer()
        self.timer_save.setObjectName("timer_save")
        self.timer_save.timeout.connect(self.__save_auto)
        self.timer_save.start( self.mili_second_save)
  

        # crea el controlador de las page
        self.controller_page_home = ControllerPageHome(self, self.getProjects())
        self.controller_page_draw = ControllerPageDraw(self)

        self.controller_page_setting = ControllerPageSetting(self)



        self.controller_page_draw.view_page_draw.signal_hide_show_draw.connect(self.hideShowDraw)

        # se agrega las vistas page a la vista main
        self.view_main_window.setPageWidget("home",self.controller_page_home.getView())
        self.view_main_window.setPageWidget("draw",self.controller_page_draw.getView())
        self.view_main_window.setPageWidget("setting",self.controller_page_setting.getView())
        
        self.controller_page_draw.controller_graphics_draw.signal_coor_mouse.connect(self._printStatusBarCoor)


        #self.controller_page_draw.signal_console_hise_show.connect(self.console_hise_show)

        self.selectedMenuSide("toolButton_home")
        



    def undo(self):   
        """ """
        self.controller_page_draw.undo()

    def redo(self):   
        """ """
        self.controller_page_draw.redo()
        


    @Slot(str)
    def selectedMenuSide(self, nameSelectedMenuButton):

        nameButton = nameSelectedMenuButton

        if nameButton==self.view_main_window.ui.toolButton_home.objectName() : 
            self.previous_selected_button = 1
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button)
            self.setting = True     

        elif nameButton==self.view_main_window.ui.toolButton_drawData.objectName() :
            self.previous_selected_button = 2
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button)
            self.controller_page_draw.selectMenu("data")       
            self.setting = True

        elif nameButton==self.view_main_window.ui.toolButton_drawMesh.objectName() :
            self.previous_selected_button = 3
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button)
            self.controller_page_draw.selectMenu("mesh")               
            self.setting = True

        elif nameButton==self.view_main_window.ui.toolButton_drawPoint.objectName() :
            self.previous_selected_button = 4
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button) 
            self.controller_page_draw.selectMenu("pointMaterial")
            self.setting = True

        elif nameButton==self.view_main_window.ui.toolButton_drawBoundary.objectName() :
            self.previous_selected_button = 5
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button) 
            self.controller_page_draw.selectMenu("boundary")
            self.setting = True
            
        elif nameButton==self.view_main_window.ui.toolButton_viewResult.objectName():
            self.previous_selected_button = 6
            self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button)
            self.setting = True
        
        elif nameButton==self.view_main_window.ui.toolButton_setting.objectName():
            
            if self.setting == True :
                self.view_main_window.viewToolButtonMenuLat(7)
                self.setting = False
            elif self.setting == False:            
                self.view_main_window.viewToolButtonMenuLat(self.previous_selected_button)
                self.setting = True

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


        #verifica si hay un proyecto actual y si es el mimo que se abre
        if self.current_project:
            if self.current_project.getPath() == path_project:
                self.view_main_window.viewToolButtonMenuLat(2)  
                return  

        #Verifica si no Existe la db
        if not QFile.exists(path_project):
            self.__showMessageCritical("No se ha encontrado el documento: {}".format(path_project)) 
            return  
        

        
        # Configura proyectos recientes
        current_project_ = self.model_projects.selectProject(path_project)        
        self.model_projects.updateProjectsList(current_project_)
        self.view_main_window.updateTitleWindow(current_project_.getName())
        self.view_main_window.updateProjectsRecentMenuSup(self.getProjectPaths())
        self.controller_page_home.updateProjectsCartView(self.getProjects())


        #Configura nuevo proyecto
        self.current_project = ModelProjectCurrent(path_project)   
        self.current_project.signal_project_changes.connect(self.projectChanges)
        self.view_main_window.activateMenuLat()
        self.selectedMenuSide("toolButton_drawData")  

        
        self.controller_page_draw.openCurrentProject(self.current_project)

        #inicializar el proyecto ...



        self.view_main_window.showMessageStatusBar("satisfactory","Proyecto <<{}>> abierto con éxito".format(current_project_.getName().replace(".mpm","")))


    @Slot(str)
    def newProject(self, path_project):
        if  self.model_projects.createProjectFile(path_project):  
            if self.model_projects.newProject(path_project):
                self.openProject(path_project)
                
    def clearRecentProject(self):
        self.view_main_window.updateProjectsRecentMenuSup([])
        self.controller_page_home.updateProjectsCartView([])      
        self.model_projects.deleteProjects()             


    def closeApp(self):
        """Evento al cerrar la ventana main window, se valida si hay proyecto actual y hay cambio,
         en ese caso se abre cuadro de dialogo para confirmar si guarda o no."""
       
        if self.current_project != None:
            checkProjectChanges = self.current_project.checkProjectChanges()            
            if checkProjectChanges: 
                dialoMsg = DialogMsg(self.view_main_window, 1, 
                                        "¿Quiere guardar los cambios de este proyecto?", 
                                        "has realizado cambios")
                dialoMsg.setTypeIcon(0)
                dialoMsg.setTextDescription("Has realizado cambios en el archivo {}".format(self.current_project.getPath()))
                dialoMsg.setModal(True)
                dialoMsg.exec()
                result = dialoMsg.getButtonSelected()
                #Guardar
                if result == "save":
                    print("# Guardar = {}".format(self.current_project.saveDataDb()))
                    #??? event.accept()
                    self.view_main_window.close()
                # No Guardar
                elif result == "not save":
                    print("# No Guardar")
                    self.view_main_window.close()

                elif result == "cancel" or result == "exit":
                    print("# Cancelar")
                    return
            else:
                self.view_main_window.close()
        else:
            self.view_main_window.close()

    @Slot(list)
    def buttonStatusBar(self, ToolButton_mode):
        self.controller_page_draw.buttonStatusBar(ToolButton_mode)


    @Slot(list)
    def _printStatusBarCoor(self, coor_list):
        """ imprime en la barra de estado las coordenadas del mouse al moverse por el QGraphics.

        Args:
            coor_list(list): coordenada X y Y
        """
        x = round(coor_list[0],4)
        y = round(coor_list[1],4)
        self.view_main_window.setTextStatusCoor(x=x,y=y)
      



    @Slot(list)
    def hideShowDraw(self,data):       

        action = data[0]
        value = data[1]
   

        if action == "ShowHideConsole":
            self.view_main_window.modeConsoleDraw(value)


    @Slot(list)
    def projectChanges(self, data):
        name_project = data[0]
        state_project_changes = data[1]
        self.view_main_window.projectChanges(name_project, state_project_changes)
     
    @Slot()
    def saveData(self):        
        if self.current_project:
            print("Save [{}]".format(self.current_project.saveDataDb()))
            self.__showMessageCommand("_save")

    @Slot(str)    
    def saveAsData(self, new_path_file):        
        if self.current_project:
            print("SaveAs [{}]".format(self.current_project.projectSaveAs(new_path_file)))
            self.openProject(new_path_file)
            self.__showMessageCommand("_saveAs")

    def settingDraw(self,setting_update):
        self.controller_page_draw.settingDraw(setting_update)



    def __save_auto(self):
        """Método para la señal de tiempo para auto guardado,
        debe estar activada la función para guardar """

        if self.autosave and self.current_project:
            self.now = datetime.now() 
            self.hour = self.now.hour
            self.minute = self.now.minute
            self.second = self.now.second
            self.microsecond = self.now.microsecond
        

            print("autoSave [{}]: {}:{}:{},{}".format(
                self.current_project.saveDataDb(),
                self.hour, self.minute ,self.second, self.microsecond ))
            self.__showMessageCommand("_autoSave")

        else:
            print("Not auto save")


 ###############################################################################
	# ::::::::::::::::::::        MÉTODOS PARA MENSAJES        ::::::::::::::::::::
	###############################################################################
    @Slot(str)
    def __showMessageCommand(self, command):
        return
        """ imprime en la consola un comando.

        Args:
            command(str): comando  

        """
        self.frame_draw.msnConsole("Command",command)
    
    @Slot(str)
    def __showMessageCritical(self, message):
        return
        """ imprime en la barra de estado un mensaje critico.

        Args:
            message(str): Mensaje critico 
        """
        self.ui.statusbar.setStyleSheet("color: #F94646;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Error",message)
    
    @Slot(str)
    def __showMessageSatisfactory(self, message):
        return
        """ imprime en la barra de estado un mensaje satisfactorio.

        Args:
            message(str): Mensaje satisfactorio 
        """
        self.ui.statusbar.setStyleSheet("color: #36C9C6;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Running",message)
    
    @Slot(str)
    def __showMessageInformative(self, message):
        return
        """ imprime en la barra de estado un mensaje informativo.

        Args:
            message(str): Mensaje informativo 
        """
        self.ui.statusbar.setStyleSheet("color: #DDDDDD;") 
        self.ui.statusbar.showMessage(message,6000)
        self.frame_draw.msnConsole("Information",message)

    @Slot()
    def changeTheme(self):
        self.controller_page_setting.changeTheme()
