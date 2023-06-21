""" Este módulo contiene la vista Ui_FormHome, para incluirla en la vista main window"""


import os
from PySide6.QtCore import (Signal)
from PySide6.QtWidgets import ( QFrame,QSizePolicy, QFileDialog)
from ui import ui_frame_setting

class ViewPageSetting(QFrame, ui_frame_setting.Ui_FormSetting):
    
    """Esta clase crea la vista  QFrame setting para agregarlo a main window. 

    Attributes:
            controller(ControllerMainWindow): Controlador de la vista ViewMainWindow

    Method:
        : r

    """
    signal_update_setting = Signal(dict)



    def __init__(self ):
        super(ViewPageSetting, self).__init__()
        self.setupUi(self)

        # Configura la UI
        self.configUi()

        # Establece los eventos de la UI
        self.initEventUi()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def configUi(self):
        """ Configura la interface de usuario (ui) """ 
        self.horizontalSlider_1.setRange(0,100)
        self.spinBox_1.setRange(0,100)
        self.horizontalSlider_2.setRange(5,50)

    
    def initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::    EVENTOS  SETTING    ::::::::::::::::::::    
        self.horizontalSlider_1.valueChanged.connect(self.updateSetting)
        self.spinBox_1.valueChanged.connect(self.updateSetting)
        self.horizontalSlider_2.valueChanged.connect(self.updateSetting)
        self.comboBox_3.currentIndexChanged.connect(self.updateSetting)

        self.doubleSpinBox_grid_spacing.valueChanged.connect(self.updateSetting)
        self.checkBox_grid_adaptative.stateChanged.connect(self.updateSetting)
        self.doubleSpinBox_snap_grid_spacing.valueChanged.connect(self.updateSetting)
        self.checkBox_snap_grid_adaptative.stateChanged.connect(self.updateSetting)

        self.comboBox_intervalAutoSave.currentIndexChanged.connect(self.updateSetting)
        self.checkBox_autoSave.stateChanged.connect(self.updateSetting)

    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS DE EVENTOS SETTING     ::::::::::::::::::::
	###############################################################################
    def updateSetting(self,value=0,updateAll=False):
        """Método para los eventos de los widget de setting. Se obtiene el widget
         que activo la señal y se redirecciona al widget correspondiente"""
        


        widgetSelected = self.sender()
        nameWidget=""
        if widgetSelected != None:        
            nameWidget = widgetSelected.objectName()

        
	    # ::::::::::::::::::::    SETTING Pantalla de dibujo    ::::::::::::::::::::

        # Cruz del puntero
        if nameWidget==self.horizontalSlider_1.objectName() or updateAll:
            self.spinBox_1.setValue(self.horizontalSlider_1.value())            
        
        if nameWidget==self.spinBox_1.objectName() or updateAll:
            value_crosshair_size = self.spinBox_1.value()
            self.horizontalSlider_1.setValue(value_crosshair_size)
            data_dict = {"setting":"crosshair_size",
                         "setting_data":[0,"TamanoCruzPuntero", value_crosshair_size]}
            self.signal_update_setting.emit(data_dict)
        
        #Caja de puntero
        if nameWidget==self.horizontalSlider_2.objectName() or updateAll:            
            value_pick_box_size = (self.horizontalSlider_2.value())
            value_Margin =18 * (1-((value_pick_box_size-5)/45))           
            self.frame_4.setContentsMargins(value_Margin, value_Margin, value_Margin, value_Margin)
            data_dict = {"setting":"pick_box_size",
                         "setting_data":[0,"TamanoCajaPuntero", value_pick_box_size]}
            self.signal_update_setting.emit(data_dict)
            
        #Estilo de vista
        if nameWidget==self.comboBox_3.objectName() or updateAll:
            index_style_view_scene = self.comboBox_3.currentIndex()
            data_dict = {"setting":"style_view_scene",
                         "setting_data":[0,"EstiloVista", index_style_view_scene]}
            self.signal_update_setting.emit(data_dict)

        #Grilla
        if nameWidget==self.checkBox_grid_adaptative.objectName() or updateAll:
            check_grid_adaptative = self.checkBox_grid_adaptative.isChecked() 
            grid_spacing = self.doubleSpinBox_grid_spacing.value()     
                  
            if check_grid_adaptative:
                self.doubleSpinBox_grid_spacing.setEnabled(False)
            else:
                self.doubleSpinBox_grid_spacing.setEnabled(True)
            data_dict = {"setting":"grid_adaptative",
                         "setting_data":[0,"GrillaAdaptativa", check_grid_adaptative]}
            self.signal_update_setting.emit(data_dict)

            data_dict = {"setting":"grid_spacing",
                         "setting_data":[0,"EspacioGrilla", grid_spacing]}
            self.signal_update_setting.emit(data_dict)

        if nameWidget==self.doubleSpinBox_grid_spacing.objectName() or updateAll:
            grid_spacing = self.doubleSpinBox_grid_spacing.value()    
            data_dict = {"setting":"grid_spacing",
                         "setting_data":[0,"EspacioGrilla", grid_spacing]}
            self.signal_update_setting.emit(data_dict)

        #Snap
        if nameWidget==self.checkBox_snap_grid_adaptative.objectName() or updateAll:
            check_snap_grid_adaptative = self.checkBox_snap_grid_adaptative.isChecked()
            snap_grid_spacing = self.doubleSpinBox_snap_grid_spacing.value() 

            if check_snap_grid_adaptative:
                self.doubleSpinBox_snap_grid_spacing.setEnabled(False)
            else:
                self.doubleSpinBox_snap_grid_spacing.setEnabled(True)

            data_dict = {"setting":"snap_grid_adaptative",
                         "setting_data":[0,"SnapGrillaAdaptativa", check_snap_grid_adaptative]}
            self.signal_update_setting.emit(data_dict)

            data_dict = {"setting":"snap_grid_spacing",
                         "setting_data":[0,"EspacioSnapGrilla", snap_grid_spacing]}
            self.signal_update_setting.emit(data_dict)


        if nameWidget==self.doubleSpinBox_snap_grid_spacing.objectName() or updateAll:
            snap_grid_spacing = self.doubleSpinBox_snap_grid_spacing.value() 
            data_dict = {"setting":"snap_grid_spacing",
                         "setting_data":[0,"EspacioSnapGrilla", snap_grid_spacing]}
            self.signal_update_setting.emit(data_dict)



        #Guardado automatico
        if nameWidget==self.checkBox_autoSave.objectName() or updateAll:
            check_auto_save = self.checkBox_autoSave.isChecked()            
            if check_auto_save:
                self.comboBox_intervalAutoSave.setEnabled(True)

            else:
                self.comboBox_intervalAutoSave.setEnabled(False)

            data_dict = {"setting":"check_auto_save",
                         "setting_data":[1,"GuardadoAutomatico", check_auto_save]}

            self.signal_update_setting.emit(data_dict)



        if nameWidget==self.comboBox_intervalAutoSave.objectName() or updateAll:
            index = self.comboBox_intervalAutoSave.currentIndex()  

            data_dict = {"setting":"interval_auto_save",
                         "setting_data":[1,"IntervaloAutoGuardado", index]}
            self.signal_update_setting.emit(data_dict)




    def iniSetting(self, setting):
        """Inicia las configuraciones de la app.

        Args:
            setting (list): Lista con las configuraciones.
        
        """

        # Setting Pantalla de dibujo
        TamanoCruzPuntero=(setting[0]["TamanoCruzPuntero"])
        self.horizontalSlider_1.setValue(TamanoCruzPuntero)   

        TamanoCajaPuntero=(setting[0]["TamanoCajaPuntero"])
        self.horizontalSlider_2.setValue(TamanoCajaPuntero)

        EstiloVista=(setting[0]["EstiloVista"])
        self.comboBox_3.setCurrentIndex(EstiloVista)

        GrillaAdaptativa=(setting[0]["GrillaAdaptativa"])
        self.checkBox_grid_adaptative.setChecked(GrillaAdaptativa) 

        EspacioGrilla=(setting[0]["EspacioGrilla"])
        self.doubleSpinBox_grid_spacing.setValue(EspacioGrilla)   

        SnapGrillaAdaptativa=(setting[0]["SnapGrillaAdaptativa"])
        self.checkBox_snap_grid_adaptative.setChecked(SnapGrillaAdaptativa)

        EspacioSnapGrilla=(setting[0]["EspacioSnapGrilla"])
        self.doubleSpinBox_snap_grid_spacing.setValue(EspacioSnapGrilla) 


        GuardadoAutomatico=(setting[1]["GuardadoAutomatico"])
        self.checkBox_autoSave.setChecked(GuardadoAutomatico)

        IntervaloAutoGuardado=(setting[1]["IntervaloAutoGuardado"])
        self.comboBox_intervalAutoSave.setCurrentIndex(IntervaloAutoGuardado)



        self.updateSetting(updateAll=True)
    
    def changeTheme(self):

        index_theme = self.comboBox_3.currentIndex()
        if index_theme ==2:
            self.comboBox_3.setCurrentIndex(0)
        else:
            self.comboBox_3.setCurrentIndex(index_theme+1)
 