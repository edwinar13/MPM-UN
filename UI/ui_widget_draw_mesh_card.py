# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_mesh_cardsQURTJ.ui'
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
    QSizePolicy, QSpacerItem, QToolButton, QWidget)

class Ui_FormDrawMeshCard(object):
    def setupUi(self, FormDrawMeshCard):
        if not FormDrawMeshCard.objectName():
            FormDrawMeshCard.setObjectName(u"FormDrawMeshCard")
        FormDrawMeshCard.resize(268, 46)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMeshCard.sizePolicy().hasHeightForWidth())
        FormDrawMeshCard.setSizePolicy(sizePolicy)
        FormDrawMeshCard.setStyleSheet(u"/*Colores primarios*/\n"
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
"QLabel#label_cardNameMesh{\n"
"font: 500 11pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"margin-left: 10px;\n"
"}\n"
"\n"
"QFrame#frame_card{\n"
"background: #222222;\n"
"border-radius:4px\n"
"}\n"
"QFrame#frame_color{\n"
"background: #D0D555;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius: 3px\n"
"}\n"
"\n"
""
                        "\n"
"QToolButton#toolButton_showHideMesh,\n"
"QToolButton#toolButton_closeMesh{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px ;\n"
"}\n"
"\n"
"QToolButton#toolButton_showHideMesh:hover, \n"
"QToolButton#toolButton_closeMesh:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton#toolButton_showHideMesh:pressed,\n"
"QToolButton#toolButton_closeMesh:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  ")
        self.horizontalLayout_2 = QHBoxLayout(FormDrawMeshCard)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 8, 5)
        self.frame_card = QFrame(FormDrawMeshCard)
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
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.frame_color = QFrame(self.frame_card)
        self.frame_color.setObjectName(u"frame_color")
        self.frame_color.setMinimumSize(QSize(10, 35))
        self.frame_color.setMaximumSize(QSize(10, 35))
        self.frame_color.setFrameShape(QFrame.StyledPanel)
        self.frame_color.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_color)

        self.label_cardNameMesh = QLabel(self.frame_card)
        self.label_cardNameMesh.setObjectName(u"label_cardNameMesh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cardNameMesh.sizePolicy().hasHeightForWidth())
        self.label_cardNameMesh.setSizePolicy(sizePolicy2)
        self.label_cardNameMesh.setMinimumSize(QSize(160, 0))
        self.label_cardNameMesh.setMaximumSize(QSize(160, 16777215))
        self.label_cardNameMesh.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_cardNameMesh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_showHideMesh = QToolButton(self.frame_card)
        self.toolButton_showHideMesh.setObjectName(u"toolButton_showHideMesh")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(25)
        sizePolicy3.setVerticalStretch(25)
        sizePolicy3.setHeightForWidth(self.toolButton_showHideMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_showHideMesh.setSizePolicy(sizePolicy3)
        self.toolButton_showHideMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_showHideMesh.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_showHideMesh.setFont(font)
        self.toolButton_showHideMesh.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideMesh.setIcon(icon)
        self.toolButton_showHideMesh.setIconSize(QSize(15, 15))
        self.toolButton_showHideMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolButton_showHideMesh)

        self.toolButton_closeMesh = QToolButton(self.frame_card)
        self.toolButton_closeMesh.setObjectName(u"toolButton_closeMesh")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.toolButton_closeMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_closeMesh.setSizePolicy(sizePolicy4)
        self.toolButton_closeMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_closeMesh.setMaximumSize(QSize(25, 25))
        self.toolButton_closeMesh.setFont(font)
        self.toolButton_closeMesh.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeMesh.setIcon(icon1)
        self.toolButton_closeMesh.setIconSize(QSize(15, 15))
        self.toolButton_closeMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolButton_closeMesh)


        self.horizontalLayout_2.addWidget(self.frame_card)


        self.retranslateUi(FormDrawMeshCard)

        QMetaObject.connectSlotsByName(FormDrawMeshCard)
    # setupUi

    def retranslateUi(self, FormDrawMeshCard):
        FormDrawMeshCard.setWindowTitle(QCoreApplication.translate("FormDrawMeshCard", u"Form", None))
        self.label_cardNameMesh.setText(QCoreApplication.translate("FormDrawMeshCard", u"Mesh 1", None))
        self.toolButton_showHideMesh.setText("")
        self.toolButton_closeMesh.setText("")
    # retranslateUi

