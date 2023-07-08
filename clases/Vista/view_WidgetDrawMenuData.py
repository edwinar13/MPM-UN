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

    signal_show_hide_items = Signal(bool)  
    signal_show_hide_label = Signal(bool)  
    
    def __init__(self):
        super(ViewWidgetDrawMenuData, self).__init__()
        self.setupUi(self)
        
        self.__hide_show_frame_data=True
        self.__hide_show_frame_data_1=True
        self.__hide_show_frame_data_2=True
        self.__hide_show_frame_data_3=True

        self.__hide_show_items=True
        self.__hide_show_label=True 
        
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
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_poin_material = QIcon()
        self.icon_show_poin_material.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_poin_material = QIcon()
        self.icon_hide_poin_material.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        

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
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardDataSubTitle1.clicked.connect(self.__clickedToolButtonCardDataSubTitle1)
        self.toolButton_cardDataSubTitle2.clicked.connect(self.__clickedToolButtonCardDataSubTitle2)
        self.toolButton_cardDataSubTitle3.clicked.connect(self.__clickedToolButtonCardDataSubTitle3)
        self.toolButton_showHideItem.clicked.connect(self.__clickedToolButtonShowHideItems)
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)

        # ::::::::::::::::::::      EVENTOS DRAW MENU DRAW     ::::::::::::::::::::
        self.toolButton_cardDataDrawPoint.clicked.connect(self.__clickedToolButtonCardDataDrawPoint)
        self.toolButton_cardDataDrawLine.clicked.connect(self.__clickedToolButtonCardDataDrawLine)
        self.toolButton_cardDataDrawRotate.clicked.connect(self.__clickedToolButtonCardDataDrawRotate)
        self.toolButton_cardDataDrawMove.clicked.connect(self.__clickedToolButtonCardDataDrawMove)
        self.toolButton_cardDataDrawCopy.clicked.connect(self.__clickedToolButtonCardDataDrawCopy)
        self.toolButton_cardDataDrawErase.clicked.connect(self.__clickedToolButtonCardDataDrawErase)
        self.toolButton_cardDataDrawImport.clicked.connect(self.__clickedToolButtonCardDataDrawImport)
        self.toolButton_cardDataDrawRule.clicked.connect(self.__clickedToolButtonCardDataDrawRule)
        self.toolButton_cardDataDrawIntersection.clicked.connect(self.__clickedToolButtonCardDataDrawIntersection)
        
        # ::::::::::::::::::::      EVENTOS DRAW MENU DATA     ::::::::::::::::::::
        self.lineEdit_textData_DataTitleProject.editingFinished.connect(self.__editingFinishedLineEditDataTitleProject)
        self.lineEdit_textData_DataLocation.editingFinished.connect(self.__editingFinishedLineEditDataLocation)
        self.lineEdit_textData_DataAuthor.editingFinished.connect(self.__editingFinishedLineEditDataAuthor)
        self.textEdit_textData_DataDescription.textChanged.connect(self.__textChangedTextEditDataDescription)
        self.lineEdit_textData_DataGravity.editingFinished.connect(self.__editingFinishedLineEditDataGravity)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

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
        
    def __clickedToolButtonCardDataSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  botones dibujo  """
        if self.__hide_show_frame_data_1 == True:
            self.frame_data0.setVisible(False)
            self.__hide_show_frame_data_1 = False
            self.toolButton_cardDataSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_1 == False:
            self.frame_data0.setVisible(True)
            self.__hide_show_frame_data_1 = True
            self.toolButton_cardDataSubTitle1.setIcon(self.icon_minimize)
        
    def __clickedToolButtonCardDataSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  datos del proyecto  """
        if self.__hide_show_frame_data_2 == True:
            self.frame_data1.setVisible(False)
            self.__hide_show_frame_data_2 = False
            self.toolButton_cardDataSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_2 == False:
            self.frame_data1.setVisible(True)
            self.__hide_show_frame_data_2 = True
            self.toolButton_cardDataSubTitle2.setIcon(self.icon_minimize)

    def __clickedToolButtonCardDataSubTitle3(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_data_3 == True:
            self.frame_data2.setVisible(False)
            self.__hide_show_frame_data_3 = False
            self.toolButton_cardDataSubTitle3.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_data_3 == False:
            self.frame_data2.setVisible(True)
            self.__hide_show_frame_data_3 = True
            self.toolButton_cardDataSubTitle3.setIcon(self.icon_minimize)


    def __clickedToolButtonShowHideItems(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_items == True:
            self.__hide_show_items = False
            self.signal_show_hide_items.emit(self.__hide_show_items)
            self.toolButton_showHideItem.setIcon(self.icon_hide_poin_material)
        elif self.__hide_show_items == False:  
            self.__hide_show_items = True
            self.signal_show_hide_items.emit(self.__hide_show_items)
            self.toolButton_showHideItem.setIcon(self.icon_show_poin_material)

    def __clickedToolButtonShowHideLabel(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_label == True:
            self.signal_show_hide_label.emit(self.__hide_show_label)
            self.__hide_show_label = False
            self.toolButton_showHideLabel.setIcon(self.icon_show_label)
        elif self.__hide_show_label == False:
            self.signal_show_hide_label.emit(self.__hide_show_label)
            self.__hide_show_label = True
            self.toolButton_showHideLabel.setIcon(self.icon_hide_label)





    # ::::::::::::::::::::      EVENTOS MENU DRAW     ::::::::::::::::::::
    def __clickedToolButtonCardDataDrawPoint(self):
        self.signal_paint_point.emit()

    def __clickedToolButtonCardDataDrawLine(self):
        self.signal_paint_line.emit()  

    def __clickedToolButtonCardDataDrawMove(self):
        self.signal_paint_move.emit()

    def __clickedToolButtonCardDataDrawRotate(self):
        self.signal_paint_rotate.emit()

    def __clickedToolButtonCardDataDrawCopy(self):
        self.signal_paint_copy.emit()
        
    def __clickedToolButtonCardDataDrawErase(self):
        self.signal_paint_erase.emit()

    def __clickedToolButtonCardDataDrawImport(self):
        self.signal_paint_import.emit()

    def __clickedToolButtonCardDataDrawRule(self):
        self.signal_paint_rule.emit()

    def __clickedToolButtonCardDataDrawIntersection(self):
        self.signal_paint_intersection.emit()

    # ::::::::::::::::::::      EVENTOS MENU DATA     ::::::::::::::::::::
    def __editingFinishedLineEditDataTitleProject(self):
        """ Actualiza name_project en la copia de la bd del proyecto """ 
        name_project = self.lineEdit_textData_DataTitleProject.text()
        self.signal_data_project.emit({"name_project":name_project})
        
    def __editingFinishedLineEditDataLocation(self):
        """ Actualiza location en la copia de la bd del proyecto """ 
        location = self.lineEdit_textData_DataLocation.text()
        self.signal_data_project.emit({"location":location})

    def __editingFinishedLineEditDataAuthor(self):
        """Actualiza author en la copia de la bd del proyecto """ 
        author = self.lineEdit_textData_DataAuthor.text()
        self.signal_data_project.emit({"author":author})

    def __textChangedTextEditDataDescription(self):
        """Actualiza description en la copia de la bd del proyecto """         
        description = self.textEdit_textData_DataDescription.toPlainText()
        self.signal_data_project.emit({"description":description})

    def __editingFinishedLineEditDataGravity(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza gravity en la copia de la bd del proyecto.
        si no es número da mensaje de error""" 
        gravity = self.lineEdit_textData_DataGravity.text()
        if general_functions.isNumber(gravity):
            self.lineEdit_textData_DataGravity.setText(str(float(gravity)))            
            self.lineEdit_textData_DataGravity.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            self.signal_data_project.emit({"gravity":gravity})       

        else:            
            self.lineEdit_textData_DataGravity.setFocus()
            self.lineEdit_textData_DataGravity.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la gravedad")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))


    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  GENERALES        ::::::::::::::::::::
	###############################################################################

    def setTextWidget(self, data_info, data_config):
   
        self.name_project=data_info[0]
        self.location=data_info[1]
        self.author=data_info[2]
        self.description=data_info[3]
        self.gravity=data_config[0]
  
        self.lineEdit_textData_DataTitleProject.setText(self.name_project)
        self.lineEdit_textData_DataLocation.setText(self.location)
        self.lineEdit_textData_DataAuthor.setText(self.author)
        self.textEdit_textData_DataDescription.setText(self.description)
        self.lineEdit_textData_DataGravity.setText("{}".format(self.gravity))

