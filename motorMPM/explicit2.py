## Modulo con las funciones para solucionar material point con esquema explicito
from __future__ import division, print_function
import numpy as np
from numba import njit, jit
from motorMPM.mesh import elem_i_mp
import math

# ===========================================================================
# ====== Funcion para el calculo del delta de tiempo para estabilidad =======

def deltatime(Ep, nu, rhop, ele_size, factor):
    """Funcion que calcula el delta de tiempo necesario para convergencia 
       Courant-Friedrichs-Lewy - Velocidad del sonido en el material
        Argumentos: 
                    Ep = Array con el modulo de Young de las particulas
                    nu = Array con el coeficiente de poisson de las particulas
                    rhop = Array con la densidad de las particulas
                    ele_size = tamano de la malla de los elementos
                    factor = porcentaje en tanto por 1 del minimo delta de tiempo - recomendado 0.1
        
        Return: dt = delta de tiempo redondeado con un solo decimal diferente de cero"""

    Eedo = (1 - nu) / (1 + nu) / (1 - 2*nu) * Ep
    c = math.sqrt(np.max(np.divide(Eedo, rhop.astype(float)))) # maxima velocidad del sonido en el material

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
# ====== Funcion para evaluar las funciones de forma del elemento trianglar lineal 
# ====== y del cuadrilateeral bilineal

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
    nnodes = len(xn[:,0]) # obtener el numero de nodos del elemento para determinar si es trangular o cudrilateral
    assert (nnodes == 3 or nnodes == 4), "Hay un error en el mallado"
    
    if nnodes == 3:
        # Elemento triangular lineal 
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
    else:
        # Elemento rectangular bilineal
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
    nnodes = len(xn[:,0]) # numero de nodos
    if nnodes == 3:
        # elemento triangular lineal
        x1, x2, x3 = xn[0, 0], xn[1, 0], xn[2, 0]
        y1, y2, y3 = xn[0, 1], xn[1, 1], xn[2, 1]
        A = 1/2*(x1*y2 - x1*y3 + x2*y3 - x2*y1 + x3*y1 - x3*y2)
    else:
        # elemento cuadrilateral bilineal
        x1, x2 = xn[0, 0], xn[1, 0]
        y1, y4 = xn[0, 1], xn[3, 1]
        a = 1/2 * (x2 - x1)
        b = 1/2 * (y4 - y1)
        A = 4*a*b
    
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
    
    nnodes = len(xn[:,0]) # obtener el numero de nodos del elemento para determinar si es trangular o cudrilateral
    assert (nnodes == 3 or nnodes == 4), "Hay un error en el mallado"
    
    Ng = np.zeros((3, len(xn)))
    if nnodes == 3:
        # Elemento triangular lineal
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
    else:
        # elemento cuadrilateral bilineal
        x1, x2, x3, x4 = xn[0, 0], xn[1, 0], xn[2, 0], xn[3, 0]
        y1, y2, y3, y4 = xn[0, 1], xn[1, 1], xn[2, 1], xn[3, 1]
        a = 1/2 * (x2 - x1)
        b = 1/2 * (y4 - y1)
        x = (x1 + x2)/2 # equivalente a shi=0
        y = (y4 + y1)/2 # equivalente a eta=0
        
        # -- funciones de forma ---
        Ng[0, 0] = 1 / (4*a*b) * (x - x2) * (y - y4)
        Ng[0, 1] = -1 / (4*a*b) * (x - x1) * (y - y3)
        Ng[0, 2] = 1 / (4*a*b) * (x - x4) * (y - y2)
        Ng[0, 3] = -1 / (4*a*b) * (x - x3) * (y - y1)
        # -- Dervidas en x de las funcioens de forma
        Ng[1, 0] = 1 / (4*a*b) * (y - y4)
        Ng[1, 1] = -1 / (4*a*b) * (y - y3)
        Ng[1, 2] = 1 / (4*a*b) * (y - y2)
        Ng[1, 3] = -1 / (4*a*b) * (y - y1)
        # -- Derivadas en y de las funciones de forma
        Ng[2, 0] = 1 / (4*a*b) * (x - x2)
        Ng[2, 1] = -1 / (4*a*b) * (x - x1)
        Ng[2, 2] = 1 / (4*a*b) * (x - x4)
        Ng[2, 3] = -1 / (4*a*b) * (x - x3)
        
    return Ng

# =========================================================================
# ======== Funcion para el calculo de los vectores normales ===============

def normals(nodos, node_support, active_elem, mp_elem, inci, cor, Mp, xp):
    """Funcion que calcula los vectores normales unitarios en direccion hacia
        afuera para la lista de nodos ingresados, se usa el metodo del gradiente
        de masa nodal"""
    
    # calculo array para almacenar vectores normales
    nor = np.zeros((len(nodos),2))
    
    # ciclo en los nodos
    for k in range(len(nodos)):
        nodo = nodos[k] # tomando el id del nodo
        elems = node_support[nodo - 1,:] # elementos asociados al nodo
        
        prueba = [elems[i] in active_elem for i in range(len(elems))]
        if np.any(prueba): # algun elemento asociado esta en los elementos activos
            pass
        #else:
            #print("El nodo no tiene elementos activos asociados !!")
        
        # ciclo en los elementos
        for i in range(len(elems)):
            ele = elems[i] # elemento i
            
            # ele puede ser = 0 en los nodos de la frontera!!!!
            if ele == 0:
                continue
                                    
            # determinar si el elemento i es un elemento activo
            nodes = inci[ele - 1,:] # nodos asocidos al elemento
            xn = cor[nodes - 1, :] # coordenasdas de los nodos
            
            if ele in active_elem:
                # el elemento i  es un nodo activo
                mpe = elem_i_mp(mp_elem, ele) # particulas dentro del elemento
                #if len(mpe) == 0:
                    #print("Error - entra a un nodo activo que no tiene particulas")
                
                # ciclo en las particulas
                for j in range(len(mpe)):
                    mp = mpe[j] # particula j
                    x = xp[mp - 1, 0]; y = xp[mp - 1, 1]
                    Np = shape_func(x, y, xn) # funciones de forma y sus derivadas
                    
                    # determinar id local del nodo dentro del elemento
                    idlocal = np.where(nodes == nodo)[0]
                    # calculo gradiente masa nodal
                    nor[k,0] += Np[1,idlocal]*Mp[mp-1]
                    nor[k,1] += Np[2,idlocal]*Mp[mp-1]
                # endfor particulas
            #endif
        #endfor elementos
    #endfor nodos
    magnitud = np.array([np.sqrt(nor[:,0]**2 + nor[:,1]**2)])
    error = np.where(magnitud[:,:] == 0)[0]
    #if len(error) > 0:
        #print("Magnitudes normales igual a cero")
    
    # normalizacion vectores
    normal = np.divide(nor, np.transpose(magnitud))
    #if np.any(np.isnan(normal) == True):
        #print("algunos valores del vector de normales unitario con NaN")
    
    return normal


# ===================================================================
# ===== Funcion para transferir de las particulas a los nodos =======

@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:])))')#, parallel=True)
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
    
    # ciclo en los elementos activos del sistema
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
            shfnp[mp - 1,:] = Np.reshape(3 * len(nodes))
            #shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] = Np[0,0], Np[0,1], Np[0,2] # Ni
            #shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] = Np[1,0], Np[1,1], Np[1,2] # Ni,x
            #shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] = Np[2,0], Np[2,1], Np[2,2] # Ni,y
            
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

# ==============================================================================
# ==== Funcion para calcular el esfuerzo en los puntos de Gauss ================
    
@njit
def stress_gausspoint(xp, Vp, sig, mpe, xn):
    """ Funcion que calcula el esfuerzo en el punto de gauss para el elemnto cuadrilateral
        teniendo en cuenta una distribucion de efuerzos lineales dentro del elemento"""
    
    # Calcular las coordenas del punto de gauss - Centro del elemento
    x = (xn[0, 0] + xn[1, 0])/2 # equivalente a shi=0
    y = (xn[3, 1] + xn[0, 1])/2 # equivalente a eta=0
    
    sigq = np.zeros(3) # vector donde se guardan los esfuerzos en el punto de gauss
    LS_Ma = np.zeros((3,3)) # MAtriz con los coefcientes del sistema de Ec de minimos cuadrados
    
    # llenado la Ma de minimos cuadrados
    LS_Ma[0,0] = np.sum(Vp[mpe-1])
    LS_Ma[0,1] = np.sum(np.multiply(xp[mpe-1,0], Vp[mpe-1]))
    LS_Ma[0,2] = np.sum(np.multiply(xp[mpe-1,1], Vp[mpe-1]))
    LS_Ma[1,0] = LS_Ma[0,1]
    LS_Ma[1,1] = np.sum(np.multiply(np.multiply(xp[mpe-1,0], xp[mpe-1,0]), Vp[mpe-1]))
    LS_Ma[1,2] = np.sum(np.multiply(np.multiply(xp[mpe-1,0], xp[mpe-1,1]), Vp[mpe-1]))
    LS_Ma[2,0] = LS_Ma[0,2]
    LS_Ma[2,1] = LS_Ma[1,2]
    LS_Ma[2,2] = np.sum(np.multiply(np.multiply(xp[mpe-1,1], xp[mpe-1,1]), Vp[mpe-1]))
    
    # ciclo en las 3 componentes de esfuerzo
    for i in range(3):
        LS_Ve = np.zeros(3)
        LS_Ve[0] = np.sum(np.multiply(sig[mpe-1,i], Vp[mpe-1]))
        LS_Ve[1] = np.sum(np.multiply(np.multiply(xp[mpe-1,0], sig[mpe-1,i]), Vp[mpe-1]))
        LS_Ve[2] = np.sum(np.multiply(np.multiply(xp[mpe-1,1], sig[mpe-1,i]), Vp[mpe-1]))
        
        # solucionado el sistema de ecuaciones de minimos cuadrados
        alpha = np.linalg.solve(LS_Ma, LS_Ve)
        # Calculando el esfuerzo correspondiente en el punto de gauss
        sigq[i] = alpha[0] + alpha[1]*x + alpha[2]*y
    
    return sigq
        
# =============================================================================
# === Funcion para tranferir de las particulas a los nodos - integra mixta ====

@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:])), i8[:])')
def particles_to_nodes_gauss(grid, particle, bound_val): 
    """ Funcion que transfiere la informacion de las particulas a lo nodos de la malla
        para un formulacion dinamica con matriz de masa agrupada - Integracion mixta (Gauss y particulas)
        Elemento cuadrilateral bilineal con valor por distribucion lineal en el punto de Gauss
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
        Vele = elem_area(xn) # Volumen de los elementos
        
        # verificacion si es un elemento lleno o parcialmente lleno
        if np.sum(bound_val[mpe - 1]) >= 1 and np.sum(Vp[mpe - 1]) < 0.9 * Vele:
            # el elemento es parcialmente lleno => aplicar integracion de particulas
            inte_ptcl = True
        else:
            # el elemento esta completamente lleno => apicar integracion de Gauss para niforce
            inte_ptcl = False
            
            # Calulando el esfuerzo promedio a asignar a el punto de Gauss
            if len(nodes) == 3: # elemento triangular lineal
                sigq = np.zeros(3)
                sigq[0] = np.sum(sig[mpe - 1, 0]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
                sigq[1] = np.sum(sig[mpe - 1, 1]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
                sigq[2] = np.sum(sig[mpe - 1, 2]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            elif len(nodes) == 4: # elemento cuadrilateral bilineal
                sigq = stress_gausspoint(xp, Vp, sig, mpe, xn)
                            
            # solo se utiliza un punto de Gauss
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
            shfnp[mp - 1,:] = Np.reshape(3 * len(nodes))
            
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

# =============================================================================
# === Funcion para tranferir de las particulas a los nodos - integra mixta ====

@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:])), i8[:])')
def particles_to_nodes_gauss2(grid, particle, bound_val): 
    """ Funcion que transfiere la informacion de las particulas a lo nodos de la malla
        para un formulacion dinamica con matriz de masa agrupada - Integracion mixta (Gauss y particulas)
        Elemento cuadrilateral bilineal con valor promedio en el punto de gauss
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
            # solo se utiliza un punto de Gauss
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
            shfnp[mp - 1,:] = Np.reshape(3 * len(nodes))
            
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
    nvel = np.divide(nvel, nmass, out=np.zeros_like(nvel), where=nmass !=0) # dividiendo por la masa nodal
    
    return xp, vp, nvel


@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:])), Tuple((f8[:,:], f8[:,:], f8[:,:])), f8)')#, parallel=True)
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

@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:], f8[:,:]))(i8[:], i8[:], i8[:], f8[:,:], f8[:,:], f8[:,:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_momentum(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce,  niforce, neforce):
    """Funcion que aplica condiciones de contorno en los nodos de Dirichlet"""
    
    for i in range(len(active_nodes)):
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]:
                # el nodo activo i es un nodo de Dirchlet (fijo en x)
                nmomentum[i, 0] = 0
                nforce[i, 0] = 0
                niforce[i, 0] = 0
                neforce[i, 0] = 0
                break
        
        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]:
                # el nodo activo i es un nodo de Dirchlet (fijo en y)
                nmomentum[i, 1] = 0
                nforce[i, 1] = 0
                niforce[i, 1] = 0
                neforce[i, 1] = 0
                break
                
    return nmomentum, nforce, niforce, neforce


# ===================================================================
# === Funcion para aplicar condiciones de contorno - momentum y fuerzas ====

@njit#('Tuple((f8[:,:], f8[:,:], f8[:,:]))(i8[:], i8[:], i8[:], f8[:,:], f8[:,:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_momentum2(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, niforce, neforce):
    """Funcion que aplica condiciones de contorno en los nodos de Dirichlet"""
    
    for i in range(len(active_nodes)):
        for j in range(len(fixed_nodesX)):
            if active_nodes[i] == fixed_nodesX[j]:
                # el nodo activo i es un nodo de Dirchlet (fijo en x)
                nmomentum[i, 0] = 0
                niforce[i, 0] = 0
                neforce[i, 0] = 0
                break
        
        for k in range(len(fixed_nodesY)):
            if active_nodes[i] == fixed_nodesY[k]:
                # el nodo activo i es un nodo de Dirchlet (fijo en y)
                nmomentum[i, 1] = 0
                niforce[i, 1] = 0
                neforce[i, 1] = 0
                break
                
    return nmomentum, niforce, neforce

# ===================================================================
# === Funcion para aplicar condiciones de contorno - momentum y fuerzas ====

@njit#('Tuple((f8[:,:], f8[:,:]))(i8[:], i8[:], i8[:], f8[:,:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce):
    """Funcion que aplica condiciones de contorno en los nodos de Dirichlet al vector de fuerza nodal total"""
    
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

@njit#('f8[:,:](i8[:], i8[:], i8[:], f8[:,:])')#, parallel=True)
def BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel):
    """Funcion que aplica las condiciones de contorno en los nodos de Dirichlet - nvel = 0"""

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


# =============================================================================
# ==== Funcion para el calculo de la funcion de fluencia Mohr-Coulomb =========

@njit
def MCyield2(sig, Prop, Tr):
    """ Funcion que calcula la funcion de fluencia para el estado de esfuerzos ingresado de un punto material
        La funcion de fluencia corresponde al criterio de mohr-Coulomb modificado por Abbo-Sloan(1985) para elminar
        las singularidades de la funcion original, a traves de una funcion hiperbolica en el plano meridonial y una 
        trigonometrica en el plano desviador o plano pi"""
        
    # Angulo de Transicion
    Trang = 0.5061454830783556 # 29 grados
    
    # Variables de las propiedades
    Coh = Prop[2] # Cohesion
    Phi = Prop[3] # Angulo de friccion
    
    # Calculo del valor a de aproximacion hiperbola
    if Prop[3] > 0:
        aa = 0.05 * Coh / math.tan(Phi)
    else:
        aa = 0 # para el caso Tresca
        
    # Variables del estado de esfuerzos
    sigxx = sig[0]
    sigyy = sig[1]
    sigxy = sig[2]
    sigzz = sig[3] #nu * (sigxx + sigyy)
    
    # Calculo de las invariantes de esfuerzo
    P = 1/3 * (sigxx + sigyy + sigzz) # Esfuerzo hidroestatico - normal equivalente - SIGM
    Sx, Sy, Sz = sigxx - P, sigyy - P, sigzz - P # Desviadores de esfuerzo
    J2 = 0.5 * (Sx**2 + Sy**2 + Sz**2) + sigxy**2 # Segunda invariante de esfuerzo desviador
    J3 = Sz * (Sx*Sy - sigxy**2) # Tercera invariante de esfuerzo desviador
    J = J2**(0.5) # Esfuerzo cortante equivalente - SBAR
    
    # verificar caso de desviador nulo y calcular angulo de Lode
    if J2 > 0: # con una tolerancia o no???
        S3TA = -3*(3)**(0.5) / 2 * J3 / (J**3)
        if S3TA > 1:
            S3TA = 1
        if S3TA < -1:
            S3TA = -1
        
        Theta = 1/3 * math.asin(S3TA) # Angulo de Lode
    else:
        Theta = 0 # Angulo de Lode para el caso de desviador nulo
    
    # Calcular el valor K(theta) que define la superficie en el plano desviador
    if abs(Theta) < Trang: # Region no redondeada
        K = math.cos(Theta) - 1/(3**0.5)*math.sin(Phi)*math.sin(Theta)
    else: # Region redondeada - Aprox trigonometrica
        # coeficientes y factor A
        A1 = 3.958192584288055
        A2 = 2.93184419579309
        A = A1 + A2 * math.copysign(1,Theta) * math.sin(Phi)
        # coeficientes y factor B
        B1 = 3.0878046060459123
        B2 = 3.216156791654838
        B = B1 * math.copysign(1,Theta) + B2 * math.sin(Phi)
        # Calculo del valor K
        K = A - B * math.sin(3*Theta)
    
    # Calcular funcion de fluencia
    Fmc = P*math.sin(Phi) + ((J*K)**2 + (aa*math.sin(Phi))**2)**(0.5) - Coh*math.cos(Phi)           
    
    return Fmc

# =============================================================================
# === Funcion que calcula el gradiente de la funcion de fluencia y potencial plastico MC ==

@njit
def MCgrad2(sig, Prop, Tr, potential):
    """Funcion que calcula las derivadas de la funcion de fluencia F respecto al estado de esfuerzos
        - Mohr coulomb modificada por abbo sloan(1985) valido para condicion plana de deformaciones
        - La variable potential se usa para determinar si el gradiente evaluado es en la funcion de fluencia o en el
            potencial plasticos, si es potencial plastico se usa el angulo de dilancia en lugar del angulo de friccion
            potential = 0 : Calculo gradiente de funcion de fluencia
            potential = 1 : Calculo gradiente del potencial plastico
        Retorna vector con las derivadas de la funcion de fluencia respecto a los esfuerzos"""
    
    assert (potential == 1 or potential == 0), "El argumento Potential debe ser 1=Potential plastic o 0=Yield function"
    
    # Angulo de Transicion
    Trang = 0.5061454830783556 # 29 grados
    
    # Variables de las propiedades
    Coh = Prop[2] # Cohesion   
    if potential == 1:
        Phi = Prop[4] # Angulo de dilatancia
    else:
        Phi = Prop[3] # Angulo de friccion
    
    # Contante a aproximacion hiperbola
    if Phi > 0:
        aa = 0.05 * Coh / math.tan(Phi)
        Tresca = False
    else:
        Tresca = True
        aa = 0 # para el caso Tresca
    
    # Variables del estado de esfuerzos
    sigxx = sig[0]
    sigyy = sig[1]
    sigxy = sig[2]
    sigzz = sig[3] #nu * (sigxx + sigyy)
    
    # Calculo de las invariantes de esfuerzo
    P = 1/3 * (sigxx + sigyy + sigzz) # Esfuerzo hidroestatico - normal equivalente - SIGM
    Sx, Sy, Sz = sigxx - P, sigyy - P, sigzz - P # Desviadores de esfuerzo
    J2 = 0.5 * (Sx**2 + Sy**2 + Sz**2) + sigxy**2 # Segunda invariante de esfuerzo desviador
    J3 = Sz * (Sx*Sy - sigxy**2) # Tercera invariante de esfuerzo desviador
    J = J2**(0.5) # Esfuerzo cortante equivalente
    
    # verificacion caso de desviador nulo y calcular angulo de Lode
    if J2 > 0: # con una tolerancia o no???
        S3TA = -3*(3)**(0.5)/2 * J3 / (J**3)
        if S3TA > 1:
            S3TA = 1
        if S3TA < -1:
            S3TA = -1
        Theta = 1/3 * math.asin(S3TA) # Angulo de Lode
    else: 
        Theta = 0 # Angulo de Lode para el caso de desviador nulo
        
    # Calculo K(theta) y su derivada que define la superficie en el plano desviador
    if abs(Theta) < Trang: # Region no redondeada
        K = math.cos(Theta) - 1/(3)**(0.5)*math.sin(Phi)*math.sin(Theta)
        dK = math.sin(Theta) + 1/(3)**(0.5)*math.sin(Phi)*math.cos(Theta)
    else: # Region redondeada - Aprox trigonometrica
        # coeficientes y factor A
        A1 = 3.958192584288055
        A2 = 2.93184419579309
        A = A1 + A2 * math.copysign(1,Theta) * math.sin(Phi)
        # coeficientes y factor B
        B1 = 3.0878046060459123
        B2 = 3.216156791654838
        B = B1 * math.copysign(1,Theta) + B2 * math.sin(Phi)
        # Calculo del valor K
        K = A - B * math.sin(3*Theta)
        dK = 3*B * math.cos(3*Theta)
    
    # Calculo coeficientes de los gradientes para Mohr-Coulomb hiperbolico
    if J2 > 0 :
        # si hay esfuerzo desviador
        alpha = J*K / ((J*K)**2 + (aa*math.sin(Phi))**2)**(0.5)
        C1 = math.sin(Phi)
        C2 = alpha * (K + math.tan(3*Theta)*dK)
        C3 = alpha * ((3)**(0.5)*dK / (2*math.cos(3*Theta)*J2))
    else:
        # caso de desviador nulo
        C1 = math.sin(Phi)
        C2, C3 = 0, 0
        # valores para evitar division por cero
        J2, J = 1e-15, 1e-15
        if Tresca == True:
            print("Warning: Criterio de Tresca no puede fluir para el caso desviador cero!")
    
    # Calculo gradientes
    dF = np.zeros(4)
    dF[0] = C1/3 + C2/2/J*Sx + C3*(Sy*Sz + J2/3) # Derivada de F respecto a Sigxx
    dF[1] = C1/3 + C2/2/J*Sy + C3*(Sx*Sz + J2/3) # Derivada de F respecto a Sigyy
    dF[2] = 2*sigxy * (C2/2/J - C3*Sz) # Derivada de F respecto a Sigxy
    dF[3] = C1/3 + C2/2/J*Sz + C3*(Sx*Sy - sigxy**2 + J2/3) # Derivada de F respecto a Sigzz
    
    return dF



# ==================================================================================



# =============================================================================
# ==== Funcion para el calculo de la funcion de fluencia Mohr-Coulomb =========

@njit
def MCyield(sig, Prop, Tr):
    """ Funcion que calcula la funcion de fluencia para el estado de esfuerzos ingresado de un punto material
        La funcion de fluencia corresponde al criterio de mohr-Coulomb modificado por Abbo-Sloan(1985) para elminar
        las singularidades de la funcion original, a traves de una funcion hiperbolica en el plano meridonial y una 
        trigonometrica en el plano desviador o plano pi"""
    
    # Angulo de Transicion
    Trang = math.radians(Tr) 
    # Constante de aproximacion de la hiperbola en el apice
    aa = 0.1
    
    # Variables de las propiedades
    Coh = Prop[2] # Cohesion
    Phi = Prop[3] # Angulo de friccion
    
    # Calculo del valor a de aproximacion hiperbola
    if Prop[3] > 0:
        aa = aa * Coh/math.tan(Phi)
    else:
        aa = 0 # para el caso Tresca
        
    # Variables del estado de esfuerzos
    sigxx = sig[0]
    sigyy = sig[1]
    sigxy = sig[2]
    sigzz = sig[3] #nu * (sigxx + sigyy)
    
    # Calculo de las invariantes de esfuerzo
    P = 1/3 * (sigxx + sigyy + sigzz) # Esfuerzo hidroestatico - normal equivalente - SIGM
    Sx, Sy, Sz = sigxx - P, sigyy - P, sigzz - P # Desviadores de esfuerzo
    J2 = 1/2 * (Sx**2 + Sy**2 + Sz**2) + sigxy**2 # Segunda invariante de esfuerzo desviador
    J3 = Sz * (Sx*Sy - sigxy**2) # Tercera invariante de esfuerzo desviador
    J = J2**(1/2) # Esfuerzo cortante equivalente - SBAR
    
    # verificar caso de desviador nulo y calcular angulo de Lode
    if J2 > 0: # con una tolerancia o no???
        S3TA = -3*(3)**(1/2)/2 * J3 / (J**3)
        if S3TA > 1:
            S3TA = 1
        if S3TA < -1:
            S3TA = -1
        
        Theta = 1/3 * math.asin(S3TA) # Angulo de Lode
    else:
        Theta = 0 # Angulo de Lode para el caso de desviador nulo
    
    # Calcular el valor K(theta) que define la superficie en el plano desviador
    if abs(Theta) < Trang: # Region no redondeada
        K = math.cos(Theta) - 1/(3)**(1/2)*math.sin(Phi)*math.sin(Theta)
    else: # Region redondeada - Aprox trigonometrica
        # coeficientes y factor A
        A1 = 1/3*math.cos(Trang) * (3 + math.tan(Trang)*math.tan(3*Trang)) 
        A2 = 1/3*math.cos(Trang) / (3)**(1/2) * (math.tan(3*Trang) - 3*math.tan(Trang))
        A = A1 + A2 * math.copysign(1,Theta) * math.sin(Phi)
        # coeficientes y factor B
        B1 = 1/3/math.cos(3*Trang) * math.sin(Trang)
        B2 = 1/3/math.cos(3*Trang) / (3)**(1/2) * math.cos(Trang)
        B = B1 * math.copysign(1,Theta) + B2 * math.sin(Phi)
        # Calculo del valor K
        K = A - B * math.sin(3*Theta)
    
    # Calcular funcion de fluencia
    Fmc = P*math.sin(Phi) + ((J*K)**2 + (aa*math.sin(Phi))**2)**(1/2) - Coh*math.cos(Phi)           
    
    return Fmc

# =============================================================================
# === Funcion que calcula el gradiente de la funcion de fluencia y potencial plastico MC ==

@njit
def MCgrad(sig, Prop, Tr, potential):
    """Funcion que calcula las derivadas de la funcion de fluencia F respecto al estado de esfuerzos
        - Mohr coulomb modificada por abbo sloan(1985) valido para condicion plana de deformaciones
        - La variable potential se usa para determinar si el gradiente evaluado es en la funcion de fluencia o en el
            potencial plasticos, si es potencial plastico se usa el angulo de dilancia en lugar del angulo de friccion
            potential = 0 : Calculo gradiente de funcion de fluencia
            potential = 1 : Calculo gradiente del potencial plastico
        Retorna vector con las derivadas de la funcion de fluencia respecto a los esfuerzos"""
    
    assert (potential == 1 or potential == 0), "El argumento Potential debe ser 1=Potential plastic o 0=Yield function"
    
    # Angulo de Transicion
    Trang = math.radians(Tr) 
    # Constante de aproximacion de la hiperbola en el apice
    aa = 0.1
    
    # Variables de las propiedades
    Coh = Prop[2] # Cohesion   
    if potential == 1:
        Phi = Prop[4] # Angulo de dilatancia
    else:
        Phi = Prop[3] # Angulo de friccion
    
    # Contante a aproximacion hiperbola
    if Phi > 0:
        aa = aa * Coh/math.tan(Phi)
        Tresca = False
    else:
        Tresca = True
        aa = 0 # para el caso Tresca
    
    # Variables del estado de esfuerzos
    sigxx = sig[0]
    sigyy = sig[1]
    sigxy = sig[2]
    sigzz = sig[3] #nu * (sigxx + sigyy)
    
    # Calculo de las invariantes de esfuerzo
    P = 1/3 * (sigxx + sigyy + sigzz) # Esfuerzo hidroestatico - normal equivalente - SIGM
    Sx, Sy, Sz = sigxx - P, sigyy - P, sigzz - P # Desviadores de esfuerzo
    J2 = 1/2 * (Sx**2 + Sy**2 + Sz**2) + sigxy**2 # Segunda invariante de esfuerzo desviador
    J3 = Sz * (Sx*Sy - sigxy**2) # Tercera invariante de esfuerzo desviador
    J = J2**(0.5) # Esfuerzo cortante equivalente
    
    # verificacion caso de desviador nulo y calcular angulo de Lode
    if J2 > 0: # con una tolerancia o no???
        S3TA = -3*(3)**(0.5)/2 * J3 / (J**3)
        if S3TA > 1:
            S3TA = 1
        if S3TA < -1:
            S3TA = -1
        Theta = 1/3 * math.asin(S3TA) # Angulo de Lode
    else: 
        Theta = 0 # Angulo de Lode para el caso de desviador nulo
        
    # Calculo K(theta) y su derivada que define la superficie en el plano desviador
    if abs(Theta) < Trang: # Region no redondeada
        K = math.cos(Theta) - 1/(3)**(0.5)*math.sin(Phi)*math.sin(Theta)
        dK = math.sin(Theta) + 1/(3)**(0.5)*math.sin(Phi)*math.cos(Theta)
    else: # Region redondeada - Aprox trigonometrica
        # coeficientes y factor A
        A1 = 1/3*math.cos(Trang) * (3 + math.tan(Trang)*math.tan(3*Trang)) 
        A2 = 1/3*math.cos(Trang) / (3)**(0.5) * (math.tan(3*Trang) - 3*math.tan(Trang))
        A = A1 + A2 * math.copysign(1,Theta) * math.sin(Phi)
        # coeficientes y factor B
        B1 = 1/3/math.cos(3*Trang) * math.sin(Trang)
        B2 = 1/3/math.cos(3*Trang) / (3)**(0.5) * math.cos(Trang)
        B = B1 * math.copysign(1,Theta) + B2 * math.sin(Phi)
        # Calculo del valor K
        K = A - B * math.sin(3*Theta)
        dK = 3*B * math.cos(3*Theta)
    
    # Calculo coeficientes de los gradientes para Mohr-Coulomb hiperbolico
    if J2 > 0 :
        # si hay esfuerzo desviador
        alpha = J*K / ((J*K)**2 + (aa*math.sin(Phi))**2)**(0.5)
        C1 = math.sin(Phi)
        C2 = alpha * (K + math.tan(3*Theta)*dK)
        C3 = alpha * ((3)**(0.5)*dK / (2*math.cos(3*Theta)*J2))
    else:
        # caso de desviador nulo
        C1 = math.sin(Phi)
        C2, C3 = 0, 0
        # valores para evitar division por cero
        J2, J = 1e-15, 1e-15
        if Tresca == True:
            print("Warning: Criterio de Tresca no puede fluir para el caso desviador cero!")
    
    # Calculo gradientes
    dF = np.zeros(4)
    dF[0] = C1/3 + C2/2/J*Sx + C3*(Sy*Sz + J2/3) # Derivada de F respecto a Sigxx
    dF[1] = C1/3 + C2/2/J*Sy + C3*(Sx*Sz + J2/3) # Derivada de F respecto a Sigyy
    dF[2] = 2*sigxy * (C2/2/J - C3*Sz) # Derivada de F respecto a Sigxy
    dF[3] = C1/3 + C2/2/J*Sz + C3*(Sx*Sy - sigxy**2 + J2/3) # Derivada de F respecto a Sigzz
    
    return dF




# ==================================================================================
# === Funcion para el calculo de esfuerzos y deformaciones ELASTOPLASTICIDAD =======

@njit
def MC_elastoplastic(sigA, deps, Prop, epse, epsp, mp):
    """Funcion que calcula el estado de esfuerzo, el incremento de deformacion elastica y plastica
        de acuerdo con la formulacion de Mohr-Coulomb de Abbo-Sloan elasto plastica perfecta"""
    Tr = 29 # angulo de transicion que puede ser modificado

    # parametros de la particula mp-1
    E = Prop[0] # Modulo de Young
    nu = Prop[1] # Coeficiente de Poisson
    Yield = Prop[5] # variable que indica si la aprticula se ha plastifiado o no
    
    # Matriz de rigidez elastica lineal
    De = constitutive_matrix_elastic(1, E, nu)
    # matriz elastica lineal de (4x4) - termino sigzz
    De4 = np.zeros((4,4))
    De4[:3,:3] = De
    De4[0,3], De4[3,0] = De[0,1], De[0,1]
    De4[1,3], De4[3,1] = De[0,1], De[0,1]
    De4[3,3] = De[0,0]
    
    # Esfuerzo trial elastico - td el incremento es elastico
    dsigt = np.dot(De, deps)
    dsig = np.zeros(len(dsigt)+1)
    dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
    
    sigC = sigA + dsig
    # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
    FsigC = MCyield(sigC, Prop, Tr)
    
    # === CONDICION PARA SABER SI EL INCREMENTO ES SOLO ELASTICO
    if FsigC < 0:
        # El incremento es elastico
        sigD2 = sigC
        epse += deps
    else:
        # Incremento elastoplastico
        FsigA = MCyield(sigA, Prop, Tr) # en el estado inicial
        if FsigA < 0:
            # La particula no se habia plasticido en la iteracion anterior
            alp1 = FsigA / (FsigA - FsigC) # primera aproximacion de alpha
            sigk1 = sigA + alp1 * dsig # primera aproxiamcion del esfuerzo
            Fsigk1 = MCyield(sigk1, Prop, Tr)
            #error = np.linalg.norm(sigk1 - sigA) / np.linalg.norm(sigA)
            error = 1e-3
            while error > 1e-10:              
                sigk = sigk1 # tomando el esfuerzo anterior
                alp = alp1 # el alpha anterior
                Fsigk = MCyield(sigk, Prop, Tr)
                ak = MCgrad(sigk, Prop, Tr, 0)
                alp1 = alp - Fsigk / (np.dot(ak, dsig)) # Newton Raphson
                #print("alpha nicial: ", alp, "  alpha final: ", alp1)
                sigk1 = sigA + alp1*dsig # actualizacion del esfuerzo
                # calculo del error
                error = np.linalg.norm(sigk1 - sigk) / np.linalg.norm(sigk)
            
            sigB = sigk1 # asignando el valor de la iteracion con el esfuerzo en la s de fluencia
            R = 1 - alp1 # R como el complemente de alpha - valor de esfuerzo a ajustar
        else:
            # La particula se habia plastificado en la iteracion anterior
            R = 1
            sigB = sigA # todo el incremento se debe corregir
        
        # calculando la funcion de fluencia y derivadas en el punto B - sobre F=0
        
        # SE DEBE TOMAR EL TERMINO F - SIGZZ??????
        FsigB = MCyield(sigB, Prop, Tr)
        if abs(FsigB) > 1e-6:
            print("Warning: F en B = ", FsigB, "Valor en primera aprox ", Fsigk1)
        
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        #dsig3 = dsig[:3]
        
        # Calculo del multiplicador plastico
        lam = (np.dot(aB, dsig))/(R * np.dot(aB, np.dot(De4, aBpr))) # con termino sigz
        if lam < 0:
            # valor de lambda negativo
            print("Warning: Multiplicador plastico negativo!!")
        
        #lam = (np.dot(aB[:3], dsig3))/(R * np.dot(aB[:3], np.dot(De, aBpr[:3]))) # sin termino sigz
        
        # Calculo de esfuerzo en D - que esta fuera de la superficie de fluencia
        #sigD = sigC[:3] - lam * np.dot(De, aBpr[:3]) # sin el termino sigz
        #sigD = np.append(sigD, nu *(sigD[0] + sigD[1])) # garantizando plane strain
        
        sigD = sigC - lam * np.dot(De4, aBpr) # con el termino sigz
        
        # Calculo de la funcion de fluencia
        FsigD = MCyield(sigD, Prop, Tr)
        
        # Calculo del coeficiente de ajuste
        # DRIFT CORRECTION
        sig1 = sigD
        F1 = FsigD
        for m in range(20): # maximo 10 veces correccion consistente
            # tomando los valores iniciales
            sig0 = sig1
            F0 = F1
            # calculando derivadas de funcion de fluencia y potencial plastico
            a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
            a0pr = MCgrad(sig0, Prop, Tr, 1) # potencial plastico
            # calculado incremento de esfuerzo corrector drift
            delsig = -F0 * np.dot(De4, a0pr) / np.dot(a0, np.dot(De4, a0pr)) # con termino sigz
            #delsig1 = -F0 * np.dot(De, a0pr[:3]) / np.dot(a0, np.dot(De4, a0pr)) # sin termino sigz
            #delsig = np.zeros(len(delsig1) + 1)
            #delsig[:len(delsig1)], delsig[-1] = delsig1, nu*(delsig1[0]+delsig1[1])
            # calculando nuevo esfuerzo
            sig1 = sig0 + delsig
            F1 = MCyield(sig1, Prop, Tr)
            if abs(F1) < 1e-6:
                break
            if m == 19: # ultima iteracion y no convergio
                # APLICAR CORRECION NORMAL
                print("Warning: Correcion normal")
                sig1 = sigD
                F1 = FsigD
                while abs(F1) > 1e-6:
                    # tomando los valores iniciales
                    sig0 = sig1
                    F0 = F1
                    # calculando derivadas
                    a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
                    # calculando inremento de esfuerzo
                    delsig = -F0 * a0 / np.dot(a0, a0)
                    sig1 = sig0 + delsig
                    F1 = MCyield(sig1, Prop, Tr)
                                                
        sigD2 = sig1 # estado de esfuerzo final
        FsigD2 = MCyield(sigD2, Prop, Tr)
        if abs(FsigD2) > 1e-5:
            print("Warning: el F en D = ", FsigD2, "F en B = ", FsigB)
        
        # Calculo del incremeto de deformacion plastica y actualizar deformaciones
        depsp = lam * aBpr[:3] # qitando e ultimo termino
        epsp += depsp
        epse += deps - depsp
        #depspzz = lam*aBpr[3]
    
    # ===  FIN CONDICION PARA SABER SI EL INCREMENTO ES SOLO ELASTICO
        
    return sigD2, epse, epsp, Yield

# ==================================================================================
# === Funcion para el calculo de esfuerzos y deformaciones ELASTOPLASTICIDAD =======

@njit
def MC_elastoplastic3(sigA, deps, Prop):
    """Funcion que calcula el estado de esfuerzo, el incremento de deformacion elastica y plastica
        de acuerdo con la formulacion de Mohr-Coulomb de Abbo-Sloan elasto plastica perfecta
        sin aplicar alpha and drift correction"""
    Tr = 29 # angulo de transicion que puede ser modificado

    # parametros de la particula mp-1
    E = Prop[0] # Modulo de Young
    nu = Prop[1] # Coeficiente de Poisson
    Yield = Prop[5] # variable que indica si la aprticula se ha plastifiado o no
    
    # Matriz de rigidez elastica lineal
    De = constitutive_matrix_elastic(1, E, nu)
    # matriz elastica lineal de (4x4) - termino sigzz
    De4 = np.zeros((4,4))
    De4[:3,:3] = De
    De4[0,3], De4[3,0] = De[0,1], De[0,1]
    De4[1,3], De4[3,1] = De[0,1], De[0,1]
    De4[3,3] = De[0,0]
    
    # Esfuerzo trial elastico - td el incremento es elastico
    dsigt = np.dot(De, deps)
    dsig = np.zeros(len(dsigt)+1)
    dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
    
    sigC = sigA + dsig
    # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
    FsigA = MCyield(sigA, Prop, Tr)
    FsigC = MCyield(sigC, Prop, Tr)
    
    # === CONDICION PARA SABER SI EL INCREMENTO ES SOLO ELASTICO
    if FsigC < 0 and FsigA < 1e-5: # tolerancia de F
        # El incremento es elastico
        sigD2 = sigC
        depse = deps
        depsp = np.zeros(len(deps))
    else:
        # Incremento elastoplastico
        if FsigA > 1e-3:
            print("Warning: Estado inicial fuera de la la superficie, F en A = ", FsigA)
            print("Estado de esfuerzos: ", sigA)
            outF = 1 # ????????????
        else:
            outF = 0 # ???????????
                
        if FsigA < 1e-5 and outF == 0:
            Yield = 1
            # La particula no se habia plasticido en la iteracion anterior
            alp1 = FsigA / (FsigA - FsigC) # primera aproximacion de alpha
            sigk1 = sigA + alp1 * dsig # primera aproxiamcion del esfuerzo
            Fsigk1 = MCyield(sigk1, Prop, Tr)
            while abs(Fsigk1) > 1e-6:              
                sigk = sigk1 # tomando el esfuerzo anterior
                alp = alp1 # el alpha anterior
                Fsigk = MCyield(sigk, Prop, Tr)
                ak = MCgrad(sigk, Prop, Tr, 0)
                alp1 = alp - Fsigk / (np.dot(ak, dsig)) # Newton Raphson
                #print("alpha nicial: ", alp, "  alpha final: ", alp1)
                sigk1 = sigA + alp1*dsig # actualizacion del esfuerzo
                Fsigk1 = MCyield(sigk1, Prop, Tr)
                        
            sigB = sigk1 # asignando el valor de la iteracion con el esfuerzo en la s de fluencia
            R = 1 - alp1 # R como el complemente de alpha - valor de esfuerzo a ajustar
        else:
            # La particula se habia plastificado en la iteracion anterior
            print("INCREMENTO PLASTICO")
            R = 1
            sigB = sigA # todo el incremento se debe corregir
        
        # calculando la funcion de fluencia y derivadas en el punto B - sobre F=0
        
        # SE DEBE TOMAR EL TERMINO F - SIGZZ??????
        FsigB = MCyield(sigB, Prop, Tr)
        #if abs(FsigB) > 1e-3:
            #print("Warning: F en B = ", FsigB)
        
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        
        # Calculo del multiplicador plastico
        lam = (np.dot(aB, dsig))/(R * np.dot(aB, np.dot(De4, aBpr))) # con termino sigz
        if lam < 0:
            # valor de lambda negativo
            print("Warning: Multiplicador plastico negativo!!")
        
        #dsig3 = dsig[:3]
        #lam = (np.dot(aB[:3], dsig3))/(R * np.dot(aB[:3], np.dot(De, aBpr[:3]))) # sin termino sigz
        
        # Calculo de esfuerzo en D - que esta fuera de la superficie de fluencia
        #sigD1 = sigC[:3] - lam * np.dot(De, aBpr[:3]) # sin el termino sigz
        #sigD = np.zeros(len(sigD1) + 1)
        #sigD[:len(sigD1)], sigD[-1] = sigD1, nu *(sigD1[0] + sigD1[1])
        
        sigD = sigC - lam * np.dot(De4, aBpr) # con el termino sigz
        # Calculo de la funcion de fluencia
        FsigD = MCyield(sigD, Prop, Tr)
        
        # Calculo del coeficiente de ajuste
        # DRIFT CORRECTION
        sig1 = sigD
        F1 = FsigD
        for m in range(20): # maximo 10 veces correccion consistente
            # tomando los valores iniciales
            sig0 = sig1
            F0 = F1
            # calculando derivadas de funcion de fluencia y potencial plastico
            a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
            a0pr = MCgrad(sig0, Prop, Tr, 1) # potencial plastico
            # calculado incremento de esfuerzo corrector drift
            delsig = -F0 * np.dot(De4, a0pr) / np.dot(a0, np.dot(De4, a0pr)) # con termino sigz
            #delsig1 = -F0 * np.dot(De, a0pr[:3]) / np.dot(a0, np.dot(De4, a0pr)) # sin termino sigz
            #delsig = np.zeros(len(delsig1) + 1)
            #delsig[:len(delsig1)], delsig[-1] = delsig1, nu*(delsig1[0]+delsig1[1])
            # calculando nuevo esfuerzo
            sig1 = sig0 + delsig
            F1 = MCyield(sig1, Prop, Tr)
            if abs(F1) < 1e-6:
                break
            if m == 19: # ultima iteracion y no convergio
                # APLICAR CORRECION NORMAL
                #print("Warning: Correcion normal")
                sig1 = sigD
                F1 = FsigD
                while abs(F1) > 1e-6:
                    # tomando los valores iniciales
                    sig0 = sig1
                    F0 = F1
                    # calculando derivadas
                    a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
                    # calculando inremento de esfuerzo
                    delsig = -F0 * a0 / np.dot(a0, a0)
                    sig1 = sig0 + delsig
                    F1 = MCyield(sig1, Prop, Tr)
                                        
        sigD2 = sig1 # estado de esfuerzo final
        FsigD2 = MCyield(sigD2, Prop, Tr)
        if abs(FsigD2) > 1e-5:
            print("Warning: el F en D = ", FsigD2, "F en B = ", FsigB)
        
        # Calculo del incremeto de deformacion plastica y actualizar deformaciones
        depsp = lam * aBpr[:3] # qitando e ultimo termino
        depse = deps - depsp
        #depspzz = lam*aBpr[3]
    
    # ===  FIN CONDICION PARA SABER SI EL INCREMENTO ES SOLO ELASTICO
        
    return sigD2, depse, depsp, Yield


# ==================================================================================
# === Funcion para el calculo de esfuerzos y deformaciones ELASTOPLASTICIDAD =======

@njit
def MC_elastoplastic4(sigA, deps, Prop):
    """Funcion que calcula el estado de esfuerzo, el incremento de deformacion elastica y plastica
        de acuerdo con la formulacion de Mohr-Coulomb de Abbo-Sloan elasto plastica perfecta
        con algortimo de Pegasus (modified regular falsi)"""
    Tr = 29 # angulo de transicion que puede ser modificado
    Ftol = 1e-6

    # parametros de la particula mp-1
    E = Prop[0] # Modulo de Young
    nu = Prop[1] # Coeficiente de Poisson
    Yield = Prop[5] # variable que indica si la aprticula se ha plastifiado o no
    
    # Matriz de rigidez elastica lineal
    De = constitutive_matrix_elastic(1, E, nu)
    # matriz elastica lineal de (4x4) - termino sigzz
    De4 = np.zeros((4,4))
    De4[:3,:3] = De
    De4[0,3], De4[3,0] = De[0,1], De[0,1]
    De4[1,3], De4[3,1] = De[0,1], De[0,1]
    De4[3,3] = De[0,0]
    
    # Esfuerzo trial elastico - td el incremento es elastico
    dsigt = np.dot(De, deps)
    dsig = np.zeros(len(dsigt)+1)
    dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
    
    sigC = sigA + dsig
    # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
    FsigA = MCyield(sigA, Prop, Tr)
    FsigC = MCyield(sigC, Prop, Tr)
    
    # ==== ALGORITMO =====
    if FsigA <= 0:
        # el estado inicial esta dentro del s. de fluencia
        if FsigC <= 0:
            elastic = True
            # el incremento es elastico
            sigD2 = sigC
            depse = deps
            depsp = np.zeros(len(deps))
        else:
            # incremento elastoplastico
            elastic = False
            # Determinar sigB punto de interseccion con la superficie
            
            # -- ALGORITMO PEGASUS --
            alpha0 = 0
            alpha1 = 1
            F0 = MCyield(sigA + alpha0*dsig, Prop, Tr)
            F1 = MCyield(sigA + alpha1*dsig, Prop, Tr)
            for n in range(10): # maximo 10 iteraciones en el algoritmo
                alpha = alpha1 - F1*(alpha1 - alpha0) / (F1 - F0)
                Fnew = MCyield(sigA + alpha*dsig, Prop, Tr)
                
                if abs(Fnew) <= Ftol:
                    break
                
                if np.sign(Fnew) != np.sign(F0):
                    alpha1 = alpha0
                    F1 = F0
                else:
                    F1 = F1*F0 / (F0 + Fnew)
                
                alpha0 = alpha
                F0 = Fnew
            
            if abs(Fnew) > Ftol:
                print("Warning: 10 iteraciones y no convergio algortimo Pegasus")
                #alpha0 = 0
                #alpha1 = 1
                #F0 = MCyield(sigA + alpha0*dsig, Prop, Tr)
                #F1 = MCyield(sigA + alpha1*dsig, Prop, Tr)
                #print("estados iniciales de iteracion: F0 = ", F0, " F1 = ", F1)
            
            # -- FIN ALGORTIMO PEGAUS --
            
            sigB = sigA  + alpha*dsig # Estado de esfuerzos en la superficie de fluencia
            R = 1 - alpha # R como el complemente de alpha - valor de esfuerzo a ajustar
        
    else:
        # El estado de esfuerzo inicial esta sobre la superficie
        # Todo el incremento es plastico
        R = 1
        sigB = sigA
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        costhe = (np.dot(aB, dsig)/np.linalg.norm(aB)/np.linalg.norm(dsig))
        if costhe < -1e-4:
            # descarga elastica
            #if FsigC > 0:
                # descarga elastoplsatica
                #print("Warning: descarga elastoplastica")
            elastic = True
            sigD2 = sigC
            depse = deps
            depsp = np.zeros(len(deps))
        else:
            # incremento carga plasticamente
            elastic = False
    
    
    if elastic == False:
        # hallar incremento plastico
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        
        FsigB = MCyield(sigB, Prop, Tr)        
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        if R > 1:
            print("ERROR valores de R  - alpha > 1")
        
        # Calculo del multiplicador plastico
        lam = (np.dot(aB, dsig))/(R * np.dot(aB, np.dot(De4, aBpr))) # con termino sigz
        if lam < 0:
            # valor de lambda negativo
            thet =math.acos(np.dot(aB, dsig)/np.linalg.norm(aB)/np.linalg.norm(dsig))
            print("Warning: Multiplicador plastico negativo!!")
            #print("F en A = ", FsigA, "F en B", FsigC )
            print("valor de theta = ", thet*180/math.pi)
        
        sigD = sigC - lam * np.dot(De4, aBpr) # con el termino sigz
        # Calculo de la funcion de fluencia
        FsigD = MCyield(sigD, Prop, Tr)
        
        # DRIFT CORRECTION
        sig1 = sigD
        F1 = FsigD
        for m in range(20): # maximo 20 veces correccion consistente
            # tomando los valores iniciales
            sig0 = sig1
            F0 = F1
            # calculando derivadas de funcion de fluencia y potencial plastico
            a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
            a0pr = MCgrad(sig0, Prop, Tr, 1) # potencial plastico
            # calculado incremento de esfuerzo corrector drift
            delsig = -F0 * np.dot(De4, a0pr) / np.dot(a0, np.dot(De4, a0pr)) # con termino sigz
            # calculando nuevo esfuerzo
            sig1 = sig0 + delsig
            F1 = MCyield(sig1, Prop, Tr)
            if abs(F1) < Ftol:
                break
            if m == 19: # ultima iteracion y no convergio
                # APLICAR CORRECION NORMAL
                #print("Warning: Correcion normal")
                sig1 = sigD
                F1 = FsigD
                while abs(F1) > Ftol:
                    # tomando los valores iniciales
                    sig0 = sig1
                    F0 = F1
                    # calculando derivadas
                    a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
                    # calculando inremento de esfuerzo
                    delsig = -F0 * a0 / np.dot(a0, a0)
                    sig1 = sig0 + delsig
                    F1 = MCyield(sig1, Prop, Tr)
                                        
        sigD2 = sig1 # estado de esfuerzo final
        FsigD2 = MCyield(sigD2, Prop, Tr)
        if abs(FsigD2) > Ftol:
            print("Warning: el F en D = ", FsigD2, "F en B = ", FsigB)
        
        # Calculo del incremeto de deformacion plastica y actualizar deformaciones
        depsp = lam * aBpr[:3] # qitando e ultimo termino
        depse = deps - depsp
    
    return sigD2, depse, depsp, Yield

# ==========================================================================
# ================= Algortimo Pegasus ===============

@njit
def pegasus(dsig, sigA, Prop, Tr, alpha0, alpha1):
    """ Funcion para encontrar ceros de la funcion con el algortmo Regular falsi
        modificado o algortmo Pegasus (Dowell, 1972), funcion usada para encontrar 
        el punto de interseccion con la superficie de fluencia"""
    
    Ftol = 1e-6
    F0 = MCyield(sigA + alpha0*dsig, Prop, Tr)
    F1 = MCyield(sigA + alpha1*dsig, Prop, Tr)
    
    if F0*F1 > 0:
        print("Warning: valores inciales de algorimto pegasus no confina el CERO")
    
    for n in range(20): # maximo 10 iteraciones en el algoritmo
        alpha = alpha1 - F1*(alpha1 - alpha0) / (F1 - F0)
        Fnew = MCyield(sigA + alpha*dsig, Prop, Tr)
        
        if abs(Fnew) <= Ftol:
            break
        
        if np.sign(Fnew) != np.sign(F0):
            alpha1 = alpha0
            F1 = F0
        else:
            F1 = F1*F0 / (F0 + Fnew)
        
        alpha0 = alpha
        F0 = Fnew
        
    if abs(Fnew) > Ftol:
        print("Warning: 20 iteraciones y no convergio algortimo Pegasus")
        # +++ PROCEDIMENTO NEWTON RAPSHON +++++
        alp1 = alpha0 # primera aproximacion de alpha
        sigk1 = sigA + alp1 * dsig # primera aproxiamcion del esfuerzo
        Fsigk1 = MCyield(sigk1, Prop, Tr)
        
        while abs(Fsigk1) > Ftol:              
            sigk = sigk1 # tomando el esfuerzo anterior
            alp = alp1 # el alpha anterior
            Fsigk = MCyield(sigk, Prop, Tr)
            ak = MCgrad(sigk, Prop, Tr, 0)
            
            # nueva aproximacion de alpha
            alp1 = alp - Fsigk / (np.dot(ak, dsig)) # Newton Raphson
            sigk1 = sigA + alp1*dsig # actualizacion del esfuerzo
            Fsigk1 = MCyield(sigk1, Prop, Tr)
        
    return alpha


# ===========================================================================
# ============== Funcion descarga elastoplastica ======================
@njit
def unload_elpl(dsig, sigA, Prop, Tr):
    """Funcion que determina el punto de interseccion para la descarga elastoplastica
        segun el algoritmo presentado por Aboo Sloan 2001"""
    
    Ftol = 1e-6
    dalp = np.linspace(0,1,20)
    Fsigs = np.zeros(len(dalp))
    # lista por comprension para determinar los valores de F
    for i in range(len(dalp)):
        Fsigs[i] = MCyield(sigA + dalp[i]*dsig, Prop, Tr)
    
    if np.min(Fsigs) >= -Ftol:
        # no entro a la superficie - DESCARGA TANGENTE
        alpha = 0 # todo el incremento es plastico
    else:
        # si entro a la superficie - DESCARGA ELASTOPLASTICA
        Fmin = np.where(Fsigs < -Ftol)[0] # array con indices
        alp0 = dalp[Fmin[-1]] # valor max para F<-Ftol
        if Fsigs[Fmin[-1]] >= -Ftol:
            print("Error: no escogio el valor adecuado de alp0")
        Fmax = np.where(Fsigs[Fmin[-1]:] > Ftol)[0] # array con indices
        alp1 = dalp[Fmax[0] + Fmin[-1]] # valor max para F > Ftol
        if Fsigs[Fmax[0] + Fmin[-1]] <= Ftol:
            print("Error: no escogio el valor adecuado de alp1")
        # con los valores alp0 y alp1 determinar la interseccion con la S. fluencia
        alpha = pegasus(dsig, sigA, Prop, Tr, alp0, alp1)
    
    return alpha
        
# ==================================================================================
# === Funcion para el calculo de esfuerzos y deformaciones ELASTOPLASTICIDAD =======

@njit
def MC_elastoplastic2(sigA, deps, Prop):
    """Funcion que calcula el estado de esfuerzo, el incremento de deformacion elastica y plastica
        de acuerdo con la formulacion de Mohr-Coulomb de Abbo-Sloan elasto plastica perfecta
        con algortimo de Pegasus (modified regular falsi)"""
        
    Tr = 25 # angulo de transicion que puede ser modificado
    Ftol = 1e-6

    # parametros de la particula mp-1
    E = Prop[0] # Modulo de Young
    nu = Prop[1] # Coeficiente de Poisson
    Yield = Prop[5] # variable que indica si la aprticula se ha plastifiado o no
    
    # Matriz de rigidez elastica lineal
    De = constitutive_matrix_elastic(1, E, nu)
    # matriz elastica lineal de (4x4) - termino sigzz
    De4 = np.zeros((4,4))
    De4[:3,:3] = De
    De4[0,3], De4[3,0] = De[0,1], De[0,1]
    De4[1,3], De4[3,1] = De[0,1], De[0,1]
    De4[3,3] = De[0,0]
    
    # Esfuerzo trial elastico - td el incremento es elastico
    dsigt = np.dot(De, deps)
    dsig = np.zeros(len(dsigt)+1)
    dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
    
    sigC = sigA + dsig
    # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
    FsigA = MCyield(sigA, Prop, Tr)
    FsigC = MCyield(sigC, Prop, Tr)
    
    # ==== ALGORITMO =====
    if FsigA < -Ftol:
        # el estado inicial esta dentro del s. de fluencia
        if FsigC < Ftol: # 
            elastic = True
            # el incremento es elastico
            sigD2 = sigC
            depse = deps
            depsp = np.zeros(len(deps))
        else:
            # incremento elastoplastico
            elastic = False
            # Determinar sigB punto de interseccion con la superficie
            alpha = pegasus(dsig, sigA, Prop, Tr, 0, 1)
            
            sigB = sigA  + alpha*dsig # Estado de esfuerzos en la superficie de fluencia
            R = 1 - alpha # R como el complemente de alpha - valor de esfuerzo a ajustar
        
    else:
        # El estado de esfuerzo inicial esta sobre la superficie
        
        # Todo el incremento es plastico
        aA = MCgrad(sigA, Prop, Tr, 0) # funcion de fluencia
        # determinar direccion de carga
        costhe = (np.dot(aA, dsig)/np.linalg.norm(aA)/np.linalg.norm(dsig))
        
        ######### =========== FORMULACION DETALLADA
        #if FsigC > Ftol:
            # carga
            #if costhe < -1e-4:
                # Descarga elastoplastica
                #elastic = False
                #alpha = unload_elpl(dsig, sigA, Prop, Tr)
                #sigB = sigA + alpha*dsig
                #R = 1 - alpha
            #else:
                # Carga plastica
                #elastic = False
                #sigB = sigA
                #R = 1
                
        #elif FsigC < -Ftol:
            # descarga
            #if costhe < -1e-4:
                #elastic = True
                #sigD2 = sigC
                #depse = deps
                #depsp = np.zeros(len(deps))
            #else:
                # Error (?)
                #print("Error: ")
        #else:
            # permanece en la superfice
            #elastic = False
            #sigB = sigA
            #R = 1
        
        ########## ========= FIN FORMULACION DETALLADA
        
        #### ==== FORMULACION CON DESCARGA
        if costhe < -1e-4:
            if FsigC > Ftol:
                # descarga elastoplsatica
                elastic = False
                alpha = unload_elpl(dsig, sigA, Prop, Tr)
                sigB = sigA + alpha*dsig
                R = 1 - alpha
            
            else:
                # descarga elastica
                elastic = True
                sigD2 = sigC
                depse = deps
                depsp = np.zeros(len(deps))
        else:
            # incremento carga plasticamente
            elastic = False
            R = 1
            sigB = sigA
        
        #### ======= FIN formulacion con descarga
        
        #elastic = False
        #R = 1
        #sigB = sigA
        
        ###### ===================
    
    if elastic == False:
        # hallar incremento plastico              
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        if R > 1:
            print("ERROR valores de R  - alpha > 1")
        
        # Calculo del multiplicador plastico
        lam = (np.dot(aB, dsig))/(R * np.dot(aB, np.dot(De4, aBpr))) # con termino sigz
        #dsig3 = dsig[:3]
        #lam = (np.dot(aB[:3], dsig3))/(R * np.dot(aB[:3], np.dot(De, aBpr[:3]))) # sin termino sigz
        
        # Calculo de esfuerzo en D - que esta fuera de la superficie de fluencia
        
        #sigD1 = sigC[:3] - lam * np.dot(De, aBpr[:3]) # sin el termino sigz
        #sigD = np.zeros(len(sigD1) + 1)
        #sigD[:len(sigD1)], sigD[-1] = sigD1, nu *(sigD1[0] + sigD1[1])
        sigD = sigC - lam * np.dot(De4, aBpr) # con el termino sigz
        
        # Calculo de la funcion de fluencia
        FsigD = MCyield(sigD, Prop, Tr)
        
        # DRIFT CORRECTION
        sig1 = sigD
        F1 = FsigD
        for m in range(20): # maximo 20 veces correccion consistente
            # tomando los valores iniciales
            sig0 = sig1
            F0 = F1
            # calculando derivadas de funcion de fluencia y potencial plastico
            a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
            a0pr = MCgrad(sig0, Prop, Tr, 1) # potencial plastico
            # calculado incremento de esfuerzo corrector drift
            delsig = -F0 * np.dot(De4, a0pr) / np.dot(a0, np.dot(De4, a0pr)) # con termino sigz
            #delsig1 = -F0 * np.dot(De, a0pr[:3]) / np.dot(a0[:3], np.dot(De, a0pr[:3])) # sin termino sigz
            #delsig = np.zeros(len(delsig1) + 1)
            #delsig[:len(delsig1)], delsig[-1] = delsig1, nu * (delsig1[0] + delsig1[1])
            
            # calculando nuevo esfuerzo
            sig1 = sig0 + delsig
            F1 = MCyield(sig1, Prop, Tr)
            if abs(F1) < Ftol:
                break
            if m == 19: # ultima iteracion y no convergio
                # APLICAR CORRECION NORMAL
                #print("Warning: Correcion normal")
                sig1 = sigD
                F1 = FsigD
                cont = 0
                while abs(F1) > Ftol:
                    # tomando los valores iniciales
                    sig0 = sig1
                    F0 = F1
                    # calculando derivadas
                    a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
                    # calculando inremento de esfuerzo
                    delsig = -F0 * a0 / np.dot(a0, a0)
                    sig1 = sig0 + delsig
                    F1 = MCyield(sig1, Prop, Tr)
                    cont += 1
                    if cont == 30:
                        print("Warning: > 30 itera - no converge correccion normal")
                    elif cont == 40:
                        print("Warning: >40 itera - no converge correccion normal")
                                                
        sigD2 = sig1 # estado de esfuerzo final   
        # Calculo del incremeto de deformacion plastica y actualizar deformaciones
        depsp = lam * aBpr[:3] # qitando e ultimo termino
        depse = deps - depsp
    
    return sigD2, depse, depsp, Yield


# ==================================================================================


# ==================================================================================
# === Funcion para el calculo de esfuerzos y deformaciones ELASTOPLASTICIDAD =======

@njit
def MC_elastoplastic5(sigA, deps, Prop):
    """Funcion que calcula el estado de esfuerzo, el incremento de deformacion elastica y plastica
        de acuerdo con la formulacion de Mohr-Coulomb de Abbo-Sloan elasto plastica perfecta
        con algortimo de Pegasus (modified regular falsi)"""
    Tr = 25 # angulo de transicion que puede ser modificado
    Ftol = 1e-6

    # parametros de la particula mp-1
    E = Prop[0] # Modulo de Young
    nu = Prop[1] # Coeficiente de Poisson
    Yield = Prop[5] # variable que indica si la aprticula se ha plastifiado o no
    
    # Matriz de rigidez elastica lineal
    De = constitutive_matrix_elastic(1, E, nu)
    # matriz elastica lineal de (4x4) - termino sigzz
    De4 = np.zeros((4,4))
    De4[:3,:3] = De
    De4[0,3], De4[3,0] = De[0,1], De[0,1]
    De4[1,3], De4[3,1] = De[0,1], De[0,1]
    De4[3,3] = De[0,0]
    
    # Esfuerzo trial elastico - td el incremento es elastico
    dsigt = np.dot(De, deps)
    dsig = np.zeros(len(dsigt)+1)
    dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
    
    sigC = sigA + dsig
    # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
    FsigA = MCyield(sigA, Prop, Tr)
    FsigC = MCyield(sigC, Prop, Tr)
    
    # ==== ALGORITMO =====
    if FsigA <= 0:
        # el estado inicial esta dentro del s. de fluencia
        if FsigC <= 0:
            elastic = True
            # el incremento es elastico
            sigD2 = sigC
            depse = deps
            depsp = np.zeros(len(deps))
        else:
            # incremento elastoplastico
            elastic = False
            # Determinar sigB punto de interseccion con la superficie
            # algoritmo Newton - Raphson
            alp1 = FsigA / (FsigA - FsigC) # primera aproximacion de alpha
            sigk1 = sigA + alp1 * dsig # primera aproxiamcion del esfuerzo
            Fsigk1 = MCyield(sigk1, Prop, Tr)
            while abs(Fsigk1) > Ftol:              
                sigk = sigk1 # tomando el esfuerzo anterior
                alp = alp1 # el alpha anterior
                Fsigk = MCyield(sigk, Prop, Tr)
                ak = MCgrad(sigk, Prop, Tr, 0)
                alp1 = alp - Fsigk / (np.dot(ak, dsig)) # Newton Raphson
                #print("alpha nicial: ", alp, "  alpha final: ", alp1)
                sigk1 = sigA + alp1*dsig # actualizacion del esfuerzo
                Fsigk1 = MCyield(sigk1, Prop, Tr)
                        
            sigB = sigk1 # asignando el valor de la iteracion con el esfuerzo en la s de fluencia
            R = 1 - alp1 # R como el complemente de alpha - valor de esfuerzo a ajustar
        
    else:
        # El estado de esfuerzo inicial esta sobre la superficie
        # Todo el incremento es plastico
        R = 1
        sigB = sigA
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        costhe = (np.dot(aB, dsig)/np.linalg.norm(aB)/np.linalg.norm(dsig))
        if costhe < -1e-4:
            # descarga elastica
            if FsigC > 0:
                # descarga elastoplsatica
                dalpha = np.linspace(0,1,15) # diviiendo el incrmento
                Fsign = np.zeros(len(dalpha))
                
                for n in range(len(dalpha)):
                    sign = sigA + dalpha[n]*dsig
                    Fsign[n] = MCyield(sign, Prop, Tr)
                
                Fmin = np.min(Fsign)
                if Fmin > 0:
                    # quiere decir que nunca entro a la superficie de fluencia
                    print("Incremento tangente a la superficie")
                else:
                    print("Warning: descarga elastoplastica")
            
            elastic = True
            sigD2 = sigC
            depse = deps
            depsp = np.zeros(len(deps))
        else:
            # incremento carga plasticamente
            elastic = False
    
    
    if elastic == False:
        # hallar incremento plastico              
        aB = MCgrad(sigB, Prop, Tr, 0) # funcion de fluencia
        aBpr = MCgrad(sigB, Prop, Tr, 1) # potencial plastico
        if R > 1:
            print("ERROR valores de R  - alpha > 1")
        
        # Calculo del multiplicador plastico
        lam = (np.dot(aB, dsig))/(R * np.dot(aB, np.dot(De4, aBpr))) # con termino sigz
        #if lam < 0:
            # valor de lambda negativo
            #thet =math.acos(np.dot(aB, dsig)/np.linalg.norm(aB)/np.linalg.norm(dsig))
            #print("Warning: Multiplicador plastico negativo!!")
            #print("F en A = ", FsigA, "F en B", FsigC )
            #print("valor de theta = ", thet*180/math.pi)
        
        sigD = sigC - lam * np.dot(De4, aBpr) # con el termino sigz
        # Calculo de la funcion de fluencia
        FsigD = MCyield(sigD, Prop, Tr)
        
        # DRIFT CORRECTION
        sig1 = sigD
        F1 = FsigD
        for m in range(20): # maximo 20 veces correccion consistente
            # tomando los valores iniciales
            sig0 = sig1
            F0 = F1
            # calculando derivadas de funcion de fluencia y potencial plastico
            a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
            a0pr = MCgrad(sig0, Prop, Tr, 1) # potencial plastico
            # calculado incremento de esfuerzo corrector drift
            delsig = -F0 * np.dot(De4, a0pr) / np.dot(a0, np.dot(De4, a0pr)) # con termino sigz
            # calculando nuevo esfuerzo
            sig1 = sig0 + delsig
            F1 = MCyield(sig1, Prop, Tr)
            if abs(F1) < Ftol:
                break
            if m == 19: # ultima iteracion y no convergio
                # APLICAR CORRECION NORMAL
                #print("Warning: Correcion normal")
                sig1 = sigD
                F1 = FsigD
                while abs(F1) > Ftol:
                    # tomando los valores iniciales
                    sig0 = sig1
                    F0 = F1
                    # calculando derivadas
                    a0 = MCgrad(sig0, Prop, Tr, 0) # funcion de fluencia
                    # calculando inremento de esfuerzo
                    delsig = -F0 * a0 / np.dot(a0, a0)
                    sig1 = sig0 + delsig
                    F1 = MCyield(sig1, Prop, Tr)
                                        
        sigD2 = sig1 # estado de esfuerzo final   
        # Calculo del incremeto de deformacion plastica y actualizar deformaciones
        depsp = lam * aBpr[:3] # qitando e ultimo termino
        depse = deps - depsp
    
    return sigD2, depse, depsp, Yield



# ====================================================================
# === Funcion para transferir de los nodos a las particulas los esfeurzos ===

#@njit#('Tuple((f8[:,:], f8[:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:], f8[:], f8[:])), f8[:,:], f8 )')
def nodes_to_particle_stress(grid, particle, nvel, dtime, elapla): 
    """ Funcion que calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
        para el calculo del gradiente de velocida Lp - Metodo MUSL, doble transferencia
        Variable elapla = 0 (cero) Lineal elastico
                        = 1 (uno) Elastoplastico perfecto
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal"""
                
    assert (elapla == 1 or elapla == 0), "La variable elapla debe ser 0(cero) o 1(uno)"
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop = particle

    # ==================================================================
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            # organizado las funciones de forma y sus derivadas en el array correspondiente
            Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np = shfnp[mp - 1,:].reshape((3, len(nodes)))
            #Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            #Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            #Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y
            
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
            F = np.dot((np.identity(2) + Lp*dtime), Fp[mp - 1, :].reshape((2, 2)))
            #Fpt = np.zeros((2, 2)) # matriz grandiente deformacion en tiempo t
            #Fpt[0, 0], Fpt[0, 1], Fpt[1, 0], Fpt[1, 1] = Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3]
            #F = np.dot((np.identity(2) + Lp*dtime), Fpt) # matriz grandiente de deformacion en el tiempo t+1
            Fp[mp - 1, :] = F.reshape((1, 4))
            #Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3] = F[0, 0], F[0, 1], F[1, 0], F[1, 1] 
            # actualizar volumen de las particulas
            Vp[mp - 1] = np.linalg.det(F) * Vp0[mp - 1]
            # calculo de incremento de deformacion y de esfuerzos
            deps1 = dtime / 2 * (Lp + Lp.T) # se obtiene tensor de deformaciones!!
            deps = np.array([deps1[0,0], deps1[1,1], 2*deps1[0,1]]) # notacion de Voight
            nor_deps = np.linalg.norm(deps)
            
            if nor_deps == 0:
                # incremento de deformacion nulo!!
                pass
            else:
                # incremento de deformacion no nulo!!
            
                # actualizacion de esfuerzo - depende si eslastico o plastico
                if elapla == 0:
                    # lineal elastico
                    C2D_stress = constitutive_matrix_elastic(1, Prop[mp - 1,0], Prop[mp - 1,1]) # matriz constitutiva condicion plana de esfuerzos
                    dsig = np.dot(C2D_stress, deps) # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
                    dsig1 = np.zeros(4)
                    dsig1[:3], dsig1[3] = dsig, Prop[mp - 1,1]*(dsig[0] + dsig[1])
                    # Actualizar esfuerzo y deformacion sumando el incremento
                    epse[mp - 1, :] += deps
                    sig[mp - 1, :] += dsig1
                else:
                    # Elastoplastico
                    try:
                        # probando convergencia elastoplasticidad
                        sig[mp-1,:], depse, depsp, Prop[mp-1,5] = MC_elastoplastic2(sig[mp-1,:], deps, Prop[mp-1,:])
                        epse[mp-1,:] += depse
                        epsp[mp-1,:] += depsp
                    except ZeroDivisionError:
                        print("No convergencia del Algo de integracion de esfuerzos")
                        
                        # ++++ CALCULANDO Fa Y Fc ++++
                        Tr = 25
                        E = Prop[mp-1, 0] # Modulo de Young
                        nu = Prop[mp-1,1] # Coeficiente de Poisson
                        
                        # Matriz de rigidez elastica lineal
                        De = constitutive_matrix_elastic(1, E, nu)
                        # matriz elastica lineal de (4x4) - termino sigzz
                        De4 = np.zeros((4,4))
                        De4[:3,:3] = De
                        De4[0,3], De4[3,0] = De[0,1], De[0,1]
                        De4[1,3], De4[3,1] = De[0,1], De[0,1]
                        De4[3,3] = De[0,0]
                        
                        # Esfuerzo trial elastico - td el incremento es elastico
                        dsigt = np.dot(De, deps)
                        dsig = np.zeros(len(dsigt)+1)
                        dsig[:len(dsigt)], dsig[-1] = dsigt, nu *(dsigt[0] + dsigt[1])
                        
                        sigC = sig[mp-1,:] + dsig
                        # Chequeo si el esfuerzo trial esta fuera de la superficie de fluencia
                        FsigA = MCyield(sig[mp-1,:], Prop[mp-1,:], Tr)
                        FsigC = MCyield(sigC, Prop[mp-1,:], Tr)
                        print("Valor incial de F = ", FsigA, " Valor final de F = ", FsigC)
                        print("Delta de deformacion = ", deps, "Delta de esfuerzo = ", dsig)
                        
                        # Aplicar elastoplasticidad por incrementos
                        nincr = 10 # 10 incrementos
                        for m in range(nincr):
                            sig[mp-1,:], depse, depsp, Prop[mp-1,5] = MC_elastoplastic2(sig[mp-1,:], deps/nincr, Prop[mp-1,:])
                            epse[mp-1,:] += depse
                            epsp[mp-1,:] += depsp
                    
                    # Fin del Try - Except
    
    
    return Fp, Vp, epse, epsp, sig



# ====================================================================
# === Funcion para transferir de los nodos a las particulas los esfeurzos ===

@njit#('Tuple((f8[:,:], f8[:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:], f8[:], f8[:])), f8[:,:], f8 )')
def nodes_to_particle_stress2(grid, particle, nvel, dtime, elapla): 
    """ Funcion que calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
        para el calculo del gradiente de velocida Lp - Metodo MUSL, doble transferencia
        Variable elapla = 0 (cero) Lineal elastico
                        = 1 (uno) Elastoplastico perfecto
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal
        ++++ PRUEBA CON 10 SUBINCREMENTOS DE DEFORMACION ++++ """
                
    assert (elapla == 1 or elapla == 0), "La variable elapla debe ser 0(cero) o 1(uno)"
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop = particle

    # ==================================================================
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        
        # ciclo en las particulas
        for j in range(len(mpe)):
            mp = mpe[j] # numero de mp - particula
            # organizado las funciones de forma y sus derivadas en el array correspondiente
            Np = np.zeros((3, len(nodes))) # array para funciones de forma
            Np = shfnp[mp - 1,:].reshape((3, len(nodes)))
            #Np[0,0], Np[0,1], Np[0,2] = shfnp[mp - 1, 0], shfnp[mp - 1, 1], shfnp[mp - 1, 2] # Ni
            #Np[1,0], Np[1,1], Np[1,2] = shfnp[mp - 1, 3], shfnp[mp - 1, 4], shfnp[mp - 1, 5] # Ni,x
            #Np[2,0], Np[2,1], Np[2,2] = shfnp[mp - 1, 6], shfnp[mp - 1, 7], shfnp[mp - 1, 8] # Ni,y
            
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
            F = np.dot((np.identity(2) + Lp*dtime), Fp[mp - 1, :].reshape((2, 2)))
            #Fpt = np.zeros((2, 2)) # matriz grandiente deformacion en tiempo t
            #Fpt[0, 0], Fpt[0, 1], Fpt[1, 0], Fpt[1, 1] = Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3]
            #F = np.dot((np.identity(2) + Lp*dtime), Fpt) # matriz grandiente de deformacion en el tiempo t+1
            Fp[mp - 1, :] = F.reshape((1, 4))
            #Fp[mp - 1, 0], Fp[mp - 1, 1], Fp[mp - 1, 2], Fp[mp - 1, 3] = F[0, 0], F[0, 1], F[1, 0], F[1, 1] 
            # actualizar volumen de las particulas
            Vp[mp - 1] = np.linalg.det(F) * Vp0[mp - 1]
            # calculo de incremento de deformacion y de esfuerzos
            deps1 = dtime / 2 * (Lp + Lp.T) # se obtiene tensor de deformaciones!!
            deps = np.array([deps1[0,0], deps1[1,1], 2*deps1[0,1]]) # notacion de Voight
            nor_deps = np.linalg.norm(deps)
            
            if nor_deps == 0:
                # incremento de deformacion nulo!!
                pass
            else:
                # incremento de deformacion no nulo!!
            
                # actualizacion de esfuerzo - depende si eslastico o plastico
            
                if elapla == 0:
                    # lineal elastico
                    C2D_stress = constitutive_matrix_elastic(1, Prop[mp - 1,0], Prop[mp - 1,1]) # matriz constitutiva condicion plana de esfuerzos
                    dsig = np.dot(C2D_stress, deps) # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
                    dsig1 = np.zeros(4)
                    dsig1[:3], dsig1[3] = dsig, Prop[mp - 1,1]*(dsig[0] + dsig[1])
                    # Actualizar esfuerzo y deformacion sumando el incremento
                    epse[mp - 1, :] += deps
                    sig[mp - 1, :] += dsig1
                else:
                    # Elastoplastico
                    nincr = 10 # 10 incrementos
                    for m in range(nincr):
                        sig[mp-1,:], depse, depsp, Prop[mp-1,5] = MC_elastoplastic2(sig[mp-1,:], deps/nincr, Prop[mp-1,:])
                        epse[mp-1,:] += depse
                        epsp[mp-1,:] += depsp
        
        # Fin ciclo en las particulas
    
    return Fp, Vp, epse, epsp, sig


# ====================================================================
# === Funcion para transferir de los nodos a las particulas los esfeurzos ===

@njit#('Tuple((f8[:,:], f8[:], f8[:,:], f8[:,:]))(Tuple((i8[:,:], f8[:,:], i8[:], i8[:], i8[:,:])), Tuple((f8[:,:], f8[:], f8[:], f8[:,:], f8[:,:], f8[:,:], f8[:], f8[:])), f8[:,:], f8 )')
def nodes_to_particle_stress_gauss(grid, particle, bound_val ,nvel, dtime, elapla): 
    """ Funcion que calcula esfuerzo y deformacion de las particulas, transfiriendo la velocidad nodal de las particulas
        para el calculo del gradiente de velocida Lp - Metodo MUSL, doble transferencia
        Variable elapla = 0 (cero) Lineal elastico
                        = 1 (uno) Elastoplastico perfecto
        ------
        Return ----
                xp = vector posicion de las particulas
                vp = vector velocidad de las particulas
                vn = vector de velocidad nodal"""
                
    assert (elapla == 1 or elapla == 0), "La variable elapla debe ser 0(cero) o 1(uno)"
    # organizando los argumentos de las listas
    inci, cor, active_elem, active_nodes, mp_elem = grid
    Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop = particle

    # ==================================================================
    # ciclo en los elementos activos
    for i in range(len(active_elem)):
        ele = active_elem[i] # numero del elemento
        nodes = inci[ele - 1,:] # nodos asocidos al elemento
        xn = cor[nodes - 1, :] # coordenasdas de los nodos
        mpe = elem_i_mp(mp_elem, active_elem[i]) # MPs (particulas) en el elemento i
        Vele = elem_area(xn) # Volumen de los elementos
        
        # verificacion si es un elemento lleno o parcialmente lleno
        if np.sum(bound_val[mpe - 1]) >= 1 and np.sum(Vp[mpe - 1]) < 0.9 * Vele:
            # el elemento es parcialmente lleno 
            # APLICAR PROCEDIMIENTO CORREINTE ????
            inte_ptcl = True
            # ciclo en las particulas
            for j in range(len(mpe)):
                mp = mpe[j] # numero de mp - particula
                # organizado las funciones de forma y sus derivadas en el array correspondiente - solo funciona para elm trian
                Np = np.zeros((3, len(nodes))) # array para funciones de forma
                Np = shfnp[mp - 1,:].reshape((3, len(nodes)))
                
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
                F = np.dot((np.identity(2) + Lp*dtime), Fp[mp - 1, :].reshape((2, 2)))
                Fp[mp - 1, :] = F.reshape((1, 4))
                # actualizar volumen de las particulas
                Vp[mp - 1] = np.linalg.det(F) * Vp0[mp - 1]
                # calculo de incremento de deformacion y de esfuerzos
                deps1 = dtime / 2 * (Lp + Lp.T) # se obtiene tensor de deformaciones!!
                deps = np.array([deps1[0,0], deps1[1,1], 2*deps1[0,1]]) # notacion de Voight
                
                # actualizacion de esfuerzo - depende si eslastico o plastico
                if elapla == 0:
                    # lineal elastico
                    C2D_stress = constitutive_matrix_elastic(1, Prop[mp - 1,0], Prop[mp - 1,1]) # matriz constitutiva condicion plana de esfuerzos
                    dsig = np.dot(C2D_stress, deps) # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
                    dsig1 = np.zeros(4)
                    dsig1[:3], dsig1[3] = dsig, Prop[mp - 1,1]*(dsig[0] + dsig[1])
                    # Actualizar esfuerzo y deformacion sumando el incremento
                    epse[mp - 1, :] += deps
                    sig[mp - 1, :] += dsig1
                else:
                    # Elastoplastico
                    for m in range(10):
                        # dividiendo el incremento de deformacion en 10 subincrementos
                        sig[mp-1,:], depse, depsp, Prop[mp-1,5] = MC_elastoplastic2(sig[mp-1,:], deps/10, Prop[mp-1,:])
                        epse[mp-1,:] += depse
                        epsp[mp-1,:] += depsp
        
        
        else:
            # el elemento esta completamente lleno
            # APLICAR EUACION CONSTITUTIVA EN LOS PUNTOS DE GAUSS
            inte_ptcl = False
            
            # Calulando el esfuerzo promedio a asignar a el punto de Gauss
            sigq = np.zeros(4)
            sigq[0] = np.sum(sig[mpe - 1, 0]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            sigq[1] = np.sum(sig[mpe - 1, 1]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            sigq[2] = np.sum(sig[mpe - 1, 2]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            sigq[3] = np.sum(sig[mpe - 1, 3]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            # calculando el grandiente de deformacion promedio - punto de gauss
            Fq = np.zeros(4)
            Fq[0] = np.sum(Fp[mpe - 1, 0]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            Fq[1] = np.sum(Fp[mpe - 1, 1]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            Fq[2] = np.sum(Fp[mpe - 1, 2]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            Fq[3] = np.sum(Fp[mpe - 1, 3]*Vp[mpe - 1])/ np.sum(Vp[mpe - 1])
            # solo se utiliza un punto de Gauss
            Nq = shapfunc_gauss1(xn) # funciones de forma evaluadas en el punto de Gauss
            # propiedades en el punto de Gauss???
    
            # ciclo en los nodos del elemento
            Lq = np.zeros((2, 2)) # creando matriz gradiente de velociad para el punto de gauss
            for k in range(len(nodes)):
                nng = nodes[k] # numero del nodo global
                # -- ciclo para determinar ubicacion del nodo en la lista de nodos activos--
                for m in range(len(active_nodes)):
                    if active_nodes[m] == nng:
                        nna = m
                        break
                # -- fin de ciclo
                
                # Calculo de gradiente de velocidad y salir del ciclo en los nodos
                #Lp += np.array([[nvel[nna, 0]], [nvel[nna, 1]]]) * np.array([[Np[1, k], Np[2, k]]])
                Lq[0, 0] += nvel[nna, 0]*Nq[1, k]
                Lq[0, 1] += nvel[nna, 0]*Nq[2, k]
                Lq[1, 0] += nvel[nna, 1]*Nq[1, k]
                Lq[1, 1] += nvel[nna, 1]*Nq[2, k]
            
            # Calculo de grandiente de deformacion
            F = np.dot((np.identity(2) + Lq*dtime), Fq.reshape((2, 2)))
            Fp[mpe - 1, :] = F.reshape((1, 4)) # Es correcto ??
            # actualizar volumen de las particulas
            Vp[mpe - 1] = np.linalg.det(F) * Vp0[mpe - 1] # Es correcto ????
            # calculo de incremento de deformacion 
            deps1 = dtime / 2 * (Lq + Lq.T) # Tensor de defomacion
            deps = np.array([deps1[0,0], deps1[1,1], 2*deps1[0,1]]) # Vector de def notacion de Voight
            
            # actualizacion de esfuerzo - depende si eslastico o plastico
            if elapla == 0:
                # lineal elastico
                mp = mpe[0] # Para tomar las propiedades de la particula 1
                C2D_stress = constitutive_matrix_elastic(1, Prop[mp - 1,0], Prop[mp - 1,1]) # matriz constitutiva condicion plana de esfuerzos
                dsig = np.dot(C2D_stress, deps) # multiplicar matriz constitutiva por vector de deformaciones - notacion de Voight!!
                dsig1 = np.zeros(4)
                dsig1[:3], dsig1[3] = dsig, Prop[mp - 1,1]*(dsig[0] + dsig[1])
                # Actualizar esfuerzo y deformacion sumando el incremento
                epse[mpe - 1, :] += deps # Es correcto?
                sig[mpe - 1, :] += dsig1 # Es correcto?
            else:
                # Elastoplastico
                # PENDIENTE POR ACTUALIZAR  - VARIABLE YIELD
                Propq = Prop[mpe[0] - 1,:] # tomando las propiedades de la 1 particula
                for m in range(10):
                    # tomando 10 subincrementos de deformacion
                    sigq, depse, depsp, Propq[5] = MC_elastoplastic2(sigq, deps/10, Propq)
                    sig[mpe - 1,:] = sigq
                    epse[mpe - 1,:] += depse
                    epsp[mpe - 1,:] += depsp
                    Prop[mpe - 1,5] = Propq[5] # actualizar variable Yield
    
        
    return Fp, Vp, epse, epsp, sig


# ======================================================================================
# ============ Funcion para determinar equilibrio cuasi-estatico =======================

def static_convergence(nmass, niforce, neforce, nvel, dtime, nework0):
    """Funcion para determinacion de equilibrio cuasi-estatico, a partir de la fuerza de desbalance
        y la energia cinetica de las fuerzas externas"""
    
    # criterio de balance de fuerzas
    #ff = abs(np.linalg.norm(neforce) - np.linalg.norm(niforce))/np.linalg.norm(neforce)
    ff = np.linalg.norm(neforce + niforce)/np.linalg.norm(neforce)
    
    # criterio de energia cinetica
    ke = 1/2*np.sum(nmass*nvel*nvel) # energia cinetica
    du = nvel*dtime # desplazamiento nodal
    nework = nework0 + np.sum(du*neforce) # trabajo externo
    ee = ke/nework
    
    return ff, ee, nework

# ======================================================================================
# ============ Funcion para determinar equilibrio cuasi-estatico =======================

def static_convergence2(nmass, niforce, neforce, ndamping, nvel, dtime, nework, ff, ee, t, efo, ifo, ke):
    """Funcion para determinacion de equilibrio cuasi-estatico, a partir de la fuerza de desbalance
        y la energia cinetica de las fuerzas externas"""
    
    # criterio de balance de fuerzas
    ff[t] = np.linalg.norm(neforce + niforce)/np.linalg.norm(neforce)
    efo[t] = np.linalg.norm(neforce)
    ifo[t] = np.linalg.norm(niforce)
    # criterio de energia cinetica
    ke[t] = 1/2*np.sum(nmass*nvel*nvel) # energia cinetica
    du = nvel*dtime # desplazamiento nodal
    nework[t + 1] = nework[t] + np.sum(du*neforce) # trabajo externo
    ee[t] = ke[t]/nework[t + 1]
    
    return ff, ee, efo, ifo,ke, nework

# =====================================================================================
# ========== Funcion algorimto de contacto ===========================================

def contact(body1, body2, nmassS, nmomentumS, mesh, dt, miu):
    """Funcion para lal correcion de velocidad nodal para un algoritmo de contacto friccional
        de coulomb - Algoritmo predictor corrector"""
    
    inci, cor, node_support, active_nodes = mesh
    nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1 = body1
    nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2 = body2
    
    # numero de nodos activos en el sistema
    nnodes = len(nmass_1[:,0])
    # crear array para almacenar la velocidad nodal
    nvelo_1 = np.zeros((nnodes, 2))
    nvelo_2 = np.zeros((nnodes, 2))
    nveloS = np.zeros((nnodes, 2))
    
    for i in range(nnodes):
        if nmass_1[i] != 0: # evitar division por cero
            nvelo_1[i,0] = nmomentum_1[i,0] / nmass_1[i]
            nvelo_1[i,1] = nmomentum_1[i,1] / nmass_1[i]
        if nmass_2[i] != 0:
            nvelo_2[i,0] = nmomentum_2[i,0] / nmass_2[i]
            nvelo_2[i,1] = nmomentum_2[i,1] / nmass_2[i]
        # velocidad del sistema
        nveloS[i,0] = nmomentumS[i,0] / nmassS[i]
        nveloS[i,1] = nmomentumS[i,1] / nmassS[i]
    
    
    #  ########## CUERPO 1 #####################
    # id nodes activos cuerpo 1 dentro del array elementos activos del sistema
    id_nodes_1 = np.array([np.where(active_nodes == active_nodes_1[i])[0][0] for i in range(len(active_nodes_1))])
    # detectar nodos de contacto
    ncontac_1 = np.unique(np.where(np.absolute(nvelo_1[id_nodes_1,:] - nveloS[id_nodes_1,:]) > 1e-10)[0]) # numeracion en nodos activos del cuerpo 2
    ncontac_1S = id_nodes_1[ncontac_1] # numeracion en nodos activos del sistema    
    ncontac_1G = active_nodes[ncontac_1S] # ??????? numeracion en nodos globales - Indexacion desde 1!
    
    # Calculo de normales de los nodos
    #norm_1 = normals(ncontac_1G, node_support, active_elem_1, mp_elem_1, inci, cor, Mp_1, xp_1)
    norm_1 = np.zeros((len(ncontac_1G),2))
    norm_1[:,1] = 1
    
    # Detectar cuerpos se aproximan o se separan
    vel_rela = np.dot((nvelo_1[ncontac_1S,:] - nveloS[ncontac_1S,:]), np.transpose(norm_1)).diagonal() # array 1D
    naprox = np.where(vel_rela > 0)[0] # nodos aproximan en los nodos de contacto
    naproxS = ncontac_1S[naprox] # nodos aproximan en los nodos activos del sistema
    
    # componentes de velocidad relativa
    vnormal = np.multiply(norm_1[naprox,:], np.transpose(np.array([vel_rela[naprox]])))
    vtangen = nvelo_1[naproxS,:] - nveloS[naproxS,:] - vnormal
    
    # +++ Correccion componente normal de velocidad ++++
    nvelo_1[naproxS,:] = nvelo_1[naproxS,:] - vnormal
    
    # Fuerza tangenete
    Ftan_1 = 1/dt * np.multiply(nmass_1[naproxS], vtangen) # fuerza tangente - Array 2D
    magFtan_1 = np.array([np.sqrt(Ftan_1[:,0]**2 + Ftan_1[:,1]**2)]) # magnitud fuerza tangente - Array 2D fila
    tan_1 = np.divide(Ftan_1, np.transpose(magFtan_1), out=np.zeros_like(Ftan_1), where=np.transpose(magFtan_1) !=0) # Vector tange unitaria
    
    # nodos a corregir por exeder fuerza tangente - nodos que deslizan
    Fcoulomb_1 = miu / dt * np.multiply(nmass_1[naproxS], np.transpose(np.array([vel_rela[naprox]]))) # fuerza tangente maxima
    ntang = np.where(magFtan_1[0,:] > Fcoulomb_1[:,0])[0] # id nodos que deslizan en los nodos que aproximan
    ntangS = ncontac_1S[naprox[ntang]] # id nodos que deslizan en los nodos activos del sistema
    nstick = np.where(magFtan_1[0,:] <= Fcoulomb_1[:,0])[0] # id nodos que NO deslizan
    nstickS = ncontac_1S[naprox[nstick]] # id nodos que NO delsizan en los nodos activos del sistema
    
    # +++  Correccion componente tangente de velocidad
    nvelo_1[ntangS,:] = nvelo_1[ntangS, :] - miu * np.multiply(tan_1[ntang,:], np.transpose(np.array([vel_rela[naprox[ntang]]])))
    nvelo_1[nstickS,:] = nvelo_1[nstickS, :] - vtangen[nstick, :] # correccion velocidad stick
    # ############# FIN CUERPO 1 #################################
    
    
    #  ########## CUERPO 2 #####################
    # id nodes activos cuerpo 2 dentro del array elementos activos del sistema
    id_nodes_2 = np.array([np.where(active_nodes == active_nodes_2[i])[0][0] for i in range(len(active_nodes_2))])
    # detectar nodos de contacto
    ncontac_2 = np.unique(np.where(np.absolute(nvelo_2[id_nodes_2,:] - nveloS[id_nodes_2,:]) > 1e-10)[0]) # numeracion en nodos activos del cuerpo 2
    ncontac_2S = id_nodes_2[ncontac_2] # numeracion en nodos activos del sistema    
    ncontac_2G = active_nodes[ncontac_2S] # ??????? numeracion en nodos globales - Indexacion desde 1!
    
    if np.all(ncontac_1G == ncontac_2G):
        pass
    else:
        print("diferentes nodos en contacto entre los cuerpos!!")
    
    
    # Calculo de normales de los nodos
    norm_2 = - norm_1 # garantizar colinealidad de las normales
    #norm_2 = normals(ncontac_2G, node_support, active_elem_2, mp_elem_2, inci, cor, Mp_2, xp_2)
    
    # Detectar cuerpos se aproximan o se separan
    vel_rela = np.dot((nvelo_2[ncontac_2S,:] - nveloS[ncontac_2S,:]), np.transpose(norm_2)).diagonal() # array 1D
    naprox = np.where(vel_rela > 0)[0] # nodos aproximan en los nodos de contacto
    naproxS = ncontac_2S[naprox] # nodos aproximan en los nodos activos del sistema
    
    # componentes de velocidad relativa
    vnormal = np.multiply(norm_2[naprox,:], np.transpose(np.array([vel_rela[naprox]])))
    vtangen = nvelo_2[naproxS,:] - nveloS[naproxS,:] - vnormal
    
    # +++ Correccion componente normal de velocidad ++++
    nvelo_2[naproxS,:] = nvelo_2[naproxS,:] - vnormal
    
    # Fuerza tangenete
    Ftan_2 = 1/dt * np.multiply(nmass_2[naproxS], vtangen) # fuerza tangente - Array 2D
    magFtan_2 = np.array([np.sqrt(Ftan_2[:,0]**2 + Ftan_2[:,1]**2)]) # magnitud fuerza tangente - Array 2D fila
    tan_2 = np.divide(Ftan_2, np.transpose(magFtan_2), out=np.zeros_like(Ftan_2), where=np.transpose(magFtan_2) !=0) # Vector tange unitaria
    
    # nodos a corregir por exeder fuerza tangente - nodos que deslizan
    Fcoulomb_2 = miu / dt * np.multiply(nmass_2[naproxS], np.transpose(np.array([vel_rela[naprox]]))) # fuerza tangente maxima
    ntang = np.where(magFtan_2[0,:] > Fcoulomb_2[:,0])[0] # id nodos que deslizan en los nodos que aproximan
    ntangS = ncontac_2S[naprox[ntang]] # id nodos que deslizan en los nodos activos del sistema
    nstick = np.where(magFtan_2[0,:] <= Fcoulomb_2[:,0])[0] # id nodos que NO deslizan
    nstickS = ncontac_2S[naprox[nstick]] # id nodos que NO delsizan en los nodos activos del sistema
    
    # +++  Correccion componente tangente de velocidad
    nvelo_2[ntangS,:] = nvelo_2[ntangS, :] - miu * np.multiply(tan_2[ntang,:], np.transpose(np.array([vel_rela[naprox[ntang]]])))
    nvelo_2[nstickS,:] = nvelo_2[nstickS, :] - vtangen[nstick, :] # correccion velocidad stick
    
    # ############# FIN CUERPO 2 #################################
    
    # recalcular el momentum nodal con las velocidades corregidas
    nmomentum_1 = np.multiply(nmass_1, nvelo_1)
    nmomentum_2 = np.multiply(nmass_2, nvelo_2)
    
    return nmomentum_1, nmomentum_2
    
    
    
    
    
