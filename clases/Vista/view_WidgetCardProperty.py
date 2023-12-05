""" Este módulo contiene la clase Ui_FormDrawMeshCard, para incluirla en frame draw-menu-materialPoint
Es el widget card de cada materialPoint."""
from PySide6.QtCore import ( QSize, Signal)
from PySide6.QtGui import (QColor,QIcon)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)

from ui.ui_widget_draw_property_card import Ui_FormDrawPropertyCard
from clases import class_ui_dialog_msg

 
class viewCardDrawProperty(QFrame, Ui_FormDrawPropertyCard):
    """Esta clase crea el QFrame materialPoint-card para agregarlo a Frame draw-menu-materialPoint. 

    Args:
            cardNameMesh (str):      Nombre de la malla (default = "").
            cardColorMesh (str):     Color de la malla (default = "").
            cardShowHideMesh (bool): Estado para mostrar u ocultar la malla (default = True).
            
    Attributes:
            __card_name_materialPoint (str):       Nombre de la malla.
            __card_color_material_point (str):      Color de la malla.
            __card_show_hide_material_point (bool): Estado para mostrar u ocultar la malla.

    """    

    signal_delete_property = Signal()
    signal_update_property = Signal()
    
    def __init__(self, controller_CardProperty):
        super(viewCardDrawProperty, self).__init__()
        self.setupUi(self)

        # esto solo para que sirva Slot-Signal
        self.controller_CardProperty = controller_CardProperty

        self.__card_show_data_property = True
        '''
        self.__card_name_material_point = None
        
        '''

        # Configura la UI
        self.__configUi()
        self.__initEventUi()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    
    def __configUi(self):
        """Configura la interface de usuario (ui).""" 
        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,20,100))
        self.frame_card.setGraphicsEffect(self.shadow_card)

        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show = QIcon()
        self.icon_show.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide = QIcon()
        self.icon_hide.addFile(u"recursos/iconos/iconos_menu_draw_mesh/not_view.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.lineEdit_PropertyName.setVisible(False)
        self.toolButton_PropertyOk.setVisible(False)
        self.toolButton_PropertyExit.setVisible(False)
        self.frame_edit.setVisible(False)
     
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_PropertiesShow.clicked.connect(self.__clickedToolButtonPropertiesShow)
        self.toolButton_PropertyOk.clicked.connect(self.__clickedToolButtonPropertyOk)
        self.toolButton_PropertyExit.clicked.connect(self.__clickedToolButtonPropertyExit)
        self.toolButton_PropertyEdit.clicked.connect(self.__clickedToolButtonPropertyEdit)
        self.toolButton_PropertyClose.clicked.connect(self.__clickedToolButtonPropertyDelete)
    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonPropertyExit(self): 
        self.lineEdit_PropertyName.setVisible(False)
        self.toolButton_PropertyOk.setVisible(False)
        self.toolButton_PropertyExit.setVisible(False)
        self.frame_edit.setVisible(False)

        self.label_cardPropertyName.setVisible(True)
        self.toolButton_PropertyClose.setVisible(True)
        self.toolButton_PropertyEdit.setVisible(True)
        self.frame_view.setVisible(True)
    

    def __clickedToolButtonPropertyEdit(self): 
        self.lineEdit_PropertyName.setVisible(True)
        self.toolButton_PropertyOk.setVisible(True)
        self.toolButton_PropertyExit.setVisible(True)
        self.frame_edit.setVisible(True)

        self.label_cardPropertyName.setVisible(False)
        self.toolButton_PropertyClose.setVisible(False)
        self.toolButton_PropertyEdit.setVisible(False)
        self.frame_view.setVisible(False)


        self.lineEdit_PropertyName.setText(self.label_cardPropertyName.text())
        self.lineEdit_PropertyName.setFocus()
        self.doubleSpinBoxl_textPropertiesE.setValue(float(self.label_textPropertiesE.text()))
        self.doubleSpinBoxl_textPropertiesV.setValue(float(self.label_textPropertiesV.text()))
        self.doubleSpinBoxl_textPropertiesC.setValue(float(self.label_textPropertiesC.text()))
        self.doubleSpinBoxl_textPropertiesPhi.setValue(float(self.label_textPropertiesPhi.text()))
        self.doubleSpinBoxl_textPropertiesPsi.setValue(float(self.label_textPropertiesPsi.text()))
            
    def __clickedToolButtonPropertiesShow(self):
        """ Muestra u oculta  """

        if self.__card_show_data_property:            
            self.__card_show_data_property = False
            self.toolButton_PropertiesShow.setIcon(self.icon_hide)
            self.frame_properties1.setVisible(False)
            
        else :            
            self.__card_show_data_property = True
            self.toolButton_PropertiesShow.setIcon(self.icon_show)    
            self.frame_properties1.setVisible(True)
      
    def __clickedToolButtonPropertyOk(self):

        self.lineEdit_PropertyName.setVisible(False)
        self.toolButton_PropertyOk.setVisible(False)
        self.toolButton_PropertyExit.setVisible(False)
        self.frame_edit.setVisible(False)

        self.label_cardPropertyName.setVisible(True)
        self.toolButton_PropertyClose.setVisible(True)
        self.toolButton_PropertyEdit.setVisible(True)
        self.frame_view.setVisible(True)



        self.label_cardPropertyName.setText(self.lineEdit_PropertyName.text())     
        self.label_textPropertiesE.setText(str(self.doubleSpinBoxl_textPropertiesE.value()))
        self.label_textPropertiesV.setText(str(self.doubleSpinBoxl_textPropertiesV.value()))
        self.label_textPropertiesC.setText(str(self.doubleSpinBoxl_textPropertiesC.value()))
        self.label_textPropertiesPhi.setText(str(self.doubleSpinBoxl_textPropertiesPhi.value()))
        self.label_textPropertiesPsi.setText( str(self.doubleSpinBoxl_textPropertiesPsi.value()))

        self.signal_update_property.emit()


    def __clickedToolButtonPropertyDelete(self):       
        dialoMsg = class_ui_dialog_msg.DialogMsg(self, 3, 
                                "¿Quieres eliminar la propiedad {} ?".format(self.getName()), 
                                "")
        dialoMsg.setTypeIcon(1)
        dialoMsg.setTextDescription("")
        dialoMsg.setModal(True)
        dialoMsg.exec()
        result = dialoMsg.getButtonSelected()

        #Guardar
        if result == "yes":
            print("# Guardar = {}".format(2))
            
        # No Guardar
        elif result == "not":
            print("# No Guardar")
            return

        elif result == "cancel" or result == "exit":
            print("# Cancelar")
            return
            
        self.signal_delete_property.emit()

    def deleteCardView(self):
        # Elimina la tarjeta
        self.deleteLater()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.label_cardPropertyName.text()

    def getModulusElasticity(self):
        return float(self.label_textPropertiesE.text())

    def getPoissonRatio(self):
        return float(self.label_textPropertiesV.text())

    def getCohesion(self):
        return float(self.label_textPropertiesC.text())

    def getFrictionAngle(self):
        return float(self.label_textPropertiesPhi.text())

    def getAngleDilatancy(self):
        return float(self.label_textPropertiesPsi.text())

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################


    def showData(self, name, modulus_elasticity, poisson_ratio, cohesion, friction_angle, angle_dilatancy):        
        self.label_cardPropertyName.setText(u"{}".format(name))
        self.label_textPropertiesE.setText(u"{}".format(modulus_elasticity))
        self.label_textPropertiesV.setText(u"{}".format(poisson_ratio))
        self.label_textPropertiesC.setText(u"{}".format(cohesion))
        self.label_textPropertiesPhi.setText(u"{}".format(friction_angle))
        self.label_textPropertiesPsi.setText(u"{}".format(angle_dilatancy))




















       
