from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import matplotlib.animation as animation
from mpl_toolkits.axes_grid1 import make_axes_locatable


# === funcion par graficar esfuerzos con boton next y previous ====

def graphic_button(x, y, c, s, time, dimx, dimy):
    """Funcion que grafica la variable de interes a lo largo del tiempo, se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    c = c # desplazamiento en cm
    s = s*300 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.17)
    ax.grid(True)
    b = ax.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$ (m)', ylabel='Coordenada $y$ (m)')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Esfuerzo vertical $\sigma_y$ para $t = 0 s$')
    barra = fig.colorbar(b)
    barra.set_label('Esfeurzo vertical $\sigma_y \, (kPa)$', rotation=90)
    
    # POO clase Index con los metodos Next y Prev
    class Index():
        ind = 0
        def next(self, event):
            if self.ind == len(time) -1: 
                pass
            else:
                self.ind += 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Esfuerzo vertical $\sigma_y$ para $t =\, %6.2f s$' %time[self.ind])
            plt.draw()

        def prev(self, event):
            if self.ind == 0:
                pass
            else:
                self.ind -= 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Esfuerzo vertical $\sigma_y$ para $t =\, %6.2f s$' %time[self.ind])
            plt.draw()
    
    # instanciando la clase Index
    callback = Index()
    axprev = plt.axes([0.7, 0.01, 0.1, 0.05])
    axnext = plt.axes([0.81, 0.01, 0.1, 0.05])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    
    plt.show()
    axnext._button = bnext
    axprev._button = bprev
    
# segunda funcion esfuerzos
def graphic_button2(x, y, c, s, time, dimx, dimy):
    """Funcion que grafica la variable de interes a lo largo del tiempo, se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    c = c # desplazamiento en cm
    s = s*300 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.17)
    ax.grid(True)
    b = ax.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$ (m)', ylabel='Coordenada $y$ (m)')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Velocidad de las particulas para $t = 0 s$')
    barra = fig.colorbar(b)
    barra.set_label('velocidad particulas $(m/s^2)$', rotation=90)
    
    # POO clase Index con los metodos Next y Prev
    class Index():
        ind = 0
        def next(self, event):
            if self.ind == len(time) -1: 
                pass
            else:
                self.ind += 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Velocidad de las particulas para $t =\, %6.2f s$' %time[self.ind])
            plt.draw()

        def prev(self, event):
            if self.ind == 0:
                pass
            else:
                self.ind -= 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Velocidad de las particulas para $t =\, %6.2f s$' %time[self.ind])
            plt.draw()
    
    # instanciando la clase Index
    callback = Index()
    axprev = plt.axes([0.7, 0.01, 0.1, 0.05])
    axnext = plt.axes([0.81, 0.01, 0.1, 0.05])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    
    plt.show()
    axnext._button = bnext
    axprev._button = bprev

# === funcion par graficar esfuerzos con boton next y previous ====
# se tiene una barra de colores por cada frame


# segunda funcion desplazamiento
def graphic_button3(x, y, c, s, time, dimx, dimy):
    """Funcion que grafica la variable de interes a lo largo del tiempo, se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    c = c # desplazamiento en cm
    s = s*150 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig, ax = plt.subplots(figsize=(10,4.5))
    plt.subplots_adjust(bottom=0.17)
    ax.grid(True)
    b = ax.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$ (m)', ylabel='Coordenada $y$ (m)')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Desplazamiento total $\delta$ para $g = 0 m/s^2$')
    barra = fig.colorbar(b)
    barra.set_label('Desplazamiento total $\delta \, (m)$', rotation=90)
    
    # POO clase Index con los metodos Next y Prev
    class Index():
        ind = 0
        def next(self, event):
            if self.ind == len(time) -1: 
                pass
            else:
                self.ind += 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Desplazamiento total $\delta$ para $g =\, %6.2f m/s^2$' %time[self.ind])
            plt.draw()

        def prev(self, event):
            if self.ind == 0:
                pass
            else:
                self.ind -= 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind])
            ax.set_title('Desplazamiento total $\delta$ para $g =\, %6.2f m/s^2$' %time[self.ind])
            plt.draw()
    
    # instanciando la clase Index
    callback = Index()
    axprev = plt.axes([0.7, 0.01, 0.1, 0.05])
    axnext = plt.axes([0.81, 0.01, 0.1, 0.05])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    
    plt.show()
    axnext._button = bnext
    axprev._button = bprev

# === funcion par graficar esfuerzos con boton next y previous ====
# se tiene una barra de colores por cada frame

def graphic_button4(x, y, c, s, time, dimx, dimy):
    """Funcion que grafica la variable de interes a lo largo del tiempo, se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    c = c # deformacion en tanto por 1
    s = s*300 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.17)
    ax.grid(True)
    b = ax.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c[:, 0]), vmax=np.max(c[:, 0]), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$', ylabel='Coordenada $y$')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Deformación plástica equivalente $\overline{\epsilon}_p$ en el incremento 0 kN/m')
    barra = fig.colorbar(b)
    barra.set_label('Desplazamiento ($cm$)', rotation=90)
    
    # POO clase Index con los metodos Next y Prev
    class Index():
        ind = 0
        def next(self, event):
            if self.ind == len(time) -1: 
                pass
            else:
                self.ind += 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind], vmin=np.min(c[:, self.ind]), vmax=np.max(c[:, self.ind]), cmap=plt.cm.jet)
            ax.set_title('Deformación plástica equivalente $\overline{\epsilon}_p$ en el incremento %6.2f kN/m' %time[self.ind])
            plt.draw()

        def prev(self, event):
            if self.ind == 0:
                pass
            else:
                self.ind -= 1
            b.set_offsets(np.c_[x[:, self.ind], y[:, self.ind]])
            b.set_array(c[:, self.ind], vmin=np.min(c[:, self.ind]), vmax=np.max(c[:, self.ind]), cmap=plt.cm.jet)
            ax.set_title('Deformación plástica equivalente $\overline{\epsilon}_p$ en el incremento %6.2f kN/m' %time[self.ind])
            plt.draw()
    
    # instanciando la clase Index
    callback = Index()
    axprev = plt.axes([0.7, 0.01, 0.1, 0.05])
    axnext = plt.axes([0.81, 0.01, 0.1, 0.05])
    bnext = Button(axnext, 'Siguiente')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Anterior')
    bprev.on_clicked(callback.prev)
    
    plt.show()
    axnext._button = bnext
    axprev._button = bprev



# ==== funcion para grafica dinamica en gif ===== 

def graphic_gif(x, y, c, s, time, dimx, dimy, namefolder):
    """Funcion para crear gif con los resultados se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    c = c # desplazamiento en cm
    s = s*150 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig = plt.figure(figsize=(10,3.5))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(bottom=0.22)
    ax.grid(True)
    b = plt.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c), vmax=np.max(c), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$', ylabel='Coordenada $y$')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Desplazamiento total $\delta_{t}$ en el incremento 0 kN/m')
    barra = fig.colorbar(b)
    barra.set_label('Desplazamiento ($cm$)', rotation=90)

    def update(frame_number, fig, b):
        i = frame_number % len(time) 
        b.set_offsets(np.c_[x[:, i], y[:, i]])
        b.set_array(c[:, i])
        ax.set_title('Desplazamiento total $\delta_{t}$ en el incremento %6.2f kN/m' %time[i])
        return b,

    ani = animation.FuncAnimation(fig, update, fargs = (fig, b), interval=50, repeat=False, save_count=350)
    ani.save(namefolder + '/anima1.gif', writer='imagemagick')
    
    #return animation.save(namefolder + '/anima1.gif', writer='imagemagick')
    
def graphic_video(x, y, c, s, time, dimx, dimy, namefolder):
    """Funcion para crear gif con los resultados se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=6, metadata=dict(artist='Me'), bitrate=1000)
    
    c = c # desplazamiento en cm
    s = s*360 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig = plt.figure(figsize=(6.5,5))
    ax = fig.add_subplot(111)
    plt.subplots_adjust(bottom=0.15)
    ax.grid(True)
    b = plt.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], vmin=np.min(c[:, :]), vmax=np.max(c[:, :]), cmap=plt.cm.jet)
    ax.set(xlabel='Coordenada $x$', ylabel='Coordenada $y$')
    ax.set(xlim=(0, dimx), ylim=(0, dimy))
    ax.set_title('Deformacion plastica equivalente t=0.0 $s$')
    barra = fig.colorbar(b)
    barra.set_label('Deformacion plastica equivalente', rotation=90)

    def update(frame_number, fig, b):
        i = frame_number % len(time) 
        b.set_offsets(np.c_[x[:, i], y[:, i]])
        b.set_array(c[:, i])
        ax.set_title('Deformacion plastica equivalente t=%6.2f $s$' %time[i])
        return b,

    ani = animation.FuncAnimation(fig, update, fargs = (fig, b), interval=100, repeat=False, save_count=101)
    ani.save(namefolder + '/anima.mp4', writer=writer)
    
    return None


def graphic_video2(x, y, c, s, time, dimx, dimy, namefolder):
    
    """Funcion para crear gif con los resultados se grafica por medio de circulos con un rango de colores de acuerdo al valor de la variable
        Argumentos:
                    x = Array con las coordenadas x de las particulas
                    y = Array con las coordenadas y de las particulas
                    c = Array con los valores de la variable de interes (esfuerzo, deformacion, etc)
                    s = Escalar con el volumen inicial de las particulas
                    time = Array con los pasos de tiempo correspondientes
                    dimx = dimension maxima del dominio - malla de elementos
                    dimy = dimension minimo del domino - malla de elementos"""
    
    # Set up formatting for the movie files
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=5, metadata=dict(artist='Me'), bitrate=5000)
    
    c = c # desplazamiento en cm
    s = s*300 # escalando el tamano de las particulas
    # Creando subplot tipo scatter
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    # I like to position my colorbars this way, but you don't have to
    div = make_axes_locatable(ax)
    cax = div.append_axes('right', '5%', '5%')
    
    b = plt.scatter(x[:, 0], y[:, 0], s, c=c[:, 0], cmap=plt.cm.jet)
    cb = fig.colorbar(b, cax=cax)
    tx = ax.set_title('Frame 0')
    #ax.set(xlabel='Coordenada $x$', ylabel='Coordenada $y$')
    #ax.set(xlim=(0, dimx), ylim=(0, dimy))
    #ax.set_title('Deformación plástica equivalente $\overline{\epsilon}_p$ para g=0 $m/s$')
    #barra = fig.colorbar(b)
    #barra.set_label('$\overline{\epsilon}_p$', rotation=90)

    def animate(i):
        vmax     = np.max(c[:,i])
        vmin     = np.min(c[:,i])
        b = ax.scatter(x[:, i], y[:, i], s, c=c[:, i], vmax=vmax, vmin=vmin)
        cax.cla()
        fig.colorbar(b, cax=cax)
        tx.set_text('Frame {0}'.format(i))

    ani = animation.FuncAnimation(fig, animate, frames=len(x[0,:]))
    #ani.save(namefolder + '/anima.mp4', writer=writer)
    
    return None
