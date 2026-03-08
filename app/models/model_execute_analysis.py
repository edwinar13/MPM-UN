
from motorMPM.mesh import create_uniform, contour_fixe, setup_MP,search_MP
from motorMPM.mesh import traction_forces,boundary_particles, node_conectivity
from motorMPM.explicit2 import deltatime,deltatime2, particles_to_nodes, BC_Dirichlet_momentum, particles_to_nodes_gauss2
from motorMPM.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel, nodes_to_particle_stress, static_convergence, nodes_to_particle_stress_gauss
from motorMPM.graphics import graphic_button,graphic_button2,graphic_button3,graphic_button4, graphic_video2,graphic_gif
from models.model_ProjectCurrent import ModelProjectCurrent
from models.model_Result import ModelResult
#from controllers.draw.controller_MenuExecute import AnalysisProgressDialog
from PySide6.QtWidgets import QApplication
import numpy as np
import time as tm
import math
import time
import pandas as pd

class MeshBack:
    """Clase que contiene la malla de fondo
    cor: coordenadas de los nodos
    inci: indices de los nodos de cada elemento
    ele_size: tamaño de los elementos
    nelex: numero de elementos en x    
    """
    def __init__(self, cor:np.ndarray,
                 inci:np.ndarray, 
                 ele_size:float, 
                 nelex:int):
        self.__cor = cor
        self.__inci = inci
        self.__ele_size = ele_size
        self.__nelex = nelex

        
    def cor(self):
        """Retorna las coordenadas de los nodos
        Description:
            Retorna un array con las coordenadas XY 
            de los nodos de la malla de fondo
        
        """
        return self.__cor
    
    def inci(self):
        """Retorna los indices de los nodos de cada elemento
        Description:
            Retorna un array con los indices de los nodos
            de cada elemento de la malla de fondo
        
        """
        return self.__inci
    
    def ele_size(self):
        """Retorna el tamaño de los elementos
        Description:
            Retorna el tamaño de los elementos de la malla de fondo
            el mismo para todos los elementos
        """
        return self.__ele_size
    def nelex(self):
        """Retorna el numero de elementos en x
        Description:
            Retorna el numero de elementos en x de la malla de fondo
        """
        return self.__nelex
    
    def nnodesx(self):
        """Retorna el numero de nodos en x"""
        nelex = self.nelex()
        return int(nelex + 1)
     
    def nnodesy(self):
        """Retorna el numero de nodos en y"""
        nnodesx = self.nnodesx()
        return int(len(self.__cor)/nnodesx)
    
    def nodeSupport(self):
        """Retorna la conectividad de los nodos
        Description:
            Retorna un array de los nodos y 
            los elementos a los que pertenecen                   
        """
        cor = self.cor()
        inci = self.inci()
        return node_conectivity(inci, len(cor[:,0]))

'''
class Body:
    """Clase que contiene un cuerpo (punto material + inf)
    nmp: numero de particulas
    xp: coordenadas de las particulas
    volumes: volumenes de las particulas
    velocities: velocidades de las particulas
    forces: fuerzas de las particulas 
    
    active_elem: elementos que tienen particulas
    mp_elem: elementos donde estan las particulas
    """
    def __init__(self, nmp:int, xp:np.ndarray, volumes:np.ndarray,
                 velocities:np.ndarray, forces:np.ndarray,
                 active_elem:np.ndarray, mp_elem:np.ndarray):
        self.__nmp = nmp
        self.__xp = xp
        self.__volumes = volumes
        self.__velocities = velocities
        self.__forces = forces
        self.__active_elem = active_elem
        self.__mp_elem = mp_elem
    
    def nmp(self):
        """Retorna el numero de particulas
        Description:
            Retorna el numero de particulas del cuerpo
        """
        return self.__nmp
    
    def xp(self):
        """Retorna las coordenadas de las particulas
        Description:
            Retorna un array con las coordenadas XY 
            de las particulas
        """
        return self.__xp

'''



        

class ModelExcuteAnalysisMPM:
    def __init__(self, analysis_dialog, model_current_project: ModelProjectCurrent, model_result:ModelResult,
                 dataTime, list_boundaries, list_point_material, 
                dt_time, list_time ,steps_time,
                dt_graphic, list_time_graphic, steps_time_graphic):
        
        # modelos generales y cuadros de dialogo
        self.analysis_dialog = analysis_dialog
        self.model_current_project = model_current_project
        self.model_result = model_result        
        
        # listado de puntos materiales y contornos
        self.list_boundaries = list_boundaries
        self.list_point_material = list_point_material
        
        # datos de tiempo
        self.__tm_dataTime = dataTime
        self.__tm_dt_time = dt_time
        self.__tm_dt_graphic = dt_graphic
        self.__tm_list_time = list_time
        self.__tm_list_time_graphic = list_time_graphic
        self.__tm_steps_time = steps_time
        self.__tm_steps_time_graphic = steps_time_graphic
        
         
        #===========  variables  ===========
        
        # Condiciones iniciales Cuasi-Estatico
        self.__dincre = None
        self.__nincre = None
        self.__charge = None
        self.__chargeGrav = None
        
        # Condiciones iniciales
        self.__ic_dampfac = None
        self.__ic_gravity = None
        
        # Restricciones
        self.__bo_fixed_nodesX = None
        self.__bo_fixed_nodesY = None
        
        # Puntos materiales
        self.__mp_mp_elem = None
        self.__mp_xp = None
        self.__mp_active_elem = None
        self.__mp_nmp = None
        
        # Propiedades
        self.__mp_prop = None
        self.__mp_density = None
        
        
        self.mesh = None
        self.initMeshBack()
        
        
        
    def runViga(self):  
        print("runViga")      
        response = self.initConditions()
        #response = self.initMeshBack()
        response = self.initBoundary()
        response = self.initMaterialPoint()
        response = self.initProperties()
        response = self.initVerctorAndMatrix()
        response = self.initBoundaryParticles()        
        response = self.executeAnalysisViga()       
        if response: 
            response = self.saveResults()        
        return response

    def runAnalysisCE(self):
        print("runAnalysisCE")
        response = self.initConditionsAnalysisCE()
        response = self.initConditions()
        #response = self.initMeshBack()
        response = self.initBoundary()        
        response = self.initMaterialPoint()
        response = self.initProperties()
        response = self.initVerctorAndMatrix()
        response = self.initBoundaryParticles()        
        response = self.executeAnalysisCE()         
        if response: 
            response = self.saveResults()        
        return response

    def runAnalysisDisc(self):
        print("runAnalysisDisc")
        return
        response = self.initConditions()
        #response = self.initMeshBack()
        response = self.initBoundary()        
        response = self.initMaterialPoint()
        response = self.initProperties()
        response = self.initVerctorAndMatrix()
        response =self.initStateStressGeo()
        response = self.executeAnalysisDisc() 
        return
        response = self.initBoundaryParticles()        
        if response: 
            response = self.saveResults()        
        return response
              
        
        
        
    def initConditionsAnalysisCE(self):
        nincre = self.model_current_project.getNoIncre()
        dincre = self.model_current_project.getDincre()
        dincreGrav = self.model_current_project.getDincreGrav()
        charge = -np.linspace(0, dincre*nincre, nincre + 1) # array con los valores de carga de cada incremento
        chargeGrav = -np.linspace(0, dincreGrav*nincre, nincre + 1) # array con los valores de gravedad de cada incremento 
        '''
        '''
        self.__dincre = dincre
        self.__dincreGrav = dincreGrav
        self.__charge = charge
        self.__chargeGrav = chargeGrav
        self.__nincre = nincre
        
        print("self.__dincre", self.__dincre)
        print("self.__dincreGrav", self.__dincreGrav)
        print("self.__charge", self.__charge)
        print("self.__chargeGrav", self.__chargeGrav)
        print("self.__nincre", self.__nincre)
        

    
    def initConditions(self):
        self.__ic_dampfac = self.model_current_project.getDampfac()
        self.__ic_gravity = self.model_current_project.getGravity()
        '''
        print("self.__ic_dampfac", self.__ic_dampfac)
        print("self.__ic_gravity", self.__ic_gravity)
        '''

      
    def initMeshBack(self):

        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::: malla fondo ::::::::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # las coordendas de la malla    ::  cor
        # los indices de cada elemento  ::  inci
        # el tamaño de cada elemento    ::  ele_size
        # el nuemro de elementos en x   ::  nelex
        model_mesh_back = self.model_current_project.getModelMeshBack()

        nodes = model_mesh_back.getNodes()
        elements = model_mesh_back.getElements()
        ele_size = model_mesh_back.getSizeElement()
        dx_size = model_mesh_back.getSizeDx()
        dy_size = model_mesh_back.getSizeDy()
        cor = []
        no_nodes = len(nodes.keys())
        for i in range(1, no_nodes+1):
            id_node = f'NODE#{i}'
            cor.append(
                [nodes[id_node]['COORDINATES'][0],
                nodes[id_node]['COORDINATES'][1]]
            )
        
        inci = []
        no_elements = len(elements.keys())
        for i in range(1, no_elements+1):
            id_element = f'ELEMENT#{i}'
            # ELEMENT ['NODE#1', 'NODE#2', 'NODE#13', 'NODE#12']
            #agregar solo los numeros de los nodos eje [1,2,13,12]
            inci.append(
                [int(elements[id_element][0].split('#')[1]),
                int(elements[id_element][1].split('#')[1]),
                int(elements[id_element][2].split('#')[1]),
                int(elements[id_element][3].split('#')[1])]
            )
        
        cor=np.asarray(cor)
        inci=np.asarray(inci)
        
        
        self.mesh = MeshBack(cor=cor,
                             inci= inci,
                             ele_size=ele_size,
                             nelex=int(dx_size/ele_size))
        

        
    def initBoundary(self):
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::: restriccion de movimiento ::::::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        # indices de los nodos con restriccion de movimiento en direccion x  ::  fixed_nodesX
        # indices de los nodos con restriccion de movimiento en direccion y :: fixed_nodesY
        list_boundaries = self.list_boundaries
        fixed_nodesX=[]
        fixed_nodesY=[]
        models_boundary = self.model_current_project.getModelsBoundaries()
        list_ids_boundaries =[]
        for boundary in list_boundaries:
            list_ids_boundaries.append(boundary['id'])
            
        for id_model_boundary in models_boundary:
            if id_model_boundary in list_ids_boundaries:
                model_boundary = models_boundary[id_model_boundary]
                #points = model_boundary.getPoints()
                nodes = model_boundary.getNodes()
                restriction_x = model_boundary.getRestrictionX()
                restriction_y = model_boundary.getRestrictionY()

                if restriction_x:
                    for node in nodes:
                        index = int(node.split('#')[1])
                        fixed_nodesX.append(index)

                if restriction_y:
                    for node in nodes:
                        index = int(node.split('#')[1])
                        fixed_nodesY.append(index)
 
        fixed_nodesX = list(set(fixed_nodesX))
        fixed_nodesY = list(set(fixed_nodesY))
        fixed_nodesX.sort()
        fixed_nodesY.sort()

        self.__bo_fixed_nodesX = np.asarray(fixed_nodesX)
        self.__bo_fixed_nodesY = np.asarray(fixed_nodesY)
        '''
        print("self.__bo_fixed_nodesX", self.__bo_fixed_nodesX)
        print("self.__bo_fixed_nodesY", self.__bo_fixed_nodesY)
        '''


    def initMaterialPoint(self):
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

        list_point_material = self.list_point_material
        models_material_point = self.model_current_project.getModelsPointsMaterials()

        
        model_mesh_back = self.model_current_project.getModelMeshBack()
        nodes = model_mesh_back.getNodes()
        cells = model_mesh_back.getElements()
        #---------
        mp_xp=[]
        mp_property = []
        #---------
        mp_elem=[]
        mp_volumes=[]
        mp_velocities=[]
        mp_forces=[]
                
        for id_material_point in list_point_material:
            model_material_point = models_material_point[id_material_point]
            points = model_material_point.getPoints()
            name = model_material_point.getName()
            id_property = model_material_point.getIdProperty()
            
            cells_by_point = self.findCellForPoints(material_points = points,
                                        elements=cells,
                                        nodes=nodes)           
            for cell in cells_by_point:
                mp_elem.append([int(cells_by_point[cell].split('#')[1])])
                
                
                
            for point in points:    
                '''
                "POINT#1": {
                    "COORDINATES": [3.4999999999994587, 1.3648075286198094],
                    "VOLUME": 0.5472112929297124,
                    "VELOCITY": { "X": -2.0, "Y": 0.0 },
                    "FORCE": { "X": 0.0, "Y": -2.0 }
                    },
                '''            
                p = points[point]['COORDINATES']
                mp_xp.append([p[0], p[1]])
                mp_property.append(id_property)
                vol = points[point]['VOLUME']
                mp_volumes.append(vol)
                vel = points[point]['VELOCITY']
                mp_velocities.append([vel['X'], vel['Y']])
                force = points[point]['FORCE']
                mp_forces.append([force['X'], force['Y']])
                
                    
        #variables
        self.__mp_xp = np.asarray(mp_xp)
        self.__mp_property = np.asarray(mp_property)
        self.__mp_mp_elem = np.asarray(mp_elem)
        self.__mp_active_elem = np.unique(self.__mp_mp_elem[:, 0])
        self.__mp_nmp = len(self.__mp_mp_elem)
        
        '''
        print("self.__mp_xp", self.__mp_xp)
        print("self.__mp_mp_elem", self.__mp_mp_elem)
        print("self.__mp_active_elem", self.__mp_active_elem)
        print("self.__mp_nmp", self.__mp_nmp)
        '''

        
        #►►►►►►►►►►►►►►                                 ◄◄◄◄◄◄◄◄◄◄◄◄◄
        #     esto ajjstar cuando sean dos materiales
        #     o mas, por que solo se esta asignando el
        #     ultimo material point.
        self.VOLUMES = mp_volumes
        self.VELOCITIES = mp_velocities
        self.FORCES = mp_forces
        #►►►►►►►►►►►►►►                                 ◄◄◄◄◄◄◄◄◄◄◄◄◄

    def initProperties(self):
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

        list_point_material = self.list_point_material
        models_material_point = self.model_current_project.getModelsPointsMaterials()
        models_property = self.model_current_project.getModelsProperties()
        


        mp_prop=[]
        mp_density = []
        for id_material_point in list_point_material:
            model_material_point = models_material_point[id_material_point]
            points = model_material_point.getPoints()            
            id_material = model_material_point.getIdProperty()
            
            model_property = models_property[id_material]
            '''
            {'f00e68c9-e12f-4b63-915c-215abcebad44':
                {
                'COLOR': '#646464',
                'NAME': 'material beam',
                'MODULOELASTICIDAD': 10000.0,
                'RELACIONPOISSON': 0.2,
                'COHESION': 5.0,
                'ANGULOFRICCION': 25.0,
                'DENSIDAD': 2000,
                'ANGULODILATANCIA': 5.0 }
            }
            '''
            data = model_property.getData()
            id_mat = list(data.keys())[0]
            name = data[id_mat]['NAME']
            modulus_elasticity = data[id_mat]['MODULOELASTICIDAD']
            poisson_ratio = data[id_mat]['RELACIONPOISSON']
            cohesion = data[id_mat]['COHESION']
            friction_angle = data[id_mat]['ANGULOFRICCION']
            density = data[id_mat]['DENSIDAD']
            angle_dilatancy = data[id_mat]['ANGULODILATANCIA']
            
            for point in points:     
                         
                mp_prop.append([modulus_elasticity,
                                poisson_ratio,
                                cohesion,
                                friction_angle / 180*math.pi,
                                angle_dilatancy / 180*math.pi,
                                0]) # este cero lo tiene los archivos de referencia leon(2019)
                mp_density.append(density/1000)
                
        #variables
        Prop = np.asarray(mp_prop)
        self.__mp_prop = Prop
        self.DENSITY = mp_density
        '''
        print("self.__mp_prop", self.__mp_prop)
        '''
          
    def initVerctorAndMatrix(self):
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

        density = self.DENSITY
        volumes = self.VOLUMES
        nmp = self.__mp_nmp

        Vp =  np.asarray(volumes)
        Vp0 = np.asarray(volumes)      
        rhop = np.asarray(density)
        Mp = np.multiply(rhop, Vp) 
        
        # variables
        self.__vm_Vp = Vp
        self.__vm_Vp0 = Vp0
        self.__vm_rhop = rhop
        self.__vm_Mp = Mp
        
        '''
        print("self.__vm_Vp", self.__vm_Vp)
        print("self.__vm_Vp0", self.__vm_Vp0)
        print("self.__vm_rhop", self.__vm_rhop)
        print("self.__vm_Mp", self.__vm_Mp)
        '''
                


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

        gravity = self.__ic_gravity
        '''
        vel_ini_x = self.__ic_vel_ini_x
        vel_ini_y = self.__ic_vel_ini_y
        vp = np.ones((nmp, 2)) * np.array([vel_ini_x, vel_ini_y])   
        '''
        velo_ini = self.VELOCITIES
        

        Fp = np.ones((nmp, 4))
        Fp[:,1:3] = 0        
        sig = np.zeros((nmp, 4))
        epse = np.zeros((nmp, 3))
        epsp = np.zeros((nmp, 3))        
        vp = np.asarray(velo_ini)           
        bp=np.zeros((nmp, 2))
        if gravity != 0:
            bp[:,1]=-gravity        

        tp0 = np.zeros((nmp, 2))
        for i in range(nmp):
            tp0[i][0] = self.FORCES[i][0]
            tp0[i][1] = self.FORCES[i][1]
            
        
        
        # variables
        
        self.__vm_Fp = Fp
        self.__vm_sig = sig
        self.__vm_epse = epse
        self.__vm_epsp = epsp
        self.__vm_vp = vp
        self.__vm_bp = bp
        self.__vm_tp0 = tp0
        '''
        print("self.__vm_Fp", self.__vm_Fp)
        print("self.__vm_sig", self.__vm_sig)
        print("self.__vm_epse", self.__vm_epse)
        print("self.__vm_epsp", self.__vm_epsp)
        print("self.__vm_vp", self.__vm_vp)
        print("self.__vm_bp", self.__vm_bp)
        print("self.__vm_tp0", self.__vm_tp0)

        xp = self.__mp_xp
        for tp_i in range(len(tp0)):
            #print("tp0", tp0[tp_i], "xp:", xp[tp_i])
            if tp0[tp_i][1] != 0:
                print("tp0", tp0[tp_i], "xp:", xp[tp_i])
        '''
            
        

    def initBoundaryParticles(self):
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
        
        xp = self.__mp_xp
        # si se va a emplear integracion gaussiana - obtener array con particulas de la frontera
        bound_ptcl, bound_val = boundary_particles(xp)
        '''
        print("bound_ptcl", bound_ptcl)
        print("bound_val", bound_val)
        for i in range(len(bound_ptcl)):
            if bound_val[i] == 1:
                print("bound_ptcl", bound_ptcl[i], "bound_val", bound_val[i])
        '''
        
        self.__bo_bound_ptcl = bound_ptcl
        self.__bo_bound_val = bound_val
        
    def initStateStressGeo(self):
        # ==== ESTADO DE ESFUERZOS GEOSTATICO =========
        Prop_1 = self.__mp_prop
        rhop_1 = self.__vm_rhop
        nmp_1 = self.__mp_nmp
        ele_size = self.__mb_ele_size
        xp_1 = self.__mp_xp
        sig_1 = self.__vm_sig
        
        nmpe_1 = 4
        
        # Definir un valor inicial de esfuerzo
        k0 = Prop_1[:,1] / (1 - Prop_1[:,1]) # definicion elastica
        #k0 = 1 - np.sin(Prop[:,3]) # definicion Jacky
        ymax = [np.max(xp_1[np.where(xp_1[:,0] == xp_1[i,0])[0],1]) for i in range(nmp_1)] + ele_size / (2 * (nmpe_1)**(1/2))*np.ones(nmp_1)
        sig_1[:,1] = -(ymax - xp_1[:,1]) * rhop_1[:] * 0 # 9.81 # esfuerzo en y
        sig_1[:,0] = sig_1[:,1] * k0 # esfuerzo en x
        sig_1[:,3] = sig_1[:,1] * k0 # esfuerzo en z
        
        
        
        print("K0: ", k0)
        print("Esfuerzo en y: ", sig_1[:,1])
        print("Esfuerzo en x: ", sig_1[:,0])
        print("Esfuerzo en z: ", sig_1[:,3])
                
            
    def executeAnalysisDisc(self):
        inci = self.__mb_inci
        active_elem_1 = self.__mp_active_elem
        active_nodes_1 = np.unique(inci[active_elem_1 - 1,:])
        '''
        print("active_nodes_1", active_nodes_1)
        '''
        
    def executeAnalysisCE(self):
        
        # variables necesarias
        analysis_dialog = self.analysis_dialog

        # incrementos de carga
        dincre = self.__dincre
        dincreGrav = self.__dincreGrav
        charge = self.__charge
        chargeGrav = self.__chargeGrav

        nincre = self.__nincre


        
        

        list_time_graphic = np.linspace(0, nincre, nincre+1)
        list_time = np.linspace(0, nincre, nincre+1)
        steps_time = nincre
        dtime = self.__tm_dt_time
        
    
        
      
        '''
        # mesh back
        ele_size = self.__mb_ele_size
        nelex = self.__mb_nelex
        inci = self.__mb_inci
        cor = self.__mb_cor
        '''


        
        # material point
        nmp =   self.__mp_nmp
        xp =    self.__mp_xp
        mp_elem = self.__mp_mp_elem
        
        # boundary
        fixed_nodesX = self.__bo_fixed_nodesX
        fixed_nodesY = self.__bo_fixed_nodesY
        
        #properties
        Prop = self.__mp_prop
        
        # vertor and matrix
        Fp =   self.__vm_Fp
        sig =   self.__vm_sig
        epse = self.__vm_epse
        epsp = self.__vm_epsp
        vp = self.__vm_vp
        Vp = self.__vm_Vp
        Vp0 = self.__vm_Vp0
        Mp = self.__vm_Mp
        bp = self.__vm_bp
        tp0 = self.__vm_tp0
        
        
        dampfac = self.__ic_dampfac
        
        
        bound_ptcl = self.__bo_bound_ptcl
        bound_val = self.__bo_bound_val
        
        
        
        
        t0 = tm.time()	
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'tiempo inicial: {t0}')     
        
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  arrays para guardar info a graficar :::::::::::::::::::::::::::::::::::
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

        corX = np.empty((nmp, nincre+1))
        corY = np.empty((nmp, nincre+1))  
        sigxx = np.empty((nmp, nincre+1))
        sigyy = np.empty((nmp, nincre+1))
        sigxy = np.empty((nmp, nincre+1))
        epspxx = np.empty((nmp, nincre+1))
        epspyy = np.empty((nmp, nincre+1))
        epspxy = np.empty((nmp, nincre+1))
        epsexx = np.empty((nmp, nincre+1))
        epseyy = np.empty((nmp, nincre+1))
        epsexy = np.empty((nmp, nincre+1))
        velxx = np.zeros((nmp, nincre+1))
        velyy = np.zeros((nmp, nincre+1))
        velxy = np.zeros((nmp, nincre+1))
        desplxx = np.zeros((nmp, nincre+1))
        desplyy = np.zeros((nmp, nincre+1))
        desplxy = np.zeros((nmp, nincre+1))
        eqplas = np.zeros((nmp, nincre+1))            
   

        corX[:,0], corY[:,0] = xp[:,0], xp[:,1] # coordenadas de las particulas
        sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
        epsexx[:,0], epseyy[:,0], epsexy[:,0] = epse[:,0], epse[:,1], epse[:,2] # deformaciones elasticas
        epspxx[:,0], epspyy[:,0], epspxy[:,0] = epsp[:,0], epsp[:,1], epsp[:,2] # deformaciones plasticas
        velxx[:,0], velyy[:,0] = vp[:,0], vp[:,1]
        velxy = np.sqrt(velxx[:,0]**2 + velyy[:,0]**2)
        desplxx[:,0], desplyy[:,0] , desplxy[:,0] = 0, 0, 0 # desplazamiento inicial
        eqplas[:,0] = 0 # def plastica equivalente
    
    
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

      
        
       

        #new_list_time_graphic = list_time_graphic.copy()
        #new_list_time = list_time.copy()
        #current_index_graphic = 0


        # -- INICIO CICLO INCREMENTOS DE CARGA --
        tmax = 0 # tiempo maximo por incremento
        mp = 1-1 # particula superior izquierda
        for i in range(nincre):
        
            ########################################################################
            #              Si se pausa o se cancela el análisis       
            ########################################################################                
                
            # si se cierra el dialogo
            if analysis_dialog.cancelled:
                analysis_dialog.close()
                return False
            
            # si se pausa en el dialogo
            if analysis_dialog.paused:
                analysis_dialog.setStatus(False, f"Ejecutando incremento del análisis:\n→ {i:.0f} de {nincre} pasos.\n\nAnálisis pausado")
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()  # Mantener la ventana actualizada
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                #analysis_dialog.setStatus(False, "Reanudando análisis...") 
            
            
            ########################################################################
            #              Si todo esta bien se continua con el análisis
            #                      analisis de las particulas                   
            ########################################################################        
            analysis_dialog.setProgress(100*i/nincre)
            analysis_dialog.setStatus(False, f"Ejecutando incremento del análisis:\n→ {i:.0f} de {nincre} pasos.")
            QApplication.processEvents()     
            
                
            bp[:, 1] = (i+1) * dincreGrav * bp[:, 1] # haciendo el incremento de carga de gravedad
            tp = (i+1) * dincre * tp0 # haciendo el incremento de carga  
            print("-"*20)
            print("tp", tp)
            print("bp", bp)
            print("-"*20)
            # inicializando parametros de convergencia
            ff = 1
            ee = 1
            nework = 0

            tcont = 0 # contador de interaciones
            # -- INCIAR CILO EN EL TIEMPO --
            tinicial = time.time() 
            
            while (ff > 0.011) or (ee > 0.01):
                # imprimir timepo de ejecucion en la iteracion pero borra el tiempo anterior
                analysis_dialog.setTimer(f"⏳ {time.time() - tinicial:.0f}seg")
                QApplication.processEvents()     
                #print(f"⏳ {time.time() - tinicial:.0f}seg", end="\r")
                tcont += 1 #avanzando contador de tiempo
                            
                ########################################################################
                #              Si el material se encuentra fuera de la malla            
                #                         se detiene el análisis 
                ########################################################################
                # --- buscar elementos y nodos activos ---
                mp_elem, active_elem = search_MP(mp_elem, xp, self.mesh.ele_size(), self.mesh.nelex()) # buscar en que elem estan los MPs
                active_nodes = np.unique(self.mesh.inci()[active_elem - 1,:]) # lista de nodos activos
 
                ########################################################################                    
                # --- transferir de las particulas a los nodos ----
                grid = self.mesh.inci(), self.mesh.cor(), active_elem, active_nodes, mp_elem # creando lista de valores de la malla
                particle = xp, vp, Vp, Mp, sig, bp, tp # creando lista de partiulas 


                #nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
                nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes_gauss2(grid, particle, bound_val) # habilitar si es integracion mixta
                #print(nmass, nmomentum,niforce, neforce, shfnp)
                
                
                # --- Solucion sistema de ecuaciones nodales --- EXPLICITO!!
                #dampfac = 0.75
                ndamping = -dampfac*np.multiply(np.absolute(niforce + neforce), np.sign(nmomentum))
                nforce = niforce + neforce + ndamping
                nmomentum += nforce*dtime
                
                # --- Fijar nodos de Dirichlet ---
                nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce, niforce, neforce)
                
                # --- Transferir de los nodos a las particulas - velocidad y posicion ---
                nquantities = nmass, nmomentum, nforce # creando lista de valores nodales
                particle = xp, vp, Vp, Mp, sig, shfnp # creando lista de particulas
                xp, vp, nvel = nodes_to_particle_vel(grid, particle, nquantities, dtime)

                nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel) # fijar nodos de Dirichlet nvel

 

                # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion ---
                particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
                #Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 1)
                Fp, Vp, epse, epsp, sig = nodes_to_particle_stress_gauss(grid, particle, bound_val, nvel, dtime, 1)
                '''
                print(sig[:,1])
                if i == nincre-1:
                    print(f"[{algo}] mp{mp+1}:{sig[:,1][mp]}")
                    algo += 1            
                if algo == 1:
                    return
                    
                 mp1:-0.010161493288590595
                '''
                                
                # --- Calcular parametros que determinar el equilibrio cuasi-estatico ---
                # Parametros tiempo anterior
                ff0 = ff
                ee0 = ee
                nework0 = nework 
                ff, ee, nework = static_convergence(nmass, niforce, neforce, nvel, dtime, nework0)
                
                # Condicion para que salga del ciclo si lleva mucho tiempo en la iteracion
                tiempoi = time.time() - tinicial
                if (tiempoi > 100*t0) and (i > 0):
                    # si el tiempo de ejecucion es mayor a 20 veces el max anterior a partir de i=1
                    print("se excedio tiempo maximo de ejecucion!!")
                    finfor = True
                    break
                else:
                    finfor = False

            # -- FIN CICLO DE TIEMPO --
            tiempo = time.time() - tinicial # tiempo en la iteracion
            if i == 0:
                # guardando nuevo valor de tiempo de la iteracion 1
                t0 = tiempo
            
            print("incremento ", i + 1, "numero de ciclos ", tcont)
            print("tiempo en este incremento ", tiempo, " segundos")
            print("desbalance de fuerzas ", ff, "Energia cinetica ", ee)
            print()
            # Grabar informacion del tiempo que consigue el equilibrio estatico
            corX[:,i+1], corY[:,i+1] = xp[:,0], xp[:,1] # coordenadas de las particulas
            sigxx[:,i+1], sigyy[:,i+1], sigxy[:,i+1] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos           
            epsexx[:,i+1], epseyy[:,i+1], epsexy[:,i+1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones elasticas
            epspxx[:,i+1], epspyy[:,i+1], epspxy[:,i+1] = epsp[:,0], epsp[:,1], epsp[:,2] # deformaciones plasticas
            # calcular desplazamiento total

            desplxx[:,i+1] = corX[:,i+1] -corX[:,0]
            desplyy[:,i+1] = corY[:,i+1] -corY[:,0]
            desplxy[:,i+1] = np.sqrt((corX[:,0] - corX[:,i+1])**2 + (corY[:,0] - corY[:,i+1])**2)
            # deformacion plastica equivalente
            eqplas[:,i+1] = np.sqrt(4/9*(epsp[:,0]**2 - epsp[:,0]*epsp[:,1] + epsp[:,1]**2) + 4/3*epsp[:,2]**2)
                
            if finfor == True:
                # se debe salir del ciclo for por que no se alcanzo equilibrio
                break

        # -- FIN CICLO DE INCREMENTOS DE CARGA --
                
        # tomar solo los array que se llenaron - HASTA EL VALOR QUE TENGA i
        corX, corY = corX[:,:i+2], corY[:,:i+2]
        sigxx, sigyy, sigxy = sigxx[:,:i+2], sigyy[:,:i+2], sigxy[:,:i+2]
        epsexx, epseyy, epsexy = epsexx[:,:i+2], epseyy[:,:i+2], epsexy[:,:i+2]
        epspxx, epspyy, epspxy = epspxx[:,:i+2], epspyy[:,:i+2], epspxy[:,:i+2]        
        eqplas = eqplas[:,:i+2]
        charge = charge[:i+2]

        #print("Desplazamiento en la parte superior: ", corY[-int((xf-xi)/ele_size/2)*nmpe,0] - corY[-int((xf-xi)/ele_size/2)*nmpe, -1])
        #print("Esfuerzo syy en la base: ", sigyy[int((xf-xi)/ele_size/2)*nmpe, -1])

    
        tf =tm.time()
        print("tiempo", tf- t0)
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        dimy = 2
        dimx = 2
        #print(corX, corY, sigyy, Vp0[0]*(12/dimy)**2, charge, dimx, dimy)
        graphic_button2(corX, corY, desplxy, Vp0[0]*(12/dimy)**2, charge, dimx, dimy)
        #guardar en un archivo excel corX, corY, sigyy
        self.save_results_excel(corX, corY, sigyy)

    
        # con np
        self.__rs_new_list_time = list_time.copy()
        #self.__rs_new_list_time = new_list_time
        self.__rs_new_list_time_graphic = list_time_graphic.copy()
        #self.__rs_new_list_time_graphic = new_list_time_graphic
        self.__rs_corX = corX
        self.__rs_corY = corY
        self.__rs_sigxx = sigxx
        self.__rs_sigyy = sigyy
        self.__rs_sigxy = sigxy
        self.__rs_epsexx = epsexx
        self.__rs_epseyy = epseyy
        self.__rs_epsexy = epsexy
        self.__rs_epspxx = epspxx
        self.__rs_epspyy = epspyy
        self.__rs_epspxy = epspxy
        self.__rs_velxy = velxy
        self.__rs_velxx = velxx
        self.__rs_velyy = velyy
        self.__rs_desplxy = desplxy
        self.__rs_desplxx = desplxx
        self.__rs_desplyy = desplyy
        self.__rs_eqplas = eqplas               
        
        
        return True

    def executeAnalysisViga(self):       
        
        # variables necesarias
        analysis_dialog = self.analysis_dialog
        
        list_time_graphic = self.__tm_list_time_graphic
        list_time =         self.__tm_list_time
        steps_time =        self.__tm_steps_time
        dt_time =           self.__tm_dt_time
        
        # mesh back
        '''
        ele_size = self.__mb_ele_size
        nelex = self.__mb_nelex
        inci = self.__mb_inci
        cor = self.__mb_cor
        '''
        
        # material point
        nmp =   self.__mp_nmp
        xp =    self.__mp_xp
        mp_elem = self.__mp_mp_elem
        
        # boundary
        fixed_nodesX = self.__bo_fixed_nodesX
        fixed_nodesY = self.__bo_fixed_nodesY
        
        #properties
        Prop = self.__mp_prop
        
        # vertor and matrix
        Fp =   self.__vm_Fp
        sig =   self.__vm_sig
        epse = self.__vm_epse
        epsp = self.__vm_epsp
        vp = self.__vm_vp
        Vp = self.__vm_Vp
        Vp0 = self.__vm_Vp0
        Mp = self.__vm_Mp
        bp = self.__vm_bp
        tp = self.__vm_tp0
        
        
        dampfac = self.__ic_dampfac
        
        
        
        
        
        t0 = tm.time()	
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'tiempo inicial: {t0}')     
        
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::::::::::::::::  arrays para guardar info a graficar :::::::::::::::::::::::::::::::::::
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

        corX = np.zeros((nmp, len(list_time_graphic)))
        corY = np.zeros((nmp, len(list_time_graphic)))     
        sigxx = np.zeros((nmp, len(list_time_graphic)))
        sigyy = np.zeros((nmp, len(list_time_graphic)))
        sigxy = np.zeros((nmp, len(list_time_graphic)))
        epsexx = np.zeros((nmp, len(list_time_graphic)))
        epseyy = np.zeros((nmp, len(list_time_graphic)))
        epsexy = np.zeros((nmp, len(list_time_graphic)))
        epspxx = np.zeros((nmp, len(list_time_graphic)))
        epspyy = np.zeros((nmp, len(list_time_graphic)))
        epspxy = np.zeros((nmp, len(list_time_graphic)))
        velxx = np.zeros((nmp, len(list_time_graphic)))
        velyy = np.zeros((nmp, len(list_time_graphic)))
        velxy = np.zeros((nmp, len(list_time_graphic)))
        desplxx = np.zeros((nmp, len(list_time_graphic)))
        desplyy = np.zeros((nmp, len(list_time_graphic)))
        desplxy = np.zeros((nmp, len(list_time_graphic)))
        eqplas = np.zeros((nmp, len(list_time_graphic)))
        
   
 
        corX[:,0], corY[:,0] = xp[:,0], xp[:,1]
        sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2]
        epspxx[:,0], epspyy[:,0], epspxy[:,0] = epsp[:,0], epsp[:,1], epsp[:,2]
        epsexx[:,0], epseyy[:,0], epsexy[:,0] = epse[:,0], epse[:,1], epse[:,2]
        velxx[:,0], velyy[:,0] = vp[:,0], vp[:,1]   
        velxy[:, 0] = np.sqrt(velxx[:,0]**2 + velyy[:,0]**2)
        desplxx[:,0], desplyy[:,0] , desplxy[:,0] = 0, 0, 0
        eqplas[:,0] = 0 # def plastica equivalente

        



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
            mp_elem, active_elem = search_MP(mp_elem, xp, self.mesh.ele_size(), self.mesh.nelex())      
            try:
                active_nodes = np.unique(self.mesh.inci()[active_elem-1, :])
            except Exception as e:
                
                print("---------------------//-------------------------")
                print("Error: ", e)
                print("Error en el tiempo: ", current_time, " paso: ", index)
                print("Tamaño de inci:", self.mesh.inci().shape)
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
                        epspxx = epspxx[:, :position_max]
                        epspyy = epspyy[:, :position_max]
                        epspxy = epspxy[:, :position_max]
                        epsexx = epsexx[:, :position_max]
                        epseyy = epseyy[:, :position_max]
                        epsexy = epsexy[:, :position_max]
                        velxx = velxx[:, :position_max]
                        velyy = velyy[:, :position_max]
                        velxy = velxy[:, :position_max]
                        desplxx = desplxx[:, :position_max]
                        desplyy = desplyy[:, :position_max]
                        desplxy = desplxy[:, :position_max]
                        eqplas = eqplas[:, :position_max]
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
            grid = self.mesh.inci(), self.mesh.cor(), active_elem, active_nodes, mp_elem
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
                epsexx[:,current_index_graphic + 1],epseyy[:,current_index_graphic + 1],epsexy[:,current_index_graphic + 1]=epse[:,0],epse[:,1],epse[:,2]
                epspxx[:,current_index_graphic + 1],epspyy[:,current_index_graphic + 1],epspxy[:,current_index_graphic + 1]=epsp[:,0],epsp[:,1],epsp[:,2]
                velxx[:,current_index_graphic + 1], velyy[:,current_index_graphic + 1] = vp[:,0], vp[:,1]
                velxy[:, current_index_graphic + 1] = np.sqrt(vp[:,0]**2 + vp[:,1]**2)
                desplxx[:,current_index_graphic + 1] = corX[:,current_index_graphic + 1] - corX[:,0]
                desplyy[:,current_index_graphic + 1] = corY[:,current_index_graphic + 1] - corY[:,0]
                desplxy[:,current_index_graphic + 1] = np.sqrt((corX[:,0] - corX[:,current_index_graphic + 1])**2 + (corY[:,0] - corY[:,current_index_graphic + 1])**2)                   
                current_index_graphic += 1
          
        print(">>: ", vp[0])
        print('*/*/*/* velxy ', velxy.shape)
        print('++/++/++/++ velx ', velxx.shape)
        tf =tm.time()
        print("tiempo", tf- t0)
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        
        self.__rs_new_list_time = new_list_time
        self.__rs_new_list_time_graphic = new_list_time_graphic
        self.__rs_corX = corX
        self.__rs_corY = corY
        self.__rs_sigxx = sigxx
        self.__rs_sigyy = sigyy
        self.__rs_sigxy = sigxy
        self.__rs_epsexx = epsexx
        self.__rs_epseyy = epseyy
        self.__rs_epsexy = epsexy
        self.__rs_epspxx = epspxx
        self.__rs_epspyy = epspyy
        self.__rs_epspxy = epspxy
        self.__rs_velxy = velxy
        self.__rs_velxx = velxx
        self.__rs_velyy = velyy
        self.__rs_desplxx = desplxx
        self.__rs_desplyy = desplyy
        self.__rs_desplxy = desplxy
        self.__rs_eqplas = eqplas
        
        
        
        return True
    
    def saveResults(self):
        model_mesh_back = self.model_current_project.getModelMeshBack()
        
        #variables iniciales
        list_point_material = self.list_point_material
        models_material_point = self.model_current_project.getModelsPointsMaterials()
        list_boundaries = self.list_boundaries
        models_boundary = self.model_current_project.getModelsBoundaries()
        
        #result
        new_list_time = self.__rs_new_list_time
        new_list_time_graphic = self.__rs_new_list_time_graphic
        corX = self.__rs_corX
        corY = self.__rs_corY
        sigxx = self.__rs_sigxx
        sigyy = self.__rs_sigyy
        sigxy = self.__rs_sigxy
        epspxx = self.__rs_epspxx
        epspyy = self.__rs_epspyy
        epspxy = self.__rs_epspxy        
        epsexx = self.__rs_epsexx
        epseyy = self.__rs_epseyy
        epsexy = self.__rs_epsexy
        velxy = self.__rs_velxy
        velxx = self.__rs_velxx
        velyy = self.__rs_velyy
        desplxx = self.__rs_desplxx
        desplyy = self.__rs_desplyy
        desplxy = self.__rs_desplxy
        eqplas = self.__rs_eqplas
        
        ########################################################################
        #                           analisis finalizado
        ########################################################################        
        self.model_result.clearResult()        
        
        self.model_result.updateResultDataBase(
            gravity= self.__ic_gravity,
            dampfac=  self.__ic_dampfac
        )
        
        
        for id_material_point in list_point_material:    
            model_material_point = models_material_point[id_material_point]
            model_property = model_material_point.getProperty()


            self.model_result.addResultProperty(
                id_property = model_property.getId(),
                name = model_property.getName(),
                color= model_property.getColor(),
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
                points = model_material_point.getPoints(),
                id_property = model_property.getId()
            )
        
        for boundary in list_boundaries:
            id_boundary = boundary['id']
            name = boundary['name']
            model_boundary = models_boundary[id_boundary]
            nodes = model_boundary.getNodes()
            restriction_x = model_boundary.getRestrictionX()
            restriction_y = model_boundary.getRestrictionY()
            self.model_result.addResultBoundary(
                id_boundary = id_boundary,
                name = name,
                nodes = nodes,
                restrictionX = restriction_x,
                restrictionY = restriction_y
            )
            
       
        self.model_result.updateResultDataTimes(
            id_material=self.__tm_dataTime['id_property'],
            courant_number=self.__tm_dataTime['courant_number'],
            analysis_time=self.__tm_dataTime['analysis_time'],
            fps=self.__tm_dataTime['fps'],
            dt_analysis=self.__tm_dataTime['dt_analysis'],
            dt_graphic=self.__tm_dataTime['dt_graphic'],
            analysis_steps=self.__tm_dataTime['analysis_steps'],
            graphic_steps=self.__tm_dataTime['graphic_steps'],
            speed_cp=self.__tm_dataTime['speed_cp'],
            time_reached=new_list_time[-1]                
        )
        #    time_reached=new_list_time[-1]                
        




        self.model_result.updateResultMeshBack(
            size_dx=model_mesh_back.getSizeDx(),
            size_dy=model_mesh_back.getSizeDy(),
            size_element=self.mesh.ele_size(),
            nodes=model_mesh_back.getNodes(),
            elements=model_mesh_back.getElements(),
            nodes_boundary_top=model_mesh_back.getBoundaryNodes()[0],
            nodes_boundary_bottom=model_mesh_back.getBoundaryNodes()[1],
            nodes_boundary_left=model_mesh_back.getBoundaryNodes()[2],
            nodes_boundary_right=model_mesh_back.getBoundaryNodes()[3]  
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
            epspxx=epspxx.min(),
            epspyy=epspyy.min(),
            epspxy=epspxy.min(),
            epsexx=epsexx.min(),
            epseyy=epseyy.min(),
            epsexy=epsexy.min(),            
            velxy=velxy.min(),
            velxx=velxx.min(),
            velyy=velyy.min(),
            desplxx=desplxx.min(),
            desplyy=desplyy.min(),
            desplxy=desplxy.min(),
            eqplas=eqplas.min()
        )
        self.model_result.updateResultMax(
            corx=corX.max(),
            cory=corY.max(),
            sigxx=sigxx.max(),
            sigyy=sigyy.max(),
            sigxy=sigxy.max(),
            epspxx=epspxx.max(),
            epspyy=epspyy.max(),
            epspxy=epspxy.max(),
            epsexx=epsexx.max(),
            epseyy=epseyy.max(),
            epsexy=epsexy.max(),
            velxy=velxy.max(),
            velxx=velxx.max(),
            velyy=velyy.max(),
            desplxx=desplxx.max(),
            desplyy=desplyy.max(),
            desplxy=desplxy.max(),
            eqplas=eqplas.max()
            
        )
        

                
        for node in range(len(corX)):
            self.model_result.addResultNode(
                id_result_node=node+1, 
                material_node=self.__mp_property[node],
                corx=corX.tolist()[node],
                cory=corY.tolist()[node],
                sigxx=sigxx.tolist()[node],
                sigyy=sigyy.tolist()[node],
                sigxy=sigxy.tolist()[node],
                epsexx=epsexx.tolist()[node],
                epseyy=epseyy.tolist()[node],
                epsexy=epsexy.tolist()[node],
                epspxx=epspxx.tolist()[node],
                epspyy=epspyy.tolist()[node],
                epspxy=epspxy.tolist()[node],
                velxy=velxy.tolist()[node],
                velxx=velxx.tolist()[node],
                velyy=velyy.tolist()[node],
                desplxx=desplxx.tolist()[node],
                desplyy=desplyy.tolist()[node],
                desplxy=desplxy.tolist()[node],
                eqplas=eqplas.tolist()[node]
            )
        
        self.model_result.updateResult()
        return True
    

    
    def save_results_excel(self, corX, corY, sigyy):
        #guardar en un archivo excel corX, corY, sigyy con pandas
        path = "D:/Programacion/Tesis UNAL Geotecnia/2 Software/MPM-UN/test/3  archivos _mpm 2404\EXCEL/"
        name = "resultados_CE.xlsx"
        with pd.ExcelWriter(path + name) as writer:
            df = pd.DataFrame(corX)
            df.to_excel(writer, sheet_name='corX')
            df = pd.DataFrame(corY)
            df.to_excel(writer, sheet_name='corY')
            df = pd.DataFrame(sigyy)
            df.to_excel(writer, sheet_name='sigyy')
        return
        # abrir archivo
        #import subprocess
        #subprocess.Popen([path_data], shell=True)
    


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

              
        print("este es el mismo metodo que el de controller menu excecute linea 466 ")
        
        result = {}
        for point in material_points:
            for i, element in enumerate(elements):
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