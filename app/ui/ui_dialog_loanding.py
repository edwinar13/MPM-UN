# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_loandingXxcAwZ.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_DialogLoanding(object):
    def setupUi(self, DialogLoanding):
        if not DialogLoanding.objectName():
            DialogLoanding.setObjectName(u"DialogLoanding")
        DialogLoanding.setEnabled(True)
        DialogLoanding.resize(621, 387)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogLoanding.sizePolicy().hasHeightForWidth())
        DialogLoanding.setSizePolicy(sizePolicy)
        DialogLoanding.setStyleSheet(u"/*Colores primarios*/\n"
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
"\n"
"QFrame#frame_dialog{\n"
"	background-color: #333333;\n"
"	border-radius:15px;\n"
"}\n"
"\n"
"QFrame#frame_content{\n"
"	background-color: #444444;\n"
"	border-radius:5px;\n"
"}\n"
"\n"
"\n"
"QLabel#label_text{\n"
"	font: 300 10pt \"Ubuntu\";\n"
"	color: #DDDDDD;\n"
"mar"
                        "gin-left: 10px;\n"
"}\n"
"QTextBrowser#textBrowser_description{\n"
"	background-color: transparent;\n"
"	font: 300 10pt \"Ubuntu\";\n"
"	color: #999999;\n"
"	margin-left: 20px;\n"
"	border: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton#toolButton_exit{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QPushButton[style_msn_button=\"1\"]{\n"
"font: 500 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QPushButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton[QPushButtonStyle=\"1\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 8px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"1\"]:hover{\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"\n"
"/*************************"
                        "****************/\n"
"QPushButton[QPushButtonStyle=\"2\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #910D3F;\n"
"border: none;\n"
"padding: 6px 5px;\n"
"border-radius: 8px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"2\"]:hover{\n"
"background-color: #C70039;\n"
"}\n"
"\n"
"\n"
"\n"
"/*****************************************/\n"
"QPushButton[QPushButtonStyle=\"3\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #999999;\n"
"border: none;\n"
"padding: 6px 5px;\n"
"border-radius: 8px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"3\"]:hover{\n"
"background-color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"\n"
"QProgressBar#progressBar_loanding{\n"
"border: none;\n"
"border-radius: 8px ;\n"
"    border: 2px solid grey;\n"
"    \n"
"    background: lightgrey;\n"
"}\n"
"\n"
"\n"
"QProgressBar#progressBar_loanding::chunk {\n"
"\n"
"    width: 10px; /* Tama\u00f1o del chunk (barra de progreso) */\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(DialogLoanding)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_dialog = QFrame(DialogLoanding)
        self.frame_dialog.setObjectName(u"frame_dialog")
        sizePolicy.setHeightForWidth(self.frame_dialog.sizePolicy().hasHeightForWidth())
        self.frame_dialog.setSizePolicy(sizePolicy)
        self.frame_dialog.setFrameShape(QFrame.StyledPanel)
        self.frame_dialog.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_dialog)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_icon = QLabel(self.frame_dialog)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy1)
        self.label_icon.setMinimumSize(QSize(0, 100))
        self.label_icon.setMaximumSize(QSize(100, 100))
        self.label_icon.setPixmap(QPixmap(u"app/resources/iconos/iconos_msg/question.svg"))
        self.label_icon.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_icon)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.frame_content = QFrame(self.frame_dialog)
        self.frame_content.setObjectName(u"frame_content")
        sizePolicy.setHeightForWidth(self.frame_content.sizePolicy().hasHeightForWidth())
        self.frame_content.setSizePolicy(sizePolicy)
        self.frame_content.setMinimumSize(QSize(0, 0))
        self.frame_content.setMaximumSize(QSize(16777215, 16777215))
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_content)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.progressBar_loanding = QProgressBar(self.frame_content)
        self.progressBar_loanding.setObjectName(u"progressBar_loanding")
        self.progressBar_loanding.setValue(24)

        self.verticalLayout.addWidget(self.progressBar_loanding)

        self.textBrowser_description = QTextBrowser(self.frame_content)
        self.textBrowser_description.setObjectName(u"textBrowser_description")
        sizePolicy.setHeightForWidth(self.textBrowser_description.sizePolicy().hasHeightForWidth())
        self.textBrowser_description.setSizePolicy(sizePolicy)
        self.textBrowser_description.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.textBrowser_description)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_accept = QPushButton(self.frame_content)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_accept.sizePolicy().hasHeightForWidth())
        self.pushButton_accept.setSizePolicy(sizePolicy2)
        self.pushButton_accept.setMinimumSize(QSize(0, 30))
        self.pushButton_accept.setMaximumSize(QSize(120, 30))
        self.pushButton_accept.setProperty("style_msn_button", 1)
        self.pushButton_accept.setProperty("QPushButtonStyle", 1)

        self.horizontalLayout_2.addWidget(self.pushButton_accept)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.horizontalLayout.addWidget(self.frame_dialog)


        self.retranslateUi(DialogLoanding)

        QMetaObject.connectSlotsByName(DialogLoanding)
    # setupUi

    def retranslateUi(self, DialogLoanding):
        DialogLoanding.setWindowTitle(QCoreApplication.translate("DialogLoanding", u"Dialog", None))
        self.label_icon.setText("")
        self.textBrowser_description.setHtml(QCoreApplication.translate("DialogLoanding", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:300; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Cargando</p></body></html>", None))
        self.pushButton_accept.setText(QCoreApplication.translate("DialogLoanding", u"Aceptar", None))
    # retranslateUi

