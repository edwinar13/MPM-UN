# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_material_point_cardCIEfQX.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_FormDrawMaterialPointCard(object):
    def setupUi(self, FormDrawMaterialPointCard):
        if not FormDrawMaterialPointCard.objectName():
            FormDrawMaterialPointCard.setObjectName(u"FormDrawMaterialPointCard")
        FormDrawMaterialPointCard.resize(481, 89)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMaterialPointCard.sizePolicy().hasHeightForWidth())
        FormDrawMaterialPointCard.setSizePolicy(sizePolicy)
        FormDrawMaterialPointCard.setStyleSheet(u"/*Colores primarios*/\n"
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
"QLabel#label_cardNameMaterialPoint{\n"
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
"}"
                        "\n"
"\n"
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
"QLineEdit#lineEdit_nameMaterialPoint{\n"
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
"border-radius: 15px\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"    selection-background-co"
                        "lor: #808080;\n"
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
        self.verticalLayout = QVBoxLayout(FormDrawMaterialPointCard)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 8, 5)
        self.frame_card = QFrame(FormDrawMaterialPointCard)
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

        self.toolButton_colorMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_colorMaterialPoint.setObjectName(u"toolButton_colorMaterialPoint")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_colorMaterialPoint.setIcon(icon)
        self.toolButton_colorMaterialPoint.setIconSize(QSize(20, 20))
        self.toolButton_colorMaterialPoint.setArrowType(Qt.NoArrow)

        self.horizontalLayout.addWidget(self.toolButton_colorMaterialPoint)

        self.label_cardNameMaterialPoint = QLabel(self.frame_card)
        self.label_cardNameMaterialPoint.setObjectName(u"label_cardNameMaterialPoint")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cardNameMaterialPoint.sizePolicy().hasHeightForWidth())
        self.label_cardNameMaterialPoint.setSizePolicy(sizePolicy2)
        self.label_cardNameMaterialPoint.setMinimumSize(QSize(150, 0))
        self.label_cardNameMaterialPoint.setMaximumSize(QSize(160, 16777215))
        self.label_cardNameMaterialPoint.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_cardNameMaterialPoint)

        self.lineEdit_nameMaterialPoint = QLineEdit(self.frame_card)
        self.lineEdit_nameMaterialPoint.setObjectName(u"lineEdit_nameMaterialPoint")
        sizePolicy2.setHeightForWidth(self.lineEdit_nameMaterialPoint.sizePolicy().hasHeightForWidth())
        self.lineEdit_nameMaterialPoint.setSizePolicy(sizePolicy2)
        self.lineEdit_nameMaterialPoint.setMinimumSize(QSize(0, 0))
        self.lineEdit_nameMaterialPoint.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_nameMaterialPoint)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_okMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_okMaterialPoint.setObjectName(u"toolButton_okMaterialPoint")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_okMaterialPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_okMaterialPoint.setSizePolicy(sizePolicy3)
        self.toolButton_okMaterialPoint.setMinimumSize(QSize(25, 25))
        self.toolButton_okMaterialPoint.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_okMaterialPoint.setFont(font)
        self.toolButton_okMaterialPoint.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_generales/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_okMaterialPoint.setIcon(icon1)
        self.toolButton_okMaterialPoint.setIconSize(QSize(15, 15))
        self.toolButton_okMaterialPoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_okMaterialPoint.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_okMaterialPoint)

        self.toolButton_exitMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_exitMaterialPoint.setObjectName(u"toolButton_exitMaterialPoint")
        sizePolicy3.setHeightForWidth(self.toolButton_exitMaterialPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_exitMaterialPoint.setSizePolicy(sizePolicy3)
        self.toolButton_exitMaterialPoint.setMinimumSize(QSize(25, 25))
        self.toolButton_exitMaterialPoint.setMaximumSize(QSize(25, 25))
        self.toolButton_exitMaterialPoint.setFont(font)
        self.toolButton_exitMaterialPoint.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_generales/exit_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_exitMaterialPoint.setIcon(icon2)
        self.toolButton_exitMaterialPoint.setIconSize(QSize(15, 15))
        self.toolButton_exitMaterialPoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_exitMaterialPoint.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_exitMaterialPoint)

        self.toolButton_editMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_editMaterialPoint.setObjectName(u"toolButton_editMaterialPoint")
        sizePolicy3.setHeightForWidth(self.toolButton_editMaterialPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_editMaterialPoint.setSizePolicy(sizePolicy3)
        self.toolButton_editMaterialPoint.setMinimumSize(QSize(25, 25))
        self.toolButton_editMaterialPoint.setMaximumSize(QSize(25, 25))
        self.toolButton_editMaterialPoint.setFont(font)
        self.toolButton_editMaterialPoint.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_generales/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_editMaterialPoint.setIcon(icon3)
        self.toolButton_editMaterialPoint.setIconSize(QSize(15, 15))
        self.toolButton_editMaterialPoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_editMaterialPoint.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_editMaterialPoint)

        self.toolButton_showHideMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_showHideMaterialPoint.setObjectName(u"toolButton_showHideMaterialPoint")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(25)
        sizePolicy4.setVerticalStretch(25)
        sizePolicy4.setHeightForWidth(self.toolButton_showHideMaterialPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_showHideMaterialPoint.setSizePolicy(sizePolicy4)
        self.toolButton_showHideMaterialPoint.setMinimumSize(QSize(25, 25))
        self.toolButton_showHideMaterialPoint.setMaximumSize(QSize(25, 25))
        self.toolButton_showHideMaterialPoint.setFont(font)
        self.toolButton_showHideMaterialPoint.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideMaterialPoint.setIcon(icon4)
        self.toolButton_showHideMaterialPoint.setIconSize(QSize(15, 15))
        self.toolButton_showHideMaterialPoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_showHideMaterialPoint.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_showHideMaterialPoint)

        self.toolButton_closeMaterialPoint = QToolButton(self.frame_card)
        self.toolButton_closeMaterialPoint.setObjectName(u"toolButton_closeMaterialPoint")
        sizePolicy3.setHeightForWidth(self.toolButton_closeMaterialPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_closeMaterialPoint.setSizePolicy(sizePolicy3)
        self.toolButton_closeMaterialPoint.setMinimumSize(QSize(25, 25))
        self.toolButton_closeMaterialPoint.setMaximumSize(QSize(25, 25))
        self.toolButton_closeMaterialPoint.setFont(font)
        self.toolButton_closeMaterialPoint.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeMaterialPoint.setIcon(icon5)
        self.toolButton_closeMaterialPoint.setIconSize(QSize(15, 15))
        self.toolButton_closeMaterialPoint.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_closeMaterialPoint.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_closeMaterialPoint)


        self.verticalLayout.addWidget(self.frame_card)

        self.frame_edit = QFrame(FormDrawMaterialPointCard)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_edit)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 20, 5)
        self.label_textPointMaterialProperty = QLabel(self.frame_edit)
        self.label_textPointMaterialProperty.setObjectName(u"label_textPointMaterialProperty")
        self.label_textPointMaterialProperty.setMinimumSize(QSize(80, 0))
        self.label_textPointMaterialProperty.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_textPointMaterialProperty.setProperty("QLabelStyle", 3)

        self.horizontalLayout_2.addWidget(self.label_textPointMaterialProperty)

        self.comboBox_PointMaterialProperty = QComboBox(self.frame_edit)
        self.comboBox_PointMaterialProperty.setObjectName(u"comboBox_PointMaterialProperty")
        self.comboBox_PointMaterialProperty.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialProperty.setFocusPolicy(Qt.WheelFocus)
        self.comboBox_PointMaterialProperty.setProperty("QComboBoxStyle", 1)

        self.horizontalLayout_2.addWidget(self.comboBox_PointMaterialProperty)


        self.verticalLayout.addWidget(self.frame_edit)


        self.retranslateUi(FormDrawMaterialPointCard)

        QMetaObject.connectSlotsByName(FormDrawMaterialPointCard)
    # setupUi

    def retranslateUi(self, FormDrawMaterialPointCard):
        FormDrawMaterialPointCard.setWindowTitle(QCoreApplication.translate("FormDrawMaterialPointCard", u"Form", None))
        self.toolButton_colorMaterialPoint.setText("")
        self.toolButton_colorMaterialPoint.setProperty("style_material_point_card_button", QCoreApplication.translate("FormDrawMaterialPointCard", u"1", None))
        self.label_cardNameMaterialPoint.setText(QCoreApplication.translate("FormDrawMaterialPointCard", u"Material. Point 1", None))
        self.lineEdit_nameMaterialPoint.setText("")
        self.toolButton_okMaterialPoint.setText("")
        self.toolButton_exitMaterialPoint.setText("")
        self.toolButton_editMaterialPoint.setText("")
        self.toolButton_showHideMaterialPoint.setText("")
        self.toolButton_closeMaterialPoint.setText("")
        self.label_textPointMaterialProperty.setText(QCoreApplication.translate("FormDrawMaterialPointCard", u"Material:", None))
    # retranslateUi

