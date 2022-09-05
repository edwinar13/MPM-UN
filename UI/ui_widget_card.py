# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_cardewLldG.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 295)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"/*Colores primarios*/\n"
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
"QLabel#label_cardName{\n"
"font: 700 11pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QLabel#label_cardDataTime, QLabel#label_cardPath{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #999999;\n"
"}\n"
"\n"
"QFrame#frame_card{\n"
"background: #333333;\n"
"border-radius: 5px\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_card = QFrame(Form)
        self.frame_card.setObjectName(u"frame_card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_card.sizePolicy().hasHeightForWidth())
        self.frame_card.setSizePolicy(sizePolicy1)
        self.frame_card.setMinimumSize(QSize(200, 150))
        self.frame_card.setMaximumSize(QSize(200, 150))
        self.frame_card.setFrameShape(QFrame.StyledPanel)
        self.frame_card.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_card)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_img = QLabel(self.frame_card)
        self.label_img.setObjectName(u"label_img")
        sizePolicy1.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy1)
        self.label_img.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_img.setScaledContents(True)
        self.label_img.setWordWrap(False)
        self.label_img.setOpenExternalLinks(False)

        self.verticalLayout_9.addWidget(self.label_img)

        self.frame_11 = QFrame(self.frame_card)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setMaximumSize(QSize(200, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_cardName = QLabel(self.frame_11)
        self.label_cardName.setObjectName(u"label_cardName")

        self.verticalLayout_14.addWidget(self.label_cardName)

        self.label_cardDataTime = QLabel(self.frame_11)
        self.label_cardDataTime.setObjectName(u"label_cardDataTime")

        self.verticalLayout_14.addWidget(self.label_cardDataTime)

        self.label_cardPath = QLabel(self.frame_11)
        self.label_cardPath.setObjectName(u"label_cardPath")
        self.label_cardPath.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_14.addWidget(self.label_cardPath)

        self.pushButton = QPushButton(self.frame_11)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_14.addWidget(self.pushButton)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.verticalLayout.addWidget(self.frame_card)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_img.setText("")
        self.label_cardName.setText(QCoreApplication.translate("Form", u"3 SIG 83 obras", None))
        self.label_cardDataTime.setText(QCoreApplication.translate("Form", u"25/02/2022 07:32:52 A.M.", None))
        self.label_cardPath.setText(QCoreApplication.translate("Form", u"D:/Document/Ejem", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
    # retranslateUi

