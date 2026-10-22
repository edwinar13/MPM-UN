
from PySide6.QtCore import (Qt,QMimeData)
from PySide6.QtWidgets import (QApplication, QFrame, QMenu,QTableWidgetItem,QHeaderView)
from PySide6.QtGui import (QActionGroup,QAction)
from ui.ui_frame_result import Ui_FormResult
from utils.general_functions import TABLE_COLUMNS, table_rows
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ViewPageResult(QFrame, Ui_FormResult):
 
    def __init__(self, parent = None, ):
        super(ViewPageResult, self).__init__(parent)
        self.setupUi(self)

        self.list_graphics=[]

        # Configura la UI
        self.__configUi()
        self.__initEventUi()
 
    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
    ###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """

        # ::::::::::   AJUSTA LA GRÁFICA  ::::::::::::
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)        
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout_chart.addWidget(self.canvas)
        self.title ="Coordenada X (m)"
        self.islabel = False
        self.setTitleChart(self.title)
        self.setLabelXChart("Tiempo")
        self.setLabelYChart(self.title)
 
        #:::::::::::::::::::   EVENTO HOVER   ::::::::::::::::::::::::::::::::::::
        def hover(event):
            # Si el ratón está dentro de los ejes
            if event.inaxes == self.ax and self.islabel:
                # Se obtiene la posición del ratón en coordenadas de datos
                x, y = event.xdata, event.ydata
                # Se actualiza la posición del texto
                self.ax.format_coord = lambda x, y: f'{self.title} → x={x:.2f}, y={y:.2f}'
                # Se actualiza el texto
                self.ax.set_title(self.ax.format_coord(x, y))
                # Se actualiza la gráfica
                self.canvas.draw()
            else:
                self.setTitleChart(self.title)                            
        # Se conecta el evento de movimiento del ratón con la función hover
        self.fig.canvas.mpl_connect('motion_notify_event', hover)
        
        # ::::::::::   AJUSTA LA TABLA DE RESUMEN  ::::::::::::      
        self.tableWidget_tableResult.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_tableResult.setColumnCount(len(TABLE_COLUMNS))
        self.tableWidget_tableResult.setHorizontalHeaderLabels(TABLE_COLUMNS)
        # 21 columnas: ancho según contenido y barra horizontal (Stretch las aplastaba)
        self.tableWidget_tableResult.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.copy_information = QApplication.clipboard()
        self.tabWidget.setCurrentIndex(0)
        

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """           

        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::   
        self.tabWidget.currentChanged.connect(self.__currentChangedTabWidget)
        self.tableWidget_tableResult.customContextMenuRequested.connect(self.__customContextMenuRequestedTableWidgetTableResult)
        
                  
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    # ::::::::::::::::::::      EVENTOS PAGE RESULT     ::::::::::::::::::::
    def __currentChangedTabWidget(self, index):
        
        self.drawMenuAnimation.setVisible(False)
        self.drawMenuGraph.setVisible(False)
        self.drawMenuTable.setVisible(False)
        if index == 0:
            self.drawMenuAnimation.setVisible(True)
        elif index == 1:
            self.drawMenuGraph.setVisible(True)
        elif index == 2:
            self.drawMenuTable.setVisible(True)
            
    # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
    def __customContextMenuRequestedTableWidgetTableResult(self, position):
        indices = self.tableWidget_tableResult.selectedIndexes()
        if indices:
            menu = QMenu()
            itemsGrupo = QActionGroup(self)
            itemsGrupo.setExclusive(True)            
            menu.addAction(QAction("Copiar todo", itemsGrupo))
            columns = [self.tableWidget_tableResult.horizontalHeaderItem(columna).text()
                        for columna in range(self.tableWidget_tableResult.columnCount())
                        if not self.tableWidget_tableResult.isColumnHidden(columna)]
            copy_single = menu.addMenu("Copiar individual") 
            for indice, item in enumerate(columns, start=0):
                accion = QAction(item, itemsGrupo)
                accion.setData(indice)                
                copy_single.addAction(accion)
            itemsGrupo.triggered.connect(self.copyTableWidgetItem)            
            menu.exec(self.tableWidget_tableResult.viewport().mapToGlobal(position))

 

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    
    def setViewGraphicsWidget(self, view_graphics):         
        self.verticalLayout_pointMaterial.addWidget(view_graphics)        
                  
    def setMenuWidget(self, menu, view_menu):
        
        if menu == "animation":
            self.drawMenuAnimation = view_menu
            self.horizontalLayout_result.addWidget(self.drawMenuAnimation)
            self.drawMenuAnimation.setVisible(True)

        elif menu == "graph":
            self.drawMenuGraph = view_menu
            self.horizontalLayout_result.addWidget(self.drawMenuGraph)
            self.drawMenuGraph.setVisible(False)

        elif menu == "summary_table":
            self.drawMenuTable = view_menu
            self.horizontalLayout_result.addWidget(self.drawMenuTable)
            self.drawMenuTable.setVisible(False)
            
    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS  GENERALES CHART      ::::::::::::::::::::
	###############################################################################

    def setHideShowLabel(self, hide_show):
        self.islabel = hide_show
        if not hide_show:            
            self.setTitleChart(self.title)
            self.canvas.draw()

    def setTitleChart(self, title:str): 
        self.title = title       
        self.ax.set_title(title, fontweight="bold")  # sin upper(): las unidades (m, m/s) cambian

    def setLabelXChart(self, label_x:str):
        self.ax.set_xlabel(label_x)

    def setLabelYChart(self, label_y:str):
        self.ax.set_ylabel(label_y)


    def setYAxisLimitsChart(self, ymin, ymax):
        self.ax.set_ylim(ymin, ymax)
        self.canvas.draw()
    
    def setXAxisLimitsChart(self, xmin, xmax):
        self.ax.set_xlim(xmin, xmax)
        self.canvas.draw()
  

    
    def setDatePointChart(self,x, y, label_name:str):
        
        line, = self.ax.plot(x,y,label=label_name)   
        self.ax.legend(ncol=4)
        color = line.get_color()    
        self.list_graphics.append(line)
        return color
    
    def updateColorPointChart(self, id_point, color):
        for line in self.list_graphics:
            if id_point == line.get_label():
                line.set_color(color) 
        self.ax.legend(ncol=4)
        self.canvas.draw()

    def showPointChart(self, id_point, is_visible):
        for line in self.list_graphics:
            if id_point == line.get_label():                
                line.set_visible(is_visible)
        self.ax.legend(ncol=4)
        self.canvas.draw()
        
    def showAllPointChart(self, show_series):
        for line in self.list_graphics:               
            line.set_visible(show_series)
        self.ax.legend(ncol=4)
        self.canvas.draw()
        
    

    def deletePointChart(self, id_point):
        for line in self.list_graphics:
            if id_point == line.get_label():                
                self.list_graphics.remove(line)
                line.remove()
        if len(self.list_graphics)>0:
            self.ax.legend(ncol=4)
        else:
            self.ax.legend([])
        self.canvas.draw()
        
    def deleteAllPointChart(self):
        for line in self.list_graphics:               
            line.remove()
        self.list_graphics.clear()
        self.ax.legend([])
        self.canvas.draw()

    def changeTypeResultChart(self, id_point, y_new):
        for line in self.list_graphics:
            if id_point == line.get_label():
                line.set_ydata( y_new)

    def changeLinesTypeChart(self, line_type):
        for line in self.list_graphics:    
            if line_type == "points":
                line.set_linestyle(':')  # Línea sólida
                line.set_marker('')  # Elimina el marcador
            if line_type == "line":
                line.set_linestyle('-')  # Línea sólida
                line.set_marker('')  # Elimina el marcador
            elif line_type == "curve":
                line.set_linestyle('--')  # Línea sólida
                line.set_marker('')  # Círculos como puntos
                line.set_markevery(None)  # Elimina la opción markevery
            elif line_type == "circles":
                line.set_linestyle('-')  # Elimina la línea
                line.set_marker('o')  # Círculos como puntos
                line.set_markevery(True) 

        if len(self.list_graphics)>0:
            self.ax.legend(ncol=4)
        else:
            self.ax.legend([])
        self.canvas.draw()

    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS  GENERALES TABLE      ::::::::::::::::::::
	###############################################################################


    def clearViewTableResult(self):      
        self.tableWidget_tableResult.clearContents()
        self.tableWidget_tableResult.setRowCount(0)

    def updateViewTableResult(self, data, data_time=None):
        """Llena la tabla con los resultados de los nodos de `data` (vacío = limpiar)."""
        table = self.tableWidget_tableResult
        table.clearContents()
        rows = list(table_rows(data, data_time)) if data else []
        table.setRowCount(len(rows))
        for row, values in enumerate(rows):
            for column, value in enumerate(values):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                table.setItem(row, column, item)

    def copyTableWidgetItem(self, action):
        rows_selected = self.tableWidget_tableResult.selectedIndexes()

        if not rows_selected:
            return

        clipboard = QApplication.clipboard()
        mime_data = QMimeData()

        # Obtener los índices de fila de cada celda seleccionada
        row_indices = set(index.row() for index in rows_selected)

        data_by_row = {}  # Diccionario para agrupar los datos por fila

        for index in rows_selected:
            row = index.row()
            column = index.column()
            data = index.data(Qt.DisplayRole)  # Usar el rol Qt.DisplayRole para obtener el texto visible

            if row not in data_by_row:
                data_by_row[row] = []

            data_by_row[row].append((column, data))

        selected_data = ""

        for row in sorted(data_by_row.keys()):
            # Ordenar los datos en cada fila según la columna
            sorted_data = sorted(data_by_row[row], key=lambda x: x[0])
            row_data = "\t".join(str(data) for _, data in sorted_data)
            selected_data += row_data + "\n"

        mime_data.setText(selected_data)
        clipboard.setMimeData(mime_data)
       
    def hideShowColumnTable(self, dict_data):
        column_select = dict_data['column']
        cheked = dict_data['checked']
        
        if column_select == -1:  # mostrar todas
            for column in range(len(TABLE_COLUMNS)):
                self.tableWidget_tableResult.setColumnHidden(column, False)
        else:            
            self.tableWidget_tableResult.setColumnHidden(column_select, not cheked)
            
    def updateMenuResults(self):
        max = 1
        min = 0        
        self.setYAxisLimitsChart(min, max)
        self.setXAxisLimitsChart(min, max)
        
