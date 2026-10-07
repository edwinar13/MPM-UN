
from motorMPM.mesh import search_MP, boundary_particles3, node_conectivity
from models.model_analysis_config import AnalysisConfig, StageType, stage_use_gauss
from models.analysis_utils import compute_min_dt, build_time_arrays
from motorMPM.explicit2 import particles_to_nodes, BC_Dirichlet_momentum, particles_to_nodes_gauss2
from motorMPM.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel, nodes_to_particle_stress2, static_convergence, nodes_to_particle_stress_gauss
from motorMPM.explicit2 import BC_Dirichlet_momentum3, contact2
from motorMPM.dos_fases import (deltatime_two_phases_CFL, particles_to_nodes_two_phases,
                                nodes_to_particle_vel_two_phases, nodes_to_particle_xp_two_phases,
                                BC_Dirichlet_acele_force_two_phases, BC_Dirichlet_vel_two_phases,
                                nodes_to_particle_stress_MP_and_pore_pressure_SRI_k_act_NUMBA)
from models.model_ProjectCurrent import ModelProjectCurrent
from models.model_Result import ModelResult
#from controllers.draw.controller_MenuExecute import AnalysisProgressDialog
from PySide6.QtWidgets import QApplication
import numpy as np
import time as tm
import math
import time
import os
import json
from datetime import datetime

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
    # Densidad del agua (Mg/m³) en la etapa de consolidación
    RHO_W = 1.0

    def __init__(self, analysis_dialog, model_current_project: ModelProjectCurrent, model_result:ModelResult,
                 dataTime, list_boundaries, list_point_material, 
                dt_time, list_time ,steps_time,
                dt_graphic, list_time_graphic, steps_time_graphic,
                analysis_config: AnalysisConfig = None):
        
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
        
        # Configuración de análisis genérica (FASE 2)
        self.analysis_config = analysis_config

        # Etapa en curso (para los mensajes de progreso)
        self.__stage_index = 0
        self.__n_stages = 1

        # Resultados acumulados por etapa (ver _append_stage_results)
        self.__rs_stages = []
        self.__rs_stages_frames = []
        # True si el usuario canceló pero se alcanzó a guardar algo
        self.cancelled_partial = False
        # Motivo del fallo, para que el controlador lo muestre
        self.error_message = ""
         
        #===========  variables  ===========

        # Condiciones iniciales
        self.__ic_gravity = None
        
        # Restricciones
        self.__bo_fixed_nodesX = None
        self.__bo_fixed_nodesY = None
        
        # Puntos materiales
        self.__mp_mp_elem = None
        self.__mp_xp = None
        self.__mp_active_elem = None
        self.__mp_nmp = None
        # Cuerpos: un grupo de puntos materiales = un rango [start, end) de
        # los arrays de partículas (ver initMaterialPoint). Los arrays siguen
        # siendo uno solo; un cuerpo es una vista sobre ellos.
        self.__bodies = []
        self.__node_support = None

        # Vertor and matrix
        self.__vm_Fp = None
        self.__vm_sig = None
        self.__vm_epse = None
        self.__vm_epsp = None
        self.__vm_vp = None
        self.__vm_bp = None
        self.__vm_bp0 = None
        self.__vm_tp0 = None

        # Doble fase (etapa de consolidación, docs/plan_dos_fases_ui.md).
        # None hasta la primera etapa de consolidación, que los crea.
        self.__vm_wp = None    # velocidad del agua (nmp, 2)
        self.__vm_pp = None    # presión de poros (nmp, 3), compresión < 0 (σ = σ' + pp)
        self.__vm_np = None    # porosidad (nmp,)
        self.__vm_kp = None    # permeabilidad (nmp,)
        self.__two_phase = None  # (n0, k0, Kw) del material de la etapa en curso

        self.mesh = None
        self.initMeshBack()
        
        
        
    # ===================================================================
    #  Ejecución
    # ===================================================================
    def run(self):
        """Inicializa el modelo, corre todas las etapas de
        self.analysis_config y guarda los resultados."""
        config = self.analysis_config
        if config is None:
            self.error_message = "No hay configuración de análisis (etapas)."
            print(f"[ERROR] {self.error_message}")
            return False

        print(f"[MPM-UN] run() con config: {config.analysis_type.value}")

        self.__rs_stages = []
        self.cancelled_partial = False
        self.error_message = ""

        # Pipeline de inicialización (genérico, no cambia)
        self.initConditions()
        self.initBoundary()
        self.initMaterialPoint()
        self.initProperties()
        self.initVerctorAndMatrix()
        self.initBoundaryParticles()

        # Ejecutar según tipo de análisis
        response = self.execute(config)

        if not response and self.__rs_stages:
            # Cancelado a mitad de camino pero hay etapas (o parte de una)
            # ya calculadas: se guardan en vez de perderse.
            print(f"[MPM-UN] Cancelado: se guardan {len(self.__rs_stages)} bloque(s) de resultados")
            self.cancelled_partial = True
            response = True

        if response:
            if not self.__rs_stages:
                print("[MPM-UN] No hay resultados que guardar")
                return False
            self._finalize_results()
            response = self.saveResults()
        return response
    
    def execute(self, config: AnalysisConfig):
        """Ejecuta el análisis recorriendo TODAS las etapas de config.

        Entre una etapa y la siguiente pasa el estado físico
        (esfuerzos, posiciones, deformaciones...) con _capture_state /
        _inject_state. Una sola etapa = una sola vuelta sin inyección,
        idéntico al comportamiento anterior.
        """
        n_stages = len(config.stages)
        self.__n_stages = n_stages

        prev_state = None
        prev_stage = None
        start_index = 0

        # Validar TODAS las etapas antes de correr la primera: un error de
        # configuración en la etapa 2 no debe descubrirse tras horas de la 1.
        models_property = self.model_current_project.getModelsProperties()
        for index, stage in enumerate(config.stages):
            targets = self._stage_materials(config, index)
            missing = [t for t in targets if t not in models_property]
            if missing:
                msg = (f"Etapa '{stage.name or stage.stage_type.value}': cambia a un "
                       f"material que ya no existe en el proyecto.")
            else:
                flags = [stage.plasticity_flag if self._material_row(t)[2] else 0
                         for t in targets]
                msg = self._check_stage_bodies(stage, stage_use_gauss(stage), flags)
                if not msg and stage.stage_type == StageType.CONSOLIDATION:
                    msg = self._check_consolidation(stage, targets)
            if msg:
                self.error_message = msg
                print(f"[ERROR] {msg}")
                return False

        # ── Reanudar desde un checkpoint, si se pidió ──
        resume = int(getattr(config, 'resume_from_stage', 0) or 0)
        if resume >= 2:
            if resume > n_stages:
                self.error_message = (
                    f"Se pidió reanudar en la etapa {resume} pero solo hay {n_stages} etapas.")
                print(f"[ERROR] {self.error_message}")
                return False
            state, meta = self._load_checkpoint(resume - 1)
            if state is None:
                self.error_message = meta  # aquí meta es el mensaje de error
                print(f"[ERROR] {self.error_message}")
                return False
            # No se inyecta aquí: _handoff() lo hace en la primera vuelta del
            # bucle, junto con initBoundaryParticles() y la regla de vp=0.
            prev_state = state
            prev_stage = config.stages[resume - 2]
            start_index = resume - 1
            msg = (f"Reanudando desde el checkpoint de la etapa {resume - 1} "
                   f"({meta.get('fecha', '')})")
            print(f"[RESUME] {msg}")
            self.analysis_dialog.setStatus(False, msg)
            QApplication.processEvents()

        for index in range(start_index, n_stages):
            stage = config.stages[index]
            self.__stage_index = index
            print(f"[EXECUTE] Etapa {index + 1}/{n_stages}: {stage.stage_type.value}")

            # Heredar el estado de la etapa anterior (handoff).
            # En una corrida reanudada, la primera vuelta ya trae el estado
            # del checkpoint: solo falta la regla de vp=0 al entrar a dinámica.
            if prev_state is not None:
                self._handoff(prev_state, prev_stage, stage)

            # Material vigente de cada cuerpo (antes del dt, que depende de él)
            self._apply_stage_materials(config, index)
            if stage.stage_type == StageType.CONSOLIDATION:
                self._enter_consolidation(config, index, stage)

            # Configurar dt y arrays de tiempo de ESTA etapa (según su Courant)
            self._prepare_stage_time(stage)

            ok = self._dispatch_stage(config, stage)
            if not ok:
                return False

            # Tomar la 'foto' del estado para entregarla a la etapa siguiente
            prev_state = self._capture_state()
            prev_stage = stage
            self._save_checkpoint(index + 1, stage, prev_state)

        return True

    def _stage_label(self, stage):
        """Prefijo 'Etapa i/n — nombre' para los mensajes de progreso."""
        name = stage.name or stage.stage_type.value
        return f"Etapa {self.__stage_index + 1}/{self.__n_stages} — {name}"

    def _dispatch_stage(self, config: AnalysisConfig, stage):
        """Despacha UNA etapa a su bucle según el tipo."""
        if stage.stage_type == StageType.DYNAMIC:
            return self._run_dynamic_loop(config, stage)
        elif stage.stage_type == StageType.LOAD_INCREMENT:
            return self._run_quasi_static_increment_loop(config, stage)
        elif stage.stage_type == StageType.GEOSTATIC:
            return self._run_quasi_static_increment_loop(config, stage)
        elif stage.stage_type == StageType.CONSOLIDATION:
            # Avanza en el tiempo igual que la dinámica; cambia el paso (doble fase)
            return self._run_dynamic_loop(config, stage)
        else:
            print(f"[ERROR] Tipo de etapa no soportado: {stage.stage_type}")
            return False

    def _prepare_stage_time(self, stage):
        """Calcula el dt de ESTA etapa (según su Courant y los materiales
        presentes) y, para etapas dinámicas, reconstruye los arrays de
        tiempo a partir de la duración de la etapa. Los loops cuasi-estáticos
        solo usan el dt (sus 'pasos' son los incrementos)."""
        ele_size = self.mesh.ele_size()
        # Materiales únicos presentes: (E, nu, rho[Mg/m³])
        mat = np.column_stack((self.__mp_prop[:, 0], self.__mp_prop[:, 1], self.__vm_rhop))
        uniq = np.unique(mat, axis=0)
        materials = [(float(r[0]), float(r[1]), float(r[2])) for r in uniq]
        dt, cp, _ = compute_min_dt(materials, ele_size, stage.courant_number)
        if dt is None:
            raise RuntimeError("No se pudo calcular dt: la etapa no tiene materiales")
        if stage.stage_type == StageType.CONSOLIDATION:
            # Onda de compresión no drenada (domina Kw/n0): mucho más rápida
            # que la del esqueleto. Misma función que el script de validación.
            n0, _, kw = self.__two_phase
            rho_sat = self.__vm_rhop + n0 * self.RHO_W   # ρd + n0·ρw
            dt = deltatime_two_phases_CFL(self.__mp_prop[:, 0], self.__mp_prop[:, 1],
                                          rho_sat, ele_size, stage.courant_number, kw, n0)
        self.__tm_dt_time = dt

        if stage.stage_type in (StageType.DYNAMIC, StageType.CONSOLIDATION):
            fps = 30
            if isinstance(self.__tm_dataTime, dict):
                fps = self.__tm_dataTime.get('fps', 30)
            ta = build_time_arrays(dt, stage.analysis_time, fps)
            self.__tm_list_time = ta['tiempo']
            self.__tm_list_time_graphic = ta['tiempographic']
            self.__tm_dt_graphic = ta['dt_graphic']
            self.__tm_steps_time = ta['steps']
            self.__tm_steps_time_graphic = ta['steps_graphic']

        print(f"[STAGE TIME] {stage.stage_type.value}: courant={stage.courant_number}, dt={dt:.3e}")

    def _run_one_mpm_step(self, use_gauss, plasticity_flags):
        """Ejecuta UN paso del MPM: particles→nodes→BC→nodes→particles.

        Este es el corazón del MPM que no cambia nunca.
        Retorna las variables actualizadas.

        Un solo campo de velocidad para todos los grupos (interfaz adherida).

        Args:
            use_gauss: Si True, usa particles_to_nodes_gauss2 y nodes_to_particle_stress_gauss.
            plasticity_flags: flag de plasticidad (0 o 1) de cada cuerpo, ver
                _body_plasticity_flags(). Si todos coinciden, el esfuerzo se
                actualiza en una sola llamada, exactamente como antes.
        """
        # Referencias locales
        xp = self.__mp_xp
        vp = self.__vm_vp
        Vp = self.__vm_Vp
        Vp0 = self.__vm_Vp0
        Mp = self.__vm_Mp
        sig = self.__vm_sig
        bp = self.__vm_bp
        tp = self.__vm_tp_current  # tp actual (puede cambiar por incremento)
        Fp = self.__vm_Fp
        epse = self.__vm_epse
        epsp = self.__vm_epsp
        Prop = self.__mp_prop
        mp_elem = self.__mp_mp_elem
        fixed_nodesX = self.__bo_fixed_nodesX
        fixed_nodesY = self.__bo_fixed_nodesY
        dampfac = self.__step_dampfac
        dtime = self.__tm_dt_time
        bound_val = self.__bo_bound_val


        
        # 1 → Buscar elementos activos
        mp_elem, active_elem = search_MP(mp_elem, xp, self.mesh.ele_size(), self.mesh.nelex())
        active_nodes = np.unique(self.mesh.inci()[active_elem - 1, :])
        

        
        # 2 → Transferir partículas a nodos
        grid = self.mesh.inci(), self.mesh.cor(), active_elem, active_nodes, mp_elem
        particle = xp, vp, Vp, Mp, sig, bp, tp

        if use_gauss:
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes_gauss2(grid, particle, bound_val)
        else:
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)

        # 3 → Solución sistema de ecuaciones nodales (EXPLÍCITO)
        nforce = niforce + neforce
        ndamping = -dampfac * np.multiply(np.absolute(nforce), np.sign(nmomentum))
        nforce = nforce + ndamping
        nmomentum += nforce * dtime

        # 4 → Condiciones de contorno Dirichlet
        nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(
            active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce, niforce, neforce)

        # 5 → Transferir nodos a partículas: velocidad y posición
        nquantities = nmass, nmomentum, nforce
        particle = xp, vp, Vp, Mp, sig, shfnp

        xp, vp, nvel = nodes_to_particle_vel(grid, particle, nquantities, dtime)
        nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel)
        
        # 6 → Transferir nodos a partículas: esfuerzo y deformación
        # Flag de plasticidad: 0 = elástico lineal, 1 = elastoplástico (Mohr-Coulomb)
        particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop

        if len(set(plasticity_flags)) == 1:
            plasticity_flag = plasticity_flags[0]
            if use_gauss:
                # La variante gauss ya sub-incrementa la plasticidad (deps/10).
                Fp, Vp, epse, epsp, sig = nodes_to_particle_stress_gauss(
                    grid, particle, bound_val, nvel, dtime, plasticity_flag)
            else:
                # stress2 = misma rama elástica que nodes_to_particle_stress, pero
                # la rama plástica siempre usa 10 sub-incrementos de deformación.
                # Es la que emplea el script de referencia talud_2021_v2.py (l. 689-693).
                Fp, Vp, epse, epsp, sig = nodes_to_particle_stress2(
                    grid, particle, nvel, dtime, plasticity_flag)
        else:
            # Cuerpos con distinto flag (un material elástico junto a uno
            # Mohr-Coulomb en una etapa plástica). stress2 actualiza cada
            # partícula por separado, así que llamarla por cuerpo da lo mismo
            # que una sola llamada, pero con el flag de cada uno. La variante
            # gauss promedia por elemento entre partículas: no se puede partir
            # así (se valida antes de la etapa, ver _check_stage_bodies).
            for body, flag in zip(self.__bodies, plasticity_flags):
                s = slice(body['start'], body['end'])
                grid_b = grid[0], grid[1], grid[2], grid[3], mp_elem[s]
                particle_b = Fp[s], Vp[s], Vp0[s], epse[s], epsp[s], sig[s], shfnp[s], Prop[s]
                Fp[s], Vp[s], epse[s], epsp[s], sig[s] = nodes_to_particle_stress2(
                    grid_b, particle_b, nvel, dtime, flag)

        # Actualizar variables de instancia
        self.__mp_xp = xp
        self.__vm_vp = vp
        self.__vm_Vp = Vp
        self.__vm_Fp = Fp
        self.__vm_sig = sig
        self.__vm_epse = epse
        self.__vm_epsp = epsp
        self.__mp_mp_elem = mp_elem


        return nmass, niforce, neforce, nvel

    # ===================================================================
    #  Varios cuerpos con contacto (FASE B, docs/plan_fase_b.md)
    # ===================================================================
    def _body_plasticity_flags(self, stage):
        """Flag de plasticidad de cada cuerpo en esta etapa.

        Plastifica si el material es Mohr-Coulomb Y la etapa lo permite: el
        material dice si PUEDE plastificar, la etapa si se permite AHORA.
        """
        return [stage.plasticity_flag if body['plastic'] else 0
                for body in self.__bodies]

    def _check_stage_bodies(self, stage, use_gauss, flags):
        """Combinaciones que el motor todavía no resuelve. Devuelve un
        mensaje de error, o '' si la etapa se puede correr."""
        name = stage.name or stage.stage_type.value
        if use_gauss and len(set(flags)) > 1:
            return (f"Etapa '{name}': hay materiales elásticos y Mohr-Coulomb con "
                    f"integración gauss. Esa combinación aún no está soportada; "
                    f"usa una etapa sin gauss o sin plasticidad.")
        if stage.multi_body:
            if stage.stage_type != StageType.DYNAMIC or use_gauss:
                return (f"Etapa '{name}': el contacto entre cuerpos solo está "
                        f"disponible en etapas dinámicas sin integración gauss.")
            if len(self.__bodies) != 2:
                return (f"Etapa '{name}': el contacto entre cuerpos funciona por ahora "
                        f"con exactamente 2 grupos de puntos materiales "
                        f"(hay {len(self.__bodies)}).")
        return ""

    def _run_one_mpm_step_multibody(self, plasticity_flags, mu, normals='fija_y'):
        """Un paso con un campo de velocidad por cuerpo y contacto friccional.

        Mismo orden de operaciones que la fase de falla de la referencia
        (talud_2021_v2.py, l. 616-693):
          search_MP por cuerpo → malla activa del SISTEMA
          particles_to_nodes por cuerpo → predictor por cuerpo
          campo del sistema → contact2 (corrector)
          fuerza = Δmomentum/dt → Dirichlet por cuerpo → nodos→partículas.

        Cada cuerpo trabaja sobre vistas (rangos) de los arrays de partículas,
        así que los resultados se escriben en su sitio.
        """
        inci, cor = self.mesh.inci(), self.mesh.cor()
        ele_size, nelex = self.mesh.ele_size(), self.mesh.nelex()
        fixed_nodesX = self.__bo_fixed_nodesX
        fixed_nodesY = self.__bo_fixed_nodesY
        dampfac = self.__step_dampfac
        dtime = self.__tm_dt_time
        if self.__node_support is None:
            self.__node_support = self.mesh.nodeSupport()

        xp, vp, Vp, Vp0, Mp = (self.__mp_xp, self.__vm_vp, self.__vm_Vp,
                               self.__vm_Vp0, self.__vm_Mp)
        sig, bp, tp = self.__vm_sig, self.__vm_bp, self.__vm_tp_current
        Fp, epse, epsp, Prop = (self.__vm_Fp, self.__vm_epse,
                                self.__vm_epsp, self.__mp_prop)
        slices = [slice(b['start'], b['end']) for b in self.__bodies]

        # --- elementos y nodos activos: por cuerpo y del sistema ---
        mp_elem_b, active_elem_b = [], []
        for s in slices:
            m, a = search_MP(self.__mp_mp_elem[s], xp[s], ele_size, nelex)
            mp_elem_b.append(m)
            active_elem_b.append(a)
        active_elem = np.unique(np.concatenate(active_elem_b, axis=0))
        active_nodes_b = [np.unique(inci[a - 1, :]) for a in active_elem_b]
        active_nodes = np.unique(inci[active_elem - 1, :])

        # --- partículas → nodos y predictor, por cuerpo ---
        grids, nmass_b, nmomentum_b, nmomentum_bt, shfnp_b = [], [], [], [], []
        for s, m in zip(slices, mp_elem_b):
            grid = inci, cor, active_elem, active_nodes, m
            particle = xp[s], vp[s], Vp[s], Mp[s], sig[s], bp[s], tp[s]
            nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
            nmomentum_t = np.copy(nmomentum)
            ndamping = -dampfac*np.multiply(np.absolute(niforce + neforce), np.sign(nmomentum))
            nforce = niforce + neforce + ndamping
            nmomentum += nforce*dtime
            grids.append(grid)
            nmass_b.append(nmass)
            nmomentum_b.append(nmomentum)
            nmomentum_bt.append(nmomentum_t)
            shfnp_b.append(shfnp)

        # --- campo del sistema y corrector de contacto ---
        nmassS = nmass_b[0] + nmass_b[1]
        nmomentumS = nmomentum_b[0] + nmomentum_b[1]
        mesh = inci, cor, self.__node_support, active_nodes
        bodies = [
            (nmass_b[k], nmomentum_b[k], active_elem_b[k], active_nodes_b[k],
             mp_elem_b[k], Mp[slices[k]], xp[slices[k]]) for k in (0, 1)]
        nmomentum_b = contact2(bodies, nmassS, nmomentumS, mesh, dtime, mu,
                               normales=normals)

        # --- nodos → partículas, por cuerpo ---
        for k, s in enumerate(slices):
            nforce = 1 / dtime * (nmomentum_b[k] - nmomentum_bt[k])
            nmomentum, nforce = BC_Dirichlet_momentum3(
                active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_b[k], nforce)
            nquantities = nmass_b[k], nmomentum, nforce
            particle = xp[s], vp[s], Vp[s], Mp[s], sig[s], shfnp_b[k]
            xp[s], vp[s], nvel = nodes_to_particle_vel(grids[k], particle, nquantities, dtime)
            nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel)

            particle = Fp[s], Vp[s], Vp0[s], epse[s], epsp[s], sig[s], shfnp_b[k], Prop[s]
            Fp[s], Vp[s], epse[s], epsp[s], sig[s] = nodes_to_particle_stress2(
                grids[k], particle, nvel, dtime, plasticity_flags[k])
            self.__mp_mp_elem[s] = mp_elem_b[k]

    # ===================================================================
    #  Consolidación: doble fase v-w (docs/plan_dos_fases_ui.md)
    # ===================================================================
    def _two_phase_params(self, id_material):
        """(n0, k [m/s], Kw [kPa]) de un material; ceros si no los tiene."""
        data = self.model_current_project.getModelsProperties()[id_material].getData()
        mat = data[list(data.keys())[0]]
        return (float(mat.get('POROSIDAD', 0.0) or 0.0),
                float(mat.get('PERMEABILIDAD', 0.0) or 0.0),
                float(mat.get('MODULOAGUA', 0.0) or 0.0))

    def _check_consolidation(self, stage, targets):
        """Lo que la etapa de consolidación necesita. Devuelve un mensaje de
        error, o '' si se puede correr."""
        name = stage.name or stage.stage_type.value
        if stage.multi_body:
            return f"Etapa '{name}': la consolidación no admite contacto entre cuerpos."
        if len(set(targets)) > 1:
            # La función SRI de la referencia usa n0, k0 y Kw escalares
            return (f"Etapa '{name}': la consolidación funciona por ahora con un solo "
                    f"material para todos los grupos de puntos materiales.")
        n0, k, kw = self._two_phase_params(targets[0])
        if not (0.0 < n0 < 1.0 and k > 0.0 and kw > 0.0):
            return (f"Etapa '{name}': el material necesita porosidad (entre 0 y 1), "
                    f"permeabilidad y módulo volumétrico del agua mayores que cero.")
        return ""

    def _enter_consolidation(self, config, index, stage):
        """Fija los parámetros de doble fase de la etapa y, si es la primera
        de consolidación, crea el estado del agua.

        Condición inicial (como la referencia, caso 7.1): presión de poros
        uniforme p0 = PRESIONPOROSINICIAL, velocidad del agua igual a la del
        esqueleto, porosidad y permeabilidad iniciales del material. Una etapa
        de consolidación posterior hereda el estado del agua sin tocarlo.
        """
        target = self._stage_materials(config, index)[0]
        n0, k0, kw = self._two_phase_params(target)
        self.__two_phase = (n0, k0, kw)
        if self.__vm_pp is not None:
            print("[CONSOLIDACIÓN] se conserva la presión de poros de la etapa anterior")
            return
        nmp = self.__mp_nmp
        self.__vm_np = np.full(nmp, n0)
        self.__vm_kp = np.full(nmp, k0)
        self.__vm_wp = np.copy(self.__vm_vp)
        self.__vm_pp = np.full((nmp, 3), -float(stage.initial_pore_pressure))
        print(f"[CONSOLIDACIÓN] n0={n0}, k={k0} m/s, Kw={kw} kPa, "
              f"p0={stage.initial_pore_pressure} kPa")

    def _run_one_mpm_step_two_phase(self, plasticity_flag):
        """Un paso del MPM de doble fase y único punto (formulación v-w).

        Algoritmo 2 de Caro González (2024), igual que
        tools/experimentos/consolidacion_1d.py (validado contra Terzaghi):
        partículas→nodos de las dos fases, ecuación nodal del agua y de la
        mezcla con amortiguamiento local, Dirichlet en aceleraciones,
        velocidades (MUSL), posiciones, esfuerzo efectivo en partículas y
        presión de poros con SRI.

        Drenaje: la velocidad del agua se restringe en los mismos nodos que la
        del esqueleto (contorno restringido = impermeable); una superficie
        libre drena (p = 0 en forma débil).
        """
        inci, cor = self.mesh.inci(), self.mesh.cor()
        fixed_nodesX = self.__bo_fixed_nodesX
        fixed_nodesY = self.__bo_fixed_nodesY
        alpha = self.__step_dampfac
        dtime = self.__tm_dt_time
        n0, k0, kw = self.__two_phase
        rho_w = self.RHO_W

        xp, vp, wp = self.__mp_xp, self.__vm_vp, self.__vm_wp
        Vp, Vp0 = self.__vm_Vp, self.__vm_Vp0
        sig_e, pp = self.__vm_sig, self.__vm_pp
        n_p, k_p = self.__vm_np, self.__vm_kp
        bp, tp = self.__vm_bp, self.__vm_tp_current
        Fp, epse, epsp, Prop = self.__vm_Fp, self.__vm_epse, self.__vm_epsp, self.__mp_prop
        Mp_s0 = self.__vm_Mp                      # ρd·Vp0: masa de sólidos, constante
        nmp = self.__mp_nmp

        # 1 → elementos y nodos activos
        mp_elem, active_elem = search_MP(self.__mp_mp_elem, xp, self.mesh.ele_size(), self.mesh.nelex())
        active_nodes = np.unique(inci[active_elem - 1, :])
        grid = inci, cor, active_elem, active_nodes, mp_elem

        # 2 → partículas a nodos; masa del agua según la porosidad actual
        Mp_w = n_p * rho_w * Vp
        Mp_weq = rho_w * Vp
        Mp = Mp_w + Mp_s0
        sig_t = np.copy(sig_e)
        sig_t[:, :2] += pp[:, :2]
        pb_p = np.zeros((nmp, 2))                 # presión prescrita en el contorno: 0
        particle = (xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, Mp_weq, sig_t, sig_e, pp,
                    bp, tp, pb_p, n_p, k_p, rho_w)
        (nmass_s, nmass_w, nmass_weq, nmass, nmom_s, nmom_w, niforce_w, neforce_w,
         ndforce_w, neforce_m, niforce_m, shfnp) = particles_to_nodes_two_phases(grid, particle)

        # 3 → ecuación nodal con amortiguamiento local (Ec. 5-28, 5-29)
        fw = niforce_w + neforce_w
        fm = niforce_m + neforce_m
        if alpha > 0:
            w_n = np.divide(nmom_w, nmass_w, out=np.zeros_like(nmom_w), where=nmass_w != 0)
            v_n = np.divide(nmom_s, nmass_s, out=np.zeros_like(nmom_s), where=nmass_s != 0)
            damp_w = -alpha * np.abs(fw) * np.sign(w_n)
            damp_s = -alpha * np.abs(fm - fw) * np.sign(v_n)
        else:
            damp_w = damp_s = 0.0
        nforce_w = fw + ndforce_w + damp_w
        nforce_m = fm + damp_s + damp_w
        nacele_w = nforce_w / nmass_weq
        nacele_s = (nforce_m - nmass_w * nacele_w) / nmass_s

        # 4 → Dirichlet en aceleraciones (las dos fases)
        nq = (nacele_w, nacele_s, nforce_w, niforce_w, neforce_w, ndforce_w,
              nforce_m, neforce_m, niforce_m)
        nacele_s, nacele_w = BC_Dirichlet_acele_force_two_phases(
            active_nodes, fixed_nodesX, fixed_nodesY, nq)[:2]

        # 5 → velocidades de partículas y nodales (MUSL), posiciones
        vp, wp, nvel_s, nvel_w = nodes_to_particle_vel_two_phases(
            grid, (xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, shfnp),
            (nacele_w, nacele_s, nmass, nmass_w, nmass_s, nmass_weq), dtime)
        nvel_s, nvel_w = BC_Dirichlet_vel_two_phases(
            active_nodes, fixed_nodesX, fixed_nodesY, nvel_s, nvel_w)
        xp = nodes_to_particle_xp_two_phases(xp, nvel_s, grid, shfnp, dtime)

        # 6 → esfuerzo efectivo, presión de poros (SRI) y porosidad
        bound_val = np.zeros(nmp, dtype=np.int64)  # no lo usa la función SRI
        Fp, Vp, epse, epsp, sig_e, pp, n_p, k_p = \
            nodes_to_particle_stress_MP_and_pore_pressure_SRI_k_act_NUMBA(
                grid, (Fp, Vp, Vp0, n_p, np.full(nmp, n0), k_p, k0, n0, epse, epsp,
                       sig_e, sig_t, pp, shfnp, Prop),
                bound_val, nvel_s, nvel_w, dtime, plasticity_flag, kw)

        self.__mp_xp = xp
        self.__vm_vp, self.__vm_wp = vp, wp
        self.__vm_Vp, self.__vm_Fp = Vp, Fp
        self.__vm_sig, self.__vm_epse, self.__vm_epsp = sig_e, epse, epsp
        self.__vm_pp, self.__vm_np, self.__vm_kp = pp, n_p, k_p
        self.__mp_mp_elem = mp_elem

    # ===================================================================
    #  Handoff de estado entre etapas (FASE A)
    # ===================================================================
    def _capture_state(self):
        """Toma una 'foto' del estado físico actual de las partículas.

        Empaqueta (con copia) las variables que evolucionan durante una
        etapa, para entregarlas como condición inicial de la etapa
        siguiente (p.ej. handoff geoestático → falla).
        """
        state = {
            'xp': np.copy(self.__mp_xp),
            'vp': np.copy(self.__vm_vp),
            'Vp': np.copy(self.__vm_Vp),
            'Fp': np.copy(self.__vm_Fp),
            'sig': np.copy(self.__vm_sig),
            'epse': np.copy(self.__vm_epse),
            'epsp': np.copy(self.__vm_epsp),
            'mp_elem': np.copy(self.__mp_mp_elem),
            # bp: fuerza de cuerpo alcanzada al final de la etapa (una rampa
            # de gravedad interrumpida la deja parcial). Necesaria para que un
            # checkpoint reanude con la misma gravedad que tenía.
            'bp': np.copy(self.__vm_bp),
        }
        # Estado del agua: solo existe desde la primera etapa de consolidación
        if self.__vm_pp is not None:
            state.update(wp=np.copy(self.__vm_wp), pp=np.copy(self.__vm_pp),
                         n_p=np.copy(self.__vm_np), k_p=np.copy(self.__vm_kp))
        return state

    def _inject_state(self, state):
        """Pega un estado (de _capture_state) sobre las variables de
        instancia, para que la etapa actual arranque desde ese estado
        en lugar de desde cero."""
        self.__mp_xp = np.copy(state['xp'])
        self.__vm_vp = np.copy(state['vp'])
        self.__vm_Vp = np.copy(state['Vp'])
        self.__vm_Fp = np.copy(state['Fp'])
        self.__vm_sig = np.copy(state['sig'])
        self.__vm_epse = np.copy(state['epse'])
        self.__vm_epsp = np.copy(state['epsp'])
        self.__mp_mp_elem = np.copy(state['mp_elem'])
        if 'bp' in state and state['bp'] is not None:
            self.__vm_bp = np.copy(state['bp'])
        if 'pp' in state:
            self.__vm_wp = np.copy(state['wp'])
            self.__vm_pp = np.copy(state['pp'])
            self.__vm_np = np.copy(state['n_p'])
            self.__vm_kp = np.copy(state['k_p'])

    # ===================================================================
    #  Checkpoints por etapa (guardar / reanudar)
    # ===================================================================
    def _save_checkpoint(self, stage_number, stage, state):
        """Guarda el estado al TERMINAR la etapa `stage_number` (1-based).

        Permite reanudar desde la etapa siguiente sin repetir las anteriores
        (p.ej. correr el geostático del talud una vez y luego iterar la falla).
        Mismo espíritu que el .npz de talud_2021_v2.py (l. 372-385).
        """
        try:
            path = self.model_current_project.getCheckpointPath(stage_number)
            os.makedirs(os.path.dirname(path), exist_ok=True)
            np.savez_compressed(
                path,
                nmp=np.int64(self.__mp_nmp),
                ele_size=np.float64(self.mesh.ele_size()),
                stage_index=np.int64(stage_number),
                stage_json=json.dumps(stage.to_dict()),
                fecha=datetime.now().strftime("%Y-%m-%d %H:%M"),
                **state)
            print(f"[CHECKPOINT] guardado: {path}")
            return True
        except BaseException as err:
            # No es fatal: el análisis ya corrió, solo se pierde el atajo
            print(f"[CHECKPOINT] no se pudo guardar la etapa {stage_number}: "
                  f"{type(err).__name__}: {err}")
            return False

    def _load_checkpoint(self, stage_number):
        """Carga el checkpoint de la etapa `stage_number` (1-based).

        Returns:
            (state, meta) o (None, mensaje de error) si no se puede usar.
        """
        path = self.model_current_project.getCheckpointPath(stage_number)
        if not os.path.exists(path):
            return None, f"No existe el checkpoint de la etapa {stage_number}"
        try:
            data = np.load(path, allow_pickle=False)
        except BaseException as err:
            return None, f"No se pudo leer el checkpoint: {type(err).__name__}: {err}"

        # El checkpoint debe corresponder al mismo modelo: si cambió el número
        # de partículas o la malla, los arrays no encajan.
        nmp_ck = int(data['nmp'])
        if nmp_ck != int(self.__mp_nmp):
            return None, (f"El checkpoint tiene {nmp_ck} partículas y el modelo "
                          f"actual {int(self.__mp_nmp)}. Vuelve a correr desde el inicio.")
        ele_ck = float(data['ele_size'])
        ele_now = float(self.mesh.ele_size())
        if abs(ele_ck - ele_now) > 1e-9:
            return None, (f"El checkpoint se hizo con malla de {ele_ck} y la actual "
                          f"es {ele_now}. Vuelve a correr desde el inicio.")

        state = {k: data[k] for k in
                 ('xp', 'vp', 'Vp', 'Fp', 'sig', 'epse', 'epsp', 'mp_elem', 'bp',
                  'wp', 'pp', 'n_p', 'k_p')
                 if k in data.files}
        meta = {
            'fecha': str(data['fecha']) if 'fecha' in data.files else '',
            'stage_json': str(data['stage_json']) if 'stage_json' in data.files else '',
        }
        return state, meta

    def _handoff(self, prev_state, prev_stage, stage):
        """Entrega el estado de la etapa anterior a la etapa `stage`.

        Además de inyectar el estado:
        - recalcula las partículas de frontera con las posiciones nuevas;
        - al entrar a una etapa DINÁMICA desde una cuasi-estática, pone la
          velocidad en cero. La velocidad residual del amortiguamiento
          cuasi-estático no es física: el script de referencia
          talud_2021_v2.py crea `vp` nuevo en cero al iniciar el colapso
          (l. 474) en vez de heredarlo del paso geoestático.
        """
        self._inject_state(prev_state)
        self.initBoundaryParticles()

        if (stage.stage_type in (StageType.DYNAMIC, StageType.CONSOLIDATION) and
                prev_stage is not None and
                prev_stage.stage_type in (StageType.GEOSTATIC, StageType.LOAD_INCREMENT)):
            self.__vm_vp[:] = 0.0
            if self.__vm_wp is not None:
                self.__vm_wp[:] = 0.0
            print(f"[HANDOFF] vp=0 al entrar a la etapa {stage.stage_type.value} "
                  f"(desde {prev_stage.stage_type.value})")

        if stage.reset_strains:
            # Deformaciones a cero; esfuerzos y posiciones se conservan. Con
            # Fp = I el volumen vuelve a Vp0 (Vp = det(Fp)·Vp0).
            self.__vm_Fp[:] = 0.0
            self.__vm_Fp[:, 0] = 1.0
            self.__vm_Fp[:, 3] = 1.0
            self.__vm_epse[:] = 0.0
            self.__vm_epsp[:] = 0.0
            self.__vm_Vp[:] = self.__vm_Vp0
            print("[HANDOFF] deformaciones reiniciadas (Fp = I, eps = 0, Vp = Vp0)")

    def _init_result_arrays(self, n_steps):
        """Inicializa los arrays de resultados para n_steps pasos gráficos."""
        nmp = self.__mp_nmp
        xp = self.__mp_xp
        sig = self.__vm_sig
        epse = self.__vm_epse
        epsp = self.__vm_epsp
        vp = self.__vm_vp
        
        corX = np.zeros((nmp, n_steps))
        corY = np.zeros((nmp, n_steps))
        sigxx = np.zeros((nmp, n_steps))
        sigyy = np.zeros((nmp, n_steps))
        sigxy = np.zeros((nmp, n_steps))
        epsexx = np.zeros((nmp, n_steps))
        epseyy = np.zeros((nmp, n_steps))
        epsexy = np.zeros((nmp, n_steps))
        epspxx = np.zeros((nmp, n_steps))
        epspyy = np.zeros((nmp, n_steps))
        epspxy = np.zeros((nmp, n_steps))
        velxx = np.zeros((nmp, n_steps))
        velyy = np.zeros((nmp, n_steps))
        velxy = np.zeros((nmp, n_steps))
        desplxx = np.zeros((nmp, n_steps))
        desplyy = np.zeros((nmp, n_steps))
        desplxy = np.zeros((nmp, n_steps))
        eqplas = np.zeros((nmp, n_steps))
        
        # Condiciones iniciales (paso 0)
        corX[:, 0], corY[:, 0] = xp[:, 0], xp[:, 1]
        sigxx[:, 0], sigyy[:, 0], sigxy[:, 0] = sig[:, 0], sig[:, 1], sig[:, 2]
        epsexx[:, 0], epseyy[:, 0], epsexy[:, 0] = epse[:, 0], epse[:, 1], epse[:, 2]
        epspxx[:, 0], epspyy[:, 0], epspxy[:, 0] = epsp[:, 0], epsp[:, 1], epsp[:, 2]
        velxx[:, 0], velyy[:, 0] = vp[:, 0], vp[:, 1]
        velxy[:, 0] = np.sqrt(velxx[:, 0]**2 + velyy[:, 0]**2)
        # Presión de poros (kPa, + compresión); cero mientras no haya agua
        presporos = np.zeros((nmp, n_steps))
        if self.__vm_pp is not None:
            presporos[:, 0] = -self.__vm_pp[:, 0]

        return {
            'presporos': presporos,
            'corX': corX, 'corY': corY,
            'sigxx': sigxx, 'sigyy': sigyy, 'sigxy': sigxy,
            'epsexx': epsexx, 'epseyy': epseyy, 'epsexy': epsexy,
            'epspxx': epspxx, 'epspyy': epspyy, 'epspxy': epspxy,
            'velxx': velxx, 'velyy': velyy, 'velxy': velxy,
            'desplxx': desplxx, 'desplyy': desplyy, 'desplxy': desplxy,
            'eqplas': eqplas
        }
    
    def _save_step_to_arrays(self, arrays, step_idx):
        """Guarda el estado actual de las partículas en los arrays de resultados."""
        xp = self.__mp_xp
        sig = self.__vm_sig
        epse = self.__vm_epse
        epsp = self.__vm_epsp
        vp = self.__vm_vp
        
        arrays['corX'][:, step_idx] = xp[:, 0]
        arrays['corY'][:, step_idx] = xp[:, 1]
        arrays['sigxx'][:, step_idx] = sig[:, 0]
        arrays['sigyy'][:, step_idx] = sig[:, 1]
        arrays['sigxy'][:, step_idx] = sig[:, 2]
        arrays['epsexx'][:, step_idx] = epse[:, 0]
        arrays['epseyy'][:, step_idx] = epse[:, 1]
        arrays['epsexy'][:, step_idx] = epse[:, 2]
        arrays['epspxx'][:, step_idx] = epsp[:, 0]
        arrays['epspyy'][:, step_idx] = epsp[:, 1]
        arrays['epspxy'][:, step_idx] = epsp[:, 2]
        arrays['velxx'][:, step_idx] = vp[:, 0]
        arrays['velyy'][:, step_idx] = vp[:, 1]
        arrays['velxy'][:, step_idx] = np.sqrt(vp[:, 0]**2 + vp[:, 1]**2)
        arrays['desplxx'][:, step_idx] = arrays['corX'][:, step_idx] - arrays['corX'][:, 0]
        arrays['desplyy'][:, step_idx] = arrays['corY'][:, step_idx] - arrays['corY'][:, 0]
        arrays['desplxy'][:, step_idx] = np.sqrt(
            (arrays['corX'][:, 0] - arrays['corX'][:, step_idx])**2 +
            (arrays['corY'][:, 0] - arrays['corY'][:, step_idx])**2
        )
        arrays['eqplas'][:, step_idx] = np.sqrt(
            4/9 * (epsp[:, 0]**2 - epsp[:, 0] * epsp[:, 1] + epsp[:, 1]**2) +
            4/3 * epsp[:, 2]**2
        )
        if self.__vm_pp is not None:
            arrays['presporos'][:, step_idx] = -self.__vm_pp[:, 0]

    def _check_dialog_cancel_pause(self, msg):
        """Verifica si el usuario canceló o pausó el diálogo.
        Retorna True si se canceló, False si continúa."""
        analysis_dialog = self.analysis_dialog
        if analysis_dialog.cancelled:
            analysis_dialog.close()
            return True
        if analysis_dialog.paused:
            analysis_dialog.setStatus(False, msg + "\n\nAnálisis pausado")
            while analysis_dialog.paused:
                time.sleep(0.1)
                QApplication.processEvents()
                if analysis_dialog.cancelled:
                    analysis_dialog.close()
                    return True
        return False
    
    def _append_stage_results(self, stage, arrays, list_time, list_time_graphic):
        """Guarda el bloque de resultados de UNA etapa.

        Antes cada bucle sobrescribía los resultados de la etapa anterior,
        así que de un análisis geostático→falla solo sobrevivían los frames
        de la falla. Ahora cada etapa aporta su bloque y _finalize_results()
        los concatena.
        """
        self.__rs_stages.append({
            'stage': stage,
            'dt': self.__tm_dt_time,
            'arrays': {k: v for k, v in arrays.items()},
            'list_time': np.asarray(list_time, dtype=float),
            'list_time_graphic': np.asarray(list_time_graphic, dtype=float),
        })
        n_frames = arrays['corX'].shape[1]
        print(f"[RESULTS] Etapa '{stage.name or stage.stage_type.value}': "
              f"{n_frames} frame(s) guardado(s)")

    def _finalize_results(self):
        """Concatena los bloques de todas las etapas y los deja en las
        variables __rs_* que saveResults() ya lee.

        Detalles:
        - El frame 0 de cada etapa es el estado con el que arrancó, que es
          el último de la etapa anterior: se descarta salvo en el primer
          bloque (donde es la única representación del estado inicial).
        - El eje de tiempo se hace monótono desplazando cada etapa por el
          acumulado. Las unidades son mixtas (incrementos en cuasi-estático,
          segundos en dinámico); ETAPAS_FRAMES dice qué es cada tramo.
        - Los desplazamientos NO se re-referencian: cada etapa los mide
          desde su propio frame 0 (convención geotécnica: se reinician
          después del geostático). Ver _save_step_to_arrays.
        """
        keys = list(self.__rs_stages[0]['arrays'].keys())
        blocks = {k: [] for k in keys}
        times, times_graphic, frames_meta = [], [], []

        offset_t = 0.0
        offset_tg = 0.0
        frame_cursor = 0

        for i, block in enumerate(self.__rs_stages):
            skip = 0 if i == 0 else 1  # descartar el frame duplicado del handoff
            arrays = block['arrays']
            n_frames = arrays['corX'].shape[1]
            if n_frames <= skip:
                continue  # etapa sin frames útiles (cancelada de inmediato)

            for k in keys:
                blocks[k].append(arrays[k][:, skip:])

            lt = block['list_time']
            ltg = block['list_time_graphic']
            times.append(lt[skip:] + offset_t if lt.size > skip else lt[:0])
            times_graphic.append(ltg[skip:] + offset_tg if ltg.size > skip else ltg[:0])

            n_added = n_frames - skip
            stage = block['stage']
            frames_meta.append({
                'ETAPA': i + 1,
                'TIPO': stage.stage_type.value,
                'NOMBRE': stage.name or stage.stage_type.value,
                'FRAME_INICIO': frame_cursor,
                'FRAME_FIN': frame_cursor + n_added - 1,
                'DT': block['dt'],
            })
            frame_cursor += n_added

            if lt.size:
                offset_t += float(lt[-1])
            if ltg.size:
                offset_tg += float(ltg[-1])

        self.__rs_stages_frames = frames_meta
        self.__rs_new_list_time = np.concatenate(times) if times else np.zeros(0)
        self.__rs_new_list_time_graphic = (
            np.concatenate(times_graphic) if times_graphic else np.zeros(0))

        merged = {k: np.concatenate(blocks[k], axis=1) for k in keys}
        self.__rs_corX = merged['corX']
        self.__rs_corY = merged['corY']
        self.__rs_sigxx = merged['sigxx']
        self.__rs_sigyy = merged['sigyy']
        self.__rs_sigxy = merged['sigxy']
        self.__rs_epsexx = merged['epsexx']
        self.__rs_epseyy = merged['epseyy']
        self.__rs_epsexy = merged['epsexy']
        self.__rs_epspxx = merged['epspxx']
        self.__rs_epspyy = merged['epspyy']
        self.__rs_epspxy = merged['epspxy']
        self.__rs_velxy = merged['velxy']
        self.__rs_velxx = merged['velxx']
        self.__rs_velyy = merged['velyy']
        self.__rs_desplxx = merged['desplxx']
        self.__rs_desplyy = merged['desplyy']
        self.__rs_desplxy = merged['desplxy']
        self.__rs_eqplas = merged['eqplas']
        # La presión de poros solo se guarda si alguna etapa la calculó: así
        # los proyectos de una fase no crecen.
        has_pp = any(b['stage'].stage_type == StageType.CONSOLIDATION
                     for b in self.__rs_stages)
        self.__rs_presporos = merged['presporos'] if has_pp else None

        print(f"[RESULTS] Total: {merged['corX'].shape[1]} frames de "
              f"{len(frames_meta)} etapa(s)")
        for f in frames_meta:
            print(f"   Etapa {f['ETAPA']} ({f['TIPO']}): frames "
                  f"{f['FRAME_INICIO']}-{f['FRAME_FIN']}")


    def _run_dynamic_loop(self, config: AnalysisConfig, stage):
        """Bucle dinámico: for t in range(N).

        Mismo esquema que beam.py y la fase de falla de talud_2021_v2.py.
        """
        analysis_dialog = self.analysis_dialog
        list_time_graphic = self.__tm_list_time_graphic
        list_time = self.__tm_list_time
        steps_time = self.__tm_steps_time
        dt_time = self.__tm_dt_time
        
        # Configurar damping y tp para este bucle
        self.__step_dampfac = stage.damping_factor
        self.__vm_tp_current = self.__vm_tp0.copy()

        # Gravedad completa y explícita: una etapa cuasi-estática previa
        # interrumpida a mitad de la rampa deja bp parcial.
        self.__vm_bp[:] = self.__vm_bp0

        use_gauss = stage_use_gauss(stage)
        plasticity_flags = self._body_plasticity_flags(stage)
        stage_label = self._stage_label(stage)
        multi_body = stage.multi_body
        consolidation = stage.stage_type == StageType.CONSOLIDATION

        t0 = tm.time()
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'[{"CONSOLIDATION" if consolidation else "DYNAMIC"}] {stage_label}. '
              f'Steps={steps_time}, dt={dt_time}, damp={stage.damping_factor}')
        if multi_body:
            print(f"[DYNAMIC] {len(self.__bodies)} cuerpos con contacto, mu={stage.friction}, "
                  f"plasticidad por cuerpo={plasticity_flags}")
        
        # Inicializar arrays de resultados
        n_graphic_steps = len(list_time_graphic)
        arrays = self._init_result_arrays(n_graphic_steps)
        
        new_list_time_graphic = list_time_graphic.copy()
        new_list_time = list_time.copy()
        current_index_graphic = 0
        
        for index in range(list_time.size - 1):
            current_time = list_time[index]

            # Verificar cancelación/pausa
            msg = f"{stage_label}\n→ paso {index:.0f} de {steps_time}."
            if self._check_dialog_cancel_pause(msg):
                # Guardar lo alcanzado hasta aquí en vez de descartarlo
                n_keep = current_index_graphic + 1
                for key in arrays:
                    arrays[key] = arrays[key][:, :n_keep]
                self._append_stage_results(
                    stage, arrays, new_list_time[:index + 1],
                    new_list_time_graphic[:n_keep])
                return False

            # Verificar que las partículas están dentro de la malla
            try:
                # Ejecutar un paso MPM
                analysis_dialog.setProgress(100 * index / steps_time)
                analysis_dialog.setStatus(False, msg)
                QApplication.processEvents()
                
                if consolidation:
                    self._run_one_mpm_step_two_phase(plasticity_flags[0])
                elif multi_body:
                    self._run_one_mpm_step_multibody(plasticity_flags, stage.friction,
                                                     stage.contact_normals)
                else:
                    self._run_one_mpm_step(use_gauss, plasticity_flags)

            except Exception as e:
                print(f"---------------------//-------------------------")
                print(f"Error: {e}")
                print(f"Error en el tiempo: {current_time}, paso: {index}")
                print(f"---------------------//-------------------------")
                
                text_error = f"Paso:[{index} de {steps_time}]\n"
                text_error += f"El material se encuentra fuera de la malla\nEl análisis se detendrá en este punto.\n"
                analysis_dialog.setStatus(True, text_error)
                text_question = f"¿Quieres finalizar el análisis hasta este punto\n"
                text_question += f"y guardar los resultados?"
                analysis_dialog.setQuestion(text_question)
                analysis_dialog.pauseAnalysis()
                analysis_dialog.setViewError()
                while analysis_dialog.paused:
                    time.sleep(0.1)
                    QApplication.processEvents()
                    if analysis_dialog.cancelled:
                        analysis_dialog.close()
                        return False
                    if analysis_dialog.accepted:
                        analysis_dialog.close()
                        # Truncar arrays
                        position_max = current_index_graphic
                        new_list_time = new_list_time[:index]
                        new_list_time_graphic = new_list_time_graphic[:position_max]
                        for key in arrays:
                            arrays[key] = arrays[key][:, :position_max]
                        break
                break
            
            # Guardar datos cuando toca el frame gráfico.
            # El estado que acaba de calcularse corresponde a list_time[index+1],
            # no a list_time[index]: hay que compararlo contra el frame gráfico
            # SIGUIENTE. Comparando contra el actual, el frame k terminaba
            # guardando el estado del paso ndt*(k-1)+1 en vez del paso ndt*k
            # — con fps 30 y dt 1e-3, 32 pasos antes de lo que dice su rótulo.
            # Mismo criterio que los scripts de referencia (beam.py l. 139,
            # talud_2021.py fase_falla).
            next_graphic = current_index_graphic + 1
            if (next_graphic < n_graphic_steps and
                    abs(list_time[index + 1] -
                        list_time_graphic[next_graphic]) < 1e-13):
                self._save_step_to_arrays(arrays, next_graphic)
                current_index_graphic = next_graphic
        
        tf = tm.time()
        print(f"[DYNAMIC] Fin. Tiempo total: {tf - t0:.2f}s")
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")

        self._append_stage_results(stage, arrays, new_list_time, new_list_time_graphic)
        return True
    
    def _run_quasi_static_increment_loop(self, config: AnalysisConfig, stage):
        """Bucle cuasi-estático con incrementos de carga:
        for i in range(nincre): while(ff > tol).

        Mismo esquema que Ca_portante2.py y la fase geostática de
        talud_2021_v2.py.
        """
        analysis_dialog = self.analysis_dialog
        
        # Parámetros de incrementos (por etapa)
        # - Geostática: rampa de gravedad 0 → 100 % en nincre pasos; las
        #   fuerzas de las partículas NO se aplican (solo peso propio).
        # - Incrementos de carga: gravedad completa; Fx/Fy de las partículas
        #   es la fuerza FINAL y se llega a ella en rampa: (i+1)/nincre.
        nincre = stage.n_increments if stage.n_increments and stage.n_increments > 0 else 1
        geostatic = stage.stage_type == StageType.GEOSTATIC
        dincreGrav = 1.0 / nincre if geostatic else 0.0
        dtime = self.__tm_dt_time

        # Configurar damping
        self.__step_dampfac = stage.damping_factor

        use_gauss = stage_use_gauss(stage)
        plasticity_flags = self._body_plasticity_flags(stage)
        stage_label = self._stage_label(stage)

        # Arrays de tiempo para CE
        list_time_graphic = np.linspace(0, nincre, nincre + 1)
        list_time = np.linspace(0, nincre, nincre + 1)

        t0 = tm.time()
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
        print(f'[QUASI-STATIC] {stage_label}. Incrementos={nincre}, '
              f'{"solo peso propio" if geostatic else "Fx/Fy en rampa hasta el 100 %"}, '
              f'damp={stage.damping_factor}')
        
        # Inicializar arrays de resultados
        arrays = self._init_result_arrays(nincre + 1)
        
        # Tolerancias de convergencia
        tol_ff = stage.convergence_tol_force
        tol_ee = stage.convergence_tol_energy
        
        finfor = False
        last_i = 0
        # Duración del primer incremento; sirve de referencia para el corte por
        # tiempo. Antes esto reusaba t0 y rompía el total impreso al final.
        t_first_incr = 1e9

        for i in range(nincre):
            # Verificar cancelación/pausa
            msg = f"{stage_label}\n→ incremento {i:.0f} de {nincre}."
            if self._check_dialog_cancel_pause(msg):
                # Guardar los incrementos ya convergidos en vez de descartarlos
                n_keep = i + 1  # frame 0 (inicial) + i incrementos completados
                for key in arrays:
                    arrays[key] = arrays[key][:, :n_keep]
                self._append_stage_results(
                    stage, arrays, list_time[:n_keep], list_time_graphic[:n_keep])
                return False

            analysis_dialog.setProgress(100 * i / nincre)
            analysis_dialog.setStatus(False, msg)
            QApplication.processEvents()
            
            # Aplicar incremento de carga
            bp0 = self.__vm_bp0
            if dincreGrav != 0:
                self.__vm_bp[:, 1] = (i + 1) * dincreGrav * bp0[:, 1]                
            else:
                self.__vm_bp[:, 1] = bp0[:, 1]
                
            if geostatic:
                self.__vm_tp_current = 0.0 * self.__vm_tp0
            else:
                # Multiplicar primero y dividir al final: así el resultado es
                # el redondeo correcto de (i+1)·Fy/n, idéntico bit a bit al
                # esquema anterior (i+1)·Δ·Fy_semilla con Fy = Δ·n·Fy_semilla.
                # (i+1)/n·Fy se separa en 1 ulp en algunos incrementos (n=56).
                self.__vm_tp_current = (i + 1) * self.__vm_tp0 / nincre

            # Inicializar convergencia
            ff = 1
            ee = 1
            nework = 0
            tcont = 0
            tinicial = time.time()
            while (ff > tol_ff) or (ee > tol_ee):

                analysis_dialog.setTimer(f"⏳ {time.time() - tinicial:.0f}seg")
                QApplication.processEvents()
                tcont += 1
                if tcont % 100 == 0:
                    print("----- Iteracion=",tcont,"ff=",ff,"ee=",ee)

                nmass, niforce, neforce, nvel = self._run_one_mpm_step(use_gauss, plasticity_flags)

                # Evaluar convergencia
                nework0 = nework
                ff, ee, nework = static_convergence(nmass, niforce, neforce, nvel, dtime, nework0)

                # ff y ee son cocientes: si no hay fuerza externa el denominador
                # es 0 y salen nan/inf. Con nan la condición del while es falsa y
                # el incremento se daría por convergido en silencio; con inf el
                # bucle no terminaría nunca. En ambos casos hay que avisar.
                if not (np.isfinite(ff) and np.isfinite(ee)):
                    print(f"[AVISO] incremento {i + 1}: convergencia no evaluable "
                          f"(ff={ff}, ee={ee}). Suele significar que no hay fuerza "
                          f"externa en esta etapa (¿gravedad 0 y sin cargas?). "
                          f"Se da por convergido tras {tcont} iteración(es).")
                    break

                # Tope de iteraciones de la etapa: evita que un incremento que no
                # converge se lleve horas de una validación.
                if stage.max_iterations and tcont >= stage.max_iterations:
                    print(f"[AVISO] incremento {i + 1}: se alcanzó el máximo de "
                          f"{stage.max_iterations} iteraciones sin converger "
                          f"(ff={ff:.4g}, ee={ee:.4g}). Se detiene la etapa.")
                    finfor = True
                    break

                # Condición de seguridad: tiempo máximo
                tiempoi = time.time() - tinicial
                if (tiempoi > 100 * t_first_incr) and (i > 0):
                    print("se excedió tiempo máximo de ejecución!!")
                    finfor = True
                    break
                else:
                    finfor = False

            
            # Guardar resultados del incremento
            tiempo_incr = time.time() - tinicial
            if i == 0:
                # Referencia para el corte por tiempo: si un incremento tarda
                # 100x lo que tardó el primero, algo se atascó.
                t_first_incr = tiempo_incr

            print(f"incremento {i + 1}, num ciclos {tcont}")
            print(f"tiempo en este incremento {tiempo_incr:.2f}s")
            print(f"desbalance fuerzas {ff}, Energía cinética {ee}")
            
            self._save_step_to_arrays(arrays, i + 1)
            last_i = i
            
            if finfor:
                break
        
        # Truncar arrays al número real de incrementos completados
        final_idx = last_i + 2
        for key in arrays:
            arrays[key] = arrays[key][:, :final_idx]
        
        tf = tm.time()
        print(f"[QUASI-STATIC] Fin. Tiempo total: {tf - t0:.2f}s")
        print("#►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
                
        list_time = list_time[:final_idx]
        list_time_graphic = list_time_graphic[:final_idx]
        self._append_stage_results(stage, arrays, list_time, list_time_graphic)
        return True
    
    # ===================================================================
    #  Inicialización (común a todas las etapas)
    # ===================================================================
    def initConditions(self):
        # El damping ya no es global: lo fija cada etapa (stage.damping_factor).
        self.__ic_gravity = self.model_current_project.getGravity()

      
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
        #    NOTA xp (orden): en MPM-UN original la lista tiene otro orden
        #             inf-izq, inf-der, sup-izq, sup-der
        #             en este programa
        #             sup-izq, inf-izq, inf-der, sup-der
        #             Relevante al validar contra el script: el orden de
        #             particulas difiere, comparar alineando por coordenada.

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
        bodies = []

        for id_material_point in list_point_material:
            model_material_point = models_material_point[id_material_point]
            points = model_material_point.getPoints()
            name = model_material_point.getName()
            id_property = model_material_point.getIdProperty()
            bodies.append({'id': id_material_point, 'name': name,
                           'start': len(mp_xp), 'end': len(mp_xp) + len(points),
                           'plastic': True})  # 'plastic' lo fija initProperties

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
        self.__bodies = bodies
        assert bodies[-1]['end'] == self.__mp_nmp, "rangos de cuerpos inconsistentes"

        '''
        print("self.__mp_xp", self.__mp_xp)
        print("self.__mp_mp_elem", self.__mp_mp_elem)
        print("self.__mp_active_elem", self.__mp_active_elem)
        print("self.__mp_nmp", self.__mp_nmp)
        '''

        
        self.VOLUMES = mp_volumes
        self.VELOCITIES = mp_velocities
        self.FORCES = mp_forces

    def initProperties(self):
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄
        #::::::::::::  propiedades de las particlas :::::::::::::::
        #►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄    
        # modulo de elasticidad KPa     :: E
        # Coeficiente de poisson        :: nu
        # Cohesion KPa                  :: C'
        # Angulo de friccion            :: Phi
        # Angulo de dilatancia          :: psi

        list_point_material = self.list_point_material
        models_material_point = self.model_current_project.getModelsPointsMaterials()

        mp_prop=[]
        mp_density = []
        for body, id_material_point in zip(self.__bodies, list_point_material):
            model_material_point = models_material_point[id_material_point]
            points = model_material_point.getPoints()
            id_material = model_material_point.getIdProperty()
            row, density, plastic = self._material_row(id_material)
            # Material con que se armó el grupo, y el que tiene aplicado ahora
            # (una etapa puede cambiarlo, ver _apply_stage_materials)
            body['material0'] = id_material
            body['material'] = id_material
            body['plastic'] = plastic

            for point in points:
                mp_prop.append(list(row))
                mp_density.append(density)

        #variables
        Prop = np.asarray(mp_prop)
        self.__mp_prop = Prop
        self.DENSITY = mp_density

    def _material_row(self, id_material):
        """Propiedades de un material como las usa el motor.

        Returns:
            (fila de Prop [E, nu, c, phi(rad), psi(rad), 0], densidad en Mg/m³,
             True si es Mohr-Coulomb / False si es elástico lineal)
        """
        # getData() = {id: {'NAME', 'MODULOELASTICIDAD', 'RELACIONPOISSON',
        #                   'COHESION', 'ANGULOFRICCION', 'DENSIDAD' [kg/m³],
        #                   'ANGULODILATANCIA', 'MODELO' (opcional)}}
        data = self.model_current_project.getModelsProperties()[id_material].getData()
        mat = data[list(data.keys())[0]]
        row = [mat['MODULOELASTICIDAD'],
               mat['RELACIONPOISSON'],
               mat['COHESION'],
               mat['ANGULOFRICCION'] / 180*math.pi,
               mat['ANGULODILATANCIA'] / 180*math.pi,
               0]  # este cero lo tiene los archivos de referencia leon(2019)
        # Modelo constitutivo: 'MOHR_COULOMB' (default) o 'ELASTICO'. Un
        # material elástico no plastifica aunque la etapa lo permita.
        plastic = mat.get('MODELO', 'MOHR_COULOMB') != 'ELASTICO'
        return row, mat['DENSIDAD']/1000, plastic

    def _stage_materials(self, config, index):
        """Material vigente de cada cuerpo en la etapa `index`: el último
        CAMBIOMATERIAL de las etapas 0..index, o el material del grupo."""
        targets = []
        for body in self.__bodies:
            target = body['material0']
            for st in config.stages[:index + 1]:
                target = st.material_changes.get(body['id'], target)
            targets.append(target)
        return targets

    def _apply_stage_materials(self, config, index):
        """Asigna a cada cuerpo el material vigente en la etapa `index`.

        El vigente es el último cambio (CAMBIOMATERIAL) de las etapas 0..index,
        o el material con que se armó el grupo. Se recalcula desde cero en
        cada etapa, así que también vale al reanudar desde un checkpoint.
        Solo toca los cuerpos cuyo material cambia: los demás conservan su
        Prop tal cual (la columna 5 es una variable de estado de la
        plasticidad). Al cambiar, se hace como la fase de falla de la
        referencia: Prop nueva con columna 5 en cero y Mp = rho·Vp0.
        """
        for body, target in zip(self.__bodies, self._stage_materials(config, index)):
            if target == body['material']:
                continue
            row, density, plastic = self._material_row(target)
            s = slice(body['start'], body['end'])
            self.__mp_prop[s] = row
            self.__vm_rhop[s] = density
            self.__vm_Mp[s] = np.multiply(self.__vm_rhop[s], self.__vm_Vp0[s])
            body['material'] = target
            body['plastic'] = plastic
            print(f"[MATERIAL] cuerpo '{body['name']}': material {target} "
                  f"(E={row[0]}, c={row[2]}, rho={density}, "
                  f"{'Mohr-Coulomb' if plastic else 'elástico'})")

    def initVerctorAndMatrix(self, initial_state=None):
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
        bp0=np.zeros((nmp, 2))
        if gravity != 0:
            bp[:,1]=-gravity        
            bp0[:,1]=-gravity        

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
        self.__vm_bp0 = bp0
        self.__vm_tp0 = tp0

        # Handoff (FASE A): si se entrega un estado inicial — de una etapa
        # previa o de un geoestatico guardado — arrancar desde ahi en vez
        # de desde cero (sobrescribe sig/Fp/epse/epsp/xp/vp/Vp/mp_elem).
        if initial_state is not None:
            self._inject_state(initial_state)
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
        inferior a superior, en todo caso la de boundary_particles2 es mejor para
        taludes pero aplica tambien para un cuadrado"""
        
        xp = self.__mp_xp
        # si se va a emplear integracion gaussiana - obtener array con particulas de la frontera
        bound_ptcl, bound_val = boundary_particles3(xp)
        
        '''
        print("bound_ptcl", bound_ptcl)
        print("bound_val", bound_val)
        for i in range(len(bound_ptcl)):
            if bound_val[i] == 1:
                print("bound_ptcl", bound_ptcl[i], "bound_val", bound_val[i])
        '''
        
        self.__bo_bound_ptcl = bound_ptcl
        self.__bo_bound_val = bound_val
        
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
        presporos = self.__rs_presporos   # None si ninguna etapa la calculó

        ########################################################################
        #                           analisis finalizado
        ########################################################################        
        self.model_result.clearResult()

        # Etapas ejecutadas + a qué frames corresponde cada una. DAMPFAC se
        # guarda solo como dato informativo (el de la primera etapa): el que
        # gobierna es el de cada etapa, que va completo en ETAPAS.
        # run() no llega aquí sin al menos un bloque de resultados.
        stages_dicts = [b['stage'].to_dict() for b in self.__rs_stages]
        dampfac = self.__rs_stages[0]['stage'].damping_factor
        self.model_result.updateResultDataBase(
            gravity= self.__ic_gravity,
            dampfac=  dampfac,
            stages=stages_dicts,
            stages_frames=self.__rs_stages_frames
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
            eqplas=eqplas.min(),
            presporos=None if presporos is None else float(presporos.min())
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
            eqplas=eqplas.max(),
            presporos=None if presporos is None else float(presporos.max())
        )
        

                
        corX_l = corX.tolist(); corY_l = corY.tolist()
        sigxx_l = sigxx.tolist(); sigyy_l = sigyy.tolist(); sigxy_l = sigxy.tolist()
        epsexx_l = epsexx.tolist(); epseyy_l = epseyy.tolist(); epsexy_l = epsexy.tolist()
        epspxx_l = epspxx.tolist(); epspyy_l = epspyy.tolist(); epspxy_l = epspxy.tolist()
        velxy_l = velxy.tolist(); velxx_l = velxx.tolist(); velyy_l = velyy.tolist()
        desplxx_l = desplxx.tolist(); desplyy_l = desplyy.tolist(); desplxy_l = desplxy.tolist()
        eqplas_l = eqplas.tolist()
        presporos_l = presporos.tolist() if presporos is not None else None

        for node in range(len(corX)):
            self.model_result.addResultNode(
                id_result_node=node+1,
                material_node=self.__mp_property[node],
                corx=corX_l[node],
                cory=corY_l[node],
                sigxx=sigxx_l[node],
                sigyy=sigyy_l[node],
                sigxy=sigxy_l[node],
                epsexx=epsexx_l[node],
                epseyy=epseyy_l[node],
                epsexy=epsexy_l[node],
                epspxx=epspxx_l[node],
                epspyy=epspyy_l[node],
                epspxy=epspxy_l[node],
                velxy=velxy_l[node],
                velxx=velxx_l[node],
                velyy=velyy_l[node],
                desplxx=desplxx_l[node],
                desplyy=desplyy_l[node],
                desplxy=desplxy_l[node],
                eqplas=eqplas_l[node],
                presporos=presporos_l[node] if presporos_l is not None else None
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