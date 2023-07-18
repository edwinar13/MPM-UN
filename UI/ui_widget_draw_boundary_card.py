# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_boundary_cardmkQqpN.ui'
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
    QLineEdit, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormDrawBoundaryCard(object):
    def setupUi(self, FormDrawBoundaryCard):
        if not FormDrawBoundaryCard.objectName():
            FormDrawBoundaryCard.setObjectName(u"FormDrawBoundaryCard")
        FormDrawBoundaryCard.resize(517, 41)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawBoundaryCard.sizePolicy().hasHeightForWidth())
        FormDrawBoundaryCard.setSizePolicy(sizePolicy)
        FormDrawBoundaryCard.setStyleSheet(u"/*Colores primarios*/\n"
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
"QLabel#label_cardNameBoundary{\n"
"margin-left: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame#frame_card{\n"
"background: #222222;\n"
"border-radius:4px\n"
"}\n"
"\n"
"QFrame[QFrameStyle_=\"1\"]{\n"
"background: transparent;\n"
"}\n"
"\n"
"QFrame[QFrameStyle_=\"2\"]{\n"
"background: transparent;\n"
"border-radius:5px;\n"
"bor"
                        "der: 1px solid #F94646;\n"
"}\n"
"\n"
"QToolButton[style_material_point_card_button=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px ;\n"
"}\n"
"\n"
"QToolButton[style_material_point_card_button=\"1\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[style_material_point_card_button=\"1\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"QLineEdit#lineEdit_nameBoundary{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QFrame#frame_edit{\n"
"background: #333333;\n"
"border: 1px solid #222222;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QLabel[QLabelStyle=\"1\"] {\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QLabel[QLabelStyle=\"2\"] {\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QLabel[QLabelStyle=\"3\"] {\n"
"font: 300 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QComboBox[QComboBoxStyle=\"1\"] {\n"
"    border: none;\n"
"    background-color: #444444;\n"
"	color: #DDDDDD;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"	font:  9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"QComboBox[QComboBoxStyle=\"1\"] QAbstractItemView {\n"
"    border: none;\n"
"    background-color: #404040;\n"
"    color: white;\n"
"    selec"
                        "tion-background-color: #808080;\n"
"    font: 700 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox[QComboBoxStyle=\"2\"] {\n"
"    border: none;\n"
"    background-color: transparent;\n"
"	color: #DDDDDD;\n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"	font:  9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"\n"
"QComboBox[QComboBoxStyle=\"2\"]::down-arrow {\n"
"    /* Para ocultar la flecha de selecci\u00f3n */\n"
"    width: 0;\n"
"    height: 0;\n"
"    padding: 0;\n"
"    border: none;\n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(FormDrawBoundaryCard)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 5)
        self.frame_card = QFrame(FormDrawBoundaryCard)
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
        self.horizontalLayout.setContentsMargins(5, 3, 0, 3)
        self.frame_Tx = QFrame(self.frame_card)
        self.frame_Tx.setObjectName(u"frame_Tx")
        self.frame_Tx.setMinimumSize(QSize(20, 20))
        self.frame_Tx.setMaximumSize(QSize(10, 20))
        self.frame_Tx.setFrameShape(QFrame.StyledPanel)
        self.frame_Tx.setFrameShadow(QFrame.Raised)
        self.frame_Tx.setProperty("QFrameStyle_", 2)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_Tx)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.label_BoundaryTx = QLabel(self.frame_Tx)
        self.label_BoundaryTx.setObjectName(u"label_BoundaryTx")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_BoundaryTx.sizePolicy().hasHeightForWidth())
        self.label_BoundaryTx.setSizePolicy(sizePolicy2)
        self.label_BoundaryTx.setMinimumSize(QSize(0, 0))
        self.label_BoundaryTx.setMaximumSize(QSize(160, 16777215))
        self.label_BoundaryTx.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_BoundaryTx.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_BoundaryTx)


        self.horizontalLayout.addWidget(self.frame_Tx)

        self.frame_Ty = QFrame(self.frame_card)
        self.frame_Ty.setObjectName(u"frame_Ty")
        self.frame_Ty.setMinimumSize(QSize(20, 20))
        self.frame_Ty.setMaximumSize(QSize(20, 20))
        self.frame_Ty.setFrameShape(QFrame.StyledPanel)
        self.frame_Ty.setFrameShadow(QFrame.Raised)
        self.frame_Ty.setProperty("QFrameStyle_", 2)
        self.verticalLayout_2 = QVBoxLayout(self.frame_Ty)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 0, 0, 0)
        self.label_BoundaryTy = QLabel(self.frame_Ty)
        self.label_BoundaryTy.setObjectName(u"label_BoundaryTy")
        sizePolicy2.setHeightForWidth(self.label_BoundaryTy.sizePolicy().hasHeightForWidth())
        self.label_BoundaryTy.setSizePolicy(sizePolicy2)
        self.label_BoundaryTy.setMinimumSize(QSize(0, 0))
        self.label_BoundaryTy.setMaximumSize(QSize(160, 16777215))
        self.label_BoundaryTy.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_BoundaryTy.setProperty("QLabelStyle", 1)

        self.verticalLayout_2.addWidget(self.label_BoundaryTy)


        self.horizontalLayout.addWidget(self.frame_Ty)

        self.label_cardNameBoundary = QLabel(self.frame_card)
        self.label_cardNameBoundary.setObjectName(u"label_cardNameBoundary")
        sizePolicy2.setHeightForWidth(self.label_cardNameBoundary.sizePolicy().hasHeightForWidth())
        self.label_cardNameBoundary.setSizePolicy(sizePolicy2)
        self.label_cardNameBoundary.setMinimumSize(QSize(0, 0))
        self.label_cardNameBoundary.setMaximumSize(QSize(130, 16777215))
        self.label_cardNameBoundary.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_cardNameBoundary.setProperty("QLabelStyle", 3)

        self.horizontalLayout.addWidget(self.label_cardNameBoundary)

        self.lineEdit_nameBoundary = QLineEdit(self.frame_card)
        self.lineEdit_nameBoundary.setObjectName(u"lineEdit_nameBoundary")
        sizePolicy2.setHeightForWidth(self.lineEdit_nameBoundary.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameBoundary.setSizePolicy(sizePolicy2)
        self.lineEdit_nameBoundary.setMinimumSize(QSize(0, 0))
        self.lineEdit_nameBoundary.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_nameBoundary)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_okBoundary = QToolButton(self.frame_card)
        self.toolButton_okBoundary.setObjectName(u"toolButton_okBoundary")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_okBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_okBoundary.setSizePolicy(sizePolicy3)
        self.toolButton_okBoundary.setMinimumSize(QSize(25, 25))
        self.toolButton_okBoundary.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_okBoundary.setFont(font)
        self.toolButton_okBoundary.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_generales/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_okBoundary.setIcon(icon)
        self.toolButton_okBoundary.setIconSize(QSize(15, 15))
        self.toolButton_okBoundary.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_okBoundary.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_okBoundary)

        self.toolButton_exitBoundary = QToolButton(self.frame_card)
        self.toolButton_exitBoundary.setObjectName(u"toolButton_exitBoundary")
        sizePolicy3.setHeightForWidth(self.toolButton_exitBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_exitBoundary.setSizePolicy(sizePolicy3)
        self.toolButton_exitBoundary.setMinimumSize(QSize(25, 25))
        self.toolButton_exitBoundary.setMaximumSize(QSize(25, 25))
        self.toolButton_exitBoundary.setFont(font)
        self.toolButton_exitBoundary.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_generales/exit_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_exitBoundary.setIcon(icon1)
        self.toolButton_exitBoundary.setIconSize(QSize(15, 15))
        self.toolButton_exitBoundary.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_exitBoundary.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_exitBoundary)

        self.toolButton_editBoundary = QToolButton(self.frame_card)
        self.toolButton_editBoundary.setObjectName(u"toolButton_editBoundary")
        sizePolicy3.setHeightForWidth(self.toolButton_editBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_editBoundary.setSizePolicy(sizePolicy3)
        self.toolButton_editBoundary.setMinimumSize(QSize(25, 25))
        self.toolButton_editBoundary.setMaximumSize(QSize(25, 25))
        self.toolButton_editBoundary.setFont(font)
        self.toolButton_editBoundary.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_generales/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_editBoundary.setIcon(icon2)
        self.toolButton_editBoundary.setIconSize(QSize(15, 15))
        self.toolButton_editBoundary.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_editBoundary.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_editBoundary)

        self.toolButton_showHideBoundary = QToolButton(self.frame_card)
        self.toolButton_showHideBoundary.setObjectName(u"toolButton_showHideBoundary")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(25)
        sizePolicy4.setVerticalStretch(25)
        sizePolicy4.setHeightForWidth(self.toolButton_showHideBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_showHideBoundary.setSizePolicy(sizePolicy4)
        self.toolButton_showHideBoundary.setMinimumSize(QSize(25, 25))
        self.toolButton_showHideBoundary.setMaximumSize(QSize(25, 25))
        self.toolButton_showHideBoundary.setFont(font)
        self.toolButton_showHideBoundary.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideBoundary.setIcon(icon3)
        self.toolButton_showHideBoundary.setIconSize(QSize(15, 15))
        self.toolButton_showHideBoundary.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_showHideBoundary.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_showHideBoundary)

        self.toolButton_closeBoundary = QToolButton(self.frame_card)
        self.toolButton_closeBoundary.setObjectName(u"toolButton_closeBoundary")
        sizePolicy3.setHeightForWidth(self.toolButton_closeBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_closeBoundary.setSizePolicy(sizePolicy3)
        self.toolButton_closeBoundary.setMinimumSize(QSize(25, 25))
        self.toolButton_closeBoundary.setMaximumSize(QSize(25, 25))
        self.toolButton_closeBoundary.setFont(font)
        self.toolButton_closeBoundary.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeBoundary.setIcon(icon4)
        self.toolButton_closeBoundary.setIconSize(QSize(15, 15))
        self.toolButton_closeBoundary.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_closeBoundary.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_closeBoundary)


        self.verticalLayout.addWidget(self.frame_card)


        self.retranslateUi(FormDrawBoundaryCard)

        QMetaObject.connectSlotsByName(FormDrawBoundaryCard)
    # setupUi

    def retranslateUi(self, FormDrawBoundaryCard):
        FormDrawBoundaryCard.setWindowTitle(QCoreApplication.translate("FormDrawBoundaryCard", u"Form", None))
        self.label_BoundaryTx.setText(QCoreApplication.translate("FormDrawBoundaryCard", u"Tx", None))
        self.label_BoundaryTy.setText(QCoreApplication.translate("FormDrawBoundaryCard", u"Ty", None))
        self.label_cardNameBoundary.setText(QCoreApplication.translate("FormDrawBoundaryCard", u"Material. Point 1", None))
        self.lineEdit_nameBoundary.setText("")
        self.toolButton_okBoundary.setText("")
        self.toolButton_exitBoundary.setText("")
        self.toolButton_editBoundary.setText("")
        self.toolButton_showHideBoundary.setText("")
        self.toolButton_closeBoundary.setText("")
    # retranslateUi

