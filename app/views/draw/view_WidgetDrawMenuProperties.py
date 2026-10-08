
from PySide6.QtCore import ( Signal, QSize,QTimer)
from PySide6.QtGui import (QIcon, QFont, QColor)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy, QColorDialog)

from ui.ui_widget_draw_menu_properties import Ui_FormDrawMenuProperties
from utils import class_general

# (texto visible, valor guardado en MATERIALES.<id>.MODELO)
MODEL_OPTIONS = [("Mohr-Coulomb", "MOHR_COULOMB"), ("Elástico", "ELASTICO")]

# Doble fase (solo la usa la etapa de consolidación): (clave, rótulo, unidad, valor por defecto)
TWO_PHASE_FIELDS = [("POROSIDAD", "Porosidad n0:", "", 0.3),
                    ("PERMEABILIDAD", "Permeabilidad k:", "m/s", 1e-5),
                    ("MODULOAGUA", "Módulo agua Kw:", "kPa", 2.2e6)]
TWO_PHASE_TIP = ("Solo para la etapa de consolidación (doble fase).\n"
                 "En ella la densidad del material se toma como densidad SECA ρd;\n"
                 "la de sólidos es ρd/(1−n0) y la del agua 1000 kg/m³.\n"
                 "Kw real ≈ 2.2e6 kPa; un valor menor agranda el paso de tiempo.")


class TwoPhaseFields:
    """Las tres filas de doble fase (n0, k, Kw) del formulario. Los campos están
    en el .ui con los mismos nombres en el menú y en la tarjeta
    (lineEdit_textPropertiesPorosity/Permeability/Kw); aquí se leen y escriben.
    Acepta notación científica (1e-5)."""

    WIDGETS = {"POROSIDAD": "Porosity", "PERMEABILIDAD": "Permeability", "MODULOAGUA": "Kw"}

    def __init__(self, form):
        self.edits = {}
        for key, _, unit, _ in TWO_PHASE_FIELDS:
            suffix = self.WIDGETS[key]
            edit = getattr(form, f"lineEdit_textProperties{suffix}")
            edit.setToolTip(f"{unit}\n{TWO_PHASE_TIP}" if unit else TWO_PHASE_TIP)
            getattr(form, f"label_textProperties{suffix}").setToolTip(TWO_PHASE_TIP)
            self.edits[key] = edit
        self.set(None)

    def set(self, values):
        """Muestra `values` (dict) o los valores por defecto si es None."""
        for key, _, _, default in TWO_PHASE_FIELDS:
            v = default if not values or key not in values else values[key]
            self.edits[key].setText(f"{v:g}")

    def get(self):
        """dict con los tres valores, o None si alguno no es un número válido."""
        out = {}
        for key, *_ in TWO_PHASE_FIELDS:
            try:
                out[key] = float(self.edits[key].text().replace(",", "."))
            except ValueError:
                return None
        return out


def fill_model_combo(combo, label=None):
    """Opciones de MODEL_OPTIONS (texto visible + valor guardado) y su tooltip."""
    for text, value in MODEL_OPTIONS:
        combo.addItem(text, value)
    tip = ("Mohr-Coulomb: plastifica en las etapas con plasticidad activa.\n"
           "Elástico lineal: nunca plastifica (c, φ y ψ no se usan).")
    for w in (combo, label):
        if w is not None:
            w.setToolTip(tip)


def format_two_phase(values):
    """Texto corto para mostrar los datos de doble fase en una tarjeta."""
    if not values:
        return "—"
    return (f"n0={values['POROSIDAD']:g}, k={values['PERMEABILIDAD']:g} m/s, "
            f"Kw={values['MODULOAGUA']:g} kPa")


class ViewWidgetDrawMenuProperties(QFrame, Ui_FormDrawMenuProperties):
    signal_new_property= Signal() 
    signal_show_hide_properties = Signal(bool)
    
    def __init__(self):
        super(ViewWidgetDrawMenuProperties, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_properties=True
        self.__hide_show_frame_properties_1=True
        self.__hide_show_frame_properties_2=True

        self.__hide_show_properties = True        
        
        self.__color_property = None
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
        
                        
        self.icon_show_properties = QIcon()
        self.icon_show_properties.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.icon_hide_properties = QIcon()
        self.icon_hide_properties.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        '''
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('INFORMACIÓN DEL PROYECTO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)
        
         #self.toolButton_updateData.setVisible(False)
        '''
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('MATERIALES')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)
        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Modelo constitutivo y doble fase: filas del .ui; aquí solo las opciones
        # del combo (cada una con su valor guardado) y los tooltips.
        fill_model_combo(self.comboBox_textPropertiesModel, self.label_textPropertiesModel)
        self.two_phase_fields = TwoPhaseFields(self)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::

        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardPropertiesSubTitle1.clicked.connect(self.__clickedToolButtonCardPropertiesSubTitle1)
        self.toolButton_cardPropertiesSubTitle2.clicked.connect(self.__clickedToolButtonCardPropertiesSubTitle2)
        self.toolButton_showHideProperties.clicked.connect(self.__clickedToolButtonShowHideProperties)
        # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::
        self.lineEdit_textPropertiesName.editingFinished.connect(self.__editingFinishedLineEditPropertiesName)
        self.toolButton_PropertiesColor.clicked.connect(self.__clickedToolButtonPropertiesColorPicker)
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
            
            
    def __clickedToolButtonShowHideProperties(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_properties == True:
            self.__hide_show_properties = False
            self.signal_show_hide_properties.emit(self.__hide_show_properties)
            self.toolButton_showHideProperties.setIcon(self.icon_hide_properties)
            
        elif self.__hide_show_properties == False:  
            self.__hide_show_properties = True
            self.signal_show_hide_properties.emit(self.__hide_show_properties)
            self.toolButton_showHideProperties.setIcon(self.icon_show_properties)


    # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::

  

        

     
    def __editingFinishedLineEditPropertiesName(self):
        self.lineEdit_textPropertiesName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 
          
    def __clickedToolButtonPropertiesColorPicker(self):
        color = QColorDialog.getColor(initial=QColor(100 ,100, 100))
        if color.isValid():
            self.__color_property=color.name()
            self.lineEdit_textPropertiesColor.setStyleSheet('background-color : {}'.format(self.__color_property))

    def __clickedToolButtonPropertiesCancel(self):
        self.endProperty()

    def __clickedToolButtonPropertiesCreateProperty(self):
        self.signal_new_property.emit()


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName (self):        
        return self.lineEdit_textPropertiesName.text()
    
    def getColor(self):     
        return self.__color_property
    
    
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

    def getPropertiesModel(self):
        return self.comboBox_textPropertiesModel.currentData()

    def getPropertiesTwoPhase(self):
        """dict de doble fase, o None si algún valor no es un número."""
        return self.two_phase_fields.get()

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
        # Al eliminar la tarjeta (p. ej. borrar el elemento) sale de la lista;
        # si no, al abrir otro proyecto se intenta quitar un widget ya destruido.
        card_property.destroyed.connect(
            lambda *_: card_property in self.list_view_card and self.list_view_card.remove(card_property))
        last_index = self.verticalLayout_containerCardProperties.count() - 1
        self.verticalLayout_containerCardProperties.insertWidget(last_index, self.frame_empty)

    def endProperty(self):
        self.lineEdit_textPropertiesName.setText("")
        self.doubleSpinBoxl_textPropertiesE.setValue(1000)
        self.doubleSpinBoxl_textPropertiesV.setValue(0.3)
        self.doubleSpinBoxl_textPropertiesC.setValue(5)
        self.doubleSpinBoxl_textPropertiesPhi.setValue(1000)
        self.doubleSpinBoxl_textPropertiesPsi.setValue(5)
        self.comboBox_textPropertiesModel.setCurrentIndex(0)
        self.two_phase_fields.set(None)
        self.__color_property = None
        self.lineEdit_textPropertiesColor.setStyleSheet('background-color : #333333')
        

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



    def msnAlertColor(self, error, msn=""):
        if not error:
            self.lineEdit_textPropertiesColor.setStyleSheet("border-color: #444444;background-color: {};".format(self.__color_property))
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textPropertiesColor.setFocus()
            self.lineEdit_textPropertiesColor.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))


    def msnAlertDefault(self, msn=""):
        self.label_msn.setStyleSheet("color:  #F94646")  
        self.label_msn.setText(msn)          
        QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

