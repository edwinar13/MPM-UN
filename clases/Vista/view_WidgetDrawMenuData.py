""" Este módulo contiene la clase Ui_FormDrawMenuData, para incluirla en frame draw
es el widget menú de datos del proyecto."""

from PySide6.QtCore import ( Signal, QSize,QTimer)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy)
from ui import ui_widget_draw_menu_data
from clases import general_functions
from clases import class_general


class ViewWidgetDrawMenuData(QFrame, ui_widget_draw_menu_data.Ui_FormDrawMenuData):
    """Esta clase crea el QFrame draw-menu-data para agregarlo a Frame Draw.

    Attributes:
            name_project (str): Nombre del proyecto.
            location (str): Localización del proyecto.
            author (str): Autor del proyecto.
            description (str):Descripción del proyecto.
            gravity (str): Gravedad para el proyecto.
            hide_show_frame_data_1 (bool): Cambio para hide-Show de frame datos.
            hide_show_frame_data_2 (bool): Cambio para hide-Show de frame configuración.
            hide_show_frame_data (bool): Cambio para hide-Show draw-menu-data.
            projectActual (Project): Objeto del proyecto actual.
    Method:
            : initDrawMenuDataProject

    """ 
    signal_msn_critical = Signal(str)    
    signal_msn_satisfactory = Signal(str)    
    signal_msn_informative = Signal(str)  
    signal_data_project = Signal(dict)

    signal_paint_point = Signal() 
    signal_paint_line = Signal() 
    signal_paint_rotate = Signal() 
    signal_paint_move = Signal() 
    signal_paint_copy = Signal() 
    signal_paint_erase = Signal()
    signal_paint_import = Signal()
    signal_paint_rule = Signal()
    signal_paint_intersection = Signal()
    
    def __init__(self):
        super(ViewWidgetDrawMenuData, self).__init__()
        self.setupUi(self)
        

        self.__hide_show_frame_data_0=True
        self.__hide_show_frame_data_1=True
        self.__hide_show_frame_data_2=True
        self.__hide_show_frame_data=True

          

        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('INFORMACIÓN DEL PROYECTO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

        self.toolButton_updateData.setVisible(False)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        # ::::::::::::::::::::      EVENTOS DRAW MENU DATA     ::::::::::::::::::::
        self.lineEdit_textData1.editingFinished.connect(self.__editingFinishedLineEditWDP1)
        self.lineEdit_textData2.editingFinished.connect(self.__editingFinishedLineEditWDP2)
        self.lineEdit_textData3.editingFinished.connect(self.__editingFinishedLineEditWDP3)
        self.textEdit_textData4.textChanged.connect(self.__textChangedTextEditWDP4)
        self.lineEdit_textData5.editingFinished.connect(self.__editingFinishedLineEditWDP5)

        # ::::::::::::::::::::      EVENTOS DRAW MENU DRAW     ::::::::::::::::::::
        self.toolButton_cardMeshDrawPoint.clicked.connect(self.__clickedToolButtonCardMeshDrawPoint)
        self.toolButton_cardMeshDrawLine.clicked.connect(self.__clickedToolButtonCardMeshDrawLine)
        self.toolButton_cardMeshDrawRotate.clicked.connect(self.__clickedToolButtonCardMeshDrawRotate)
        self.toolButton_cardMeshDrawMove.clicked.connect(self.__clickedToolButtonCardMeshDrawMove)
        self.toolButton_cardMeshDrawCopy.clicked.connect(self.__clickedToolButtonCardMeshDrawCopy)
        self.toolButton_cardMeshDrawErase.clicked.connect(self.__clickedToolButtonCardMeshDrawErase)
        self.toolButton_cardMeshDrawImport.clicked.connect(self.__clickedToolButtonCardMeshDrawImport)
        self.toolButton_cardMeshDrawRule.clicked.connect(self.__clickedToolButtonCardMeshDrawRule)
        self.toolButton_cardMeshDrawIntersection.clicked.connect(self.__clickedToolButtonCardMeshDrawIntersection)
        
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardDataSubTitle0.clicked.connect(self.__clickedToolButtonCardDataSubTitle0)
        self.toolButton_cardDataSubTitle1.clicked.connect(self.__clickedToolButtonCardDataSubTitle1)
        self.toolButton_cardDataSubTitle2.clicked.connect(self.__clickedToolButtonCardDataSubTitle2)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    """ Métodos para los eventos de los botones y widget """

    # ::::::::::::::::::::      EVENTOS MENU DATA     ::::::::::::::::::::
    def __editingFinishedLineEditWDP1(self):
        """ Actualiza name_project en la copia de la bd del proyecto """ 
        name_project = self.lineEdit_textData1.text()
        self.signal_data_project.emit({"name_project":name_project})
        return

    def __editingFinishedLineEditWDP2(self):
        """ Actualiza location en la copia de la bd del proyecto """ 
        location = self.lineEdit_textData2.text()
        self.signal_data_project.emit({"location":location})

    def __editingFinishedLineEditWDP3(self):
        """Actualiza author en la copia de la bd del proyecto """ 
        author = self.lineEdit_textData3.text()
        self.signal_data_project.emit({"author":author})

    def __textChangedTextEditWDP4(self):
        """Actualiza description en la copia de la bd del proyecto """         
        description = self.textEdit_textData4.toPlainText()
        self.signal_data_project.emit({"description":description})

    def __editingFinishedLineEditWDP5(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza gravity en la copia de la bd del proyecto.
        si no es número da mensaje de error""" 
        gravity = self.lineEdit_textData5.text()
        if general_functions.isNumber(gravity):
            self.lineEdit_textData5.setText(str(float(gravity)))            
            self.lineEdit_textData5.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            self.signal_data_project.emit({"gravity":gravity})       

        else:            
            self.lineEdit_textData5.setFocus()
            self.lineEdit_textData5.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la gravedad")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))


            

    # ::::::::::::::::::::      EVENTOS MENU DRAW     ::::::::::::::::::::
    def __clickedToolButtonCardMeshDrawPoint(self):
        self.signal_paint_point.emit()

    def __clickedToolButtonCardMeshDrawLine(self):
        self.signal_paint_line.emit()  

    def __clickedToolButtonCardMeshDrawMove(self):
        self.signal_paint_move.emit()

    def __clickedToolButtonCardMeshDrawRotate(self):
        self.signal_paint_rotate.emit()

    def __clickedToolButtonCardMeshDrawCopy(self):
        self.signal_paint_copy.emit()
        
    def __clickedToolButtonCardMeshDrawErase(self):
        self.signal_paint_erase.emit()

    def __clickedToolButtonCardMeshDrawImport(self):
        self.signal_paint_import.emit()

    def __clickedToolButtonCardMeshDrawRule(self):
        self.signal_paint_rule.emit()

    def __clickedToolButtonCardMeshDrawIntersection(self):
        self.signal_paint_intersection.emit()


    # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """
        if self.__hide_show_frame_data == True:
            self.frame_data.setVisible(False)
            self.__hide_show_frame_data = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_data == False:
            self.frame_data.setVisible(True)
            self.__hide_show_frame_data = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)
        
    def __clickedToolButtonCardDataSubTitle0(self):
        """ Muestra o oculta el submenú data de draw  >  botones dibujo  """
        if self.__hide_show_frame_data_0 == True:
            self.frame_data0.setVisible(False)
            self.__hide_show_frame_data_0 = False
            self.toolButton_cardDataSubTitle0.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_0 == False:
            self.frame_data0.setVisible(True)
            self.__hide_show_frame_data_0 = True
            self.toolButton_cardDataSubTitle0.setIcon(self.icon_minimize)
        
    def __clickedToolButtonCardDataSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  datos del proyecto  """
        if self.__hide_show_frame_data_1 == True:
            self.frame_data1.setVisible(False)
            self.__hide_show_frame_data_1 = False
            self.toolButton_cardDataSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_1 == False:
            self.frame_data1.setVisible(True)
            self.__hide_show_frame_data_1 = True
            self.toolButton_cardDataSubTitle1.setIcon(self.icon_minimize)

    def __clickedToolButtonCardDataSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_data_2 == True:
            self.frame_data2.setVisible(False)
            self.__hide_show_frame_data_2 = False
            self.toolButton_cardDataSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_2 == False:
            self.frame_data2.setVisible(True)
            self.__hide_show_frame_data_2 = True
            self.toolButton_cardDataSubTitle2.setIcon(self.icon_minimize)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  GENERALES        ::::::::::::::::::::
	###############################################################################

    def setTextWidget(self, data_info, data_config):
   
        self.name_project=data_info["NOMBREPROYECTO"]
        self.location=data_info["LOCALIZACION"]
        self.author=data_info["AUTOR"]
        self.description=data_info["DESCRIPCION"]
        self.gravity=data_config["GRAVEDAD"]
  

        """ Recupera información de los atributos y la coloca en los campos del draw-menu-data """
        self.lineEdit_textData1.setText(self.name_project)
        self.lineEdit_textData2.setText(self.location)
        self.lineEdit_textData3.setText(self.author)
        self.textEdit_textData4.setText(self.description)
        self.lineEdit_textData5.setText("{}".format(self.gravity))