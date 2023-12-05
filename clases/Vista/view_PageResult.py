
from PySide6.QtCore import (Signal,QRectF,Qt,QPointF, QLineF,QSize,QEvent,Slot,QMimeData)
from PySide6.QtWidgets import (QApplication, QVBoxLayout,QGraphicsRectItem, QGraphicsLineItem, QFrame, QGraphicsScene,QGraphicsView,QGraphicsItem,
                            QGraphicsPolygonItem,QMenu,QTableWidgetItem,QHeaderView, QSplitter,QDockWidget, QGraphicsItemGroup, QFileDialog)
from PySide6.QtGui import (QColor, QPen,QBrush,QClipboard,QActionGroup,
                            QPainter,QPixmap,QPolygonF,
                            QPainterPath,QFont,
                            QKeyEvent,QShortcut, QKeySequence,
                            QFocusEvent,QIcon,QUndoStack,QAction,QUndoCommand,QTransform)
from ui.ui_frame_result import Ui_FormResult
from clases.Vista.view_GraphicsDraw import PointItem,LineItem,TextItem
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class ViewPageResult(QFrame, Ui_FormResult):
    """Esta clase crea el QFrame draw para agregarlo a main window. """ 

    signal_scene_type_result = Signal()
    signal_scene_regress = Signal()
    signal_scene_stop = Signal()    
    signal_scene_play = Signal()    
    signal_scene_advance = Signal()

    signal_chart_add_card = Signal()
    signal_chart_type_result = Signal()
    signal_chart_type_style = Signal()

    signal_table_search_point = Signal()
    signal_table_all_point = Signal()
 
    def __init__(self, parent = None, ):
        super(ViewPageResult, self).__init__(parent)
        self.setupUi(self)

        self.list_view_card =[]
        self.list_graphics=[]

        # Configura la UI
        self.__configUi()
        self.__initEventUi()
 
    ###############################################################################
    # ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
    ###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """

        # ::::::::::   AJUSTA LA ESCENA  ::::::::::::
        self.icon_play = QIcon()
        self.icon_play.addFile(u"recursos/iconos/icono_result/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_pause = QIcon()
        self.icon_pause.addFile(u"recursos/iconos/icono_result/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # ::::::::::   AJUSTA LA GRÁFICA  ::::::::::::
        self.fig, self.ax = plt.subplots()
        self.ax.grid(True)        
        self.canvas = FigureCanvas(self.fig)
        self.verticalLayout_chart.addWidget(self.canvas)
        self.setTitleChart("Coordenada X")
        self.setLabelXChart("Tiempo (??)")
        self.setLabelYChart("Desplazamiento (??)")

        # ::::::::::   AJUSTA LA TABLA DE RESUMEN  ::::::::::::
        result_column_names = ('ID Nodo', 'dt', 'cor x', 'cor y',
                                        'sigxx', 'sigyy', 'sigxy',
                                        'epsxx', 'epsyy', 'epsxy', 'Todos')
        self.menu_tableHideShowColumn = QMenu(self)
        for index, column in enumerate(result_column_names, start=0):
            action = QAction(column, self.menu_tableHideShowColumn)
            if index != 10:
                action.setCheckable(True)
                action.setChecked(True)
            else:
                self.menu_tableHideShowColumn.addSeparator()
            action.setData(index)
            self.menu_tableHideShowColumn.addAction(action)
        self.pushButton_tableShowHideColumn.setMenu(self.menu_tableHideShowColumn)
        self.tableWidget_tableResult.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tableWidget_tableResult.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget_tableResult.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        self.copy_information = QApplication.clipboard()

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """   
        # ::::::::::::::::::::      EVENTOS PAGE SCENE     ::::::::::::::::::::
        self.comboBox_sceneTypeResult.currentIndexChanged.connect(self.__currentIndexChangedComboBoxSceneTypeResult)
        self.toolButton_sceneRegress.clicked.connect(self.__clickedToolButtonSceneRegress)
        self.toolButton_scenePlay.clicked.connect(self.__clickedToolButtonScenePlay)
        self.toolButton_sceneStop.clicked.connect(self.__clickedToolButtonSceneStop)
        self.toolButton_sceneAdvance.clicked.connect(self.__clickedToolButtonSceneAdvance)
        
        # ::::::::::::::::::::      EVENTOS PAGE CHART     ::::::::::::::::::::
        self.comboBox_chartTypeResult.currentIndexChanged.connect(self.__currentIndexChangedComboBoxChartTypeResult)
        self.toolButton_chartTypeStyle.clicked.connect(self.__clickedToolButtonChangeChartTypeStyle)
        self.toolButton_chartAddPoint.clicked.connect(self.__clickedToolButtonChartAddPoint)

        # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
        self.lineEdit_tableSearchByPointId.textEdited.connect(self.__textEditedLineEditTableSearchByPointId)
        self.menu_tableHideShowColumn.triggered.connect(self.__triggeredMenuTableHideShowColumn)
        self.tableWidget_tableResult.customContextMenuRequested.connect(self.__customContextMenuRequestedTableWidgetTableResult)
        self.pushButton_tableSearchAllPoints.clicked.connect(self.__clickedToolButtonTableSearchAllPoints)
        
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    # ::::::::::::::::::::      EVENTOS PAGE SCENE     ::::::::::::::::::::
    def __currentIndexChangedComboBoxSceneTypeResult(self):
        self.signal_scene_type_result.emit()

    def __clickedToolButtonSceneRegress(self):
        self.signal_scene_regress.emit()
        
    def __clickedToolButtonSceneStop(self):
        self.signal_scene_stop.emit()

    def __clickedToolButtonScenePlay(self):
        self.signal_scene_play.emit()

    def __clickedToolButtonSceneAdvance(self):
        self.signal_scene_advance.emit()

    # ::::::::::::::::::::      EVENTOS PAGE CHART     ::::::::::::::::::::
    def __currentIndexChangedComboBoxChartTypeResult(self):
        self.signal_chart_type_result.emit()

    def __clickedToolButtonChangeChartTypeStyle(self):
        self.signal_chart_type_style.emit()

    def __clickedToolButtonChartAddPoint(self):
        self.signal_chart_add_card.emit()

    # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::
    def __textEditedLineEditTableSearchByPointId(self):
        self.signal_table_search_point.emit()

    def __triggeredMenuTableHideShowColumn(self, action):
        column_select = action.data()
        if column_select == 10: #mostrar todos 
            for column in range(0,10):
                self.tableWidget_tableResult.setColumnHidden(column, False)
            for action in self.menu_tableHideShowColumn.actions():
                action.setChecked(True)
        else:
            if action.isChecked():
                self.tableWidget_tableResult.setColumnHidden(column_select, False)
            else:
                self.tableWidget_tableResult.setColumnHidden(column_select, True)

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

    def __clickedToolButtonTableSearchAllPoints(self):
        self.signal_table_all_point.emit()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    # ::::::::::::::::::::      GET/SET PAGE SCENE     ::::::::::::::::::::
    def getTypeResultScene(self):
        return self.comboBox_sceneTypeResult.currentText()
    
    def setViewGraphicsWidget(self, view_graphics):         
        self.verticalLayout_pointMaterial.addWidget(view_graphics)        
    
    # ::::::::::::::::::::      GET/SET PAGE CHART     ::::::::::::::::::::
    def getIdPointGraphics(self):
        return self.lineEdit_chartPointName.text()
    
    def getTypeResult(self):
        return self.comboBox_chartTypeResult.currentText()
    
    # ::::::::::::::::::::      GET/SET  PAGE TABLE     ::::::::::::::::::::
    def getIdPointSearch(self):
        return self.lineEdit_tableSearchByPointId.text()




    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS  GENERALES SCENE      ::::::::::::::::::::
	###############################################################################

    def stopAnimation(self):
        self.toolButton_scenePlay.setIcon(self.icon_play)
        
    def playPauseAnimation(self, play):
        if play:            
            self.toolButton_scenePlay.setIcon(self.icon_pause)            
        else :            
            self.toolButton_scenePlay.setIcon(self.icon_play)   

    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS  GENERALES CHART      ::::::::::::::::::::
	###############################################################################

    def setTitleChart(self, title:str):        
        self.ax.set_title(title.upper(),fontweight ="bold")

    def setLabelXChart(self, label_x:str):
        self.ax.set_xlabel(label_x)

    def setLabelYChart(self, label_y:str):
        self.ax.set_ylabel(label_y)

    def setYAxisLimitsChart(self, ymin, ymax):
        self.ax.set_ylim(ymin, ymax)
        self.canvas.draw()
    
    def setDatePointChart(self,x, y, label_name:str):
        line, = self.ax.plot(x,y,label=label_name)   
        self.ax.legend()
        color = line.get_color()    
        self.list_graphics.append(line)
        return color
    
    def updateColorPointChart(self, id_point, color):
        for line in self.list_graphics:
            if id_point == line.get_label():
                line.set_color(color) 
        self.ax.legend()
        self.canvas.draw()

    def showPointChart(self, id_point, is_visible):
        for line in self.list_graphics:
            if id_point == line.get_label():                
                line.set_visible(is_visible)
        self.ax.legend()
        self.canvas.draw()

    def deletePointChart(self, id_point):
        for line in self.list_graphics:
            if id_point == line.get_label():                
                self.list_graphics.remove(line)
                line.remove()
        if len(self.list_graphics)>0:
            self.ax.legend()
        else:
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
                line.set_marker(None)  # Elimina el marcador
            if line_type == "line":
                line.set_linestyle('-')  # Línea sólida
                line.set_marker(None)  # Elimina el marcador
            elif line_type == "curve":
                line.set_linestyle('--')  # Línea sólida
                line.set_marker(None)  # Círculos como puntos
                line.set_markevery(None)  # Elimina la opción markevery
            elif line_type == "circles":
                line.set_linestyle('-')  # Elimina la línea
                line.set_marker('o')  # Círculos como puntos
                line.set_markevery(True) 

        if len(self.list_graphics)>0:
            self.ax.legend()
        else:
            self.ax.legend([])
        self.canvas.draw()

    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS  GENERALES TABLE      ::::::::::::::::::::
	###############################################################################

    def clearViewTableResult(self):      
        self.tableWidget_tableResult.clearContents()
        self.tableWidget_tableResult.setRowCount(0)

    def updateViewTableResult(self, data): 
        return     
        self.tableWidget_tableResult.clearContents()
        self.tableWidget_tableResult.setRowCount(0)
                  
        row = 0
        for data_node in data:
            dt = data[data_node]['TIEMPOS']
            corx = data[data_node]['CORX']
            cory = data[data_node]['CORY']    

            sigxx = data[data_node]['SIGXX']            
            sigyy = data[data_node]['SIGYY']            
            sigxy = data[data_node]['SIGXY']   

            epsxx = data[data_node]['EPSXX']            
            epsyy = data[data_node]['EPSYY']            
            epsxy = data[data_node]['EPSXY']                   
            
            for i in range(len(corx)):
                self.tableWidget_tableResult.setRowCount(row + 1)

                id_node = QTableWidgetItem(data_node)
                id_node.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 0, id_node)

                dt_i = QTableWidgetItem("{:.6e}".format(dt[i]))
                dt_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 1, dt_i)

                corx_i = QTableWidgetItem("{:.10e}".format(corx[i]))
                corx_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 2, corx_i)

                cory_i = QTableWidgetItem("{:.10e}".format(cory[i]))
                cory_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 3, cory_i)

                sigxx_i = QTableWidgetItem("{:.10e}".format(sigxx[i]))
                sigxx_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 4, sigxx_i)

                sigyy_i = QTableWidgetItem("{:.10e}".format(sigyy[i]))
                sigyy_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 5, sigyy_i)

                sigxy_i = QTableWidgetItem("{:.10e}".format(sigxy[i]))
                sigxy_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 6, sigxy_i)

                epsxx_i = QTableWidgetItem("{:.10e}".format(epsxx[i]))
                epsxx_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 7, epsxx_i)

                epsyy_i = QTableWidgetItem("{:.10e}".format(epsyy[i]))
                epsyy_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 8, epsyy_i)

                epsxy_i = QTableWidgetItem("{:.10e}".format(epsxy[i]))
                epsxy_i.setTextAlignment(Qt.AlignCenter)
                self.tableWidget_tableResult.setItem(row, 9, epsxy_i)

                row += 1
    
    def clearLineEdit(self):
        self.lineEdit_tableSearchByPointId.setText('')

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

    def addCardPoint(self, card_point):
        
        self.verticalLayout_containerCardPoint.insertWidget(0,card_point)
        self.list_view_card.append(card_point)
        return
        last_index = self.verticalLayout_containerCardPoint.count() - 1
        self.verticalLayout_containerCardPoint.insertWidget(last_index, self.frame_empt)
        last_index = self.verticalLayout_containerCardPoint.count() - 1
        self.verticalLayout_containerCardPoint.insertWidget(last_index, self.verticalSpacer)


