from PySide6.QtCore import ( Slot)
from clases.Vista.view_PageSetting import ViewPageSetting
from clases.Modelo.model_SettingApp import ModelSettingApp
#from clases.Controlador.controller_MainWindow import ControllerMainWindow

 
class ControllerPageSetting():

    def __init__(self, controller_main) -> None:
        self.controller_main = controller_main

        #Crea la vista ViewPageHome
        self.view_page_setting = ViewPageSetting()
        self.model_setting_app = ModelSettingApp()

        self.view_page_setting.signal_update_setting.connect(self.updateSetting)  


        self.view_page_setting.iniSetting(self.getSetting())


    def getView(self):
        return self.view_page_setting

    def getSetting(self):
        return self.model_setting_app.getSetting()
    

    @Slot(dict)
    def updateSetting(self,setting_update):

         
        self.model_setting_app.updateSetting(setting_update)

        if setting_update["setting"] == "style_view_scene" or setting_update["setting"] == "crosshair_size"  or setting_update["setting"] == "pick_box_size"  or setting_update["setting"] == "grid_adaptative" or setting_update["setting"] == "grid_spacing" or setting_update["setting"] == "snap_grid_adaptative" or setting_update["setting"] == "snap_grid_spacing":
            self.controller_main.settingDraw(setting_update)    

        if setting_update["setting"] == "check_auto_save":
            autosave = setting_update["setting_data"][2]
            self.controller_main.autosave = autosave

        if setting_update["setting"] == "interval_auto_save":
            index = setting_update["setting_data"][2]
            if index == 0:
                self.mili_second_save = 5 * 60 * 1000
            elif index == 1:
                self.mili_second_save = 15 * 60 * 1000
            elif index == 2:
                self.mili_second_save = 30 * 60 * 1000
            elif index == 3:
                self.mili_second_save = 60 * 60 * 1000

            self.controller_main.timer_save.setInterval(self.mili_second_save)

    def changeTheme(self):
        self.view_page_setting.changeTheme()



