
from PySide6.QtCore import ( Signal, QSize,QTimer, Qt)
from PySide6.QtGui import (QIcon, QFont, QPixmap, QColor, QPainter, QPen)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy, QColorDialog)
from ui.ui_widget_draw_menu_pointMaterial import Ui_FormDrawMenuPointMaterial
from clases import class_general

class ViewWidgetDrawMenuPointMaterial(QFrame, Ui_FormDrawMenuPointMaterial):

    signal_new_points_material = Signal()  

    def __init__(self):
        super(ViewWidgetDrawMenuPointMaterial, self).__init__()
        self.setupUi(self)

        self.hide_show_frame_material_point = True
        self.__hide_show_frame_material_point_2=True
        self.__hide_show_frame_material_point=True
        self.__color_material_point = None

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
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('PUNTO MATERIAL')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 

        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardPointMaterialSubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_cardPointMaterialSubTitle3.clicked.connect(self.__clickedToolButtonCardMeshSubTitle3)
        
        self.lineEdit_textPointMaterialName.editingFinished.connect(self.__editingFinishedLineEditPointMaterialName)
        self.toolButton_PointMaterialColor.clicked.connect(self.__clickedToolButtonPointMaterialColorPicker)        
        self.toolButton_PointMaterialCancel.clicked.connect(self.__clickedToolButtonPointMaterialCancel)
        self.toolButton_PointMaterial.clicked.connect(self.__clickedToolButtonPointMaterial)
        
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """

        if self.hide_show_frame_material_point == True:
            self.frame_pointMaterial.setVisible(False)
            self.hide_show_frame_material_point = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.hide_show_frame_material_point == False:
            self.frame_pointMaterial.setVisible(True)
            self.hide_show_frame_material_point = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)
    
    def __clickedToolButtonCardMeshSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_material_point_2 == True:
            self.frame_materialPoint2.setVisible(False)
            self.__hide_show_frame_material_point_2 = False
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_material_point_2 == False:
            self.frame_materialPoint2.setVisible(True)
            self.__hide_show_frame_material_point_2 = True
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle3(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_material_point == True:
            self.frame_materialPoint3.setVisible(False)
            self.__hide_show_frame_material_point = False
            self.toolButton_cardPointMaterialSubTitle3.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_material_point == False:
            self.frame_materialPoint3.setVisible(True)
            self.__hide_show_frame_material_point = True
            self.toolButton_cardPointMaterialSubTitle3.setIcon(self.icon_minimize)


    def __editingFinishedLineEditPointMaterialName(self):
        self.lineEdit_textPointMaterialName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 

    def __clickedToolButtonPointMaterialColorPicker(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__color_material_point=color.name()
            self.lineEdit_textPointMaterialColor.setStyleSheet('background-color : {}'.format(self.__color_material_point))

    def __clickedToolButtonPointMaterialCancel(self):
        self.endPointMaterial()

    def __clickedToolButtonPointMaterial(self):
        self.signal_new_points_material.emit()


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.lineEdit_textPointMaterialName.text()
    
    def getColor(self):     
        return self.__color_material_point
    
    def getBaseMesh(self):
        name = self.comboBox_PointMaterialBaseMesh.currentText()
        index = self.comboBox_PointMaterialBaseMesh.currentIndex()
        id_selected = self.comboBox_PointMaterialBaseMesh.itemData(index, Qt.UserRole)
        return [id_selected, name]
    
    def getNoPoints(self):
        return self.comboBox_PointMaterialNPoints.currentText()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    
    def addCardMaterialPoint(self, card_material_point):                  

        self.verticalLayout_containerCardMaterialPoint.addWidget(card_material_point)
        last_index = self.verticalLayout_containerCardMaterialPoint.count() - 1
        self.verticalLayout_containerCardMaterialPoint.insertWidget(last_index, self.frame_empty)
    
    def setListBaseMesh(self, mesh_data):              
        self.comboBox_PointMaterialBaseMesh.clear()
        for item_index in range(len(mesh_data)):
            mesh_id =mesh_data[item_index][0]
            mesh_name =mesh_data[item_index][1]
            mesh_color =mesh_data[item_index][2]            
            
            self.comboBox_PointMaterialBaseMesh.addItem(mesh_name)   

            color_icon = QColor(mesh_color)
            pixmap = QPixmap(20, 20)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setPen(QPen(color_icon, 3))
            painter.setBrush(Qt.NoBrush)
            painter.drawRoundedRect(pixmap.rect().adjusted(1, 1, -2, -2), 5, 5)
            painter.end()
            self.comboBox_PointMaterialBaseMesh.setItemIcon(item_index, QIcon(pixmap))    
            self.comboBox_PointMaterialBaseMesh.setItemData(self.comboBox_PointMaterialBaseMesh.count() - 1, mesh_id, Qt.UserRole)

    def setBaseMesh(self, index):     
        self.comboBox_PointMaterialBaseMesh.setCurrentIndex(index)
    
    def setListNoPoints(self):
        list_no_points = ["1x","2x"]
        for item_index in range(len(list_no_points)):
            self.comboBox_PointMaterialNPoints.addItem(list_no_points[item_index])    

    def setNoPoints(self, index):     
        self.comboBox_PointMaterialNPoints.setCurrentIndex(index)
    
    def endPointMaterial(self):
        self.lineEdit_textPointMaterialName.setText("")
        self.__color_material_point=None
        self.lineEdit_textPointMaterialColor.setStyleSheet('background-color : #333333')
        self.setBaseMesh(-1)
        self.setNoPoints(-1)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  MENSAJES         ::::::::::::::::::::
	###############################################################################

    def msnAlertName(self, error, msn=""):
        if not error:
            self.lineEdit_textPointMaterialName.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textPointMaterialName.setFocus()
            self.lineEdit_textPointMaterialName.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertColor(self, error, msn=""):
        if not error:
            self.lineEdit_textPointMaterialColor.setStyleSheet("border-color: #444444;background-color: {};".format(self.__color_material_point))
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textPointMaterialColor.setFocus()
            self.lineEdit_textPointMaterialColor.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertBaseMesh(self, error, msn=""):
        if not error:
            self.comboBox_PointMaterialBaseMesh.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.comboBox_PointMaterialBaseMesh.setFocus()
            self.comboBox_PointMaterialBaseMesh.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertNoPoints(self, error, msn=""):
        if not error:
            self.comboBox_PointMaterialNPoints.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.comboBox_PointMaterialNPoints.setFocus()
            self.comboBox_PointMaterialNPoints.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

