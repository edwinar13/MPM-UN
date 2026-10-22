## Funciones del MPM de doble fase y único punto (formulación v-w)
#
# Copiadas sin cambios del motor de Caro González (2024), módulo 2_explicit2.py
# (carpeta mpm_un_two_phase, fuera de este repo). Solo cambia el decorador:
# @njit(cache=True), como el resto del motor de la app.
#
# Las funciones comunes con el motor de una fase (funciones de forma, matriz
# elástica, Mohr-Coulomb, elem_i_mp) tienen el mismo cuerpo en ambos motores,
# así que se importan de explicit2.py / mesh.py en lugar de duplicarlas. Este
# módulo no modifica el motor de una fase.
#
# El ciclo de cálculo (ecuación nodal, amortiguamiento, drenaje, carga) no está
# aquí: lo armaba el programa principal de la referencia, que no se conserva. Se
# reconstruye a partir del Algoritmo 2 de la tesis (cap. 6.3); ver
# tools/experimentos/consolidacion_1d.py.
from __future__ import division, print_function
import math

import numpy as np
from numba import njit

from motorMPM.mesh import elem_i_mp
from motorMPM.explicit2 import (shape_func, shapfunc_gauss1,
                                constitutive_matrix_elastic, MC_elastoplastic2)


def deltatime_two_phases_CFL(Ep, nu, rho_sat_p, ele_size, No_courant, K_w, n_0):
    """Funcion que calcula el delta de tiempo necesario para convergencia
       Courant-Friedrichs-Lewy - Velocidad de onda de compresion no drenada
       Aplica para MPM-2FASES
        Argumentos:
                    Ep = Array con el modulo de Young de las particulas
                    nu = Array con el coeficiente de poisson de las particulas
                    rhop = Array con la densidad de las particulas
                    ele_size = tamano de la malla de los elementos
                    No_courant = porcentaje en tanto por 1 del minimo delta de tiempo

        Return: dt = delta de tiempo redondeado con un solo decimal diferente de cero"""

    Eedo = (1 - nu) / (1 + nu) / (1 - 2*nu) * Ep # Modulo edometrico Ec
    Eedo_und = Eedo + K_w/n_0 # Modelo edometrico no drenado (Ec,u)
    cp = math.sqrt(np.max(np.divide(Eedo_und, rho_sat_p.astype(float)))) # Velocidad de la onda de compresión no drenada en el material
    dt_cri = ele_size / cp  # Incremento de tiempo critico - CFL
    dt = dt_cri*No_courant # Incremento de tiempo a emplear segun numero de Courant (0.1-0.9)
    # Redondeo del dt a un solo decimal distinto de cero
    sgn = -1 if dt < 0 else 1
    scale = int(-math.floor(math.log10(abs(dt))))
    if scale <= 0:
        scale = 1
    factor = 10**scale
    dt = sgn*math.floor(abs(dt)*factor)/factor

    return dt


@njit(cache=True)
def particles_to_nodes_two_phases(grid, particle):
    """ Funcion que transfiere la informacion de las particulas a los nodos de la malla
        para un formulacion dinamica doble fase v-w con matriz de masa agrupada - MPM 2 FASES
        ------
        Return ---- Cantidades nodales
                nmass_s = masa nodal - fase solida,
                nmass_w = masa nodal - fase liquida
                nmass_weq =  masa nodal equivalente - fase liquida
                nmass =  masa nodal total(nmass_s + mass_w) - fase liquida + fase solida
                nmomentum_s = cantidad de movimiento - fase solida
                nmomentum_w = cantidad de movimiento - fase liquida
                niforce_w = fuerza interna nodal - Ec fase liquida
                neforce_w = fuerza externa nodal - Ec fase liquida
                ndforce_w = fuerza de arrastre nodal - Ec fase liquida
                neforce_m = fuerza externa nodal - Ec mezcla
                niforce_m = fuerza interna nodal - Ec mezcla
                shfnp = matriz - funciones de forma de los elementos """

    # --------------- Organizando los argumentos de las listas ---------------

    inci, cor, active_elem, active_nodes, mp_elem = grid
    xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, Mp_weq, sig_t, sig_e, pp, bp, tp, pb_p, n_p, k_p, rho_w  = particle
    nnodes = len(active_nodes) # Numero de nodos activos

    # ------------- Inicializar variables nodales ----------------------------

    nmass_s = np.zeros((nnodes, 1)) # Vector de masa nodal - fase solida
    nmass_w = np.zeros((nnodes, 1)) # Vector de masa nodal - fase liquida
    nmass_weq = np.zeros((nnodes, 1)) # Vector de masa nodal equivalente - fase liquida
    nmass = np.zeros((nnodes, 1)) # Vector de masa nodal total - mezcla

    nmomentum_s = np.zeros((nnodes, 2)) # Vector de momentum nodal - fase solida
    nmomentum_w = np.zeros((nnodes, 2)) # Vector de momentum nodal - fase liquida

    niforce_w = np.zeros((nnodes, 2)) # Vector de fuerzas internas nodales - Ec fase liquida
    neforce_w = np.zeros((nnodes, 2)) # Vector de fuerzas externas nodales - Ec fase liquida
    ndforce_w = np.zeros((nnodes, 2)) # Vector de fuerzas de arrastre - Ec fase liquida

    niforce_m = np.zeros((nnodes, 2)) # Vector de fuerzas internas nodales - Ec mezcla
    neforce_m = np.zeros((nnodes, 2)) # Vector de fuerzas externas nodales - Ec mezcla

    # -- Crear array para las funciones de forma --
    shfnp = np.zeros((len(xp), inci.shape[1]*3)) # En cada fila las 3 funciones de forma y sus derivadas

    # ==================================================================

    # Ciclo en los elementos activos del sistema
    for i in range(len(active_elem)):
        ele = active_elem[i] # Numero del elemento
        nodes = inci[ele - 1,:] # Nodos asociados al elemento
        xn = cor[nodes - 1, :] # Coordenadas de los nodos
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i

        # Ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # Numero de mp - particula
            x = xp[mp - 1, 0]; y = xp[mp - 1, 1]
            Np = shape_func(x, y, xn) # Funciones de forma y sus derivadas
            # Guardando las funciones de forma y sus derivadas en el array correspondiente
            shfnp[mp - 1, :] = Np.reshape(3 * len(nodes))
            #shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] = Np[0,0], Np[0,1], Np[0,2] # Ni
            #shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] = Np[1,0], Np[1,1], Np[1,2] # Ni,x
            #shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] = Np[2,0], Np[2,1], Np[2,2] # Ni,y

            # Ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # Numero del nodo global
                # -- Ciclo para determinar ubicacion del nodo en la lista de nodos activos --
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- Fin de ciclo --

                #------------- Calculo de masas nodales -----------------------
                nmass_s[nna, 0] += Np[0, k]*Mp_s0[mp - 1] # Masa nodal - Fase solida
                nmass_w[nna, 0] += Np[0, k]*Mp_w[mp - 1] # Masa nodal - Fase liquida
                nmass_weq[nna, 0] += Np[0, k]*Mp_weq[mp - 1] # Masa nodal equivalente - Fase liquida
                nmass[nna, 0] += Np[0, k]*Mp[mp - 1] # Masa nodal total - Mezcla

                #------------ Calculo de cantidades de movimiento nodales -----
                nmomentum_s[nna, 0] += Np[0, k]*Mp_s0[mp - 1]*vp[mp - 1, 0] # Momentum nodal en x - Fase solida
                nmomentum_s[nna, 1] += Np[0, k]*Mp_s0[mp - 1]*vp[mp - 1, 1] # Momentum nodal en y - Fase solida

                nmomentum_w[nna, 0] += Np[0, k]*Mp_w[mp - 1]*wp[mp - 1, 0] # Momentum nodal en x - Fase liquida
                nmomentum_w[nna, 1] += Np[0, k]*Mp_w[mp - 1]*wp[mp - 1, 1] # Momentum nodal en y - Fase liquida

                #------------- Calculo de fuerzas nodales ---------------------
                niforce_w[nna, 0] -= Vp[mp - 1]*pp[mp - 1, 0]*Np[1, k] # Fuerza interna en x - Ec Fase liquida
                niforce_w[nna, 1] -= Vp[mp - 1]*pp[mp - 1, 1]*Np[2, k] # Fuerza interna en y - Ec Fase liquida

                neforce_w[nna, 0] += Np[0, k]*Mp_weq[mp - 1]*bp[mp - 1, 0] + Np[0, k]*pb_p[mp - 1, 0] # Fuerza externa en x - Ec Fase liquida
                neforce_w[nna, 1] += Np[0, k]*Mp_weq[mp - 1]*bp[mp - 1, 1] + Np[0, k]*pb_p[mp - 1, 1] # Fuerza externa en y - Ec Fase liquida

                ndforce_w[nna, 0] -= (Vp[mp - 1]*Np[0, k]*n_p[mp - 1]*rho_w*9.81*(wp[mp - 1, 0] - vp[mp - 1, 0])) / k_p[mp - 1] # Fuerza de arrastre en x - Ec Fase liquida
                ndforce_w[nna, 1] -= (Vp[mp - 1]*Np[0, k]*n_p[mp - 1]*rho_w*9.81*(wp[mp - 1, 1] - vp[mp - 1, 1])) / k_p[mp - 1] # Fuerza de arrastre en y - Ec Fase liquida

                niforce_m[nna, 0] -= Vp[mp - 1]*(sig_e[mp - 1, 0]*Np[1, k] + sig_e[mp - 1, 2]*Np[2, k]) + Vp[mp - 1]*pp[mp -1, 0]*Np[1, k] # Fuerza interna en x - Ec Mezcla
                niforce_m[nna, 1] -= Vp[mp - 1]*(sig_e[mp - 1, 2]*Np[1, k] + sig_e[mp - 1, 1]*Np[2, k]) + Vp[mp - 1]*pp[mp -1, 1]*Np[2, k] # Fuerza interna en y - Ec Mezcla

                neforce_m[nna, 0] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 0] + Np[0, k]*tp[mp - 1, 0]  # Fuerza externa en x - Ec Mezcla
                neforce_m[nna, 1] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 1] + Np[0, k]*tp[mp - 1, 1]  # Fuerza externa en y - Ec Mezcla

    return nmass_s, nmass_w, nmass_weq, nmass, nmomentum_s, nmomentum_w, niforce_w, neforce_w, ndforce_w, neforce_m, niforce_m, shfnp


def nodes_to_particle_vel_two_phases(grid, particle, nquantities, dtime):
    """ Funcion que calcula la velocidad y posicion de las particulas, transfiriendo de los nodos a las particulas
        Adicionalmente calcula la velocidad nodal - Metodo MUSL, doble transferencia
        Formulacion de doble fase y unico punto (v-w)
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal"""

    # organizando los argumentos de las listas
    nacele_w, nacele_s, nmass, nmass_w, nmass_s,nmass_weq = nquantities

    # llamando la funcion interna
    vp, wp, nvel_s, nvel_w = nodes_to_particle_vel_two_phases_inte(grid, particle, nquantities, dtime)

    nvel_w = np.divide(nvel_w, nmass_w, out=np.zeros_like(nvel_w), where=nmass_w !=0) # dividiendo por la masa nodal - Fase liquida
    nvel_s = np.divide(nvel_s, nmass_s, out=np.zeros_like(nvel_s), where=nmass_s !=0) # dividiendo por la masa nodal - Fase solida

    return vp, wp, nvel_s, nvel_w


@njit(cache=True)
def nodes_to_particle_vel_two_phases_inte(grid, particle, nquantities, dtime):
    """ Funcion interna de la funcion nodes_to_particle_vel_two_phases"""

    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    xp, vp, wp, Vp, Mp, Mp_w, Mp_s0, shfnp = particle
    nacele_w, nacele_s, nmass, nmass_w, nmass_s,nmass_weq = nquantities #cantidades nodales

    nnodes = len(active_nodes) # numero de nodos activos
    nvel_w = np.zeros((nnodes, 2)) #array velocidad nodal fase liquida
    nvel_s = np.zeros((nnodes, 2)) #array velocidad nodal fase solida

    # ==================================================================
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1, :] # nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            # organizado las funciones de forma y sus derivadas en el array correspondiente - solo funciona para elm trian
            # (se puede obviar) Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np = shfnp[mp - 1,:].reshape((3, len(nodes)))
            #Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            #Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            #Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y

            # ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo

                # calculo de velocidades de fase y posicion de las particulas

                wp[mp - 1, 0] += dtime*Np[0, k]*nacele_w[nna, 0] #Velocidad de las particulas en x - Fase liquida
                wp[mp - 1, 1] += dtime*Np[0, k]*nacele_w[nna, 1] #Velocidad de las particulas en y - Fase liquida

                vp[mp - 1, 0] += dtime*Np[0, k]*nacele_s[nna, 0] #Velocidad de las particulas en x - Fase liquida
                vp[mp - 1, 1] += dtime*Np[0, k]*nacele_s[nna, 1] #Velocidad de las particulas en y - Fase liquida

            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo

                # calculo de las velocidades nodales de fase acutalizadas
                nvel_w[nna, 0] += Np[0, k]*Mp_w[mp - 1]*wp[mp - 1, 0] #Velocidad nodal en x - Fase liquida
                nvel_w[nna, 1] += Np[0, k]*Mp_w[mp - 1]*wp[mp - 1, 1] #Velocidad nodal en y - Fase liquida

                nvel_s[nna, 0] += Np[0, k]*Mp_s0[mp - 1]*vp[mp - 1, 0] #Velocidad nodal en x - Fase solida
                nvel_s[nna, 1] += Np[0, k]*Mp_s0[mp - 1]*vp[mp - 1, 1] #Velocidad nodal en y - Fase solida

    return vp, wp, nvel_s, nvel_w


@njit(cache=True)
def nodes_to_particle_xp_two_phases(xp, nvel_s, grid, shfnp, dtime):
    """ Funcion que calcula la posicion de las particulas con la velocidad nodal de la fase solida actualizada"""

    # Organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid

    # ==================================================================
    # Ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # Numero del elemento
        nodes = inci[ele - 1, :] # Nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        # Ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # Numero de mp - particula
            # Organizando las funciones de forma y sus derivadas en el array correspondiente - solo funciona para elm trian
            # (se puede obviar) Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np = shfnp[mp - 1,:].reshape((3, len(nodes)))
            #Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            #Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            #Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y

            # Ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                # calculo de las posiciones de las particulas mediante la velocidad nodal - fase solida
                xp[mp - 1, 0] += dtime*Np[0, k]*nvel_s[nna, 0]
                xp[mp - 1, 1] += dtime*Np[0, k]*nvel_s[nna, 1]

    return xp


@njit(cache=True)
def BC_Dirichlet_acele_force_two_phases(active_nodes, fixed_nodesX, fixed_nodesY, nquantities):
    """Funcion que aplica condiciones de contorno en los nodos de Dirichlet - aceleraciones nodales
    Formulacion de doble fase y unico punto (v-w)"""

    nacele_w, nacele_s, nforce_w, niforce_w, neforce_w, ndforce_w, nforce_m, neforce_m, niforce_m = nquantities # Desempacando cantidades nodales

    # Ciclo en los nodos para fijar aceleraciones y fuerzas en los nodos segun restricciones del dominio
    for i in range(len(active_nodes)):
        # Ciclo en nodos para restriccion horizontal
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]: # El nodo activo i es un nodo de Dirichlet (fijo en x)

                nacele_s[i, 0] = 0 # Aceleracion nodal - Fase solida (en x)
                nacele_w[i, 0] = 0 # Aceleracion nodal - Fase liquida (en x)

                nforce_w[i, 0] = 0 # Fuerza nodal total - Fase liquida (en x)
                niforce_w[i, 0] = 0 # Fuerza nodal interna - Fase liquida (en x)
                neforce_w[i, 0] = 0 # Fueza nodal externa - Fase Liquida (en x)
                ndforce_w[i, 0] = 0 # Fuerza nodal de arrastre - Fase liquida (en x)

                nforce_m[i, 0] = 0 # Fuerza nodal total - Mezcla (en x)
                niforce_m[i, 0] = 0 # Fuerza nodal interna - Mezcla (en x)
                neforce_m[i, 0] = 0 # Fuerza nodal externa - Mezcla  (en x)

                break

        # Ciclo en nodos para restriccion vertical
        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]: # El nodo activo i es un nodo de Dirichlet (fijo en y)

                nacele_s[i, 1] = 0 # Aceleracion nodal - Fase solida  (en y)
                nacele_w[i, 1] = 0 # Aceleracion nodal - Fase liquida (en y)

                nforce_w[i, 1] = 0 # Fuerza nodal total - Fase liquida (en y)
                niforce_w[i, 1] = 0 # Fuerza nodal interna - Fase liquida (en y)
                neforce_w[i, 1] = 0 # Fueza nodal externa - Fase Liquida (en y)
                ndforce_w[i, 1] = 0 # Fuerza nodal de arrastre - Fase liquida (en y)

                nforce_m[i, 1] = 0 # Fuerza nodal total - Mezcla (en y)
                niforce_m[i, 1] = 0 # Fuerza nodal interna - Mezcla (en y)
                neforce_m[i, 1] = 0 # Fuerza nodal externa - Mezcla (en y)

                break

    return nacele_s, nacele_w, nforce_w, niforce_w, neforce_w, ndforce_w, nforce_m, neforce_m, niforce_m


@njit(cache=True)
def BC_Dirichlet_vel_two_phases(active_nodes, fixed_nodesX, fixed_nodesY, nvel_s, nvel_w):
    """Funcion que aplica las condiciones de contorno en los nodos de Dirichlet -  velocidades nodales nvel = 0
    Formulación de doble fase y unico punto (v-w) """

    for i in range(len(active_nodes)):
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]:
                # El nodo activo i es un nodo de Dirichlet (fijo en x)
                nvel_s[i, 0] = 0 # Restriccion de movimiento - Fase solida - en x
                nvel_w[i, 0] = 0 # Restriccion de movimiento - Fase liquida - Condicion de impermeabilidad - en x
                break

        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]:
                # El nodo activo i es un nodo de Dirichlet (fijo en y)
                nvel_s[i, 1] = 0 # Restriccion de movimiento - Fase solida - en y
                nvel_w[i, 1] = 0 # Restriccion de movimiento - Fase liquida - Condicion de impermeabilidad - en y
                break

    return nvel_s, nvel_w


@njit(cache=True)
def nodes_to_particle_stress_MP_and_pore_pressure_SRI_k_act_NUMBA(grid, particle, bound_val, nvel_s, nvel_w, dtime, elapla, Kw):
    """ Funcion que calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
        para el calculo del gradiente de velocida Lp - Metodo MUSL, doble transferencia
        Formulación doble fase - empleando Integración Selectiva Reducida para el calculo de los incrementos de la presion de poros
        Variable elapla = 0 (cero) Lineal elastico
                        = 1 (uno) Elastoplastico perfecto
    ACTUALIZA POROSIDAD PERO NO LA CONDUCTIVIDAD HIDRAULICA - K SE ASUME CONSTANTE EN TODA LA SIMULACION
    """

    assert (elapla == 1 or elapla == 0), "La variable elapla debe ser 0(cero) o 1(uno)"
    # Organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    Fp, Vp, Vp0, n_p, n_0p, k_p, k_0, n_0, epse_s, epsp_s, sig_e, sig_t, pp, shfnp, Prop = particle

    # ========================== Actualización de esfuerzos efectivos (Integracion en particulas) ==============================

    # Ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i]  # numero del elemento
        nodes = inci[ele - 1, :]  # nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i])  # MPs (particulas) en el elemento i

        # Ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j]  # Numero de mp - particulas
            # Organizando las funciones de forma y sus derivadas en el array correspondiente
            Np = shfnp[mp - 1, :].reshape((3, len(nodes)))

            Lp_s = np.zeros((2, 2))  # Creando matriz gradiente de velocidad de la particula MPs - Fase solida

            # Ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k]  # Numero del nodo global

                # -- Ciclo para determinar ubicacion del nodo en la lista de nodos activos --
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- Fin de ciclo - sino se compila usar funcion np.where

                # Calculo de gradiente de velocidad Fase solida - MPs y salir del ciclo en los nodos
                # Lp += np.array([[nvel[nna, 0]], [nvel[nna, 1]]]) * np.array([[Np[1, k], Np[2, k]]])
                Lp_s[0, 0] += nvel_s[nna, 0] * Np[1, k]
                Lp_s[0, 1] += nvel_s[nna, 0] * Np[2, k]
                Lp_s[1, 0] += nvel_s[nna, 1] * Np[1, k]
                Lp_s[1, 1] += nvel_s[nna, 1] * Np[2, k]

            # Calculo gradiente de deformacion fase solida - MPs
            F = np.dot((np.identity(2) + Lp_s * dtime), Fp[mp - 1, :].reshape((2, 2)))
            Fp[mp - 1, :] = F.reshape((1, 4))

            # Actualizar volumen de las particulas con la deformacion de fase solida
            Vp[mp - 1] = np.linalg.det(F) * Vp0[mp - 1]

            # Calculo de incremento de deformacion Fase solida y de esfuerzos efectivos
            deps1_s = dtime / 2 * (Lp_s + Lp_s.T)  # # incremento de deformacion para cada particula
            deps_s = np.array([deps1_s[0, 0], deps1_s[1, 1], 2 * deps1_s[0, 1]])  # tensor de incremento de deformacion en notacion de Voight
            nor_deps_s = np.linalg.norm(deps_s)  # norma del vector de deformacion en cada particula

            # Calculo de incremento de esfuerzos efectivos y actualizacion de tensor de esfuerzos efectivos
            if nor_deps_s == 0:
                # incremento de deformacion nulo!!
                pass
            else:
                # Incremento de deformacion no nulo!!

                # Actualizacion de esfuerzo - depende si eslastico o plastico
                if elapla == 0:
                    # Lineal elastico
                    C2D_stress = constitutive_matrix_elastic(1, Prop[mp - 1, 0], Prop[mp - 1, 1])  # matriz constitutiva condicion plana de esfuerzos
                    dsig_e = np.dot(C2D_stress, deps_s)  # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
                    dsig1_e = np.zeros(4)
                    dsig1_e[:3], dsig1_e[3] = dsig_e, Prop[mp - 1, 1] * (dsig_e[0] + dsig_e[1])
                    # Actualizar esfuerzo y deformacion sumando el incremento
                    epse_s[mp - 1, :] += deps_s
                    sig_e[mp - 1, :] += dsig1_e
                else:
                    # Elastoplastico
                    for m in range(10):
                        sig_e[mp - 1, :], depse_s, depsp_s, Prop[mp - 1, 5] = MC_elastoplastic2(sig_e[mp - 1, :], deps_s / 10, Prop[mp - 1, :])
                        epse_s[mp - 1, :] += depse_s
                        epsp_s[mp - 1, :] += depsp_s

    # ========================== Actualización de presion de poros (Puntos de Gauss - Selective Reductive Integration) ==============================

    # Ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i]  # Numero del elemento
        nodes = inci[ele - 1, :]  # Nodos asocidos al elemento
        xn = cor[nodes - 1, :]  # Coordenadas de los nodos
        mpe = elem_i_mp(mp_elem, active_elem[i])  # MPs (particulas) en el elemento i

        # Calculando el esfuerzo promedio a asignar - Gauss Points
        sigq_e = np.zeros(4)
        sigq_e[0] = np.sum(sig_e[mpe - 1, 0] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        sigq_e[1] = np.sum(sig_e[mpe - 1, 1] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        sigq_e[2] = np.sum(sig_e[mpe - 1, 2] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        sigq_e[3] = np.sum(sig_e[mpe - 1, 3] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])

        # Calculando el gradiente de deformacion promedio - Gauss Points
        Fq = np.zeros(4)
        Fq[0] = np.sum(Fp[mpe - 1, 0] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        Fq[1] = np.sum(Fp[mpe - 1, 1] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        Fq[2] = np.sum(Fp[mpe - 1, 2] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])
        Fq[3] = np.sum(Fp[mpe - 1, 3] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])

        Nq = shapfunc_gauss1(xn)  # Funciones de forma evaluadas - Gauss Points

        Lq_s = np.zeros((2, 2))  # Creando matriz gradiente de velocidad en los GPs - Fase solida
        Lq_w = np.zeros((2, 2))  # Creando matriz gradiente de velocidad en los GPs - Fase liquida

        # Calculando la presion de poros promedio - Gauss Points

        pp_q = np.zeros(3)
        pp_q[:] = np.sum(pp[mpe - 1, 0] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])

        # Calculando la porosidad promedio - Gauss Points

        n_q = np.sum(n_p[mpe - 1] * Vp[mpe - 1]) / np.sum(Vp[mpe - 1])  # Array con la porosidad promedio en los GPs - en cada elemento

        # Ciclo en los nodos del elemento
        for k in range(len(nodes)):
            nng = nodes[k]  # Numero del nodo global
            # -- Ciclo para determinar ubicacion del nodo en la lista de nodos activos --
            for m in range(len(active_nodes)):
                if active_nodes[m] == nng:
                    nna = m
                    break
            # -- Fin de ciclo --

            # Calculo de gradiente de velocidad Fase liquida - GPs y salir del ciclo en los nodos

            Lq_s[0, 0] += nvel_s[nna, 0] * Nq[1, k]
            Lq_s[0, 1] += nvel_s[nna, 0] * Nq[2, k]
            Lq_s[1, 0] += nvel_s[nna, 1] * Nq[1, k]
            Lq_s[1, 1] += nvel_s[nna, 1] * Nq[2, k]

            Lq_w[0, 0] += nvel_w[nna, 0] * Nq[1, k]
            Lq_w[0, 1] += nvel_w[nna, 0] * Nq[2, k]
            Lq_w[1, 0] += nvel_w[nna, 1] * Nq[1, k]
            Lq_w[1, 1] += nvel_w[nna, 1] * Nq[2, k]

        # Calculo de deformacion fase solida - Gauss Points
        deps1_s_q = dtime / 2 * (Lq_s + Lq_s.T)  # Incremento de deformacion - GPs
        deps_s_q = np.array([deps1_s_q[0, 0], deps1_s_q[1, 1], 2 * deps1_s_q[0, 1]])  # Incremento de deformacion en notacion de Voight
        deps_vol_s_q = deps_s_q[0] + deps_s_q[1]  # Deformacion volumetrica fase solida - GPs

        # Calculo de deformacion fase liquida - Gauss Points
        deps1_w_q = dtime / 2 * (Lq_w + Lq_w.T)  # Incremento de deformacion - GPs
        deps_w_q = np.array([deps1_w_q[0, 0], deps1_w_q[1, 1], 2 * deps1_w_q[0, 1]])  # Incremento de deformacion en notacion de Voight
        deps_vol_w_q = deps_w_q[0] + deps_w_q[1]  # Deformacion volumetrica fase liquida - GPs

        # Calculo de la presion de poros actualizada - Gauss Points
        pp_q += (Kw / n_q) * (((1 - n_q) * deps_vol_s_q) + (n_q * deps_vol_w_q))  # Actualizacion de la presion de poros para las particulas en cada elem - pp constante en cada elemento
        pp[mpe - 1, :] = pp_q

        # Calculo de porosidad actualizada en cada elemento - Gauss Points
        n_q = 1 - ((1 - n_q) / (1 + deps_vol_s_q))  # Porosidad actualizada de cada particula
        n_p[mpe - 1] = n_q

        # Calculo de la permeabilidad actualizada
        k_p[mpe - 1] = k_0 * ((1 - n_0) / (1 - n_q)) ** 2

    return Fp, Vp, epse_s, epsp_s, sig_e, pp, n_p, k_p
