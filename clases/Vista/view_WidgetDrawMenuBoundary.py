
from PySide6.QtCore import ( Signal, QSize,QTimer)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy)
from ui.ui_widget_draw_menu_boundary import Ui_FormDrawMenuBoundary
from clases import class_general


class ViewWidgetDrawMenuBoundary(QFrame, Ui_FormDrawMenuBoundary):

    signal_select_point_mesh= Signal() 
    signal_new_boundary_automatic= Signal() 
    signal_new_boundary_manual= Signal() 
    signal_show_hide_boundaries = Signal(bool)
    signal_show_hide_labels = Signal(bool)



    def __init__(self):
        super(ViewWidgetDrawMenuBoundary, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_boundary=True
        self.__hide_show_frame_boundary_1=True
        self.__hide_show_frame_boundary_2=True
        self.__hide_show_frame_boundary_3=True

        self.__hide_show_boundary=True
        self.__hide_show_label=True

        self.list_view_card =[]
        self.user_interaction = False

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
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_boundary = QIcon()
        self.icon_show_boundary.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_boundary = QIcon()
        self.icon_hide_boundary.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_show_label = QIcon()
        self.icon_show_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_hide_label = QIcon()
        self.icon_hide_label.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        

        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('CONTORNO')
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
        self.toolButton_cardBoundarySubTitle1.clicked.connect(self.__clickedToolButtonCardMeshSubTitle1)
        self.toolButton_cardBoundarySubTitle2.clicked.connect(self.__clickedToolButtonCardMeshSubTitle2)
        self.toolButton_cardBoundarySubTitle3.clicked.connect(self.__clickedToolButtonCardMeshSubTitle3)
        self.toolButton_showHideBoundary.clicked.connect(self.__clickedToolButtonShowHideMesh)
        self.toolButton_showHideLabel.clicked.connect(self.__clickedToolButtonShowHideLabel)

        # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::

        self.lineEdit_textBoundaryName.editingFinished.connect(self.__editingFinishedLineEditBoundaryName)
        self.toolButton_cardBoundaryDrawSelected.clicked.connect(self.__clickedToolButtonBoundarySelected)
        self.toolButton_boundaryCancel_2.clicked.connect(self.__clickedToolButtonBoundaryCancel)
        self.toolButton_boundaryCreate_1.clicked.connect(self.__clickedToolButtonBoundaryCreate1)
        self.toolButton_boundaryCreate_2.clicked.connect(self.__clickedToolButtonBoundaryCreate2)
        

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     :::::::::::::::::::: 
    def __clickedToolButtonHideShow(self):
        """ Muestra o oculta el menú data de draw """
        if self.__hide_show_frame_boundary == True:
            self.frame_boundary.setVisible(False)
            self.__hide_show_frame_boundary = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.__hide_show_frame_boundary == False:
            self.frame_boundary.setVisible(True)
            self.__hide_show_frame_boundary = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)

    def __clickedToolButtonCardMeshSubTitle1(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_boundary_1 == True:
            self.frame_boundary1.setVisible(False)
            self.__hide_show_frame_boundary_1 = False
            self.toolButton_cardBoundarySubTitle1.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_boundary_1 == False:
            self.frame_boundary1.setVisible(True)
            self.__hide_show_frame_boundary_1 = True
            self.toolButton_cardBoundarySubTitle1.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle2(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_boundary_2 == True:
            self.frame_boundary2.setVisible(False)
            self.__hide_show_frame_boundary_2 = False
            self.toolButton_cardBoundarySubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_boundary_2 == False:
            self.frame_boundary2.setVisible(True)
            self.__hide_show_frame_boundary_2 = True
            self.toolButton_cardBoundarySubTitle2.setIcon(self.icon_minimize)

    def __clickedToolButtonCardMeshSubTitle3(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_frame_boundary_3 == True:
            self.frame_boundary3.setVisible(False)
            self.__hide_show_frame_boundary_3 = False
            self.toolButton_cardBoundarySubTitle3.setIcon(self.icon_maximize)
            self.verticalSpacer_2.changeSize(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        elif self.__hide_show_frame_boundary_3 == False:
            self.frame_boundary3.setVisible(True)
            self.__hide_show_frame_boundary_3 = True
            self.toolButton_cardBoundarySubTitle3.setIcon(self.icon_minimize)
            self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __clickedToolButtonShowHideMesh(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_boundary == True:
            self.__hide_show_boundary = False
            self.signal_show_hide_boundaries.emit(self.__hide_show_boundary)
            self.toolButton_showHideBoundary.setIcon(self.icon_hide_boundary)
        elif self.__hide_show_boundary == False:  
            self.__hide_show_boundary = True
            self.signal_show_hide_boundaries.emit(self.__hide_show_boundary)
            self.toolButton_showHideBoundary.setIcon(self.icon_show_boundary)

    def __clickedToolButtonShowHideLabel(self):
        """ Muestra o oculta el submenú data de draw  >  configuración del proyecto """
        if self.__hide_show_label == True:
            self.signal_show_hide_labels.emit(self.__hide_show_label)
            self.__hide_show_label = False
            self.toolButton_showHideLabel.setIcon(self.icon_show_label)
        elif self.__hide_show_label == False:
            self.signal_show_hide_labels.emit(self.__hide_show_label)
            self.__hide_show_label = True
            self.toolButton_showHideLabel.setIcon(self.icon_hide_label)

    # ::::::::::::::::::::      EVENTOS DRAW MENU BOUNDARY     ::::::::::::::::::::


    def __editingFinishedLineEditBoundaryName(self):
        self.lineEdit_textBoundaryName.setStyleSheet("border-color: #444444")
        self.label_msn.setText("Empty")
        self.label_msn.setStyleSheet("color: #333333") 

    def __clickedToolButtonBoundarySelected(self):
        self.signal_select_point_mesh.emit()
        self.lineEdit_textBoundarySelected.setText("{} Elementos".format(0)) 
        self.setPropertyStyle(self.toolButton_cardBoundaryDrawSelected, 4)   
        
    def __clickedToolButtonBoundaryCancel(self):
        self.endBoundary2()
          
    def __clickedToolButtonBoundaryCreate1(self):
        self.signal_new_boundary_automatic.emit()

    def __clickedToolButtonBoundaryCreate2(self):
        self.signal_new_boundary_manual.emit()





 ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getName (self):        
        return self.lineEdit_textBoundaryName.text()
    
    def getTx (self):        
        return self.checkBox_BoundaryRestrictionTX.checkState()
    
    def getTy (self):
        return self.checkBox_BoundaryRestrictionTY.checkState() 
    
    def getTxTyAutomatic (self):
        result ={
            "Top":[self.checkBox_BoundaryRestrictionTXTop.isChecked() ,self.checkBox_BoundaryRestrictionTYTop.isChecked()],
            "Bottom":[self.checkBox_BoundaryRestrictionTXBottom.isChecked() ,self.checkBox_BoundaryRestrictionTYBottom.isChecked()],
            "Left":[self.checkBox_BoundaryRestrictionTXleft.isChecked() ,self.checkBox_BoundaryRestrictionTYleft.isChecked()],
            "Right":[self.checkBox_BoundaryRestrictionTXRight.isChecked() ,self.checkBox_BoundaryRestrictionTYRight.isChecked()],
        }
        return result
    
        
    def getShowBoundary(self):
        return self.__hide_show_mesh


    def setNoSelectPointsMesh(self, no_lines):
        self.lineEdit_textBoundarySelected.setText("{} Elementos".format(no_lines))   
        self.setPropertyStyle(self.toolButton_cardBoundaryDrawSelected, 1)
    

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	##############################################################################

    def removeCardBoundary(self):
        view_card=None
        if len(self.list_view_card) != 0:
            for view_card in self.list_view_card: 
                self.verticalLayout_containerCardBoundary.removeWidget(view_card)
                view_card.deleteLater()
            self.list_view_card=[]


    def addCardBoundary(self, card_boundary):
        self.verticalLayout_containerCardBoundary.addWidget(card_boundary)
        self.list_view_card.append(card_boundary)
        last_index = self.verticalLayout_containerCardBoundary.count() - 1
        self.verticalLayout_containerCardBoundary.insertWidget(last_index, self.frame_empty)

    def endBoundary1(self):
        self.checkBox_BoundaryRestrictionTXTop.setChecked(False)
        self.checkBox_BoundaryRestrictionTXBottom.setChecked(True)
        self.checkBox_BoundaryRestrictionTXleft.setChecked(True)
        self.checkBox_BoundaryRestrictionTXRight.setChecked(True)

        self.checkBox_BoundaryRestrictionTYTop.setChecked(False)
        self.checkBox_BoundaryRestrictionTYBottom.setChecked(True)
        self.checkBox_BoundaryRestrictionTYleft.setChecked(False)
        self.checkBox_BoundaryRestrictionTYRight.setChecked(False)
        
    def endBoundary2(self):
        self.lineEdit_textBoundaryName.setText("")
        self.lineEdit_textBoundarySelected.setText("")
        self.setPropertyStyle(self.toolButton_cardBoundaryDrawSelected, 1)
        self.checkBox_BoundaryRestrictionTX.setChecked(False)
        self.checkBox_BoundaryRestrictionTY.setChecked(False)
      
        
    def setPropertyStyle(self, widget, property: int):
        widget.setProperty("QToolButtonStyle", property)
        widget.style().unpolish(widget)
        widget.style().polish(widget)
        widget.update()