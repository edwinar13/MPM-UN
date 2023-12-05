""" Este módulo contiene la clase Ui_FormDrawMenuMesh, para incluirla en frame draw
es el widget menú de mallas."""

from PySide6.QtCore import ( Signal, QSize,QTimer, Qt)
from PySide6.QtGui import (QIcon, QFont,QTransform, QPen, QBrush, QPolygonF, QColor, QPalette)
from PySide6.QtWidgets import ( QLabel,QFrame, QSpacerItem, QSizePolicy,QColorDialog)
from ui.ui_widget_draw_menu_mesh import Ui_FormDrawMenuMesh
from clases import class_general


class ViewWidgetDrawMenuMesh(QFrame, Ui_FormDrawMenuMesh):
    """Esta clase crea el QFrame draw-menu-mesh para agregarlo a Frame Draw.

    Args:
            scene (QGraphicsScene): es la escena actual para draw
            view (QGraphicsView): es la vista actual para draw

    Attributes:
            name_mesh (str): 
            color_mesh (str):
            size_element_mesh (str):
            selected_objects (str):
            gravity (str):
            projectActual (Project): Objeto del proyecto actual.
            graphicsScene (QGraphicsScene): es la escena actual para draw
            graphicsView (QGraphicsView): es la vista actual para draw

            hide_show_frame_data_1 (bool): Estado hide-Show de draw-menu-mesh Dibujo.
            hide_show_frame_data_2 (bool): Estado hide-Show de draw-menu-mesh Malla Regular cuadrilátero.
            hide_show_frame_data_3 (bool): Estado hide-Show de draw-menu-mesh lista de mallas.
            hide_show_frame_data (bool): Esatdo hide-Show draw-menu-mesh.
            
    Method:
            :

    """ 
    signal_select_line_mesh= Signal() 
    signal_size_mesh= Signal() 
    signal_new_mesh= Signal() 
    signal_mesh_back_changed = Signal()
    signal_mesh_back_show= Signal(bool) 
    signal_show_hide_meshs = Signal(bool)
    signal_show_hide_label = Signal(bool)
    
    
    def __init__(self):

        super(ViewWidgetDrawMenuMesh, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_mesh=True
        self.__hide_show_frame_mesh_0=True
        self.__hide_show_frame_mesh_1=True
        self.__hide_show_frame_mesh_2=True

        self.__hide_show_mesh=True
        self.__hide_show_label=True

        self.list_view_card =[]
        self.user_interaction = False

        self.__color_mesh = None
        self.contador=0

        # Configura la UI
        self.__configUi()
        self.__initEventUi()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """ 
        
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_mesh = QIcon()
        self.icon_show_mesh.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_mesh = QIcon()
        self.icon_hide_mesh.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
                
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('MALLADO')
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
        self.toolButton_cardMeshSubTitle0.clicked.connect(self.__clickedToolButtonCardMeshSubTitle0)
        self.toolButton_cardMeshSubTitle1.clicked.connect(self.__clickedToolButtonCardMeshSubTitle1)
        self.toolButton_cardMeshSubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_showHideMesh.clicked.connect(self.__clickedToolButtonShowHideMesh)
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)

        # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::
        self.toolButton_meshShow.clicked.connect(self.__clickedToolButton_meshShow)
        self.toolButton_meshHide.clicked.connect(self.__clickedToolButton_meshHide)       
        self.toolButton_cardMeshDrawUpdate.clicked.connect(self.__clickedToolButton_meshUpdate) 
        self.lineEdit_textMeshName.editingFinished.connect(self.__editingFinishedLineEditMeshName)
        self.toolButton_cardMeshDrawSize.clicked.connect(self.__clickedToolButtonSizeMesh)  
        self.toolButton_cardMeshDrawSelected.clicked.connect(self.__clickedToolButtonSelectLine)  
        self.toolButton_cardMeshDrawColor.clicked.connect(self.__clickedToolButtonColorPicker)        
        self.toolButton_meshCancel.clicked.connect(self.__clickedToolButtonMeshCancel)
        self.toolButton_meshMeshing.clicked.connect(self.__clickedToolButton_mesh)
        
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     :::::::::::::::::::: 
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """
        if self.__hide_show_frame_mesh == True:
            self.frame_mesh.setVisible(False)
            self.__hide_show_frame_mesh = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_mesh == False:
            self.frame_mesh.setVisible(True)
            self.__hide_show_frame_mesh = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)

    def __clickedToolButtonCardMeshSubTitle0(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_mesh_0 == True:
            self.frame_mesh2_2.setVisible(False)
            self.__hide_show_frame_mesh_0 = False
            self.toolButton_cardMeshSubTitle0.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_mesh_0 == False:
            self.frame_mesh2_2.setVisible(True)
            self.__hide_show_frame_mesh_0 = True
            self.toolButton_cardMeshSubTitle0.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_mesh_1 == True:
            self.frame_mesh2.setVisible(False)
            self.__hide_show_frame_mesh_1 = False
            self.toolButton_cardMeshSubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_mesh_1 == False:
            self.frame_mesh2.setVisible(True)
            self.__hide_show_frame_mesh_1 = True
            self.toolButton_cardMeshSubTitle1.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_mesh_2 == True:
            self.frame_mesh3.setVisible(False)
            self.__hide_show_frame_mesh_2 = False
            self.toolButton_cardMeshSubTitle2.setIcon(self.icon_maximize)
            self.verticalSpacer_2.changeSize(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        elif self.__hide_show_frame_mesh_2 == False:
            self.frame_mesh3.setVisible(True)
            self.__hide_show_frame_mesh_2 = True
            self.toolButton_cardMeshSubTitle2.setIcon(self.icon_minimize)
            self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __clickedToolButtonShowHideMesh(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_mesh == True:
            self.__hide_show_mesh = False
            self.signal_show_hide_meshs.emit(self.__hide_show_mesh)
            self.toolButton_showHideMesh.setIcon(self.icon_hide_mesh)
        elif self.__hide_show_mesh == False:  
            self.__hide_show_mesh = True
            self.signal_show_hide_meshs.emit(self.__hide_show_mesh)
            self.toolButton_showHideMesh.setIcon(self.icon_show_mesh)

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


    # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::

  
    def __clickedToolButton_meshUpdate(self):
        if self.user_interaction:
            self.signal_mesh_back_changed.emit()
        

    def __clickedToolButton_meshHide(self):
        self.setPropertyStyle(self.toolButton_meshShow, 6)
        self.setPropertyStyle(self.toolButton_meshHide, 7)
        self.signal_mesh_back_show.emit(False)

    def __clickedToolButton_meshShow(self):
        self.setPropertyStyle(self.toolButton_meshShow, 5)
        self.setPropertyStyle(self.toolButton_meshHide, 8)
        self.signal_mesh_back_show.emit(True)
     
    def __editingFinishedLineEditMeshName(self):
        self.lineEdit_textMeshName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 
          
    def __clickedToolButtonColorPicker(self):
        self.setPropertyStyle(self.toolButton_cardMeshDrawColor, 4)             
        color = QColorDialog.getColor(initial=QColor(200,200,200))
        if color.isValid():
            self.__color_mesh=color.name()
            self.lineEdit_textMeshColor.setStyleSheet('background-color : {}'.format(self.__color_mesh))
        self.setPropertyStyle(self.toolButton_cardMeshDrawColor, 1)

    def __clickedToolButtonSelectLine(self):
        self.signal_select_line_mesh.emit()
        self.lineEdit_textMeshSelected.setText("{} Elementos".format(0)) 
        self.setPropertyStyle(self.toolButton_cardMeshDrawSelected, 4)
        self.setPropertyStyle(self.toolButton_cardMeshDrawSize, 1)

    def __clickedToolButtonSizeMesh(self):
        self.signal_size_mesh.emit()
        self.setPropertyStyle(self.toolButton_cardMeshDrawSize, 4)
        self.setPropertyStyle(self.toolButton_cardMeshDrawSelected, 1)

    def __clickedToolButtonMeshCancel(self):
        self.endMesh()

    def __clickedToolButton_mesh(self):
        self.signal_new_mesh.emit()

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName (self):        
        return self.lineEdit_textMeshName.text()
    
    def getColor (self):        
        return self.__color_mesh
    
    def getSize (self):
        return self.doubleSpinBoxl_textMeshSize.value()    
    
    def getType (self):
        return self.comboBox_MeshType.currentText()
    
    def getMeshDx(self):
        return self.doubleSpinBoxl_textMeshDx.value()

    def getMeshDy(self):
        return self.doubleSpinBoxl_textMeshDy.value()
        
    def getMeshBackSize(self):
        return self.doubleSpinBoxl_textMeshSize_2.value()
    
        
    def getShowMesh(self):
        return self.__hide_show_mesh



    def setNoSelectLineMesh(self, no_lines):
        self.lineEdit_textMeshSelected.setText("{} Elementos".format(no_lines))   
        self.setPropertyStyle(self.toolButton_cardMeshDrawSelected, 1)
    
    def setSizeMesh(self, dist):
        self.doubleSpinBoxl_textMeshSize.setValue(dist)
        self.setPropertyStyle(self.toolButton_cardMeshDrawSize, 1)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def removeCardMesh(self ):
        view_card=None
        if len(self.list_view_card) != 0:
            for view_card in self.list_view_card: 
                self.verticalLayout_containerCardMesh.removeWidget(view_card)
                view_card.deleteLater()
            self.list_view_card=[]


    def addCardMesh(self, card_mesh):
        self.verticalLayout_containerCardMesh.addWidget(card_mesh)
        self.list_view_card.append(card_mesh)
        last_index = self.verticalLayout_containerCardMesh.count() - 1
        self.verticalLayout_containerCardMesh.insertWidget(last_index, self.frame_empty)

    def endMesh(self):
        self.lineEdit_textMeshName.setText("")
        self.__color_mesh=None
        self.lineEdit_textMeshColor.setStyleSheet('background-color : #333333')
        self.lineEdit_textMeshSelected.setText("")
        self.doubleSpinBoxl_textMeshSize.setValue(1)
        self.setPropertyStyle(self.toolButton_cardMeshDrawSelected, 1)
        self.setPropertyStyle(self.toolButton_cardMeshDrawSize, 1)
        self.setType(0)

    def setPropertyStyle(self, widget, property: int):

        widget.setProperty("QToolButtonStyle", property)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()

    def setListTypes(self):
        list_types = ["Triangular","Cuadrilátera"]
        for item_index in range(len(list_types)):
            self.comboBox_MeshType.addItem(list_types[item_index])  

    def setType(self, index):     
        self.comboBox_MeshType.setCurrentIndex(index)
    

    def setTextWidgetMeshBack(self, data):
        size_dx=data[0]
        size_dy=data[1]
        size_element=data[2]
        color=data[3]

        self.doubleSpinBoxl_textMeshDx.setValue(size_dx)
        self.doubleSpinBoxl_textMeshDy.setValue(size_dy)
        self.doubleSpinBoxl_textMeshSize_2.setValue(size_element)
        self.user_interaction =True





    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  MENSAJES         ::::::::::::::::::::
	##############################################################################

    def msnAlertName(self, error, msn=""):
        if not error:
            self.lineEdit_textMeshName.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMeshName.setFocus()
            self.lineEdit_textMeshName.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertColor(self, error, msn=""):
        if not error:
            self.lineEdit_textMeshColor.setStyleSheet("border-color: #444444;background-color: {};".format(self.__color_mesh))
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMeshColor.setFocus()
            self.lineEdit_textMeshColor.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlertSelected(self, error, msn=""):
        if not error:
            self.lineEdit_textMeshSelected.setStyleSheet("border-color: #444444")
            self.label_msn.setText("Empty")
            self.label_msn.setStyleSheet("color: #333333") 
            
        else:
            self.lineEdit_textMeshSelected.setFocus()
            self.lineEdit_textMeshSelected.setStyleSheet("border: 1px solid #F94646")  
            self.label_msn.setStyleSheet("color:  #F94646")  
            self.label_msn.setText(msn)          
            QTimer.singleShot(4000, lambda: self.label_msn.setText(""))

    def msnAlert(self, error, msn=""):
            if not error:
                self.label_msn.setStyleSheet("border-radius: 3px ;padding-top: 4px; padding-bottom: 4px;background: #aaa; color:  #222;")  
                self.label_msn.setText(msn)          
                QTimer.singleShot(4000, self.clearLabel)

            else:
                self.label_msn.setStyleSheet("color:  #F94646")  
                self.label_msn.setText(msn)          
                QTimer.singleShot(4000, lambda: self.clearLabel)

    def clearLabel(self):
        self.label_msn.setText("")
        self.label_msn.setStyleSheet("border-radius: 0px ;padding-top: 0px; padding-bottom: 0px;background: transparent; color: #222;")
