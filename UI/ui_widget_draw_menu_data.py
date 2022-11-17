# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_datamtLUar.ui'
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

class Ui_FormDrawMenuData(object):
    def setupUi(self, FormDrawMenuData):
        if not FormDrawMenuData.objectName():
            FormDrawMenuData.setObjectName(u"FormDrawMenuData")
        FormDrawMenuData.resize(350, 477)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuData.sizePolicy().hasHeightForWidth())
        FormDrawMenuData.setSizePolicy(sizePolicy)
        FormDrawMenuData.setMinimumSize(QSize(0, 0))
        FormDrawMenuData.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuData.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_dataProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
""
                        "\n"
"/*#################################################################*/\n"
"/*####################       FRAME HIDE       ###########################*/\n"
"/*#################################################################*/\n"
"\n"
"QFrame#frame_hide{\n"
"background: transparent;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"QFrame#frame_hide2{\n"
"background: #222222;\n"
"border-top-left-radius: 8px;\n"
"}\n"
"QToolButton#toolButton_hideShow{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*####################       FRAME DATA       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_data{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardDataTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_dataSubTitle1,\n"
"QFrame#frame_dataSub"
                        "Title2{\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"QLabel#label_cardDataSubTitle1,\n"
"QLabel#label_cardDataSubTitle2{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QToolButton#toolButton_cardDataSubTitle1,\n"
"QToolButton#toolButton_cardDataSubTitle2{\n"
"background-color: transparent;\n"
"}\n"
"QLabel#label_textData1,\n"
"QLabel#label_textData2,\n"
"QLabel#label_textData3,\n"
"QLabel#label_textData4,\n"
"QLabel#label_textData5{\n"
"font: 300 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QLineEdit#lineEdit_textData1,\n"
"QLineEdit#lineEdit_textData2,\n"
"QLineEdit#lineEdit_textData3,\n"
"QLineEdit#lineEdit_textData5{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
"QTextEdit#textEdit_textData4{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
"QToolButton#toolButton"
                        "_updateData{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 15px ;\n"
"}\n"
"\n"
"QToolButton#toolButton_saveData:hover{\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel#label_msn{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuData)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_dataProject = QFrame(FormDrawMenuData)
        self.frame_dataProject.setObjectName(u"frame_dataProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_dataProject.sizePolicy().hasHeightForWidth())
        self.frame_dataProject.setSizePolicy(sizePolicy1)
        self.frame_dataProject.setFrameShape(QFrame.StyledPanel)
        self.frame_dataProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_dataProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_dataProject)
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
        self.frame_hide2 = QFrame(self.frame_hide)
        self.frame_hide2.setObjectName(u"frame_hide2")
        sizePolicy2.setHeightForWidth(self.frame_hide2.sizePolicy().hasHeightForWidth())
        self.frame_hide2.setSizePolicy(sizePolicy2)
        self.frame_hide2.setMinimumSize(QSize(20, 0))
        self.frame_hide2.setFrameShape(QFrame.StyledPanel)
        self.frame_hide2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_hide2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_hideShow = QToolButton(self.frame_hide2)
        self.toolButton_hideShow.setObjectName(u"toolButton_hideShow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_hideShow.sizePolicy().hasHeightForWidth())
        self.toolButton_hideShow.setSizePolicy(sizePolicy3)
        self.toolButton_hideShow.setMinimumSize(QSize(20, 30))
        self.toolButton_hideShow.setMaximumSize(QSize(20, 30))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_hideShow.setFont(font)
        self.toolButton_hideShow.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_hideShow.setIcon(icon)
        self.toolButton_hideShow.setIconSize(QSize(15, 15))
        self.toolButton_hideShow.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hideShow)


        self.verticalLayout_2.addWidget(self.frame_hide2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_data = QFrame(self.frame_dataProject)
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
        self.frame_dataSubTitle1 = QFrame(self.frame_info)
        self.frame_dataSubTitle1.setObjectName(u"frame_dataSubTitle1")
        self.frame_dataSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_dataSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_dataSubTitle1)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle1 = QLabel(self.frame_dataSubTitle1)
        self.label_cardDataSubTitle1.setObjectName(u"label_cardDataSubTitle1")

        self.horizontalLayout_4.addWidget(self.label_cardDataSubTitle1)

        self.toolButton_cardDataSubTitle1 = QToolButton(self.frame_dataSubTitle1)
        self.toolButton_cardDataSubTitle1.setObjectName(u"toolButton_cardDataSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataSubTitle1.setIcon(icon1)
        self.toolButton_cardDataSubTitle1.setArrowType(Qt.NoArrow)

        self.horizontalLayout_4.addWidget(self.toolButton_cardDataSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_dataSubTitle1)

        self.frame_data1 = QFrame(self.frame_info)
        self.frame_data1.setObjectName(u"frame_data1")
        self.frame_data1.setFrameShape(QFrame.StyledPanel)
        self.frame_data1.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_data1)
        self.formLayout.setObjectName(u"formLayout")
        self.label_textData1 = QLabel(self.frame_data1)
        self.label_textData1.setObjectName(u"label_textData1")
        self.label_textData1.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_textData1)

        self.lineEdit_textData1 = QLineEdit(self.frame_data1)
        self.lineEdit_textData1.setObjectName(u"lineEdit_textData1")
        self.lineEdit_textData1.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textData1)

        self.label_textData2 = QLabel(self.frame_data1)
        self.label_textData2.setObjectName(u"label_textData2")
        self.label_textData2.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_textData2)

        self.lineEdit_textData2 = QLineEdit(self.frame_data1)
        self.lineEdit_textData2.setObjectName(u"lineEdit_textData2")
        self.lineEdit_textData2.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_textData2)

        self.label_textData3 = QLabel(self.frame_data1)
        self.label_textData3.setObjectName(u"label_textData3")
        self.label_textData3.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_textData3)

        self.lineEdit_textData3 = QLineEdit(self.frame_data1)
        self.lineEdit_textData3.setObjectName(u"lineEdit_textData3")
        self.lineEdit_textData3.setMinimumSize(QSize(150, 25))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_textData3)

        self.label_textData4 = QLabel(self.frame_data1)
        self.label_textData4.setObjectName(u"label_textData4")
        self.label_textData4.setMinimumSize(QSize(110, 0))

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_textData4)

        self.textEdit_textData4 = QTextEdit(self.frame_data1)
        self.textEdit_textData4.setObjectName(u"textEdit_textData4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textEdit_textData4.sizePolicy().hasHeightForWidth())
        self.textEdit_textData4.setSizePolicy(sizePolicy5)
        self.textEdit_textData4.setMinimumSize(QSize(150, 75))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_textData4)


        self.verticalLayout_5.addWidget(self.frame_data1)

        self.frame_dataSubTitle2 = QFrame(self.frame_info)
        self.frame_dataSubTitle2.setObjectName(u"frame_dataSubTitle2")
        self.frame_dataSubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_dataSubTitle2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_dataSubTitle2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle2 = QLabel(self.frame_dataSubTitle2)
        self.label_cardDataSubTitle2.setObjectName(u"label_cardDataSubTitle2")

        self.horizontalLayout_3.addWidget(self.label_cardDataSubTitle2)

        self.toolButton_cardDataSubTitle2 = QToolButton(self.frame_dataSubTitle2)
        self.toolButton_cardDataSubTitle2.setObjectName(u"toolButton_cardDataSubTitle2")
        self.toolButton_cardDataSubTitle2.setIcon(icon1)
        self.toolButton_cardDataSubTitle2.setArrowType(Qt.NoArrow)

        self.horizontalLayout_3.addWidget(self.toolButton_cardDataSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_dataSubTitle2)

        self.frame_data2 = QFrame(self.frame_info)
        self.frame_data2.setObjectName(u"frame_data2")
        self.frame_data2.setFrameShape(QFrame.StyledPanel)
        self.frame_data2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_data2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_textData5 = QLabel(self.frame_data2)
        self.label_textData5.setObjectName(u"label_textData5")
        self.label_textData5.setMinimumSize(QSize(110, 0))

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_textData5)

        self.lineEdit_textData5 = QLineEdit(self.frame_data2)
        self.lineEdit_textData5.setObjectName(u"lineEdit_textData5")
        self.lineEdit_textData5.setMinimumSize(QSize(150, 25))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textData5)


        self.verticalLayout_5.addWidget(self.frame_data2)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msn = QLabel(self.frame_info)
        self.label_msn.setObjectName(u"label_msn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_msn.sizePolicy().hasHeightForWidth())
        self.label_msn.setSizePolicy(sizePolicy6)
        self.label_msn.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_msn)

        self.toolButton_updateData = QToolButton(self.frame_info)
        self.toolButton_updateData.setObjectName(u"toolButton_updateData")

        self.horizontalLayout_5.addWidget(self.toolButton_updateData)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_data)


        self.horizontalLayout_6.addWidget(self.frame_dataProject)


        self.retranslateUi(FormDrawMenuData)

        QMetaObject.connectSlotsByName(FormDrawMenuData)
    # setupUi

    def retranslateUi(self, FormDrawMenuData):
        FormDrawMenuData.setWindowTitle(QCoreApplication.translate("FormDrawMenuData", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardDataTitle.setText(QCoreApplication.translate("FormDrawMenuData", u"INFORMACI\u00d3N DEL PROYECTO", None))
        self.label_cardDataSubTitle1.setText(QCoreApplication.translate("FormDrawMenuData", u"Datos del proyecto", None))
        self.toolButton_cardDataSubTitle1.setText("")
        self.label_textData1.setText(QCoreApplication.translate("FormDrawMenuData", u"T\u00edtulo del proyecto:", None))
        self.label_textData2.setText(QCoreApplication.translate("FormDrawMenuData", u"Localizaci\u00f3n:", None))
        self.label_textData3.setText(QCoreApplication.translate("FormDrawMenuData", u"Autor:", None))
        self.label_textData4.setText(QCoreApplication.translate("FormDrawMenuData", u"Descripci\u00f3n:", None))
        self.label_cardDataSubTitle2.setText(QCoreApplication.translate("FormDrawMenuData", u"Configuraci\u00f3n del proyecto", None))
        self.toolButton_cardDataSubTitle2.setText("")
        self.label_textData5.setText(QCoreApplication.translate("FormDrawMenuData", u"<html><head/><body><p>Gravedad [m/s<span style=\" vertical-align:super;\">2</span>]:</p></body></html>", None))
        self.lineEdit_textData5.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuData", u"Empty", None))
        self.toolButton_updateData.setText(QCoreApplication.translate("FormDrawMenuData", u"Actualizar", None))
    # retranslateUi

