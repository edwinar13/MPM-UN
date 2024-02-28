# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_result_card_pointWIksBz.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_FormResultCardPoint(object):
    def setupUi(self, FormResultCardPoint):
        if not FormResultCardPoint.objectName():
            FormResultCardPoint.setObjectName(u"FormResultCardPoint")
        FormResultCardPoint.resize(321, 45)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormResultCardPoint.sizePolicy().hasHeightForWidth())
        FormResultCardPoint.setSizePolicy(sizePolicy)
        FormResultCardPoint.setStyleSheet(u"/*Colores primarios*/\n"
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
"\n"
"QFrame#frame_card{\n"
"background: #222222;\n"
"border-radius:6px\n"
"}\n"
"QFrame#frame_color{\n"
"background: #D0D555;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius: 3px\n"
"}\n"
"\n"
"\n"
"QToolButton[style_mesh_card_button=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid"
                        " #222222;\n"
"border-radius: 3px ;\n"
"}\n"
"\n"
"QToolButton[style_mesh_card_button=\"1\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[style_mesh_card_button=\"1\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"QLabel[QLabelStyle=\"1\"]{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(FormResultCardPoint)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.frame_card = QFrame(FormResultCardPoint)
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
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 2, 0)
        self.frame_color = QFrame(self.frame_card)
        self.frame_color.setObjectName(u"frame_color")
        self.frame_color.setMinimumSize(QSize(20, 30))
        self.frame_color.setMaximumSize(QSize(10, 30))
        self.frame_color.setFrameShape(QFrame.StyledPanel)
        self.frame_color.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_color)

        self.label_cardNamePoint = QLabel(self.frame_card)
        self.label_cardNamePoint.setObjectName(u"label_cardNamePoint")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cardNamePoint.sizePolicy().hasHeightForWidth())
        self.label_cardNamePoint.setSizePolicy(sizePolicy2)
        self.label_cardNamePoint.setMinimumSize(QSize(35, 0))
        self.label_cardNamePoint.setMaximumSize(QSize(35, 16777215))
        self.label_cardNamePoint.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_cardNamePoint.setProperty("QLabelStyle", 1)

        self.horizontalLayout.addWidget(self.label_cardNamePoint)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_showHidePoint = QToolButton(self.frame_card)
        self.toolButton_showHidePoint.setObjectName(u"toolButton_showHidePoint")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(25)
        sizePolicy3.setVerticalStretch(25)
        sizePolicy3.setHeightForWidth(self.toolButton_showHidePoint.sizePolicy().hasHeightForWidth())
        self.toolButton_showHidePoint.setSizePolicy(sizePolicy3)
        self.toolButton_showHidePoint.setMinimumSize(QSize(25, 25))
        self.toolButton_showHidePoint.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_showHidePoint.setFont(font)
        self.toolButton_showHidePoint.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHidePoint.setIcon(icon)
        self.toolButton_showHidePoint.setIconSize(QSize(15, 15))
        self.toolButton_showHidePoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_showHidePoint.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_showHidePoint)

        self.toolButton_closePoint = QToolButton(self.frame_card)
        self.toolButton_closePoint.setObjectName(u"toolButton_closePoint")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.toolButton_closePoint.sizePolicy().hasHeightForWidth())
        self.toolButton_closePoint.setSizePolicy(sizePolicy4)
        self.toolButton_closePoint.setMinimumSize(QSize(25, 25))
        self.toolButton_closePoint.setMaximumSize(QSize(25, 25))
        self.toolButton_closePoint.setFont(font)
        self.toolButton_closePoint.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closePoint.setIcon(icon1)
        self.toolButton_closePoint.setIconSize(QSize(15, 15))
        self.toolButton_closePoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_closePoint.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_closePoint)


        self.horizontalLayout_2.addWidget(self.frame_card)


        self.retranslateUi(FormResultCardPoint)

        QMetaObject.connectSlotsByName(FormResultCardPoint)
    # setupUi

    def retranslateUi(self, FormResultCardPoint):
        FormResultCardPoint.setWindowTitle(QCoreApplication.translate("FormResultCardPoint", u"Form", None))
        self.label_cardNamePoint.setText(QCoreApplication.translate("FormResultCardPoint", u"0000", None))
        self.toolButton_showHidePoint.setText("")
        self.toolButton_closePoint.setText("")
    # retranslateUi

