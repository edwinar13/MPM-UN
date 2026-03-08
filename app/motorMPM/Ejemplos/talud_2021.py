from __future__ import division
from __future__ import print_function
#import time
import os
import numpy as np
import math,time
from mpm_un.mesh import create_uniform,contour_fixe,setup_MP,search_MP, traction_forces, boundary_particles2
from mpm_un.mesh import create_uniform2,setup_MP2,search_MP2
from mpm_un.explicit2 import deltatime,particles_to_nodes, particles_to_nodes_gauss, BC_Dirichlet_momentum,particles_to_nodes_gauss2
from mpm_un.explicit2 import nodes_to_particle_vel,BC_Dirichlet_vel,nodes_to_particle_stress, static_convergence,nodes_to_particle_stress_gauss, static_convergence2
from mpm_un.graphics import graphic_button,graphic_button2,graphic_gif,graphic_video


def run():
    t0 =time.time()#tiempoinicial

    # rampaparaincrementodegravedad
    grav =np.linspace(0.01,1,50)#100incrementosdecargaiguales
    #grav =np.array([0.01,0.03,0.06,0.10,0.15,0.21,0.29,0.39,0.50,0.62,0.75,0.87, 1.0])

    # ===GUARDANDOLADIRECCIONYNOMBREDELARCHIVO===
    cdir =os.getcwd()
    namescript =os.path.basename(__file__)
    namescript =namescript[:len(namescript)-3]


    # =====CREARMALLADEELEMENTOSFINITOS========
    dimx, dimy,ele_size=60,20,1.0
    mesh =create_uniform(dimx,dimy,ele_size)
    cor, inci,nelex=mesh
    nnodesx =int(nelex+1)
    nnodesy =int(len(cor)/nnodesx)
    fixed_nodesX, fixed_nodesY=contour_fixe(nnodesx,nnodesy,0,0,0,1)


    # ==========INICIALIZARMPs=============
    xi, yi,xf,yf=0,0,60.0,17.0#coordenadainicialyfinaldelrectanguloque define eldominio
    nmpe =4 #numerodeMPsporelemento
    # funcionsetup_MP=obtieneelementoasociadoacadamp,coordenadasmpylista de elementoactivos
    mp_elem, xp,active_elem=setup_MP(xi,yi,xf,yf,cor,inci,nmpe)


    # +++++++++TOMARDOMINIOINCLINADO-TALUD+++++++++
    x1, x2,y1=8,14,.5
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
    print(xp)

    #dibujar en matplotlib
    import matplotlib.pyplot as plt
    fig, ax=plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    ax.scatter(xp[:,0],xp[:,1],15,c='b')
    ax.set_xlabel('Coordenada $x$(m)',fontsize=13)
    ax.set_ylabel('Coordenada $y$(m)',fontsize=13)
    ax.set(xlim=(0, dimx),ylim=(0,dimy))
    ax.tick_params(labelsize=11)
    ax.set_title('Distribucion inicial de particulas',fontsize=14)
    plt.show()

    

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

    nmp =len(mp_elem)#Numerodemp
    Vp =(ele_size**2)/nmpe*np.ones(nmp)#vectordevolumenes
    Vp0 =(ele_size**2)/nmpe*np.ones(nmp)#vectordevolumenesiniciales
    rhop =1.8*np.ones(nmp)#enMg/m3-vectordedensidadesdelaspartculas
    rhop[idM1] =2.6
    Mp =np.multiply(rhop,Vp)#enMg-vectordemasas

    # ARRAYCONLASPROPIEDADESDELASPARTICULAS-E,nu,C',phi',psi'
    Prop =np.zeros((nmp,6))
    Prop[:,0] =15e3#modulosdeelasticidadenkPa
    Prop[:,1] =0.3#coeficientedePoisson
    Prop[:,2] =5#enkPa-cohesion
    Prop[idM1,2] =50#CohesionparaM1
    Prop[:,3] =25/180*math.pi#25gradosdeangulodefriccion
    Prop[:,4] =25/180*math.pi#25gradosdeangulodedilatancia

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
        tgrav =time.time()
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
                print("Iteracion=",tcont,"ff=",ff,"ee=",ee)
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
            xp, vp,nvel=nodes_to_particle_vel(grid,particle,nquantities,dtime)
            nvel =BC_Dirichlet_vel(active_nodes,fixed_nodesX,fixed_nodesY,nvel)#fijar        nodos deDirichletnvel
            
            
            # ---Transferirdelosnodosalasparticulas-Esfuerzoydeformacion---
            tcont +=1
            particle =Fp,Vp,Vp0,epse,epsp,sig,shfnp,Prop
            #Fp, Vp,epse,epsp,sig=nodes_to_particle_stress(grid,particle,nvel, dtime,0)
            Fp, Vp,epse,epsp,sig=nodes_to_particle_stress_gauss(grid,particle,
            bound_val,
            nvel, dtime,0)
            
            
            # ---Calcularparametrosquedeterminarelequilibriocuasi-estatico---
            nework0 =nework
            ff, ee,nework=static_convergence(nmass,niforce,neforce,nvel,dtime,nework0)

        # ====FINPASOEQUILIBRIOGEOSTATICO====
        tgravf =time.time()
        tejecuciong =tgravf-tgrav
        print("Fin incrementogeoestatico",j+1,"Porcentajegravedad=",grav[j])
        print("Numero deiteraciones=",tcont,"Tiempodeejecucion=",tejecuciong)
        print("ff =",ff,"/ee=",ee)
        print()
        
    # ====FINEQUILIBRIOGEOSTATICOTODOSLOSINCREMENTOS====
    tf =time.time()
    tejecucion =tf-t0
    print("FIN PASOGEOSTATICO")
    print("Tiempo deejecuciontotal=",tejecucion)
    # Calculodedesplazamientoenpasogeoestatic
    despl =np.sqrt((xp[:,0]-xp0[:,0])**2+(xp[:,1]-xp0[:,1])**2)
    
    # graficadeladistribucioninicialdeesfuerzos
    import matplotlib.pyplot as plt
    props =dict(boxstyle='round',facecolor='white',alpha=1.0)#propiedadestextframe
    syymax =np.max(sig[:,1])
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
    

    # guardando estadode esfuerzos geoestatico
    import pickle
    with open("geostatic_z8_s12",'wb') as f:
        pickle.dump(sig,f)



run()
