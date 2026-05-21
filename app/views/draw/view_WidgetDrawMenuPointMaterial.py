
from PySide6.QtCore import ( Signal, QSize,QTimer, Qt)
from PySide6.QtGui import (QIcon, QFont, QPixmap, QColor, QPainter, QPen)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy, QColorDialog, QFileDialog)

from ui.ui_widget_draw_menu_pointMaterial import Ui_FormDrawMenuPointMaterial
from utils import class_general
from utils import general_functions

class ViewWidgetDrawMenuPointMaterial(QFrame, Ui_FormDrawMenuPointMaterial):

    signal_new_points_material = Signal()  
    signal_show_hide_points_materials = Signal(bool)  
    signal_show_hide_label = Signal(bool)  
    signal_change_size_point = Signal()  
    
    signal_select_points_material = Signal()
    signal_cancel_select = Signal()
    signal_assing_points_material = Signal()
    

    def __init__(self):
        
        super(ViewWidgetDrawMenuPointMaterial, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_material_point = True
        self.__hide_show_frame_material_point_1=True
        self.__hide_show_frame_material_point_2=True
        self.__hide_show_frame_material_point_3=True

        self.__hide_show_poin_material=True
        self.__hide_show_label=True


        self.list_view_card = []
        self.path_file = None


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
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_poin_material = QIcon()
        self.icon_show_poin_material.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_poin_material = QIcon()
        self.icon_hide_poin_material.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        

        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('PUNTO MATERIAL')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)
        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Ocultar widgets de carga de archivo al inicio
        self.toolButton_PointMaterialUploadFile.setVisible(False)
        self.label_textPointMaterial_path.setVisible(False)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardPointMaterialSubTitle1.clicked.connect(self.__clickedToolButtonCardMeshSubTitle1)
        self.toolButton_cardPointMaterialSubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_cardPointMaterialSubTitle3.clicked.connect(self.__clickedToolButtonCardMeshSubTitle3)
        
        self.toolButton_showHidePointMaterial.clicked.connect(self.__clickedToolButtonShowHideMesh)
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)
        self.horizontalSlider_PointMaterialSize.valueChanged.connect(self.__valueChangedHorizontalSliderPointMaterialSize)
 
        
        # ::::::::::::::::::::      EVENTOS DRAW MENU POINT MATERIAL     ::::::::::::::::::::
        self.lineEdit_textPointMaterialName.editingFinished.connect(self.__editingFinishedLineEditPointMaterialName)
        self.toolButton_PointMaterialCancel.clicked.connect(self.__clickedToolButtonPointMaterialCancel)
        self.toolButton_PointMaterial.clicked.connect(self.__clickedToolButtonPointMaterial)
        
        
        # ::::::::::::::::::::      EVENTOS DRAW MENU ASIGNAR FUERZAS Y VEL     ::::::::::::::::::::
        self.toolButton_btnMPDrawSelected.clicked.connect(self.__clickedToolButtonMPSelected)
        self.lineEdit_textPM_Velx.editingFinished.connect(self.__editingFinishedLineEditVelx)
        self.lineEdit_textPM_Vely.editingFinished.connect(self.__editingFinishedLineEditVely)
        self.lineEdit_textPM_Felx.editingFinished.connect(self.__editingFinishedLineEditFelx)
        self.lineEdit_textPM_Fely.editingFinished.connect(self.__editingFinishedLineEditFely)
        self.toolButton_PointMaterialCancel_2.clicked.connect(self.__clickedToolButtonPointMaterialCancelAssing)
        self.toolButton_PointMaterialAssing.clicked.connect(self.__clickedToolButtonPointMaterialAssing)

        # Eventos carga por archivo
        self.comboBox_PointMaterialBaseMesh.currentIndexChanged.connect(self.__currentIndexChangedComboBoxBaseMesh)
        self.toolButton_PointMaterialUploadFile.clicked.connect(self.__clickedToolButtonUploadFile)

        
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """

        if self.__hide_show_frame_material_point == True:
            self.frame_pointMaterial.setVisible(False)
            self.__hide_show_frame_material_point = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_material_point == False:
            self.frame_pointMaterial.setVisible(True)
            self.__hide_show_frame_material_point = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)
    
    def __clickedToolButtonCardMeshSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_material_point_1 == True:
            self.frame_materialPoint2.setVisible(False)
            self.__hide_show_frame_material_point_1 = False
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_material_point_1 == False:
            self.frame_materialPoint2.setVisible(True)
            self.__hide_show_frame_material_point_1 = True
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_material_point_2 == True:
            self.frame_materialPoint3.setVisible(False)
            self.__hide_show_frame_material_point_2 = False
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_maximize)
            self.verticalSpacer_2.changeSize(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        elif self.__hide_show_frame_material_point_2 == False:
            self.frame_materialPoint3.setVisible(True)
            self.__hide_show_frame_material_point_2 = True
            self.toolButton_cardPointMaterialSubTitle2.setIcon(self.icon_minimize)
            self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)
    
    def __clickedToolButtonCardMeshSubTitle3(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_material_point_3 == True:
            self.frame_materialPoint4.setVisible(False)
            self.__hide_show_frame_material_point_3 = False
            self.toolButton_cardPointMaterialSubTitle3.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_material_point_3 == False:
            self.frame_materialPoint4.setVisible(True)
            self.__hide_show_frame_material_point_3 = True
            self.toolButton_cardPointMaterialSubTitle3.setIcon(self.icon_minimize)

    def __clickedToolButtonShowHideMesh(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_poin_material == True:
            self.__hide_show_poin_material = False
            self.signal_show_hide_points_materials.emit(self.__hide_show_poin_material)
            self.toolButton_showHidePointMaterial.setIcon(self.icon_hide_poin_material)
        elif self.__hide_show_poin_material == False:  
            self.__hide_show_poin_material = True
            self.signal_show_hide_points_materials.emit(self.__hide_show_poin_material)
            self.toolButton_showHidePointMaterial.setIcon(self.icon_show_poin_material)

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

    def __valueChangedHorizontalSliderPointMaterialSize(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        self.signal_change_size_point.emit()

    def __doubleClickedHorizontalSliderPointMaterialSize(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        self.horizontalSlider_PointMaterialSize.setValue(100)



    # ::::::::::::::::::::      EVENTOS DRAW MENU POINT MATERIAL     ::::::::::::::::::::
    def __editingFinishedLineEditPointMaterialName(self):
        self.lineEdit_textPointMaterialName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 


    def __clickedToolButtonPointMaterialCancel(self):
        self.endPointMaterial()

    def __clickedToolButtonPointMaterial(self):
        self.signal_new_points_material.emit()

    def __currentIndexChangedComboBoxBaseMesh(self):
        """Muestra u oculta los controles de carga por archivo segun la seleccion."""
        index = self.comboBox_PointMaterialBaseMesh.currentIndex()
        data = self.comboBox_PointMaterialBaseMesh.itemData(index, Qt.UserRole)
        is_file = (data is not None and data.get("mesh_type") == "Archivo")
        self.toolButton_PointMaterialUploadFile.setVisible(is_file)
        self.label_textPointMaterial_path.setVisible(is_file)
        # Ocultar seleccion de puntos por elemento cuando es Archivo (no aplica)
        self.comboBox_PointMaterialNPoints.setEnabled(not is_file)
        if not is_file:
            self.path_file = None
            self.label_textPointMaterial_path.setText("")

    def __clickedToolButtonUploadFile(self):
        """Abre el explorador de archivos y guarda la ruta del .txt seleccionado."""
        options = QFileDialog.Options()
        txt_file_path, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar archivo de puntos", "", "Text Files (*.txt)", options=options)
        if txt_file_path:
            self.path_file = txt_file_path
            # Mostrar solo el nombre del archivo, no la ruta completa
            import os
            self.label_textPointMaterial_path.setText(os.path.basename(txt_file_path))
        
    def __clickedToolButtonMPSelected(self):
        self.signal_select_points_material.emit()
        self.lineEdit_textMPSelected.setText("{} Puntos".format(0)) 
        self.setPropertyStyle(self.toolButton_btnMPDrawSelected, 4)   
        self.lineEdit_textMPSelected.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 
        
        
    def __editingFinishedLineEditVelx(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza factor damping en la copia de la bd del proyecto.
        si no es número da mensaje de error"""
        velx = self.lineEdit_textPM_Velx.text()
        if general_functions.isNumber(velx):
            self.lineEdit_textPM_Velx.setText(str(float(velx)))            
            self.lineEdit_textPM_Velx.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 

        else:            
            self.lineEdit_textPM_Velx.setFocus()
            self.lineEdit_textPM_Velx.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la velocidad en x")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
            
    def __editingFinishedLineEditVely(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza factor damping en la copia de la bd del proyecto.
        si no es número da mensaje de error"""
        vely = self.lineEdit_textPM_Vely.text()
        if general_functions.isNumber(vely):
            self.lineEdit_textPM_Vely.setText(str(float(vely)))            
            self.lineEdit_textPM_Vely.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 

        else:            
            self.lineEdit_textPM_Vely.setFocus()
            self.lineEdit_textPM_Vely.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la velocidad en y")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
        
    def __editingFinishedLineEditFelx(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza factor damping en la copia de la bd del proyecto.
        si no es número da mensaje de error"""
        felx = self.lineEdit_textPM_Felx.text()
        if general_functions.isNumber(felx):
            self.lineEdit_textPM_Felx.setText(str(float(felx)))            
            self.lineEdit_textPM_Felx.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 

        else:            
            self.lineEdit_textPM_Felx.setFocus()
            self.lineEdit_textPM_Felx.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la fuerza en x")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
            
    def __editingFinishedLineEditFely(self):
        """Verifica al salir del QLineEdit si el texto es
        un número, si es verdadero le da formato decimal y
        actualiza factor damping en la copia de la bd del proyecto.
        si no es número da mensaje de error"""
        fely = self.lineEdit_textPM_Fely.text()
        if general_functions.isNumber(fely):
            self.lineEdit_textPM_Fely.setText(str(float(fely)))            
            self.lineEdit_textPM_Fely.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 

        else:            
            self.lineEdit_textPM_Fely.setFocus()
            self.lineEdit_textPM_Fely.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText("Revisa la fuerza en y")          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))
            
    def __clickedToolButtonPointMaterialAssing(self):
        self.signal_assing_points_material.emit()
    
    def __clickedToolButtonPointMaterialCancelAssing(self):
        self.endPointMaterialAssing()
        self.signal_cancel_select.emit()
        
       

    
    def endPointMaterialAssing(self):        
        self.lineEdit_textMPSelected.setText("")
        self.lineEdit_textPM_Velx.setText('0.0')
        self.lineEdit_textPM_Vely.setText('0.0')
        self.lineEdit_textPM_Felx.setText('0.0')
        self.lineEdit_textPM_Fely.setText('0.0')
        self.lineEdit_textPM_Velx.setStyleSheet("border-color: #444444")
        self.lineEdit_textPM_Vely.setStyleSheet("border-color: #444444")
        self.lineEdit_textPM_Felx.setStyleSheet("border-color: #444444")
        self.lineEdit_textPM_Fely.setStyleSheet("border-color: #444444")
        self.setPropertyStyle(self.toolButton_btnMPDrawSelected, 1)


    def setPropertyStyle(self, widget, property: int):
        widget.setProperty("QToolButtonStyle", property)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()
    
    
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName(self):
        return self.lineEdit_textPointMaterialName.text()
    

    def getBaseMesh(self):
        """return [id_selected, name,mesh_type]"""
        name = self.comboBox_PointMaterialBaseMesh.currentText()
        index = self.comboBox_PointMaterialBaseMesh.currentIndex()
        if self.comboBox_PointMaterialBaseMesh.count() == 0:
            return ["","",""]
        id_selected = self.comboBox_PointMaterialBaseMesh.itemData(index, Qt.UserRole)["mesh_id"]
        mesh_type = self.comboBox_PointMaterialBaseMesh.itemData(index, Qt.UserRole)["mesh_type"]

        return [id_selected, name,mesh_type]
    
    def getProperty(self):
        """return [id_selected, name]"""
        name = self.comboBox_PointMaterialProperty.currentText()
        index = self.comboBox_PointMaterialProperty.currentIndex()
        if self.comboBox_PointMaterialProperty.count() == 0:
            return ["",""]
        id_selected = self.comboBox_PointMaterialProperty.itemData(index, Qt.UserRole)["id_property"]
        return [id_selected, name]
    

    def getNoPoints(self):
        return self.comboBox_PointMaterialNPoints.currentText()

    def getSizePoint(self):
        return self.horizontalSlider_PointMaterialSize.value()

    def getVoxVoy(self):
        """return [vox, voy] float float"""
        vox = self.lineEdit_textPM_Velx.text()
        voy = self.lineEdit_textPM_Vely.text()
        return [float(vox), float(voy)]
    
    def getFxFy(self):
        """return [fx, fy]"""
        fx = self.lineEdit_textPM_Felx.text()
        fy = self.lineEdit_textPM_Fely.text()
        return [float(fx), float(fy)]

    def getPathFile(self):
        """Retorna la ruta del archivo .txt seleccionado, o None si no hay."""
        return self.path_file

    def isFileMode(self):
        """True si la malla base seleccionada es de tipo Archivo."""
        index = self.comboBox_PointMaterialBaseMesh.currentIndex()
        data = self.comboBox_PointMaterialBaseMesh.itemData(index, Qt.UserRole)
        return data is not None and data.get("mesh_type") == "Archivo"


    def setListBaseMesh(self, mesh_data):      
        self.comboBox_PointMaterialBaseMesh.clear()
        for item_index in range(len(mesh_data)):
            mesh_id =mesh_data[item_index][0]
            mesh_name =mesh_data[item_index][1]
            mesh_color =mesh_data[item_index][2]   
            mesh_type =  mesh_data[item_index][3]         
            
            self.comboBox_PointMaterialBaseMesh.addItem(mesh_name)   

            color_icon = QColor(mesh_color)
            pixmap = QPixmap(20, 20)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setPen(QPen(color_icon, 3))
            painter.setBrush(QColor(color_icon.red(), color_icon.green(), color_icon.blue(), 50))
            painter.drawRect(1, 1, 18, 18)
            painter.end()

            self.comboBox_PointMaterialBaseMesh.setItemIcon(item_index, QIcon(pixmap))    
            self.comboBox_PointMaterialBaseMesh.setItemData(self.comboBox_PointMaterialBaseMesh.count() - 1, {"mesh_id": mesh_id, "mesh_type": mesh_type}, Qt.UserRole)

        # Agregar opcion "Archivo" al final
        archivo_index = self.comboBox_PointMaterialBaseMesh.count()
        self.comboBox_PointMaterialBaseMesh.addItem("📂  Archivo")
        self.comboBox_PointMaterialBaseMesh.setItemData(archivo_index, {"mesh_id": None, "mesh_type": "Archivo"}, Qt.UserRole)

    def setListProperties(self, properties_data): 
        
        self.comboBox_PointMaterialProperty.clear()
        for item_index in range(len(properties_data)):
            id_property =properties_data[item_index][0]
            name_property =properties_data[item_index][1]   
            color_property =properties_data[item_index][2]  
            
            self.comboBox_PointMaterialProperty.addItem(name_property) 

            # icono circulo con el color de la propiedad
            pixmap = QPixmap(20, 20)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setPen(QPen(QColor(color_property), 3))
            painter.setBrush(QColor(color_property))
            painter.drawEllipse(1, 1, 18, 18)
            painter.end()
            
            
            self.comboBox_PointMaterialProperty.setItemIcon(item_index, QIcon(pixmap))            
                 
            self.comboBox_PointMaterialProperty.setItemData(self.comboBox_PointMaterialProperty.count() - 1, {"id_property": id_property}, Qt.UserRole)





    def setBaseMesh(self, index):     
        self.comboBox_PointMaterialBaseMesh.setCurrentIndex(index)
    
    def setListNoPoints(self):
        list_no_points = ["1x","2x"]
        for item_index in range(len(list_no_points)):
            self.comboBox_PointMaterialNPoints.addItem(list_no_points[item_index])    

    def setNoPoints(self, index):     
        self.comboBox_PointMaterialNPoints.setCurrentIndex(index)
        
        
    def setNoSelectPointsMaterial(self, no_points):
        self.lineEdit_textMPSelected.setText("{} Puntos".format(no_points))
        self.setPropertyStyle(self.toolButton_btnMPDrawSelected, 1)
    
    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    
    def clearListProperties(self):
        self.comboBox_PointMaterialProperty.clear()
        

            
    def removeCardMaterialPoint(self ):
        view_card=None
        if len(self.list_view_card) != 0:
            for view_card in self.list_view_card: 
                self.verticalLayout_containerCardMaterialPoint.removeWidget(view_card)
                view_card.deleteLater()
            self.list_view_card=[]

    def addCardMaterialPoint(self, card_material_point):                  

        self.verticalLayout_containerCardMaterialPoint.addWidget(card_material_point)
        self.list_view_card.append(card_material_point)
        last_index = self.verticalLayout_containerCardMaterialPoint.count() - 1
        self.verticalLayout_containerCardMaterialPoint.insertWidget(last_index, self.frame_empty)
    
    def endPointMaterial(self):
        self.lineEdit_textPointMaterialName.setText("")
        self.path_file = None
        self.label_textPointMaterial_path.setText("")
        self.setBaseMesh(0)
        self.setNoPoints(0)
        
    def endVectorQuantity(self):
        self.lineEdit_textPM_Velx.setText('0.0')
        self.lineEdit_textPM_Vely.setText('0.0')
        self.lineEdit_textPM_Felx.setText('0.0')
        self.lineEdit_textPM_Fely.setText('0.0')
        self.lineEdit_textMPSelected.setText("")

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
            
    def msnAlertSelect(self, error, msn=""):
        if not error:
            self.lineEdit_textMPSelected.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMPSelected.setFocus()
            self.lineEdit_textMPSelected.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

