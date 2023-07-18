from PySide6.QtCore import (Slot)
from clases.Vista.view_WidgetDrawMenuExecute import ViewWidgetDrawMenuExecute
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardMaterialPoint import ControllerCardMaterialPoint


class ControllerMenuExecute():

    def __init__(self) -> None:

        self.view_menu_execute = ViewWidgetDrawMenuExecute()
        self.model_current_project = None
        self.list_controller_card=[]

        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_execute.signal_execute.connect(self.executeAnalysis)
        self.view_menu_execute.signal_state_view_boundary.connect(self.stateViewBoundary)

    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project

    def configDrawMenuExecute(self):

        self.view_menu_execute.removeItemsLists()

        points_material = []
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        for id_PM in models_points_materials:
            name_PM = models_points_materials[id_PM].getName()
            color_PM = models_points_materials[id_PM].getColor()
            points_material.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
        self.view_menu_execute.addItemsListsMaterialPoint(points_material)
       



        boundaries = []
        models_boundaries = self.model_current_project.getModelsBoundaries()
        for id_boundary in models_boundaries:
            name_boundary = models_boundaries[id_boundary].getName()
            boundaries.append({'name': name_boundary, 'id': id_boundary})

        self.view_menu_execute.addItemsListsBoundaries(boundaries)
       
    def getView(self):
        return self.view_menu_execute
    
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::
    @Slot()
    def executeAnalysis(self):
        list_point_material = self.view_menu_execute.getListExecutePointMaterial()
        list_boundaries = self.view_menu_execute.getListExecuteBoundaries()
        if not list_point_material:
            self.view_menu_execute.msnAlertDefault("Selecciona los puntos materiales")
            return
        elif not list_boundaries:
            self.view_menu_execute.msnAlertDefault("Selecciona los contornos")
            return
        print("ANALISIS")

    @Slot(dict)
    def stateViewBoundary(self, data):
        self.model_current_project.stateViewBoundary(data)
        
        

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
