from PySide6.QtCore import (Slot, Signal, QObject)
from PySide6.QtWidgets import (QMessageBox, QProgressBar, QLabel, QVBoxLayout)
from PySide6.QtCore import (Qt, Signal)
from views.draw.view_WidgetDrawMenuExecute import ViewWidgetDrawMenuExecute
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMaterialPoint import ControllerCardMaterialPoint
from utils.class_ui_dialog_loanding import DialogLoanding
from utils import class_ui_dialog_msg

from models.model_execute_analysis import ModelExcuteAnalysisMPM
from models.model_analysis_config import AnalysisConfig

import os
import numpy as np
import math
import time as tm
import  matplotlib.pyplot as plt
import json



from motorMPM.mesh import create_uniform, contour_fixe, setup_MP,search_MP
from motorMPM.mesh import traction_forces,boundary_particles
from motorMPM.explicit2 import deltatime,deltatime2, particles_to_nodes, BC_Dirichlet_momentum
from motorMPM.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel, nodes_to_particle_stress
from motorMPM.graphics import graphic_button,graphic_button2,graphic_button3,graphic_button4, graphic_video2,graphic_gif

from ui.ui_dialog_loanding import Ui_DialogLoanding

from PySide6.QtWidgets import QApplication, QVBoxLayout, QLabel, QProgressBar, QDialog, QPushButton
import time

class AnalysisProgressDialog(QDialog, Ui_DialogLoanding):
    signal_cancelled = Signal()
    signal_paused = Signal()
    signal_resumed = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        
        self.setWindowTitle("Ejecutando análisis")
        self.cancel_button.clicked.connect(self.cancelAnalysis)
        self.pause_button.clicked.connect(self.pauseAnalysis)
        self.acept_button.clicked.connect(self.acceptAnalysis)


        self.cancelled = False
        self.paused = False
        self.accepted = False
        self.configUI()
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def configUI(self):
        self.acept_button.setEnabled(False)
        self.acept_button.setVisible(False)
        
    def acceptAnalysis(self):
        self.accepted = True
 
        
    def cancelAnalysis(self):
        self.cancelled = True
        self.close()
    
    def pauseAnalysis(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.setText("Reanudar")
            self.signal_paused.emit()
            
        else:
            self.pause_button.setText("Pausar")
            self.signal_resumed.emit()
            
    def setQuestion(self, question):
        self.question_label.setText(question)

    def setStatus(self, error=False, status =""):    
        self.status_label.setText(status)
        if error:
            self.status_label.setStyleSheet("color: #f36c42")
        else:
            '''
            QLabel#status_label{
                    font: 300 10pt "Ubuntu";
                    color: #DDDDDD;
                margin-left: 10px;
                }
            '''
            self.status_label.setStyleSheet("color: #DDDDDD")
    
    def setTimer(self, time):
        self.timer_label.setText(time)

    def setProgress(self, value):
        self.progress_bar.setValue(value)
        
    def setViewError(self):
        self.acept_button.setEnabled(True)
        self.acept_button.setVisible(True)
        
        self.pause_button.setEnabled(False)
        self.pause_button.setVisible(False)
        
        


class ControllerMenuExecute(QObject):

    signal_enable_results =Signal()
    signal_update_menu_result = Signal()
    
    def __init__(self) -> None:
        super().__init__()
        self.view_menu_execute = ViewWidgetDrawMenuExecute()
        self.model_current_project = None
        self.model_result = None
        self.list_controller_card=[]
        self.dtime = None
        self.tiempo = None
        self.dtimegraphic = None
        self.tiempographic = None
        self.__dataTime = None


        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_execute.signal_execute.connect(self.executeAnalysis)
        self.view_menu_execute.signal_state_view_boundary.connect(self.stateViewBoundary)
        self.view_menu_execute.signal_update_time.connect(self.updateTime)
        
        self.view_menu_execute.signal_change_state_analysis_ce.connect(self.changeStateAnalysisCE)
        self.view_menu_execute.Signal_update_dincre.connect(self.updateDincre)
        # Signal_update_dincreGrav ya no se conecta: dincreGrav se calcula automaticamente
        self.view_menu_execute.signal_update_no_incre.connect(self.updateNoIncre)
        
    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project
        self.model_result = model_current_project.getModelResult()
        
    def activateMenu(self):
        self.view_menu_execute.activateMenu()

    def configDrawMenuExecute(self):
        self.setListPointsMaterialView()
        self.setListBoundariesView()
        if self.model_result.getDataTimes() :        
            numbre_courant = self.model_result.getDataTimes()['NUMEROCOURANT']
            time_analysis = self.model_result.getDataTimes()['TIEMPOANALISIS']
            
            fps = self.model_result.getDataTimes()['FPS']      
            self.view_menu_execute.setNumberCourant(numbre_courant)
            self.view_menu_execute.setTimeAnalysis(time_analysis)
            self.view_menu_execute.setFps(fps)
                       
   
        execute_analysis_CE = self.model_current_project.getExecuteAnalysisCE()
        dincre = self.model_current_project.getDincre()
        noincre = self.model_current_project.getNoIncre()
        # Calcular dincreGrav automaticamente
        dincreGrav = 1.0 / noincre if noincre > 0 else 1.0
        
        self.view_menu_execute.setCheckBoxExecuteAnalysisCE(execute_analysis_CE)
        self.view_menu_execute.setDincre(dincre)
        self.view_menu_execute.setDincreGrav(dincreGrav)
        self.view_menu_execute.setNoIncre(noincre)
        # Guardar en BD el valor calculado
        self.model_current_project.updateConfigAnalysis(dincreGrav=dincreGrav)
        

        self.updateTime()
    
        
    
    def setListPointsMaterialView(self):
        self.view_menu_execute.removeItemsListsMaterialPoint()
        
        result_point_materia = self.model_result.getPointMaterials()
        ids_result_point_materia = list(result_point_materia.keys())
        
        points_material_from = []
        points_material_to = []
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        
        for id_PM in models_points_materials:
            name_PM = models_points_materials[id_PM].getName()
            property_PM = models_points_materials[id_PM].getProperty()
            color_PM = property_PM.getColor()
            if id_PM in ids_result_point_materia:
                points_material_to.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
            else:
                points_material_from.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
                
        self.view_menu_execute.addItemsListsMaterialPointFrom(points_material_from)
        self.view_menu_execute.addItemsListsMaterialPointTo(points_material_to)
        
        
    
    def setListBoundariesView(self):
        self.view_menu_execute.removeItemsListsBoundaries()
        
        result_boundaries = self.model_result.getBoundarys()
        ids_result_boundaries = list(result_boundaries.keys())
        
        boundaries_from = []
        boundaries_to = []
        models_boundaries = self.model_current_project.getModelsBoundaries()
        
        for id_boundary in models_boundaries:
            name_boundary = models_boundaries[id_boundary].getName()
            if id_boundary in ids_result_boundaries:
                boundaries_to.append({'name': name_boundary, 'id': id_boundary})
            else:
                boundaries_from.append({'name': name_boundary, 'id': id_boundary})
                
        self.view_menu_execute.addItemsListsBoundariesFrom(boundaries_from)
        self.view_menu_execute.addItemsListsBoundariesTo(boundaries_to)
        

    
    def newItemsListsMaterialPoint(self, id_material_point):
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        name_PM = models_points_materials[id_material_point].getName()
        color_PM = models_points_materials[id_material_point].getColor()
        self.view_menu_execute.addItemsListsMaterialPointFrom([{'name': name_PM, 'id': id_material_point, 'color': color_PM}])
    
    def newItemsListsBoundaries(self, id_boundary):
        models_boundaries = self.model_current_project.getModelsBoundaries()
        name_boundary = models_boundaries[id_boundary].getName()
        self.view_menu_execute.addItemsListsBoundariesFrom([{'name': name_boundary, 'id': id_boundary}])    
    
    
    
    def getView(self):
        return self.view_menu_execute
    
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::
    @Slot()
    def executeAnalysis(self):
        analysis_dialog = AnalysisProgressDialog(self.view_menu_execute)
        analysis_dialog.show()
        analysis_dialog.rejected.connect(analysis_dialog.cancelAnalysis)
        
        list_point_material = self.view_menu_execute.getListExecutePointMaterial()
        list_boundaries = self.view_menu_execute.getListExecuteBoundaries()
                
        dtime = self.dtime
        tiempo = self.tiempo
        steps_time = self.__dataTime['analysis_steps']
        dtimegraphic = self.dtimegraphic
        tiempographic = self.tiempographic
        steps_timegraphic = self.__dataTime['graphic_steps']
        
        # verificar que los puntos materiales y los contornos esten seleccionados
        if not list_point_material:
            #loading_popup.close()
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los puntos materiales")
            return
        
        elif not list_boundaries:
            #loading_popup.close()
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los contornos")
            return
        
        elif dtime is None or tiempo is None or steps_time is None or dtimegraphic is None or tiempographic is None or steps_timegraphic is None:
            self.view_menu_execute.msnAlertDefault(True,"Evalué los parámetros de tiempo")
            return
        
        # verificar que los puntos materiales esten en la malla de fondo
        model_mesh_back = self.model_current_project.model_mesh_back
        
        
        nodes = model_mesh_back.getNodes()
        cells = model_mesh_back.getElements()        

        for id_mp in list_point_material:            
            model_mp = self.model_current_project.getModelsPointsMaterials()[id_mp]
            points = model_mp.getPoints()
            cells_by_point = self.findCellForPoints(material_points=points, 
                                                    elements=cells,
                                                    nodes=nodes)
            
            if len(cells_by_point) != len(points):
                self.view_menu_execute.msnAlertDefault(True," pm fuera la malla de fondo '{}'".format(model_mp.getName()))
                analysis_dialog.close()
                return
        
        
        #ejectuar el análisis

        
        # Construir AnalysisConfig según tipo de análisis
        type_analysis_ce = self.model_current_project.getExecuteAnalysisCE()
        gravity = self.model_current_project.getGravity()
        dampfac = self.model_current_project.getDampfac()
        
        if type_analysis_ce:
            nincre = self.model_current_project.getNoIncre()
            dincre_val = self.model_current_project.getDincre()
            # dincreGrav se calcula automaticamente
            dincreGrav_val = 1.0 / nincre if nincre > 0 else 1.0
            analysis_config = AnalysisConfig.from_legacy_ce(
                dataTime=self.__dataTime,
                gravity=gravity,
                dampfac=dampfac,
                nincre=nincre,
                dincre=dincre_val,
                dincreGrav=dincreGrav_val
            )
        else:
            analysis_config = AnalysisConfig.from_legacy_viga(
                dataTime=self.__dataTime,
                gravity=gravity,
                dampfac=dampfac
            )
        
        print(f"[Controller] AnalysisConfig: {analysis_config}")
        
        analysis_mpm = ModelExcuteAnalysisMPM(
                                    analysis_dialog= analysis_dialog,
                                    model_current_project=self.model_current_project,
                                    model_result=self.model_result,
                                    dataTime=self.__dataTime,
                                    list_boundaries=list_boundaries,
                                    list_point_material=list_point_material, 
                                    dt_time=dtime,
                                    list_time=tiempo,
                                    steps_time=steps_time,
                                    dt_graphic= dtimegraphic,
                                    list_time_graphic=tiempographic,
                                    steps_time_graphic=steps_timegraphic,
                                    analysis_config=analysis_config)
        
        # Ejecutar con el método unificado
        state_ok = analysis_mpm.run()
        
        if state_ok:
            self.signal_enable_results.emit()
            analysis_dialog.setStatus("Análisis completado")
            analysis_dialog.close() 
            self.view_menu_execute.msnAlertDefault(False,"Análisis ejecutado")
            self.signal_update_menu_result.emit()
            print("[OK→] Análisis finalizado")
            
        else:
            analysis_dialog.setStatus("Análisis cancelado")
            analysis_dialog.close()
            self.view_menu_execute.msnAlertDefault(True,"Análisis cancelado")
            print("[NOT→] Análisis cancelado")
            
            


    @Slot(dict)
    def stateViewBoundary(self, data):
        self.model_current_project.stateViewBoundary(data)


    @Slot(bool)
    def changeStateAnalysisCE(self, state):
        self.model_current_project.updateConfigAnalysis(execute_analysis_CE=state)
        self.configDrawMenuExecute()
        
    @Slot()
    def updateDincre(self):
        dincre = self.view_menu_execute.getDincre()
        self.model_current_project.updateConfigAnalysis(dincre=dincre)

    @Slot()
    def updateNoIncre(self):
        noincre = self.view_menu_execute.getNoIncre()
        self.model_current_project.updateConfigAnalysis(noincre=noincre)
        # Auto-calcular dincreGrav = 1/nincre
        dincreGrav = 1.0 / noincre if noincre > 0 else 1.0
        self.view_menu_execute.setDincreGrav(dincreGrav)
        self.model_current_project.updateConfigAnalysis(dincreGrav=dincreGrav)
        
    @Slot()
    def updateTime(self):   
 
        list_mp = self.view_menu_execute.getListExecutePointMaterial()        
        len_list_mp = len(list_mp)
        if len_list_mp == 0:
            self.view_menu_execute.resetDataTime()
            return
        
        models_properties = self.model_current_project.models_properties
        models_material_point = self.model_current_project.models_material_point        
        
        result_dtime = {}
        for id_mp in list_mp:            
            model_mp = models_material_point[id_mp]
            model_propertie = model_mp.getProperty()
            data = model_propertie.getData()
            id = list(data.keys())[0]
            modulus_elasticity = data[id]["MODULOELASTICIDAD"]
            poisson_ratio = data[id]["RELACIONPOISSON"]
            density = data[id]["DENSIDAD"]
            
            number_courant = self.view_menu_execute.getNumberCourant()
            model_mesh_black = self.model_current_project.model_mesh_back
            ele_size = model_mesh_black.getSizeElement()

            density = density / 1000 # kg/m3 to Mg/m3            
            dtime, velocity_cp = deltatime(Ep = modulus_elasticity,
                            nu = poisson_ratio, 
                            rhop = density,
                            ele_size = ele_size,
                            factor = number_courant)            
            result_dtime[id_mp] = {'dtime': dtime, 'velocity_cp': velocity_cp, 'id_property': id}
            
            
        # min dtime
        min_dtime = min(result_dtime, key=lambda k: result_dtime[k]['dtime'])
        dtime = result_dtime[min_dtime]['dtime']
        velocity_cp = result_dtime[min_dtime]['velocity_cp']   
        id_property = result_dtime[min_dtime]['id_property']     
        name_property = models_properties[id_property].getName()
            
            
        time_ini = self.view_menu_execute.getTimeAnalysis()
        time = math.ceil(time_ini / dtime) * dtime    
        tiempo = np.arange(0, time, dtime)    #genera el rango de 0 a tiempo - dtime con paso dtime  
        tiempo = np.append(tiempo, time)    # se agregó el tiempo final

        fps = self.view_menu_execute.getFps()        
        
        if dtime < 1/fps:
            ndt = math.floor(1/fps/dtime)
            dtimegraphic = ndt*dtime
        else:
            dtimegraphic = dtime     
        tiempographic = np.arange(0, time, dtimegraphic)
        tiempographic = np.append(tiempographic, time)    # se agregó el tiempo final
      

        step_time = len(tiempo)-1
        step_timegraphic = len(tiempographic)-1
      
        self.view_menu_execute.setResultRTimes(
                                            name_property,
                                            velocity_cp,
                                            dtime,
                                            step_time,
                                            dtimegraphic,
                                            step_timegraphic)
        

        self.dtime = dtime
        self.tiempo = tiempo
        self.dtimegraphic = dtimegraphic
        self.tiempographic = tiempographic
        
        
        self.__dataTime = {'id_property': id_property,
                        'courant_number': number_courant,
                            'analysis_time': time_ini,                            
                            'fps': fps,
                            'dt_analysis': dtime,
                            'dt_graphic': dtimegraphic,
                            'analysis_steps': step_time,
                            'graphic_steps': step_timegraphic,
                            'speed_cp': velocity_cp}
        return     
    


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################



    def findCellForPoints(self, material_points, elements, nodes) -> dict:
        """Encuentra la celda a la que pertenece cada punto.
        Descripcion detallada de la función:  
        Encuentra la celda a la que pertenece cada punto, para lo cual se 
        recorre cada punto y se compara con las coordenadas de cada celda.
        
        Args:
            material_points (list): Lista de puntos materiales.
            elements (list): Lista de elementos  de la malla de fondo.
            nodes (list): Lista de nodos de la malla de fondo.
        Returns:
            dict: Diccionario con el punto y la celda a la que pertenece.
        """

              
        print("esto se puede optimizar no buscando primero en los vencinos hacia afura, sin tener que rrecorrer todos los elementos de la malla de fondo, solo los que estan cerca del punto material.")
        print("creo que esto se peude aplicar tambien en la busqueda de los puntos en el analisis, salbo que s eaga con gunciones d eforma o algo asi que sea mas directo")
        result = {}
        for point in material_points:
            ''' result: POINT#1'''
            ''' punto data:  {
                'COORDINATES': [1.25, 11.25],
                'VOLUME': 6.250000000000009, 
                'VELOCITY': {'X': 0.0, 'Y': 0.0},
                'FORCE': {'X': 0.0, 'Y': 0.0}} '''
            for i, element in enumerate(elements):
                ''' element: ELEMENT#1'''
                ''' elemento data:  ['NODE#1', 'NODE#2', 'NODE#13', 'NODE#12'] '''
                
                '''   esto es de otra version 
                x_values = [nodes[idx-1][0] for idx in element]
                y_values = [nodes[idx-1][1] for idx in element]
                min_x = min(x_values)
                max_x = max(x_values)
                min_y = min(y_values)
                max_y = max(y_values)
               
                '''
                min_x = 0
                min_y = 0
                
                max_x = max(
                    nodes[elements[element][0]]['COORDINATES'][0],
                    nodes[elements[element][1]]['COORDINATES'][0],
                    nodes[elements[element][2]]['COORDINATES'][0],
                    nodes[elements[element][3]]['COORDINATES'][0]
                )
                
                max_y = max(
                    nodes[elements[element][0]]['COORDINATES'][1],
                    nodes[elements[element][1]]['COORDINATES'][1],
                    nodes[elements[element][2]]['COORDINATES'][1],
                    nodes[elements[element][3]]['COORDINATES'][1]
                )
                

                x = material_points[point]['COORDINATES'][0]
                y = material_points[point]['COORDINATES'][1]
                if min_x <=  x <= max_x and min_y <= y <= max_y:
                    result.update({point: element})
                    break
                
        return result


    def analysisViga(self,analysis_dialog, list_boundaries, list_point_material, 
                     dt_time, list_time ,steps_time,
                     dt_graphic, list_time_graphic, steps_time_graphic):
        
        t0 = tm.time()	
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'tiempo inicial: {t0}')
                
        
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::: malla fondo ::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # las coordendas de la malla    ::  cor
        # los indices de cada elemento  ::  inci
        # el tamaño de cada elemento    ::  ele_size
        # el nuemro de elementos en x   ::  nelex
        model_mesh_black = self.model_current_project.model_mesh_black
        points = model_mesh_black.getPoints()
        Quadrilaterals = model_mesh_black.getQuadrilaterals()
        ele_size = model_mesh_black.getSizeElement()
        dx_size = model_mesh_black.getSizeDx()
        dy_size = model_mesh_black.getSizeDy()

        #variables
        cor = np.asarray(points)
        inci = np.asarray(Quadrilaterals)
        ele_size = cor[1][0] - cor[0][0]
        nelex = np.asarray(int(dx_size/ele_size))
        

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: restriccion de movimiento ::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # indices de los nodos con restriccion de movimiento en direccion x  ::  fixed_nodesX
        # indices de los nodos con restriccion de movimiento en direccion y :: fixed_nodesY
        fixed_nodesX=[]
        fixed_nodesY=[]
        models_boundary = self.model_current_project.models_boundary
        list_ids_boundaries =[]
        for boundary in list_boundaries:
            list_ids_boundaries.append(boundary['id'])
        for id_model_boundary in models_boundary:
            if id_model_boundary in list_ids_boundaries:
                model_boundary = models_boundary[id_model_boundary]
                points = model_boundary.getPoints()
                nodes = model_boundary.getNodes()
                restriction_x = model_boundary.getRestrictionX()
                restriction_y = model_boundary.getRestrictionY()

                if restriction_x:
                    for node in nodes:
                        fixed_nodesX.append(node)

                if restriction_y:
                    for node in nodes:
                        fixed_nodesY.append(node)

        #variables
        fixed_nodesX = np.asarray(list(set(fixed_nodesX)))
        fixed_nodesY = np.asarray(list(set(fixed_nodesY)))


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #:::::::::::::::: incializar puntos :::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # nuemro total de particulas                        ::  nmp
        # elementos donde esta cada punto material      ::  mp_elem
        # los elementos que tienen puntos materiales    :: active_elem 
        # coordenadas de los puntos materiales          ::  xp
        #    NOTA xp: en MPM-UN orginal la lista tiene otro orden 
        #             inf-izq, inf-der, sup-izq, sup-der 
        #             en este programa
        #             sup-izq, inf-izq, inf-der,  sup-der 
        #             Tambien revisar por que se esta asignado points,
        #             pero si son varios materiales no agrega todos
        #             sino el ultimo material point


        models_material_point = self.model_current_project.models_material_point
        list_ids_point_material =[]
        for material_point in list_point_material:
            list_ids_point_material.append(material_point['id'])

        mp_elem=[]
        for id_model_material_point in models_material_point:
            if id_model_material_point in list_ids_point_material:                
                model_material_point = models_material_point[id_model_material_point]
                points = model_material_point.getPoints()
                volumes = model_material_point.getVolumes()
                property = model_material_point.getProperty()
                cells = inci
                nodes = cor
                cells_by_point = self.findCellForPoints(points=points,
                                       cells=cells,
                                       nodes=nodes)
                    
                for cell in cells_by_point:
                    mp_elem.append(cell)
                    
        list_mp_elem=[]
        for i in list(mp_elem):
            list_mp_elem.append([i])
        
        #variables
        mp_elem = np.asarray(list_mp_elem)    
        xp = np.asarray(points)
        active_elem = np.unique(mp_elem[:, 0])
        nmp = len(mp_elem)
        

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particlas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    
        # modulo de elasticidad KPa     :: E
        # Coeficiente de poisson        :: nu
        # Cohesion KPa                  :: C'
        # Angulo de friccion            :: Phi
        # Angulo de dilatancia          :: psi
        #    NOTA property: revisar por que se esta asignado property,
        #             pero si son varios materiales no agrega todos
        #             sino el ultimo property
        
        id,name,modulus_elasticity,poisson_ratio,cohesion,friction_angle, density, angle_dilatancy = property.getData()
        Prop=np.zeros((nmp, 6))
        Prop[:,0] = modulus_elasticity               
        Prop[:,1] = poisson_ratio           
        Prop[:,2] =  cohesion             
        Prop[:,3] = friction_angle / 180*math.pi     
        Prop[:,4] = angle_dilatancy / 180*math.pi
        density = density / 1000
        
        
               

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: incializar materiales ::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    

        # vector de volumenes                               ::  Vp
        # vector de volumenes iniciales                     ::  Vp0
        #   NOTA Vp0: igual al anterioro
        # Mg/m3 vector de densisdades de las particulas     ::  rhop
        #   NOTA rhop: esto depenede de la densidad, deneria ser un
        #              parametro de material y no es el mismo para
        #              todas las particulas si tengo varios materiales 
        # vector de masas                                   ::  Mp
        #   NOTA Mp: igual al anterioro

        Vp =  np.asarray(volumes)
        Vp0 = np.asarray(volumes)      
        rhop = density * np.ones(nmp) 
        Mp = np.multiply(rhop, Vp) 


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particulas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄ 
        #    Matriz gradiente de deformacion                :: Fp
        #    Matriz de esfuerzos                            :: sig
        #    Matriz de deformaciones elasticas              :: epse
        #    Matriz de deformaciones plasticas              :: epsp
        #    Matriz de velocidades                          :: vp
        #    Matriz de fuerzas de cuerpo                    :: bp
        #    Matriz de fuerzas de traccion en la frontera   :: tp


        gravity = self.model_current_project.getGravity()
        dampfac = self.model_current_project.getDampfac()

        Fp = np.ones((nmp, 4))
        Fp[:,1:3] = 0
        sig = np.zeros((nmp, 4))
        epse = np.zeros((nmp, 3))
        epsp = np.zeros((nmp, 3))
        #inicalizar con valor de velicidad vp = 0.1
        #vp = np.zeros((nmp, 2))
        velocity_cp_x = 0
        velocity_cp_y = 0
        vp = np.ones((nmp, 2)) * np.array([velocity_cp_x, velocity_cp_y])
        
        bp=np.zeros((nmp, 2))
        #bp[:,1]=-gravity
        tp=np.zeros((nmp, 2))



        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::  particulas en la frontera del material  ::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # listado de las particulas                                                 :: bound_ptcl
        #       NOTA bound_ptcl: ojo con el orden estan en zigzag dentro del elemento
        #                         y de izq a der y de inferior a superior
        # listado que indica si las particulas estan en la frontera [1] o no [0]    :: bound_val

        """             boundary_particles
        Funcion que devuelve un array con las particulas ubicadas
        en la frontera, solo valido para la distribucion inicial
        rectangular, ojo por que esto deberia ser las particulas 
        que envuelven el material, o los materiales no lo se, y 
        en el caso de talud irregular no funciona.
        Tambien tener en cuenta que bound_ptcl y bound_val, parecierta
        estar ordenados pero en la lista de coordenanas de los puntos [xp]
        creo que estan en orden diferente al MPM-UN original, este esta
        ordenado en zigzag dentro del elemento  y de izq a der y de
        inferior a superior """
        bound_ptcl, bound_val = boundary_particles(xp)


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  Tiempo :::::::::::::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        """Crea listas que contiene los puntos y cada punto tiene una lista de los resultados en cada dtime"""
        #       :: corX
        #       :: corY
        #       :: sigxx
        #       :: sigyy
        #       :: sigxy
        #       :: epsxx
        #       :: epsyy
        #       :: epsxy
        '''
        corX = np.empty((nmp, len(list_time_graphic)))
        corY = np.empty((nmp, len(list_time_graphic)))     
        sigxx = np.empty((nmp, len(list_time_graphic)))
        sigyy = np.empty((nmp, len(list_time_graphic)))
        sigxy = np.empty((nmp, len(list_time_graphic)))
        epsxx = np.empty((nmp, len(list_time_graphic)))
        epsyy = np.empty((nmp, len(list_time_graphic)))
        epsxy = np.empty((nmp, len(list_time_graphic)))
        ''' 
        corX = np.zeros((nmp, len(list_time_graphic)))
        corY = np.zeros((nmp, len(list_time_graphic)))     
        sigxx = np.zeros((nmp, len(list_time_graphic)))
        sigyy = np.zeros((nmp, len(list_time_graphic)))
        sigxy = np.zeros((nmp, len(list_time_graphic)))
        epsxx = np.zeros((nmp, len(list_time_graphic)))
        epsyy = np.zeros((nmp, len(list_time_graphic)))
        epsxy = np.zeros((nmp, len(list_time_graphic)))
        velx = np.zeros((nmp, len(list_time_graphic)))
        vely = np.zeros((nmp, len(list_time_graphic)))
        
   

        corX[:,0], corY[:,0] = xp[:,0], xp[:,1]
        sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2]
        epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2]
        velx[:,0], vely[:,0] = vp[:,0], vp[:,1]
        



        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  Tiempo :::::::::::::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # Timepo de analisis de entrada                                         :: time_ini
        #       NOTA time: debe ser entrada de usuario
        # delta de tiempo redondeado con un solo decimal diferente de cero      :: dtime
        # el nuevo iimepo de analisis ajustado                                  :: time
        # Lista de tiempos segun timepo maximo y dtime                          :: tiempo
        # fotogramas por segundo                                                :: fps
        #       NOTA fps: no se si esto sea entrada del usuario 
        # delta de tiempo para graficar                                         :: dtimegraphic
        # Lista de tiempos para graficar segun timepo maximo y dtimegraphic     :: tiempographic

      
        
       

        new_list_time_graphic = list_time_graphic.copy()
        new_list_time = list_time.copy()
        current_index_graphic = 0


        # se usa list_time.size-1 para que no analice en el ultimo paso de tiempo
        #ya que los analisis de tiempo i dan resultados en tiempo i+1
        
        for index in range(list_time.size-1):
            
       
            current_time = list_time[index]
            current_time_graphic = list_time_graphic[current_index_graphic]


            ########################################################################
            #              Si se pausa o se cancela el análisis       
            ########################################################################                
                
            # si se cierra el dialogo
            if analysis_dialog.cancelled:
                analysis_dialog.close()
                return False
            
            # si se pausa en el dialogo
            if analysis_dialog.paused:
                analysis_dialog.setStatus(False, f"Ejecutando paso del análisis:\n→ {index:.0f} de {steps_time} pasos.\n\nAnálisis pausado")
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()  # Mantener la ventana actualizada
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                #analysis_dialog.setStatus(False, "Reanudando análisis...") 
            
            
            ########################################################################
            #              Si el material se encuentra fuera de la malla            
            #                         se detiene el análisis 
            ########################################################################
            # 1 => Buscamos en que elementos estan los MP
            mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)           
            try:
                active_nodes = np.unique(inci[active_elem-1, :])
            except Exception as e:
                
                print("---------------------//-------------------------")
                print("Error: ", e)
                print("Error en el tiempo: ", current_time, " paso: ", index)
                print("Tamaño de inci:", inci.shape)
                print("Índice a acceder:", active_elem)
                print("---------------------//-------------------------")
                
                #tiempo = tiempo[:t]
                # Abre un dialogo de error y pregunta si se desea finalizar el análisis
                text_error = f"Error en el tiempo: {current_time} "
                text_error = f"Paso:[{index} de {steps_time}]\n"
                text_error += f"El material se encuentra fuera de la malla\nEl análisis se detendrá en este punto.\n"
                analysis_dialog.setStatus(True,text_error)
                text_question = f"¿Quieres finalizar el análisis hasta este punto\n"
                text_question += f"y guardar los resultados?"
                analysis_dialog.setQuestion(text_question)
                analysis_dialog.pauseAnalysis()
                analysis_dialog.setViewError()
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()  # Mantener la ventana actualizada
                    # Si se cancela el análisis
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                    # Si se acepta el análisis
                    if analysis_dialog.accepted:
                        analysis_dialog.close()

                        # quitamos las filas que no se han llenado                       
                        new_list_time = new_list_time[:index]
                        position_max = current_index_graphic
                        new_list_time_graphic = new_list_time_graphic[:position_max]
                        corX = corX[:, :position_max] # antes era position_max+1
                        corY = corY[:, :position_max]
                        sigxx = sigxx[:, :position_max]
                        sigyy = sigyy[:, :position_max]
                        sigxy = sigxy[:, :position_max]
                        epsxx = epsxx[:, :position_max]
                        epsyy = epsyy[:, :position_max]
                        epsxy = epsxy[:, :position_max]
                        velx = velx[:, :position_max]
                        vely = vely[:, :position_max]
                        break              
                break
                
                
                
               
            ########################################################################
            #              Si todo esta bien se continua con el análisis
            #                      analisis de las particulas                   
            ########################################################################        
            analysis_dialog.setProgress(100*index/steps_time)
            analysis_dialog.setStatus(False, f"Ejecutando paso del análisis:\n→ {index:.0f} de {steps_time} pasos.")
            QApplication.processEvents()          
     
            #new_list_time.append(list_time[index])
            
            # 3 => Transferir la informacion de las particulas a lo nodos de la malla
            grid = inci, cor, active_elem, active_nodes, mp_elem
            particle = xp, vp, Vp, Mp, sig, bp, tp
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
            nforce = niforce + neforce
            
                   
            
            # 4 => Aplicar condiciones de frontera
            ndamping = dampfac * (np.multiply(np.absolute(nforce),np.sign(nmomentum)))
            nforce = nforce + ndamping
            nmomentum += nforce*dt_time
            nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX,fixed_nodesY, nmomentum, nforce,  niforce, neforce)
            
            
            # 5 => Calcula la velocidad y posicion de las particulas, transfiriendo de los nodos a las particulas
            nquantities = nmass, nmomentum, nforce
            particle= xp, vp, Vp, Mp, sig, shfnp
            xp, vp, nvel=nodes_to_particle_vel(grid, particle, nquantities, dt_time)
            
            nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY,nvel)
            
            # 6 => Calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
            particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
            Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dt_time, 0)

            # Guardar datos para graficar current_time_graphic+1 para guarde desde el segundo tiempo
            # ya que el primero es la condicion inicial en ceros
            if abs(current_time - current_time_graphic) < 1e-13: 
                corX[:,current_index_graphic + 1],corY[:,current_index_graphic + 1]= xp[:,0],xp[:,1]
                sigxx[:,current_index_graphic + 1],sigyy[:,current_index_graphic + 1],sigxy[:,current_index_graphic + 1]=sig[:,0],sig[:,1],sig[:,2]
                epsxx[:,current_index_graphic + 1],epsyy[:,current_index_graphic + 1],epsxy[:,current_index_graphic + 1]=epse[:,0],epse[:,1],epse[:,2]
                velx[:,current_index_graphic + 1], vely[:,current_index_graphic + 1] = vp[:,0], vp[:,1]
                current_index_graphic += 1

        ########################################################################
        #                           analisis finalizado
        ########################################################################        
        self.model_result.clearResult()        
        self.model_result.updateResultDataBase(
            gravity=gravity,
            dampfac=dampfac,
        )
        
        
        for point_material in list_point_material:        
            id_material_point = point_material['id']
            model_material_point = models_material_point[id_material_point]
            model_property = model_material_point.getProperty()


            self.model_result.addResultProperty(
                id_property = model_property.getId(),
                name = model_property.getName(),
                modulus_elasticity = model_property.getModulusElasticity(),
                poisson_ratio = model_property.getPoissonRatio(),
                cohesion = model_property.getCohesion(),
                friction_angle = model_property.getFrictionAngle(),
                density = model_property.getDensity(),
                angle_dilatancy = model_property.getAngleDilatancy()
            )
            
            self.model_result.addResultPointMaterial(
                id_MP = id_material_point,
                name = model_material_point.getName(),
                color = model_material_point.getColor(),
                points = model_material_point.getPoints(),
                id_property = model_property.getId()
            )
        
        for boundary in list_boundaries:
            id_boundary = boundary['id']
            name = boundary['name']
            model_boundary = models_boundary[id_boundary]
            points = model_boundary.getPoints()
            nodes = model_boundary.getNodes()
            restriction_x = model_boundary.getRestrictionX()
            restriction_y = model_boundary.getRestrictionY()
            self.model_result.addResultBoundary(
                id_boundary = id_boundary,
                name = name,
                points = points,
                nodes = nodes,
                restrictionX = restriction_x,
                restrictionY = restriction_y
            )
            
        
        self.model_result.updateResultDataTimes(
            id_material=self.__dataTime['id_property'],
            courant_number=self.__dataTime['courant_number'],
            analysis_time=self.__dataTime['analysis_time'],
            fps=self.__dataTime['fps'],
            dt_analysis=self.__dataTime['dt_analysis'],
            dt_graphic=self.__dataTime['dt_graphic'],
            analysis_steps=self.__dataTime['analysis_steps'],
            graphic_steps=self.__dataTime['graphic_steps'],
            speed_cp=self.__dataTime['speed_cp'],
            time_reached=new_list_time[-1]                
        )
        #    time_reached=new_list_time[-1]                
        
        self.model_result.updateResultMeshBack(
            size_dx=dx_size,
            size_dy=dy_size,
            size_element=ele_size,
            color=model_mesh_black.getColorStyle(),
            points=model_mesh_black.getPoints(),
            quadrilaterals=Quadrilaterals,
            points_boundary_top=model_mesh_black.getBoundaryPoints()[0],
            points_boundary_bottom=model_mesh_black.getBoundaryPoints()[1],
            points_boundary_left=model_mesh_black.getBoundaryPoints()[2],
            points_boundary_right=model_mesh_black.getBoundaryPoints()[3],
            nodes_boundary_top=model_mesh_black.getBoundaryNodes()[0],
            nodes_boundary_bottom=model_mesh_black.getBoundaryNodes()[1],
            nodes_boundary_left=model_mesh_black.getBoundaryNodes()[2],
            nodes_boundary_right=model_mesh_black.getBoundaryNodes()[3]  
        )
    
    
        self.model_result.updateResultTimes(
            analysis_times=new_list_time.tolist()
        )
        self.model_result.updateResultTimeGraphic(
            graphic_time=new_list_time_graphic.tolist()
        )
        self.model_result.updateResultMin(
            corx=corX.min(),
            cory=corY.min(),
            sigxx=sigxx.min(),
            sigyy=sigyy.min(),
            sigxy=sigxy.min(),
            epsxx=epsxx.min(),
            epsyy=epsyy.min(),
            epsxy=epsxy.min(),
            velx=velx.min(),
            vely=vely.min()
        )
        self.model_result.updateResultMax(
            corx=corX.max(),
            cory=corY.max(),
            sigxx=sigxx.max(),
            sigyy=sigyy.max(),
            sigxy=sigxy.max(),
            epsxx=epsxx.max(),
            epsyy=epsyy.max(),
            epsxy=epsxy.max(),
            velx=velx.max(),
            vely=vely.max()
            
        )
                
        corX_l = corX.tolist(); corY_l = corY.tolist()
        sigxx_l = sigxx.tolist(); sigyy_l = sigyy.tolist(); sigxy_l = sigxy.tolist()
        epsxx_l = epsxx.tolist(); epsyy_l = epsyy.tolist(); epsxy_l = epsxy.tolist()
        velx_l = velx.tolist(); vely_l = vely.tolist()

        for node in range(len(corX)):
            self.model_result.addResultNode(
                id_result_node=node+1,
                corx=corX_l[node],
                cory=corY_l[node],
                sigxx=sigxx_l[node],
                sigyy=sigyy_l[node],
                sigxy=sigxy_l[node],
                epsxx=epsxx_l[node],
                epsyy=epsyy_l[node],
                epsxy=epsxy_l[node],
                velx=velx_l[node],
                vely=vely_l[node]
            )

        self.model_result.updateResult()
        self.signal_enable_results.emit()

        tf =tm.time()
        print("tiempo", tf- t0)
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")

        return True

    def analysisCapacidadPoratnte(self,analysis_dialog, list_boundaries, list_point_material, 
                     dt_time, list_time ,steps_time,
                     dt_graphic, list_time_graphic, steps_time_graphic):
        
        t0 = tm.time()	
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'tiempo inicial: {t0}')
                
        
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::: malla fondo ::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # las coordendas de la malla    ::  cor
        # los indices de cada elemento  ::  inci
        # el tamaño de cada elemento    ::  ele_size
        # el nuemro de elementos en x   ::  nelex
        model_mesh_black = self.model_current_project.model_mesh_black
        points = model_mesh_black.getPoints()
        Quadrilaterals = model_mesh_black.getQuadrilaterals()
        ele_size = model_mesh_black.getSizeElement()
        dx_size = model_mesh_black.getSizeDx()
        dy_size = model_mesh_black.getSizeDy()

        #variables
        cor = np.asarray(points)
        inci = np.asarray(Quadrilaterals)
        nelex = np.asarray(int(dx_size/ele_size))
        

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: restriccion de movimiento ::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # indices de los nodos con restriccion de movimiento en direccion x  ::  fixed_nodesX
        # indices de los nodos con restriccion de movimiento en direccion y :: fixed_nodesY
        fixed_nodesX=[]
        fixed_nodesY=[]
        models_boundary = self.model_current_project.models_boundary
        list_ids_boundaries =[]
        for boundary in list_boundaries:
            list_ids_boundaries.append(boundary['id'])
        for id_model_boundary in models_boundary:
            if id_model_boundary in list_ids_boundaries:
                model_boundary = models_boundary[id_model_boundary]
                points = model_boundary.getPoints()
                nodes = model_boundary.getNodes()
                restriction_x = model_boundary.getRestrictionX()
                restriction_y = model_boundary.getRestrictionY()

                if restriction_x:
                    for node in nodes:
                        fixed_nodesX.append(node)

                if restriction_y:
                    for node in nodes:
                        fixed_nodesY.append(node)

        #variables
        fixed_nodesX = np.asarray(list(set(fixed_nodesX)))
        fixed_nodesY = np.asarray(list(set(fixed_nodesY)))


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #:::::::::::::::: incializar puntos :::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # nuemro total de particulas                        ::  nmp
        # elementos donde esta cada punto material      ::  mp_elem
        # los elementos que tienen puntos materiales    :: active_elem 
        # coordenadas de los puntos materiales          ::  xp
        #    NOTA xp: en MPM-UN orginal la lista tiene otro orden 
        #             inf-izq, inf-der, sup-izq, sup-der 
        #             en este programa
        #             sup-izq, inf-izq, inf-der,  sup-der 
        #             Tambien revisar por que se esta asignado points,
        #             pero si son varios materiales no agrega todos
        #             sino el ultimo material point


        models_material_point = self.model_current_project.models_material_point
        list_ids_point_material =[]
        for material_point in list_point_material:
            list_ids_point_material.append(material_point['id'])

        mp_elem=[]
        for id_model_material_point in models_material_point:
            if id_model_material_point in list_ids_point_material:                
                model_material_point = models_material_point[id_model_material_point]
                points = model_material_point.getPoints()
                volumes = model_material_point.getVolumes()
                property = model_material_point.getProperty()
                cells = inci
                nodes = cor
                cells_by_point = self.findCellForPoints(points=points,
                                       cells=cells,
                                       nodes=nodes)
                    
                for cell in cells_by_point:
                    mp_elem.append(cell)
                    
        list_mp_elem=[]
        for i in list(mp_elem):
            list_mp_elem.append([i])
        
        #variables
        mp_elem = np.asarray(list_mp_elem)    
        xp = np.asarray(points)
        active_elem = np.unique(mp_elem[:, 0])
        nmp = len(mp_elem)
        

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particlas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    
        # modulo de elasticidad KPa     :: E
        # Coeficiente de poisson        :: nu
        # Cohesion KPa                  :: C'
        # Angulo de friccion            :: Phi
        # Angulo de dilatancia          :: psi
        
        id,name,modulus_elasticity,poisson_ratio,cohesion,friction_angle, density, angle_dilatancy = property.getData()
        Prop=np.zeros((nmp, 6))
        Prop[:,0] = modulus_elasticity               
        Prop[:,1] = poisson_ratio           
        Prop[:,2] =  cohesion             
        Prop[:,3] = friction_angle / 180*math.pi     
        Prop[:,4] = angle_dilatancy / 180*math.pi
        density = density / 1000
        
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: incializar materiales ::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    

        # vector de volumenes                               ::  Vp
        # vector de volumenes iniciales                     ::  Vp0
        # Mg/m3 vector de densisdades de las particulas     ::  rhop 
        # vector de masas                                   ::  Mp

        Vp =  np.asarray(volumes)
        Vp0 = np.asarray(volumes)      
        rhop = density * np.ones(nmp) 
        Mp = np.multiply(rhop, Vp) 


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particulas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄ 
        #    Matriz gradiente de deformacion                :: Fp
        #    Matriz de esfuerzos                            :: sig
        #    Matriz de deformaciones elasticas              :: epse
        #    Matriz de deformaciones plasticas              :: epsp
        #    Matriz de velocidades                          :: vp
        #    Matriz de fuerzas de cuerpo                    :: bp
        #    Matriz de fuerzas de traccion en la frontera   :: tp


        gravity = self.model_current_project.getGravity()
        dampfac = self.model_current_project.getDampfac()

        Fp = np.ones((nmp, 4))
        Fp[:,1:3] = 0
        sig = np.zeros((nmp, 4))
        epse = np.zeros((nmp, 3))
        epsp = np.zeros((nmp, 3))
        
        
        #inicalizar con valor de velicidad vp = 0.1
        #vp = np.zeros((nmp, 2))
        velocity_cp_x = 0
        velocity_cp_y = 0
        vp = np.ones((nmp, 2)) * np.array([velocity_cp_x, velocity_cp_y])
        
        bp=np.zeros((nmp, 2))
        #bp[:,1]=-gravity
        tp=np.zeros((nmp, 2))



        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::  particulas en la frontera del material  ::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # listado de las particulas                                                 :: bound_ptcl
        #       NOTA bound_ptcl: ojo con el orden estan en zigzag dentro del elemento
        #                         y de izq a der y de inferior a superior
        # listado que indica si las particulas estan en la frontera [1] o no [0]    :: bound_val

        """             boundary_particles
        Funcion que devuelve un array con las particulas ubicadas
        en la frontera, solo valido para la distribucion inicial
        rectangular, ojo por que esto deberia ser las particulas 
        que envuelven el material, o los materiales no lo se, y 
        en el caso de talud irregular no funciona.
        Tambien tener en cuenta que bound_ptcl y bound_val, parecierta
        estar ordenados pero en la lista de coordenanas de los puntos [xp]
        creo que estan en orden diferente al MPM-UN original, este esta
        ordenado en zigzag dentro del elemento  y de izq a der y de
        inferior a superior """
        bound_ptcl, bound_val = boundary_particles(xp)


        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  Tiempo :::::::::::::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        """Crea listas que contiene los puntos y cada punto tiene una lista de los resultados en cada dtime"""
        #       :: corX
        #       :: corY
        #       :: sigxx
        #       :: sigyy
        #       :: sigxy
        #       :: epsxx
        #       :: epsyy
        #       :: epsxy
        '''
        corX = np.empty((nmp, len(list_time_graphic)))
        corY = np.empty((nmp, len(list_time_graphic)))     
        sigxx = np.empty((nmp, len(list_time_graphic)))
        sigyy = np.empty((nmp, len(list_time_graphic)))
        sigxy = np.empty((nmp, len(list_time_graphic)))
        epsxx = np.empty((nmp, len(list_time_graphic)))
        epsyy = np.empty((nmp, len(list_time_graphic)))
        epsxy = np.empty((nmp, len(list_time_graphic)))
        ''' 
        corX = np.zeros((nmp, len(list_time_graphic)))
        corY = np.zeros((nmp, len(list_time_graphic)))     
        sigxx = np.zeros((nmp, len(list_time_graphic)))
        sigyy = np.zeros((nmp, len(list_time_graphic)))
        sigxy = np.zeros((nmp, len(list_time_graphic)))
        epsxx = np.zeros((nmp, len(list_time_graphic)))
        epsyy = np.zeros((nmp, len(list_time_graphic)))
        epsxy = np.zeros((nmp, len(list_time_graphic)))
        velx = np.zeros((nmp, len(list_time_graphic)))
        vely = np.zeros((nmp, len(list_time_graphic)))
        
   

        corX[:,0], corY[:,0] = xp[:,0], xp[:,1]
        sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2]
        epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2]
        velx[:,0], vely[:,0] = vp[:,0], vp[:,1]
        



        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  Tiempo :::::::::::::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # Timepo de analisis de entrada                                         :: time_ini
        #       NOTA time: debe ser entrada de usuario
        # delta de tiempo redondeado con un solo decimal diferente de cero      :: dtime
        # el nuevo iimepo de analisis ajustado                                  :: time
        # Lista de tiempos segun timepo maximo y dtime                          :: tiempo
        # fotogramas por segundo                                                :: fps
        #       NOTA fps: no se si esto sea entrada del usuario 
        # delta de tiempo para graficar                                         :: dtimegraphic
        # Lista de tiempos para graficar segun timepo maximo y dtimegraphic     :: tiempographic

      
        
       

        new_list_time_graphic = list_time_graphic.copy()
        new_list_time = list_time.copy()
        current_index_graphic = 0


        # se usa list_time.size-1 para que no analice en el ultimo paso de tiempo
        #ya que los analisis de tiempo i dan resultados en tiempo i+1
        
        for index in range(list_time.size-1):
            
       
            current_time = list_time[index]
            current_time_graphic = list_time_graphic[current_index_graphic]


            ########################################################################
            #              Si se pausa o se cancela el análisis       
            ########################################################################                
                
            # si se cierra el dialogo
            if analysis_dialog.cancelled:
                analysis_dialog.close()
                return False
            
            # si se pausa en el dialogo
            if analysis_dialog.paused:
                analysis_dialog.setStatus(False, f"Ejecutando paso del análisis:\n→ {index:.0f} de {steps_time} pasos.\n\nAnálisis pausado")
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()  # Mantener la ventana actualizada
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                #analysis_dialog.setStatus(False, "Reanudando análisis...") 
            
            
            ########################################################################
            #              Si el material se encuentra fuera de la malla            
            #                         se detiene el análisis 
            ########################################################################
            # 1 => Buscamos en que elementos estan los MP
            mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)           
            try:
                active_nodes = np.unique(inci[active_elem-1, :])
            except Exception as e:
                
                print("---------------------//-------------------------")
                print("Error: ", e)
                print("Error en el tiempo: ", current_time, " paso: ", index)
                print("Tamaño de inci:", inci.shape)
                print("Índice a acceder:", active_elem)
                print("---------------------//-------------------------")
                
                #tiempo = tiempo[:t]
                # Abre un dialogo de error y pregunta si se desea finalizar el análisis
                text_error = f"Error en el tiempo: {current_time} "
                text_error = f"Paso:[{index} de {steps_time}]\n"
                text_error += f"El material se encuentra fuera de la malla\nEl análisis se detendrá en este punto.\n"
                analysis_dialog.setStatus(True,text_error)
                text_question = f"¿Quieres finalizar el análisis hasta este punto\n"
                text_question += f"y guardar los resultados?"
                analysis_dialog.setQuestion(text_question)
                analysis_dialog.pauseAnalysis()
                analysis_dialog.setViewError()
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()  # Mantener la ventana actualizada
                    # Si se cancela el análisis
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                    # Si se acepta el análisis
                    if analysis_dialog.accepted:
                        analysis_dialog.close()

                        # quitamos las filas que no se han llenado                       
                        new_list_time = new_list_time[:index]
                        position_max = current_index_graphic
                        new_list_time_graphic = new_list_time_graphic[:position_max]
                        corX = corX[:, :position_max] # antes era position_max+1
                        corY = corY[:, :position_max]
                        sigxx = sigxx[:, :position_max]
                        sigyy = sigyy[:, :position_max]
                        sigxy = sigxy[:, :position_max]
                        epsxx = epsxx[:, :position_max]
                        epsyy = epsyy[:, :position_max]
                        epsxy = epsxy[:, :position_max]
                        velx = velx[:, :position_max]
                        vely = vely[:, :position_max]
                        break              
                break
                
                
                
               
            ########################################################################
            #              Si todo esta bien se continua con el análisis
            #                      analisis de las particulas                   
            ########################################################################        
            analysis_dialog.setProgress(100*index/steps_time)
            analysis_dialog.setStatus(False, f"Ejecutando paso del análisis:\n→ {index:.0f} de {steps_time} pasos.")
            QApplication.processEvents()          
     
            #new_list_time.append(list_time[index])
            
            # 3 => Transferir la informacion de las particulas a lo nodos de la malla
            grid = inci, cor, active_elem, active_nodes, mp_elem
            particle = xp, vp, Vp, Mp, sig, bp, tp
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
            nforce = niforce + neforce
            
                   
            
            # 4 => Aplicar condiciones de frontera
            ndamping = dampfac * (np.multiply(np.absolute(nforce),np.sign(nmomentum)))
            nforce = nforce + ndamping
            nmomentum += nforce*dt_time
            nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX,fixed_nodesY, nmomentum, nforce,  niforce, neforce)
            
            
            # 5 => Calcula la velocidad y posicion de las particulas, transfiriendo de los nodos a las particulas
            nquantities = nmass, nmomentum, nforce
            particle= xp, vp, Vp, Mp, sig, shfnp
            xp, vp, nvel=nodes_to_particle_vel(grid, particle, nquantities, dt_time)
            
            nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY,nvel)
            
            # 6 => Calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
            particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
            Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dt_time, 0)

            # Guardar datos para graficar current_time_graphic+1 para guarde desde el segundo tiempo
            # ya que el primero es la condicion inicial en ceros
            if abs(current_time - current_time_graphic) < 1e-13: 
                corX[:,current_index_graphic + 1],corY[:,current_index_graphic + 1]= xp[:,0],xp[:,1]
                sigxx[:,current_index_graphic + 1],sigyy[:,current_index_graphic + 1],sigxy[:,current_index_graphic + 1]=sig[:,0],sig[:,1],sig[:,2]
                epsxx[:,current_index_graphic + 1],epsyy[:,current_index_graphic + 1],epsxy[:,current_index_graphic + 1]=epse[:,0],epse[:,1],epse[:,2]
                velx[:,current_index_graphic + 1], vely[:,current_index_graphic + 1] = vp[:,0], vp[:,1]
                current_index_graphic += 1

        ########################################################################
        #                           analisis finalizado
        ########################################################################        
        self.model_result.clearResult()        
        self.model_result.updateResultDataBase(
            gravity=gravity,
            dampfac=dampfac,
        )
        
        
        for point_material in list_point_material:        
            id_material_point = point_material['id']
            model_material_point = models_material_point[id_material_point]
            model_property = model_material_point.getProperty()


            self.model_result.addResultProperty(
                id_property = model_property.getId(),
                name = model_property.getName(),
                modulus_elasticity = model_property.getModulusElasticity(),
                poisson_ratio = model_property.getPoissonRatio(),
                cohesion = model_property.getCohesion(),
                friction_angle = model_property.getFrictionAngle(),
                density = model_property.getDensity(),
                angle_dilatancy = model_property.getAngleDilatancy()
            )
            
            self.model_result.addResultPointMaterial(
                id_MP = id_material_point,
                name = model_material_point.getName(),
                color = model_material_point.getColor(),
                points = model_material_point.getPoints(),
                id_property = model_property.getId()
            )
        
        for boundary in list_boundaries:
            id_boundary = boundary['id']
            name = boundary['name']
            model_boundary = models_boundary[id_boundary]
            points = model_boundary.getPoints()
            nodes = model_boundary.getNodes()
            restriction_x = model_boundary.getRestrictionX()
            restriction_y = model_boundary.getRestrictionY()
            self.model_result.addResultBoundary(
                id_boundary = id_boundary,
                name = name,
                points = points,
                nodes = nodes,
                restrictionX = restriction_x,
                restrictionY = restriction_y
            )
            
        
        self.model_result.updateResultDataTimes(
            id_material=self.__dataTime['id_property'],
            courant_number=self.__dataTime['courant_number'],
            analysis_time=self.__dataTime['analysis_time'],
            fps=self.__dataTime['fps'],
            dt_analysis=self.__dataTime['dt_analysis'],
            dt_graphic=self.__dataTime['dt_graphic'],
            analysis_steps=self.__dataTime['analysis_steps'],
            graphic_steps=self.__dataTime['graphic_steps'],
            speed_cp=self.__dataTime['speed_cp'],
            time_reached=new_list_time[-1]                
        )
        #    time_reached=new_list_time[-1]                
        
        self.model_result.updateResultMeshBack(
            size_dx=dx_size,
            size_dy=dy_size,
            size_element=ele_size,
            color=model_mesh_black.getColorStyle(),
            points=model_mesh_black.getPoints(),
            quadrilaterals=Quadrilaterals,
            points_boundary_top=model_mesh_black.getBoundaryPoints()[0],
            points_boundary_bottom=model_mesh_black.getBoundaryPoints()[1],
            points_boundary_left=model_mesh_black.getBoundaryPoints()[2],
            points_boundary_right=model_mesh_black.getBoundaryPoints()[3],
            nodes_boundary_top=model_mesh_black.getBoundaryNodes()[0],
            nodes_boundary_bottom=model_mesh_black.getBoundaryNodes()[1],
            nodes_boundary_left=model_mesh_black.getBoundaryNodes()[2],
            nodes_boundary_right=model_mesh_black.getBoundaryNodes()[3]  
        )
    
    
        self.model_result.updateResultTimes(
            analysis_times=new_list_time.tolist()
        )
        self.model_result.updateResultTimeGraphic(
            graphic_time=new_list_time_graphic.tolist()
        )
        self.model_result.updateResultMin(
            corx=corX.min(),
            cory=corY.min(),
            sigxx=sigxx.min(),
            sigyy=sigyy.min(),
            sigxy=sigxy.min(),
            epsxx=epsxx.min(),
            epsyy=epsyy.min(),
            epsxy=epsxy.min(),
            velx=velx.min(),
            vely=vely.min()
        )
        self.model_result.updateResultMax(
            corx=corX.max(),
            cory=corY.max(),
            sigxx=sigxx.max(),
            sigyy=sigyy.max(),
            sigxy=sigxy.max(),
            epsxx=epsxx.max(),
            epsyy=epsyy.max(),
            epsxy=epsxy.max(),
            velx=velx.max(),
            vely=vely.max()
            
        )
                
        corX_l = corX.tolist(); corY_l = corY.tolist()
        sigxx_l = sigxx.tolist(); sigyy_l = sigyy.tolist(); sigxy_l = sigxy.tolist()
        epsxx_l = epsxx.tolist(); epsyy_l = epsyy.tolist(); epsxy_l = epsxy.tolist()
        velx_l = velx.tolist(); vely_l = vely.tolist()

        for node in range(len(corX)):
            self.model_result.addResultNode(
                id_result_node=node+1,
                corx=corX_l[node],
                cory=corY_l[node],
                sigxx=sigxx_l[node],
                sigyy=sigyy_l[node],
                sigxy=sigxy_l[node],
                epsxx=epsxx_l[node],
                epsyy=epsyy_l[node],
                epsxy=epsxy_l[node],
                velx=velx_l[node],
                vely=vely_l[node]
            )

        self.model_result.updateResult()
        self.signal_enable_results.emit()

        tf =tm.time()
        print("tiempo", tf- t0)
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")

        return True
