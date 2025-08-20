""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize,QTimer, Qt)
from PySide6.QtGui import (QIcon, QFont,QTransform, QPen, QBrush, QPolygonF, QColor, QPalette)
from PySide6.QtWidgets import ( QLabel,QFrame, QSpacerItem, QSizePolicy,QColorDialog)
from ui.ui_widget_result_menu_animation import Ui_FormMenuResultAnimation
from utils import class_general


class ViewWidgetResultMenuAnimation(QFrame, Ui_FormMenuResultAnimation):
    """Esta clase crea el QFrame draw-menu-resulta-animation para agregarlo a Frame Result.
    """ 
    signal_result_animation_color_styles = Signal()
    signal_result_animation_grid = Signal()
    signal_result_animation_axis = Signal()
    signal_result_animation_label = Signal()
    signal_result_animation_values_text = Signal()
    signal_result_animation_size_points = Signal()
    signal_result_animation_size_texts = Signal()    
 
    signal_scene_type_result = Signal()
    signal_scene_regress = Signal()
    signal_scene_stop = Signal()    
    signal_scene_play = Signal()    
    signal_scene_advance = Signal()
    signal_scene_animation_velocity = Signal()
    
    def __init__(self):

        super(ViewWidgetResultMenuAnimation, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_result_animation=True
        self.__hide_show_frame_result_animation_0=True
        self.__hide_show_frame_result_animation_1=True
        
        self.__color_custom_hue = 0
        self.color_style = 0 # 0: Para Puntos 1: Para resultados



        
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
        self.label_lat = class_general.QLabelVertical('ANIMACIONES')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

        # agregar a comboBox_sceneTypeResult los item
        self.comboBox_sceneTypeResult.addItem("Default")
        self.comboBox_sceneTypeResult.addItem("DESPL→Desplazamiento")
        self.comboBox_sceneTypeResult.addItem("VEL→Velocidad")
        self.comboBox_sceneTypeResult.addItem("SIG→Esfuerzo")
        self.comboBox_sceneTypeResult.addItem("EPSP→Def. plástica")
        self.comboBox_sceneTypeResult.addItem("EPSE→Def. elástica")
        self.comboBox_sceneTypeResult.addItem("EQPLAS→Def. plástica eq")  

           

        self.comboBox_ResultAnimationColorStyles_Puntos.addItem("Material")
        self.comboBox_ResultAnimationColorStyles_Puntos.addItem("Bicolor")
        self.comboBox_ResultAnimationColorStyles_Resultados.addItem("Rojo-Azul")
        self.comboBox_ResultAnimationColorStyles_Resultados.addItem("Escala de grises")
        self.comboBox_ResultAnimationColorStyles_Resultados.addItem("Escala color")  
        self.showStyleColor(0)
        
        self.lineEdit_textColor.setAlignment(Qt.AlignCenter)
        self.setColor(0)
        
        # ::::::::::   AJUSTA LA ESCENA  ::::::::::::
        self.icon_play = QIcon()
        self.icon_play.addFile(u"app/resources/iconos/icono_result/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_pause = QIcon()
        self.icon_pause.addFile(u"app/resources/iconos/icono_result/pause.svg", QSize(), QIcon.Normal, QIcon.Off)
        

        
    def __initEventUi(self):    
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardResultAnimationSubTitle0.clicked.connect(self.__clickedToolButtonCardResultAnimationSubTitle0)
        self.toolButton_cardResultAnimationSubTitle1.clicked.connect(self.__clickedToolButtonCardResultAnimationSubTitle1)
        
        # ::::::::::::::::::::      EVENTOS RESULT MENU ANIMATION    ::::::::::::::::::::
        self.comboBox_sceneTypeResult.currentIndexChanged.connect(self.__currentIndexChangedComboBoxSceneTypeResult)
        self.radioButton_ResultX.clicked.connect(self._currentIndexChangedComboBoxSceneAxisResult)
        self.radioButton_ResultY.clicked.connect(self._currentIndexChangedComboBoxSceneAxisResult)
        self.radioButton_ResultXY.clicked.connect(self._currentIndexChangedComboBoxSceneAxisResult)
        self.checkBox_ResultVector.stateChanged.connect(self.__stateChangedCheckBoxResultVector)
        self.spinBox_ResultAnimationVelocity.valueChanged.connect(self.__valueChangedDoubleSpinBoxlTextResultAnimationVelocity)  
        self.toolButton_sceneRegress.clicked.connect(self.__clickedToolButtonSceneRegress)
        self.toolButton_scenePlay.clicked.connect(self.__clickedToolButtonScenePlay)
        self.toolButton_sceneStop.clicked.connect(self.__clickedToolButtonSceneStop)
        self.toolButton_sceneAdvance.clicked.connect(self.__clickedToolButtonSceneAdvance)


        self.comboBox_ResultAnimationColorStyles_Puntos.currentIndexChanged.connect(self.__currentIndexChangedComboBoxResultAnimationColorStylesPoints)
        self.comboBox_ResultAnimationColorStyles_Resultados.currentIndexChanged.connect(self.__currentIndexChangedComboBoxResultAnimationColorStylesResults)
        self.btn_select_color.clicked.connect(self.__clickedToolButtonSelectColor)
        self.checkBox_ResultAnimationGrid.stateChanged.connect(self.__stateChangedCheckBoxResultAnimationGrid)
        self.checkBox_ResultAnimationCountour.stateChanged.connect(self.__stateChangedCheckBoxResultAnimationCountour)   
        self.checkBox_ResultAnimationLabel.stateChanged.connect(self.__stateChangedCheckBoxResultAnimationLabel)
        self.checkBox_ResultAnimationValues.stateChanged.connect(self.__valueChangedcheckBoxResultAnimationValuesText)
        self.doubleSpinBoxl_textResultAnimationSizePoints.valueChanged.connect(self.__valueChangedDoubleSpinBoxlTextResultAnimationSizePoints)
        self.spinBox_ResultAnimationSizeText.valueChanged.connect(self.__valueChangedSpinBoxlTextResultAnimationSizeTexts) 
          
                
        
      
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

    # ::::::::::::::::::::      EVENTOS RESULT MENU STYLES ANIMATION    ::::::::::::::::::::


    def __currentIndexChangedComboBoxResultAnimationColorStylesResults(self):
        index_selected = self.comboBox_ResultAnimationColorStyles_Resultados.currentIndex()
        self.setColor(index_selected) 
        self.signal_result_animation_color_styles.emit()


    def __currentIndexChangedComboBoxResultAnimationColorStylesPoints(self):
        index_selected = self.comboBox_ResultAnimationColorStyles_Puntos.currentIndex()
        self.setColor(index_selected) 
        self.signal_result_animation_color_styles.emit()

        
    def __clickedToolButtonSelectColor(self):
        color = QColorDialog.getColor(initial=QColor(255,0,0))
        if color.isValid():                                    
            color_hsv = color.getHsv()
            hue = color_hsv[0]
            self.__color_custom_hue = hue    
            self.setColor(index=2, color_input=color.name())            
            self.signal_result_animation_color_styles.emit()
        
    
    def __stateChangedCheckBoxResultAnimationGrid(self):
        self.signal_result_animation_grid.emit()
    
    def __stateChangedCheckBoxResultAnimationCountour(self):
        self.signal_result_animation_axis.emit()   
    
    def __stateChangedCheckBoxResultAnimationLabel(self):
        self.signal_result_animation_label.emit()
    
    def __valueChangedcheckBoxResultAnimationValuesText(self):
        self.signal_result_animation_values_text.emit()
        
    def __valueChangedDoubleSpinBoxlTextResultAnimationSizePoints(self):        
        self.signal_result_animation_size_points.emit()
        
    def __valueChangedSpinBoxlTextResultAnimationSizeTexts(self):
        self.signal_result_animation_size_texts.emit()

    # ::::::::::::::::::::      EVENTOS RESULT MENU DATA ANIMATION    ::::::::::::::::::::
    
    def __valueChangedDoubleSpinBoxlTextResultAnimationVelocity(self):
        self.signal_scene_animation_velocity.emit()
        
    def __currentIndexChangedComboBoxSceneTypeResult(self):
        self.signal_scene_type_result.emit()
    
    def _currentIndexChangedComboBoxSceneAxisResult(self):
        self.signal_scene_type_result.emit()

    def __stateChangedCheckBoxResultVector(self):
        self.signal_scene_type_result.emit()

    def __clickedToolButtonSceneRegress(self):
        self.signal_scene_regress.emit()
        
    def __clickedToolButtonSceneStop(self):
        self.signal_scene_stop.emit()

    def __clickedToolButtonScenePlay(self):
        self.signal_scene_play.emit()

    def __clickedToolButtonSceneAdvance(self):
        self.signal_scene_advance.emit()
            
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    def getColorStyle(self):
        if self.color_style == 0:
            return self.comboBox_ResultAnimationColorStyles_Puntos.currentText()
        else:
            return self.comboBox_ResultAnimationColorStyles_Resultados.currentText()

    def getTypeResult(self):
        type_result = self.comboBox_sceneTypeResult.currentText().split('→')[0].lower()
        return type_result
    
    def getAxisResult(self):
        if self.radioButton_ResultX.isChecked():
            axis = 'xx'
        elif self.radioButton_ResultY.isChecked():
            axis = 'yy'
        elif self.radioButton_ResultXY.isChecked():
            axis = 'xy'
        return axis
    def getVectorResult(self):
        return self.checkBox_ResultVector.isChecked()
    
    def getVelocity(self):
        return self.spinBox_ResultAnimationVelocity.value()
    
    def getColorCustomHue(self):
        return self.__color_custom_hue
    
    def getSizePoints(self):
        return self.doubleSpinBoxl_textResultAnimationSizePoints.value()
    
    def getSizeTexts(self):
        return self.spinBox_ResultAnimationSizeText.value()
    
    def getValuesText(self):
        return self.checkBox_ResultAnimationValues.isChecked()
    
    def resetTypeResult(self):
        self.comboBox_sceneTypeResult.setCurrentIndex(0)
        #self.comboBox_ResultAnimationColorStyles.setCurrentIndex(0)
        #self.comboBox_ResultAnimationColorStyles.setEnabled(False)
        
    '''
    def setEnableColorStyle(self, enable):
        type_result = self.getTypeResult()
        if type_result == 'default':
            self.comboBox_ResultAnimationColorStyles.setCurrentIndex(0)
        else:
            self.comboBox_ResultAnimationColorStyles.setCurrentIndex(self.color_style)
            
    '''
        #self.comboBox_ResultAnimationColorStyles.setEnabled(enable)
    
    def setEnabledSeletedAxis(self, enable):
        self.radioButton_ResultX.setEnabled(enable)
        self.radioButton_ResultY.setEnabled(enable)
        self.radioButton_ResultXY.setEnabled(enable)

    def setEnabledSeletedVector(self, enable):
        self.checkBox_ResultVector.setEnabled(enable)

    def showStyleColor(self, color_style=0):
        """ Agrega los estilos de color a la lista desplegable. 
        Args:
            color_style (int): Estilo de color.
        Values:
            0: Para Puntos
            1: Para resultados

        """
        self.color_style = color_style
        if color_style == 0:
            self.comboBox_ResultAnimationColorStyles_Puntos.setVisible(True)
            index_selected = self.comboBox_ResultAnimationColorStyles_Puntos.currentIndex()
            self.setColor(index_selected)
            self.comboBox_ResultAnimationColorStyles_Resultados.setVisible(False)
        elif color_style == 1:
            self.comboBox_ResultAnimationColorStyles_Puntos.setVisible(False)
            self.comboBox_ResultAnimationColorStyles_Resultados.setVisible(True)
            index_selected = self.comboBox_ResultAnimationColorStyles_Resultados.currentIndex()
            self.setColor(index_selected)
      







    ###############################################################################
	# ::::::::::::::::::::         OTROS MÉTODOS         ::::::::::::::::::::
	##############################################################################
 
    def stopAnimation(self):
        self.toolButton_scenePlay.setIcon(self.icon_play)
        
    def playPauseAnimation(self, play):
        if play:            
            self.toolButton_scenePlay.setIcon(self.icon_pause)            
        else :            
            self.toolButton_scenePlay.setIcon(self.icon_play)  

    def setColor(self, index, color_input="#99ff33"):
        """ Establece el color del cuadro de texto de color.
        Args:
            index (int): Índice del color.
            color_input (str): Color en formato hexadecimal.
        Values:
            para self.color_style = 0
                0: Material
                1: Bicolor
            para self.color_style = 1
                0: Rojo-Azul
                1: Escala de grises
                2: Escala color
        """

        self.btn_select_color.setEnabled(False)
        self.lineEdit_textColor.setText("")

        if self.color_style == 0:

            if index == 0:
                color = "transparent"
                self.lineEdit_textColor.setText("🟠🟢🟢🟠")
                
            elif index == 1:
                color = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.49 #a8821d, stop:0.51 #594c2b);"
        else:
            if index == 0:
                color = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.2 rgba(255, 255, 0, 255), stop:0.40 rgba(0, 255, 0, 255), stop:0.6 rgba(0, 255,255, 255), stop:0.8 rgba(0, 0, 255, 255),stop:1  rgba(250, 0, 255, 255));"
            elif index == 1:
                color = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"   
            elif index == 2:
                self.btn_select_color.setEnabled(True)
                color = QColor.fromHsv(self.__color_custom_hue, 255, 255)  
                color_input = color.name()
                color = "qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,stop:0 rgba(255, 255, 255, 255), stop:1 {});".format(color_input)
        
        self.lineEdit_textColor.setStyleSheet("border-color: #444444;background-color: {};".format(color))

    def setSteps(self, steps):
        self.label_textResultSteps.setText(str(steps))
        
    def setSizePoint(self, size):
        self.doubleSpinBoxl_textResultAnimationSizePoints.setValue(size)
        
    def setTimeView(self, time):
        self.label_textResultTime.setText(str(time))
        
    def setStepView(self, step):
        self.label_textResultStep.setText(str(step))

