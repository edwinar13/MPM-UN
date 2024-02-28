# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_mesh_cardOjXmhM.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QToolButton,
    QWidget)

class Ui_FormDrawMeshCard(object):
    def setupUi(self, FormDrawMeshCard):
        if not FormDrawMeshCard.objectName():
            FormDrawMeshCard.setObjectName(u"FormDrawMeshCard")
        FormDrawMeshCard.resize(481, 41)
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
"font: 500 9pt \"Ubuntu\";\n"
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
"QToolButton[style_mesh_card_button=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
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
"QLineEdit#lineEdit_nameMesh{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"")
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
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.frame_color = QFrame(self.frame_card)
        self.frame_color.setObjectName(u"frame_color")
        self.frame_color.setMinimumSize(QSize(10, 30))
        self.frame_color.setMaximumSize(QSize(10, 30))
        self.frame_color.setFrameShape(QFrame.StyledPanel)
        self.frame_color.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_color)

        self.toolButton_colorMesh = QToolButton(self.frame_card)
        self.toolButton_colorMesh.setObjectName(u"toolButton_colorMesh")
        icon = QIcon()
        icon.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_colorMesh.setIcon(icon)
        self.toolButton_colorMesh.setIconSize(QSize(20, 20))
        self.toolButton_colorMesh.setArrowType(Qt.NoArrow)
        self.toolButton_colorMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_colorMesh)

        self.label_cardNameMesh = QLabel(self.frame_card)
        self.label_cardNameMesh.setObjectName(u"label_cardNameMesh")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cardNameMesh.sizePolicy().hasHeightForWidth())
        self.label_cardNameMesh.setSizePolicy(sizePolicy2)
        self.label_cardNameMesh.setMinimumSize(QSize(150, 0))
        self.label_cardNameMesh.setMaximumSize(QSize(160, 16777215))
        self.label_cardNameMesh.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_cardNameMesh)

        self.lineEdit_nameMesh = QLineEdit(self.frame_card)
        self.lineEdit_nameMesh.setObjectName(u"lineEdit_nameMesh")
        sizePolicy2.setHeightForWidth(self.lineEdit_nameMesh.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameMesh.setSizePolicy(sizePolicy2)
        self.lineEdit_nameMesh.setMinimumSize(QSize(0, 0))
        self.lineEdit_nameMesh.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_nameMesh)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_okMesh = QToolButton(self.frame_card)
        self.toolButton_okMesh.setObjectName(u"toolButton_okMesh")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_okMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_okMesh.setSizePolicy(sizePolicy3)
        self.toolButton_okMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_okMesh.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_okMesh.setFont(font)
        self.toolButton_okMesh.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/iconos/iconos_generales/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_okMesh.setIcon(icon1)
        self.toolButton_okMesh.setIconSize(QSize(15, 15))
        self.toolButton_okMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_okMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_okMesh)

        self.toolButton_exitMesh = QToolButton(self.frame_card)
        self.toolButton_exitMesh.setObjectName(u"toolButton_exitMesh")
        sizePolicy3.setHeightForWidth(self.toolButton_exitMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_exitMesh.setSizePolicy(sizePolicy3)
        self.toolButton_exitMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_exitMesh.setMaximumSize(QSize(25, 25))
        self.toolButton_exitMesh.setFont(font)
        self.toolButton_exitMesh.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"app/resources/iconos/iconos_generales/exit_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_exitMesh.setIcon(icon2)
        self.toolButton_exitMesh.setIconSize(QSize(15, 15))
        self.toolButton_exitMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_exitMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_exitMesh)

        self.toolButton_editMesh = QToolButton(self.frame_card)
        self.toolButton_editMesh.setObjectName(u"toolButton_editMesh")
        sizePolicy3.setHeightForWidth(self.toolButton_editMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_editMesh.setSizePolicy(sizePolicy3)
        self.toolButton_editMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_editMesh.setMaximumSize(QSize(25, 25))
        self.toolButton_editMesh.setFont(font)
        self.toolButton_editMesh.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"app/resources/iconos/iconos_generales/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_editMesh.setIcon(icon3)
        self.toolButton_editMesh.setIconSize(QSize(15, 15))
        self.toolButton_editMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_editMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_editMesh)

        self.toolButton_showHideMesh = QToolButton(self.frame_card)
        self.toolButton_showHideMesh.setObjectName(u"toolButton_showHideMesh")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(25)
        sizePolicy4.setVerticalStretch(25)
        sizePolicy4.setHeightForWidth(self.toolButton_showHideMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_showHideMesh.setSizePolicy(sizePolicy4)
        self.toolButton_showHideMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_showHideMesh.setMaximumSize(QSize(25, 25))
        self.toolButton_showHideMesh.setFont(font)
        self.toolButton_showHideMesh.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideMesh.setIcon(icon4)
        self.toolButton_showHideMesh.setIconSize(QSize(15, 15))
        self.toolButton_showHideMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_showHideMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_showHideMesh)

        self.toolButton_closeMesh = QToolButton(self.frame_card)
        self.toolButton_closeMesh.setObjectName(u"toolButton_closeMesh")
        sizePolicy3.setHeightForWidth(self.toolButton_closeMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_closeMesh.setSizePolicy(sizePolicy3)
        self.toolButton_closeMesh.setMinimumSize(QSize(25, 25))
        self.toolButton_closeMesh.setMaximumSize(QSize(25, 25))
        self.toolButton_closeMesh.setFont(font)
        self.toolButton_closeMesh.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"app/resources/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeMesh.setIcon(icon5)
        self.toolButton_closeMesh.setIconSize(QSize(15, 15))
        self.toolButton_closeMesh.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_closeMesh.setProperty("style_mesh_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_closeMesh)


        self.horizontalLayout_2.addWidget(self.frame_card)


        self.retranslateUi(FormDrawMeshCard)

        QMetaObject.connectSlotsByName(FormDrawMeshCard)
    # setupUi

    def retranslateUi(self, FormDrawMeshCard):
        FormDrawMeshCard.setWindowTitle(QCoreApplication.translate("FormDrawMeshCard", u"Form", None))
        self.toolButton_colorMesh.setText("")
        self.label_cardNameMesh.setText(QCoreApplication.translate("FormDrawMeshCard", u"Mesh 1", None))
        self.lineEdit_nameMesh.setText("")
        self.toolButton_okMesh.setText("")
        self.toolButton_exitMesh.setText("")
        self.toolButton_editMesh.setText("")
        self.toolButton_showHideMesh.setText("")
        self.toolButton_closeMesh.setText("")
    # retranslateUi

