#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 09:54:30 2018

@author: David Leon Vanegas - deleonv@unal.edu.co

 === PROCEDIMIENTO GENERAL DE CALCULO  - METODO DEL PUNTO MATERIAL ===
 == CAPACIDAD PORTANTE DE UN CIMIENTO CORRIDO EN SUELO TRESCA ==
"""

# === REALIZANDO LAS IMPORTACIONES NECESARIAS === 
from __future__ import division
from __future__ import print_function
import time
import os
import numpy as np
import math
from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP, traction_forces, boundary_particles
from mpm_un.mesh import create_uniform2, setup_MP2, search_MP2
from mpm_un.explicit2 import deltatime, particles_to_nodes, particles_to_nodes_gauss, BC_Dirichlet_momentum, particles_to_nodes_gauss2
from mpm_un.explicit2 import nodes_to_particle_vel, BC_Dirichlet_vel, nodes_to_particle_stress, static_convergence, nodes_to_particle_stress_gauss
from mpm_un.graphics import graphic_button, graphic_button2, graphic_gif, graphic_video

# === GUARDANDO LA DIRECCION Y NOMBRE DEL ARCHIVO ===
cdir = os.getcwd()
namescript = os.path.basename(__file__)
namescript = namescript[:len(namescript) - 3]

# ===== CREAR MALLA DE ELEMENTOS FINITOS ========
dimx, dimy, ele_size = 20, 15, 0.5
mesh = create_uniform(dimx, dimy, ele_size)
cor, inci, nelex = mesh
nnodesx = int(nelex + 1)
nnodesy = int(len(cor)/nnodesx)




fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)

# ========== INICIALIZAR MPs =============
xi, yi, xf, yf = 0, 0, 20, 10 # coordenas inicial y final del rectangulo que define el dominio
nmpe = 4 # numero de MPs por elemento
# funcion setup_MP = obtiene elem asociado a cada mp, coordenadas mp y lista de elem activos
mp_elem, xp, active_elem = setup_MP(xi, yi, xf, yf, cor, inci, nmpe)
nmp = len(mp_elem) # Numero de mp



Vp = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes
Vp0 = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes iniciales
rhop = 1.8 * np.ones(nmp) # en Mg/m3 - vector de densidades de las particulas
Mp = np.multiply(rhop, Vp) # en Mg - vector de masas

# ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
Prop = np.zeros((nmp,6)) 
Prop[:,0] = 10e3  # modulos de elasticidad en kPa
Prop[:,1] = 0.49 # coeficiente de poisson
Prop[:,2] = 20  # en kPa - cohesion
Prop[:,3] = 0/180*math.pi # 25 grados de angulo de friccion
Prop[:,4] = 0/180*math.pi # 5 grados de angulo de dilatancia





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
#→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→
#bp[:,1] = -9.81  # la fuerza de cuerbo by es igual a la gravedad
# Matriz de fuerzas de traccion en la frontera
tp0 = traction_forces(xp, 3, 1, 0, 5) # valor unitario
#→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→


# si se va a emplear integracion gaussiana - obtener array con particulas de la frontera
bound_ptcl, bound_val = boundary_particles(xp)


# ============ PROCEDIMIENTO SOLUCION ===============

# calculo del delta de tiempo para convergencia
dtime = deltatime(Prop[:,0], Prop[:,1], rhop, ele_size, 0.1)

# DEFINICION DE INCREMENTOS DE CARGA
dincre = -2 # en KN/m - valor de delta de incremento
nincre = 56 # numero de incrementos
charge = -np.linspace(0, dincre*nincre, nincre + 1) # array con los valores de carga de cada incremento

# Creando arrays para guardar info a graficar
corX = np.empty((nmp, nincre + 1))
corY = np.empty((nmp, nincre + 1))
sigxx = np.empty((nmp, nincre + 1))
sigyy = np.empty((nmp, nincre + 1))
sigxy = np.empty((nmp, nincre + 1))
epsxx = np.empty((nmp, nincre + 1))
epsyy = np.empty((nmp, nincre + 1))
epsxy = np.empty((nmp, nincre + 1))
despl = np.empty((nmp, nincre + 1))
eqplas = np.empty((nmp, nincre + 1)) # deformacion plastica equivalente

# Guardando valores iniciales
corX[:,0], corY[:,0] = xp[:,0], xp[:,1] # coordenadas de las particulas
sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
despl[:,0] = 0 # desplazamiento inicial
eqplas[:,0] = 0 # def plastica equivalente


# -- INICIO CICLO INCREMENTOS DE CARGA --
t0 = 0 # tiempo maximo por incremento
for i in range(nincre):
    tp = (i+1) * dincre * tp0 # haciendo el incremento de carga
    
    # inicializando parametros de convergencia
    ff = 1
    ee = 1
    nework = 0

    tcont = 0 # contador de interaciones
    # -- INCIAR CILO EN EL TIEMPO --
    tinicial = time.time()
    while (ff > 0.011) or (ee > 0.01):
        tcont += 1 #avanzando contador de tiempo
    
        # --- buscar elementos y nodos activos ---
        mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex) # buscar en que elem estan los MPs
        active_nodes = np.unique(inci[active_elem - 1,:]) # lista de nodos activos
            
        # --- transferir de las particulas a los nodos ----
        grid = inci, cor, active_elem, active_nodes, mp_elem # creando lista de valores de la malla
        particle = xp, vp, Vp, Mp, sig, bp, tp # creando lista de partiulas 
        #nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
        nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes_gauss2(grid, particle, bound_val) # habilitar si es integracion mixta
        nforce = niforce + neforce
            
        # --- Solucion sistema de ecuaciones nodales --- EXPLICITO!!
        dampfac = 0.75
        ndamping = -dampfac*np.multiply(np.absolute(nforce), np.sign(nmomentum))
        nforce = nforce + ndamping
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
        
        # --- Calcular parametros que determinar el equilibrio cuasi-estatico ---
        # Parametros tiempo anterior
        ff0 = ff
        ee0 = ee
        nework0 = nework 
        ff, ee, nework = static_convergence(nmass, niforce, neforce, nvel, dtime, nework0)
        
        # Condicion para que salga del ciclo si lleva mucho tiempo en la iteracion
        tiempoi = time.time() - tinicial
        if (tiempoi > 10*t0) and (i > 0):
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
    epsxx[:,i+1], epsyy[:,i+1], epsxy[:,i+1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
    # calcular desplazamiento total
    despl[:,i+1] = np.sqrt((corX[:,0] - corX[:,i+1])**2 + (corY[:,0] - corY[:,i+1])**2)
    # deformacion plastica equivalente
    eqplas[:,i+1] = np.sqrt(4/9*(epsp[:,0]**2 - epsp[:,0]*epsp[:,1] + epsp[:,1]**2) + 4/3*epsp[:,2]**2)
        
    if finfor == True:
        # se debe salir del ciclo for por que no se alcanzo equilibrio
        break
 
# -- FIN CICLO DE INCREMENTOS DE CARGA --
        
# tomar solo los array que se llenaron - HASTA EL VALOR QUE TENGA i
corX, corY = corX[:,:i+2], corY[:,:i+2]
sigxx, sigyy, sigxy = sigxx[:,:i+2], sigyy[:,:i+2], sigxy[:,:i+2]
epsxx, epsyy, epsxy = epsxx[:,:i+2], epsyy[:,:i+2], epsxy[:,:i+2]
eqplas = eqplas[:,:i+2]
charge = charge[:i+2]

# ====== GRAFICAR RESULTADOS =======

graphic_button2(corX, corY, sigyy, Vp0[0]*(12/dimy)**2, charge, dimx, dimy)
graphic_button(corX, corY, eqplas, Vp0[0]*(12/dimy)**2, charge, dimx, dimy)

# === CREAR GIF CON LOS RESULTADOS ====
# creando carpeta para guardar los archivos gif
newfolder = cdir + '/graphics_' + namescript
if not os.path.exists(newfolder):
    os.mkdir(newfolder)

#graphic_gif(corX, corY, despl, Vp0[0]*(12/dimy)**2, charge, dimx, dimy, newfolder)
#graphic_video(corX, corY, despl, Vp0[0]*(12/dimy)**2, charge, dimx, dimy, newfolder)


print("Desplazamiento en la parte superior: ", corY[-int((xf-xi)/ele_size/2)*nmpe,0] - corY[-int((xf-xi)/ele_size/2)*nmpe, -1])

print("Esfuerzo syy en la base: ", sigyy[int((xf-xi)/ele_size/2)*nmpe, -1])


# GRAFICA DE CARGA VS DESPLAZAMIENTO
import matplotlib.pyplot as plt

# tomar identicacion del nodo a calcular desplazamiento
idnodo = np.where((corX[:,0] == np.min(corX[:,0])) & (corY[:,0] == np.max(corY[:,0])))
des_nodo = corY[idnodo,0] - corY[idnodo,:]

fig, axes = plt.subplots()
axes.plot(des_nodo[0,:][0], charge, '-b', label="Sol. Numérica (MPM)")
axes.set(Title="Carga zapata vs desplazamiento - Tresca ($S_u = 20 kPa$)", ylabel="Carga en la zapata ($kPa$)", xlabel="Desplazamiento ($m$)")
axes.grid(True)
#axes.legend()
axes.plot()

#grafica de malla y particulas
mayorticksX = np.arange(0, dimx + ele_size, 2)
minorticksX = np.arange(0, dimx + ele_size, ele_size)
mayorticksY = np.arange(0, dimy + ele_size, 2)
minorticksY = np.arange(0, dimy + ele_size, ele_size)

s = (Vp0[0]*(12/dimy)**2) * 100
#c = corY[:,0] # graficar en color la posicion Y inicial
c = np.zeros(len(corY[:,0]))
fig, ax = plt.subplots(figsize=(8,6))
plt.subplots_adjust(bottom=0.15, right=0.90)
b0 = ax.scatter(corX[:, 0], corY[:, 0], s, c=c, vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
ax.set_xlabel('Coordenada $x$ (m)', fontsize=11)
ax.set_ylabel('Coordenada $y$ (m)', fontsize=11)
ax.set(xlim=(0, dimx), ylim=(0, dimy))
ax.set_xticks(mayorticksX)
ax.set_xticks(minorticksX, minor=True)
ax.set_yticks(mayorticksY)
ax.set_yticks(minorticksY, minor=True)
ax.grid(which='both')
ax.tick_params(labelsize=10)
ax.set_title('Configuración inicial', fontsize=12)
