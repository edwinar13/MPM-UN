# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_homeqrkvyS.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QScrollArea, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_FormHome(object):
    def setupUi(self, FormHome):
        if not FormHome.objectName():
            FormHome.setObjectName(u"FormHome")
        FormHome.resize(943, 720)
        FormHome.setMaximumSize(QSize(16777215, 16777215))
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
"\n"
"\n"
"\n"
"/*######################      CONTAINER        ############################*/\n"
"#FormHome{\n"
"background-color: #222222;\n"
"}\n"
"QFrame#frame_empty_home{\n"
"background-color: #222222;\n"
"}\n"
"\n"
"/*######################      PAGE HOME      ############################*/\n"
"\n"
"QLabel#label_title_1{\n"
"color: #DDDDDD; \n"
"font: 500 30pt \"Ubuntu\";\n"
"}\n"
"QLabel#label_title_2{\n"
"color: #C8CC8E;\n"
"font: 700 30pt \"Ubuntu\";\n"
"font-weight:b"
                        "old;\n"
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
"QFrame#frame_proyectos{\n"
" background: #444444;\n"
"border-radius: 5px;\n"
" }\n"
"Line#line_1,\n"
"Line#line_2{\n"
"background: #999999;\n"
"}\n"
"QLabel#label_subTitle1,\n"
"QLabel#label_subTitle2,\n"
"QLabel#label_subTitle3,\n"
"QLabel#label_subTitle4{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QLabel#label_cardNew1,\n"
"QLabel#label_cardNew2,\n"
"Q"
                        "Label#label_cardNew3,\n"
"QLabel#label_cardNew4,\n"
"QLabel#label_cardNew5{\n"
"font:  9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_cardNew1,\n"
"QFrame#frame_cardNew2,\n"
"QFrame#frame_cardNew3,\n"
"QFrame#frame_cardNew4,\n"
"QFrame#frame_cardNew5{\n"
"background: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QToolButton#toolButton_cardNew1,\n"
"QToolButton#toolButton_cardNew2,\n"
"QToolButton#toolButton_cardNew3,\n"
"QToolButton#toolButton_cardNew4,\n"
"QToolButton#toolButton_cardNew5{\n"
"background: rgb(255, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*######################      SCROLL BAR    VERTICAL  ############################*/\n"
"\n"
"QScrollBar:vertical {    \n"
"	border: none;\n"
"    width: 14px;\n"
"	border-radius: 0px;\n"
"	margin: 15px 0px 15px 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #333333;\n"
"    min-height: 14px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #"
                        "910D3F;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #C70039;\n"
"}\n"
"\n"
"/*TOP*/\n"
"QScrollBar::sub-line:vertical{\n"
"    background-color: #444444;\n"
"	border: none;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-radius: 7px;\n"
"	height: 15px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"    background-color: #910D3F;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color: #C70039;\n"
"}\n"
"\n"
"/*BOTTON*/\n"
"QScrollBar::add-line:vertical{\n"
"    background-color: #444444;\n"
"	border: none;	\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	height: 15px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"    background-color: #910D3F;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"   background-color: #C70039;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:ver"
                        "tical,QScrollBar::down-arrow:vertical{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"/*######################      SCROLL BAR    HORIZONTAL  ############################*/\n"
"\n"
"QScrollBar:horizontal{\n"
"height: 14px;\n"
"border: none;\n"
"border-radius: 0px;\n"
"margin: 0px 15px 0px 15px;\n"
"}\n"
"\n"
"\n"
"/*Deslizador*/\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #333333;\n"
"	border-radius: 7px;\n"
"	min-width: 14px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #910D3F;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #C70039;\n"
"}\n"
"  \n"
"QScrollBar::sub-line:horizontal{\n"
"background-color: #666666;\n"
"border: none;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"width: 15px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"    backgr"
                        "ound-color: #910D3F;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color: #C70039;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    background-color: #666666;\n"
"	border: none;	\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	width: 15px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover{\n"
"    background-color: #910D3F;\n"
"}QScrollBar::add-line:vertical:pressed{\n"
"    background-color: #C70039;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:horizontal{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"background: none;\n"
"}")
        self.horizontalLayout_22 = QHBoxLayout(FormHome)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(FormHome)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, -1)
        self.label_logo = QLabel(self.frame)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy1)
        self.label_logo.setMinimumSize(QSize(100, 100))
        self.label_logo.setMaximumSize(QSize(100, 100))
        self.label_logo.setPixmap(QPixmap(u"app/resources/iconos/iconos_logo/Logo_V1.svg"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setWordWrap(False)
        self.label_logo.setOpenExternalLinks(False)

        self.horizontalLayout_9.addWidget(self.label_logo)

        self.label_title_1 = QLabel(self.frame)
        self.label_title_1.setObjectName(u"label_title_1")

        self.horizontalLayout_9.addWidget(self.label_title_1)

        self.label_title_2 = QLabel(self.frame)
        self.label_title_2.setObjectName(u"label_title_2")

        self.horizontalLayout_9.addWidget(self.label_title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addWidget(self.frame)

        self.frame_3 = QFrame(FormHome)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.label_subTitle1 = QLabel(self.frame_3)
        self.label_subTitle1.setObjectName(u"label_subTitle1")

        self.horizontalLayout_3.addWidget(self.label_subTitle1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.line_1 = QFrame(self.frame_3)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShadow(QFrame.Sunken)
        self.line_1.setLineWidth(1)
        self.line_1.setFrameShape(QFrame.HLine)

        self.verticalLayout_5.addWidget(self.line_1)

        self.scrollArea_1 = QScrollArea(self.frame_3)
        self.scrollArea_1.setObjectName(u"scrollArea_1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_1.sizePolicy().hasHeightForWidth())
        self.scrollArea_1.setSizePolicy(sizePolicy2)
        self.scrollArea_1.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"")
        self.scrollArea_1.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_1.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 970, 201))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents_2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents_2.setSizePolicy(sizePolicy1)
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 15, 0, 0)
        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 16)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_5)

        self.frame_cardNew1 = QFrame(self.frame_4)
        self.frame_cardNew1.setObjectName(u"frame_cardNew1")
        self.frame_cardNew1.setMinimumSize(QSize(90, 120))
        self.frame_cardNew1.setMaximumSize(QSize(90, 120))
        self.frame_cardNew1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cardNew1.setFrameShape(QFrame.StyledPanel)
        self.frame_cardNew1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_cardNew1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.toolButton_cardNew1 = QToolButton(self.frame_cardNew1)
        self.toolButton_cardNew1.setObjectName(u"toolButton_cardNew1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_cardNew1.sizePolicy().hasHeightForWidth())
        self.toolButton_cardNew1.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.toolButton_cardNew1)


        self.horizontalLayout_8.addWidget(self.frame_cardNew1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.label_cardNew1 = QLabel(self.frame_4)
        self.label_cardNew1.setObjectName(u"label_cardNew1")
        self.label_cardNew1.setMinimumSize(QSize(120, 40))
        self.label_cardNew1.setMaximumSize(QSize(16777215, 40))
        self.label_cardNew1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_cardNew1)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)

        self.frame_cardNew2 = QFrame(self.frame_4)
        self.frame_cardNew2.setObjectName(u"frame_cardNew2")
        self.frame_cardNew2.setMinimumSize(QSize(90, 120))
        self.frame_cardNew2.setMaximumSize(QSize(90, 120))
        self.frame_cardNew2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cardNew2.setFrameShape(QFrame.StyledPanel)
        self.frame_cardNew2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_cardNew2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.toolButton_cardNew2 = QToolButton(self.frame_cardNew2)
        self.toolButton_cardNew2.setObjectName(u"toolButton_cardNew2")
        sizePolicy3.setHeightForWidth(self.toolButton_cardNew2.sizePolicy().hasHeightForWidth())
        self.toolButton_cardNew2.setSizePolicy(sizePolicy3)
        icon = QIcon()
        icon.addFile(u"app/resources/imagenes/ejemplo_viga.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardNew2.setIcon(icon)
        self.toolButton_cardNew2.setIconSize(QSize(100, 100))

        self.horizontalLayout_15.addWidget(self.toolButton_cardNew2)


        self.horizontalLayout_11.addWidget(self.frame_cardNew2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_8)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.label_cardNew2 = QLabel(self.frame_4)
        self.label_cardNew2.setObjectName(u"label_cardNew2")
        self.label_cardNew2.setMinimumSize(QSize(120, 40))
        self.label_cardNew2.setMaximumSize(QSize(16777215, 40))
        self.label_cardNew2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_cardNew2)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_11)

        self.frame_cardNew3 = QFrame(self.frame_4)
        self.frame_cardNew3.setObjectName(u"frame_cardNew3")
        self.frame_cardNew3.setMinimumSize(QSize(90, 120))
        self.frame_cardNew3.setMaximumSize(QSize(90, 120))
        self.frame_cardNew3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cardNew3.setFrameShape(QFrame.StyledPanel)
        self.frame_cardNew3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_cardNew3)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.toolButton_cardNew3 = QToolButton(self.frame_cardNew3)
        self.toolButton_cardNew3.setObjectName(u"toolButton_cardNew3")
        sizePolicy3.setHeightForWidth(self.toolButton_cardNew3.sizePolicy().hasHeightForWidth())
        self.toolButton_cardNew3.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u"app/resources/imagenes/ejemplo_capacidad_portante.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardNew3.setIcon(icon1)
        self.toolButton_cardNew3.setIconSize(QSize(100, 100))

        self.horizontalLayout_16.addWidget(self.toolButton_cardNew3)


        self.horizontalLayout_13.addWidget(self.frame_cardNew3)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.label_cardNew3 = QLabel(self.frame_4)
        self.label_cardNew3.setObjectName(u"label_cardNew3")
        self.label_cardNew3.setMinimumSize(QSize(0, 40))
        self.label_cardNew3.setMaximumSize(QSize(16777215, 40))
        self.label_cardNew3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_cardNew3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_9)

        self.frame_cardNew4 = QFrame(self.frame_4)
        self.frame_cardNew4.setObjectName(u"frame_cardNew4")
        self.frame_cardNew4.setMinimumSize(QSize(90, 120))
        self.frame_cardNew4.setMaximumSize(QSize(90, 120))
        self.frame_cardNew4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cardNew4.setFrameShape(QFrame.StyledPanel)
        self.frame_cardNew4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_cardNew4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.toolButton_cardNew4 = QToolButton(self.frame_cardNew4)
        self.toolButton_cardNew4.setObjectName(u"toolButton_cardNew4")
        sizePolicy3.setHeightForWidth(self.toolButton_cardNew4.sizePolicy().hasHeightForWidth())
        self.toolButton_cardNew4.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u"app/resources/imagenes/ejemplo_disco.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardNew4.setIcon(icon2)
        self.toolButton_cardNew4.setIconSize(QSize(100, 100))

        self.horizontalLayout_17.addWidget(self.toolButton_cardNew4)


        self.horizontalLayout_12.addWidget(self.frame_cardNew4)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)


        self.verticalLayout_14.addLayout(self.horizontalLayout_12)

        self.label_cardNew4 = QLabel(self.frame_4)
        self.label_cardNew4.setObjectName(u"label_cardNew4")
        self.label_cardNew4.setMinimumSize(QSize(0, 40))
        self.label_cardNew4.setMaximumSize(QSize(16777215, 40))
        self.label_cardNew4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_cardNew4)


        self.horizontalLayout_4.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.frame_cardNew5 = QFrame(self.frame_4)
        self.frame_cardNew5.setObjectName(u"frame_cardNew5")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(90)
        sizePolicy4.setVerticalStretch(120)
        sizePolicy4.setHeightForWidth(self.frame_cardNew5.sizePolicy().hasHeightForWidth())
        self.frame_cardNew5.setSizePolicy(sizePolicy4)
        self.frame_cardNew5.setMinimumSize(QSize(90, 120))
        self.frame_cardNew5.setMaximumSize(QSize(90, 120))
        self.frame_cardNew5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_cardNew5.setFrameShape(QFrame.StyledPanel)
        self.frame_cardNew5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_cardNew5)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.toolButton_cardNew5 = QToolButton(self.frame_cardNew5)
        self.toolButton_cardNew5.setObjectName(u"toolButton_cardNew5")
        sizePolicy3.setHeightForWidth(self.toolButton_cardNew5.sizePolicy().hasHeightForWidth())
        self.toolButton_cardNew5.setSizePolicy(sizePolicy3)
        icon3 = QIcon()
        icon3.addFile(u"app/resources/imagenes/ejemplo_talud.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardNew5.setIcon(icon3)
        self.toolButton_cardNew5.setIconSize(QSize(100, 100))

        self.horizontalLayout_18.addWidget(self.toolButton_cardNew5)


        self.horizontalLayout_14.addWidget(self.frame_cardNew5)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)


        self.verticalLayout_15.addLayout(self.horizontalLayout_14)

        self.label_cardNew5 = QLabel(self.frame_4)
        self.label_cardNew5.setObjectName(u"label_cardNew5")
        self.label_cardNew5.setMinimumSize(QSize(0, 40))
        self.label_cardNew5.setMaximumSize(QSize(16777215, 401))
        self.label_cardNew5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_cardNew5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_15)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_4)

        self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_5.addWidget(self.scrollArea_1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(FormHome)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 10, -1, -1)
        self.label_subTitle2 = QLabel(self.frame_2)
        self.label_subTitle2.setObjectName(u"label_subTitle2")

        self.horizontalLayout_6.addWidget(self.label_subTitle2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.frame_cardTitle = QFrame(self.frame_2)
        self.frame_cardTitle.setObjectName(u"frame_cardTitle")
        sizePolicy2.setHeightForWidth(self.frame_cardTitle.sizePolicy().hasHeightForWidth())
        self.frame_cardTitle.setSizePolicy(sizePolicy2)
        self.frame_cardTitle.setMinimumSize(QSize(0, 0))
        self.frame_cardTitle.setMaximumSize(QSize(16777215, 16777215))
        self.frame_cardTitle.setFrameShape(QFrame.StyledPanel)
        self.frame_cardTitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_cardTitle)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, 10, 23, 0)
        self.label_icon1 = QLabel(self.frame_cardTitle)
        self.label_icon1.setObjectName(u"label_icon1")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(30)
        sizePolicy5.setVerticalStretch(30)
        sizePolicy5.setHeightForWidth(self.label_icon1.sizePolicy().hasHeightForWidth())
        self.label_icon1.setSizePolicy(sizePolicy5)
        self.label_icon1.setMinimumSize(QSize(30, 30))
        self.label_icon1.setMaximumSize(QSize(30, 30))
        self.label_icon1.setPixmap(QPixmap(u"app/resources/iconos/iconos_frame_inicio/doc_basic.svg"))
        self.label_icon1.setScaledContents(True)

        self.horizontalLayout_7.addWidget(self.label_icon1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.label_subTitle3 = QLabel(self.frame_cardTitle)
        self.label_subTitle3.setObjectName(u"label_subTitle3")

        self.verticalLayout_6.addWidget(self.label_subTitle3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.horizontalSpacer_15 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_15)

        self.label_subTitle4 = QLabel(self.frame_cardTitle)
        self.label_subTitle4.setObjectName(u"label_subTitle4")
        self.label_subTitle4.setMinimumSize(QSize(160, 0))
        self.label_subTitle4.setMaximumSize(QSize(160, 16777215))
        self.label_subTitle4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_subTitle4)


        self.verticalLayout_7.addWidget(self.frame_cardTitle)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_5 = QFrame(FormHome)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.scrollArea_2 = QScrollArea(self.frame_5)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 903, 210))
        self.horizontalLayout_20 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy6.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy6)
        self.frame_6.setStyleSheet(u"background-color: transparent;\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_containerCard = QVBoxLayout()
        self.verticalLayout_containerCard.setSpacing(5)
        self.verticalLayout_containerCard.setObjectName(u"verticalLayout_containerCard")

        self.verticalLayout_8.addLayout(self.verticalLayout_containerCard)


        self.horizontalLayout_20.addWidget(self.frame_6)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_10.addWidget(self.scrollArea_2)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout_22.addLayout(self.verticalLayout)


        self.retranslateUi(FormHome)

        QMetaObject.connectSlotsByName(FormHome)
    # setupUi

    def retranslateUi(self, FormHome):
        FormHome.setWindowTitle(QCoreApplication.translate("FormHome", u"Form", None))
        self.label_logo.setText("")
        self.label_title_1.setText(QCoreApplication.translate("FormHome", u"Bienvenidos a", None))
        self.label_title_2.setText(QCoreApplication.translate("FormHome", u"MPM-UN", None))
        self.label_subTitle1.setText(QCoreApplication.translate("FormHome", u"Proyecto nuevo", None))
        self.toolButton_cardNew1.setText(QCoreApplication.translate("FormHome", u".   .   .", None))
        self.label_cardNew1.setText(QCoreApplication.translate("FormHome", u"Proyecto nuevo", None))
        self.toolButton_cardNew2.setText("")
        self.label_cardNew2.setText(QCoreApplication.translate("FormHome", u"Vibraci\u00f3n axial \n"
"barra empotrada", None))
        self.toolButton_cardNew3.setText("")
        self.label_cardNew3.setText(QCoreApplication.translate("FormHome", u"Capacidad portante\n"
"sobre suelo tresca", None))
        self.toolButton_cardNew4.setText("")
        self.label_cardNew4.setText(QCoreApplication.translate("FormHome", u"Disco deslizando sobre\n"
"un plano inclinado", None))
        self.toolButton_cardNew5.setText("")
        self.label_cardNew5.setText(QCoreApplication.translate("FormHome", u"Falla de un talud\n"
"elastopl\u00e1stico", None))
        self.label_subTitle2.setText(QCoreApplication.translate("FormHome", u"Recientes", None))
        self.label_icon1.setText("")
        self.label_subTitle3.setText(QCoreApplication.translate("FormHome", u"Nombre", None))
        self.label_subTitle4.setText(QCoreApplication.translate("FormHome", u"Fecha de modificaci\u00f3n", None))
    # retranslateUi

