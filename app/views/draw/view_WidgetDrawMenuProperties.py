
from PySide6.QtCore import ( Signal, QSize,QTimer)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy)
from ui.ui_widget_draw_menu_properties import Ui_FormDrawMenuProperties
from utils import class_general


class ViewWidgetDrawMenuProperties(QFrame, Ui_FormDrawMenuProperties):
    signal_new_property= Signal() 
    def __init__(self):
        super(ViewWidgetDrawMenuProperties, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_properties=True
        self.__hide_show_frame_properties_1=True
        self.__hide_show_frame_properties_2=True

        self.list_view_card =[]

        # Configura la UI
        self.__configUi()
        self.__initEventUi()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"app/resources/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('INFORMACIÓN DEL PROYECTO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)
        
         #self.toolButton_updateData.setVisible(False)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('MATERIALES')
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
        self.toolButton_cardPropertiesSubTitle1.clicked.connect(self.__clickedToolButtonCardPropertiesSubTitle1)
        self.toolButton_cardPropertiesSubTitle2.clicked.connect(self.__clickedToolButtonCardPropertiesSubTitle2)
        # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::
        self.lineEdit_textPropertiesName.editingFinished.connect(self.__editingFinishedLineEditPropertiesName)

        self.toolButton_PropertiesCancel.clicked.connect(self.__clickedToolButtonPropertiesCancel)
        self.toolButton_PropertiesCreateProperty.clicked.connect(self.__clickedToolButtonPropertiesCreateProperty)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     :::::::::::::::::::: 
    def __clickedToolButtonHideShow(self):
        if self.__hide_show_frame_properties == True:
            self.frame_properties.setVisible(False)
            self.__hide_show_frame_properties = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_properties == False:
            self.frame_properties.setVisible(True)
            self.__hide_show_frame_properties = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)

    def __clickedToolButtonCardPropertiesSubTitle1(self):
        if self.__hide_show_frame_properties_1 == True:
            self.frame_properties1.setVisible(False)
            self.__hide_show_frame_properties_1 = False
            self.toolButton_cardPropertiesSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_properties_1 == False:
            self.frame_properties1.setVisible(True)
            self.__hide_show_frame_properties_1 = True
            self.toolButton_cardPropertiesSubTitle1.setIcon(self.icon_minimize)

    def __clickedToolButtonCardPropertiesSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_properties_2 == True:
            self.frame_properties2.setVisible(False)
            self.__hide_show_frame_properties_2 = False
            self.toolButton_cardPropertiesSubTitle2.setIcon(self.icon_maximize)
            self.verticalSpacer_2.changeSize(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        elif self.__hide_show_frame_properties_2 == False:
            self.frame_properties2.setVisible(True)
            self.__hide_show_frame_properties_2 = True
            self.toolButton_cardPropertiesSubTitle2.setIcon(self.icon_minimize)
            self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)


    # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::

  

        

     
    def __editingFinishedLineEditPropertiesName(self):
        self.lineEdit_textPropertiesName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 
          

    def __clickedToolButtonPropertiesCancel(self):
        self.endProperty()

    def __clickedToolButtonPropertiesCreateProperty(self):
        self.signal_new_property.emit()


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName (self):        
        return self.lineEdit_textPropertiesName.text()
    
    
    def getPropertiesE (self):
        return self.doubleSpinBoxl_textPropertiesE.value()    
    
    def getPropertiesV (self):
        return self.doubleSpinBoxl_textPropertiesV.value()
    
    def getPropertiesC(self):
        return self.doubleSpinBoxl_textPropertiesC.value()

    def getPropertiesPhi(self):
        return self.doubleSpinBoxl_textPropertiesPhi.value()
    
    def getPropertiesRho(self):
        return self.doubleSpinBoxl_textPropertiesP.value()
        
    def getPropertiesPsi(self):
        return self.doubleSpinBoxl_textPropertiesPsi.value()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def removeCardProperty(self):
        view_card=None
        if len(self.list_view_card) != 0:
            for view_card in self.list_view_card: 
                self.verticalLayout_containerCardProperties.removeWidget(view_card)
                view_card.deleteLater()
            self.list_view_card=[]


    def addCardProperty(self, card_property):
        self.verticalLayout_containerCardProperties.addWidget(card_property)
        self.list_view_card.append(card_property)
        last_index = self.verticalLayout_containerCardProperties.count() - 1
        self.verticalLayout_containerCardProperties.insertWidget(last_index, self.frame_empty)

    def endProperty(self):
        self.lineEdit_textPropertiesName.setText("")
        self.doubleSpinBoxl_textPropertiesE.setValue(1000)
        self.doubleSpinBoxl_textPropertiesV.setValue(0.3)
        self.doubleSpinBoxl_textPropertiesC.setValue(5)
        self.doubleSpinBoxl_textPropertiesPhi.setValue(1000)
        self.doubleSpinBoxl_textPropertiesPsi.setValue(5)
        

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  MENSAJES         ::::::::::::::::::::
	##############################################################################

    def msnAlertName(self, error, msn=""):
        if not error:
            self.lineEdit_textPropertiesName.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textPropertiesName.setFocus()
            self.lineEdit_textPropertiesName.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))





    def msnAlertDefault(self, msn=""):
        self.label_msn.setStyleSheet("color:  #F94646")  
        self.label_msn.setText(msn)          
        QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

