
from motorMPM.mesh import create_uniform, contour_fixe, setup_MP,search_MP
from motorMPM.mesh import traction_forces,boundary_particles
from motorMPM.explicit2 import deltatime,deltatime2, particles_to_nodes, BC_Dirichlet_momentum
from motorMPM.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel, nodes_to_particle_stress
from motorMPM.graphics import graphic_button,graphic_button2,graphic_button3,graphic_button4, graphic_video2,graphic_gif
from models.model_ProjectCurrent import ModelProjectCurrent
from models.model_Result import ModelResult
from PySide6.QtWidgets import QApplication
import numpy as np
import time as tm
import math
import time

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
        # Condiciones iniciales
        self.__ic_dampfac = None
        self.__ic_gravity = None
        self.__ic_vel_ini_x = None
        self.__ic_vel_ini_y = None
        
        # Malla de fondo
        self.__mb_cor = None
        self.__mb_inci = None
        self.__mb_ele_size = None
        self.__mb_nelex = None

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
        
        
        

        
        
    def runViga(self):        
        response = self.initConditions()
        response = self.initMeshBack()
        response = self.initBoundary()
        response = self.initMaterialPoint()
        response = self.initProperties()
        response = self.initVerctorAndMatrix()
        response = self.initBoundaryParticles()        
        response = self.executeAnalysisViga()       
        if response: 
            response = self.saveResults()        
        return response

    
    def initConditions(self):
        self.__ic_dampfac = self.model_current_project.getDampfac()
        self.__ic_gravity = self.model_current_project.getGravity()
        print("self.__ic_gravity", self.__ic_gravity)
      
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
        
        #variables
        self.__mb_cor = np.asarray(cor)
        self.__mb_inci = np.asarray(inci)
        self.__mb_ele_size = ele_size
        self.__mb_nelex = np.asarray(int(dx_size/ele_size))
                
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
        mp_elem=[]
        mp_xp=[]
        mp_volumes=[]
        mp_velocities=[]
        mp_forces=[]
                
        for id_material_point in list_point_material:
            model_material_point = models_material_point[id_material_point]
            points = model_material_point.getPoints()
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
                vol = points[point]['VOLUME']
                mp_volumes.append(vol)
                vel = points[point]['VELOCITY']
                mp_velocities.append([vel['X'], vel['Y']])
                force = points[point]['FORCE']
                mp_forces.append([force['X'], force['Y']])
                
                    
        #variables
        self.__mp_mp_elem = np.asarray(mp_elem)
        self.__mp_xp = np.asarray(mp_xp)
        self.__mp_active_elem = np.unique(self.__mp_mp_elem[:, 0])
        self.__mp_nmp = len(self.__mp_mp_elem)
        '''
        print("self.__mp_mp_elem", self.__mp_mp_elem)
        print("self.__mp_xp", self.__mp_xp)
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
                                angle_dilatancy / 180*math.pi])
                mp_density.append(density/1000)
                
        #variables
        Prop = np.asarray(mp_prop)
        self.__mp_prop = Prop
        self.DENSITY = mp_density
          
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
        tp=np.zeros((nmp, 2))
        
        
        # variables
        
        self.__vm_Fp = Fp
        self.__vm_sig = sig
        self.__vm_epse = epse
        self.__vm_epsp = epsp
        self.__vm_vp = vp
        self.__vm_bp = bp
        self.__vm_tp = tp
        '''
        print("self.__vm_Fp", self.__vm_Fp)
        print("self.__vm_sig", self.__vm_sig)
        print("self.__vm_epse", self.__vm_epse)
        print("self.__vm_epsp", self.__vm_epsp)
        print("self.__vm_vp", self.__vm_vp)
        print("self.__vm_bp", self.__vm_bp)
        print("self.__vm_tp", self.__vm_tp)
        print("self.__vm_bp", self.__vm_bp)
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
    
    def executeAnalysisViga(self):
        
        
        
        # variables necesarias
        analysis_dialog = self.analysis_dialog
        
        list_time_graphic = self.__tm_list_time_graphic
        list_time =         self.__tm_list_time
        steps_time =        self.__tm_steps_time
        dt_time =           self.__tm_dt_time
        
        # mesh back
        ele_size = self.__mb_ele_size
        nelex = self.__mb_nelex
        inci = self.__mb_inci
        cor = self.__mb_cor
        
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
        tp = self.__vm_tp
        
        
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

        print("dampfac", dampfac)
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
        self.__rs_epsxx = epsxx
        self.__rs_epsyy = epsyy
        self.__rs_epsxy = epsxy
        self.__rs_velx = velx
        self.__rs_vely = vely
        
        
        
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
        epsxx = self.__rs_epsxx
        epsyy = self.__rs_epsyy
        epsxy = self.__rs_epsxy
        velx = self.__rs_velx
        vely = self.__rs_vely
        
        ########################################################################
        #                           analisis finalizado
        ########################################################################        
        self.model_result.clearResult()        
        
        self.model_result.updateResultDataBase(
            gravity= self.__ic_gravity,
            dampfac=  self.__ic_dampfac
        )
        
        print(list_point_material)
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
            size_element=self.__mb_ele_size,
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
                epsxy=epsxy.tolist()[node],
                velx=velx.tolist()[node],
                vely=vely.tolist()[node]
            )
        
        self.model_result.updateResult()
        return True
    
    


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