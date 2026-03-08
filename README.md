<h1 align="center">
  <br>
  <img src="app/resources/iconos/iconos_logo/Logo_V1.svg" alt="MPM-UN" width="200">
  <br>
  MPM-UN
  <br>
</h1>

<h4 align="center">Aplicación de simulación numérica para análisis geotécnicos utilizando el <b>Método del Punto Material (MPM)</b>.</h4>

<p align="center">
  <a href="#características">Características</a> •
  <a href="#instalación">Instalación</a> •
  <a href="#uso">Uso</a> •
  <a href="#estructura-del-proyecto">Estructura</a> •
  <a href="#contribución">Contribución</a>
</p>

---

**MPM-UN** es una aplicación desarrollada como parte de investigación de posgrado en geotecnia en la Universidad Nacional de Colombia. Proporciona una interfaz gráfica moderna (UI) que envuelve un motor de cálculo explícito en Python basado en el **Material Point Method (MPM)**, facilitando la simulación de problemas de mecánica de sólidos deformables y grandes deformaciones.

## ✨ Características

* 🖥️ **Interfaz Gráfica Intuitiva (GUI):** Construida mediante el patrón MVC y PySide6, permite configurar geometrías, mallas y condiciones de frontera sin lidiar con el código matriz.
* ⚙️ **Potente Motor MPM:** Integración de rutinas de integración de tiempo explícita asistidas por **Numba** (`@njit`) para cálculos de alta eficiencia.
* 📊 **Análisis Generalizados:** Soporte para análisis cuasi-estáticos y dinámicos para casos como capacidad portante, falla de taludes, etc.
* 📈 **Visualización Integrada:** Herramientas para visualizar datos iterativos de esfuerzos, deformaciones y desplazamientos directamente, junto con animaciones generadas cuadro por cuadro.

## 🛠 Estructura del Proyecto

El código está enfocado en la modularidad para separar claramente los cálculos pesados de la manipulación visual:

```txt
MPM-UN/
├── app/
│   ├── main.py                # Punto de entrada de la GUI
│   ├── controllers/           # Controladores MVC (lógica de interacción UI)
│   ├── models/                # Modelos MVC (gestión de estado de proyecto y análisis)
│   ├── views/                 # Vistas MVC (componentes gráficos PySide6)
│   ├── ui/                    # Archivos generados de Qt Designer (.ui y .py)
│   ├── motorMPM/              # 🧠 Motor del Método del Punto Material (Rutinas Críticas)
│   │   ├── explicit2.py       # Funciones integradoras principales con Numba
│   │   ├── mesh.py            # Rutinas de generación de malla de fondo y conectividad
│   │   └── graphics.py        # Salidas gráficas del motor puro
│   └── resources/             # Íconos, CSS, fuentes y ejemplos pre-construidos (.mpm)
├── tests/                     # Archivos de prueba y validación (.mpm experimentales)
├── requirements.txt           # Dependencias principales del software
└── README.md                  # Este documento
```

## 💻 Instalación

### Requisitos Previos
- **Python 3.9+**
- (Recomendado) Sistema operativo de 64-bits debido al alto requerimiento de memoria en simulaciones extensas con NumPy/Numba.

### Pasos

1. **Clona el repositorio** en tu entorno local:
   ```bash
   git clone https://github.com/tu_usuario/MPM-UN.git
   cd MPM-UN
   ```

2. **Crea y activa un entorno virtual** (Buenas prácticas):
   * En Windows:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   * En macOS/Linux:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Instala las dependencias** requeridas (PySide6, NumPy, Numba, Matplotlib, Pandar, etc):
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Uso

Para abrir la interfaz gráfica, simplemente ejecuta:

```bash
python app/main.py
```

Una vez abierta la aplicación, podrás:
1. Crear un nuevo proyecto o abrir uno de los ejemplos ubicados en `app/resources/ejemplos/`.
2. Modificar la geometría, asignar propiedades de material y dibujar la zona discretizada por puntos materiales.
3. Definir la malla de fondo (Background Mesh).
4. Proceder a la pestaña de ejecución para procesar la simulación a través del orquestador del Motor MPM.

## 🤝 Contribución

¡Las contribuciones son bienvenidas, particularmente en la generalización del motor MPM y mejoras de UI!

1. Haz un *Fork* del repositorio.
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`).
3. Realiza tus commits (`git commit -m 'Add some AmazingFeature'`).
4. Haz *Push* a tu cuenta (`git push origin feature/AmazingFeature`).
5. Abre un *Pull Request*.

## 📄 Licencia

Construido para propósitos académicos y de investigación. Revisa el archivo `LICENSE` proporcionado en el directorio para más detalles.






lan de Implementación: Generalización de Conexión UI-Motor MPM
El objetivo principal es desacoplar la interfaz gráfica (UI) del motor de cálculo (MPM) para que la ejecución no dependa de casos específicos (
runViga
 o 
runAnalysisCE
), sino que sea un proceso de simulación general basado en los datos de entrada.

Diagnóstico Actual
Actualmente, la clase 
ModelExcuteAnalysisMPM
 en 
app/models/model_execute_analysis.py
 extrae los datos directamente de los modelos de la UI (ModelProjectCurrent) y ejecuta bucles transitorios anudados con la lógica del MPM. Esto crea un fuerte acoplamiento y obliga a programar un método run... para cada tipo de problema.

Cambios Propuestos
1. Definición de un Formato de Entrada Estándar (Input Config)
El Motor MPM no debería conocer nada sobre los objetos de la UI (e.g., model_current_project). La UI debe generar un "paquete" de datos estándar (un diccionario de Python o JSON) que el motor pueda leer.

Mesh: Coordenadas nodales, tamaño de elemento, nodos activos.
Particles (Points): Posiciones, volúmenes, velocidades, id de material.
Properties: Módulo de elasticidad, Poisson, densidad, cohesión, etc.
Boundaries: Condiciones de contorno de Dirichlet (velocidad 0) en X e Y.
Time Settings: dt, pasos, gravedad, amortiguamiento, Courant, etc.
2. Creación de un Orquestador en motorMPM
Crear un nuevo archivo, por ejemplo app/motorMPM/runner.py (o solver.py), que albergue una clase o función general MotorMPMRun(config_dict).

Este runner tomará el archivo o diccionario de entrada.
Inicializará todos los arrays de Numpy (Fp, sig, epse, epsp, vp, bp, etc.) genéricamente iterando sobre la configuración.
Tendrá un único bucle de tiempo general que llame a las funciones de numba en 
explicit.py
/
explicit2.py
/
explicit3.py
.
Retornará los resultados empaquetados.
3. Refactorización de la UI (
model_execute_analysis.py
)
La UI simplemente actuará como un traductor:

Extraerá la información visual.
Formará el config_dict.
Llamará a MotorMPMRun(config).
Tomará los arrays resultantes y los guardará en ModelResult.
Verification Plan
Manual Verification
Abrir la UI de MPM-UN.
Cargar uno de los ejemplos (por ejemplo, Ejemplo viga o Ejemplo capacidad portante).
Ejecutar el análisis y verificar que el "Runner" general es el que se ejecuta.
Validar que la barra de progreso avanza y que los resultados generados (esfuerzos, posiciones) coinciden visualmente con la versión anterior.