"""

 === PROCEDIMIENTO GENERAL DE CALCULO  - METODO DEL PUNTO MATERIAL ===
 === VIGA EMPOTRADA GRAVEDAD INSTANTANEA ===
"""

# === REALIZANDO LAS IMPORTACIONES NECESARIAS === 
from __future__ import division
from __future__ import print_function
import os
import numpy as np
import math
import time as tm
from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP
from mpm_un.mesh import traction_forces, boundary_particles
from mpm_un.explicit2 import deltatime, particles_to_nodes, BC_Dirichlet_momentum
from mpm_un.explicit2 import nodes_to_particle_vel, BC_Dirichlet_vel, nodes_to_particle_stress
from mpm_un.graphics import graphic_button, graphic_video

def run():
    # === GUARDANDO LA DIRECCION Y NOMBRE DEL ARCHIVO ===
    cdir = os.getcwd()
    namescript = os.path.basename(__file__)
    namescript = namescript[:len(namescript) - 3]

    t0 = tm.time()
    # ===== CREAR MALLA DE ELEMENTOS FINITOS ========
    dimx, dimy, ele_size = 4, 4, 0.2
    mesh = create_uniform(dimx, dimy, ele_size)
    cor, inci, nelex = mesh
    nnodesx = int(nelex + 1)
    nnodesy = int(len(cor)/nnodesx)
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 1, 1, 0, 0)
    

    # ========== INICIALIZAR MPs =============
    xi, yi, xf, yf = 0, 2.6, 3.8, 3.4# coordenas inicial y final del rectangulo que define el dominio
    nmpe = 4 # numero de MPs por elemento
    mp_elem, xp, active_elem = setup_MP(xi, yi, xf, yf, cor, inci, nmpe)
    nmp = len(mp_elem) # Numero total de particulas
    '''
    print("mp_elem: ", mp_elem)
    print("xp: ", xp)
    print("active_elem: ", active_elem)
    print("nmp: ", nmp)
    '''
    
    

    Vp = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes
    Vp0 = (ele_size ** 2) / nmpe * np.ones(nmp) # vector de volumenes iniciales
    rhop = 2.0 * np.ones(nmp) # vector de densidades de las particulas
    Mp = np.multiply(rhop, Vp) # vector de masas

    # ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
    Prop = np.zeros((nmp,6)) 
    Prop[:,0] = 10e3  # modulos de elasticidad en kPa
    Prop[:,1] = 0.2 # coeficiente de poisson
    Prop[:,2] = 5  # en kPa - cohesion
    Prop[:,3] = 5/180*math.pi # 25 grados de angulo de friccion
    Prop[:,4] = 5/180*math.pi # 5 grados de angulo de dilatancia




    Fp = np.ones((nmp, 4)) # Matriz gradiente de deformacion
    Fp[:, 1:3] = 0
    sig = np.zeros((nmp, 4)) # Matriz de esfuerzos
    epse = np.zeros((nmp, 3)) # Matriz de deformaciones elasticas
    epsp = np.zeros((nmp, 3)) # Matriz de deformaciones plasticas
    vp = np.zeros((nmp, 2)) # Matriz de velocidades
    bp = np.zeros((nmp, 2)) # Matriz de fuerzas de cuerpo
    bp[:,1] = -9.81  # la fuerza de cuerbo by es igual a la gravedad
    tp = np.zeros((nmp, 2)) # Matriz de fuerzas de traccion en la frontera
    #tp = traction_forces(xp, 3, 0e3, xi, xf)

    # si se va a emplear integracion gaussiana - obtener array con particulas de la frontera
    bound_ptcl, bound_val = boundary_particles(xp)

    # ============ PROCEDIMIENTO SOLUCION ===============
    # --- CICLO EN EL TIEMPO ---
    time = 4 # tiempo de simulación segundos

    dtime = deltatime(Prop[:,0], Prop[:,1], rhop, ele_size, 0.5) # Dt para convergencia
    time = math.ceil(time / dtime)*dtime # recalculando time para ajustar con dtime
    tiempo = np.arange(0, time, dtime)

    # array para graficar
    fps = 40 # numero max de cuadros por segundo
    if dtime < 1/fps:
        ndt = math.floor(1/fps/ dtime)
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

    # Guardando valores iniciales
    corX[:,0], corY[:,0] = xp[:,0], xp[:,1] # coordenadas de las particulas
    sigxx[:,0], sigyy[:,0], sigxy[:,0] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
    epsxx[:,0], epsyy[:,0], epsxy[:,0] = epse[:,0], epse[:,1], epse[:,2] # deformaciones

    tgraphic = 0 # incializando contador de tiempo para graficas
    for t in range(len(tiempo)):
        
        # --- buscar elementos y nodos activos ---
        mp_elem, active_elem = search_MP(mp_elem, xp, ele_size, nelex)        
        active_nodes = np.unique(inci[active_elem - 1,:])
        
        # --- transferir de las particulas a los nodos ----
        grid = inci, cor, active_elem, active_nodes, mp_elem # lista info de la malla
        particle = xp, vp, Vp, Mp, sig, bp, tp # lista info de particulas 
        nmass, nmomentum, niforce, neforce, shfnp = particles_to_nodes(grid, particle)
        nforce = niforce + neforce
        
        
        
        
        
        # --- Solucion sistema de ecuaciones nodales
        dampfac = 0.00 # coeficiente de amortiguamiento
        ndamping = -dampfac*(np.multiply(np.absolute(nforce), np.sign(nmomentum)))
        nforce = nforce + ndamping
        nmomentum += nforce*dtime 
        
        # --- Fijar nodos de Dirichlet ---
        nmomentum, nforce, niforce, neforce = BC_Dirichlet_momentum(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum, nforce, niforce, neforce)
        
        # --- Transferir de los nodos a las particulas - velocidad y posicion ---
        nquantities = nmass, nmomentum, nforce # lista info de valores nodales
        particle = xp, vp, Vp, Mp, sig, shfnp # lista info de particulas
        xp, vp, nvel = nodes_to_particle_vel(grid, particle, nquantities, dtime)
        nvel = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel) # fijar nodos de Dirichlet 
        
        # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion ---
        particle = Fp, Vp, Vp0, epse, epsp, sig, shfnp, Prop
        Fp, Vp, epse, epsp, sig = nodes_to_particle_stress(grid, particle, nvel, dtime, 0)
        
        # --- Guardando informacion a graficar --
        if t == len(tiempo) - 1:
            # guarar info en la ultima posicion
            corX[:,-1], corY[:,-1] = xp[:,0], xp[:,1] # coordenadas de las particulas
            sigxx[:,-1], sigyy[:,-1], sigxy[:,-1] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
            epsxx[:,-1], epsyy[:,-1], epsxy[:,-1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
        
        elif abs(tiempo[t+1] - tiempographic[tgraphic + 1])<1e-13:
            # el tiempo t coincide con un tiempo del array tiempographic
            corX[:,tgraphic + 1], corY[:,tgraphic + 1] = xp[:,0], xp[:,1] # coordenadas de las particulas
            sigxx[:,tgraphic + 1], sigyy[:,tgraphic + 1], sigxy[:,tgraphic + 1] = sig[:,0], sig[:,1], sig[:,2] # esfuerzos
            epsxx[:,tgraphic + 1], epsyy[:,tgraphic + 1], epsxy[:,tgraphic + 1] = epse[:,0], epse[:,1], epse[:,2] # deformaciones
            if tgraphic != len(tiempographic) - 2:
                tgraphic +=1

            
    # -- FIN CICLO DE TIEMPO --

    tiempographic = np.append(tiempographic, tiempo[-1] + dtime) # array con los pasos de tiempo

    tf = tm.time()
    print("Tiempo de simulacion = ", tf - t0)

    # ====== GRAFICAR RESULTADOS =======
    graphic_button(corX, corY, sigxx, 4*Vp0[0], tiempographic, dimx, dimy)

    #guardar resultados en archivo txt los array corX, corY, sigxx
    i = 0
    for x in corX:
        if x[0] == 3.75:
            print(f"y: {corY[i][0]}")
            if corY[i][0] == 2.65:
                print(f"i: {i}")
                np.savetxt(cdir + '/graphics_' + namescript + '/tiempo' + str(i) + '.txt', tiempographic)
                np.savetxt(cdir + '/graphics_' + namescript + '/corX_' + str(i) + '.txt', x)
                np.savetxt(cdir + '/graphics_' + namescript + '/corY_' + str(i) + '.txt', corY[i])
                np.savetxt(cdir + '/graphics_' + namescript + '/sigxx_' + str(i) + '.txt', sigxx[i])        
                break
                '''
                '''
        i += 1
    '''
    np.savetxt(cdir + '/graphics_' + namescript + '/corX.txt', corX)
    np.savetxt(cdir + '/graphics_' + namescript + '/corY.txt', corY)
    np.savetxt(cdir + '/graphics_' + namescript + '/sigxx.txt', sigxx)
    '''



    # === CREAR GIF CON LOS RESULTADOS ====
    # creando carpeta para guardar los archivos gif
    newfolder = cdir + '/graphics_' + namescript
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)

    #graphic_gif(corX, corY, sigxx, 4*Vp0[0], tiempographic, dimx, dimy, newfolder)
    graphic_video(corX, corY, sigxx, 4*Vp0[0], tiempographic, dimx, dimy, newfolder)
        

run()
print("=== PROGRAMA FINALIZADO ===")
    