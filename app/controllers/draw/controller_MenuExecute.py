from PySide6.QtCore import (Slot, Signal, QObject)
from PySide6.QtWidgets import (QMessageBox, QProgressBar, QLabel, QVBoxLayout)
from PySide6.QtCore import (Qt)
from views.draw.view_WidgetDrawMenuExecute import ViewWidgetDrawMenuExecute
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMaterialPoint import ControllerCardMaterialPoint
from utils.class_ui_dialog_loanding import DialogLoanding

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


class ControllerMenuExecute(QObject):

    signal_enable_results =Signal()
    def __init__(self) -> None:
        super().__init__()
        self.view_menu_execute = ViewWidgetDrawMenuExecute()
        self.model_current_project = None
        self.model_result = None
        self.list_controller_card=[]
        self.dtime = None
        self.tiempo = None
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
        
    def setCurrentProject(self, model_current_project:ModelProjectCurrent):  
        self.model_current_project = model_current_project
        self.model_result = model_current_project.getModelResult()
        
    def activateMenu(self):
        self.view_menu_execute.activateMenu()

    def configDrawMenuExecute(self):
        if self.model_result.getDataTimes() :        
            numbre_courant = self.model_result.getDataTimes()['NUMEROCOURANT']
            time_analysis = self.model_result.getDataTimes()['TIEMPOANALISIS']
            fps = self.model_result.getDataTimes()['FPS']      
            self.view_menu_execute.setNumberCourant(numbre_courant)
            self.view_menu_execute.setTimeAnalysis(time_analysis)
            self.view_menu_execute.setFps(fps)

        result_point_materia = self.model_result.getPointMaterials()
        ids_result_point_materia = list(result_point_materia.keys())
        
        result_boundaries = self.model_result.getBoundarys()
        ids_result_boundaries = list(result_boundaries.keys())        
        
        self.view_menu_execute.removeItemsLists()

        points_material_from = []
        points_material_to = []
        models_points_materials = self.model_current_project.getModelsPointsMaterials()
        
        for id_PM in models_points_materials:
            name_PM = models_points_materials[id_PM].getName()
            color_PM = models_points_materials[id_PM].getColor()
            if id_PM in ids_result_point_materia:
                points_material_to.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
            else:
                points_material_from.append({'name': name_PM, 'id': id_PM, 'color': color_PM})
            
        self.view_menu_execute.addItemsListsMaterialPointFrom(points_material_from)
        self.view_menu_execute.addItemsListsMaterialPointTo(points_material_to)
       
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
        self.updateTime()
    
    
    
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
        loading_popup = QMessageBox()
        loading_popup.setWindowTitle("Loading")

        # Configurar la barra de progreso
        progress_bar = QProgressBar()
        progress_bar.setRange(0, 0)  # Configurar la barra de progreso como indefinida
        progress_bar.setAlignment(Qt.AlignCenter)
        
        # Configurar el mensaje en el cuadro de diálogo
        message_label = QLabel("Realizando análisis, por favor espera...")
        message_label.setAlignment(Qt.AlignCenter)

        # Crear un layout vertical y agregar los elementos
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(progress_bar)

        # Establecer el layout en el cuadro de diálogo
        loading_popup.setLayout(layout)

        # Mostrar el cuadro de diálogo
        loading_popup.show()
        
        list_point_material = self.view_menu_execute.getListExecutePointMaterial()
        list_boundaries = self.view_menu_execute.getListExecuteBoundaries()
        
        
        dtime = self.dtime
        tiempo = self.tiempo
        tiempographic = self.tiempographic
        
        if dtime is None or tiempo is None or tiempographic is None:
            self.view_menu_execute.msnAlertDefault(True,"Evalué los parámetros de tiempo")
            return
        
        elif not list_point_material:
            loading_popup.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los puntos materiales")
            return
        
        elif not list_boundaries:
            loading_popup.close()
            self.view_menu_execute.msnAlertDefault(True,"Selecciona los contornos")
            return
        
        
        
        state_ok = self.analysisViga(list_boundaries=list_boundaries,
                                     list_point_material=list_point_material, 
                                     dtime=dtime,
                                     tiempo=tiempo,
                                     tiempographic=tiempographic)
        if state_ok:
            loading_popup.close()
            self.view_menu_execute.msnAlertDefault(False,"Análisis ejecutado")


    @Slot(dict)
    def stateViewBoundary(self, data):
        self.model_current_project.stateViewBoundary(data)



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
        for mp in list_mp:
            id_mp = mp['id']
            
            model_mp = models_material_point[id_mp]
            model_propertie = model_mp.getProperty()
            id,name,modulus_elasticity,poisson_ratio,cohesion,friction_angle, density, angle_dilatancy = model_propertie.getData()
            number_courant = self.view_menu_execute.getNumberCourant()
            model_mesh_black = self.model_current_project.model_mesh_black
            points = model_mesh_black.getPoints()
            cor = np.asarray(points)
            ele_size = cor[1][0] - cor[0][0]
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
        tiempo = np.arange(0, time+dtime, dtime)      

        fps = self.view_menu_execute.getFps()        
        
        if dtime < 1/fps:
            ndt = math.floor(1/fps/dtime)
            dtimegraphic = ndt*dtime
        else:
            dtimegraphic = dtime     
        tiempographic = np.arange(0, time+dtimegraphic, dtimegraphic)
                

           
        self.view_menu_execute.setResultRTimes(
                                            name_property,
                                            velocity_cp,
                                            dtime,
                                            len(tiempo),
                                            dtimegraphic,
                                            len(tiempographic))
        
        self.dtime = dtime
        self.tiempo = tiempo
        self.tiempographic = tiempographic
        
        self.__dataTime = {'id_property': id_property,
                        'courant_number': number_courant,
                            'analysis_time': time_ini,                            
                            'fps': fps,
                            'dt_analysis': dtime,
                            'dt_graphic': dtimegraphic,
                            'analysis_steps': len(tiempo),
                            'graphic_steps': len(tiempographic),
                            'speed_cp': velocity_cp}
        
        return     
    

        

        
        '''

            
            id,name,modulus_elasticity,poisson_ratio,cohesion,friction_angle, density, angle_dilatancy = model.getData()
            number_courant = self.view_menu_execute.getNumberCourant()
            model_mesh_black = self.model_current_project.model_mesh_black
            points = model_mesh_black.getPoints()
            cor = np.asarray(points)
            ele_size = cor[1][0] - cor[0][0]
            density = density / 1000 # kg/m3 to Mg/m3
            dtime, velocity_cp = deltatime(Ep = modulus_elasticity,
                                nu = poisson_ratio, 
                                rhop = density,
                                ele_size = ele_size,
                                factor = number_courant)
            time_ini = self.view_menu_execute.getTimeAnalysis()
            time = math.ceil(time_ini / dtime) * dtime
            tiempo = np.arange(0, time, dtime)
            fps = self.view_menu_execute.getFps()
            if dtime < 1/fps:
                ndt = math.floor(1/fps/dtime)
                dtimegraphic = ndt*dtime
            else:
                dtimegraphic = dtime
            tiempographic = np.arange(0, time, dtimegraphic)
            self.view_menu_execute.setResultRTimes(velocity_cp,
                                                   dtime,
                                                   len(tiempo),
                                                   dtimegraphic,
                                                   len(tiempographic))

            '''
        
        
          


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################



    def findCellForPoints(self, points, cells, nodes):
        result = []
        for point in points:
            for i, square in enumerate(cells):
                x_values = [nodes[idx-1][0] for idx in square]
                y_values = [nodes[idx-1][1] for idx in square]
                min_x = min(x_values)
                max_x = max(x_values)
                min_y = min(y_values)
                max_y = max(y_values)
                #print("i: ",i, " square: ", square,"  [{},{},{},{}]".format(min_x,max_x,min_y, max_y))

                
                if min_x <= point[0] <= max_x and min_y <= point[1] <= max_y:
                    result.append(i+1)
                    break
                
        return result


    def analysisViga(self,list_boundaries, list_point_material, dtime, tiempo , tiempographic):
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
        '''
        print("cor",cor)
        print("inci",inci)
        print("ele_size",ele_size)
        print("nelex",nelex)
        '''

        

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
        '''
        print("fixed_nodesX",fixed_nodesX)
        print("fixed_nodesY",fixed_nodesY)
        '''



        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #:::::::::::::::: incializar puntos :::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # numero de puntos por elemeto de malla         ::  nmpe
        #   NOTA nmpe: este valor se coloca en el codigo, pero no 
        #              deberia ser asi, no utilizar por que si los
        #              puntos estan desordenados como en una mllas
        #              trinagular
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
        mp_elem = np.asarray(list_mp_elem)    
        xp = np.asarray(points)
        active_elem = np.unique(mp_elem[:, 0])
        #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ REVISAR
        nmpe = 4
        '''
        print("nmpe",nmpe)
        print("mp_elem",mp_elem)
        print("active_ele1m",active_elem)
        print("xp",xp) 
        '''
 
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: incializar materiales ::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    
        # nuemro total de particulas                        ::  nmp
        # vector de volumenes                               ::  Vp
        #   NOTA Vp: esto depende del area que ocupa cada punto
        #            en el elemeto, pero si es malla trinagulas
        #             para puntos, puede que tenga areas muy
        #             diferentes 
        # vector de volumenes iniciales                     ::  Vp0
        #   NOTA Vp0: igual al anterioro
        # Mg/m3 vector de densisdades de las particulas     ::  rhop
        #   NOTA rhop: esto depenede de la densidad, deneria ser un
        #              parametro de material y no es el mismo para
        #              todas las particulas si tengo varios materiales 
        # vector de masas                                   ::  Mp
        #   NOTA Mp: igual al anterioro


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
       #vp = area_cuadrado /  numero de particulas por celda
        Vp = (ele_size**2) / nmpe*np.ones(nmp)      # [1. 1. 1.]
        Vp0 = (ele_size**2) / nmpe*np.ones(nmp)     # [1. 1. 1.]
        #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ REVISAR
        rhop = density * np.ones(nmp)                   # [2. 2. 2.] 
        Mp = np.multiply(rhop, Vp)                  # [2. 2. 2.]
        '''
        print ("Properties")
        print("modulus_elasticity: (kPa)",modulus_elasticity)
        print("poisson_ratio: (-)",poisson_ratio)
        print("cohesion: (kPa)",cohesion)
        print("friction_angle: (°)",friction_angle)
        print("density: (Mg/m3)",density)
        print("angle_dilatancy: (°)",angle_dilatancy)
        '''
        
        
        
        '''
        print("rhop",rhop)
        print("nmp",nmp)
        print("Vp",Vp)
        print("Vp0",Vp0)
        print("rhop",rhop)
        print("Mp",Mp)
        '''




        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particulas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄ 
        """ """   
        #     :: Fp
        #     :: sig
        #     :: epse
        #     :: epsp
        #     :: vp
        #     :: bp
        #     :: tp



        gravity = self.model_current_project.getGravity()

        Fp = np.ones((nmp, 4))
        Fp[:,1:3] = 0
        sig = np.zeros((nmp, 4))
        epse = np.zeros((nmp, 3))
        epsp = np.zeros((nmp, 3))

        vp = np.zeros((nmp, 2))
        bp=np.zeros((nmp, 2))
        bp[:,1]=-gravity
        tp=np.zeros((nmp, 2))
        '''
        print("Fp",Fp)
        print("sig",sig)
        print("epse",epse)
        print("epsp",epsp)
        print("vp",vp)
        print("bp",bp)
        print("tp",tp)

        '''


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
        '''
        print("bound_ptcl",bound_ptcl)
        print("bound_val", bound_val)
        '''
        


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
        #        :: 
        
        
        '''
        
        time_ini = time_analysis

        dtime = deltatime2(Ep = Prop[:,0],
                          nu = Prop[:,1], 
                          rhop = rhop,
                          ele_size = ele_size,
                          factor = 0.5)
        
        time = math.ceil(time_ini / dtime) * dtime
        print("-*-*-", time)
        tiempo = np.arange(0, time, dtime)



        fps = 120

        if dtime < 1/fps:
            ndt = math.floor(1/fps/dtime)
            dtimegraphic = ndt*dtime
        else:
            dtimegraphic = dtime 
    
        tiempographic = np.arange(0, time, dtimegraphic)
        
        print(len(tiempo),tiempo)
        print(len(tiempographic), tiempographic)
        
        '''
        
        
        
        
        
        
        '''
        print("time_ini",time_ini)
        print("dtime",dtime)
        print("time",time)
        print("tiempo",tiempo)
        print("fps",fps)
        print("dtimegraphic",dtimegraphic)
        print("tiempographic",tiempographic)
        '''






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



        corX = np.empty((nmp, len(tiempographic)+1))  
        corY = np.empty((nmp, len(tiempographic)+1))     
        sigxx = np.empty((nmp, len(tiempographic)+1))
        sigyy = np.empty((nmp, len(tiempographic)+1))
        sigxy = np.empty((nmp, len(tiempographic)+1))
        epsxx = np.empty((nmp, len(tiempographic)+1))
        epsyy = np.empty((nmp, len(tiempographic)+1))
        epsxy = np.empty((nmp, len(tiempographic)+1))

        #print("corX",corX)
        corX[:,0], corY[:,0] = xp[:,0], xp[:,1]
        sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2]
        epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2]
        
        '''
        print()
        print()
        print("corX",corX)
        '''

      
        dampfac = self.model_current_project.getDampfac()
        tgraphic = 0
        


        analysis_times = []
        graphic_times = [0]
        
        for t in range(len(tiempo)):

            mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)
            try:
                active_nodes = np.unique(inci[active_elem-1, :])
            except Exception as e:
                print("Error: ", e)
                print("Error en el tiempo: ", t)
                print("Tamaño de inci:", inci.shape)
                print("Índice a acceder:", active_elem)
                print("--------------------------")
                tiempo = tiempo[:t]
                #salir de la simulacion 
                break
                
                
                
            print("→ active_nodes. ",t)
            
            analysis_times.append(tiempo[t])
            
            
            

            grid = inci, cor, active_elem, active_nodes, mp_elem
            particle = xp, vp, Vp, Mp, sig, bp, tp
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
            nforce = niforce + neforce

            #↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓ REVISAR
            #dampfac = 1
            ndamping = dampfac * (np.multiply(np.absolute(nforce),np.sign(nmomentum)))
            nforce = nforce + ndamping
            nmomentum += nforce*dtime

            nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX,fixed_nodesY, nmomentum, nforce,  niforce, neforce)

            nquantities = nmass, nmomentum, nforce
            particle= xp, vp, Vp, Mp, sig, shfnp
            xp, vp, nvel=nodes_to_particle_vel(grid, particle, nquantities, dtime)
            nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY,nvel)

            particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
            Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 0)


            if t==len(tiempo)-1:
                corX[:,-1],corY[:,-1]=xp[:,0],xp[:,1]
                sigxx[:,-1],sigyy[:,-1],sigxy[:,-1]=sig[:,0],sig[:,1],sig[:,2]
                epsxx[:,-1],epsyy[:,-1],epsxy[:,-1]=epse[:,0],epse[:,1],epse[:,2]


            elif abs(tiempo[t+1]-tiempographic[tgraphic+1])<1e-13:
                
                corX[:,tgraphic+1],corY[:,tgraphic+1]= xp[:,0],xp[:,1]
                sigxx[:,tgraphic+1],sigyy[:,tgraphic+1],sigxy[:,tgraphic+1]=sig[:,0],sig[:,1],sig[:,2]
                epsxx[:,tgraphic+1],epsyy[:,tgraphic+1],epsxy[:,tgraphic+1]=epse[:,0],epse[:,1],epse[:,2]
                graphic_times.append(tiempographic[tgraphic+1])
                if tgraphic != len(tiempographic)-2:
                    tgraphic += 1

        #tiempographic = np.append(tiempographic, tiempo[-1]+dtime)
        #graphic_times.append(tiempo[-1]+dtime)

        tf =tm.time()
        print("tiempo", tf- t0)
        



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
            time_reached=tiempo[-1]                
        )

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
            analysis_times=analysis_times
        )
        self.model_result.updateResultTimeGraphic(
            graphic_time=graphic_times
        )
        self.model_result.updateResultMin(
            corx=corX.min(),
            cory=corY.min(),
            sigxx=sigxx.min(),
            sigyy=sigyy.min(),
            sigxy=sigxy.min(),
            epsxx=epsxx.min(),
            epsyy=epsyy.min(),
            epsxy=epsxy.min()
        )
        self.model_result.updateResultMax(
            corx=corX.max(),
            cory=corY.max(),
            sigxx=sigxx.max(),
            sigyy=sigyy.max(),
            sigxy=sigxy.max(),
            epsxx=epsxx.max(),
            epsyy=epsyy.max(),
            epsxy=epsxy.max()
        )
        
        for node in range(len(corX)):
            self.model_result.addResultNode(
                id_result_node=node+1, 
                corx=corX.tolist()[node],
                cory=corY.tolist()[node],
                sigxx=sigxx.tolist()[node],
                sigyy=sigyy.tolist()[node],
                sigxy=sigxy.tolist()[node],
                epsxx=epsxx.tolist()[node],
                epsyy=epsyy.tolist()[node],
                epsxy=epsxy.tolist()[node]
            )
        
        self.model_result.updateResult()
        self.signal_enable_results.emit()
        #falta eliminar datos de resultdos anteriores
        #graphic_button(corX, corY, sigxx, 4*Vp0[0],tiempographic, dx_size, dy_size)

        return True

        """
        graphic_button(corX, corY, sigxx, 4*Vp0[0],tiempographic, dimx, dimy)

        cdir = os.getcwd()
        ruta = u"c:/users/edwin arevalo/desktop/tesis unal geotecnia"
        namescript = ruta
        namescript = os.path.basename(namescript)
        namescript = namescript[:len(namescript) - 5]
        newfolder = cdir +'/graphics_'+ namescript
        if not os.path.exists(newfolder):
            os.mkdir(newfolder)



        graphic_gif(corX, corY, sigxx, 4*Vp0[0],tiempographic, dimx, dimy,newfolder)


        """
