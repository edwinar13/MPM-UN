# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenipxZmV.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QProgressBar, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(750, 500)
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_logo/Logo_WindowIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet(u"/*Colores primarios*/\n"
"/* \n"
"gris oscuro		#222222		#333333		#444444\n"
"gris claro 		#999999		#DDDDDD\n"
"verde claro						#C8CC8E\n"
"vinotinto  						#742427\n"
"*/\n"
"/*Colores secundarios */\n"
"/* \n"
"Azules  		#36C9C6		#00BDB9	#77ACA2\n"
"rojos		 	#910D3F		#C70039		#F94646\n"
"naranjas 		#D34E24		#F28123		#F7F052\n"
"*/\n"
"\n"
"/* Funetes/*\n"
"\n"
"/*\n"
"italic:				font: italic 9pt \"Ubuntu\";\n"
"regular:			font: 9pt \"Ubuntu\";\n"
"light:				font: 300 9pt \"Ubuntu\";\n"
"medium:			font: 500 9pt \"Ubuntu\";\n"
"bold:				font: 700 9pt \"Ubuntu\";\n"
"*/\n"
"\n"
"/****************************************************************************************************************************************************/\n"
"\n"
"\n"
"QMainWindow#SplashScreen{\n"
"}\n"
"QFrame#frame_background{\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(34, 34, 34, 255));\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"\n"
"QLabel#label_"
                        "title{\n"
"	background-color: transparent;	\n"
"	font: 700 70pt \"Ubuntu\";	\n"
"	color: #DDDDDD;\n"
"}\n"
"QLabel#label_version{\n"
"	background-color: transparent;	\n"
"	font: 500 20pt \"Ubuntu\";	\n"
"	color: #DDDDDD;\n"
"}\n"
"QLabel#label_info{\n"
"	background-color: transparent;	\n"
"	font: italic 10pt \"Ubuntu\";	\n"
"	color: #999999;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QProgressBar#progressBar_load{\n"
"	background-color: #333333;\n"
"	color: #C8CC8E;\n"
"	border-radius: 5px;	\n"
"	text-align: center;		\n"
"	font: 7pt \"Ubuntu\";	\n"
"}\n"
"QProgressBar#progressBar_load::chunk{\n"
"	background-color:#742427;	\n"
"	border-radius: 5px;	\n"
"}\n"
"")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_background = QFrame(self.centralwidget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setStyleSheet(u"")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_background)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_logo = QLabel(self.frame_background)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMinimumSize(QSize(150, 150))
        self.label_logo.setMaximumSize(QSize(150, 150))
        self.label_logo.setPixmap(QPixmap(u"recursos/iconos/iconos_logo/Logo_V1.svg"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_logo)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_title = QLabel(self.frame_background)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_title)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_version = QLabel(self.frame_background)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_version)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_info = QLabel(self.frame_background)
        self.label_info.setObjectName(u"label_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_info.sizePolicy().hasHeightForWidth())
        self.label_info.setSizePolicy(sizePolicy1)
        self.label_info.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_info)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.progressBar_load = QProgressBar(self.frame_background)
        self.progressBar_load.setObjectName(u"progressBar_load")
        self.progressBar_load.setMinimumSize(QSize(500, 10))
        self.progressBar_load.setMaximumSize(QSize(500, 10))
        self.progressBar_load.setStyleSheet(u"")
        self.progressBar_load.setValue(40)

        self.verticalLayout_4.addWidget(self.progressBar_load)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.frame_background)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_logo.setText("")
        self.label_title.setText(QCoreApplication.translate("SplashScreen", u"MPM-UN", None))
        self.label_version.setText(QCoreApplication.translate("SplashScreen", u"v0.1.0", None))
        self.label_info.setText(QCoreApplication.translate("SplashScreen", u"Cargando...", None))
    # retranslateUi

