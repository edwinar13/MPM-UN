#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:54:30 2018

@author: David Leon Vanegas - deleonv@unal.edu.co

 === PROCEDIMIENTO GENERAL DE CALCULO  - METODO DEL PUNTO MATERIAL ===
 ++++ EJERCICIO DE COLAPSO DE UNA COLUMANA GRANUAR +++
 ++++ De acuerdo con el aritulo de Solowski2013 +++
"""

# === REALIZANDO LAS IMPORTACIONES NECESARIAS === 
from __future__ import division
from __future__ import print_function
#import time
import os
import numpy as np
import math
from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP, traction_forces, boundary_particles2
from mpm_un.mesh import create_uniform2, setup_MP2, search_MP2
from mpm_un.explicit2 import deltatime, particles_to_nodes, particles_to_nodes_gauss, BC_Dirichlet_momentum, particles_to_nodes_gauss2
from mpm_un.explicit2 import nodes_to_particle_vel, BC_Dirichlet_vel, nodes_to_particle_stress, static_convergence, nodes_to_particle_stress_gauss, static_convergence2
from mpm_un.graphics import graphic_button, graphic_button2, graphic_gif, graphic_video

# === GUARDANDO LA DIRECCION Y NOMBRE DEL ARCHIVO ===
cdir = os.getcwd()
namescript = os.path.basename(__file__)
namescript = namescript[:len(namescript) - 3]

# ===== CREAR MALLA DE ELEMENTOS FINITOS ========
dimx, dimy, ele_size = 0.9, 0.7, 0.01
mesh = create_uniform(dimx, dimy, ele_size)
cor, inci, nelex = mesh
nnodesx = int(nelex + 1)
nnodesy = int(len(cor)/nnodesx)
fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)

# fijar en la posicion x=0.09
xBC = 0.09
nx = int(xBC / ele_size) + 1
idBC = np.linspace(nx ,(nnodesy - 1)*nnodesx + nx, nnodesy).astype(int)
# Nuevo array con id de nodos fijos en x
fixed_nodesX = np.unique(np.concatenate((fixed_nodesX, idBC), axis=0))

# ========== INICIALIZAR MPs =============
xi, yi, xf, yf = 0, 0, 0.09, 0.63 # coordenas inicial y final del rectangulo que define el dominio
nmpe = 9 # numero de MPs por elemento
# funcion setup_MP = obtiene elem asociado a cada mp, coordenadas mp y lista de elem activos
mp_elem, xp, active_elem = setup_MP(xi, yi, xf, yf, cor, inci, nmpe)

nmp = len(mp_elem) # Numero de mp

Vp = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes
Vp0 = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes iniciales
rhop = 2.6 * np.ones(nmp) # en Mg/m3 - vector de densidades de las particulas
Mp = np.multiply(rhop, Vp) # en Mg - vector de masas

# ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
Prop = np.zeros((nmp,6)) 
Prop[:,0] = 0.85e3  # modulos de elasticidad en kPa
Prop[:,1] = 0.3 # coeficiente de poisson
Prop[:,2] = 0.02  # en kPa - cohesion
Prop[:,3] = 30/180*math.pi # 25 grados de angulo de friccion
Prop[:,4] = 1/180*math.pi # 25 grados de angulo de dilatancia

# Matriz gradiente de deformacion
Fp = np.ones((nmp, 4))
Fp[:, 1:3] = 0 #  incia como matriz identidad
# Matriz de esfuerzos
sig = np.zeros((nmp, 4)) 
# Matriz de deformaciones
epse = np.zeros((nmp, 3)) # elasticas
epsp = np.zeros((nmp, 3)) # plasticas 
# Matriz de velocidades vx y vy
vp = np.zeros((nmp, 2))
vp[:,0] = 0
# Matriz de fuerzas de cuerpo bx y by
bp = np.zeros((nmp, 2))
bp[:,1] = -9.81  # la fuerza de cuerbo by es igual a la gravedad
# Matriz de fuerzas de traccion en la frontera
tp = np.zeros((nmp, 2))
#tp = traction_forces(xp, 3, -10, xi, xf)

# si se va a emplear integracion gaussiana - obtener array con particulas de la frontera
bound_ptcl, bound_val = boundary_particles2(xp)

###################    PROCEDIMIENTO SOLUCION     #########################

# calculo del delta de tiempo para convergencia
dtime = deltatime(Prop[:,0], Prop[:,1], rhop, ele_size, 0.7)

# ==== EQUILIBRIO GEOSTATICO =========

# Definir un valor inicial de esfuerzo
k0 = Prop[:,1] / (1 - Prop[:,1]) # definicion elastica
#k0 = 1 - np.sin(Prop[:,3]) # definicion Jacky
ymax = [np.max(xp[np.where(xp[:,0] == xp[i,0])[0],1]) for i in range(nmp)] + ele_size / (2 * (nmpe)**(1/2))*np.ones(nmp)
sig[:,1] = -(ymax - xp[:,1]) * rhop[:] * 9.81 # esfuerzo en y
sig[:,0] = sig[:,1] * k0 # esfuerzo en x
sig[:,3] = sig[:,1] * k0 # esfuerzo en z

# grafica de la distribucion inicial de esfuerzos
#import matplotlib.pyplot as plt
#fig, ax = plt.subplots()
#plt.subplots_adjust(bottom=0.10)
#ax.grid(True)
#ax.set(xlim=(0, dimx), ylim=(0, dimy))
#b = ax.scatter(xp[:,0], xp[:,1], 15, c=sig[:,1], vmin=np.min(sig[:,1]), vmax=np.max(sig[:,1]), cmap=plt.cm.jet)
#barra = fig.colorbar(b)

# --- CICLO EN EL TIEMPO ---
# inicializando parametros de convergencia
ff = 1
ee = 1
nework = 0

tcont = 0 # contador de interaciones
print("inicio paso geoestatico - iteracion")
while (ff > 0.011) or (ee > 0.01):
    tcont += 1
    # --- buscar elementos y nodos activos ---
    mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex) # buscar en que elem estan los MPs
    active_nodes = np.unique(inci[active_elem - 1,:]) # lista de nodos activos
        
    # --- transferir de las particulas a los nodos ----
    grid = inci, cor, active_elem, active_nodes, mp_elem # creando lista de valores de la malla
    particle = xp, vp, Vp, Mp, sig, bp, tp # creando lista de partiulas 
    #nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
    nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes_gauss2(grid, particle, bound_val) # habilitar si es integracion mixta
           
    # --- Solucion sistema de ecuaciones nodales --- EXPLICITO!!
    dampfac = 0.75
    nforce = niforce + neforce
    ndamping = -dampfac*np.multiply(np.absolute(nforce), np.sign(nmomentum))
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
    #Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 0)
    Fp, Vp, epse, epsp, sig = nodes_to_particle_stress_gauss(grid, particle, bound_val, nvel, dtime, 1)
    
    # --- Calcular parametros que determinar el equilibrio cuasi-estatico ---
    nework0 = nework
    ff, ee, nework = static_convergence(nmass, niforce, neforce, nvel, dtime, nework0)
            
# ==== FIN EQUILIBRIO GEOSTATICO ====
print("Fin paso geoestatico, numero de iteraciones = ", tcont)


# ============ PROCEDIMIENTO SOLUCION ===============

# Retirar condicion de contorno en xBC
fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)
# redefiniendo delta tiempo
dtime = deltatime(Prop[:,0], Prop[:,1], rhop, ele_size, 0.11)

# --- CICLO EN EL TIEMPO ---

# calculo del delta de tiempo para convergencia
time = 0.95
time = math.ceil(time / dtime)*dtime # recalculando time para ajustar con dtime
tiempo = np.arange(0, time, dtime)

ff = np.zeros(len(tiempo))
ee = np.zeros(len(tiempo))
efo = np.zeros(len(tiempo))
ifo = np.zeros(len(tiempo))
KE = np.zeros(len(tiempo))
nework = np.zeros(len(tiempo) + 1)
nework[0] = 0 # inicializar variable para el trabajo hecho por las fuerzas externas
velnodal = np.zeros(len(tiempo))
velnodal[0] = 0

# array para graficar - maximo 20 cuadros por segundo
if dtime < 0.01:
    ndt = math.floor(0.01 / dtime)
    dtimegraphic = ndt*dtime
else:
    dtimegraphic = dtime
    
tiempographic = np.arange(0, time, dtimegraphic)

# Creando arrays para guardar info a graficar
corX = np.empty((nmp, len(tiempographic) + 1))
corY = np.empty((nmp, len(tiempographic) + 1))
sigxx = np.empty((nmp, len(tiempographic) + 1))
sigyy = np.empty((nmp, len(tiempographic) + 1))
sigxy = np.empty((nmp, len(tiempographic) + 1))
epsxx = np.empty((nmp, len(tiempographic) + 1))
epsyy = np.empty((nmp, len(tiempographic) + 1))
epsxy = np.empty((nmp, len(tiempographic) + 1))
despl = np.empty((nmp, len(tiempographic) + 1))
eqplas = np.empty((nmp, len(tiempographic) + 1)) # def plast equivalente
velp = np.empty((nmp, len(tiempographic) + 1))

# Guardando valores iniciales
corX[:,0], corY[:,0] = xp[:,0], xp[:,1] # coordenadas de las particulas
sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
despl[:,0] = 0 # desplazamiento inicial
eqplas[:,0] = np.sqrt(4/9*(epsp[:,0]**2 - epsp[:,0]*epsp[:,1] + epsp[:,1]**2) + 4/3*epsp[:,2]**2) # def plastica equivalente
velp[:,0] = 0

tgraphic = 0 # incializando contador de tiempo para graficas
for t in range(len(tiempo)):
    if tiempo[t] > 0.5 and tiempo[t] < 0.5005:
        print("Simulacion paso los 0.5 segundos")
            
    # --- buscar elementos y nodos activos ---
    mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex) # buscar en que elem estan los MPs
    active_nodes = np.unique(inci[active_elem - 1,:]) # lista de nodos activos
        
    # --- transferir de las particulas a los nodos ----
    grid = inci, cor, active_elem, active_nodes, mp_elem # creando lista de valores de la malla
    particle = xp, vp, Vp, Mp, sig, bp, tp # creando lista de partiulas 
    nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
    #nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes_gauss2(grid, particle, bound_val) # habilitar si es integracion mixta
           
    # --- Solucion sistema de ecuaciones nodales --- EXPLICITO!!
    dampfac = 0.04
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
    Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 1)
    #Fp, Vp, epse, epsp, sig =  nodes_to_particle_stress_gauss(grid, particle, bound_val, nvel, dtime, 1)
    
    
    # --- Calcular parametros que determinar el equilibrio cuasi-estatico ---
    ff, ee, efo, ifo, KE, nework = static_convergence2(nmass, niforce, neforce, ndamping, nvel, dtime, nework, ff, ee, t, efo, ifo, KE)
    velnodal[t] = np.linalg.norm(nvel)
    
    # --- Guardando informacion a graficar --
    if t == len(tiempo) - 1:
        # guarar info en la ultima posicion
        corX[:,-1], corY[:,-1] = xp[:,0], xp[:,1] # coordenadas de las particulas
        sigxx[:,-1], sigyy[:,-1], sigxy[:,-1] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
        epsxx[:,-1], epsyy[:,-1], epsxy[:,-1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
        # calcular desplazamiento total
        despl[:,-1] = np.sqrt((corX[:,0] - corX[:,-1])**2 + (corY[:,0] - corY[:,-1])**2)
        # deformacion plastica equivalente
        eqplas[:,-1] = np.sqrt(4/9*(epsp[:,0]**2 - epsp[:,0]*epsp[:,1] + epsp[:,1]**2) + 4/3*epsp[:,2]**2)
        velp[:,-1] = np.sqrt(vp[:,0]**2 + vp[:,1]**2)
    
    elif abs(tiempo[t+1] - tiempographic[tgraphic + 1]) < 1e-13:
        # el tiempo t coincide con un tiempo del array tiempographic
        corX[:,tgraphic + 1], corY[:,tgraphic + 1] = xp[:,0], xp[:,1] # coordenadas de las particulas
        sigxx[:,tgraphic + 1], sigyy[:,tgraphic + 1], sigxy[:,tgraphic + 1] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
        epsxx[:,tgraphic + 1], epsyy[:,tgraphic + 1], epsxy[:,tgraphic + 1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
        # calcular desplazamiento total
        despl[:,tgraphic + 1] = np.sqrt((corX[:,0] - corX[:,tgraphic + 1])**2 + (corY[:,0] - corY[:,tgraphic + 1])**2)
        # deformacion plastica equivalente
        eqplas[:,tgraphic + 1] = np.sqrt(4/9*(epsp[:,0]**2 - epsp[:,0]*epsp[:,1] + epsp[:,1]**2) + 4/3*epsp[:,2]**2)
        velp[:,tgraphic + 1] = np.sqrt(vp[:,0]**2 + vp[:,1]**2)
    
        if tgraphic != len(tiempographic) - 2:
            tgraphic +=1
       
# -- FIN CICLO DE TIEMPO --
# Por fuera del ciclo del tiempo se tiene los arrays con la informacion a graficar

tiempographic = np.append(tiempographic, tiempo[-1] + dtime) # array con los pasos de tiempo

# ====== GRAFICAR RESULTADOS =======

#graphic_button(corX, corY, sigyy, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy)

# === CREAR GIF CON LOS RESULTADOS ====
# creando carpeta para guardar los archivos gif
newfolder = cdir + '/graphics_' + namescript
if not os.path.exists(newfolder):
    os.mkdir(newfolder)

#graphic_gif(corX, corY, despl, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy, newfolder)
graphic_button(corX, corY, eqplas, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy)
graphic_button2(corX, corY, corY, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy)
graphic_video(corX, corY, corY, Vp0[0]*(12/dimy)**2, tiempographic, 0.8, 0.65, newfolder)
