""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize)
from PySide6.QtGui import (QAction,QIcon, QFont, QColor)
from PySide6.QtWidgets import (QFileDialog, QMenu, QFrame, QSpacerItem, QSizePolicy,QColorDialog)
from ui.ui_widget_result_menu_table import Ui_FormMenuResultTable
from clases import class_general


class ViewWidgetResultMenuTable(QFrame, Ui_FormMenuResultTable):

    signal_table_search_point = Signal()
    signal_table_clear = Signal()
    signal_table_hise_show_column = Signal(dict)
    signal_save_data = Signal(str) 
    
    def __init__(self):

        super(ViewWidgetResultMenuTable, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_result_animation=True
        self.__hide_show_frame_result_animation_0=True
        self.__hide_show_frame_result_animation_1=True        

        # Configura la UI
        self.__configUi()
        self.__initEventUi()
               

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_mesh = QIcon()
        self.icon_show_mesh.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_mesh = QIcon()
        self.icon_hide_mesh.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('TABLA RESUMEN')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
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
        
    def __initEventUi(self):
    
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardResultAnimationSubTitle1.clicked.connect(self.__clickedToolButtonCardResultAnimationSubTitle1)
        
        # ::::::::::::::::::::      EVENTOS RESULT MENU GRAPH    ::::::::::::::::::::
        self.pushButton_ClearTable.clicked.connect(self.__clickedToolButtonClearTable)
        self.lineEdit_tableSearchByPointId.textEdited.connect(self.__textEditedLineEditTableSearchByPointId)
        self.menu_tableHideShowColumn.triggered.connect(self.__triggeredMenuTableHideShowColumn)
        self.pushButton_SaveData.clicked.connect(self.__clickedToolButtonSaveData)
      
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     :::::::::::::::::::: 
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """
        if self.__hide_show_frame_result_animation == True:
            self.frame_ResultAnimation.setVisible(False)
            self.__hide_show_frame_result_animation = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_result_animation == False:
            self.frame_ResultAnimation.setVisible(True)
            self.__hide_show_frame_result_animation = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)

    def __clickedToolButtonCardResultAnimationSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_result_animation_1 == True:
            self.frame_ResultAnimation1.setVisible(False)
            self.__hide_show_frame_result_animation_1 = False
            self.toolButton_cardResultAnimationSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_result_animation_1 == False:
            self.frame_ResultAnimation1.setVisible(True)
            self.__hide_show_frame_result_animation_1 = True
            self.toolButton_cardResultAnimationSubTitle1.setIcon(self.icon_minimize)

    # ::::::::::::::::::::      EVENTOS PAGE TABLE     ::::::::::::::::::::

    def __clickedToolButtonClearTable(self):
        self.signal_table_clear.emit()
        
    def __textEditedLineEditTableSearchByPointId(self):
        self.signal_table_search_point.emit()
        
    def __triggeredMenuTableHideShowColumn(self, action):
        column_select = action.data()
        
        if column_select == 10: 
            for action in self.menu_tableHideShowColumn.actions():
                action.setChecked(True)
        
        self.signal_table_hise_show_column.emit({'column':column_select, 'checked':action.isChecked()})
    
    def __clickedToolButtonSaveData(self):
        #abri dialogo para guardar csv
        options = QFileDialog.Options()
        new_path_file, _ = QFileDialog.getSaveFileName(self,"Exportar datos","","Archivos CSV (*.csv)", options=options)
        if new_path_file:
            self.signal_save_data.emit(new_path_file)     
    
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getIdPointSearch(self):
        return self.lineEdit_tableSearchByPointId.text()

    ###############################################################################
	# ::::::::::::::::::::            OTROS MÉTODOS            ::::::::::::::::::::
	###############################################################################
    def clearLineEdit(self):
        self.lineEdit_tableSearchByPointId.setText('')