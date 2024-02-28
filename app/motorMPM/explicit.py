## Modulo con las funciones para solucionar material point con esquema explicito
from __future__ import division, print_function
import numpy as np
from numba import njit, prange, vectorize
from _func.mesh import elem_i_mp
import math

# ===========================================================================
# ====== Funcion para el calculo del delta de tiempo para estabilidad =======

def deltatime(Ep, rhop, ele_size, factor):
    """Funcion que calcula el delta de tiempo necesario para convergencia 
       Courant-Friedrichs-Lewy - Velocidad del sonido en el material
        Argumentos: 
                    Ep = Array con el modulo de Young de las particulas
                    rhop = Array con la densidad de las particulas
                    ele_size = tamano de la malla de los elementos
                    factor = porcentaje en tanto por 1 del minimo delta de tiempo - recomendado 0.1
        
        Return: dt = delta de tiempo redondeado con un solo decimal diferente de cero"""
    
    c = math.sqrt(np.max(np.divide(Ep, rhop))) # maxima velocidad del sonido en el material
    dt = ele_size / c * factor # minimo delta de tiempo
    
    # redondeo del dt a un solo decimal distinto de cero
    sgn = -1 if dt < 0 else 1
    scale = int(-math.floor(math.log10(abs(dt))))
    if scale <= 0:
        scale = 1
    factor = 10**scale
    dt = sgn*math.floor(abs(dt)*factor)/factor
    
    return dt

# ====================================================================
# ====== Funcion para evaluar las funciones de forma del elemento trianglar lineal ====

@njit
def shape_func(x, y, xn):
    """Funcion que calcula las funciones de forma y sus derivadas evaluadas en xp
        x = coordenada x de la particula
        y = coordenada y de la particula
        xn = array con las coordenas de los nodos del elemento donde se encuentra la particula
        --------
        Return - Np = Array de 3 filas 
                        - En la primera fila estan las funciones de forma
                        - En la segunda fila las derivadas en x de las funciones de forma
                        - En la tercera fila las derivadas en y de las funciones de forma"""
    Np = np.zeros((3, len(xn)))
    x1, x2, x3 = xn[0, 0], xn[1, 0], xn[2, 0]
    y1, y2, y3 = xn[0, 1], xn[1, 1], xn[2, 1]
    A = 1/2*(x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2)
    # -- funciones de forma ---
    Np[0, 0] = 1/(2*A)*(x2*y3 - x3*y2 + (y2 - y3)*x + (x3 - x2)*y)
    Np[0, 1] = 1/(2*A)*(x3*y1 - x1*y3 + (y3 - y1)*x + (x1 - x3)*y)
    Np[0, 2] = 1/(2*A)*(x1*y2 - x2*y1 + (y1 - y2)*x + (x2 - x1)*y)
    # -- Dervidas en x de las funcioens de forma
    Np[1, 0] = 1/(2*A)*(y2 - y3)
    Np[1, 1] = 1/(2*A)*(y3 - y1)
    Np[1, 2] = 1/(2*A)*(y1 - y2)
    # -- Derivadas en y de las funciones de forma
    Np[2, 0] = 1/(2*A)*(x3 - x2)
    Np[2, 1] = 1/(2*A)*(x1 - x3)
    Np[2, 2] = 1/(2*A)*(x2 - x1)
    
    return Np

# ====================================================================
# === Funcion para evaluar las funciones de forma del elemento cuadrilateral bilineal ==

@njit
def shape_func2(x, y, xn):
    """Funcion que calcula las funciones de forma y sus derivadas evaluadas en xp
        x = coordenada x de la particula
        y = coordenada y de la particula
        xn = array con las coordenas de los nodos del elemento donde se encuentra la particula
        --------
        Return - Np = Array de 3 filas 
                        - En la primera fila estan las funciones de forma
                        - En la segunda fila las derivadas en x de las funciones de forma
                        - En la tercera fila las derivadas en y de las funciones de forma"""
    Np = np.zeros((3, len(xn)))
    x1, x2, x3, x4 = xn[0, 0], xn[1, 0], xn[2, 0], xn[3, 0]
    y1, y2, y3, y4 = xn[0, 1], xn[1, 1], xn[2, 1], xn[3, 1]
    a = 1/2 * (x2 - x1)
    b = 1/2 * (y4 - y1)
    
    # -- funciones de forma ---
    Np[0, 0] = 1 / (4*a*b) * (x - x2) * (y - y4)
    Np[0, 1] = -1 / (4*a*b) * (x - x1) * (y - y3)
    Np[0, 2] = 1 / (4*a*b) * (x - x4) * (y - y2)
    Np[0, 3] = -1 / (4*a*b) * (x - x3) * (y - y1)
    # -- Dervidas en x de las funcioens de forma
    Np[1, 0] = 1 / (4*a*b) * (y - y4)
    Np[1, 1] = -1 / (4*a*b) * (y - y3)
    Np[1, 2] = 1 / (4*a*b) * (y - y2)
    Np[1, 3] = -1 / (4*a*b) * (y - y1)
    # -- Derivadas en y de las funciones de forma
    Np[2, 0] = 1 / (4*a*b) * (x - x2)
    Np[2, 1] = -1 / (4*a*b) * (x - x1)
    Np[2, 2] = 1 / (4*a*b) * (x - x4)
    Np[2, 3] = -1 / (4*a*b) * (x - x3)
    
    return Np


# =======================================================================
# ====== Funcion que calcula el area del elemento ======================

@njit
def elem_area(xn):
    """Funcion que calcula el area del elemento
        xn = array con las coordenas de los nodos del elemento donde se encuentra la particula
        --------
        Return - A = el area de los elementos"""
    x1, x2, x3 = xn[0, 0], xn[1, 0], xn[2, 0]
    y1, y2, y3 = xn[0, 1], xn[1, 1], xn[2, 1]
    A = 1/2*(x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2)
    return A

# ==========================================================================
# === Funcion que calcula las funciones de forma para un punto de gauss ====

@njit
def shapfunc_gauss1(xn):
    """Funcion que calcula las funciones de forma evaluadas en el punto de gauss (1/3, 1/3, 1/3)
        xn = array con las coordenas de los nodos del elemento donde se encuentra la particula
        --------
        Return - Nq = Array de 3 filas 
                        - En la primera fila estan las funciones de forma
                        - En la segunda fila las derivadas en x de las funciones de forma
                        - En la tercera fila las derivadas en y de las funciones de forma"""
    Ng = np.zeros((3, len(xn)))
    x1, x2, x3 = xn[0, 0], xn[1, 0], xn[2, 0]
    y1, y2, y3 = xn[0, 1], xn[1, 1], xn[2, 1]
    A = 1/2*(x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2)
    # -- funciones de forma ---
    Ng[0, 0] = 1 / 3
    Ng[0, 1] = 1 / 3
    Ng[0, 2] = 1 / 3
    # -- Dervidas en x de las funcioens de forma
    Ng[1, 0] = 1/(2*A)*(y2 - y3)
    Ng[1, 1] = 1/(2*A)*(y3 - y1)
    Ng[1, 2] = 1/(2*A)*(y1 - y2)
    # -- Derivadas en y de las funciones de forma
    Ng[2, 0] = 1/(2*A)*(x3 - x2)
    Ng[2, 1] = 1/(2*A)*(x1 - x3)
    Ng[2, 2] = 1/(2*A)*(x2 - x1)
    return Ng

# ===================================================================
# ===== Funcion para transferir de las particulas a los nodos =======

@njit('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:])))')#, parallel=True)
def particles_to_nodes(grid, particle): 
    """ Funcion que transfiere la informacion de las particulas a lo nodos de la malla
        para un formulacion dinamica con matriz de masa agrupada
        ------
        Return ----
                nmass = vector de masa nodal de tamano igual al numero de nodos activos
                nmomentum = vetor de momentum nodal
                nforce = vetor de fuerzas nodal"""
    
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    xp, vp, Vp, Mp, sig, bp, tp = particle
    nnodes = len(active_nodes) # numero de nodos activos
    # --- incializar variables nodales ---
    nmass = np.zeros((nnodes, 1)) # vector de masa nodal
    nmomentum = np.zeros((nnodes, 2)) # vector de momentum nodal
    niforce = np.zeros((nnodes, 2)) # vector de fuerzas internas nodales
    neforce = np.zeros((nnodes, 2)) # vector de fuerzas externas nodales
    # -- crear array para las funciones de forma -- 
    shfnp = np.zeros((len(xp), inci.shape[1]*3)) # en cada fila las 3 funciones de forma y sus derivadas
    
    # ==================================================================
    
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        xn = cor[nodes - 1, :] # coordenasdas de los nodos
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            x = xp[mp - 1, 0]; y = xp[mp - 1, 1]
            Np = shape_func(x, y, xn) # funciones de forma y sus derivadas
            # guardando las funciones de forma y sus derivadas en el array correspondiente
            shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] = Np[0,0], Np[0,1], Np[0,2] # Ni
            shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] = Np[1,0], Np[1,1], Np[1,2] # Ni,x
            shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] = Np[2,0], Np[2,1], Np[2,2] # Ni,y
            
            # ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                nmass[nna, 0] += Np[0, k]*Mp[mp - 1] # masa nodal
                nmomentum[nna, 0] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 0] # momentum nodal en x
                nmomentum[nna, 1] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 1] # momentum nodal en y
                niforce[nna, 0] -= Vp[mp - 1]*(sig[mp - 1, 0]*Np[1, k] + sig[mp - 1, 2]*Np[2, k]) # fuerza interna en x
                niforce[nna, 1] -= Vp[mp - 1]*(sig[mp - 1, 2]*Np[1, k] + sig[mp - 1, 1]*Np[2, k]) # fuerza interna en y
                neforce[nna, 0] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 0] + Np[0, k]*tp[mp - 1, 0] #Fuerza externa en x
                neforce[nna, 1] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 1] + Np[0, k]*tp[mp - 1, 1] #Fuerza externa en y
    
    return nmass, nmomentum, niforce, neforce, shfnp

# =============================================================================
# === Funcion para tranferir de las particulas a los nodos - integra mixta ====

@njit('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:])), i8[:])')
def particles_to_nodes_gauss(grid, particle, bound_val): 
    """ Funcion que transfiere la informacion de las particulas a lo nodos de la malla
        para un formulacion dinamica con matriz de masa agrupada - Integracion mixta (Gauss y particulas)
        ------
        Return ----
                nmass = vector de masa nodal de tamano igual al numero de nodos activos
                nmomentum = vetor de momentum nodal
                nforce = vetor de fuerzas nodal"""
    
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    xp, vp, Vp, Mp, sig, bp, tp = particle
    nnodes = len(active_nodes) # numero de nodos activos
    # --- incializar variables nodales ---
    nmass = np.zeros((nnodes, 1)) # vector de masa nodal
    nmomentum = np.zeros((nnodes, 2)) # vector de momentum nodal
    niforce = np.zeros((nnodes, 2)) # vector de fuerzas internas nodales
    neforce = np.zeros((nnodes, 2)) # vector de fuerzas externas nodales
    # -- crear array para las funciones de forma -- 
    shfnp = np.zeros((len(xp), inci.shape[1]*3)) # en cada fila las 3 funciones de forma y sus derivadas
    
    # ==================================================================
    
    # ciclo en los elementos activos
    for i in prange(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        xn = cor[nodes - 1, :] # coordenasdas de los nodos
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        Vele = elem_area(xn) # Volumen de los elementos
        
        # verificacion si es un elemento lleno o parcialmente lleno
        if np.sum(bound_val[mpe - 1]) >= 1 and np.sum(Vp[mpe - 1]) < 0.9 * Vele:
            # el elemento es parcialmente lleno => aplicar integracion de particulas
            inte_ptcl = True
        else:
            # el elemento esta completamente lleno => apicar integracion de Gauss para niforce
            inte_ptcl = False
            # Calulando el esfuerzo promedio a asignar a el punto de Gauss
            sigq = np.zeros(3)
            sigq[0] = np.sum(sig[mpe - 1, 0]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            sigq[1] = np.sum(sig[mpe - 1, 1]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            sigq[2] = np.sum(sig[mpe - 1, 2]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            # solo se utiliza un punto de Gauss - (1/3, 1/3, 1/3)
            Nq = shapfunc_gauss1(xn) # funciones de forma evaluadas en el punto de Gauss
    
            # ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                # asignar fuerza interna a los nodos con las funciones de forma
                niforce[nna, 0] -= Vele*(sigq[0]*Nq[1, k] + sigq[2]*Nq[2, k]) # fuerza interna en x
                niforce[nna, 1] -= Vele*(sigq[2]*Nq[1, k] + sigq[1]*Nq[2, k]) # fuerza interna en y

        # Inicia ciclo para transferir las demas variables - integracion particulas        
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            x = xp[mp - 1, 0]; y = xp[mp - 1, 1]
            Np = shape_func(x, y, xn) # funciones de forma y sus derivadas
            # guardando las funciones de forma y sus derivadas en el array correspondiente
            shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] = Np[0,0], Np[0,1], Np[0,2] # Ni
            shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] = Np[1,0], Np[1,1], Np[1,2] # Ni,x
            shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] = Np[2,0], Np[2,1], Np[2,2] # Ni,y
            
            # ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                nmass[nna, 0] += Np[0, k]*Mp[mp - 1] # masa nodal
                nmomentum[nna, 0] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 0] # momentum nodal en x
                nmomentum[nna, 1] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 1] # momentum nodal en y
                neforce[nna, 0] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 0] + Np[0, k]*tp[mp - 1, 0] #Fuerza externa en x
                neforce[nna, 1] += Np[0, k]*Mp[mp - 1]*bp[mp - 1, 1] + Np[0, k]*tp[mp - 1, 1] #Fuerza externa en y
                # calcular las fuerzas internas si es integracion particulas !!!
                if inte_ptcl == True:
                    niforce[nna, 0] -= Vp[mp - 1]*(sig[mp - 1, 0]*Np[1, k] + sig[mp - 1, 2]*Np[2, k]) # fuerza interna en x
                    niforce[nna, 1] -= Vp[mp - 1]*(sig[mp - 1, 2]*Np[1, k] + sig[mp - 1, 1]*Np[2, k]) # fuerza interna en y
                

    return nmass, nmomentum, niforce, neforce, shfnp


# ====================================================================
# ==== Funcion para transferir de los nodos a las particulas la velocidad

def nodes_to_particle_vel(grid, particle, nquantities, dtime): 
    """ Funcion que calcula la velocidad y posicion de las particulas, transfiriendo de los nodos a las particulas
        Adicionalmente calcula la velocidad nodal - Metodo MUSL, doble transferencia
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal"""
    
    # organizando los argumentos de las listas
    nmass, nmomentum, nforce = nquantities
    # llamando la funcion interna
    xp, vp, nvel = nodes_to_particle_vel_inte(grid, particle, nquantities, dtime)
    nvel = np.divide(nvel, nmass) # dividiendo por la masa nodal
    
    return xp, vp, nvel


@njit('Tuple((f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:,:])), f8)')#, parallel=True)
def nodes_to_particle_vel_inte(grid, particle, nquantities, dtime): 
    """ Funcion interna de la funcion nodes_to_particle_vel"""
    
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    xp, vp, Vp, Mp, sig, shfnp = particle
    nmass, nmomentum, nforce = nquantities
    nnodes = len(active_nodes) # numero de nodos activos
    nvel = np.zeros((nnodes, 2))
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
            Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y
            
            # ciclo en los nodos del elemento
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                
                # calculo de velocidad y posicion de las particulas
                vp[mp - 1, 0] += dtime*Np[0, k]*nforce[nna, 0]/nmass[nna, 0]
                vp[mp - 1, 1] += dtime*Np[0, k]*nforce[nna, 1]/nmass[nna, 0]
                
                xp[mp - 1, 0] += dtime*Np[0, k]*nmomentum[nna, 0]/nmass[nna, 0] 
                xp[mp - 1, 1] += dtime*Np[0, k]*nmomentum[nna, 1]/nmass[nna, 0]
            
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                # calculo de la velocidad nodal
                nvel[nna, 0] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 0]
                nvel[nna, 1] += Np[0, k]*Mp[mp - 1]*vp[mp - 1, 1]
                    
    return xp, vp, nvel


# ===================================================================
# === Funcion para aplicar condiciones de contorno - momentum y fuerzas ====

@njit('Tuple((f8[:,:], f8[:,:]))(i8[:], i8[:], i8[:], f8[:,:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_momentum(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce):
    """Funcion que aplica condiciones de contorno en los nodos de Dirichlet"""
    
    for i in range(len(active_nodes)):
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]:
                # el nodo activo i es un nodo de Dirchlet (fijo en x)
                nmomentum[i, 0] = 0
                nforce[i, 0] = 0
                break
        
        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]:
                # el nodo activo i es un nodo de Dirchlet (fijo en y)
                nmomentum[i, 1] = 0
                nforce[i, 1] = 0
                break
                
    return nmomentum, nforce


# ===================================================================
# ===== Funcion para aplicar condiciones de contorno - velocidades ====

@njit('f8[:,:](i8[:], i8[:], i8[:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel):
    """Funcion que aplica las condiciones de contorno en los nodos de Dirichlet - vel = 0"""

    for i in range(len(active_nodes)):
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]:
                # el nodo activo i es un nodo de Dirchlet (fijo en x)
                nvel[i, 0] = 0
                break
        
        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]:
                # el nodo activo i es un nodo de Dirchlet (fijo en y)
                nvel[i, 1] = 0
                break

    return nvel

# ====================================================================
# ===== Funcion que devuelve la matriz constitutiva elastica lineal 2D =====

@njit
def constitutive_matrix_elastic(plane_condition, E, nu):
    '''Funcion para el calculo de la matriz constitutiva elastica lineal para condcion 
        plana de esfuerzo o plana de deformaciones
        plane_condition = escribir 0 (cero) para condicion plana de esfuerzos
                          escribir 1 (uno) para dondicion plana de deformacion
        E = Modulo de Young
        nu = Relacion de Poisson'''
    
    assert (plane_condition == 0 or plane_condition == 1), "El argumento plane_condition debe tener un valor de 0 o de 1 - mirar descripcion de la funcion"
    C2D = np.zeros((3, 3)) # creando array para la matriz de rigidez
    if plane_condition == 0:
        # condicion plana de esfuerzos
        C2D[0, 0], C2D[1, 1] = E / (1 - nu ** 2), E / (1 - nu ** 2)
        C2D[0, 1], C2D[1, 0] = E * nu / (1 - nu ** 2), E * nu / (1 - nu ** 2)
        C2D[2, 2] = E / 2 / (1 + nu)
    else:
        # condicion plana de deformaciones
        C2D[0, 0], C2D[1, 1] = E * (1 - nu)/ (1 + nu)/ (1 - 2 * nu), E * (1 - nu)/ (1 + nu)/ (1 - 2 * nu)
        C2D[0, 1], C2D[1, 0] = E * nu / (1 + nu)/ (1 - 2 * nu), E * nu / (1 + nu)/ (1 - 2 * nu)
        C2D[2, 2] = E / 2 / (1 + nu)
    
    return C2D


# ====================================================================
# === Funcion para transferir de los nodos a las particulas los esfeurzos ===

@njit('Tuple((f8[:,:], f8[:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:], f8[:], f8[:])), f8[:,:], f8 )')
def nodes_to_particle_stress(grid, particle, nvel, dtime): 
    """ Funcion que calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
        para el calculo del gradiente de velocida Lp - Metodo MUSL, doble transferencia
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal"""
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    Fp, Vp, Vp0, eps, sig, shfnp, Ep, nup = particle

    # ==================================================================
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            # organizado las funciones de forma y sus derivadas en el array correspondiente - solo funciona para elm trian
            Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y
            
            # ciclo en los nodos del elemento
            Lp = np.zeros((2, 2)) # creando matriz gradiente de velociad de la particula mp
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo - sino se compila usar funcion np.where
                
                # Calculo de gradiente de velocidad y salir del ciclo en los nodos
                #Lp += np.array([[nvel[nna, 0]], [nvel[nna, 1]]]) * np.array([[Np[1, k], Np[2, k]]])
                Lp[0, 0] += nvel[nna, 0]*Np[1, k]
                Lp[0, 1] += nvel[nna, 0]*Np[2, k]
                Lp[1, 0] += nvel[nna, 1]*Np[1, k]
                Lp[1, 1] += nvel[nna, 1]*Np[2, k]
            
            # Calculo gradiente de deformacion
            #F = np.dot((np.identity(2) + Lp*dtime), Fp[mp - 1, :].reshape((2, 2)))
            Fpt = np.zeros((2, 2)) # matriz grandiente deformacion en tiempo t
            Fpt[0, 0], Fpt[0, 1], Fpt[1, 0], Fpt[1, 1] = Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3]
            F = np.dot((np.identity(2) + Lp*dtime), Fpt) # matriz grandiente de deformacion en el tiempo t+1
            #Fp[mp - 1, :] = F.reshape((1, 4))
            Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3] = F[0, 0], F[0, 1], F[1, 0], F[1, 1] 
            # actualizar volumen de las particulas
            Vp[mp - 1] = np.linalg.det(F) * Vp0[mp - 1]
            # calculo de incremento de deformacion y de esfuerzos
            deps = dtime / 2 * (Lp + Lp.T) # se obtiene tensor de deformaciones!!
            C2D_stress = constitutive_matrix_elastic(0, Ep[mp - 1], nup[mp - 1]) # matriz constitutiva condicion plana de esfuerzos
            dsig = np.dot(C2D_stress, np.array([deps[0,0], deps[1,1], 2*deps[0,1]])) # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
            # Actualizar esfuerzo y deformacion sumando el incremento
            eps[mp - 1, :] += np.array([deps[0,0], deps[1,1], 2*deps[0,1]])
            sig[mp - 1, :] += dsig
                    
    return Fp, Vp, eps, sig


# ======================================================================================
# ============ Funcion para determinar equilibrio cuasi-estatico =======================

def static_convergence(nmass, niforce, neforce, ndamping, nvel, dtime, nework, ff, ee, t, efo, ifo):
    """Funcion para determinacion de equilibrio cuasi-estatico, a partir de la fuerza de desbalance
        y la energia cinetica de las fuerzas externas"""
    
    # criterio de balance de fuerzas
    ff[t] = np.linalg.norm(neforce + niforce)/np.linalg.norm(neforce)
    efo[t] = np.linalg.norm(neforce)
    ifo[t] = np.linalg.norm(niforce)
    # criterio de energia cinetica
    KE = 1/2*np.sum(nmass*nvel*nvel) # energia cinetica
    du = nvel*dtime # desplazamiento nodal
    nework += np.sum(du*neforce) # trabajo externo
    ee[t] = KE/nework
    
    return ff, ee, efo, ifo