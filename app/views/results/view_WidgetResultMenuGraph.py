""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import (QFrame, QSpacerItem, QSizePolicy)
from ui.ui_widget_result_menu_graph import Ui_FormMenuResultGraph
from utils import class_general
from utils import general_functions

class ViewWidgetResultMenuGraph(QFrame, Ui_FormMenuResultGraph):

    signal_chart_add_card = Signal()
    signal_chart_type_result = Signal()
    signal_chart_type_style = Signal()
    signal_show_hide_series = Signal(bool)
    signal_show_hide_label = Signal(bool)
    signal_delete_series = Signal()
    

    signal_max_min = Signal(list)
    signal_update_limit = Signal()
    

    
    def __init__(self):

        super(ViewWidgetResultMenuGraph, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_result_animation=True
        self.__hide_show_frame_result_animation_0=True
        self.__hide_show_frame_result_animation_1=True        
        
        self.__hide_show_series=True
        self.__hide_show_label=False
        self.list_view_card =[]

        # Configura la UI
        self.__configUi()
        self.__initEventUi()
               

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"app/resources/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_mesh = QIcon()
        self.icon_show_mesh.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_mesh = QIcon()
        self.icon_hide_mesh.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('GRAFICAS')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
        
       
    def __initEventUi(self):

    
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardResultAnimationSubTitle0.clicked.connect(self.__clickedToolButtonCardResultAnimationSubTitle0)
        self.toolButton_cardResultAnimationSubTitle1.clicked.connect(self.__clickedToolButtonCardResultAnimationSubTitle1)
        
        self.toolButton_showHideSeries.clicked.connect(self.__clickedToolButtonShowHideSeries)
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)
        self.toolButton_deleteSeries.clicked.connect(self.__clickedToolButtonDeleteSeries)
        
        self.radioButton_automatic.toggled.connect(self.__toggledRadioButtonModeLimits)
        self.radioButton_manual.toggled.connect(self.__toggledRadioButtonModeLimits)
        self.lineEdit_Xmin.editingFinished.connect(self.__editingFinishedLineEditMaxMin)
        self.lineEdit_Xmax.editingFinished.connect(self.__editingFinishedLineEditMaxMin)
        self.lineEdit_Ymin.editingFinished.connect(self.__editingFinishedLineEditMaxMin)
        self.lineEdit_Ymax.editingFinished.connect(self.__editingFinishedLineEditMaxMin)
        self.toolButton_updateLimit.clicked.connect(self.__clickedToolButtonUpdateLimit)
        
        # ::::::::::::::::::::      EVENTOS RESULT MENU GRAPH    ::::::::::::::::::::
        self.comboBox_chartTypeResult.currentIndexChanged.connect(self.__currentIndexChangedComboBoxChartTypeResult)
        self.toolButton_chartTypeStyle.clicked.connect(self.__clickedToolButtonChangeChartTypeStyle)
        self.toolButton_chartAddPoint.clicked.connect(self.__clickedToolButtonChartAddPoint)

      
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

    def __clickedToolButtonCardResultAnimationSubTitle0(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_result_animation_0 == True:
            self.frame_ResultAnimation0.setVisible(False)
            self.__hide_show_frame_result_animation_0 = False
            self.toolButton_cardResultAnimationSubTitle0.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_result_animation_0 == False:
            self.frame_ResultAnimation0.setVisible(True)
            self.__hide_show_frame_result_animation_0 = True
            self.toolButton_cardResultAnimationSubTitle0.setIcon(self.icon_minimize)

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
                                    
    def __clickedToolButtonShowHideSeries(self):
        if self.__hide_show_series == True:
            self.__hide_show_series = False
            self.signal_show_hide_series.emit(self.__hide_show_series)
            self.toolButton_showHideSeries.setIcon(self.icon_hide_mesh)
        elif self.__hide_show_series == False:  
            self.__hide_show_series = True
            self.signal_show_hide_series.emit(self.__hide_show_series)
            self.toolButton_showHideSeries.setIcon(self.icon_show_mesh)
            
    def __clickedToolButtonShowHideLabel(self):
        if self.__hide_show_label == True:
            self.__hide_show_label = False
            self.signal_show_hide_label.emit(self.__hide_show_label)
            self.toolButton_showHideLabel.setIcon(self.icon_hide_label)
        elif self.__hide_show_label == False:
            self.__hide_show_label = True
            self.signal_show_hide_label.emit(self.__hide_show_label)
            self.toolButton_showHideLabel.setIcon(self.icon_show_label)
            
    def __clickedToolButtonDeleteSeries(self):
        self.signal_delete_series.emit()
    
    
    
    
    def __toggledRadioButtonModeLimits(self):
        is_cheked_aut = self.radioButton_automatic.isChecked()
        is_cheked_manu = self.radioButton_manual.isChecked()
        if is_cheked_aut:
            self.toolButton_updateLimit.setEnabled(True)
            self.lineEdit_Xmin.setEnabled(False)
            self.lineEdit_Xmax.setEnabled(False)
            self.lineEdit_Ymin.setEnabled(False)
            self.lineEdit_Ymax.setEnabled(False)
        elif is_cheked_manu:
            self.toolButton_updateLimit.setEnabled(False)            
            self.lineEdit_Xmin.setEnabled(True)
            self.lineEdit_Xmax.setEnabled(True)
            self.lineEdit_Ymin.setEnabled(True)
            self.lineEdit_Ymax.setEnabled(True)
            
            
            
        
        
    def __editingFinishedLineEditMaxMin(self):        
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza el valor       
        si no es número retorno""" 

        input_lines = [
            self.lineEdit_Xmin,
            self.lineEdit_Xmax,
            self.lineEdit_Ymin,
            self.lineEdit_Ymax]
        limits =[]
        for input_line in input_lines:            
            data = input_line.text()            
            if general_functions.isNumber(data):
                limits.append(float(data))
                input_line.setText(str(float(data)))            
                input_line.setStyleSheet("border-color: #444444")   
                    
            else:            
                input_line.setFocus()
                input_line.setStyleSheet("border: 1px solid #F94646")  
                return
                
        #verificar que los minimos sean menores a los maximos 
        if limits[0] >= limits[1]:
            input_lines[0].setStyleSheet("border: 1px solid #F94646")  
            input_lines[1].setStyleSheet("border: 1px solid #F94646")  
            return
        
        if limits[2] >= limits[3]:
            input_lines[2].setStyleSheet("border: 1px solid #F94646")  
            input_lines[3].setStyleSheet("border: 1px solid #F94646")  
            return
            
                        
        self.signal_max_min.emit(limits)
        
    def __clickedToolButtonUpdateLimit(self):
        self.signal_update_limit.emit()
        
    

    
    
    def __currentIndexChangedComboBoxChartTypeResult(self):
        self.signal_chart_type_result.emit()

    def __clickedToolButtonChangeChartTypeStyle(self):
        self.signal_chart_type_style.emit()

    def __clickedToolButtonChartAddPoint(self):
        self.signal_chart_add_card.emit()
            
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      GET/SET PAGE CHART     ::::::::::::::::::::
    def getIdPointGraphics(self):
        return self.lineEdit_chartPointName.text()
    
    def getTypeResult(self):
        return self.comboBox_chartTypeResult.currentText()    

    ###############################################################################
	# ::::::::::::::::::::            OTROS MÉTODOS            ::::::::::::::::::::
	###############################################################################
    def addCardPoint(self, card_point):        
        self.verticalLayout_containerCardPoint.insertWidget(0,card_point)
        self.list_view_card.append(card_point)

    def resetTypeResult(self):
        self.comboBox_chartTypeResult.setCurrentIndex(0)