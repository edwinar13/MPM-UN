# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_card_2UOTmsN.ui'
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
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_FormCard(object):
    def setupUi(self, FormCard):
        if not FormCard.objectName():
            FormCard.setObjectName(u"FormCard")
        FormCard.resize(533, 263)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormCard.sizePolicy().hasHeightForWidth())
        FormCard.setSizePolicy(sizePolicy)
        FormCard.setStyleSheet(u"/*Colores primarios*/\n"
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
        self.horizontalLayout_2 = QHBoxLayout(FormCard)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_card = QFrame(FormCard)
        self.frame_card.setObjectName(u"frame_card")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_card.sizePolicy().hasHeightForWidth())
        self.frame_card.setSizePolicy(sizePolicy1)
        self.frame_card.setMinimumSize(QSize(0, 0))
        self.frame_card.setMaximumSize(QSize(16777215, 16777215))
        self.frame_card.setFrameShape(QFrame.StyledPanel)
        self.frame_card.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_card)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_img = QLabel(self.frame_card)
        self.label_img.setObjectName(u"label_img")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_img.sizePolicy().hasHeightForWidth())
        self.label_img.setSizePolicy(sizePolicy2)
        self.label_img.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_img.setScaledContents(True)
        self.label_img.setWordWrap(False)
        self.label_img.setOpenExternalLinks(False)

        self.horizontalLayout.addWidget(self.label_img)

        self.label = QLabel(self.frame_card)
        self.label.setObjectName(u"label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(30)
        sizePolicy3.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy3)
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u"recursos/iconos/iconos_frame_inicio/doc_mpm.svg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, -1, -1)
        self.label_cardName = QLabel(self.frame_card)
        self.label_cardName.setObjectName(u"label_cardName")

        self.verticalLayout.addWidget(self.label_cardName)

        self.label_cardPath = QLabel(self.frame_card)
        self.label_cardPath.setObjectName(u"label_cardPath")
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_cardPath.sizePolicy().hasHeightForWidth())
        self.label_cardPath.setSizePolicy(sizePolicy4)
        self.label_cardPath.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.label_cardPath)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_cardDataTime = QLabel(self.frame_card)
        self.label_cardDataTime.setObjectName(u"label_cardDataTime")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_cardDataTime.sizePolicy().hasHeightForWidth())
        self.label_cardDataTime.setSizePolicy(sizePolicy5)
        self.label_cardDataTime.setMinimumSize(QSize(160, 0))
        self.label_cardDataTime.setMaximumSize(QSize(160, 16777215))
        self.label_cardDataTime.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_cardDataTime)


        self.horizontalLayout_2.addWidget(self.frame_card)


        self.retranslateUi(FormCard)

        QMetaObject.connectSlotsByName(FormCard)
    # setupUi

    def retranslateUi(self, FormCard):
        FormCard.setWindowTitle(QCoreApplication.translate("FormCard", u"Form", None))
        self.label_img.setText("")
        self.label.setText("")
        self.label_cardName.setText(QCoreApplication.translate("FormCard", u"3 SIG 83 obras", None))
        self.label_cardPath.setText(QCoreApplication.translate("FormCard", u"D:/Document/EjemD:/Document/EjemD:/Document/EjemD:/Document/Ejem", None))
        self.label_cardDataTime.setText(QCoreApplication.translate("FormCard", u"25/02/2022 07:32:52 A.M.", None))
    # retranslateUi

