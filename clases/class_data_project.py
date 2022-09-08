from cmath import inf
from importlib.resources import path
import time
from tokenize import String
from unicodedata import name
from PySide6.QtCore import ( QObject,QEvent, Signal, Slot,QThread, QSize,)
from PySide6.QtGui import (QColor,QIcon,QPainter,QFontMetrics,QFont)
from PySide6.QtWidgets import ( QFrame, QGraphicsDropShadowEffect,QWidget,QLabel,QHBoxLayout,QSpacerItem,QSizePolicy)

from ui import ui_widget_data_project
from clases import data_base
from clases import functions_general
from clases import class_general


class DataProject(QFrame, ui_widget_data_project.Ui_FormDataProject):
    signal_msn_critical = Signal(str)    
    signal_msn_Satisfactory = Signal(str)    
    signal_msn_Informative = Signal(str)        
    
    def __init__(self):
        super(DataProject, self).__init__()
        self.setupUi(self)
        self.hide_show_frame_data_1=True
        self.hide_show_frame_data_2=True
        self.hide_show_frame_data=True


        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"recursos/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)
        
        self.label_lat = class_general.QLabelVertical('INFORMACIÓN DEL PROYECTO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}"); 
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)

        '''
        # se lee los proyectos de db y se almacenan como objetos en list_projects
        self.db_project = data_base.DataBaseProject(path=path)

        info = self.db_project.getInformationDB()
        data_config = self.db_project.getConfigDB()
        print(info)
        print(type(info))
        self.setTextWidget(info,data_config)

        '''

        """
        for info in self.db_project.getInformationDB():
            print(info)
            print(type(info))
            name = info['nombreArchivo']
            path = info['ruta']
            data = info['fecha']
            hour = info['hora']
            self.list_projects.append(Project(name_file=name, path=path, data=data, hour=hour))

        """
        # :::::::::::::::::::::::::::::::::::    EVENTOS   :::::::::::::::::::::::::::::::::::
        self.lineEdit_WDP_5.editingFinished.connect(self.editingFinishedLineEditWDP5)
        self.toolButton_saveData.clicked.connect(self.clickedToolButtonSaveData)
        self.toolButton_hide_show.clicked.connect(self.clickedToolButtonHideShow)
        self.toolButton_cardDataSubTitle_1.clicked.connect(self.clickedToolButtonCardDataSubTitle1)
        self.toolButton_cardDataSubTitle_2.clicked.connect(self.clickedToolButtonCardDataSubTitle2)

    def editingFinishedLineEditWDP5(self):
        gravity=self.lineEdit_WDP_5.text()
        gravity = functions_general.addZeroNumber(gravity)
        self.lineEdit_WDP_5.setText(gravity)


    def clickedToolButtonSaveData(self):
        name_project=self.lineEdit_WDP_1.text()
        location=self.lineEdit_WDP_2.text()
        author=self.lineEdit_WDP_3.text()
        description=self.textEdit_WDP_4.toPlainText()
        self.lineEdit_WDP_1.setFocus()
        self.lineEdit_WDP_5.setFocus()
        gravity=self.lineEdit_WDP_5.text()

        if not functions_general.IsNumber(gravity):
            self.signal_msn_critical.emit("Revisa la gravedad")
            return
        
        if(self.db_project.addInformationDB(name_project=name_project,location=location,author=author,description=description)):
            if(self.db_project.addConfigDB(gravity=gravity)):
                self.signal_msn_Satisfactory.emit("Información guardada correctamente")
            else:
                self.signal_msn_critical.emit("Error al guardar la información ")
        else:
            self.signal_msn_critical.emit("Error al guardar la información ")

    def clickedToolButtonHideShow(self):
        if self.hide_show_frame_data == True:
            self.frame_data.setVisible(False)
            self.hide_show_frame_data = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide_2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)
        elif self.hide_show_frame_data == False:
            self.frame_data.setVisible(True)
            self.hide_show_frame_data = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide_2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)
        

    def clickedToolButtonCardDataSubTitle1(self):
        if self.hide_show_frame_data_1 == True:
            self.frame_data_1.setVisible(False)
            self.hide_show_frame_data_1 = False
            self.toolButton_cardDataSubTitle_1.setIcon(self.icon_maximize)
        elif self.hide_show_frame_data_1 == False:
            self.frame_data_1.setVisible(True)
            self.hide_show_frame_data_1 = True
            self.toolButton_cardDataSubTitle_1.setIcon(self.icon_minimize)

    def clickedToolButtonCardDataSubTitle2(self):
        if self.hide_show_frame_data_2 == True:
            self.frame_data_2.setVisible(False)
            self.hide_show_frame_data_2 = False
            self.toolButton_cardDataSubTitle_2.setIcon(self.icon_maximize)
        elif self.hide_show_frame_data_2 == False:
            self.frame_data_2.setVisible(True)
            self.hide_show_frame_data_2 = True
            self.toolButton_cardDataSubTitle_2.setIcon(self.icon_minimize)




    def setTextWidget(self):

        data_info = self.db_project.getInformationDB()
        data_config = self.db_project.getConfigDB()
        self.lineEdit_WDP_1.setText(data_info["NOMBREPROYECTO"])
        self.lineEdit_WDP_2.setText(data_info["LOCALIZACION"])
        self.lineEdit_WDP_3.setText(data_info["AUTOR"])
        self.textEdit_WDP_4.setText(data_info["DESCRIPCION"])
        self.lineEdit_WDP_5.setText("{}".format(data_config["GRAVEDAD"]))

    def setPathProject(self, path):
        self.db_project = data_base.DataBaseProject(path=path)


