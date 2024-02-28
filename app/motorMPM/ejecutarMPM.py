# Importamos librerias y fuciones


from __future__ import division
from __future__ import print_function

import os
import numpy as np
import math
import time as tm
import  matplotlib.pyplot as plt
import json


from _func.mesh import create_uniform, contour_fixe, setup_MP,search_MP
from _func.mesh import traction_forces,boundary_particles
from _func.explicit2 import deltatime, particles_to_nodes, BC_Dirichlet_momentum
from _func.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel, nodes_to_particle_stress
from _func.graphics import graphic_button, graphic_video,graphic_gif
from _func import database


def ejecutar_MPM(objeto, ruta):
	cdir = os.getcwd()
	namescript = ruta
	namescript = os.path.basename(namescript)
	namescript = namescript[:len(namescript) - 5]

	
	#::::::::::::::::::::: Creamos malla::::::::::::::::::::::::
	t0 = tm.time()


	#
	#  aca debe leer de json la malla
	#

	'''
	dimx, dimy, ele_size = 4, 4, 0.2
	mesh= create_uniform(dimx,dimy,ele_size)
	'''
	lista_puntos = database.getDatatMalla_COORDENADAS_CONTORNO(objeto, ruta)	
	dimx = lista_puntos[2][0]
	dimy = lista_puntos[2][1]


	result = database.getDatatMalla(objeto, ruta)

	cor=np.asarray(result[0])
	
	ele_size = cor[1][0] - cor[0][0]
	print(ele_size)
	inci=np.asarray(result[1])
	nelex=np.asarray(result[2])


	nnodesx = int(nelex + 1)
	nnodesy = int(len(cor) / nnodesx)
	fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 1, 1, 0, 0)


	#:::::::::::::::::::: incializar puntos :::::::::::::::::::::::::

	#
	#  aca debe leer de json la particulas
	#

	'''
	xi, yi, xf, yf = 0, 2.6, 3.8, 3.4
	nmpe = 4 # nuemro de particulas por elemento
	mp_elem, xp, active_elem = setup_MP(xi, yi, xf, yf, cor, inci, nmpe)

	'''
	result = database.opeProject(objeto, ruta)
	datos = result[4]
	for nombre_material in datos:
		nmpe = datos[nombre_material]['nmpe']
		xi, yi, xf, yf = datos[nombre_material]['COORDENADAS_CONTORNO']
		mp_elem = np.asarray(datos[nombre_material]['mp_elem'])
		active_elem = np.asarray(datos[nombre_material]['active_elem'])
		xp = np.asarray(datos[nombre_material]['xp'])



	nmp = len(mp_elem) # nuemro total de particulas

	Vp = (ele_size**2) / nmpe*np.ones(nmp) # vector de volumenes
	Vp0 = (ele_size**2) / nmpe*np.ones(nmp) # vector de volumenes iniciales
	rhop = 2.0 * np.ones(nmp) # Mg/m3 vector de densisdades de las particulas 
	Mp = np.multiply(rhop, Vp) # vector de masas

	#:::::::::::::::::  propiedades de las particlas :::::::::::::::::::::::::
	#E,nu,C',Phi, psi
	#
	#  aca debe leer de json los parametros
	#

	'''

	'''
	Prop=np.zeros((nmp, 6))
	Prop[:,0] = 10e3 # modulo de eslasticidad KPa
	Prop[:,1] = 0.2 # Coeficiente de poisson
	Prop[:,2] = 5	# Cohesion KPa
	Prop[:,3] = 5 / 180*math.pi # Angulo de friccion 
	Prop[:,4] = 5 / 180*math.pi # Angulo de dilatancia



	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
	

	Fp = np.ones((nmp, 4))
	Fp[:,1:3] = 0
	sig = np.zeros((nmp, 4))
	epse = np.zeros((nmp, 3))
	epsp = np.zeros((nmp, 3))
	vp = np.zeros((nmp, 2))

	bp=np.zeros((nmp, 2))
	bp[:,1]=-9.81
	tp=np.zeros((nmp, 2))

	bound_ptcl, bound_val = boundary_particles(xp)

	time = 2

	dtime = deltatime(Prop[:,0], Prop[:,1], rhop, ele_size, 0.5)
	time = math.ceil(time / dtime) * dtime
	tiempo = np.arange(0, time, dtime)

	fps = 40


	if dtime < 1/fps:
		ndt = math.floor(1/fps/dtime)
		dtimegraphic = ndt*dtime
	else:
		dtimegraphic = dtime





	tiempographic = np.arange(0, time, dtimegraphic)


	corX = np.empty((nmp, len(tiempographic)+1))
	corY = np.empty((nmp, len(tiempographic)+1))
	sigxx = np.empty((nmp, len(tiempographic)+1))
	sigyy = np.empty((nmp, len(tiempographic)+1))
	sigxy = np.empty((nmp, len(tiempographic)+1))
	epsxx = np.empty((nmp, len(tiempographic)+1))
	epsyy = np.empty((nmp, len(tiempographic)+1))
	epsxy = np.empty((nmp, len(tiempographic)+1))

	corX[:,0], corY[:,0] = xp[:,0], xp[:,1]
	sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2]
	epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2]


	tgraphic = 0


	for t in range(len(tiempo)):
		mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)
		active_nodes = np.unique(inci[active_elem-1, :])

		grid = inci, cor, active_elem, active_nodes, mp_elem
		particle = xp, vp, Vp, Mp, sig, bp, tp
		nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
		nforce = niforce + neforce

		dampfac = 0.00
		ndamping = dampfac * (np.multiply(np.absolute(nforce),np.sign(nmomentum)))
		nforce = nforce + ndamping
		nmomentum += nforce*dtime

		nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX,fixed_nodesY, nmomentum, nforce,  niforce, neforce)

		nquantities = nmass, nmomentum, nforce
		particle= xp, vp, Vp, Mp, sig, shfnp
		xp, vp, nvel=nodes_to_particle_vel(grid, particle, nquantities, dtime)
		nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY,nvel)

		particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
		Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 0)


		if t==len(tiempo)-1:
			corX[:,-1],corY[:,-1]=xp[:,0],xp[:,1]
			sigxx[:,-1],sigyy[:,-1],sigxy[:,-1]=sig[:,0],sig[:,1],sig[:,2]
			epsxx[:,-1],epsyy[:,-1],epsxy[:,-1]=epse[:,0],epse[:,1],epse[:,2]


		elif abs(tiempo[t+1]-tiempographic[tgraphic+1])<1e-13:
			corX[:,tgraphic+1],corY[:,tgraphic+1]= xp[:,0],xp[:,1]
			sigxx[:,tgraphic+1],sigyy[:,tgraphic+1],sigxy[:,tgraphic+1]=sig[:,0],sig[:,1],sig[:,2]
			epsxx[:,tgraphic+1],epsyy[:,tgraphic+1],epsxy[:,tgraphic+1]=epse[:,0],epse[:,1],epse[:,2]
			if tgraphic != len(tiempographic)-2:
				tgraphic += 1

	tiempographic = np.append(tiempographic, tiempo[-1]+dtime)

	tf =tm.time()
	print("tiempo", tf- t0)





	graphic_button(corX, corY, sigxx, 4*Vp0[0],tiempographic, dimx, dimy)


	newfolder = cdir +'/graphics_'+ namescript
	if not os.path.exists(newfolder):
		os.mkdir(newfolder)



	graphic_gif(corX, corY, sigxx, 4*Vp0[0],tiempographic, dimx, dimy,newfolder)
	