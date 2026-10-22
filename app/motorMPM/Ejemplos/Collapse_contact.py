#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:54:30 2018

@author: David Leon Vanegas - deleonv@unal.edu.co

 === PROCEDIMIENTO GENERAL DE CALCULO  - METODO DEL PUNTO MATERIAL ===
 ==== COLAPSO DE COLUMNA GRANULAR CON CONTACTO EN LA BASE =======
"""

# === REALIZANDO LAS IMPORTACIONES NECESARIAS === 
from __future__ import division
from __future__ import print_function
#import time
import os
import numpy as np
import math
from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP, traction_forces, boundary_particles2
from mpm_un.mesh import create_uniform2, setup_MP2, search_MP2, node_conectivity
from mpm_un.explicit2 import deltatime, particles_to_nodes, particles_to_nodes_gauss, BC_Dirichlet_momentum, BC_Dirichlet_momentum2, particles_to_nodes_gauss2, contact
from mpm_un.explicit2 import nodes_to_particle_vel, BC_Dirichlet_vel, nodes_to_particle_stress, static_convergence, nodes_to_particle_stress_gauss, static_convergence2, BC_Dirichlet_momentum3
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
node_support = node_conectivity(inci, len(cor[:,0])) # conectividad de los nodos


# fijar en la posicion x=0.09
xBC = 0.09
nx = int(xBC / ele_size) + 1
idBC = np.linspace(nx ,(nnodesy - 1)*nnodesx + nx, nnodesy).astype(int)
# Nuevo array con id de nodos fijos en x
fixed_nodesX = np.unique(np.concatenate((fixed_nodesX, idBC), axis=0))


# ############### INICIALIZAR PARTICULAS - CUERPO 1  ##########################
xi, yi, xf, yf = 0, 0, 0.9, 0.02 # coordenas inicial y final del rectangulo que define el dominio
nmpe_1 = 1 # numero de MPs por elemento
# funcion setup_MP = obtiene elem asociado a cada mp, coordenadas mp y lista de elem activos
mp_elem_1, xp_1, active_elem_1 = setup_MP(xi, yi, xf, yf, cor, inci, nmpe_1)

# +++++ ACTUALIZAR CANTIDAES DE PARTICULAS =++++
active_nodes_1 = np.unique(inci[active_elem_1 - 1,:]) # lista de nodos activos

# ++++++ INICIAR CANTIDADES DE PARTICULAS ++++++++++
nmp_1 = len(mp_elem_1) # Numero de mp

Vp_1 = (ele_size ** 2) / nmpe_1 * np.ones(nmp_1) # vector de volumenes
Vp0_1 = (ele_size ** 2) / nmpe_1 * np.ones(nmp_1) # vector de volumenes iniciales
rhop_1 = 26 * np.ones(nmp_1) # en Mg/m3 - vector de densidades de las particulas
Mp_1 = np.multiply(rhop_1, Vp_1) # en Mg - vector de masas

# ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
Prop_1 = np.zeros((nmp_1,6)) 
Prop_1[:,0] = 8.5e3  # modulos de elasticidad en kPa
Prop_1[:,1] = 0.3 # coeficiente de poisson
Prop_1[:,2] = 34  # en kPa - cohesion
Prop_1[:,3] = 30/180*math.pi # 25 grados de angulo de friccion
Prop_1[:,4] = 30/180*math.pi # 5 grados de angulo de dilatancia

Fp_1 = np.ones((nmp_1, 4)) # Mat gradiente de deformacion
Fp_1[:, 1:3] = 0 # inicia como Mat identidad
sig_1 = np.zeros((nmp_1, 4)) # Mat esfuerzos
epse_1 = np.zeros((nmp_1, 3)) # Mat def elasticas
epsp_1 = np.zeros((nmp_1, 3)) # Mat def plasticas 
vp_1 = np.zeros((nmp_1, 2)) # Mat velocidd vx y vy
bp_1 = np.zeros((nmp_1, 2)) # Mat fuerzas de cuerpo bx y by
bp_1[:,1] = 0 #-9.81 # by = a la gravedad
tp_1 = np.zeros((nmp_1, 2)) # Mat fuerzas de superficie
#tp_1 = traction_forces(xp_1, 3, -10, xi, xf) # Fuerza sobre cara
#bound_ptcl_1, bound_val_1 = boundary_particles2(xp_1) # particulas frontera - integra gauss


# ==== ESTADO DE ESFUERZOS GEOSTATICO =========

# Definir un valor inicial de esfuerzo
k0 = Prop_1[:,1] / (1 - Prop_1[:,1]) # definicion elastica
#k0 = 1 - np.sin(Prop[:,3]) # definicion Jacky
ymax = [np.max(xp_1[np.where(xp_1[:,0] == xp_1[i,0])[0],1]) for i in range(nmp_1)] + ele_size / (2 * (nmpe_1)**(1/2))*np.ones(nmp_1)
sig_1[:,1] = -(ymax - xp_1[:,1]) * rhop_1[:] * 0 # 9.81 # esfuerzo en y
sig_1[:,0] = sig_1[:,1] * k0 # esfuerzo en x
sig_1[:,3] = sig_1[:,1] * k0 # esfuerzo en z

# ######################## FIN CUERPO 1 #######################################


# ############### INICIALIZAR PARTICULAS - CUERPO 2  ##########################
xi, yi, xf, yf = 0.0, 0.02, 0.09, 0.65  # coordenas inicial y final del rectangulo que define el dominio
nmpe_2 = 9 # numero de MPs por elemento
# funcion setup_MP = obtiene elem asociado a cada mp, coordenadas mp y lista de elem activos
mp_elem_2, xp_2, active_elem_2 = setup_MP(xi, yi, xf, yf, cor, inci, nmpe_2)

active_nodes_2 = np.unique(inci[active_elem_2 - 1,:]) # lista de nodos activos

# ++++++ INICIAR CANTIDADES DE PARTICULAS ++++++++++
nmp_2 = len(mp_elem_2) # Numero de mp

Vp_2 = (ele_size ** 2) / nmpe_2 * np.ones(nmp_2) # vector de volumenes
Vp0_2 = (ele_size ** 2) / nmpe_2 * np.ones(nmp_2) # vector de volumenes iniciales
rhop_2 = 2.6 * np.ones(nmp_2) # en Mg/m3 - vector de densidades de las particulas
Mp_2 = np.multiply(rhop_2, Vp_2) # en Mg - vector de masas

# ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
Prop_2 = np.zeros((nmp_2,6)) 
Prop_2[:,0] = 0.85e3  # modulos de elasticidad en kPa
Prop_2[:,1] = 0.3 # coeficiente de poisson
Prop_2[:,2] = 0.02  # en kPa - cohesion
Prop_2[:,3] = 30/180*math.pi # 25 grados de angulo de friccion
Prop_2[:,4] = 1/180*math.pi # 5 grados de angulo de dilatancia

Fp_2 = np.ones((nmp_2, 4)) # Mat gradiente de deformacion
Fp_2[:, 1:3] = 0 # inicia como Mat identidad
sig_2 = np.zeros((nmp_2, 4)) # Mat esfuerzos
epse_2 = np.zeros((nmp_2, 3)) # Mat def elasticas
epsp_2 = np.zeros((nmp_2, 3)) # Mat def plasticas 
vp_2 = np.zeros((nmp_2, 2)) # Mat velocidd vx y vy
bp_2 = np.zeros((nmp_2, 2)) # Mat fuerzas de cuerpo bx y by
bp_2[:,1] = -9.81  # by = a la gravedad

tp_2 = np.zeros((nmp_2, 2)) # Mat fuerzas de superficie
#tp_1 = traction_forces(xp_1, 3, -10, xi, xf) # Fuerza sobre cara
#bound_ptcl_2, bound_val_2 = boundary_particles2(xp_2) # particulas frontera - integra gauss

# ==== ESTADO DE ESFUERZOS GEOSTATICO INICIAL =========
# Definir un valor inicial de esfuerzo
k0 = Prop_2[:,1] / (1 - Prop_2[:,1]) # definicion elastica
#k0 = 1 - np.sin(Prop[:,3]) # definicion Jacky
ymax = [np.max(xp_2[np.where(xp_2[:,0] == xp_2[i,0])[0],1]) for i in range(nmp_2)] + ele_size / (2 * (nmpe_2)**(1/2))*np.ones(nmp_2)
sig_2[:,1] = -(ymax - xp_2[:,1]) * rhop_2[:] * 9.81 # esfuerzo en y
sig_2[:,0] = sig_2[:,1] * k0 # esfuerzo en x
sig_2[:,3] = sig_2[:,1] * k0 # esfuerzo en z

# ######################## FIN CUERPO 2 #######################################


###################    PROCEDIMIENTO SOLUCION     #########################

# calculo del delta de tiempo para convergencia
dtime_1 = deltatime(Prop_1[:,0], Prop_1[:,1], rhop_1, ele_size, 0.1)
dtime_2 = deltatime(Prop_2[:,0], Prop_2[:,1], rhop_2, ele_size, 0.1)
dtime = np.min([dtime_1, dtime_2]) # tomando el minio dt

# SIN PASO GEOSTATIC

# --- CICLO EN EL TIEMPO  - PROBLEMA DINAMICO DE COLAPSO---
# calculo del delta de tiempo para convergencia
time = 0.20
time = math.ceil(time / dtime)*dtime # recalculando time para ajustar con dtime
tiempo = np.arange(0, time, dtime)

# Retirar condicion de contorno en xBC
fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)

# array para graficar - maximo 20 cuadros por segundo
if dtime < 0.01:
    ndt = math.floor(0.01 / dtime)
    dtimegraphic = ndt*dtime
else:
    dtimegraphic = dtime
    
tiempographic = np.arange(0, time, dtimegraphic)

# ++++++++++ CREANDO ARRAYS PARA GRAFICAR ++++++++++++++++
# Arrays con las particulas de todo el sistema
nmp = nmp_1 + nmp_2 # numero de particulas del sistema
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
corX[:nmp_1,0], corY[:nmp_1,0] = xp_1[:,0], xp_1[:,1] # coordenadas cuerpo 1
corX[nmp_1:,0], corY[nmp_1:,0] = xp_2[:,0], xp_2[:,1] # coordenadas cuerpo 2
sigxx[:nmp_1,0], sigyy[:nmp_1,0], sigxy[:nmp_1,0] = sig_1[:,0], sig_1[:,1], sig_1[:,2] # esfuerzos cuerpo 1
sigxx[nmp_1:,0], sigyy[nmp_1:,0], sigxy[nmp_1:,0] = sig_2[:,0], sig_2[:,1], sig_2[:,2] # esfuerzos cuerpo 2
epsxx[:nmp_1,0], epsyy[:nmp_1,0], epsxy[:nmp_1,0] = epse_1[:,0], epse_1[:,1], epse_1[:,2] # defor elastica cuerpo 1
epsxx[nmp_1:,0], epsyy[nmp_1:,0], epsxy[nmp_1:,0] = epse_2[:,0], epse_2[:,1], epse_2[:,2] # defor elastica cuerpo 2
despl[:,0] = 0 # desplazamiento inicial
eqplas[:,0] = 0 # def plastica equivalente
velp[:,0] = 0

tgraphic = 0 # incializando contador de tiempo para graficas

print("Inicio solucion en el tiempo - abertura de compuertas")
for t in range(len(tiempo)):        
    # --- buscar elementos y nodos activos ---
    mp_elem_1, active_elem_1 = search_MP(mp_elem_1, xp_1, ele_size, nelex) # cuerpo 1
    mp_elem_2, active_elem_2 = search_MP(mp_elem_2, xp_2, ele_size, nelex) # cuerpo 1
    active_elem = np.unique(np.concatenate((active_elem_1, active_elem_2), axis=0)) # elem activos del sistema
    active_nodes_1 = np.unique(inci[active_elem_1 - 1,:]) # lista de nodos activos cuerpo 1
    active_nodes_2 = np.unique(inci[active_elem_2 - 1,:]) # lista de nodos activos cuerpo 2
    active_nodes = np.unique(inci[active_elem - 1,:]) # nodos activos del sistema
        
    # --- transferir de las particulas a los nodos CUERPO 1----
    grid_1 = inci, cor, active_elem, active_nodes, mp_elem_1 # creando lista de valores de la malla 
    particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, bp_1, tp_1 # creando lista de partiulas 
    nmass_1, nmomentum_1, niforce_1, neforce_1, shfnp_1 = particles_to_nodes(grid_1, particle_1)
    # --- transferir de las particulas a los nodos CUERPO 2----
    grid_2 = inci, cor, active_elem, active_nodes, mp_elem_2 # creando lista de valores de la malla 
    particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, bp_2, tp_2 # creando lista de partiulas 
    nmass_2, nmomentum_2, niforce_2, neforce_2, shfnp_2 = particles_to_nodes(grid_2, particle_2)
    
    # almacenar variables del tiempo t  - para recaluclar vector de fuerzas
    nmomentum_1t = np.copy(nmomentum_1) 
    nmomentum_2t = np.copy(nmomentum_2)
    
    dampfac = 0.04
    # --- Solucion sistema de ecuaciones nodales --- CUERPO 1----
    ndamping_1 = -dampfac*np.multiply(np.absolute(niforce_1 + neforce_1), np.sign(nmomentum_1))
    nforce_1 = niforce_1 + neforce_1 + ndamping_1
    nmomentum_1 += nforce_1*dtime
    # --- Solucion sistema de ecuaciones nodales --- CUERPO 2----
    ndamping_2 = -dampfac*np.multiply(np.absolute(niforce_2 + neforce_2), np.sign(nmomentum_2))
    nforce_2 = niforce_2 + neforce_2 + ndamping_2
    nmomentum_2 += nforce_2*dtime
    
    #   ###### CANTIDADES NODALES DEL SISTEMA ###########
    nmassS = nmass_1 + nmass_2
    niforceS = niforce_1 + niforce_2
    neforceS = neforce_1 + neforce_2
    nmomentumS = nmomentum_1 + nmomentum_2
    
    #  #### SOLUCION ALGORITMO DE CONTACTO ##########
    mu = 0.5 # coeficiente de friccion
    mesh = inci, cor, node_support, active_nodes
    body1 = nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1
    body2 = nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2
    nmomentum_1, nmomentum_2 = contact(body1, body2, nmassS, nmomentumS, mesh, dtime, mu)
    # correccion vector de fuerzas
    nforce_1 = 1 / dtime * (nmomentum_1 - nmomentum_1t)
    nforce_2 = 1 / dtime * (nmomentum_2 - nmomentum_2t)
       
    # --- Fijar nodos de Dirichlet
    nmomentum_1, nforce_1 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_1, nforce_1) # CUERPO 1
    nmomentum_2, nforce_2 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_2, nforce_2) # CUERPO 2
    
    # --- Transferir de los nodos a las particulas - vp y xp CUERPO 1---
    nquantities_1 = nmass_1, nmomentum_1, nforce_1 # creando lista de valores nodales
    particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, shfnp_1 # creando lista de particulas
    xp_1, vp_1, nvel_1 = nodes_to_particle_vel(grid_1, particle_1, nquantities_1, dtime)
    nvel_1 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_1) # fijar nodos de Dirichlet nvel
    # --- Transferir de los nodos a las particulas - vp y xp CUERPO 2---
    nquantities_2 = nmass_2, nmomentum_2, nforce_2 # creando lista de valores nodales
    particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, shfnp_2 # creando lista de particulas
    xp_2, vp_2, nvel_2 = nodes_to_particle_vel(grid_2, particle_2, nquantities_2, dtime)
    nvel_2 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_2) # fijar nodos de Dirichlet nvel
    
    # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion CUERPO 1 ---
    particle_1 = Fp_1, Vp_1, Vp0_1, epse_1, epsp_1, sig_1, shfnp_1, Prop_1
    Fp_1, Vp_1, epse_1, epsp_1, sig_1 = nodes_to_particle_stress(grid_1, particle_1, nvel_1, dtime, 0)
    # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion CUERPO 2 ---
    particle_2 = Fp_2, Vp_2, Vp0_2, epse_2, epsp_2, sig_2, shfnp_2, Prop_2
    Fp_2, Vp_2, epse_2, epsp_2, sig_2 = nodes_to_particle_stress(grid_2, particle_2, nvel_2, dtime, 0)
        
    # --- INFORMACION A GRAFICAR --
    if t == len(tiempo) - 1:
        # guarar info en la ultima posicion
        corX[:nmp_1,-1], corY[:nmp_1,-1] = xp_1[:,0], xp_1[:,1] # cuerpo 1
        corX[nmp_1:,-1], corY[nmp_1:,-1] = xp_2[:,0], xp_2[:,1] # cuerpo 2
        sigxx[:nmp_1,-1], sigyy[:nmp_1,-1], sigxy[:nmp_1,-1] = sig_1[:,0], sig_1[:,1], sig_1[:,2] # cuerpo 1
        sigxx[nmp_1:,-1], sigyy[nmp_1:,-1], sigxy[nmp_1:,-1] = sig_2[:,0], sig_2[:,1], sig_2[:,2] # cuerpo 2
        epsxx[:nmp_1,-1], epsyy[:nmp_1,-1], epsxy[:nmp_1,-1] = epse_1[:,0], epse_1[:,1], epse_1[:,2] # cuerpo 1
        epsxx[nmp_1:,-1], epsyy[nmp_1:,-1], epsxy[nmp_1:,-1] = epse_2[:,0], epse_2[:,1], epse_2[:,2] # cuerpo 2
        # calcular desplazamiento total
        despl[:,-1] = np.sqrt((corX[:,0] - corX[:,-1])**2 + (corY[:,0] - corY[:,-1])**2)
        # deformacion plastica equivalente
        eqplas[:nmp_1,-1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2) + 4/3*epsp_1[:,2]**2) # cuerpo 1
        eqplas[nmp_1:,-1] = np.sqrt(4/9*(epsp_2[:,0]**2 - epsp_2[:,0]*epsp_2[:,1] + epsp_2[:,1]**2) + 4/3*epsp_2[:,2]**2) # cuerpo 1
        # velocidad particulas
        velp[:nmp_1,-1] = np.sqrt(vp_1[:,0]**2 + vp_1[:,1]**2) # cuerpo 1
        velp[nmp_1:,-1] = np.sqrt(vp_2[:,0]**2 + vp_2[:,1]**2) # cuerpo 1
    
    elif abs(tiempo[t+1] - tiempographic[tgraphic + 1])<1e-13:
        # el tiempo t coincide con un tiempo del array tiempographic
        corX[:nmp_1,tgraphic + 1], corY[:nmp_1,tgraphic + 1] = xp_1[:,0], xp_1[:,1] # cuerpo 1
        corX[nmp_1:,tgraphic + 1], corY[nmp_1:,tgraphic + 1] = xp_2[:,0], xp_2[:,1] # cuerpo 2
        sigxx[:nmp_1,tgraphic + 1], sigyy[:nmp_1,tgraphic + 1], sigxy[:nmp_1,tgraphic + 1] = sig_1[:,0], sig_1[:,1], sig_1[:,2] # cuerpo 1
        sigxx[nmp_1:,tgraphic + 1], sigyy[nmp_1:,tgraphic + 1], sigxy[nmp_1:,tgraphic + 1] = sig_2[:,0], sig_2[:,1], sig_2[:,2] # cuerpo 2
        epsxx[:nmp_1,tgraphic + 1], epsyy[:nmp_1,tgraphic + 1], epsxy[:nmp_1,tgraphic + 1] = epse_1[:,0], epse_1[:,1], epse_1[:,2] # cuerpo 1
        epsxx[nmp_1:,tgraphic + 1], epsyy[nmp_1:,tgraphic + 1], epsxy[nmp_1:,tgraphic + 1] = epse_2[:,0], epse_2[:,1], epse_2[:,2] # cuerpo 2
        # calcular desplazamiento total
        despl[:,tgraphic + 1] = np.sqrt((corX[:,0] - corX[:,tgraphic + 1])**2 + (corY[:,0] - corY[:,tgraphic + 1])**2)
        # deformacion plastica equivalente
        eqplas[:nmp_1,tgraphic + 1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2) + 4/3*epsp_1[:,2]**2) # cuerpo 1
        eqplas[nmp_1:,tgraphic + 1] = np.sqrt(4/9*(epsp_2[:,0]**2 - epsp_2[:,0]*epsp_2[:,1] + epsp_2[:,1]**2) + 4/3*epsp_2[:,2]**2) # cuerpo 1
        # velocidad particulas
        velp[:nmp_1,tgraphic + 1] = np.sqrt(vp_1[:,0]**2 + vp_1[:,1]**2) # cuerpo 1
        velp[nmp_1:,tgraphic + 1] = np.sqrt(vp_2[:,0]**2 + vp_2[:,1]**2) # cuerpo 1
        
        if tgraphic != len(tiempographic) - 2:
            tgraphic +=1
       
# -- FIN CICLO DE TIEMPO --
# Por fuera del ciclo del tiempo se tiene los arrays con la informacion a graficar

tiempographic = np.append(tiempographic, tiempo[-1] + dtime) # array con los pasos de tiempo

# ====== GRAFICAR RESULTADOS =======

# ====== GRAFICAR RESULTADOS =======

#graphic_button(corX, corY, sigyy, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy)

# === CREAR GIF CON LOS RESULTADOS ====
# creando carpeta para guardar los archivos gif
newfolder = cdir + '/graphics_' + namescript
if not os.path.exists(newfolder):
    os.mkdir(newfolder)

#graphic_gif(corX, corY, despl, Vp0[0]*(12/dimy)**2, tiempographic, dimx, dimy, newfolder)
graphic_button(corX, corY, eqplas, Vp0_2[0]*(12/dimy)**2, tiempographic, dimx, dimy)
graphic_button2(corX, corY, corY, Vp0_2[0]*(12/dimy)**2, tiempographic, dimx, dimy)
graphic_video(corX, corY, corY, Vp0_2[0]*(12/dimy)**2, tiempographic, 0.8, 0.65, newfolder)

