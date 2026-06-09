from __future__ import division
from __future__ import print_function
import os
import numpy as np
import time as tm
import math, pickle, dill
import matplotlib.pyplot as plt
from mpm_un.mesh import create_uniform, contour_fixe, setup_MP, search_MP, traction_forces, boundary_particles2
from mpm_un.mesh import create_uniform2, setup_MP2, search_MP2, node_conectivity
from mpm_un.explicit2 import deltatime, particles_to_nodes, particles_to_nodes_gauss, BC_Dirichlet_momentum, BC_Dirichlet_momentum2, particles_to_nodes_gauss2, contact
from mpm_un.explicit2 import nodes_to_particle_vel, BC_Dirichlet_vel, nodes_to_particle_stress, nodes_to_particle_stress2, static_convergence, nodes_to_particle_stress_gauss, static_convergence2, BC_Dirichlet_momentum3
from mpm_un.graphics import graphic_button, graphic_button2, graphic_button3, graphic_gif, graphic_video


def fase_geoestatica():
    t0 =tm.time()#tiempoinicial

    # rampaparaincrementodegravedad
    #grav =np.linspace(0.01,1,50)#100incrementosdecargaiguales
    #grav =np.array([0.01,0.03,0.06,0.10,0.15,0.21,0.29,0.39,0.50,0.62,0.75,0.87, 1.0])
    grav =np.array([0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])
    #grav =np.array([1.0])

    # ===GUARDANDOLADIRECCIONYNOMBREDELARCHIVO===
    cdir =os.getcwd()
    namescript =os.path.basename(__file__)
    namescript =namescript[:len(namescript)-3]


    # =====CREARMALLADEELEMENTOSFINITOS========
    dimx, dimy,ele_size=60,32,0.25
    mesh =create_uniform(dimx,dimy,ele_size)
    cor, inci,nelex=mesh
    nnodesx =int(nelex+1)
    nnodesy =int(len(cor)/nnodesx)
    fixed_nodesX, fixed_nodesY=contour_fixe(nnodesx,nnodesy,0,0,0,1)


    # ==========INICIALIZARMPs=============
    xi, yi, xf, yf = 0.0, 0.0, 60.0, 30.25
    nmpe = 4 #numerodeMPsporelemento
    # funcionsetup_MP=obtieneelementoasociadoacadamp,coordenadasmpylista de elementoactivos
    # Usamos yf=dimy para asegurar que tome elementos superiores si ele_size=1.0
    mp_elem, xp,active_elem=setup_MP(xi,yi,xf,yf,cor,inci,nmpe)


    # +++++++++TOMARDOMINIOINCLINADO-TALUD+++++++++
    x1, x2,y1=8,18,0.25
    idpa =np.zeros(len(xp[:,0])).astype(int)
    idcont =0
    for j in range(len(xp[:,0])):
        # FuncionPiecewiseparageometria
        if xp[j,0]<=x1:
            # primertramo
            idpa[idcont] =j
            idcont +=1
        elif xp[j,0]<=x2:
            # segundotramoinclinado
            ylim =(yf*x2-y1*x1)/(x2-x1)-(yf-y1)/(x2-x1)*xp[j,0]
            if xp[j,1]<=(ylim+1e-10):
                # estaparticulapermaneceeneldominio
                idpa[idcont] =j
                idcont +=1
        else:
            # tercertramo
            ylim =y1#tramorecto
            #ylim =(y1*xf)/(xf-x2)-(y1)/(xf-x2)*xp[j,0]#tramoinclinado
            if xp[j,1]<=ylim:
                # estaparticulasemantiene
                idpa[idcont] =j
                idcont +=1
                
    # indexararrayidpaparaelnumerodeparulasingresadas
    idpa =idpa[:idcont]#idpaesarrayconeliddelaspartculasqueestan dentro deldominio
    xp =xp[idpa,:]#indexandoarraydecoordenadasparalaspartculasdentrodeldominio
    mp_elem =mp_elem[idpa,:]
    np.savetxt("xp_coords.txt", xp, fmt="%.6f", header="x_coord y_coord")
    print("Coordenadas de las partículas guardadas en xp_coords.txt")


    # COPIADEPOSICIONINICIAL
    xp0 =np.copy(xp)

    # ++++Estratoinferior+++++
    idM1 =np.zeros(len(xp[:,0])).astype(int)
    idcontM1 =0
    for j in range(len(xp[:,0])):
        ylim =y1#estratorecto
        if xp[j,1]<=ylim:
            #Material bajoy1esmaterial1
            idM1[idcontM1] =j
            idcontM1 +=1
    idM1 =idM1[:idcontM1]
    # ++++++++FINDOMINIOINCLINADO+++++++

    # Identificar el material 2 (particulas que no pertenecen a M1)
    idM2 = np.setdiff1d(np.arange(len(xp[:,0])), idM1)

    #dibujar en matplotlib
    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    # Dibujar grupos con colores distintos
    ax.scatter(xp[idM1,0], xp[idM1,1], 0.5, c='r', label='Material 1 (Estrato inferior)')
    ax.scatter(xp[idM2,0], xp[idM2,1], 0.5, c='b', label='Material 2 (Estrato superior)')
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)
    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Distribucion inicial de particulas',fontsize=14)
    ax.legend(loc='upper right', fontsize=10)
    plt.show()

    nmp =len(mp_elem)#Numerodemp
    Vp =(ele_size**2)/nmpe*np.ones(nmp)#vectordevolumenes
    Vp0 =(ele_size**2)/nmpe*np.ones(nmp)#vectordevolumenesiniciales
    rhop =1.8*np.ones(nmp)#enMg/m3-vectordedensidadesdelaspartculas
    rhop[idM1] =2.6 # 
    Mp =np.multiply(rhop,Vp)#enMg-vectordemasas

    # ARRAYCONLASPROPIEDADESDELASPARTICULAS-E,nu,C',phi',psi'
    Prop =np.zeros((nmp,6))
    Prop[:,0] =15e3#modulosdeelasticidadenkPa
    Prop[:,1] =0.3#coeficientedePoisson
    Prop[:,2] =5#enkPa-cohesion
    Prop[idM1,2] =200#CohesionparaM1
    Prop[:,3] =35/180*math.pi#35gradosdeangulodefriccion
    Prop[:,4] =35/180*math.pi#35gradosdeangulodedilatancia

    # Matrizgradientededeformacion
    Fp =np.ones((nmp,4))
    Fp[:, 1:3]=0#inciacomomatrizidentidad
    # Matrizdeesfuerzos
    sig =np.zeros((nmp,4))
    # Matrizdedeformaciones
    epse =np.zeros((nmp,3))#elasticas
    epsp =np.zeros((nmp,3))#plasticas
    # Matrizdevelocidadesvxyvy
    vp =np.zeros((nmp,2))
    vp[:,0] =0
    # Matrizdefuerzasdecuerpobxyby
    bp =np.zeros((nmp,2))
    bp[:,1] =-9.81*grav[0]#lafuerzadecuerbobyesigualalagravedad
    # Matrizdefuerzasdetraccionenlafrontera
    tp =np.zeros((nmp,2))
    #tp =traction_forces(xp,3,-10,xi,xf)


    # sisevaaemplearintegraciongaussiana-obtenerarrayconpartculasdelafrontera
    bound_ptcl, bound_val=boundary_particles2(xp)

    ################### PROCEDIMIENTOSOLUCION #########################
    # calculodeldeltadetiempoparaconvergencia
    dtime =deltatime(Prop[:,0],Prop[:,1],rhop,ele_size,0.6)
    print("dtime=",dtime)
    

    # ====ESTADODEESFUEROSDEPRUEBA=========
    # Definirunvalorinicialdeesfuerzo
    #k0 =Prop[:,1]/(1-Prop[:,1])#definicionelastica
    #k0 =1-np.sin(Prop[:,3])#definicionJacky
    #ymax =[np.max(xp[np.where(xp[:,0]==xp[i,0])[0],1]) for i in range(nmp)]+ele_size/(2*(nmpe)**(1/2))*np.ones(nmp)
    #sig[:,1] =-(ymax-xp[:,1])*rhop[:]*9.81#esfuerzoeny
    #sig[:,0] =sig[:,1]*k0#esfuerzoenx
    #sig[:,3] =sig[:,1]*k0#esfuerzoenz

    # cicloparaincrementodecarga
    print("inicio pasogeoestatico-incrementosdecarga")
    for j in range(len(grav)):
        
        # incrementarlagravedad
        tgrav =tm.time()
        bp[:,1] =-9.81*grav[j]#incrementodegravedadcorrespondiente
        print("Valor degravedaddelpaso=",bp[0,1])
        # ---CICLOENELTIEMPO---
        # inicializandoparametrosdeconvergencia
        ff =1
        ee =1
        nework =0
        tcont =0#contadordeinteraciones
        while (ff>0.01)or(ee>0.01):

            tcont +=1
            if tcont % 100 == 0:
                print("----- Iteracion=",tcont,"ff=",ff,"ee=",ee)
            #print("Iteracion=",tcont,"ff=",ff,"ee=",ee)
            # ---buscarelementosynodosactivos---
            mp_elem, active_elem=search_MP(mp_elem,xp,ele_size,nelex)#buscar         en queelementoestanlosMPs
            active_nodes =np.unique(inci[active_elem-1,:])#listadenodosactivos

            # ---transferirdelaspartculasalosnodos----
            grid =inci,cor,active_elem,active_nodes,mp_elem#creandolistade        valores delamalla
            particle =xp,vp,Vp,Mp,sig,bp,tp#creandolistadepartiulas
            #nmass, nmomentum,niforce,neforce,shfnp=particles_to_nodes(grid,particle)
            nmass, nmomentum,niforce,neforce,shfnp=particles_to_nodes_gauss2(grid,
            particle, bound_val)#habilitarsiesintegracionmixta

            # ---Solucionsistemadeecuacionesnodales---EXPLICITO
            dampfac =0.75
            nforce =niforce+neforce
            ndamping =-dampfac*np.multiply(np.absolute(nforce),np.sign(nmomentum))
            nforce =niforce+neforce+ndamping
            nmomentum +=nforce*dtime

            # ---FijarnodosdeDirichlet---
            nmomentum, nforce,niforce,neforce=BC_Dirichlet_momentum(active_nodes,
            fixed_nodesX, fixed_nodesY,nmomentum,nforce,niforce,neforce)

            # ---Transferirdelosnodosalasparticulas-velocidadyposicion---
            nquantities =nmass,nmomentum,nforce#creandolistadevaloresnodales
            particle =xp,vp,Vp,Mp,sig,shfnp#creandolistadeparticulas

            #with open("result_iteracion.txt", "a") as f:
                #f.write(str(grid) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(particle) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(nquantities) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(dtime) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(active_nodes) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(fixed_nodesX) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(fixed_nodesY) + "\n")
                #f.write( "---------------------------------\n")
                #f.write(str(nvel) + "\n")
                #f.write( "---------------------------------\n")

            xp, vp,nvel=nodes_to_particle_vel(grid,particle,nquantities,dtime)
            nvel =BC_Dirichlet_vel(active_nodes,fixed_nodesX,fixed_nodesY,nvel)#fijar        nodos deDirichletnvel

            
            # ---Transferirdelosnodosalasparticulas-Esfuerzoydeformacion---
            particle =Fp,Vp,Vp0,epse,epsp,sig,shfnp,Prop
            #Fp, Vp,epse,epsp,sig=nodes_to_particle_stress(grid,particle,nvel, dtime,0)

            '''
            with open("result_iteracion.txt", "a") as f:
                f.write(str(grid) + "\n")
                f.write(str(particle) + "\n")
                f.write(str(bound_val) + "\n")
                f.write(str(nvel) + "\n")
                f.write(str(dtime) + "\n")
                f.write( "---------------------------------\n")
            '''

            Fp, Vp,epse,epsp,sig=nodes_to_particle_stress_gauss(grid,particle,
            bound_val,
            nvel, dtime,0)
            #print("dtime",dtime)
            #print("sig max x",np.max(sig[:,0]))

            
            # ---Calcularparametrosquedeterminarelequilibriocuasi-estatico---
            nework0 =nework
            ff, ee,nework=static_convergence(nmass,niforce,neforce,nvel,dtime,nework0)
            if tcont == 1:
                pass
                #a= 5/0
        # ====FINPASOEQUILIBRIOGEOSTATICO====
        tgravf =tm.time()
        tejecuciong =tgravf-tgrav
        print("Fin incrementogeoestatico",j+1,"Porcentajegravedad=",grav[j])
        print("Numero deiteraciones=",tcont,"Tiempodeejecucion=",tejecuciong)
        print("ff =",ff,"/ee=",ee)
        print()
        
    # ====FINEQUILIBRIOGEOSTATICOTODOSLOSINCREMENTOS====
    tf =tm.time()
    tejecucion =tf-t0
    print("FIN PASOGEOSTATICO")
    print("Tiempo deejecuciontotal=",tejecucion)
    # Calculodedesplazamientoenpasogeoestatic
    despl =np.sqrt((xp[:,0]-xp0[:,0])**2+(xp[:,1]-xp0[:,1])**2)
    
    # graficadeladistribucioninicialdeesfuerzos
    props =dict(boxstyle='round',facecolor='white',alpha=1.0)#propiedadestextframe
    syymax =np.max(sig[:,1])
    print("syymax=",syymax)
    tmax ='max='+str(np.round(syymax,2))
    idmax =np.where(sig[:,1]==syymax)[0][0]
    syymin =np.min(sig[:,1])
    tmin ='min='+str(np.round(syymin,2))
    idmin =np.where(sig[:,1]==syymin)[0][0]
    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    b =ax.scatter(xp[:,0],xp[:,1],15,c=sig[:,1],vmin=np.min(sig[:,1]),
    vmax=np.max(sig[:,1]), cmap=plt.cm.jet_r)
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)

    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Estado deesfuerzosgeostatico',fontsize=14)
    ax.text(xp[idmax,0], xp[idmax,1],tmax,fontsize=9,verticalalignment='center',
    bbox=props)
    ax.text(xp[idmin,0], xp[idmin,1],tmin,fontsize=9,verticalalignment='center',
    bbox=props)
    barra =fig.colorbar(b)
    barra.ax.tick_params(labelsize=11)
    barra.set_label('Esfuerzo vertical$\\sigma{yy}$(kPa)',rotation=90,fontsize=12)
    plt.show()
    
    # esfuerzocortante
    txymax =np.max(sig[:,2])
    tmax ='max='+str(np.round(txymax,2))
    idmax =np.where(sig[:,2]==txymax)[0][0]
    txymin =np.min(sig[:,2])
    tmin ='min='+str(np.round(txymin,2))
    idmin =np.where(sig[:,2]==txymin)[0][0]

    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    b =ax.scatter(xp[:,0],xp[:,1],15,c=sig[:,2],vmin=np.min(sig[:,2]),
    vmax=np.max(sig[:,2]), cmap=plt.cm.jet)
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)
    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Estado deesfuerzosgeostatico',fontsize=14)
    ax.text(xp[idmax,0], xp[idmax,1],tmax,fontsize=9,verticalalignment='center',
    bbox=props)
    ax.text(xp[idmin,0], xp[idmin,1],tmin,fontsize=9,verticalalignment='center',
    bbox=props)
    barra =fig.colorbar(b)
    barra.ax.tick_params(labelsize=11)
    barra.set_label('Esfuerzo cortante$\\sigma_{xy}$(kPa)',rotation=90,fontsize=12)
    plt.show()

    # graficacondesplazamientodelpasogeoesatico
    demax =np.max(despl)
    tmax ='max='+str(np.round(demax,3))
    idmax =np.where(despl==demax)[0][0]
    demin =np.min(despl)
    tmin ='min='+str(np.round(demin,2))
    idmin =np.where(despl==demin)[0][0]
    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    b =ax.scatter(xp[:,0],xp[:,1],15,c=despl,vmin=np.min(despl),vmax=np.max(despl),
    cmap=plt.cm.jet)
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)
    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Desplazamiento pasogeostatico',fontsize=14)
    ax.text(xp[idmax,0], xp[idmax,1],tmax,fontsize=9,verticalalignment='center',
    bbox=props)
    #ax.text(xp[idmin,0], xp[idmin,1],tmin,fontsize=9,verticalalignment='center',bbox=props)
    barra =fig.colorbar(b)
    barra.ax.tick_params(labelsize=11)
    barra.set_label('Desplazamiento total$\\delta$(m)',rotation=90,fontsize=12)
    plt.show()

    # grafica ultimo desplzamiento xp
    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    ax.scatter(xp[:,0],xp[:,1],15,c='b')
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)
    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Distribucion final de particulas',fontsize=14)
    plt.show()
    

    # Guardar todo el estado geoestatico en NPZ (robusto a versiones)
    np.savez_compressed(
        "result_talud_2021/geostatic_state.npz",
        # Esfuerzos y deformaciones finales
        sig=sig, Fp=Fp, epse=epse, epsp=epsp,
        # Posiciones y desplazamientos
        xp=xp, xp0=xp0, despl=despl,
        # Volumenes
        Vp=Vp, Vp0=Vp0, rhop=rhop,
        # Propiedades del material
        Prop=Prop,
        # Conectividad de MPs
        mp_elem=mp_elem,
        # Parametros geometricos y numericos
        dimx=dimx, dimy=dimy, ele_size=ele_size,
        dtime=dtime, nmp=nmp,
        # Separacion de materiales
        idM1=idM1, idM2=idM2
    )


def fase_falla():
    # === PARAMETROS DE LA SIMULACION ===
    Young = 3.8e3 
    alpha = 0.10 
    name1 = 'S14_'
    Coh = 20
    Phi = 20
    tie = 8.0 # tiempo de simulacion
    Mu = 0.268
    Psi = 10 
    name = 'G9'
    t0 = tm.time() # tiempo inicial

    # Cargar estado geoestatico desde NPZ
    geostatic_file = "result_talud_2021/geostatic_state.npz"
    geo_data = np.load(geostatic_file)
    sig = geo_data['sig']  # esfuerzos iniciales

    # === GUARDANDO LA DIRECCION Y NOMBRE DEL ARCHIVO ===
    cdir = os.getcwd()

    # ===== CREAR MALLA DE ELEMENTOS FINITOS ========
    dimx, dimy, ele_size = 60, 32, 0.25
    mesh = create_uniform(dimx, dimy, ele_size) 
    cor, inci, nelex = mesh
    nnodesx = int(nelex + 1) 
    nnodesy = int(len(cor)/nnodesx)
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1) 
    node_support = node_conectivity(inci, len(cor[:,0])) # conectividad de los nodos

    # ############### INICIALIZAR PARTICULAS - UNIFICADO ##########################
    # Usamos la misma logica que en fase_geoestatica para asegurar consistencia
    xi, yi, xf, yf = 0, 0, 60.0, 30.25
    nmpe = 4 
    mp_elem_full, xp_full, active_elem_full = setup_MP(xi, yi, xf, yf, cor, inci, nmpe)

    # Parametros de geometria (yf real para el talud)
    yf_real = 30.25

    # +++++++++ TOMAR DOMINIO INCLINADO - TALUD +++++++++
    x1, x2, y1_geom = 8, 18, 0.25
    idpa = np.zeros(len(xp_full[:,0])).astype(int)
    idcont = 0
    for j in range(len(xp_full[:,0])):
        if xp_full[j,0] <= x1:
            idpa[idcont] = j
            idcont += 1
        elif xp_full[j,0] <= x2:
            ylim = (yf_real*x2 - y1_geom*x1)/(x2 - x1) - (yf_real - y1_geom)/(x2 - x1) * xp_full[j,0]
            if xp_full[j,1] <= (ylim + 1e-10):
                idpa[idcont] = j
                idcont += 1
        else:
            ylim = y1_geom
            if xp_full[j,1] <= ylim:
                idpa[idcont] = j
                idcont += 1
    idpa = idpa[:idcont]
    xp_full = xp_full[idpa,:]
    mp_elem_full = mp_elem_full[idpa,:]

    # Separar en Cuerpo 1 (bajo y1=0.25) y Cuerpo 2 (sobre y1=0.25)
    idM1 = np.where(xp_full[:,1] <= y1_geom)[0]
    idM2 = np.where(xp_full[:,1] > y1_geom)[0]

    # CUERPO 1 (Base/Estrato inferior)
    xp_1 = xp_full[idM1,:]
    mp_elem_1 = mp_elem_full[idM1,:]
    nmp_1 = len(idM1)
    Vp_1 = (ele_size ** 2) / nmpe * np.ones(nmp_1)
    Vp0_1 = (ele_size ** 2) / nmpe * np.ones(nmp_1) 
    rhop_1 = 2.6 * np.ones(nmp_1) 
    Mp_1 = np.multiply(rhop_1, Vp_1) 
    Prop_1 = np.zeros((nmp_1,6))
    Prop_1[:,0] = 10e3 
    Prop_1[:,1] = 0.3 
    Prop_1[:,2] = 200 
    Prop_1[:,3] = 35/180*math.pi 
    Prop_1[:,4] = 35/180*math.pi 
    Fp_1 = np.ones((nmp_1, 4)) 
    Fp_1[:, 1:3] = 0 
    sig_1 = sig[idM1,:]
    epse_1 = np.zeros((nmp_1, 3)) 
    epsp_1 = np.zeros((nmp_1, 3)) 
    vp_1 = np.zeros((nmp_1, 2)) 
    bp_1 = np.zeros((nmp_1, 2)) 
    bp_1[:,1] = 0 
    tp_1 = np.zeros((nmp_1, 2)) 

    # CUERPO 2 (Talud/Estrato superior)
    xp_2 = xp_full[idM2,:]
    mp_elem_2 = mp_elem_full[idM2,:]
    nmp_2 = len(idM2)
    Vp_2 = (ele_size ** 2) / nmpe * np.ones(nmp_2)
    Vp0_2 = (ele_size ** 2) / nmpe * np.ones(nmp_2) 
    rhop_2 = 1.8 * np.ones(nmp_2) 
    Mp_2 = np.multiply(rhop_2, Vp_2) 
    Prop_2 = np.zeros((nmp_2,6))
    Prop_2[:,0] = Young 
    Prop_2[:,1] = 0.3 
    Prop_2[:,2] = Coh 
    Prop_2[:,3] = Phi/180*math.pi 
    Prop_2[:,4] = Psi/180*math.pi 
    Fp_2 = np.ones((nmp_2, 4)) 
    Fp_2[:, 1:3] = 0 
    sig_2 = sig[idM2, :]
    epse_2 = np.zeros((nmp_2, 3)) 
    epsp_2 = np.zeros((nmp_2, 3)) 
    vp_2 = np.zeros((nmp_2, 2)) 
    bp_2 = np.zeros((nmp_2, 2)) 
    bp_2[:,1] = -9.81 
    tp_2 = np.zeros((nmp_2, 2)) 

    # === PROCEDIMIENTO SOLUCION ===
    dtime_1 = deltatime(Prop_1[:,0], Prop_1[:,1], rhop_1, ele_size, 0.1) 
    dtime_2 = deltatime(Prop_2[:,0], Prop_2[:,1], rhop_2, ele_size, 0.1) 
    dtime = np.min([dtime_1, dtime_2]) 
    time_sim = tie
    time_sim = math.ceil(time_sim / dtime)*dtime 
    tiempo = np.arange(0, time_sim, dtime)
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)

    if dtime < 0.05:
        ndt = math.floor(0.05 / dtime) 
        dtimegraphic = ndt*dtime
    else:
        dtimegraphic = dtime
    tiempographic = np.arange(0, time_sim, dtimegraphic)

    nmp = nmp_1 + nmp_2
    corX = np.empty((nmp, len(tiempographic) + 1))
    corY = np.empty((nmp, len(tiempographic) + 1))
    sigxx = np.empty((nmp, len(tiempographic) + 1))
    sigyy = np.empty((nmp, len(tiempographic) + 1))
    sigxy = np.empty((nmp, len(tiempographic) + 1))
    epsxx = np.empty((nmp, len(tiempographic) + 1))
    epsyy = np.empty((nmp, len(tiempographic) + 1))
    epsxy = np.empty((nmp, len(tiempographic) + 1))
    despl = np.empty((nmp, len(tiempographic) + 1))
    eqplas = np.empty((nmp, len(tiempographic) + 1))
    velp = np.empty((nmp, len(tiempographic) + 1))

    # Guardando valores iniciales
    corX[:nmp_1,0], corY[:nmp_1,0] = xp_1[:,0], xp_1[:,1]
    corX[nmp_1:,0], corY[nmp_1:,0] = xp_2[:,0], xp_2[:,1]
    sigxx[:nmp_1,0], sigyy[:nmp_1,0], sigxy[:nmp_1,0] = sig_1[:,0], sig_1[:,1], sig_1[:,2]
    sigxx[nmp_1:,0], sigyy[nmp_1:,0], sigxy[nmp_1:,0] = sig_2[:,0], sig_2[:,1], sig_2[:,2]
    epsxx[:nmp_1,0], epsyy[:nmp_1,0], epsxy[:nmp_1,0] = epse_1[:,0], epse_1[:,1], epse_1[:,2]
    epsxx[nmp_1:,0], epsyy[nmp_1:,0], epsxy[nmp_1:,0] = epse_2[:,0], epse_2[:,1], epse_2[:,2]
    despl[:,0] = 0
    eqplas[:,0] = 0
    velp[:,0] = 0
    tgraphic = 0

    print("Inicio simulacion de colapso")
    print(f"Paso de tiempo dtime = {dtime:.6f} s | Total de pasos = {len(tiempo)}")
    for t in range(len(tiempo)):
        mp_elem_1, active_elem_1 = search_MP(mp_elem_1, xp_1, ele_size, nelex)
        mp_elem_2, active_elem_2 = search_MP(mp_elem_2, xp_2, ele_size, nelex)
        active_elem = np.unique(np.concatenate((active_elem_1, active_elem_2), axis=0))
        active_nodes = np.unique(inci[active_elem - 1,:])
        active_nodes_1 = np.unique(inci[active_elem_1 - 1,:])
        active_nodes_2 = np.unique(inci[active_elem_2 - 1,:])

        grid_1 = inci, cor, active_elem, active_nodes, mp_elem_1
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, bp_1, tp_1
        nmass_1, nmomentum_1, niforce_1, neforce_1, shfnp_1 = particles_to_nodes(grid_1, particle_1)

        grid_2 = inci, cor, active_elem, active_nodes, mp_elem_2
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, bp_2, tp_2
        nmass_2, nmomentum_2, niforce_2, neforce_2, shfnp_2 = particles_to_nodes(grid_2, particle_2)

        nmomentum_1t = np.copy(nmomentum_1)
        nmomentum_2t = np.copy(nmomentum_2)
        dampfac = alpha

        ndamping_1 = -dampfac*np.multiply(np.absolute(niforce_1 + neforce_1), np.sign(nmomentum_1))
        nforce_1 = niforce_1 + neforce_1 + ndamping_1
        nmomentum_1 += nforce_1*dtime

        ndamping_2 = -dampfac*np.multiply(np.absolute(niforce_2 + neforce_2), np.sign(nmomentum_2))
        nforce_2 = niforce_2 + neforce_2 + ndamping_2
        nmomentum_2 += nforce_2*dtime

        nmassS = nmass_1 + nmass_2
        nmomentumS = nmomentum_1 + nmomentum_2
        mesh_data = inci, cor, node_support, active_nodes
        body1 = nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1
        body2 = nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2
        nmomentum_1, nmomentum_2 = contact(body1, body2, nmassS, nmomentumS, mesh_data, dtime, Mu)
        
        nforce_1 = 1 / dtime * (nmomentum_1 - nmomentum_1t)
        nforce_2 = 1 / dtime * (nmomentum_2 - nmomentum_2t)

        nmomentum_1, nforce_1 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_1, nforce_1)
        nmomentum_2, nforce_2 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_2, nforce_2)

        nquantities_1 = nmass_1, nmomentum_1, nforce_1
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, shfnp_1
        xp_1, vp_1, nvel_1 = nodes_to_particle_vel(grid_1, particle_1, nquantities_1, dtime)
        nvel_1 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_1)

        nquantities_2 = nmass_2, nmomentum_2, nforce_2
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, shfnp_2
        xp_2, vp_2, nvel_2 = nodes_to_particle_vel(grid_2, particle_2, nquantities_2, dtime)
        nvel_2 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_2)

        particle_1 = Fp_1, Vp_1, Vp0_1, epse_1, epsp_1, sig_1, shfnp_1, Prop_1
        Fp_1, Vp_1, epse_1, epsp_1, sig_1 = nodes_to_particle_stress2(grid_1, particle_1, nvel_1, dtime, 0)

        particle_2 = Fp_2, Vp_2, Vp0_2, epse_2, epsp_2, sig_2, shfnp_2, Prop_2
        Fp_2, Vp_2, epse_2, epsp_2, sig_2 = nodes_to_particle_stress2(grid_2, particle_2, nvel_2, dtime, 1)

        if t == len(tiempo) - 1:
            corX[:nmp_1,-1], corY[:nmp_1,-1] = xp_1[:,0], xp_1[:,1]
            corX[nmp_1:,-1], corY[nmp_1:,-1] = xp_2[:,0], xp_2[:,1]
            sigxx[:nmp_1,-1], sigyy[:nmp_1,-1], sigxy[:nmp_1,-1] = sig_1[:,0], sig_1[:,1], sig_1[:,2]
            sigxx[nmp_1:,-1], sigyy[nmp_1:,-1], sigxy[nmp_1:,-1] = sig_2[:,0], sig_2[:,1], sig_2[:,2]
            epsxx[:nmp_1,-1], epsyy[:nmp_1,-1], epsxy[:nmp_1,-1] = epse_1[:,0], epse_1[:,1], epse_1[:,2]
            epsxx[nmp_1:,-1], epsyy[nmp_1:,-1], epsxy[nmp_1:,-1] = epse_2[:,0], epse_2[:,1], epse_2[:,2]
            despl[:,-1] = np.sqrt((corX[:,0] - corX[:,-1])**2 + (corY[:,0] - corY[:,-1])**2)
            eqplas[:nmp_1,-1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2) + 4/3*epsp_1[:,2]**2)
            eqplas[nmp_1:,-1] = np.sqrt(4/9*(epsp_2[:,0]**2 - epsp_2[:,0]*epsp_2[:,1] + epsp_2[:,1]**2) + 4/3*epsp_2[:,2]**2)
            velp[:nmp_1,-1] = np.sqrt(vp_1[:,0]**2 + vp_1[:,1]**2)
            velp[nmp_1:,-1] = np.sqrt(vp_2[:,0]**2 + vp_2[:,1]**2)
        elif abs(tiempo[t+1] - tiempographic[tgraphic + 1])<1e-13:
            corX[:nmp_1,tgraphic + 1], corY[:nmp_1,tgraphic + 1] = xp_1[:,0], xp_1[:,1]
            corX[nmp_1:,tgraphic + 1], corY[nmp_1:,tgraphic + 1] = xp_2[:,0], xp_2[:,1]
            sigxx[:nmp_1,tgraphic + 1], sigyy[:nmp_1,tgraphic + 1], sigxy[:nmp_1,tgraphic + 1] = sig_1[:,0], sig_1[:,1], sig_1[:,2]
            sigxx[nmp_1:,tgraphic + 1], sigyy[nmp_1:,tgraphic + 1], sigxy[nmp_1:,tgraphic + 1] = sig_2[:,0], sig_2[:,1], sig_2[:,2]
            epsxx[:nmp_1,tgraphic + 1], epsyy[:nmp_1,tgraphic + 1], epsxy[:nmp_1,tgraphic + 1] = epse_1[:,0], epse_1[:,1], epse_1[:,2]
            epsxx[nmp_1:,tgraphic + 1], epsyy[nmp_1:,tgraphic + 1], epsxy[nmp_1:,tgraphic + 1] = epse_2[:,0], epse_2[:,1], epse_2[:,2]
            despl[:,tgraphic + 1] = np.sqrt((corX[:,0] - corX[:,tgraphic + 1])**2 + (corY[:,0] - corY[:,tgraphic + 1])**2)
            eqplas[:nmp_1,tgraphic + 1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2) + 4/3*epsp_1[:,2]**2)
            eqplas[nmp_1:,tgraphic + 1] = np.sqrt(4/9*(epsp_2[:,0]**2 - epsp_2[:,0]*epsp_2[:,1] + epsp_2[:,1]**2) + 4/3*epsp_2[:,2]**2)
            velp[:nmp_1,tgraphic + 1] = np.sqrt(vp_1[:,0]**2 + vp_1[:,1]**2)
            velp[nmp_1:,tgraphic + 1] = np.sqrt(vp_2[:,0]**2 + vp_2[:,1]**2)
            print(f"  -> Paso grafico guardado: {tgraphic + 1}/{len(tiempographic)} | Tiempo: {tiempo[t+1]:.3f} s / {time_sim:.3f} s | Progreso: {((t+1)/len(tiempo))*100:.1f}%")
            if tgraphic != len(tiempographic) - 2: tgraphic +=1

    print("Fin simulacion de colapso - tiempo =", tm.time() - t0)
    
    # === GRAFICAR RESULTADOS FINALES ===
    tiempographic = np.append(tiempographic, tiempo[-1] + dtime)
    s_size = (Vp0_1[0]*(12/dimy)**2) * 80
    fig, ax = plt.subplots(3, 1, sharex=True, sharey=True, figsize=(9,13))
    props = dict(boxstyle='round', facecolor='white', alpha=0.9)
    
    # Tiempos para graficar (ajustar segun disponibilidad en tiempographic)
    idx_plots = [5, len(tiempographic)//2, -1]
    for i, idx in enumerate(idx_plots):
        b = ax[i].scatter(corX[:, idx], corY[:, idx], s_size, c=eqplas[:, idx], vmin=0, vmax=np.max(eqplas), cmap=plt.cm.jet)
        ax[i].set(xlim=(0, dimx), ylim=(0, dimy))
        ax[i].text(0.85, 0.9, f't = {tiempographic[idx]:.2f} s', transform=ax[i].transAxes, bbox=props)
        fig.colorbar(b, ax=ax[i], label='eq_plas')
    
    ax[2].set_xlabel('Coordenada x (m)')
    ax[1].set_ylabel('Coordenada y (m)')
    plt.show()

    # Guardar resultados en NPZ (robusto a versiones Python/numba)
    filename_npz = name1 + name + '_data.npz'
    np.savez_compressed(
        f"result_talud_2021/{filename_npz}",
        corX=corX, corY=corY,
        sigxx=sigxx, sigyy=sigyy, sigxy=sigxy,
        epsxx=epsxx, epsyy=epsyy, epsxy=epsxy,
        despl=despl, eqplas=eqplas, velp=velp,
        dimx=dimx, dimy=dimy, ele_size=ele_size,
        nmp=nmp, nmp_1=nmp_1, nmp_2=nmp_2,
        Vp0_1=Vp0_1, Vp0_2=Vp0_2,
        dtime=dtime, tiempographic=tiempographic,
        Young=Young, alpha=alpha, Coh=Coh, Phi=Phi, Psi=Psi, Mu=Mu,
        runout1=np.max(corX[nmp_1:,-1]) - np.max(corX[nmp_1:,0]),
        runout2=despl[-1,-1]
    )

def fase_falla2():
    # === PARAMETROS DE LA SIMULACION ===
    Young = 3.8e3 
    alpha = 0.10 
    name1 = 'S14_'
    Coh = 20
    Phi = 20
    tie = 8.0 # tiempo de simulacion
    #Mu = np.array([0.2, 0.2, 0.2, 0.4, 0.4, 0.4, 0.6, 0.6, 0.6])
    #Psi = np.array([10, 5, 1, 10, 5, 1, 10, 5, 1])
    #runout1 = np.zeros(len(Mu)) # Array con runout base 
    #runout2 = np.zeros(len(Mu))# Array con runout cresta
    #name = ('mu=0.2_psi=10', 'mu=0.2_psi=5', 'mu=0.2_psi=1', 'mu=0.4_psi=10', 'mu=0.4_psi=5', 'mu=0.4_psi=1', 'mu=0.6_psi=10', 'mu=0.6_psi=5', 'mu=0.6_psi=1')

    Mu = 0.268
    Psi = 10
    name = 'G9'

    t0 = tm.time() # tiempo inicial

    # Cargar estado geoestatico desde NPZ
    geostatic_file = "result_talud_2021/geostatic_state.npz"
    geo_data = np.load(geostatic_file)
    sig = geo_data['sig']  # esfuerzos iniciales
    xp_geo = geo_data['xp']  # posiciones finales del paso geoestatico
    Fp_geo = geo_data['Fp']  # gradiente deformacion
    epse_geo = geo_data['epse']  # deformaciones elasticas
    epsp_geo = geo_data['epsp']  # deformaciones plasticas
    Vp_geo = geo_data['Vp']  # volumenes
    Vp0_geo = geo_data['Vp0']  # volumenes iniciales
    rhop_geo = geo_data['rhop']  # densidades
    Prop_geo = geo_data['Prop']  # propiedades
    mp_elem_geo = geo_data['mp_elem']  # conectividad inicial
    idM1_geo = geo_data['idM1']  # indices material 1

    # === GUARDANDO LA DIRECCION Y NOMBRE DEL ARCHIVO ===
    cdir = os.getcwd()
    namescript = os.path.basename( __file__ )
    namescript = namescript[:len(namescript) - 3]

    # ===== CREAR MALLA DE ELEMENTOS FINITOS ========
    dimx, dimy, ele_size = 60, 32, 0.25
    mesh = create_uniform(dimx, dimy, ele_size)
    cor, inci, nelex = mesh
    nnodesx = int(nelex + 1)
    nnodesy = int(len(cor)/nnodesx)
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)
    node_support = node_conectivity(inci, len(cor[:,0])) # conectividad de los nodos

    # ############### INICIALIZAR PARTICULAS - CUERPO 1	##########################
    xi, yi, xf, yf = 0, 0, 60, 0.25 # coordenas inicial y final del rect´angulo que define el dominio
    
    nmpe_1 = 4 # numero de MPs por elemento
    # funcion setup_MP = obtiene elemento asociado a cada mp, coordenadas mp y lista de elemento activos
    mp_elem_1, xp_1, active_elem_1 = setup_MP(xi, yi, xf, yf, cor, inci, nmpe_1)

    # +++++ ACTUALIZAR CANTIDAES DE PARTICULAS =++++
    active_nodes_1 = np.unique(inci[active_elem_1 - 1,:]) # lista de nodos activos

    # ++++++ INICIAR CANTIDADES DE PARTICULAS ++++++++++
    nmp_1 = len(mp_elem_1) # Numero de mp

    Vp_1 = (ele_size ** 2) / nmpe_1 * np.ones(nmp_1) # vector de volumenes
    Vp0_1 = (ele_size ** 2) / nmpe_1 * np.ones(nmp_1) # vector de volumenes iniciales
    rhop_1 = 2.6 * np.ones(nmp_1) # en Mg/m3 - vector de densidades de las particulas
    Mp_1 = np.multiply(rhop_1, Vp_1) # en Mg - vector de masas

    # ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
    Prop_1 = np.zeros((nmp_1,6))
    Prop_1[:,0] = 10e3		# modulos de elasticidad en kPa
    Prop_1[:,1] = 0.3 # coeficiente de poisson
    Prop_1[:,2] = 200	# en kPa - cohesion
    Prop_1[:,3] = 35/180*math.pi # 25 grados de angulo de friccion
    Prop_1[:,4] = 35/180*math.pi # 5 grados de angulo de dilatancia

    Fp_1 = np.ones((nmp_1, 4)) # Mat gradiente de deformacion
    Fp_1[:, 1:3] = 0 # inicia como Mat identidad
    sig_1 = np.zeros((nmp_1, 4)) # Mat esfuerzos
    sig_1 = sig[:nmp_1,:]

    epse_1 = np.zeros((nmp_1, 3)) # Mat def elasticas
    epsp_1 = np.zeros((nmp_1, 3)) # Mat def plasticas
    vp_1 = np.zeros((nmp_1, 2)) # Mat velocidd vx y vy
    bp_1 = np.zeros((nmp_1, 2)) # Mat fuerzas de cuerpo bx y by
    bp_1[:,1] = 0 #-9.81 # by = a la gravedad
    tp_1 = np.zeros((nmp_1, 2)) # Mat fuerzas de superficie
    #tp_1 = traction_forces(xp_1, 3, -10, xi, xf) # Fuerza sobre cara 
    #bound_ptcl_1, bound_val_1 = boundary_particles2(xp_1) # particulas frontera - integra gauss

    # ######################## FIN CUERPO 1 #######################################

    # ############### INICIALIZAR PARTICULAS - CUERPO 2	##########################
    xi, yi, xf, yf = 0.0, 0.25, 60, 30.25	# coordenadas inicial y final del rect´angulo que define el dominio
    nmpe_2 = 4 # numero de MPs por elemento
    
    # funcion setup_MP = obtiene elemento asociado a cada mp, coordenadas mp y lista de elemento activos
    mp_elem_2, xp_2, active_elem_2 = setup_MP(xi, yi, xf, yf, cor, inci, nmpe_2)

    # +++++++++ TOMAR DOMINIO INCLINADO - TALUD +++++++++ 
    x1, x2, y1 = 8, 18, 0.25
    idpa  =  np.zeros(len(xp_2[:,0])).astype(int)
    idcont = 0
    for j in range(len(xp_2[:,0])):
        # Funcion Piece wise para geometria
        if xp_2[j,0] <= x1:
            # primer tramo
            idpa[idcont] = j
            idcont += 1
        else:
            # segundo tramo inclinado
            ylim = (yf*x2 - y1*x1)/(x2 - x1) - (yf - y1)/(x2 -x1) * xp_2[j,0] 
            if xp_2[j,1] <= (ylim + 1e-10):
                # esta particula permanece en el dominio
                idpa[idcont] = j
                idcont += 1

    # indexar array idpa para el numero de part´ıculas ingresadas
    idpa = idpa[:idcont] # idpa es array con el id de las part´ıculas que est´an dentro del dominio
    xp_2 = xp_2[idpa,:] # indexando array de coordenadas para las part´ıculas dentro del dominio
    mp_elem_2 = mp_elem_2[idpa, :]

    active_nodes_2 = np.unique(inci[active_elem_2 - 1,:]) # lista de nodos activos 

    # ++++++ INICIAR CANTIDADES DE PARTICULAS ++++++++++
    nmp_2 = len(mp_elem_2) # Numero de mp
    Vp_2 = (ele_size ** 2) / nmpe_2 * np.ones(nmp_2) # vector de volumenes
    Vp0_2 = (ele_size ** 2) / nmpe_2 * np.ones(nmp_2) # vector de volumenes iniciales
    rhop_2 = 1.8 * np.ones(nmp_2) # en Mg/m3 - vector de densidades de las particulas
    Mp_2 = np.multiply(rhop_2, Vp_2) # en Mg - vector de masas

    # ARRAY CON LAS PROPIEDADES DE LAS PARTICULAS - E, nu, C', phi', psi'
    Prop_2 = np.zeros((nmp_2,6))
    Prop_2[:,0] = Young	# modulos de elasticidad en kPa
    Prop_2[:,1] = 0.3 # coeficiente de poisson
    Prop_2[:,2] = Coh	# en kPa - cohesion
    Prop_2[:,3] = Phi/180*math.pi # 25 grados de angulo de friccion
    Prop_2[:,4] = Psi/180*math.pi # 5 grados de angulo de dilatancia

    Fp_2 = np.ones((nmp_2, 4)) # Mat gradiente de deformacion
    Fp_2[:, 1:3] = 0 # inicia como Mat identidad
    sig_2 = np.zeros((nmp_2, 4)) # Mat esfuerzos
    sig_2 = sig[nmp_1:, :]

    epse_2 = np.zeros((nmp_2, 3)) # Mat def elasticas
    epsp_2 = np.zeros((nmp_2, 3)) # Mat def plasticas
    vp_2 = np.zeros((nmp_2, 2)) # Mat velocidd vx y vy
    bp_2 = np.zeros((nmp_2, 2)) # Mat fuerzas de cuerpo bx y by
    bp_2[:,1] = -9.81  # by = a la gravedad

    tp_2 = np.zeros((nmp_2, 2)) # Mat fuerzas de superficie
    #tp_1 = traction_forces(xp_1, 3, -10, xi, xf) # Fuerza sobre cara 
    #bound_ptcl_2, bound_val_2 = boundary_particles2(xp_2) # particulas frontera- integra gauss

    # ######################## FIN CUERPO 2 ####################################### 

    # Graficasmo los dos puntos materiales
    figura3 = plt.figure()
    ax3 = figura3.add_subplot(1,1,1)
    ax3.plot(xp_1[:,0], xp_1[:,1], '.', markersize= 0.5, color = 'k' )
    ax3.plot(xp_2[:,0], xp_2[:,1], '.', markersize= 0.5, color = 'r' )
    ax3.set_aspect('equal')
    plt.show()


    # ###################	PROCEDIMIENTO SOLUCION	#########################
    # calculo del delta de tiempo para convergencia
    dtime_1 = deltatime(Prop_1[:,0], Prop_1[:,1], rhop_1, ele_size, 0.1)
    dtime_2 = deltatime(Prop_2[:,0], Prop_2[:,1], rhop_2, ele_size, 0.1)
    dtime = np.min([dtime_1, dtime_2]) # tomando el minio dt

    # SIN PASO GEOSTATIC
    # --- CICLO EN EL TIEMPO	- PROBLEMA DINAMICO DE COLAPSO---
    # calculo del delta de tiempo para convergencia 
    time = tie
    time = math.ceil(time / dtime)*dtime # recalculando time para ajustar con dtime 
    tiempo = np.arange(0, time, dtime)

    # Retirar condicion de contorno en xBC
    fixed_nodesX, fixed_nodesY = contour_fixe(nnodesx, nnodesy, 0, 0, 0, 1)

    # array para graficar - maximo 20 cuadros por segundo
    if dtime < 0.05:
        ndt = math.floor(0.05 / dtime)
        dtimegraphic = ndt*dtime
    else:
        dtimegraphic = dtime
    



    tiempographic = np.arange(0, time, dtimegraphic)
    # ++++++++++ CREANDO ARRAYS PARA GRAFICAR ++++++++++++++++

    # Arrays con las particulas de todo el sistema
    nmp = nmp_1 + nmp_2 # numero de particulas del sistema 
    corX = np.empty((nmp, len(tiempographic) + 1))
    corY = np.empty((nmp, len(tiempographic) + 1))
    sigxx	=	np.empty((nmp,	len(tiempographic)	+	1))
    sigyy	=	np.empty((nmp,	len(tiempographic)	+	1))
    sigxy	=	np.empty((nmp,	len(tiempographic)	+	1))
    epsxx	=	np.empty((nmp,	len(tiempographic)	+	1))
    epsyy	=	np.empty((nmp,	len(tiempographic)	+	1))
    epsxy	=	np.empty((nmp,	len(tiempographic)	+	1))
    despl	=	np.empty((nmp,	len(tiempographic)	+	1))
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

    tgraphic = 0 # incializando contador de tiempo para graficas print("Inicio simulacion ", name)
    
    print("Inicio simulacion de colapso")
    print(f"Paso de tiempo dtime = {dtime:.6f} s | Total de pasos = {len(tiempo)}")
    
    for t in range(len(tiempo)):
        # --- buscar elementos y nodos activos ---
        mp_elem_1, active_elem_1 = search_MP(mp_elem_1, xp_1, ele_size, nelex) # cuerpo 1 
        mp_elem_2, active_elem_2 = search_MP(mp_elem_2, xp_2, ele_size, nelex) # cuerpo 2 
        active_elem = np.unique(np.concatenate((active_elem_1, active_elem_2),axis=0)) # elemento activos del sistema

        active_nodes_1 = np.unique(inci[active_elem_1 - 1,:]) # lista de nodos activos cuerpo 1
        active_nodes_2 = np.unique(inci[active_elem_2 - 1,:]) # lista de nodos activos cuerpo 2
        active_nodes = np.unique(inci[active_elem - 1,:]) # nodos activos del sistema 
        
        # --- transferir de las particulas a los nodos CUERPO 1----
        grid_1 = inci, cor, active_elem, active_nodes, mp_elem_1 # creando lista de valores de la malla
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, bp_1, tp_1 # creando lista de part´ıculas 
        nmass_1, nmomentum_1, niforce_1, neforce_1, shfnp_1 = particles_to_nodes(grid_1, particle_1)
        
        # --- transferir de las particulas a los nodos CUERPO 2----
        grid_2 = inci, cor, active_elem, active_nodes, mp_elem_2 # creando lista de valores de la malla
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, bp_2, tp_2 # creando lista de part´ıculas 
        nmass_2, nmomentum_2, niforce_2, neforce_2, shfnp_2 = particles_to_nodes(grid_2, particle_2)
        
        # almacenar variables del tiempo t	- para recaluclar vector de fuerzas 
        nmomentum_1t = np.copy(nmomentum_1)
        nmomentum_2t = np.copy(nmomentum_2)
        dampfac = alpha


        # --- Solucion sistema de ecuaciones nodales --- CUERPO 1---- 
        ndamping_1 = -dampfac*np.multiply(np.absolute(niforce_1 + neforce_1), np.sign(nmomentum_1))
        nforce_1 = niforce_1 + neforce_1 + ndamping_1 
        nmomentum_1 += nforce_1*dtime
        
        # --- Solucion sistema de ecuaciones nodales --- CUERPO 2---- 
        ndamping_2 = -dampfac*np.multiply(np.absolute(niforce_2 + neforce_2), np.sign(nmomentum_2))
        nforce_2 = niforce_2 + neforce_2 + ndamping_2 
        nmomentum_2 += nforce_2*dtime
        
        #	###### CANTIDADES NODALES DEL SISTEMA ###########
        nmassS = nmass_1 + nmass_2 
        niforceS = niforce_1 + niforce_2 
        neforceS = neforce_1 + neforce_2
        nmomentumS = nmomentum_1 + nmomentum_2

        #	#### SOLUCION ALGORITMO DE CONTACTO ##########
        mu = Mu # coeficiente de friccion
        mesh = inci, cor, node_support, active_nodes
        body1 = nmass_1, nmomentum_1, active_elem_1, active_nodes_1, mp_elem_1, Mp_1, xp_1 
        body2 = nmass_2, nmomentum_2, active_elem_2, active_nodes_2, mp_elem_2, Mp_2, xp_2 
        nmomentum_1, nmomentum_2 = contact(body1, body2, nmassS, nmomentumS, mesh, dtime, mu) # correccion vector de fuerzas
        nforce_1 = 1 / dtime * (nmomentum_1 - nmomentum_1t) 
        nforce_2 = 1 / dtime * (nmomentum_2 - nmomentum_2t)
        



        # --- Fijar nodos de Dirichlet
        nmomentum_1, nforce_1 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_1, nforce_1) # CUERPO 1
        nmomentum_2, nforce_2 = BC_Dirichlet_momentum3(active_nodes, fixed_nodesX, fixed_nodesY, nmomentum_2, nforce_2) # CUERPO 2
        
        # --- Transferir de los nodos a las particulas - vp y xp CUERPO 1--- 
        nquantities_1 = nmass_1, nmomentum_1, nforce_1 # creando lista de valores nodales 
        particle_1 = xp_1, vp_1, Vp_1, Mp_1, sig_1, shfnp_1 # creando lista de particulas
        xp_1, vp_1, nvel_1 = nodes_to_particle_vel(grid_1, particle_1, nquantities_1, dtime) 
        nvel_1 = BC_Dirichlet_vel(active_nodes, fixed_nodesX,
        fixed_nodesY, nvel_1) # fijar nodos de Dirichlet nvel

        # --- Transferir de los nodos a las particulas - vp y xp CUERPO 2--- 
        nquantities_2 = nmass_2, nmomentum_2, nforce_2 # creando lista de valores nodales 
        particle_2 = xp_2, vp_2, Vp_2, Mp_2, sig_2, shfnp_2 # creando lista de particulas
        xp_2, vp_2, nvel_2 = nodes_to_particle_vel(grid_2, particle_2, nquantities_2, dtime) 
        nvel_2 = BC_Dirichlet_vel(active_nodes, fixed_nodesX, fixed_nodesY, nvel_2) # fijar nodos de Dirichlet nvel
        
        # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion CUERPO 1 --- 
        particle_1 = Fp_1, Vp_1, Vp0_1, epse_1, epsp_1, sig_1, shfnp_1, Prop_1
        Fp_1, Vp_1, epse_1, epsp_1, sig_1 = nodes_to_particle_stress2(grid_1, particle_1, nvel_1, dtime, 0)
        
        # --- Transferir de los nodos a las particulas - Esfuerzo y deformacion CUERPO 2 --- 
        particle_2 = Fp_2, Vp_2, Vp0_2, epse_2, epsp_2, sig_2, shfnp_2, Prop_2
        Fp_2, Vp_2, epse_2, epsp_2, sig_2 = nodes_to_particle_stress2(grid_2, particle_2, nvel_2, dtime, 1)



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
            despl[:,-1] = np.sqrt((corX[:,0] - corX[:,-1])**2 + (corY[:,0] - corY[:,-1])**2) # deformacion plastica equivalente
            eqplas[:nmp_1,-1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2)  +  4/3*epsp_1[:,2]**2)  #  cuerpo  1
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
            
            # deformaci´on pl´astica equivalente
            eqplas[:nmp_1,tgraphic + 1] = np.sqrt(4/9*(epsp_1[:,0]**2 - epsp_1[:,0]*epsp_1[:,1] + epsp_1[:,1]**2) + 4/3*epsp_1[:,2]**2) # cuerpo 1 
            eqplas[nmp_1:,tgraphic + 1] = np.sqrt(4/9*(epsp_2[:,0]**2 - epsp_2[:,0]*epsp_2[:,1] + epsp_2[:,1]**2) + 4/3*epsp_2[:,2]**2) # cuerpo 1 # velocidad particulas
            velp[:nmp_1,tgraphic + 1] = np.sqrt(vp_1[:,0]**2 + vp_1[:,1]**2) # cuerpo 1 
            velp[nmp_1:,tgraphic + 1] = np.sqrt(vp_2[:,0]**2 + vp_2[:,1]**2) # cuerpo 1
            print(f"  -> Paso grafico guardado: {tgraphic + 1}/{len(tiempographic)} | Tiempo: {tiempo[t+1]:.3f} s / {time:.3f} s | Progreso: {((t+1)/len(tiempo))*100:.1f}%")
            if tgraphic != len(tiempographic) - 2: 
                tgraphic +=1

    # -- FIN CICLO DE TIEMPO --

    print("Fin simulacion de colapso - tiempo =", tm.time() - t0)
    # Por fuera del ciclo del tiempo se tiene los arrays con la informaci´on a graficar
    tiempographic = np.append(tiempographic, tiempo[-1] + dtime) # array con los pasos de tiempo
    tf = tm.time() # tiempo final
    print("Fin simulacion - tiempo = ", tf - t0) 
    print()

    # guardar resutados de runout
    runout1 = np.max(corX[nmp_1:,-1]) - np.max(corX[nmp_1:,0])
    


    runout2 = despl[-1,-1]
    # Guardar todos los resultados en NPZ (robusto a versiones Python/numba)
    filename_npz = name1 + name + '_data.npz'
    np.savez_compressed(
        f"result_talud_2021/{filename_npz}",
        # Arrays de resultados (N particulas x T pasos de tiempo)
        corX=corX, corY=corY,
        sigxx=sigxx, sigyy=sigyy, sigxy=sigxy,
        epsxx=epsxx, epsyy=epsyy, epsxy=epsxy,
        despl=despl, eqplas=eqplas, velp=velp,
        # Parámetros y geometría
        dimx=dimx, dimy=dimy, ele_size=ele_size,
        nmp=nmp, nmp_1=nmp_1, nmp_2=nmp_2,
        Vp0_1=Vp0_1, Vp0_2=Vp0_2,
        dtime=dtime, tiempographic=tiempographic,
        Young=Young, alpha=alpha, Coh=Coh, Phi=Phi, Psi=Psi, Mu=Mu,
        # Resultados finales de runout
        runout1=runout1, runout2=runout2,
        # Estados finales de material (para posibles análisis avanzados)
        Fp_1=Fp_1, Fp_2=Fp_2,
        epsp_1=epsp_1, epsp_2=epsp_2,
        sig_1=sig_1, sig_2=sig_2
    )

    # ====== GRAFICAR RESULTADOS =======
    #import matplotlib.pyplot as plt
    graphic_button3(corX, corY, despl, Vp0_1[0]*(12/dimy)**2, tiempographic, dimx, dimy)



    # Graficar particulas 1 y 2
    fig, ax = plt.subplots()
    ax.scatter(xp_1[:,0], xp_1[:,1], color='blue', s=1, label='Cuerpo 1')
    ax.scatter(xp_2[:,0], xp_2[:,1], color='red', s=1, label='Cuerpo 2')
    ax.set_aspect('equal')
    ax.legend()
    plt.show()


def graficar_resultados():

    #4.	Runout Graphics
    #Funci´on para carga los resultados del problema de runout
    from mpm_un.graphics import graphic_button, graphic_button2, graphic_button3, graphic_gif, graphic_video
    import matplotlib.pyplot as plt
    filename_npz = 'result_talud_2021/S14_G9_data.npz'
    # Cargar todos los resultados desde NPZ
    data = np.load(filename_npz)
    corX = data['corX']
    corY = data['corY']
    eqplas = data['eqplas']
    tiempographic = data['tiempographic']
    despl = data['despl']
    Vp0_1 = data['Vp0_1']
    dimx = int(data['dimx'])
    dimy = int(data['dimy'])
    nmp_1 = int(data['nmp_1'])
    '''
    # grafica de malla y particulas mayorticksX = np.arange(0, dimx + 5, 5)
    minorticksX = np.arange(0, dimx + ele_size, ele_size) mayorticksY = np.arange(0, dimy + 3, 3)
    minorticksY = np.arange(0, dimy + ele_size, ele_size)
    s = (Vp0_1[0]*(12/dimy)**2) * 400
    #c = corY[:,0] # graficar en color la posicion Y inicial c = np.zeros(len(corY[:,0]))
    c[:nmp_1] = 1
    tiempo = str(np.round(tiempographic[0], 2)) fig, ax = plt.subplots(figsize=(12,4.5)) plt.subplots_adjust(bottom=0.12, right=0.91)
    b0 = ax.scatter(corX[:, 0], corY[:, 0], s, c=c, vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
    ax.set_xlabel('Coordenada $x$ (m)', fontsize=11) ax.set_ylabel('Coordenada $y$ (m)', fontsize=11) ax.set(xlim=(0, dimx), ylim=(0, dimy)) ax.set_xticks(mayorticksX) ax.set_xticks(minorticksX, minor=True)
    


    ax.set_yticks(mayorticksY) ax.set_yticks(minorticksY, minor=True) ax.grid(which='both') ax.tick_params(labelsize=10)
    ax.set_title('Configuraci´on inicial', fontsize=12) '''
    # grafias de resultados para diferentes instantes de tiempo
    props  =  dict(boxstyle='round',  facecolor='white',  alpha=0.9)
    # Creando subplot tipo scatter deformacion plastica equivalente
    s = (Vp0_1[0]*(12/dimy)**2) * 80
    fig, ax = plt.subplots(3, 1, sharex=True, sharey=True, figsize=(9,13))
    plt.subplots_adjust(bottom=0.1)
    # primer plot ax[0].grid(True)
    b0 = ax[0].scatter(corX[:, 5], corY[:, 5], s, c=eqplas[:,5], vmin=np.min(eqplas[:,5]), vmax=0.08, cmap=plt.cm.jet)
    ax[0].set(xlim=(0, dimx), ylim=(0, dimy)) 
    ax[0].tick_params(labelsize=10)
    #ax[0].set_title('Deformaci´on pl´astica equivalente $\overline{\epsilon}_p$ - $E=10\,MPa \,\, \alpha=0.10$', fontsize=11.5)
    ax[0].set_title(r'$E=10 MPa - \alpha=0.10 - \mu=0.2 - \psi=10^{\circ}$', fontsize=11.5) 
    ax[0].text(0.86, 0.90, 't = '+str(tiempographic[5])+' s', transform=ax[0].transAxes, fontsize=9, verticalalignment='top', bbox=props)
    barra0 = fig.colorbar(b0, ax=ax[0]) 
    barra0.set_ticks([0.0,0.02,0.04,0.06,0.08,0.10])
    barra0.ax.tick_params(labelsize=9)
    barra0.set_label(r'$\overline{\epsilon}_p$', rotation=90, fontsize=11)
    # segundo plot ax[1].grid(True)
    b1 = ax[1].scatter(corX[:, 25], corY[:, 25], s, c=eqplas[:,25], vmin=np.min(eqplas[:,25]), vmax=np.max(eqplas[:,25]), cmap=plt.cm.jet) 
    ax[1].set_ylabel('Coordenada $y$ (m)', fontsize=11)
    ax[1].set(xlim=(0, dimx), ylim=(0, dimy)) 
    ax[1].tick_params(labelsize=10)
    ax[1].text(0.87, 0.90, 't = '+str(tiempographic[20])+' s', transform=ax[1].transAxes, fontsize=9, verticalalignment='top', bbox=props) 
    barra1 = fig.colorbar(b1, ax=ax[1])
    barra1.set_ticks([0.0,0.5,1.0,1.5,2.0,2.5,3.0])
    barra1.ax.tick_params(labelsize=9)
    barra1.set_label(r'$\overline{\epsilon}_p$', rotation=90, fontsize=11)
    # tercer subpplot ax[2].grid(True)
    


    b2 = ax[2].scatter(corX[:, [-1]], corY[:, [-1]], s, c=eqplas[:,[-1]],
    vmin=np.min(eqplas[:,[-1]]), vmax=np.max(eqplas[:,[-1]]), cmap=plt.cm.jet) 
    ax[2].set_xlabel('Coordenada $x$ (m)', fontsize=11)
    ax[2].set(xlim=(0, dimx), ylim=(0, dimy)) 
    ax[2].tick_params(labelsize=10)
    ax[2].text(0.86, 0.90, 't = '+str(tiempographic[-1])+' s', transform=ax[2].transAxes, fontsize=9, verticalalignment='top', bbox=props) 
    ax[2].plot([0,8,15.5], [30.25, 30.25,0.25], ls=':', c='black')
    ax[2].plot([15.5,15.5, np.max(corX[nmp_1:,-1]), np.max(corX[nmp_1:,-1])], [0.4, 3.2, 3.2, 0.4], ls='--', c='m')
    ax[2].text(0.5, 0.25, 'Distancia d', transform=ax[2].transAxes, fontsize=8, verticalalignment='top', bbox=props)
    barra2 = fig.colorbar(b2, ax=ax[2]) 
    barra2.set_ticks([0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0])
    barra2.ax.tick_params(labelsize=9)
    barra2.set_label(r'$\overline{\epsilon}_p$', rotation=90, fontsize=11)
    plt.tight_layout()
    plt.show()

    # Visualizacion interactiva por pasos de tiempo
    velp = data['velp']
    graphic_button3(corX, corY, despl, Vp0_1[0]*(12/dimy)**2, tiempographic, dimx, dimy)

    




if __name__ == "__main__":
    # IMPORTANTE: Si cambias el tamaño de malla (ele_size), borra el archivo 'geostatic_results.pkl'
    # para que se regenere con la nueva configuración.
    
    if not os.path.exists("result_talud_2021/geostatic_state.npz"):
        print("Archivo 'geostatic_state.npz' no encontrado. Iniciando fase_geoestatica...")
        fase_geoestatica()
    else:
        print("Archivo 'geostatic_state.npz' encontrado. Saltando fase_geoestatica.")

    if not os.path.exists("result_talud_2021/S14_G9_data.npz"):
        print("Archivo 'S14_G9_data.npz' no encontrado. Iniciando fase_falla...")
        #fase_falla()
        fase_falla2()
    else:
        print("Archivo 'S14_G9_data.npz' encontrado. Saltando fase_falla.")
    
    graficar_resultados()
