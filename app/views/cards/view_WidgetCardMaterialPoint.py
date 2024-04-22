
from PySide6.QtCore import ( Signal, QSize,QTimer, Qt)
from PySide6.QtGui import (QIcon, QFont, QPixmap, QColor, QPainter, QPen)


from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect, QColorDialog)

from ui.ui_widget_draw_material_point_card import Ui_FormDrawMaterialPointCard
from utils import class_ui_dialog_msg

 
class viewCardDrawMaterialPoint(QFrame, Ui_FormDrawMaterialPointCard):
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
    signal_hide_show_material_point = Signal(bool)
    signal_hide_show_label = Signal(bool)
    signal_delete_material_point = Signal()
    signal_update_material_point = Signal()
    
    def __init__(self, controller_CardMesh):
        super(viewCardDrawMaterialPoint, self).__init__()
        self.setupUi(self)

        # esto solo para que sirva Slot-Signal
        self.controller_CardMesh = controller_CardMesh

        self.__card_show_hide_material_point = True
        self.__card_show_hide_label = False
        self.__card_name_material_point = None
        
        self.current_index_property = None
        
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
        self.icon_show.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide = QIcon()
        self.icon_hide.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/not_view.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        

        self.lineEdit_nameMaterialPoint.setVisible(False)
        
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)

        self.comboBox_PointMaterialProperty.setEnabled(False)
        self.setPropertyStyle(widget=self.comboBox_PointMaterialProperty, name_property="QComboBoxStyle", property= 2)
     
    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)
        self.toolButton_showHideMaterialPoint.clicked.connect(self.__clickedToolButtonShowHideMaterialPoint)
        self.toolButton_deleteMaterialPoint.clicked.connect(self.__clickedToolButtonDeleteMaterialPoint)
        self.toolButton_editMaterialPoint.clicked.connect(self.__clickedToolButtonEditMaterialPoint) 
        self.toolButton_okMaterialPoint.clicked.connect(self.__clickedToolButtonOkMaterialPoint)
        self.toolButton_exitMaterialPoint.clicked.connect(self.__clickedToolButtonExitMaterialPoint)
    
    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################

    def __clickedToolButtonEditMaterialPoint(self):
        self.lineEdit_nameMaterialPoint.setVisible(True)
        self.toolButton_okMaterialPoint.setVisible(True)
        self.toolButton_exitMaterialPoint.setVisible(True)

        self.toolButton_deleteMaterialPoint.setVisible(False)
        self.toolButton_editMaterialPoint.setVisible(False)
        self.toolButton_showHideLabel.setVisible(False)
        self.toolButton_showHideMaterialPoint.setVisible(False)
        self.label_cardNameMaterialPoint.setVisible(False)
        self.frame_color.setFixedWidth(20)

        self.lineEdit_nameMaterialPoint.setText(self.label_cardNameMaterialPoint.text())
        self.lineEdit_nameMaterialPoint.setFocus()
 
        self.comboBox_PointMaterialProperty.setEnabled(True)
        self.current_index_property = self.comboBox_PointMaterialProperty.currentIndex()
        self.setPropertyStyle(widget=self.comboBox_PointMaterialProperty, name_property="QComboBoxStyle", property= 1)

    def __clickedToolButtonExitMaterialPoint(self): 
        self.lineEdit_nameMaterialPoint.setVisible(False)        
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)
        
        self.toolButton_deleteMaterialPoint.setVisible(True)
        self.toolButton_editMaterialPoint.setVisible(True)
        self.toolButton_showHideLabel.setVisible(True)
        self.toolButton_showHideMaterialPoint.setVisible(True)
        self.label_cardNameMaterialPoint.setVisible(True)
        self.frame_color.setFixedWidth(10)

        #self.frame_color.setStyleSheet('background-color : {}'.format(self.__card_color_material_point))
        self.comboBox_PointMaterialProperty.setEnabled(False)
        self.comboBox_PointMaterialProperty.setCurrentIndex(self.current_index_property)
        self.setPropertyStyle(widget=self.comboBox_PointMaterialProperty, name_property="QComboBoxStyle", property= 2)
 

    def __clickedToolButtonOkMaterialPoint(self):
        self.lineEdit_nameMaterialPoint.setVisible(False)
        self.toolButton_okMaterialPoint.setVisible(False)
        self.toolButton_exitMaterialPoint.setVisible(False)
        
        self.toolButton_deleteMaterialPoint.setVisible(True)
        self.toolButton_editMaterialPoint.setVisible(True)
        self.toolButton_showHideMaterialPoint.setVisible(True)
        self.label_cardNameMaterialPoint.setVisible(True)
        self.frame_color.setFixedWidth(10)

        self.__card_name_material_point = self.lineEdit_nameMaterialPoint.text()
        self.lineEdit_nameMaterialPoint.setText("")
        self.label_cardNameMaterialPoint.setText(self.__card_name_material_point)

        self.comboBox_PointMaterialProperty.setEnabled(False)
        self.current_index_property = None
        self.setPropertyStyle(widget=self.comboBox_PointMaterialProperty, name_property="QComboBoxStyle", property= 2)
        
        self.signal_update_material_point.emit()
        
    def __clickedToolButtonShowHideLabel(self):
        """ Muestra u oculta la etiqueta """
        if self.__card_show_hide_label:            
            self.signal_hide_show_label.emit(False)
        else :
            self.signal_hide_show_label.emit(True)
        
    def __clickedToolButtonShowHideMaterialPoint(self):
        """ Muestra u oculta los puntos materiales"""
        if self.__card_show_hide_material_point:            
            self.signal_hide_show_material_point.emit(False)            
        else :            
            self.signal_hide_show_material_point.emit(True)

      
         
    def __clickedToolButtonDeleteMaterialPoint(self):       
        dialoMsg = class_ui_dialog_msg.DialogMsg(self, 3, 
                                "¿Quieres eliminar los puntos materiales {} ?".format(self.getName()), 
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
            
        self.signal_delete_material_point.emit()

        # Elimina la tarjeta
        self.deleteLater()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        self.__card_name_material_point = self.label_cardNameMaterialPoint.text()
        return self.__card_name_material_point

    def getProperty(self):
        """return [id_selected, name]"""
        name = self.comboBox_PointMaterialProperty.currentText()
        index = self.comboBox_PointMaterialProperty.currentIndex()
        if self.comboBox_PointMaterialProperty.count() == 0:
            return ["",""]
        id_selected = self.comboBox_PointMaterialProperty.itemData(index, Qt.UserRole)["id_property"]
        return [id_selected, name]
    
    def getMeshBase(self):
        return self.label_textPointMaterialMesh.text()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def showData(self, name, color, name_property, name_mesh):        
        self.label_cardNameMaterialPoint.setText(u"{}".format(name))
        self.frame_color.setStyleSheet('background-color : {}'.format(color))
        self.label_textPointMaterialMesh.setText(name_mesh)


    def setListProperties(self, properties_data, selected_property):         
        self.comboBox_PointMaterialProperty.clear()
        for item_index in range(len(properties_data)):
            id_property =properties_data[item_index][0]
            name_property =properties_data[item_index][1]                    
            self.comboBox_PointMaterialProperty.addItem(name_property)      
            self.comboBox_PointMaterialProperty.setItemData(self.comboBox_PointMaterialProperty.count() - 1, {"id_property": id_property}, Qt.UserRole)
        self.comboBox_PointMaterialProperty.setCurrentText(selected_property)

    def setColor(self, color):

        self.frame_color.setStyleSheet('background-color : {}'.format(color))
        
    def setBaseMesh(self, name_mesh):        
        self.label_textPointMaterialMesh.setText(name_mesh)

    def setPropertyStyle(self, widget, name_property, property: int):
        widget.setProperty(name_property, property)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()




    def ShowHideMaterialPoint(self, value):

        self.__card_show_hide_material_point = value
        if self.__card_show_hide_material_point:          
            self.toolButton_showHideMaterialPoint.setIcon(self.icon_show)  
        else :            
            self.toolButton_showHideMaterialPoint.setIcon(self.icon_hide)


    def showHideLabel(self, value):
        self.__card_show_hide_label = value
        if value:
            self.toolButton_showHideLabel.setIcon(self.icon_show_label)  
        else :            
            self.toolButton_showHideLabel.setIcon(self.icon_hide_label)








       
