# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_property_cardZHyEYY.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormDrawPropertyCard(object):
    def setupUi(self, FormDrawPropertyCard):
        if not FormDrawPropertyCard.objectName():
            FormDrawPropertyCard.setObjectName(u"FormDrawPropertyCard")
        FormDrawPropertyCard.resize(437, 339)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawPropertyCard.sizePolicy().hasHeightForWidth())
        FormDrawPropertyCard.setSizePolicy(sizePolicy)
        FormDrawPropertyCard.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_properties1{\n"
"background: #333333;\n"
"border: 1px solid #222222;\n"
"border-radius: 15px\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel#label_cardPropertyName{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"margin-left: 5px;\n"
"}\n"
"\n"
"QFrame#frame_card{\n"
"background: #222222;\n"
"border-radius:4px\n"
""
                        "}\n"
"QFrame#frame_color{\n"
"background: #D0D555;\n"
"border-top-right-radius:3px;\n"
"border-bottom-right-radius: 3px\n"
"}\n"
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
"QLineEdit#lineEdit_PropertyName{\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QToolButton[QToolButtonSubTitleStyle=\"1\"] {\n"
"background-color: transparent;\n"
"margin-left: 5px;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QDoubleSpinBox           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QDou"
                        "bleSpinBox[QDoubleSpinBoxStyle=\"1\"]{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}")
        self.verticalLayout = QVBoxLayout(FormDrawPropertyCard)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 8, 5)
        self.frame_card = QFrame(FormDrawPropertyCard)
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
        self.toolButton_PropertiesShow = QToolButton(self.frame_card)
        self.toolButton_PropertiesShow.setObjectName(u"toolButton_PropertiesShow")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PropertiesShow.setIcon(icon)
        self.toolButton_PropertiesShow.setArrowType(Qt.NoArrow)
        self.toolButton_PropertiesShow.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout.addWidget(self.toolButton_PropertiesShow)

        self.label_cardPropertyName = QLabel(self.frame_card)
        self.label_cardPropertyName.setObjectName(u"label_cardPropertyName")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_cardPropertyName.sizePolicy().hasHeightForWidth())
        self.label_cardPropertyName.setSizePolicy(sizePolicy2)
        self.label_cardPropertyName.setMinimumSize(QSize(150, 0))
        self.label_cardPropertyName.setMaximumSize(QSize(160, 16777215))
        self.label_cardPropertyName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_cardPropertyName)

        self.lineEdit_PropertyName = QLineEdit(self.frame_card)
        self.lineEdit_PropertyName.setObjectName(u"lineEdit_PropertyName")
        sizePolicy2.setHeightForWidth(self.lineEdit_PropertyName.sizePolicy().hasHeightForWidth())
        self.lineEdit_PropertyName.setSizePolicy(sizePolicy2)
        self.lineEdit_PropertyName.setMinimumSize(QSize(0, 0))
        self.lineEdit_PropertyName.setMaximumSize(QSize(160, 16777215))

        self.horizontalLayout.addWidget(self.lineEdit_PropertyName)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.toolButton_PropertyOk = QToolButton(self.frame_card)
        self.toolButton_PropertyOk.setObjectName(u"toolButton_PropertyOk")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_PropertyOk.sizePolicy().hasHeightForWidth())
        self.toolButton_PropertyOk.setSizePolicy(sizePolicy3)
        self.toolButton_PropertyOk.setMinimumSize(QSize(25, 25))
        self.toolButton_PropertyOk.setMaximumSize(QSize(25, 25))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_PropertyOk.setFont(font)
        self.toolButton_PropertyOk.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_generales/ok.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PropertyOk.setIcon(icon1)
        self.toolButton_PropertyOk.setIconSize(QSize(15, 15))
        self.toolButton_PropertyOk.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_PropertyOk.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_PropertyOk)

        self.toolButton_PropertyExit = QToolButton(self.frame_card)
        self.toolButton_PropertyExit.setObjectName(u"toolButton_PropertyExit")
        sizePolicy3.setHeightForWidth(self.toolButton_PropertyExit.sizePolicy().hasHeightForWidth())
        self.toolButton_PropertyExit.setSizePolicy(sizePolicy3)
        self.toolButton_PropertyExit.setMinimumSize(QSize(25, 25))
        self.toolButton_PropertyExit.setMaximumSize(QSize(25, 25))
        self.toolButton_PropertyExit.setFont(font)
        self.toolButton_PropertyExit.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_generales/exit_2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PropertyExit.setIcon(icon2)
        self.toolButton_PropertyExit.setIconSize(QSize(15, 15))
        self.toolButton_PropertyExit.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_PropertyExit.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_PropertyExit)

        self.toolButton_PropertyEdit = QToolButton(self.frame_card)
        self.toolButton_PropertyEdit.setObjectName(u"toolButton_PropertyEdit")
        sizePolicy3.setHeightForWidth(self.toolButton_PropertyEdit.sizePolicy().hasHeightForWidth())
        self.toolButton_PropertyEdit.setSizePolicy(sizePolicy3)
        self.toolButton_PropertyEdit.setMinimumSize(QSize(25, 25))
        self.toolButton_PropertyEdit.setMaximumSize(QSize(25, 25))
        self.toolButton_PropertyEdit.setFont(font)
        self.toolButton_PropertyEdit.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_generales/edit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PropertyEdit.setIcon(icon3)
        self.toolButton_PropertyEdit.setIconSize(QSize(15, 15))
        self.toolButton_PropertyEdit.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_PropertyEdit.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_PropertyEdit)

        self.toolButton_PropertyClose = QToolButton(self.frame_card)
        self.toolButton_PropertyClose.setObjectName(u"toolButton_PropertyClose")
        sizePolicy3.setHeightForWidth(self.toolButton_PropertyClose.sizePolicy().hasHeightForWidth())
        self.toolButton_PropertyClose.setSizePolicy(sizePolicy3)
        self.toolButton_PropertyClose.setMinimumSize(QSize(25, 25))
        self.toolButton_PropertyClose.setMaximumSize(QSize(25, 25))
        self.toolButton_PropertyClose.setFont(font)
        self.toolButton_PropertyClose.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PropertyClose.setIcon(icon4)
        self.toolButton_PropertyClose.setIconSize(QSize(15, 15))
        self.toolButton_PropertyClose.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self.toolButton_PropertyClose.setProperty("style_material_point_card_button", 1)

        self.horizontalLayout.addWidget(self.toolButton_PropertyClose)


        self.verticalLayout.addWidget(self.frame_card)

        self.frame_properties1 = QFrame(FormDrawPropertyCard)
        self.frame_properties1.setObjectName(u"frame_properties1")
        sizePolicy.setHeightForWidth(self.frame_properties1.sizePolicy().hasHeightForWidth())
        self.frame_properties1.setSizePolicy(sizePolicy)
        self.frame_properties1.setFrameShape(QFrame.StyledPanel)
        self.frame_properties1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_properties1)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_view = QFrame(self.frame_properties1)
        self.frame_view.setObjectName(u"frame_view")
        self.frame_view.setStyleSheet(u"")
        self.frame_view.setFrameShape(QFrame.StyledPanel)
        self.frame_view.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_view)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setContentsMargins(15, 0, 15, 0)
        self.label_textProperties2_3 = QLabel(self.frame_view)
        self.label_textProperties2_3.setObjectName(u"label_textProperties2_3")
        self.label_textProperties2_3.setMinimumSize(QSize(80, 0))
        self.label_textProperties2_3.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_textProperties2_3)

        self.label_textPropertiesE = QLabel(self.frame_view)
        self.label_textPropertiesE.setObjectName(u"label_textPropertiesE")
        self.label_textPropertiesE.setMinimumSize(QSize(80, 0))
        self.label_textPropertiesE.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.label_textPropertiesE)

        self.label_textProperties3_2 = QLabel(self.frame_view)
        self.label_textProperties3_2.setObjectName(u"label_textProperties3_2")
        self.label_textProperties3_2.setMinimumSize(QSize(80, 0))
        self.label_textProperties3_2.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_textProperties3_2)

        self.label_textPropertiesV = QLabel(self.frame_view)
        self.label_textPropertiesV.setObjectName(u"label_textPropertiesV")
        self.label_textPropertiesV.setMinimumSize(QSize(80, 0))
        self.label_textPropertiesV.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_textPropertiesV)

        self.label_textProperties4_2 = QLabel(self.frame_view)
        self.label_textProperties4_2.setObjectName(u"label_textProperties4_2")
        self.label_textProperties4_2.setMinimumSize(QSize(80, 0))
        self.label_textProperties4_2.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_textProperties4_2)

        self.label_textPropertiesC = QLabel(self.frame_view)
        self.label_textPropertiesC.setObjectName(u"label_textPropertiesC")
        self.label_textPropertiesC.setMinimumSize(QSize(80, 0))
        self.label_textPropertiesC.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_textPropertiesC)

        self.label_textProperties5_2 = QLabel(self.frame_view)
        self.label_textProperties5_2.setObjectName(u"label_textProperties5_2")
        self.label_textProperties5_2.setMinimumSize(QSize(80, 0))
        self.label_textProperties5_2.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_textProperties5_2)

        self.label_textPropertiesPhi = QLabel(self.frame_view)
        self.label_textPropertiesPhi.setObjectName(u"label_textPropertiesPhi")
        self.label_textPropertiesPhi.setMinimumSize(QSize(80, 0))
        self.label_textPropertiesPhi.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_textPropertiesPhi)

        self.label_textProperties6_2 = QLabel(self.frame_view)
        self.label_textProperties6_2.setObjectName(u"label_textProperties6_2")
        self.label_textProperties6_2.setMinimumSize(QSize(80, 0))
        self.label_textProperties6_2.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_textProperties6_2)

        self.label_textPropertiesPsi = QLabel(self.frame_view)
        self.label_textPropertiesPsi.setObjectName(u"label_textPropertiesPsi")
        self.label_textPropertiesPsi.setMinimumSize(QSize(80, 0))
        self.label_textPropertiesPsi.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.label_textPropertiesPsi)


        self.verticalLayout_7.addWidget(self.frame_view)

        self.frame_edit = QFrame(self.frame_properties1)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setStyleSheet(u"")
        self.frame_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_edit)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setContentsMargins(15, 0, 15, 0)
        self.label_textProperties2_4 = QLabel(self.frame_edit)
        self.label_textProperties2_4.setObjectName(u"label_textProperties2_4")
        self.label_textProperties2_4.setMinimumSize(QSize(80, 0))
        self.label_textProperties2_4.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_textProperties2_4)

        self.doubleSpinBoxl_textPropertiesE = QDoubleSpinBox(self.frame_edit)
        self.doubleSpinBoxl_textPropertiesE.setObjectName(u"doubleSpinBoxl_textPropertiesE")
        self.doubleSpinBoxl_textPropertiesE.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesE.setMinimumSize(QSize(80, 25))
        self.doubleSpinBoxl_textPropertiesE.setDecimals(0)
        self.doubleSpinBoxl_textPropertiesE.setMinimum(1.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setMaximum(1000000.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesE.setValue(1000.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesE)

        self.label_textProperties3_3 = QLabel(self.frame_edit)
        self.label_textProperties3_3.setObjectName(u"label_textProperties3_3")
        self.label_textProperties3_3.setMinimumSize(QSize(80, 0))
        self.label_textProperties3_3.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_textProperties3_3)

        self.doubleSpinBoxl_textPropertiesV = QDoubleSpinBox(self.frame_edit)
        self.doubleSpinBoxl_textPropertiesV.setObjectName(u"doubleSpinBoxl_textPropertiesV")
        self.doubleSpinBoxl_textPropertiesV.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesV.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesV.setDecimals(2)
        self.doubleSpinBoxl_textPropertiesV.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesV.setMaximum(0.500000000000000)
        self.doubleSpinBoxl_textPropertiesV.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesV.setValue(0.300000000000000)
        self.doubleSpinBoxl_textPropertiesV.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesV)

        self.label_textProperties4_3 = QLabel(self.frame_edit)
        self.label_textProperties4_3.setObjectName(u"label_textProperties4_3")
        self.label_textProperties4_3.setMinimumSize(QSize(80, 0))
        self.label_textProperties4_3.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_textProperties4_3)

        self.doubleSpinBoxl_textPropertiesC = QDoubleSpinBox(self.frame_edit)
        self.doubleSpinBoxl_textPropertiesC.setObjectName(u"doubleSpinBoxl_textPropertiesC")
        self.doubleSpinBoxl_textPropertiesC.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesC.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesC.setDecimals(2)
        self.doubleSpinBoxl_textPropertiesC.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesC.setMaximum(10000.000000000000000)
        self.doubleSpinBoxl_textPropertiesC.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesC.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesC.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesC)

        self.label_textProperties5_3 = QLabel(self.frame_edit)
        self.label_textProperties5_3.setObjectName(u"label_textProperties5_3")
        self.label_textProperties5_3.setMinimumSize(QSize(80, 0))
        self.label_textProperties5_3.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_textProperties5_3)

        self.doubleSpinBoxl_textPropertiesPhi = QDoubleSpinBox(self.frame_edit)
        self.doubleSpinBoxl_textPropertiesPhi.setObjectName(u"doubleSpinBoxl_textPropertiesPhi")
        self.doubleSpinBoxl_textPropertiesPhi.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesPhi.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesPhi.setDecimals(1)
        self.doubleSpinBoxl_textPropertiesPhi.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setSingleStep(0.100000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesPhi)

        self.label_textProperties6_3 = QLabel(self.frame_edit)
        self.label_textProperties6_3.setObjectName(u"label_textProperties6_3")
        self.label_textProperties6_3.setMinimumSize(QSize(80, 0))
        self.label_textProperties6_3.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_textProperties6_3)

        self.doubleSpinBoxl_textPropertiesPsi = QDoubleSpinBox(self.frame_edit)
        self.doubleSpinBoxl_textPropertiesPsi.setObjectName(u"doubleSpinBoxl_textPropertiesPsi")
        self.doubleSpinBoxl_textPropertiesPsi.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesPsi.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesPsi.setDecimals(1)
        self.doubleSpinBoxl_textPropertiesPsi.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setSingleStep(0.100000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxl_textPropertiesPsi.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesPsi)


        self.verticalLayout_7.addWidget(self.frame_edit)


        self.verticalLayout.addWidget(self.frame_properties1)


        self.retranslateUi(FormDrawPropertyCard)

        QMetaObject.connectSlotsByName(FormDrawPropertyCard)
    # setupUi

    def retranslateUi(self, FormDrawPropertyCard):
        FormDrawPropertyCard.setWindowTitle(QCoreApplication.translate("FormDrawPropertyCard", u"Form", None))
        self.toolButton_PropertiesShow.setText("")
        self.label_cardPropertyName.setText(QCoreApplication.translate("FormDrawPropertyCard", u"Material. Point 1", None))
        self.lineEdit_PropertyName.setText("")
        self.toolButton_PropertyOk.setText("")
        self.toolButton_PropertyExit.setText("")
        self.toolButton_PropertyEdit.setText("")
        self.toolButton_PropertyClose.setText("")
#if QT_CONFIG(tooltip)
        self.label_textProperties2_3.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"M\u00f3dulo de espasticidad", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties2_3.setText(QCoreApplication.translate("FormDrawPropertyCard", u"E (KPa):", None))
#if QT_CONFIG(tooltip)
        self.label_textPropertiesE.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"M\u00f3dulo de espasticidad", None))
#endif // QT_CONFIG(tooltip)
        self.label_textPropertiesE.setText(QCoreApplication.translate("FormDrawPropertyCard", u"E (KPa):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties3_2.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Coeficiente de poisson", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties3_2.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03bd :", None))
#if QT_CONFIG(tooltip)
        self.label_textPropertiesV.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Coeficiente de poisson", None))
#endif // QT_CONFIG(tooltip)
        self.label_textPropertiesV.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03bd :", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties4_2.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Cohesi\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties4_2.setText(QCoreApplication.translate("FormDrawPropertyCard", u"C' (KPa):", None))
#if QT_CONFIG(tooltip)
        self.label_textPropertiesC.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Cohesi\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textPropertiesC.setText(QCoreApplication.translate("FormDrawPropertyCard", u"C' (KPa):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties5_2.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de fricci\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties5_2.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03d5 (\u00b0):", None))
#if QT_CONFIG(tooltip)
        self.label_textPropertiesPhi.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de fricci\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textPropertiesPhi.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03d5 (\u00b0):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties6_2.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de dilatancia ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties6_2.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03c8 (\u00b0):", None))
#if QT_CONFIG(tooltip)
        self.label_textPropertiesPsi.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de dilatancia ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textPropertiesPsi.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03c8 (\u00b0):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties2_4.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"M\u00f3dulo de espasticidad", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties2_4.setText(QCoreApplication.translate("FormDrawPropertyCard", u"E (KPa):", None))
        self.doubleSpinBoxl_textPropertiesE.setSuffix(QCoreApplication.translate("FormDrawPropertyCard", u" KPa", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties3_3.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Coeficiente de poisson", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties3_3.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03bd :", None))
        self.doubleSpinBoxl_textPropertiesV.setSuffix("")
#if QT_CONFIG(tooltip)
        self.label_textProperties4_3.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"Cohesi\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties4_3.setText(QCoreApplication.translate("FormDrawPropertyCard", u"C' (KPa):", None))
        self.doubleSpinBoxl_textPropertiesC.setSuffix(QCoreApplication.translate("FormDrawPropertyCard", u" KPa", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties5_3.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de fricci\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties5_3.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03d5 (\u00b0):", None))
        self.doubleSpinBoxl_textPropertiesPhi.setSuffix(QCoreApplication.translate("FormDrawPropertyCard", u" \u00b0", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties6_3.setToolTip(QCoreApplication.translate("FormDrawPropertyCard", u"\u00c1ngulo  de dilatancia ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties6_3.setText(QCoreApplication.translate("FormDrawPropertyCard", u"\u03c8 (\u00b0):", None))
        self.doubleSpinBoxl_textPropertiesPsi.setSuffix(QCoreApplication.translate("FormDrawPropertyCard", u" \u00b0", None))
    # retranslateUi

