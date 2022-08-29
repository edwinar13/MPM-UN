# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenyyLSNM.ui'
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
import UI.file_icons_rc

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(750, 500)
        icon = QIcon()
        icon.addFile(u":/logo/Logo_V1.svg", QSize(), QIcon.Normal, QIcon.Off)
        SplashScreen.setWindowIcon(icon)
        SplashScreen.setStyleSheet(u"QMainWindow{\n"
"font-family: \"Ubuntu\";\n"
"}")
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.fondoFrame = QFrame(self.centralwidget)
        self.fondoFrame.setObjectName(u"fondoFrame")
        self.fondoFrame.setStyleSheet(u"QFrame{\n"
"color: #D9D9D9;\n"
"}\n"
"\n"
"\n"
"#fondoFrame{\n"
"/*background: #222222;*/\n"
"	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(85, 85, 85, 255), stop:1 rgba(34, 34, 34, 255));\n"
"border-radius:15px;\n"
"}\n"
"QLabel{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"QProgressBar{\n"
"\n"
"	background-color: #333333;\n"
"	color: #C8CC8E;\n"
"border-radius: 5px;\n"
"\n"
"	/*borde-style: none;*/\n"
"	\n"
"	text-align: center;	\n"
"	\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"/*\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.494, x2:1, y2:0.489, stop:0 rgba(116, 36, 39, 255), stop:1 rgba(200, 204, 142, 255));\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.403, x2:1, y2:0.556818, stop:0 rgba(116, 36, 39, 255), stop:0.471591 rgba(34, 34, 34, 255), stop:1 rgba(200, 204, 142, 255));	\n"
"*/\n"
"background-color:#742427;\n"
"	/*borde-style: none;*/\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"")
        self.fondoFrame.setFrameShape(QFrame.StyledPanel)
        self.fondoFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.fondoFrame)
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

        self.label_4 = QLabel(self.fondoFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(200, 200))
        self.label_4.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.fondoFrame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(50)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_3 = QLabel(self.fondoFrame)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(28)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)


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
        self.label_load = QLabel(self.fondoFrame)
        self.label_load.setObjectName(u"label_load")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_load.sizePolicy().hasHeightForWidth())
        self.label_load.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setStrikeOut(False)
        self.label_load.setFont(font2)
        self.label_load.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_load)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_7)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.progressBar = QProgressBar(self.fondoFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(500, 10))
        self.progressBar.setMaximumSize(QSize(500, 10))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(7)
        self.progressBar.setFont(font3)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(40)

        self.verticalLayout_4.addWidget(self.progressBar)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.verticalLayout.addWidget(self.fondoFrame)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"MainWindow", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("SplashScreen", u"MPM-UN", None))
        self.label_3.setText(QCoreApplication.translate("SplashScreen", u"v0.1.0", None))
        self.label_load.setText(QCoreApplication.translate("SplashScreen", u"Cargando...", None))
    # retranslateUi

