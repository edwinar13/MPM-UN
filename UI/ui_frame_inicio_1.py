# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_inicio_1vchaew.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QScrollArea, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_FormHome(object):
    def setupUi(self, FormHome):
        if not FormHome.objectName():
            FormHome.setObjectName(u"FormHome")
        FormHome.resize(684, 679)
        FormHome.setStyleSheet(u"\n"
"/*Colores primarios*/\n"
"/* \n"
"gris oscuro #222222 #333333 #444444\n"
"gris claro #999999 #DDDDDD\n"
"verde claro #C8CC8E\n"
"vinotinto #742427\n"
"*/\n"
"/*Colores secundarios */\n"
"/* \n"
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"\n"
"/* Funetes/*\n"
"\n"
"/*\n"
"italic: font: italic 9pt \"Ubuntu\";\n"
"regular: font: 9pt \"Ubuntu\";\n"
"light: font: 300 9pt \"Ubuntu\";\n"
"medium: font: 500 9pt \"Ubuntu\";\n"
"bold: font: 700 9pt \"Ubuntu\";\n"
"*/\n"
"\n"
"/****************************************************************************************************************************************************/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QMainWindow#MainWindow{\n"
"background: #333333;\n"
"}\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*####################       MENU BAR SUP      ###########################*/\n"
"/*#################################################################*/\n"
""
                        "\n"
"QMenuBar#menubar {\n"
"background-color: #333333;\n"
"spacing: 5px; \n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubuntu\";\n"
"}\n"
"QMenuBar#menubar::item {\n"
"padding: 5px 5px;\n"
"background-color: transparent;\n"
"border-radius: 2px;\n"
"}\n"
"QMenuBar#menubar::item:selected { \n"
"background-color: #222222;\n"
"}\n"
"QMenuBar#menubar::item:pressed {\n"
"background-color: #222222;\n"
"}\n"
"QMenu {\n"
"background-color: #333333;\n"
"border-radius: 4px; \n"
"border: 1px solid #222222;\n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubuntu\";\n"
"}\n"
"QMenu::item {\n"
"background-color: transparent; \n"
"padding: 5px 20px;\n"
"margin: 2px 10px; \n"
"}\n"
"QMenu::item:selected { \n"
"background-color: #444444;\n"
"color: #C8CC8E;\n"
"font: 500 10pt \"Ubuntu\";\n"
"}\n"
"QMenu::item:checked {\n"
"color: #DDDDDD;\n"
"}\n"
"QMenu::item:unchecked { \n"
"color: #999999;\n"
"}\n"
"\n"
"\n"
"\n"
"QStatusbar#statusbar{\n"
"background-color: #333333;\n"
"}\n"
"\n"
"/*######################################################"
                        "###########*/\n"
"/*####################     FRAME MENU IZQ      ##########################*/\n"
"/*#################################################################*/\n"
"\n"
"QToolButton#toolButton_inicio,\n"
"QToolButton#toolButton_resultados,\n"
"QToolButton#toolButton_puntos,\n"
"QToolButton#toolButton_contorno,\n"
"QToolButton#toolButton_data,\n"
"QToolButton#toolButton_malla,\n"
"QToolButton#toolButton_resultados,\n"
"QToolButton#toolButton_config{\n"
"background-color: transparent;\n"
"color: #DDDDDD;\n"
"font: 500 7pt \"Ubuntu\";\n"
"border: none;\n"
"padding: 8px 0px;\n"
"}\n"
"\n"
"QFrame#frame_inicio{\n"
"background: #222222;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QFrame#frame_resultados,\n"
"QFrame#frame_puntos,\n"
"QFrame#frame_contorno,\n"
"QFrame#frame_data,\n"
"QFrame#frame_malla{\n"
"background: #333333;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"/*#################################################################*/\n"
"/*#####################"
                        "#      CONTAINER PAGE       ############################*/\n"
"/*#################################################################*/\n"
"\n"
"QFrame#frame_empty{\n"
"background-color: #444444;\n"
"}\n"
"\n"
"QFrame#frame_empty_draw{\n"
"background-color: #222222;\n"
"}\n"
"\n"
"/*#################################################################*/\n"
"/*######################      PAGE HOME      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"QLabel#label_title_1{\n"
"color: #DDDDDD; \n"
"font: 500 30pt \"Ubuntu\";\n"
"}\n"
"QLabel#label_title_2{\n"
"color: #C8CC8E;\n"
"font: 700 30pt \"Ubuntu\";\n"
"font-weight:bold;\n"
"}\n"
"QFrame#frame_infEjemplos1,\n"
"QFrame#frame_infEjemplos2,\n"
"QFrame#frame_infAbrirProyecto,\n"
"QFrame#frame_infNuevoProyecto{\n"
"background-color: #C8CC8E;\n"
"border-radius: 10px\n"
"}\n"
"QFrame#frame_supEjemplos1,\n"
"QFrame#frame_supEjemplos2,\n"
"QFrame#frame_supAbrirProyecto,\n"
"QFrame#frame_supNuevoProyecto{\n"
""
                        "background-color: #DDDDDD;\n"
"border-radius: 10px\n"
"}\n"
"QToolButton#toolButton_abrirProyecto,\n"
"QToolButton#toolButton_nuevoProyecto,\n"
"QToolButton#toolButton_ejemplos1,\n"
"QToolButton#toolButton_ejemplos2{\n"
"background-color: transparent;\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #222222;\n"
"}\n"
"/*\n"
"#frame_card_1, #frame_card_2{\n"
"background: #333333;\n"
"border-radius: 5px\n"
"}\n"
"*/\n"
"QFrame#frame_proyectos{\n"
" background: #444444;\n"
"border-radius: 5px;\n"
"  }\n"
"\n"
"\n"
"/*\n"
"Esto no funciona pero lo necesito ajustar\n"
"QFrame#frame_proyectos > QLabel{\n"
"color: #DDDDDD;\n"
"font: 500 9pt \"Ubuntu\";\n"
"}\n"
"*/\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*######################      PAGE DRAW      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"\n"
"/*###################### graphicsView draw  ############################*/\n"
"QGraphicsView#graphicsView_draw{\n"
""
                        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.943, stop:0 rgba(175, 175, 175, 255), stop:0.971591 rgba(141, 211, 211, 220), stop:1 rgba(170, 255, 255, 255));\n"
"}\n"
"\n"
"/*###################### frame consola  ############################*/\n"
"\n"
"QFrame#frame_console{\n"
"background-color: #333333;\n"
"}\n"
"QTextBrowser#textBrowser_2{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"}\n"
"QToolButton#toolButton_close_console{\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit#lineEdit_console{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"padding-left: 10px;\n"
"}\n"
"QLineEdit#lineEdit_console:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit#lineEdit_console:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(FormHome)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_empty_draw = QFrame(FormHome)
        self.frame_empty_draw.setObjectName(u"frame_empty_draw")
        self.frame_empty_draw.setFrameShape(QFrame.StyledPanel)
        self.frame_empty_draw.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_empty_draw)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 20, -1, 20)
        self.label_8 = QLabel(self.frame_empty_draw)
        self.label_8.setObjectName(u"label_8")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QSize(100, 100))
        self.label_8.setMaximumSize(QSize(100, 100))
        self.label_8.setPixmap(QPixmap(u"recursos/iconos/iconos_logo/Logo_V1.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, -1)
        self.label_title_1 = QLabel(self.frame_empty_draw)
        self.label_title_1.setObjectName(u"label_title_1")

        self.horizontalLayout_9.addWidget(self.label_title_1)

        self.label_title_2 = QLabel(self.frame_empty_draw)
        self.label_title_2.setObjectName(u"label_title_2")

        self.horizontalLayout_9.addWidget(self.label_title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.frame_empty_draw)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_infNuevoProyecto = QFrame(self.frame_5)
        self.frame_infNuevoProyecto.setObjectName(u"frame_infNuevoProyecto")
        sizePolicy.setHeightForWidth(self.frame_infNuevoProyecto.sizePolicy().hasHeightForWidth())
        self.frame_infNuevoProyecto.setSizePolicy(sizePolicy)
        self.frame_infNuevoProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_infNuevoProyecto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_infNuevoProyecto)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.frame_supNuevoProyecto = QFrame(self.frame_infNuevoProyecto)
        self.frame_supNuevoProyecto.setObjectName(u"frame_supNuevoProyecto")
        sizePolicy.setHeightForWidth(self.frame_supNuevoProyecto.sizePolicy().hasHeightForWidth())
        self.frame_supNuevoProyecto.setSizePolicy(sizePolicy)
        self.frame_supNuevoProyecto.setStyleSheet(u"")
        self.frame_supNuevoProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_supNuevoProyecto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_supNuevoProyecto)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 0, 0)
        self.toolButton_nuevoProyecto = QToolButton(self.frame_supNuevoProyecto)
        self.toolButton_nuevoProyecto.setObjectName(u"toolButton_nuevoProyecto")
        self.toolButton_nuevoProyecto.setMinimumSize(QSize(150, 40))
        self.toolButton_nuevoProyecto.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_frame_inicio/open_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_nuevoProyecto.setIcon(icon)
        self.toolButton_nuevoProyecto.setIconSize(QSize(20, 20))
        self.toolButton_nuevoProyecto.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_nuevoProyecto.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_nuevoProyecto.setArrowType(Qt.NoArrow)

        self.horizontalLayout_13.addWidget(self.toolButton_nuevoProyecto)


        self.verticalLayout_6.addWidget(self.frame_supNuevoProyecto)


        self.verticalLayout_13.addWidget(self.frame_infNuevoProyecto)

        self.frame_infAbrirProyecto = QFrame(self.frame_5)
        self.frame_infAbrirProyecto.setObjectName(u"frame_infAbrirProyecto")
        sizePolicy.setHeightForWidth(self.frame_infAbrirProyecto.sizePolicy().hasHeightForWidth())
        self.frame_infAbrirProyecto.setSizePolicy(sizePolicy)
        self.frame_infAbrirProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_infAbrirProyecto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_infAbrirProyecto)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.frame_supAbrirProyecto = QFrame(self.frame_infAbrirProyecto)
        self.frame_supAbrirProyecto.setObjectName(u"frame_supAbrirProyecto")
        sizePolicy.setHeightForWidth(self.frame_supAbrirProyecto.sizePolicy().hasHeightForWidth())
        self.frame_supAbrirProyecto.setSizePolicy(sizePolicy)
        self.frame_supAbrirProyecto.setStyleSheet(u"")
        self.frame_supAbrirProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_supAbrirProyecto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_supAbrirProyecto)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 0, 0)
        self.toolButton_abrirProyecto = QToolButton(self.frame_supAbrirProyecto)
        self.toolButton_abrirProyecto.setObjectName(u"toolButton_abrirProyecto")
        self.toolButton_abrirProyecto.setMinimumSize(QSize(150, 40))
        self.toolButton_abrirProyecto.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_frame_inicio/new_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_abrirProyecto.setIcon(icon1)
        self.toolButton_abrirProyecto.setIconSize(QSize(20, 20))
        self.toolButton_abrirProyecto.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_abrirProyecto.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_12.addWidget(self.toolButton_abrirProyecto)


        self.verticalLayout_5.addWidget(self.frame_supAbrirProyecto)


        self.verticalLayout_13.addWidget(self.frame_infAbrirProyecto)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_infEjemplos2 = QFrame(self.frame_6)
        self.frame_infEjemplos2.setObjectName(u"frame_infEjemplos2")
        sizePolicy.setHeightForWidth(self.frame_infEjemplos2.sizePolicy().hasHeightForWidth())
        self.frame_infEjemplos2.setSizePolicy(sizePolicy)
        self.frame_infEjemplos2.setFrameShape(QFrame.StyledPanel)
        self.frame_infEjemplos2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_infEjemplos2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.frame_supEjemplos2 = QFrame(self.frame_infEjemplos2)
        self.frame_supEjemplos2.setObjectName(u"frame_supEjemplos2")
        sizePolicy.setHeightForWidth(self.frame_supEjemplos2.sizePolicy().hasHeightForWidth())
        self.frame_supEjemplos2.setSizePolicy(sizePolicy)
        self.frame_supEjemplos2.setFrameShape(QFrame.StyledPanel)
        self.frame_supEjemplos2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_supEjemplos2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 0, 0)
        self.toolButton_ejemplos2 = QToolButton(self.frame_supEjemplos2)
        self.toolButton_ejemplos2.setObjectName(u"toolButton_ejemplos2")
        self.toolButton_ejemplos2.setMinimumSize(QSize(150, 40))
        self.toolButton_ejemplos2.setStyleSheet(u"")
        self.toolButton_ejemplos2.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_ejemplos2.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_14.addWidget(self.toolButton_ejemplos2)


        self.verticalLayout_7.addWidget(self.frame_supEjemplos2)


        self.verticalLayout_11.addWidget(self.frame_infEjemplos2)

        self.frame_infEjemplos1 = QFrame(self.frame_6)
        self.frame_infEjemplos1.setObjectName(u"frame_infEjemplos1")
        sizePolicy.setHeightForWidth(self.frame_infEjemplos1.sizePolicy().hasHeightForWidth())
        self.frame_infEjemplos1.setSizePolicy(sizePolicy)
        self.frame_infEjemplos1.setStyleSheet(u"")
        self.frame_infEjemplos1.setFrameShape(QFrame.StyledPanel)
        self.frame_infEjemplos1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_infEjemplos1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.frame_supEjemplos1 = QFrame(self.frame_infEjemplos1)
        self.frame_supEjemplos1.setObjectName(u"frame_supEjemplos1")
        sizePolicy.setHeightForWidth(self.frame_supEjemplos1.sizePolicy().hasHeightForWidth())
        self.frame_supEjemplos1.setSizePolicy(sizePolicy)
        self.frame_supEjemplos1.setStyleSheet(u"")
        self.frame_supEjemplos1.setFrameShape(QFrame.StyledPanel)
        self.frame_supEjemplos1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_supEjemplos1)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 0, 0, 0)
        self.toolButton_ejemplos1 = QToolButton(self.frame_supEjemplos1)
        self.toolButton_ejemplos1.setObjectName(u"toolButton_ejemplos1")
        self.toolButton_ejemplos1.setMinimumSize(QSize(150, 40))
        self.toolButton_ejemplos1.setStyleSheet(u"")
        self.toolButton_ejemplos1.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_ejemplos1.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_15.addWidget(self.toolButton_ejemplos1)


        self.verticalLayout_10.addWidget(self.frame_supEjemplos1)


        self.verticalLayout_11.addWidget(self.frame_infEjemplos1)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_proyectos = QFrame(self.frame_empty_draw)
        self.frame_proyectos.setObjectName(u"frame_proyectos")
        self.frame_proyectos.setFrameShape(QFrame.StyledPanel)
        self.frame_proyectos.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_proyectos)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_home = QScrollArea(self.frame_proyectos)
        self.scrollArea_home.setObjectName(u"scrollArea_home")
        self.scrollArea_home.setStyleSheet(u"background: transparent;\n"
"")
        self.scrollArea_home.setLineWidth(0)
        self.scrollArea_home.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 448, 489))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.gridLayout_proyectos = QGridLayout()
        self.gridLayout_proyectos.setSpacing(10)
        self.gridLayout_proyectos.setObjectName(u"gridLayout_proyectos")
        self.gridLayout_proyectos.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout_proyectos.setContentsMargins(5, 5, 5, 5)

        self.horizontalLayout_18.addLayout(self.gridLayout_proyectos)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_2)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_7)

        self.scrollArea_home.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_9.addWidget(self.scrollArea_home)


        self.horizontalLayout_16.addWidget(self.frame_proyectos)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_16)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.horizontalLayout.addWidget(self.frame_empty_draw)


        self.retranslateUi(FormHome)

        QMetaObject.connectSlotsByName(FormHome)
    # setupUi

    def retranslateUi(self, FormHome):
        FormHome.setWindowTitle(QCoreApplication.translate("FormHome", u"Form", None))
        self.label_8.setText("")
        self.label_title_1.setText(QCoreApplication.translate("FormHome", u"Bienvenidos a", None))
        self.label_title_2.setText(QCoreApplication.translate("FormHome", u"MPM-UN", None))
        self.toolButton_nuevoProyecto.setText(QCoreApplication.translate("FormHome", u"  Nuevo proyecto", None))
        self.toolButton_abrirProyecto.setText(QCoreApplication.translate("FormHome", u"  Abrir proyecto", None))
        self.toolButton_ejemplos2.setText(QCoreApplication.translate("FormHome", u"Ejemplos", None))
        self.toolButton_ejemplos1.setText(QCoreApplication.translate("FormHome", u"Ejemplos", None))
    # retranslateUi

