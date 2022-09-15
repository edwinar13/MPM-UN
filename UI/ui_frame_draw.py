# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_drawUaktGh.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSplitter,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_FormDraw(object):
    def setupUi(self, FormDraw):
        if not FormDraw.objectName():
            FormDraw.setObjectName(u"FormDraw")
        FormDraw.resize(333, 479)
        FormDraw.setStyleSheet(u"\n"
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
"/*#################################################################*/\n"
"/*######################      PAGE DRAW      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"\n"
"/*###################### graphicsView draw  ###########################"
                        "#*/\n"
"QGraphicsView#graphicsView_draw{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.943, stop:0 rgba(175, 175, 175, 255), stop:0.971591 rgba(141, 211, 211, 220), stop:1\n"
" rgba(170, 255, 255, 255));\n"
"	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(216, 216, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: #444444;\n"
"border: none;\n"
"}\n"
"\n"
"/*###################### frame consola  ############################*/\n"
"\n"
"QFrame#frame_3{\n"
"background-color: #333333;\n"
"border-top-right-radius: 8px ;\n"
"\n"
"}\n"
"\n"
"\n"
"QFrame#frame_console{\n"
"background-color: #333333;\n"
"}\n"
"\n"
"QTextBrowser#textBrowser_2{\n"
"background-color: #555555;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"border-top-right-radius: 8px ;\n"
"}\n"
"QToolButton#toolButton_closeConsole{\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit#lineEdit_console{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius"
                        ": 2px ;\n"
"padding-left: 10px;\n"
"}\n"
"QLineEdit#lineEdit_console:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit#lineEdit_console:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(FormDraw)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_draw = QHBoxLayout()
        self.horizontalLayout_draw.setSpacing(0)
        self.horizontalLayout_draw.setObjectName(u"horizontalLayout_draw")
        self.splitter = QSplitter(FormDraw)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setLineWidth(0)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.graphicsView_draw = QGraphicsView(self.splitter)
        self.graphicsView_draw.setObjectName(u"graphicsView_draw")
        self.graphicsView_draw.setStyleSheet(u"")
        self.splitter.addWidget(self.graphicsView_draw)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 4, 4, 0)
        self.textBrowser_2 = QTextBrowser(self.frame_3)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QSize(0, 38))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser_2.setStyleSheet(u"")
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setOpenExternalLinks(False)
        self.textBrowser_2.setOpenLinks(False)

        self.verticalLayout_3.addWidget(self.textBrowser_2)

        self.frame_console = QFrame(self.frame_3)
        self.frame_console.setObjectName(u"frame_console")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_console.sizePolicy().hasHeightForWidth())
        self.frame_console.setSizePolicy(sizePolicy2)
        self.frame_console.setStyleSheet(u"")
        self.frame_console.setFrameShape(QFrame.StyledPanel)
        self.frame_console.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_console)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.toolButton_closeConsole = QToolButton(self.frame_console)
        self.toolButton_closeConsole.setObjectName(u"toolButton_closeConsole")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_closeConsole.sizePolicy().hasHeightForWidth())
        self.toolButton_closeConsole.setSizePolicy(sizePolicy3)
        self.toolButton_closeConsole.setMinimumSize(QSize(20, 20))
        self.toolButton_closeConsole.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_closeConsole.setFont(font)
        self.toolButton_closeConsole.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeConsole.setIcon(icon)
        self.toolButton_closeConsole.setIconSize(QSize(15, 15))
        self.toolButton_closeConsole.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_closeConsole)

        self.label_4 = QLabel(self.frame_console)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setPixmap(QPixmap(u"recursos/iconos/iconos_consola/code.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_console = QLineEdit(self.frame_console)
        self.lineEdit_console.setObjectName(u"lineEdit_console")
        self.lineEdit_console.setMinimumSize(QSize(0, 20))
        self.lineEdit_console.setMaximumSize(QSize(16777215, 18))
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit_console.setFont(font1)
        self.lineEdit_console.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lineEdit_console)


        self.verticalLayout_3.addWidget(self.frame_console)

        self.splitter.addWidget(self.frame_3)

        self.horizontalLayout_draw.addWidget(self.splitter)


        self.horizontalLayout.addLayout(self.horizontalLayout_draw)


        self.retranslateUi(FormDraw)

        QMetaObject.connectSlotsByName(FormDraw)
    # setupUi

    def retranslateUi(self, FormDraw):
        FormDraw.setWindowTitle(QCoreApplication.translate("FormDraw", u"Form", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("FormDraw", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolButton_closeConsole.setText("")
        self.label_4.setText("")
        self.lineEdit_console.setInputMask("")
        self.lineEdit_console.setText("")
        self.lineEdit_console.setPlaceholderText(QCoreApplication.translate("FormDraw", u"Ingrese comando", None))
    # retranslateUi

