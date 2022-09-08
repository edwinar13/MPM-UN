# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_data_projectiqzFCJ.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QTextEdit, QToolButton, QVBoxLayout, QWidget)

class Ui_FormDataProject(object):
    def setupUi(self, FormDataProject):
        if not FormDataProject.objectName():
            FormDataProject.setObjectName(u"FormDataProject")
        FormDataProject.resize(346, 869)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDataProject.sizePolicy().hasHeightForWidth())
        FormDataProject.setSizePolicy(sizePolicy)
        FormDataProject.setMinimumSize(QSize(0, 0))
        FormDataProject.setMaximumSize(QSize(16777215, 16777215))
        FormDataProject.setStyleSheet(u"/*Colores primarios*/\n"
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
"/*\n"
"border-top-left-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"border-bottom-left-radius: 5px\n"
"border: none;\n"
"padding: 2px 0px;\n"
"*/\n"
"\n"
"\n"
"/****************************************************************************************************************************************************/\n"
"\n"
"QWidget#FormDataProject{\n"
"\n"
"}\n"
"\n"
"QFrame#frame_data_project{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}"
                        "\n"
"\n"
"/*#################################################################*/\n"
"/*####################       FRAME HIDE       ###########################*/\n"
"/*#################################################################*/\n"
"\n"
"QFrame#frame_hide{\n"
"background: transparent;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"QFrame#frame_hide_2{\n"
"background: #222222;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"\n"
"QToolButton#toolButton_hide_show{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*####################       FRAME DATA       ###########################*/\n"
"/*#################################################################*/\n"
"\n"
"\n"
"QFrame#frame_data{\n"
"background: transparent;\n"
"}\n"
"\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"\n"
"}\n"
"\n"
"\n"
"QLabel#label_cardDataTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QFram"
                        "e#frame_DataSubTitle_1,\n"
"QFrame#frame_DataSubTitle_2{\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"QLabel#label_cardDataSubTitle_1,\n"
"QLabel#label_cardDataSubTitle_2{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QToolButton#toolButton_cardDataSubTitle_1,\n"
"QToolButton#toolButton_cardDataSubTitle_2{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"QLabel#label_WDP_1,\n"
"QLabel#label_WDP_2,\n"
"QLabel#label_WDP_3,\n"
"QLabel#label_WDP_4,\n"
"QLabel#label_WDP_5{\n"
"font: 300 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"QLineEdit#lineEdit_WDP_1,\n"
"QLineEdit#lineEdit_WDP_2,\n"
"QLineEdit#lineEdit_WDP_3,\n"
"QLineEdit#lineEdit_WDP_5{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
"QTextEdit#textEdit_WDP_4{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6p"
                        "x;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"/*\n"
"\n"
"\n"
"\n"
"\n"
"    QLineEdit#lineEdit_console:hover {\n"
"        border: 2px solid rgb(64, 71, 88);\n"
"    }\n"
"    QLineEdit#lineEdit_console:focus {\n"
"        border: 2px solid rgb(91, 101, 124);\n"
"    }\n"
"*/\n"
"\n"
"\n"
"QToolButton#toolButton_saveData{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 15px ;\n"
"\n"
"}\n"
"\n"
"QToolButton#toolButton_saveData:hover{\n"
"\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDataProject)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_data_project = QFrame(FormDataProject)
        self.frame_data_project.setObjectName(u"frame_data_project")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_data_project.sizePolicy().hasHeightForWidth())
        self.frame_data_project.setSizePolicy(sizePolicy1)
        self.frame_data_project.setFrameShape(QFrame.StyledPanel)
        self.frame_data_project.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_data_project)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_data_project)
        self.frame_hide.setObjectName(u"frame_hide")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_hide.sizePolicy().hasHeightForWidth())
        self.frame_hide.setSizePolicy(sizePolicy2)
        self.frame_hide.setMinimumSize(QSize(20, 0))
        self.frame_hide.setFrameShape(QFrame.StyledPanel)
        self.frame_hide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_hide)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_hide_2 = QFrame(self.frame_hide)
        self.frame_hide_2.setObjectName(u"frame_hide_2")
        sizePolicy2.setHeightForWidth(self.frame_hide_2.sizePolicy().hasHeightForWidth())
        self.frame_hide_2.setSizePolicy(sizePolicy2)
        self.frame_hide_2.setMinimumSize(QSize(20, 0))
        self.frame_hide_2.setFrameShape(QFrame.StyledPanel)
        self.frame_hide_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_hide_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_hide_show = QToolButton(self.frame_hide_2)
        self.toolButton_hide_show.setObjectName(u"toolButton_hide_show")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_hide_show.sizePolicy().hasHeightForWidth())
        self.toolButton_hide_show.setSizePolicy(sizePolicy3)
        self.toolButton_hide_show.setMinimumSize(QSize(20, 30))
        self.toolButton_hide_show.setMaximumSize(QSize(20, 30))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_hide_show.setFont(font)
        self.toolButton_hide_show.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_hide_show.setIcon(icon)
        self.toolButton_hide_show.setIconSize(QSize(15, 15))
        self.toolButton_hide_show.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hide_show)


        self.verticalLayout_2.addWidget(self.frame_hide_2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_data = QFrame(self.frame_data_project)
        self.frame_data.setObjectName(u"frame_data")
        sizePolicy1.setHeightForWidth(self.frame_data.sizePolicy().hasHeightForWidth())
        self.frame_data.setSizePolicy(sizePolicy1)
        self.frame_data.setFrameShape(QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_data)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_data)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy4)
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.frame_title.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cardDataTitle = QLabel(self.frame_title)
        self.label_cardDataTitle.setObjectName(u"label_cardDataTitle")

        self.horizontalLayout_2.addWidget(self.label_cardDataTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_data)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_DataSubTitle_1 = QFrame(self.frame_info)
        self.frame_DataSubTitle_1.setObjectName(u"frame_DataSubTitle_1")
        self.frame_DataSubTitle_1.setFrameShape(QFrame.StyledPanel)
        self.frame_DataSubTitle_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_DataSubTitle_1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle_1 = QLabel(self.frame_DataSubTitle_1)
        self.label_cardDataSubTitle_1.setObjectName(u"label_cardDataSubTitle_1")

        self.horizontalLayout_4.addWidget(self.label_cardDataSubTitle_1)

        self.toolButton_cardDataSubTitle_1 = QToolButton(self.frame_DataSubTitle_1)
        self.toolButton_cardDataSubTitle_1.setObjectName(u"toolButton_cardDataSubTitle_1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataSubTitle_1.setIcon(icon1)
        self.toolButton_cardDataSubTitle_1.setArrowType(Qt.NoArrow)

        self.horizontalLayout_4.addWidget(self.toolButton_cardDataSubTitle_1)


        self.verticalLayout_5.addWidget(self.frame_DataSubTitle_1)

        self.frame_data_1 = QFrame(self.frame_info)
        self.frame_data_1.setObjectName(u"frame_data_1")
        self.frame_data_1.setFrameShape(QFrame.StyledPanel)
        self.frame_data_1.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_data_1)
        self.formLayout.setObjectName(u"formLayout")
        self.label_WDP_1 = QLabel(self.frame_data_1)
        self.label_WDP_1.setObjectName(u"label_WDP_1")
        self.label_WDP_1.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_WDP_1)

        self.lineEdit_WDP_1 = QLineEdit(self.frame_data_1)
        self.lineEdit_WDP_1.setObjectName(u"lineEdit_WDP_1")
        self.lineEdit_WDP_1.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_WDP_1)

        self.label_WDP_2 = QLabel(self.frame_data_1)
        self.label_WDP_2.setObjectName(u"label_WDP_2")
        self.label_WDP_2.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_WDP_2)

        self.lineEdit_WDP_3 = QLineEdit(self.frame_data_1)
        self.lineEdit_WDP_3.setObjectName(u"lineEdit_WDP_3")
        self.lineEdit_WDP_3.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_WDP_3)

        self.label_WDP_3 = QLabel(self.frame_data_1)
        self.label_WDP_3.setObjectName(u"label_WDP_3")
        self.label_WDP_3.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_WDP_3)

        self.lineEdit_WDP_2 = QLineEdit(self.frame_data_1)
        self.lineEdit_WDP_2.setObjectName(u"lineEdit_WDP_2")
        self.lineEdit_WDP_2.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_WDP_2)

        self.label_WDP_4 = QLabel(self.frame_data_1)
        self.label_WDP_4.setObjectName(u"label_WDP_4")
        self.label_WDP_4.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_WDP_4)

        self.textEdit_WDP_4 = QTextEdit(self.frame_data_1)
        self.textEdit_WDP_4.setObjectName(u"textEdit_WDP_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit_WDP_4.sizePolicy().hasHeightForWidth())
        self.textEdit_WDP_4.setSizePolicy(sizePolicy5)
        self.textEdit_WDP_4.setMinimumSize(QSize(150, 75))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_WDP_4)


        self.verticalLayout_5.addWidget(self.frame_data_1)

        self.frame_DataSubTitle_2 = QFrame(self.frame_info)
        self.frame_DataSubTitle_2.setObjectName(u"frame_DataSubTitle_2")
        self.frame_DataSubTitle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_DataSubTitle_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_DataSubTitle_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle_2 = QLabel(self.frame_DataSubTitle_2)
        self.label_cardDataSubTitle_2.setObjectName(u"label_cardDataSubTitle_2")

        self.horizontalLayout_3.addWidget(self.label_cardDataSubTitle_2)

        self.toolButton_cardDataSubTitle_2 = QToolButton(self.frame_DataSubTitle_2)
        self.toolButton_cardDataSubTitle_2.setObjectName(u"toolButton_cardDataSubTitle_2")
        self.toolButton_cardDataSubTitle_2.setIcon(icon1)
        self.toolButton_cardDataSubTitle_2.setArrowType(Qt.NoArrow)

        self.horizontalLayout_3.addWidget(self.toolButton_cardDataSubTitle_2)


        self.verticalLayout_5.addWidget(self.frame_DataSubTitle_2)

        self.frame_data_2 = QFrame(self.frame_info)
        self.frame_data_2.setObjectName(u"frame_data_2")
        self.frame_data_2.setFrameShape(QFrame.StyledPanel)
        self.frame_data_2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_data_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_WDP_5 = QLabel(self.frame_data_2)
        self.label_WDP_5.setObjectName(u"label_WDP_5")
        self.label_WDP_5.setMinimumSize(QSize(110, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_WDP_5)

        self.lineEdit_WDP_5 = QLineEdit(self.frame_data_2)
        self.lineEdit_WDP_5.setObjectName(u"lineEdit_WDP_5")
        self.lineEdit_WDP_5.setMinimumSize(QSize(150, 25))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_WDP_5)


        self.verticalLayout_5.addWidget(self.frame_data_2)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.toolButton_saveData = QToolButton(self.frame_info)
        self.toolButton_saveData.setObjectName(u"toolButton_saveData")

        self.horizontalLayout_5.addWidget(self.toolButton_saveData)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_data)


        self.horizontalLayout_6.addWidget(self.frame_data_project)


        self.retranslateUi(FormDataProject)

        QMetaObject.connectSlotsByName(FormDataProject)
    # setupUi

    def retranslateUi(self, FormDataProject):
        FormDataProject.setWindowTitle(QCoreApplication.translate("FormDataProject", u"Form", None))
        self.toolButton_hide_show.setText("")
        self.label_cardDataTitle.setText(QCoreApplication.translate("FormDataProject", u"INFORMACI\u00d3N DEL PROYECTO", None))
        self.label_cardDataSubTitle_1.setText(QCoreApplication.translate("FormDataProject", u"Datos del proyecto", None))
        self.toolButton_cardDataSubTitle_1.setText("")
        self.label_WDP_1.setText(QCoreApplication.translate("FormDataProject", u"T\u00edtulo del proyecto:", None))
        self.label_WDP_2.setText(QCoreApplication.translate("FormDataProject", u"Localizaci\u00f3n:", None))
        self.label_WDP_3.setText(QCoreApplication.translate("FormDataProject", u"Autor:", None))
        self.label_WDP_4.setText(QCoreApplication.translate("FormDataProject", u"Descripci\u00f3n:", None))
        self.label_cardDataSubTitle_2.setText(QCoreApplication.translate("FormDataProject", u"Configuraci\u00f3n del proyecto", None))
        self.toolButton_cardDataSubTitle_2.setText("")
        self.label_WDP_5.setText(QCoreApplication.translate("FormDataProject", u"<html><head/><body><p>Gravedad [m/s<span style=\" vertical-align:super;\">2</span>]:</p></body></html>", None))
        self.lineEdit_WDP_5.setText(QCoreApplication.translate("FormDataProject", u"9.8 m/s2", None))
        self.toolButton_saveData.setText(QCoreApplication.translate("FormDataProject", u"Guardar", None))
    # retranslateUi

