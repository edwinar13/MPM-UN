## Modulo con las funciones para crear y operar malla de FE
from __future__ import division, print_function
import numpy as np
import numba
import math

# ===== funcion para crear malla de elemntos finitos triangulares =====

def create_uniform2(dimx, dimy, ele_size):
    """ Funcion que crea una malla regular uniforme de ancho dimx por dimy
        Elementos triangulares lineales
        dimx = ancho en x 
        dimy = ancho en y
        ele_size = Tamano de los elementos"""   
    #======= Instrucciones para el calculo de tabla de coordenadas ========
    nelex = int(round(dimx / ele_size)) ; neley = int(round(dimy / ele_size))
    assert (abs(dimx/ele_size - round(dimx/ele_size)) < 1e-11), "El numero de elementos no se ajusta en la direccion x"
    assert (abs(dimy/ele_size - round(dimy/ele_size))< 1e-11), "El numero de elementos no se ajusta en la direccion y"
    nnodesx = nelex + 1 ; nnodesy = neley + 1
    xx, yy = np.meshgrid(np.linspace(0, dimx, nnodesx), np.linspace(0, dimy, nnodesy))
    coord = np.empty((nnodesx * nnodesy, 2))
    coord[:, 0] = xx.reshape(1, nnodesx * nnodesy)
    coord[:, 1] = yy.reshape(1, nnodesx * nnodesy)
    
    # ====== Instruciones para el calculo de tabla de incidencias ========
    @numba.njit('i8[:,:](i8[:,:], i8, i8, i8)')
    def incidencias(inci, nnodesx, nodesy, nelex): 
        for j in range(nnodesy-1):
            for i in range(1, nnodesx):
                m = 2 * nelex * j + 2 * i - 1
                inci[m - 1, 0] = nnodesx * j + i ; inci[m, 0] = nnodesx * j + i + 1 #columna 1 nodo 1
                inci[m - 1, 1] = inci[m, 0] ; inci[m, 1] = nnodesx*(j + 1) + i + 1 #columna 2 nodo 2
                inci[m - 1, 2] = nnodesx*(j + 1) + i ; inci[m, 2] = inci[m - 1, 2] # columna 3  nodo 3
        return inci
    inci = np.empty((nelex*neley*2, 3)).astype(int)
    inci = incidencias(inci, nnodesx, nnodesy, nelex)    
            
    return coord, inci, nelex*2

#============================================================================
# ===== funcion para crear malla de elemntos finitos cuadrilaterales bilineales =====

def create_uniform(dimx, dimy, ele_size):
    """ Funcion que crea una malla regular uniforme de ancho dimx por dimy
        Elementos cuadrilaterals bilineales
        dimx = ancho en x 
        dimy = ancho en y
        ele_size = Tamano de los elementos"""   
    #======= Instrucciones para el calculo de tabla de coordenadas ========

    coord = None
    inci = None
    nelex = None
    error = False

    nelex = int(round(dimx / ele_size)) ; neley = int(round(dimy / ele_size))

    if abs(dimx/ele_size - round(dimx/ele_size)) > 1e-11:
        print("El numero de elementos no se ajusta en la direccion x")
        error= True
        return coord ,inci ,nelex, error
    if abs(dimy/ele_size - round(dimy/ele_size)) > 1e-11:
        print("El numero de elementos no se ajusta en la direccion y")
        error= True
        return coord ,inci ,nelex, error

    assert (abs(dimx/ele_size - round(dimx/ele_size)) < 1e-11), "El numero de elementos no se ajusta en la direccion x"
    assert (abs(dimy/ele_size - round(dimy/ele_size))< 1e-11), "El numero de elementos no se ajusta en la direccion y"
    nnodesx = nelex + 1 ; nnodesy = neley + 1
    xx, yy = np.meshgrid(np.linspace(0, dimx, nnodesx), np.linspace(0, dimy, nnodesy))
    coord = np.empty((nnodesx * nnodesy, 2))
    coord[:, 0] = xx.reshape(1, nnodesx * nnodesy)
    coord[:, 1] = yy.reshape(1, nnodesx * nnodesy)
    
    # ====== Instruciones para el calculo de tabla de incidencias ========
    @numba.njit#('i8[:,:](i8[:,:], i8, i8, i8)')
    def incidencias(inci, nnodesx, nodesy, nelex): 
        for j in range(nnodesy-1):
            for i in range(1, nnodesx):
                m = nelex * j + i - 1
                inci[m , 0] = nnodesx * j + i ; # nodo1
                inci[m , 1] = nnodesx * j + i + 1 # nodo2
                inci[m , 2] = nnodesx*(j + 1) + i + 1 # nodo 3
                inci[m , 3] = nnodesx*(j + 1) + i # nodo 4
        return inci
    inci = np.empty((nelex*neley, 4)).astype(int)
    inci = incidencias(inci, nnodesx, nnodesy, nelex)    
    '''
     return
        coord: devuelve lista de corrdenadas x y y [[x0,y0],[x1,y1], ...  [xf,yf]]
        inci: devuelve lista de nodos en cada elemento
        nelex: devuelve No de elemtos en x

    '''
    return coord, inci, nelex, error


def create_uniform_quadrilateral(dimx, dimy, ele_size):
    """ Funcion que crea una malla regular uniforme de ancho dimx por dimy
        Elementos cuadrilaterals bilineales
        dimx = ancho en x 
        dimy = ancho en y
        ele_size = Tamano de los elementos"""   

    ###################################################################################################################
    #   NOTA: se basa de << create_uniform >> y se ajusta para que no se cree la malla desde cero, sino desde las coordenadas recibidas
    ###################################################################################################################
    
    #======= Instrucciones para el calculo de tabla de coordenadas ========
    nelex = int(round(dimx / ele_size)) ; neley = int(round(dimy / ele_size))
    assert (abs(dimx/ele_size - round(dimx/ele_size)) < 1e-11), "El numero de elementos no se ajusta en la direccion x"
    assert (abs(dimy/ele_size - round(dimy/ele_size))< 1e-11), "El numero de elementos no se ajusta en la direccion y"
    nnodesx = nelex + 1 ; nnodesy = neley + 1
    xx, yy = np.meshgrid(np.linspace(0, dimx, nnodesx), np.linspace(0, dimy, nnodesy))
    coord = np.empty((nnodesx * nnodesy, 2))
    coord[:, 0] = xx.reshape(1, nnodesx * nnodesy)
    coord[:, 1] = yy.reshape(1, nnodesx * nnodesy)
    
    # ====== Instruciones para el calculo de tabla de incidencias ========
    @numba.njit#('i8[:,:](i8[:,:], i8, i8, i8)')
    def incidencias(inci, nnodesx, nodesy, nelex): 
        for j in range(nnodesy-1):
            for i in range(1, nnodesx):
                m = nelex * j + i - 1
                inci[m , 0] = nnodesx * j + i ; # nodo1
                inci[m , 1] = nnodesx * j + i + 1 # nodo2
                inci[m , 2] = nnodesx*(j + 1) + i + 1 # nodo 3
                inci[m , 3] = nnodesx*(j + 1) + i # nodo 4
        return inci
    inci = np.empty((nelex*neley, 4)).astype(int)
    inci = incidencias(inci, nnodesx, nnodesy, nelex)    
    '''
     return
        coord: devuelve lista de corrdenadas x y y [[x0,y0],[x1,y1], ...  [xf,yf]]
        inci: devuelve lista de nodos en cada elemento
        nelex: devuelve No de elemtos en x

    '''
    return coord, inci, nelex


# ============================================================================
# ======= funcion que obtiene el array de soporte nodal =====================

def node_conectivity(inci, nnodes):
    """Funcion que devuelve el array con el id de los elementos asociados a cada nodo"""
    
    node_support = np.zeros((nnodes, 4)).astype(int)
    
    for i in range(nnodes):
        temp = np.where(inci[:,:] == (i+1))[0] + 1
        node_support[i, :len(temp)] = temp
      
    return node_support


#=========================================================
# ======= Funcion que fija los nodos del contorno ========

def contour_fixe(nnodesx, nnodesy, left, right, up, down):
    """Funcion que fija los nodos del contorno de la malla de elementos como nodos de Dirichlet
       Fija estos con una restriccion de movimiento en x o en y dependiendo de los arguentos ingresados
       
       Argumentos --
            nnodesx = numero de nodos en direccion x
            nnodesy = numero de nodos en direccion y
            up y down     =  escalar con valor 0 si la restriccion es solo en la direccion y o 1 si es en ambas direcciones
            left y right  =  escalar con valor 0 si la restriccion es solo en la direccion x o 1 si es es ambas direcciones
       return --
               fixed_nodesX = array 1D con la lista de nodos que presentan restriccion de movimiento en direccion x
               fixed_nodesY = array 1D con la lista de nodos que presentan restriccion de movimiento en direccion y """
    
    # verificando valores de entrada
    assert (left == 0 or left == 1), "el argumento left debe tener un valor de 1 o 0"
    assert (right == 0 or right == 1), "el argumento right debe tener un valor de 1 o 0"
    assert (up == 0 or up == 1), "el argumento up debe tener un valor de 1 o 0"
    assert (down == 0 or down == 1), "el argumento down debe tener un valor de 1 o 0"
    # creando array con los nodos de cada lado
    nodes_left = np.linspace(1,(nnodesy - 1)*nnodesx + 1, nnodesy).astype(int)
    nodes_right = np.linspace(nnodesx, nnodesx*nnodesy, nnodesy).astype(int)
    nodes_down = np.linspace(1, nnodesx, nnodesx).astype(int)
    nodes_up = np.linspace((nnodesy - 1)*nnodesx + 1, nnodesx*nnodesy, nnodesx).astype(int)
    
    # concatenando en los arrays nodos fijosx y nodos fijos y
    fixed_nodesX = np.concatenate((nodes_left, nodes_right), axis=0)
    fixed_nodesY = np.concatenate((nodes_down, nodes_up), axis=0)
    # evaluando las condiciones para concatenar adicionales
    if left == 1:
        fixed_nodesY = np.concatenate((fixed_nodesY, nodes_left), axis=0)
    if right == 1:
        fixed_nodesY = np.concatenate((fixed_nodesY, nodes_right), axis=0)
    if up == 1:
        fixed_nodesX = np.concatenate((fixed_nodesX, nodes_up), axis=0)
    if down == 1:
        fixed_nodesX = np.concatenate((fixed_nodesX, nodes_down), axis=0)
    
    return np.unique(fixed_nodesX), np.unique(fixed_nodesY)




















# ====================================================
# =========== Funcion para inicialiar MP =============

def setup_MP2(xi, yi, xf, yf, cor, inci, num=1):
    """ Funcion para inicializar los MP en los elementos de la malla - TRIANGULAR LINEAL
        (xi, yi) y (xf, yf) corresponde a las coordenadas iniciales y finales del continuo del problema 
        - el area RECTANGULAR donde se crearan los MP
        cor = es la matriz de coordenadas de los nodos de la malla de elementos
        inci = en la matriz de incidencias de la malla de elementos
        num = es el numero de MP por elemento - por defecto es igual a 1"""
    assert (num == 1 or num == 4 or num == 6 or num == 12), "Esta funcion solo acepta 1, 4, 6 o 12 MP por elemento"
    assert (min(cor[:,0])<= xi and min(cor[:,1])<= yi),"El punto (xi, yi) esta fuera del dominio de la malla de elementos"
    assert (max(cor[:,0])>= xf and max(cor[:,1])>= yf),"El punto (xf, yf) esta fuera del dominio de la malla de elementos"
    mp_elem = np.empty((len(inci)*num, 1)).astype(int)
    mp_coord = np.empty((len(inci)*num, 2))
    cont = 0 # contador para el numero de MP
    for i in range(len(inci)):
        x1 = cor[inci[i, 0] - 1, 0] ; y1 = cor[inci[i, 0] - 1, 1]
        x2 = cor[inci[i, 1] - 1, 0] ; y2 = cor[inci[i, 1] - 1, 1]
        x3 = cor[inci[i, 2] - 1, 0] ; y3 = cor[inci[i, 2] - 1, 1]
        if min(x1, x2, x3) >= xi and min(y1, y2, y3) >= yi and max(x1, x2, x3) <= xf and max(y1, y2, y3) <= yf:
            # el elemento i se encuentra dentro del rango del continuo (xi, yi) - (xf, yf)
            if num == 1:
                mp_elem[cont, 0] = i + 1 # elemnto al que pertenece el MP
                mp_coord[cont, 0] = 1/3*(x1 + x2 + x3) ; mp_coord[cont, 1] = 1/3*(y1 + y2 + y3) # coordenadas del MP
                cont += 1 # aumentar el contador
            elif num == 4:
                mp_elem[cont, 0] = i + 1 # MP uno del elemento
                mp_coord[cont, 0] = 1/3*(x1 + x2 + x3) ; mp_coord[cont, 1] = 1/3*(y1 + y2 + y3)
                mp_elem[cont + 1, 0] = i + 1 # MP dos del elemento
                mp_coord[cont + 1, 0] = (4*x1 + x2 + x3)/6; mp_coord[cont + 1, 1] = (4*y1 + y2 + y3)/6
                mp_elem[cont + 2, 0] = i + 1 # MP tres del elemento
                mp_coord[cont + 2, 0] = (x1 + 4*x2 + x3)/6; mp_coord[cont + 2, 1] = (y1 + 4*y2 + y3)/6
                mp_elem[cont + 3, 0] = i + 1 # MP 4 del elemento
                mp_coord[cont + 3, 0] = (x1 + x2 + 4*x3)/6; mp_coord[cont + 3, 1] = (y1 + y2 + 4*y3)/6
                cont += 4 # aumentar el contador
            elif num == 6:
                if x1 < x2: # elemento inferior izquierdo
                    mp_elem[cont, 0] = i + 1 # MP uno del elemento
                    mp_coord[cont, 0] = (8*x1 + 3*x2 + x3)/12 ; mp_coord[cont, 1] = (8*y1 + 3*y2 + y3)/12
                    mp_elem[cont + 1, 0] = i + 1 # MP dos del elemento
                    mp_coord[cont + 1, 0] = (2*x1 + 9*x2 + x3)/12 ; mp_coord[cont + 1, 1] = (2*y1 + 9*y2 + y3)/12
                    mp_elem[cont + 2, 0] = i + 1 # MP tres del elemento
                    mp_coord[cont + 2, 0] = (8*x1 + x2 + 3*x3)/12 ; mp_coord[cont + 2, 1] = (8*y1 + y2 + 3*y3)/12
                    mp_elem[cont + 3, 0] = i + 1 # MP cuatro del elemento
                    mp_coord[cont + 3, 0] = (3*x1 + 6*x2 + 3*x3)/12 ; mp_coord[cont + 3, 1] = (3*y1 + 6*y2 + 3*y3)/12
                    mp_elem[cont + 4, 0] = i + 1 # MP cinco del elemento
                    mp_coord[cont + 4, 0] = (3*x1 + 3*x2 + 6*x3)/12 ; mp_coord[cont + 4, 1] = (3*y1 + 3*y2 + 6*y3)/12
                    mp_elem[cont + 5, 0] = i + 1 # MP seis del elemento
                    mp_coord[cont + 5, 0] = (2*x1 + x2 + 9*x3)/12 ; mp_coord[cont + 5, 1] = (2*y1 + y2 + 9*y3)/12
                else: # elemento superior derecho
                    mp_elem[cont, 0] = i + 1 # MP uno del elemento
                    mp_coord[cont, 0] = (9*x1 + 2*x2 + x3)/12 ; mp_coord[cont, 1] = (9*y1 + 2*y2 + y3)/12
                    mp_elem[cont + 1, 0] = i + 1 # MP dos del elemento
                    mp_coord[cont + 1, 0] = (6*x1 + 3*x2 + 3*x3)/12 ; mp_coord[cont + 1, 1] = (6*y1 + 3*y2 + 3*y3)/12
                    mp_elem[cont + 2, 0] = i + 1 # MP tres del elemento
                    mp_coord[cont + 2, 0] = (3*x1 + 3*x2 + 6*x3)/12 ; mp_coord[cont + 2, 1] = (3*y1 + 3*y2 + 6*y3)/12
                    mp_elem[cont + 3, 0] = i + 1 # MP cuatro del elemento
                    mp_coord[cont + 3, 0] = (3*x1 + 8*x2 + x3)/12 ; mp_coord[cont + 3, 1] = (3*y1 + 8*y2 + 1*y3)/12
                    mp_elem[cont + 4, 0] = i + 1 # MP cinco del elemento
                    mp_coord[cont + 4, 0] = (x1 + 8*x2 + 3*x3)/12 ; mp_coord[cont + 4, 1] = (y1 + 8*y2 + 3*y3)/12
                    mp_elem[cont + 5, 0] = i + 1 # MP seis del elemento
                    mp_coord[cont + 5, 0] = (x1 + 2*x2 + 9*x3)/12 ; mp_coord[cont + 5, 1] = (y1 + 2*y2 + 9*y3)/12
                cont += 6 #aumentar el contador
            elif num == 12:
                if x1 < x2: #elemento inferior izquierdo
                    mp_elem[cont, 0] = i + 1 # MP uno del elemento
                    mp_coord[cont, 0] = (9*x1 + 2*x2 + x3)/12 ; mp_coord[cont, 1] = (9*y1 + 2*y2 + y3)/12
                    mp_elem[cont + 1, 0] = i + 1 # MP dos del elemento
                    mp_coord[cont + 1, 0] = (5*x1 + 6*x2 + x3)/12 ; mp_coord[cont + 1, 1] = (5*y1 + 6*y2 + y3)/12
                    mp_elem[cont + 2, 0] = i + 1 # MP tres del elemento
                    mp_coord[cont + 2, 0] = (x1 + 10*x2 + x3)/12 ; mp_coord[cont + 2, 1] = (y1 + 10*y2 + y3)/12
                    mp_elem[cont + 3, 0] = i + 1 # MP cuatro del elemento
                    mp_coord[cont + 3, 0] = (9*x1 + x2 + 2*x3)/12 ; mp_coord[cont + 3, 1] = (9*y1 + y2 + 2*y3)/12
                    mp_elem[cont + 4, 0] = i + 1 # MP cinco del elemento
                    mp_coord[cont + 4, 0] = (6*x1 + 4*x2 + 2*x3)/12 ; mp_coord[cont + 4, 1] = (6*y1 + 4*y2 + 2*y3)/12
                    mp_elem[cont + 5, 0] = i + 1 # MP seis del elemento
                    mp_coord[cont + 5, 0] = (2*x1 + 8*x2 + 2*x3)/12 ; mp_coord[cont + 5, 1] = (2*y1 + 8*y2 + 2*y3)/12
                    mp_elem[cont + 6, 0] = i + 1 # MP siete del elemento
                    mp_coord[cont + 6, 0] = (6*x1 + 2*x2 + 4*x3)/12 ; mp_coord[cont + 6, 1] = (6*y1 + 2*y2 + 4*y3)/12
                    mp_elem[cont + 7, 0] = i + 1 # MP ocho del elemento
                    mp_coord[cont + 7, 0] = (2*x1 + 6*x2 + 4*x3)/12 ; mp_coord[cont + 7, 1] = (2*y1 + 6*y2 + 4*y3)/12
                    mp_elem[cont + 8, 0] = i + 1 # MP nueve del elemento
                    mp_coord[cont + 8, 0] = (5*x1 + x2 + 6*x3)/12 ; mp_coord[cont + 8, 1] = (5*y1 + y2 + 6*y3)/12
                    mp_elem[cont + 9, 0] = i + 1 # MP diez del elemento
                    mp_coord[cont + 9, 0] = (2*x1 + 4*x2 + 6*x3)/12 ; mp_coord[cont + 9, 1] = (2*y1 + 4*y2 + 6*y3)/12
                    mp_elem[cont + 10, 0] = i + 1 # MP once del elemento
                    mp_coord[cont + 10, 0] = (2*x1 + 2*x2 + 8*x3)/12 ; mp_coord[cont + 10, 1] = (2*y1 + 2*y2 + 8*y3)/12
                    mp_elem[cont + 11, 0] = i + 1 # MP doce del elemento
                    mp_coord[cont + 11, 0] = (x1 + x2 + 10*x3)/12 ; mp_coord[cont + 11, 1] = (y1 + y2 + 10*y3)/12
                else: # elemento superior derecho
                    mp_elem[cont, 0] = i + 1 # MP uno del elemento
                    mp_coord[cont, 0] = (10*x1 + x2 + x3)/12 ; mp_coord[cont, 1] = (10*y1 + y2 + y3)/12
                    mp_elem[cont + 1, 0] = i + 1 # MP dos del elemento
                    mp_coord[cont + 1, 0] = (8*x1 + 2*x2 + 2*x3)/12 ; mp_coord[cont + 1, 1] = (8*y1 + 2*y2 + 2*y3)/12
                    mp_elem[cont + 2, 0] = i + 1 # MP tres del elemento
                    mp_coord[cont + 2, 0] = (6*x1 + 2*x2 + 4*x3)/12 ; mp_coord[cont + 2, 1] = (6*y1 + 2*y2 + 4*y3)/12
                    mp_elem[cont + 3, 0] = i + 1 # MP cuatro del elemento
                    mp_coord[cont + 3, 0] = (6*x1 + 5*x2 + x3)/12 ; mp_coord[cont + 3, 1] = (6*y1 + 5*y2 + y3)/12
                    mp_elem[cont + 4, 0] = i + 1 # MP cinco del elemento
                    mp_coord[cont + 4, 0] = (4*x1 + 2*x2 + 6*x3)/12 ; mp_coord[cont + 4, 1] = (4*y1 + 2*y2 + 6*y3)/12
                    mp_elem[cont + 5, 0] = i + 1 # MP seis del elemento
                    mp_coord[cont + 5, 0] = (4*x1 + 6*x2 + 2*x3)/12 ; mp_coord[cont + 5, 1] = (4*y1 + 6*y2 + 2*y3)/12
                    mp_elem[cont + 6, 0] = i + 1 # MP siete del elemento
                    mp_coord[cont + 6, 0] = (2*x1 + 2*x2 + 8*x3)/12 ; mp_coord[cont + 6, 1] = (2*y1 + 2*y2 + 8*y3)/12
                    mp_elem[cont + 7, 0] = i + 1 # MP ocho del elemento
                    mp_coord[cont + 7, 0] = (2*x1 + 6*x2 + 4*x3)/12 ; mp_coord[cont + 7, 1] = (2*y1 + 6*y2 + 4*y3)/12
                    mp_elem[cont + 8, 0] = i + 1 # MP nueve del elemento
                    mp_coord[cont + 8, 0] = (2*x1 + 9*x2 + x3)/12 ; mp_coord[cont + 8, 1] = (2*y1 + 9*y2 + y3)/12
                    mp_elem[cont + 9, 0] = i + 1 # MP diez del elemento
                    mp_coord[cont + 9, 0] = (x1 + x2 + 10*x3)/12 ; mp_coord[cont + 9, 1] = (y1 + y2 + 10*y3)/12
                    mp_elem[cont + 10, 0] = i + 1 # MP once del elemento
                    mp_coord[cont + 10, 0] = (x1 + 5*x2 + 6*x3)/12 ; mp_coord[cont + 10, 1] = (y1 + 5*y2 + 6*y3)/12
                    mp_elem[cont + 11, 0] = i + 1 # MP doce del elemento
                    mp_coord[cont + 11, 0] = (x1 + 9*x2 + 2*x3)/12 ; mp_coord[cont + 11, 1] = (y1 + 9*y2 + 2*y3)/12
                cont += 12
    
    mp_elem = mp_elem[:cont, :] # tomando solo las filas que se llenaron
    mp_coord = mp_coord[:cont , :] # tomando solo las filas que se llenaron
    active_elem = np.unique(mp_elem[:, 0]) # tomando la lista de elementos activos
    return mp_elem, mp_coord, active_elem

# ====================================================
# =========== Funcion para inicialiar MP elemento cuadrilateral =============

def setup_MP(xi, yi, xf, yf, cor, inci, nmpe=1):
    """ Funcion para inicializar los MP en los elementos de la malla - RECTANGULAR BILINEAL
        (xi, yi) y (xf, yf) corresponde a las coordenadas iniciales y finales del continuo del problema 
        - el area RECTANGULAR donde se crearan los MP
        cor = es la matriz de coordenadas de los nodos de la malla de elementos
        inci = en la matriz de incidencias de la malla de elementos
        nmpe = es el numero de MP en el elemento - por defecto es igual a 1"""
    
    num = int(math.sqrt(nmpe))
    assert (min(cor[:,0])<= xi and min(cor[:,1])<= yi),"El punto (xi, yi) esta fuera del dominio de la malla de elementos"
    assert (max(cor[:,0])>= xf and max(cor[:,1])>= yf),"El punto (xf, yf) esta fuera del dominio de la malla de elementos"
    mp_elem = np.empty((len(inci)*num*num, 1)).astype(int)
    mp_coord = np.empty((len(inci)*num*num, 2))
    cont = 0 # contador para el numero de MP
    for i in range(len(inci)):
        # coordenadas de los nodos del elemento
        x1 = cor[inci[i, 0] - 1, 0] ; y1 = cor[inci[i, 0] - 1, 1]
        x2 = cor[inci[i, 1] - 1, 0] ; y2 = cor[inci[i, 1] - 1, 1]
        x3 = cor[inci[i, 2] - 1, 0] ; y3 = cor[inci[i, 2] - 1, 1]
        x4 = cor[inci[i, 3] - 1, 0] ; y4 = cor[inci[i, 3] - 1, 1]
        if (min(x1, x2, x3, x4) - xi) > -1e-12 and (min(y1, y2, y3, y4) - yi) > -1e-12 and (max(x1, x2, x3, x4) - xf) < 1e-12 and (max(y1, y2, y3, y4) - yf) <= 1e-12:
            # el elemento i se encuentra dentro del rango del continuo (xi, yi) - (xf, yf)
            
            # Calculo de las coordenadas naturales
            zai, eta = np.meshgrid(np.linspace(-(1-1/num),(1-1/num),num), np.linspace(-(1-1/num),(1-1/num),num))
            zai = zai.reshape(num**2)
            eta = eta.reshape(num**2)
            # Calculo de las funciones de forma
            N1 = 1/4 * (1 - zai) * (1 - eta)
            N2 = 1/4 * (1 + zai) * (1 - eta)
            N3 = 1/4 * (1 + zai) * (1 + eta)
            N4 = 1/4 * (1 - zai) * (1 + eta)
            # Guardando coordenadas y elemento correspondiente
            mp_elem[cont:(cont + num**2), 0] = i + 1
            mp_coord[cont:(cont + num**2), 0] = N1*x1 + N2*x2 + N3*x3 + N4*x4
            mp_coord[cont:(cont + num**2), 1] = N1*y1 + N2*y2 + N3*y3 + N4*y4
            cont += num**2
    
    mp_elem = mp_elem[:cont, :] 
    mp_coord = mp_coord[:cont , :] 
    active_elem = np.unique(mp_elem[:, 0]) # lista de elementos activos
    return mp_elem, mp_coord, active_elem

# ============================================================================
# === Funcion que inicializa MP - distribucion irregular
    
def setup_MP_irre(cdir, coord, incid, ele_size, nelex):
    """ Funcion para inicializar los MP mediante distribucción irregular en una malla de elementos finitos triangulares
        cdir = string con el directorio de trabajo
        coord = string con el nombre del archivo - coordendas de la malla
        incid = string con el nombre del archivo - matriz de incidencias
        ele_size = Tamano de los elementos malla Euleriana
        nelex = numero de ele en direccion X malla Euleriana"""
    
    # cargando informacion de la malla de elementos finitos
    coord = np.loadtxt(cdir + '/'+ coord +'.txt')
    incide = np.loadtxt(cdir + '/'+ incid +'.txt').astype(int)
    
    nmp = len(incide[:,0]) # numero de mp a crear 
    
    xp = np.zeros((nmp, 2))
    Vp = np.zeros(nmp)
    
    # ciclo en los elementos
    for i in range(len(incide[:,0])):
        nodes = incide[i,:] # nodos asociados al elem 1
        # coordenadas de los nodos
        x1, y1 = coord[nodes[0]-1, 0], coord[nodes[0]-1, 1]
        x2, y2 = coord[nodes[1]-1, 0], coord[nodes[1]-1, 1]
        x3, y3 = coord[nodes[2]-1, 0], coord[nodes[2]-1, 1]
        # area del elemento
        Vp[i] = 1/2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        # coordenadas particula
        xp[i,0] = 1/3 * (x1 + x2 + x3) - 0.2 # cambio de estas constantes 
        xp[i,1] = 1/3 * (y1 + y2 + y3) - 0.7
    
    mp_elem = np.zeros((nmp, 1)).astype(int)
    mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex) # incidencia particulas
    
    return xp, Vp, mp_elem, active_elem

# ============================================================
# ===== Funcion para buscar los elem donde estan los MP ======

def search_MP2(mp_elem, mp_coord, ele_size, nelex):
	""" Funcion para buscar en que elementos estan los MP - TRIANGULAR LINEAL
	 	mp_elm = vector con el elemento correspondiente de cada MP
	 	mp_coord = matriz de coordenadas de los MP
	 	ele_size = tamano de los elementos
	 	nelex = numero de elementos en la direccion x"""
	x = mp_coord[:, 0]
	y = mp_coord[:, 1]
	i = np.floor(x / ele_size)
	j = np.floor(y / ele_size)
	h = np.floor((y - j*ele_size) / (ele_size - x + i*ele_size))
	mp_elem[:, 0] = nelex*j + 2*i + 1 + np.ceil(h / (h + 1))
	active_elem = np.unique(mp_elem[:, 0]) # tomando la lista de elementos activos
	return mp_elem, active_elem


# ============================================================
# ===== Funcion para buscar los elem donde estan los MP  - Cuadrilateral bilineal ======

def search_MP(mp_elem, mp_coord, ele_size, nelex):
	""" Funcion para buscar en que elementos estan los MP - CUADRILATERAL BILINEAL
	 	mp_elm = vector con el elemento correspondiente de cada MP
	 	mp_coord = matriz de coordenadas de los MP
	 	ele_size = tamano de los elementos
	 	nelex = numero de elementos en la direccion x"""
	x = mp_coord[:, 0]
	y = mp_coord[:, 1]
	i = np.floor(x / ele_size)
	j = np.floor(y / ele_size)
	mp_elem[:, 0] = nelex*j + i + 1
	active_elem = np.unique(mp_elem[:, 0]) # tomando la lista de elementos activos
	return mp_elem, active_elem

# =============================================================
# ==== Funciones para buscar que MP esta en cada elem =========

@numba.njit
def elem_i_mp(mp_elem, active_elem):
    """ Funcion que determina que MP estan en el elemento i"""
    indx = [] # creando lista para los MP correspondientes del elemento i
    for j in range(len(mp_elem)):
        if mp_elem[j, 0] == active_elem:
            indx.append(j + 1) # creando lista con los MP correspondientes al elemento i
    return np.array(indx)


def incid_MP(mp_elem, active_elem):
    """ Funcion que determina que MP estan en cada elemento
    	mp_elm = vector con el elemento correspondiente de cada MP
    	active_elem = vector de elementos activos"""
    elem_mp = [elem_i_mp(mp_elem, active_elem[i]) for i in range(len(active_elem))]
    return elem_mp

#======================================================================
# ====== Funcion para calcular las fuerzas de traccion en las particulas ===

def traction_forces(xp, side, t, xi, xf):
    """Funcion para calcular las particulas que estan en el lado especificado, con el objetivo de
        aplicar fuerzas de superficie
        Argumentos:
                    xp = Array de coordenadas de las particulas
                    side = entero que indica el lado del continuo - 0 = Izquierdo - 1 = Derecho - 2 = Abajo - 3 = Arriba
                    t = carga en N/m
                    xi = coordenada inicial donde inicia la carga
                    xf = coordenada final donde termina la carga"""
    
    # comprobando datos ingresados
    assert (side == 0  or side == 1 or side == 2 or side == 3), "El argumento side debe ser un entero entre 0 y 3 - mirar descripcion de la funcion!"
    
    if side == 0: # lado izquierdo
        tp_parti = np.where(xp[:,0] == np.min(xp[:,0]))[0]
    elif side == 1: # lado derecho
        tp_parti = np.where(xp[:,0] == np.max(xp[:,0]))[0]
    elif side == 2: # lado inferior
        tp_parti = np.where(xp[:,1] == np.min(xp[:,1]))[0]
    elif side == 3: # Lado superior
        tp_parti = np.where((xp[:,1] == np.max(xp[:,1])) & (xp[:,0] >= xi) & (xp[:,0] <= xf))[0]
        
    
    ntp = len(tp_parti) # numero de particulas en la superficie frontera
    l = xf - xi # longitud donde se aplica la carga
    nmp = len(xp[:,0]) # numero total de particulas
    tp = np.zeros((nmp, 2)) # creando array con las fuerzas de traccion en las particulas
    
    if side == 0 or side == 1:
        tp[tp_parti, 0] = t * l / ntp # carga en x
    else:
        tp[tp_parti, 1] = t * l / ntp # carga en y
    
    return tp

# ===========================================================================
# ====== Funcion para obtener el array de particulas en la frontera ========

def boundary_particles(xp):
    """Funcion que devuelve un array con las particulas ubicadas en la frontera, solo valido para la distribucion inicial rectangular"""
    
    # obteniendo los arrays con las particulas de cada lado
    left = np.where(xp[:,0] == np.min(xp[:,0]))[0] + 1
    right = np.where(xp[:,0] == np.max(xp[:,0]))[0] + 1
    down = np.where(xp[:,1] == np.min(xp[:,1]))[0] + 1
    up = np.where(xp[:,1] == np.max(xp[:,1]))[0] + 1
    
    # concatenando y descartando los terminos que se repiten
    boundary_particles = np.unique(np.concatenate((left, right, up, down), axis=0))
    bound_value = np.zeros(len(xp)).astype(int)
    bound_value[boundary_particles - 1] = 1
    
    return boundary_particles, bound_value

# ============================================================================
    
# ====== Funcion para obtener el array de particulas en la frontera ========

def boundary_particles2(xp):
    """Funcion que devuelve un array con las particulas ubicadas en la frontera
        Valido para frontera superior inclinada - Talud """
    
    # obteniendo los arrays con las particulas de cada lado
    left = np.where(xp[:,0] == np.min(xp[:,0]))[0] + 1
    right = np.where(xp[:,0] == np.max(xp[:,0]))[0] + 1
    down = np.where(xp[:,1] == np.min(xp[:,1]))[0] + 1
    
    # array con los coordenas de x unicas
    xxp = np.unique(np.round(xp[:,0], 10))
    up = np.zeros(len(xxp)).astype(int)
    for i in range(len(xxp)):
        xi = xxp[i] # tomando primera coordenada
        idxi = np.where(np.absolute(xp[:,0] - xi) < 1e-10)[0] # id de mps con coordenada xi
        idymax = np.where(xp[idxi,1] == np.max(xp[idxi,1]))[0]
        if len(idymax) > 1:
            print("warning: dos particulas para el ymax, para un i=", i)
        up[i] = idxi[idymax] + 1
    
    # concatenando y descartando los terminos que se repiten
    boundary_particles = np.unique(np.concatenate((left, right, up, down), axis=0))
    bound_value = np.zeros(len(xp)).astype(int)
    bound_value[boundary_particles - 1] = 1
    
    return boundary_particles, bound_value

# ============================================================================