from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from views.results.view_WidgetResultMenuTable import ViewWidgetResultMenuTable
from models.model_ProjectCurrent import ModelProjectCurrent
from controllers.cards.controller_CardMesh import ControllerCardMesh
import pygmsh
import math
import time
from utils.general_functions import isNumber


from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import matplotlib.pyplot as plt
import numpy as np

class ControllerMenuResultTable(QObject):    
    signal_table_search_point = Signal(str)
    signal_table_clear = Signal()
    signal_table_hise_show_column = Signal(dict)
    
    def __init__(self) -> None:
        super().__init__()

        self.view_menu_result_table= ViewWidgetResultMenuTable()
     
        self.model_current_project = None
        self.model_result = None
        self.scene_is_play = True

        self.__config()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __config(self): 
        pass

    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
        self.view_menu_result_table.signal_table_search_point.connect(self.signalTableSearchPoint)
        self.view_menu_result_table.signal_table_clear.connect(self.signalTableClear)
        self.view_menu_result_table.signal_table_hise_show_column.connect(self.signalTableHiseShowColumn)   
        self.view_menu_result_table.signal_save_data.connect(self.signalSaveData) 
        self.view_menu_result_table.signal_generate_pdf.connect(self.signalGeneratePdf)
                
    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project
        self.model_result = self.model_current_project.getModelResult()     

    def getView(self):
        return self.view_menu_result_table

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
        
    # ::::::::::::::::::::      SLOT PAGE TABLE     ::::::::::::::::::::
    @Slot()
    def signalTableSearchPoint(self):        
        ids_point = self.view_menu_result_table.getIdPointSearch()
        self.signal_table_search_point.emit(ids_point)
        
    @Slot()
    def signalTableClear(self):
        self.signal_table_clear.emit()
        self.view_menu_result_table.clearLineEdit()
    
    @Slot(dict)
    def signalTableHiseShowColumn(self,dict_data):
        self.signal_table_hise_show_column.emit(dict_data)
        
    @Slot(str)
    def signalSaveData(self, path_data):
        graphic_times = self.model_result.getData()["GRAPHIC_TIME"]
        result_nodes = self.model_result.getData()["RESULT_NODES"]
        with open(path_data, 'w') as file:
            for data_node in result_nodes:
                dt = graphic_times
                
                corx = result_nodes[data_node]['CORX']
                cory = result_nodes[data_node]['CORY']    

                sigxx = result_nodes[data_node]['SIGXX']            
                sigyy = result_nodes[data_node]['SIGYY']            
                sigxy = result_nodes[data_node]['SIGXY']   

                epsxx = result_nodes[data_node]['EPSXX']            
                epsyy = result_nodes[data_node]['EPSYY']            
                epsxy = result_nodes[data_node]['EPSXY'] 
                file.write('NODO TIMEPO CORX CORY SIGXX SIGYY SIGXY EPSXX EPSYY EPSXY\n')
                for i in range(len(graphic_times)):
                    file.write(str(data_node)+' '+str(dt[i])+' '+str(corx[i])+' '+str(cory[i])+' '+str(sigxx[i])+' '+str(sigyy[i])+' '+str(sigxy[i])+' '+str(epsxx[i])+' '+str(epsyy[i])+' '+str(epsxy[i])+'\n')      
        # abrir archivo
        import subprocess
        subprocess.Popen([path_data], shell=True)

    @Slot(str)
    def signalGeneratePdf(self, path_pdf):
        
        # ::::::::::::::::::::      GENERAR PDF     ::::::::::::::::::::        
        print('Generando PDF')
        print(path_pdf)
        doc = SimpleDocTemplate(path_pdf, pagesize=letter)
        styles = getSampleStyleSheet()
        
        
        # ::::::::::::::::::::      ESTILOS     ::::::::::::::::::::
        
        # Definir un estilo personalizado para la tabla
        table_style = [('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),  # Tipo de fuente
                    ('FONTSIZE', (0, 0), (-1, -1), 8)]           # Tamaño de fuente
        table_style.append(('GRID', (0,0), (-1,-1), 1, (0,0,0)))   # Agregar bordes a la tabla
        
        '''
        align = 0 -> Izquierda
        align = 1 -> Centro
        align = 2 -> Derecha        
        '''
        # ESTILOS DE TITULOS
        title_styles = {
            "Title1": ParagraphStyle(
                "Title1",
                parent=styles["Title"],
                fontName='Times-bold',
                fontSize=30,
                spaceAfter=6,
                alignment=1,
                textColor= '#C8CC8E'
            ),
            "Title2": ParagraphStyle(
                "Title2",
                parent=styles["Title"],
                fontName='Times-bold',
                fontSize=20,
                spaceAfter=6,
                alignment=1,
                textColor= '#000000'
                
            ),
            "Title3": ParagraphStyle(
                "Title3",
                parent=styles["Title"],
                fontName='Times-bold',
                fontSize=16,
                spaceAfter=6,
                alignment=0,
                textColor= '#26a55d'                
            ),
        }
        
        # ESTILOS DE SUBTITULOS
        subtitle_styles = {
            "Subtitle1": ParagraphStyle(
                "Subtitle1",
                parent=styles["Heading1"],
                fontName='Times-bold',
                fontSize=16,
                spaceAfter=6,
                alignment=0,
                textColor= '#742427'
            ),
            "Subtitle2": ParagraphStyle(
                "Subtitle2",
                parent=styles["Heading1"],
                fontName='Times-bold',
                fontSize=14,
                spaceAfter=6,
                alignment=0,
                textColor= '#068d6c'
            ),
        }
        
        #estilos de parrafos
        '''
        align = 0 -> Izquierda
        align = 1 -> Centro
        align = 2 -> Derecha        
        '''
        paragraph_styles = {
            "Normal": ParagraphStyle(
                "Normal",
                parent=styles["Normal"],
                fontName='Times-Roman',
                fontSize=12,
                spaceAfter=6,
                alignment=0,
                textColor= '#333333'
            ),
        }
        
        # estilo simbolos
        symbol_styles = {
            "Symbol": ParagraphStyle(
                "Symbol",
                parent=styles["Normal"],
                fontName='Symbol',
                fontSize=12,
                spaceAfter=6,
                alignment=0,
                textColor= '#333333'
            ),
        }
        

        
                
   

        story = []
        
        '''
        #::::::::::::::::   EJEMPLO 3 TITULOs     ::::::::::::::::
        p = Paragraph("<b>Titulo 1</b>", title_styles["Title1"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))
        
        p = Paragraph("<b>Titulo 2</b>", title_styles["Title2"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))
        
        p = Paragraph("<b>Titulo 3</b>", title_styles["Title3"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))
        
        #::::::::::::::::   EJEMPLO 2 SUBTITULOs     ::::::::::::::::
        p = Paragraph("<b>Subtitulo 1</b>", subtitle_styles["Subtitle1"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))
        
        p = Paragraph("<b>Subtitulo 2</b>", subtitle_styles["Subtitle2"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))        
        
        #::::::::::::::::   EJEMPLO 1 PARAFRASO     ::::::::::::::::
        p = Paragraph("Parrafo de ejemplo", paragraph_styles["Normal"])
        story.append(p)
        story.append(Paragraph(" ", styles["Normal"]))
        '''
        
        
        
        

        #::::::::::::::::     Seccion inicial     :::::::::::::::: 
        
        # Titulo
        text = "MPM-UN"
        title = Paragraph("<b>"+text+"</b>", title_styles["Title1"])
        story.append(title)

        text = "INFORME DE ANÁLISIS"
        title = Paragraph("<b>"+text+"</b>", title_styles["Title2"])
        story.append(title)
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        
        # Parrafo introductorio
        text = "El presente informe muestra los resultados del análisis de un modelo del metodo del punto material, el cual fue realizado con el software <b>MPM-UN</b>. Del análisis se obtuvieron los resultados de desplazamientos, esfuerzos y deformaciones en los nodos del modelo. A continuación se presentan los resultados obtenidos."
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        
        #::::::::::::::::     Seccion de datos del proyecto     ::::::::::::::::
        
        #subtitulo
        text = "Información del proyecto"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        #nombre del proyecto
        text = "<b>Nombre del proyecto: </b><i>"+self.model_current_project.getName() +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        #localizacion
        text = "<b>Localización: </b><i>"+self.model_current_project.getLocation() +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        #autor
        text = "<b>Autor: </b><i>"+self.model_current_project.getAuthor() +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        #descripcion
        text = "<b>Descripción: </b><i>"+self.model_current_project.getDescription() +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        
        #fecha de creacion
        date = time.strftime("%d/%m/%Y")        
        text = "<b>Fecha de creación: </b><i>"+ date +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        #fin section
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        

        
        #::::::::::::::::     seccion de resultados     ::::::::::::::::
        '''
         "RESULTADOS": {
            "DATOSBASE": {
                "GRAVEDAD": 5.0,
                "DAMPFAC": 0.6
            },
        '''
        data_base = self.model_result.getDataBase()
        
        
        #subtitulo
        text = "Datos base del análisis"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        # agregar datos
        text = "<b>Gravedad: </b><i>"+str(data_base['GRAVEDAD']) +"</i> m/s^2"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Factor de amortiguamiento: </b><i>"+str(data_base['DAMPFAC']) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        story.append(Paragraph("<br/>", styles["Normal"]))
        
        # fin section
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        

        
         
        #::::::::::::::::     seccion de malla de fondo     ::::::::::::::::
        '''
                "MALLAFONDO": {
            "SIZEDX": 25.0,
            "SIZEDY": 20.0,
            "SIZEELEMENT": 1.0,
            "COLOR": 1,
            "POINTS": [
                [
                    0.0,
                    0.0
                ],
                [
                    1.0,
                    0.0
                ]...
            ],
            "QUADRILATERALS": [
                [
                    1,
                    2,
                    28,
                    27
                ],
                [
                    2,
                    3,
                    29,
                    28
                ]...
            ],
            "POINTSBOUNDARYBOTTOM": [
                [
                    0.0,
                    0.0
                ],               
                [
                    12.0,
                    0.0
                ]...
            ],
            "POINTSBOUNDARYLEFT": [
                [
                    0.0,
                    0.0
                ],
                [
                    0.0,
                    1.0
                ]...
            ],
            "POINTSBOUNDARYRIGHT": [
                [
                    25.0,
                    0.0
                ],
                [
                    25.0,
                    1.0
                ]...

            ],
            "NODESBOUNDARYTOP": [
                521,
                522,
                523,...
            ],
            "NODESBOUNDARYBOTTOM": [
                1,
                2,
                3...
            ],
            "NODESBOUNDARYLEFT": [
                1,
                27,
                53...
            ],
            "NODESBOUNDARYRIGHT": [
                26,
                52,
                78...
            ]
        },
        '''
        data_mesh = self.model_result.getMeshBack()
        

        '''
         def getData(self):
        """return: size_dx, size_dy, size_element, color, points, quadrilaterals, points_boundary_top, points_boundary_bottom, points_boundary_left, points_boundary_right, nodes_boundary_top, nodes_boundary_bottom, nodes_boundary_left, nodes_boundary_right]"""
        
        return[self.__size_dx, self.__size_dy, self.__size_element, self.__color_style, self.__points, self.__quadrilaterals, 
                self.points_boundary_top, self.points_boundary_bottom, self.points_boundary_left, self.points_boundary_right,
                self.nodes_boundary_top, self.nodes_boundary_bottom, self.nodes_boundary_left, self.nodes_boundary_right]
        '''
        
        #subtitulo
        text = "Malla de fondo"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        #agrergar datos
        text = "<b>Tamaño dx: </b><i>"+str(data_mesh[0]) +"</i> m"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)

        text = "<b>Tamaño dy: </b><i>"+str(data_mesh[1]) +"</i> m"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Tamaño de elemento: </b><i>"+str(data_mesh[2]) +"</i> m"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Total de nodos: </b><i>"+str(len(data_mesh[ 4])) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Total de elementos: </b><i>"+str(len(data_mesh[ 5])) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        # fin section
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        
       # ::::::::::::::::::::      seccion de informacion para tiempo de analisis     ::::::::::::::::::::
        '''
            "DATOSTIEMPOS": {
            "MATERIAL": "1faa8b86-1cfa-448e-8510-1132ff5bc7a2",
            "NUMEROCOURANT": 0.5,
            "TIEMPOANALISIS": 0.2,
            "FPS": 30,
            "DTANALISIS": 0.04,
            "DTGRAFICAR": 0.04,
            "PASOSANALISIS": 5,
            "PASOSGRAFICAR": 5,
            "VELOCIDADCP": 11.602387022306427,
            "TIEMPOALCANZADO": 0.16
        },
        

        data_times {
        'MATERIAL': '1faa8b86-1cfa-448e-8510-1132ff5bc7a2',
        'NUMEROCOURANT': 0.5, 'TIEMPOANALISIS': 0.2, 
        'FPS': 30,
        'DTANALISIS': 0.04, 
        'DTGRAFICAR': 0.04,
        'PASOSANALISIS': 5,
        'PASOSGRAFICAR': 5,
        'VELOCIDADCP': 11.602387022306427,
        'TIEMPOALCANZADO': 0.16}
        '''
        data_times = self.model_result.getDataTimes()
        
        #subtitulo
        text = "Datos de tiempo de análisis"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        #agrergar datos
        
        id_property =  data_times['MATERIAL']   
        name_property = self.model_result.getProperties()[id_property]['NAME']
        
        
        text = "<b>Material: </b><i>{} [id:{}]</i>".format(name_property, id_property)
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Velocidad de la onda de compresión: </b><i>{:.2f}</i> m/s".format(data_times['VELOCIDADCP'])
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Número Courant: </b><i>"+str(data_times['NUMEROCOURANT']) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Tiempo de análisis: </b><i>"+str(data_times['TIEMPOANALISIS']) +"</i> s"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>FPS: </b><i>"+str(data_times['FPS']) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>DT de análisis: </b><i>"+str(data_times['DTANALISIS']) +"</i> s"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>DT de graficar: </b><i>"+str(data_times['DTGRAFICAR']) +"</i> s"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Pasos de análisis: </b><i>"+str(data_times['PASOSANALISIS']) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        text = "<b>Pasos de graficar: </b><i>"+str(data_times['PASOSGRAFICAR']) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        

        
        text = "<b>Tiempo alcanzado: </b><i>"+str(data_times['TIEMPOALCANZADO']) +"</i> s"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
                
        # fin section        
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
       

        #::::::::::::::::     seccion de tiempos de analisis y graficar     ::::::::::::::::        
        data_times_analysis = self.model_result.getAnalysisTimes()
        data_times_graphics = self.model_result.getGrapihcsTimes()
        
        #subtitulo
        text = "Tiempo de análisis"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        text = "{}".format(data_times_analysis)
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
        
        
        #subtitulo
        text = "Tiempo para graficar"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        text = "{}".format(data_times_graphics)
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        
             
        #::::::::::::::::     seccion de materiales     ::::::::::::::::
        '''
        "MATERIALES": {
            "1faa8b86-1cfa-448e-8510-1132ff5bc7a2": {
                "NAME": "Barra",
                "MODULOELASTICIDAD": 0.1,
                "RELACIONPOISSON": 0.3,
                "COHESION": 5.0,
                "ANGULOFRICCION": 5.0,
                "DENSIDAD": 1.0,
                "ANGULODILATANCIA": 5.0
            },
            "1faa8b86-1cfa-448e-8510-1132ff5bc7a2": {
                "NAME": "Barra",
                "MODULOELASTICIDAD": 0.1,
                "RELACIONPOISSON": 0.3,
                "COHESION": 5.0,
                "ANGULOFRICCION": 5.0,
                "DENSIDAD": 1.0,
                "ANGULODILATANCIA": 5.0
            }
        },
        '''
        data_properties = self.model_result.getProperties()
        
        
        #subtitulo
        text = "Propiedades de los materiales"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        #parrafo total de materiales
        text = "<b>Total de materiales: </b><i>"+str(len(data_properties)) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
                
        
        # agregar datos
        data = [['id material', 'Nombre', 'E (KPa)', 'ν', 'C (KPa)', 'φ (°)', 'ρ (kg/m^3)', 'ψ (°)']]
        for material in data_properties:
            data.append([str(material), str(data_properties[material]['NAME']),
                         str(data_properties[material]['MODULOELASTICIDAD']), str(data_properties[material]['RELACIONPOISSON']), str(data_properties[material]['COHESION']), str(data_properties[material]['ANGULOFRICCION']), str(data_properties[material]['DENSIDAD']), str(data_properties[material]['ANGULODILATANCIA'])])
        table  = Table(data, style=table_style)
        story.append(table )
        
        # fin section
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        
        #::::::::::::::::     seccion de puntos materiales     ::::::::::::::::
        '''
        "PUNTOSMATERIAL": {
            "8d0f3c0f-b6ea-4db4-b646-1d521255f366": {
                "NAME": "Barra",
                "COLOR": "#190421",
                "POINTS": [
                    [
                        1.25,
                        11.25
                    ],
                    [
                        3.75,
                        11.25
                    ],
                    [
                        6.25,
                        11.25
                    ],
                    [
                        8.75,
                        11.25
                    ],
                    [
                        11.25,
                        11.25
                    ],
                    [
                        13.75,
                        11.25
                    ],
                    [
                        16.25,
                        11.25
                    ],
                    [
                        18.75,
                        11.25
                    ],
                    [
                        21.25,
                        11.25
                    ],
                    [
                        23.75,
                        11.25
                    ]
                ],
                "IDPROPIEDAD": "1faa8b86-1cfa-448e-8510-1132ff5bc7a2"
            }
        },
        '''
        
        data_material_points = self.model_result.getPointMaterials()
        
        #subtitulo
        
        text = "Puntos materiales"
        subtitle = Paragraph("<b>"+text+"</b>", subtitle_styles["Subtitle1"])
        story.append(subtitle)
        
        #parrafo total de puntos materiales
        text = "<b>Total de puntos materiales: </b><i>"+str(len(data_material_points)) +"</i>"
        paragraph = Paragraph(text, paragraph_styles["Normal"])
        story.append(paragraph)
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        #agregar datos
        data = [['id punto','Nombre','id Material', 'Material',]]
        for material in data_material_points:
            data.append([str(material), 
                         str(data_material_points[material]['NAME']), 
                         str(data_material_points[material]['IDPROPIEDAD']), 
                            str(data_properties[data_material_points[material]['IDPROPIEDAD']]['NAME'])])
        table  = Table(data, style=table_style)
        story.append(table )
        
        
        color_mp = data_material_points[material]['COLOR']
        data = [['puntos']]
        i = 0
        for material in data_material_points:
            data.append([str(data_material_points[material]['POINTS'])])
            #print(data)
            #print(type(data))
            i += 1
        table  = Table(data, style=table_style)
        story.append(table )
        
        
        # fin section
        story.append(Paragraph("<br/><br/>", styles["Normal"]))
        
        #::::::::::::::::     seccion de condiciones de frontera     ::::::::::::::::
        
        
        

   
        
        
        # Imagen
        fig, ax = plt.subplots()
        x = np.linspace(0, 2*np.pi, 100)
        ax.plot(x, np.sin(x))
        ax.set_title('Gráfico de ejemplo')
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Amplitud')
        fig.savefig("temp.png")
        im = Image("temp.png", 5, 2)
        story.append(im)
        story.append(Paragraph("<br/>", styles["Normal"]))
        
        # Tabla
        data = [['Nodo', 'Tiempo', 'Corx', 'Cory', 'Sigxx', 'Sigyy', 'Sigxy', 'Epsxx', 'Epsyy', 'Epsxy']]
        graphic_times = self.model_result.getGrapihcsTimes()
        result_nodes = self.model_result.getResultNodes()
        max = 10
        i = 0
        for data_node in result_nodes:
            dt = graphic_times
            corx = result_nodes[data_node]['CORX']
            cory = result_nodes[data_node]['CORY']    

            sigxx = result_nodes[data_node]['SIGXX']            
            sigyy = result_nodes[data_node]['SIGYY']            
            sigxy = result_nodes[data_node]['SIGXY']   

            epsxx = result_nodes[data_node]['EPSXX']            
            epsyy = result_nodes[data_node]['EPSYY']            
            epsxy = result_nodes[data_node]['EPSXY'] 
            

            for i in range(len(graphic_times)):
                if i > max:
                    break
                #data.append([str(data_node), str(dt[i]), str(corx[i]), str(cory[i]), str(sigxx[i]), str(sigyy[i]), str(sigxy[i]), str(epsxx[i]), str(epsyy[i]), str(epsxy[i])])
                #convertir a numero cientifico con dos decimales y despues a string
                corx_str = "{:.2e}".format(corx[i])
                cory_str = "{:.2e}".format(cory[i])
                sigxx_str = "{:.2e}".format(sigxx[i])
                sigyy_str = "{:.2e}".format(sigyy[i])
                sigxy_str = "{:.2e}".format(sigxy[i])

                epsxx_str = "{:.2e}".format(epsxx[i])
                epsyy_str = "{:.2e}".format(epsyy[i])
                epsxy_str = "{:.2e}".format(epsxy[i])
                data.append([str(data_node), str(dt[i]), corx_str, cory_str, sigxx_str, sigyy_str, sigxy_str, epsxx_str, epsyy_str, epsxy_str])
                

                
                
        table  = Table(data, style=table_style)
        story.append(table )
        story.append(Paragraph("<br/>", styles["Normal"]))
        
        # Cierre
        doc.build(story)
        print('PDF generado')
        
        #abrir pdf
        import subprocess
        subprocess.Popen([path_pdf], shell=True)
        
        