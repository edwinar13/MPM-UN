# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_msgLbEyqw.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextBrowser, QToolButton, QVBoxLayout,
    QWidget)

class Ui_DialogMsg(object):
    def setupUi(self, DialogMsg):
        if not DialogMsg.objectName():
            DialogMsg.setObjectName(u"DialogMsg")
        DialogMsg.setEnabled(True)
        DialogMsg.resize(604, 389)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMsg.sizePolicy().hasHeightForWidth())
        DialogMsg.setSizePolicy(sizePolicy)
        DialogMsg.setStyleSheet(u"/*Colores primarios*/\n"
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
"QPushButton{\n"
"font: 500 9pt \"Ubuntu\";\n"
"}")
        self.horizontalLayout = QHBoxLayout(DialogMsg)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_dialog = QFrame(DialogMsg)
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
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.toolButton_exit = QToolButton(self.frame_dialog)
        self.toolButton_exit.setObjectName(u"toolButton_exit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_exit.sizePolicy().hasHeightForWidth())
        self.toolButton_exit.setSizePolicy(sizePolicy1)
        self.toolButton_exit.setMinimumSize(QSize(20, 20))
        self.toolButton_exit.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.toolButton_exit.setFont(font)
        self.toolButton_exit.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_exit.setIcon(icon)
        self.toolButton_exit.setIconSize(QSize(15, 15))
        self.toolButton_exit.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_4.addWidget(self.toolButton_exit)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_icon = QLabel(self.frame_dialog)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy2)
        self.label_icon.setMinimumSize(QSize(0, 100))
        self.label_icon.setMaximumSize(QSize(100, 100))
        self.label_icon.setPixmap(QPixmap(u"recursos/iconos/iconos_msg/question.svg"))
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
        self.label_text = QLabel(self.frame_content)
        self.label_text.setObjectName(u"label_text")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_text.sizePolicy().hasHeightForWidth())
        self.label_text.setSizePolicy(sizePolicy3)

        self.verticalLayout.addWidget(self.label_text)

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

        self.pushButton_save = QPushButton(self.frame_content)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setMinimumSize(QSize(0, 30))
        self.pushButton_save.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_save)

        self.pushButton_yes = QPushButton(self.frame_content)
        self.pushButton_yes.setObjectName(u"pushButton_yes")
        self.pushButton_yes.setMinimumSize(QSize(0, 30))
        self.pushButton_yes.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_yes)

        self.pushButton_accept = QPushButton(self.frame_content)
        self.pushButton_accept.setObjectName(u"pushButton_accept")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_accept.sizePolicy().hasHeightForWidth())
        self.pushButton_accept.setSizePolicy(sizePolicy4)
        self.pushButton_accept.setMinimumSize(QSize(0, 30))
        self.pushButton_accept.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_accept)

        self.pushButton_notSave = QPushButton(self.frame_content)
        self.pushButton_notSave.setObjectName(u"pushButton_notSave")
        self.pushButton_notSave.setMinimumSize(QSize(0, 30))
        self.pushButton_notSave.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_notSave)

        self.pushButton_not = QPushButton(self.frame_content)
        self.pushButton_not.setObjectName(u"pushButton_not")
        self.pushButton_not.setMinimumSize(QSize(0, 30))
        self.pushButton_not.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_not)

        self.pushButton_cancel = QPushButton(self.frame_content)
        self.pushButton_cancel.setObjectName(u"pushButton_cancel")
        self.pushButton_cancel.setMinimumSize(QSize(0, 30))
        self.pushButton_cancel.setMaximumSize(QSize(120, 30))

        self.horizontalLayout_2.addWidget(self.pushButton_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.frame_content)


        self.horizontalLayout.addWidget(self.frame_dialog)


        self.retranslateUi(DialogMsg)

        QMetaObject.connectSlotsByName(DialogMsg)
    # setupUi

    def retranslateUi(self, DialogMsg):
        DialogMsg.setWindowTitle(QCoreApplication.translate("DialogMsg", u"Dialog", None))
        self.toolButton_exit.setText("")
        self.label_icon.setText("")
        self.label_text.setText(QCoreApplication.translate("DialogMsg", u"TextLabel", None))
        self.textBrowser_description.setHtml(QCoreApplication.translate("DialogMsg", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:10pt; font-weight:300; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Text drescription</p></body></html>", None))
        self.pushButton_save.setText(QCoreApplication.translate("DialogMsg", u"Guardar", None))
        self.pushButton_yes.setText(QCoreApplication.translate("DialogMsg", u"Si", None))
        self.pushButton_accept.setText(QCoreApplication.translate("DialogMsg", u"Aceptar", None))
        self.pushButton_notSave.setText(QCoreApplication.translate("DialogMsg", u"No Guardar", None))
        self.pushButton_not.setText(QCoreApplication.translate("DialogMsg", u"No", None))
        self.pushButton_cancel.setText(QCoreApplication.translate("DialogMsg", u"Cancelar", None))
    # retranslateUi

