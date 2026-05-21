# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_pointMaterialslPkUO.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormDrawMenuPointMaterial(object):
    def setupUi(self, FormDrawMenuPointMaterial):
        if not FormDrawMenuPointMaterial.objectName():
            FormDrawMenuPointMaterial.setObjectName(u"FormDrawMenuPointMaterial")
        FormDrawMenuPointMaterial.resize(350, 802)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuPointMaterial.sizePolicy().hasHeightForWidth())
        FormDrawMenuPointMaterial.setSizePolicy(sizePolicy)
        FormDrawMenuPointMaterial.setMinimumSize(QSize(0, 0))
        FormDrawMenuPointMaterial.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuPointMaterial.setStyleSheet(u"/*Colores primarios*/\n"
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
"\n"
"\n"
"QFrame#frame_pointMaterialProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"QFrame#frame_info"
                        ",\n"
"QFrame#frame_pointMaterial,\n"
"QFrame#frame_materialPoint2,\n"
"QFrame#frame_materialPoint3,\n"
"QFrame#frame_materialPoint4,\n"
"QFrame#frame_3,\n"
"QFrame#frame_8,\n"
"QFrame#frame_9,\n"
"QFrame#frame,\n"
"QFrame#frame_4{\n"
"background: transparent;\n"
"}\n"
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
"/*####################       FRAME MESH       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_mesh"
                        "{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*###########################################################################*/\n"
"/*################      FRAME MALLA REGULAR CUADRIL\u00c1TERO       ######################*/\n"
"/*###########################################################################*/\n"
"\n"
"/*\n"
"QToolButton#toolButton_cardMeshDraw1,\n"
"QToolButton#toolButton_cardMeshDraw2,\n"
"QToolButton#toolButton_cardMeshDraw3,\n"
"QToolButton#toolButton_cardMeshDraw8,\n"
"QToolButton#toolButton_cardMeshDraw9,\n"
"QToolButton#toolButton_cardMeshDraw10,\n"
"QToolButton#toolButton_cardMeshDraw11{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px ;\n"
"}\n"
"QToolButton#toolButton_cardMeshDraw1:hover,\n"
"QToolButton#toolButton_cardMeshDraw2:hover, \n"
"QToolButton#toolButton_cardMeshDraw3:hover, \n"
"QToolButton#toolButton_cardMeshDraw8:hover, \n"
"QToolButton#too"
                        "lButton_cardMeshDraw9:hover, \n"
"QToolButton#toolButton_cardMeshDraw10:hover, \n"
"QToolButton#toolButton_cardMeshDraw11:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardMeshDraw1:pressed,\n"
"QToolButton#toolButton_cardMeshDraw2:pressed,\n"
"QToolButton#toolButton_cardMeshDraw3:pressed,\n"
"QToolButton#toolButton_cardMeshDraw8:pressed,\n"
"QToolButton#toolButton_cardMeshDraw9:pressed,\n"
"QToolButton#toolButton_cardMeshDraw10:pressed,\n"
"QToolButton#toolButton_cardMeshDraw11:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*###########################################################*/\n"
"/*###############          FRAME LISTA MALLAS         ##################*/\n"
"/*###########################################################*/\n"
"\n"
"QScrollArea#scrollArea,\n"
"#verticalLayout_containerCardMesh,\n"
"#scrollAreaWidgetContents{\n"
"background-color: transparent;\n"
"}\n"
"\n"
""
                        "\n"
"/*###########################################################*/\n"
"/*################                 FRAME MSN          #####################*/\n"
"/*###########################################################*/\n"
"\n"
"\n"
"QLabel#label_msn{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*######################      SCROLL BAR    VERTICAL  ############################*/\n"
"\n"
"QScrollBar:vertical {    \n"
"	border: none;\n"
"    width: 14px;\n"
"	border-radius: 0px;\n"
"	margin: 15px 0px 15px 0px;\n"
"}\n"
"\n"
"\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #888888;\n"
"    min-height: 14px;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollBar::handle:vertical:hover {\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"/*TOP*/\n"
"QScrollBar::sub-line:vertical{\n"
"    background-color: #666666;\n"
"	border: none;\n"
"	border-top-left-radius: 7px;\n"
"	border-top-right-rad"
                        "ius: 7px;\n"
"	height: 15px;\n"
"	subcontrol-position: top;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:vertical:hover{\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::sub-line:vertical:pressed{\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"/*BOTTON*/\n"
"QScrollBar::add-line:vertical{\n"
"    background-color: #444444;\n"
"	border: none;	\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"	height: 15px;\n"
"	subcontrol-position: bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical:hover{\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::add-line:vertical:pressed{\n"
"   background-color: #666666;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical,QScrollBar::down-arrow:vertical{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"/*######################      SCROLL BAR    HORIZONTAL  ############################*/\n"
""
                        "\n"
"QScrollBar:horizontal{\n"
"height: 14px;\n"
"border: none;\n"
"border-radius: 0px;\n"
"margin: 0px 15px 0px 15px;\n"
"}\n"
"\n"
"\n"
"/*Deslizador*/\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: #888888;\n"
"	border-radius: 7px;\n"
"	min-width: 14px;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #666666;\n"
"}\n"
"  \n"
"QScrollBar::sub-line:horizontal{\n"
"background-color: #666666;\n"
"border: none;\n"
"border-top-left-radius: 7px;\n"
"border-bottom-left-radius: 7px;\n"
"width: 15px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal:hover{\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::sub-line:horizontal:pressed{\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    background-color: #666666;\n"
"	border: none;	\n"
"	border-top-right-radius: 7px;\n"
"	border-bottom-r"
                        "ight-radius: 7px;\n"
"	width: 15px;\n"
"	subcontrol-position: right;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal:hover{\n"
"    background-color: #777777;\n"
"}QScrollBar::add-line:vertical:pressed{\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:horizontal{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"QToolButton[QToolButtonStyle=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"1\"]:hover{ \n"
"background"
                        "-color: #444444;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"1\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"/*******************************************/\n"
"QToolButton[QToolButtonStyle=\"2\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 8px ;\n"
"}\n"
"QToolButton[QToolButtonStyle=\"2\"]:hover{\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"/*****************************************/\n"
"QToolButton[QToolButtonStyle=\"3\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #910D3F;\n"
"border: none;\n"
"padding: 6px 5px;\n"
"border-radius: 8px ;\n"
"}\n"
"QToolButton[QToolButtonStyle=\"3\"]:hover{\n"
"background-color: #C70039;\n"
"}\n"
"\n"
"\n"
"QToolButton[QToolButtonStyle=\"4\"]{\n"
"\n"
"background-color: #77ACA2;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"QToolButton[QTo"
                        "olButtonStyle=\"4\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"4\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"\n"
"\n"
"/* \n"
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"/*******************************************/\n"
"QToolButton[QToolButtonStyle=\"5\"],\n"
"QToolButton[QToolButtonStyle=\"6\"],\n"
"QToolButton[QToolButtonStyle=\"7\"],\n"
"QToolButton[QToolButtonStyle=\"8\"] {\n"
"    font: 500 10pt \"Ubuntu\";    \n"
"    padding: 4px 20px;\n"
"	border: 2px solid #C8CC8E;\n"
"    \n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"5\"] {\n"
"    background-color: transparent;    \n"
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-bottom-left-radius: 10px;\n"
"	color: #DDDDDD;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"6\"] {\n"
"    background-color: #C8CC8E;\n"
"	border-"
                        "top-left-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-bottom-left-radius: 10px;\n"
"	color: #222222;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"7\"] {\n"
"    background-color: transparent;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	color: #DDDDDD;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"8\"] {\n"
"    background-color: #C8CC8E;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 10px;\n"
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	color: #222222;\n"
"}\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit[QLineEditStyle=\"1\""
                        "]{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"2\"]{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #333333;\n"
"border: 1px solid #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit#lineEdit_textMesh3{\n"
"font: 7pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #333333;\n"
"border: 1px solid #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 2px;\n"
"padding-left: 2px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*\n"
"QLineEdit#lineEdit_textMesh3,\n"
"QLineEdit#lineEdit_textMesh5{\n"
"color: #888888;\n"
"}\n"
"*/\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFrame          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8*/\n"
"\n"
"QFrame[QFrameSubTitleStyle=\"1\"] {\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QToolButton[QToolButtonSubTitleStyle=\"1\"] {\n"
"background-color: transparent;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QLabel[QLabel"
                        "Style=\"3\"] {\n"
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
"    selection-background-color: #808080;\n"
"    font: 700 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"    QSlider[QSliderStyle=\"1\"] {\n"
"        background-color: transparent;\n"
"		margin: 2px 5px ;\n"
"    }\n"
"\n"
"    QSlider[QSliderStyle=\"1\"]::groove:horizontal {\n"
"        border: none;\n"
"        background-color: #444444;\n"
"        height: 18px;\n"
"		border-radius: 9px;\n"
"    }\n"
"\n"
"\n"
"    QSlider[QSliderStyle=\"1\"]::handle:horizontal {\n"
"        background-color: #fd5959;\n"
"        border: none;\n"
"        width: 18px;\n"
"        height: 18px;        \n"
"        border-radius: 9px;\n"
"    }\n"
"\n"
"QSlider[QSliderStyle=\"1\"]::handle:horizontal:hover {\n"
"    background-color: #fecdcd;\n"
"    /*box-shadow: 0 0 3px rgba(255, 0, 0, 0.5); */\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuPointMaterial)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_pointMaterialProject = QFrame(FormDrawMenuPointMaterial)
        self.frame_pointMaterialProject.setObjectName(u"frame_pointMaterialProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pointMaterialProject.sizePolicy().hasHeightForWidth())
        self.frame_pointMaterialProject.setSizePolicy(sizePolicy1)
        self.frame_pointMaterialProject.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pointMaterialProject.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_pointMaterialProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_pointMaterialProject)
        self.frame_hide.setObjectName(u"frame_hide")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_hide.sizePolicy().hasHeightForWidth())
        self.frame_hide.setSizePolicy(sizePolicy2)
        self.frame_hide.setMinimumSize(QSize(20, 0))
        self.frame_hide.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_hide.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_hide)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_hide2 = QFrame(self.frame_hide)
        self.frame_hide2.setObjectName(u"frame_hide2")
        sizePolicy2.setHeightForWidth(self.frame_hide2.sizePolicy().hasHeightForWidth())
        self.frame_hide2.setSizePolicy(sizePolicy2)
        self.frame_hide2.setMinimumSize(QSize(20, 0))
        self.frame_hide2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_hide2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_hide2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_hideShow = QToolButton(self.frame_hide2)
        self.toolButton_hideShow.setObjectName(u"toolButton_hideShow")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Maximum)
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
        icon.addFile(u"app/resources/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_hideShow.setIcon(icon)
        self.toolButton_hideShow.setIconSize(QSize(15, 15))
        self.toolButton_hideShow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hideShow)


        self.verticalLayout_2.addWidget(self.frame_hide2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_pointMaterial = QFrame(self.frame_pointMaterialProject)
        self.frame_pointMaterial.setObjectName(u"frame_pointMaterial")
        sizePolicy1.setHeightForWidth(self.frame_pointMaterial.sizePolicy().hasHeightForWidth())
        self.frame_pointMaterial.setSizePolicy(sizePolicy1)
        self.frame_pointMaterial.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_pointMaterial.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_pointMaterial)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_pointMaterial)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy4)
        self.frame_title.setMinimumSize(QSize(0, 30))
        self.frame_title.setMaximumSize(QSize(16777215, 30))
        self.frame_title.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_title.setLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_cardPointMaterialTitle = QLabel(self.frame_title)
        self.label_cardPointMaterialTitle.setObjectName(u"label_cardPointMaterialTitle")
        self.label_cardPointMaterialTitle.setProperty(u"QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardPointMaterialTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_pointMaterial)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_PointMaterialSubTitle1 = QFrame(self.frame_info)
        self.frame_PointMaterialSubTitle1.setObjectName(u"frame_PointMaterialSubTitle1")
        self.frame_PointMaterialSubTitle1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_PointMaterialSubTitle1.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_PointMaterialSubTitle1.setProperty(u"QFrameSubTitleStyle", 1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_PointMaterialSubTitle1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardPointMaterialSubTitle1 = QLabel(self.frame_PointMaterialSubTitle1)
        self.label_cardPointMaterialSubTitle1.setObjectName(u"label_cardPointMaterialSubTitle1")
        self.label_cardPointMaterialSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardPointMaterialSubTitle1.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardPointMaterialSubTitle1)

        self.toolButton_cardPointMaterialSubTitle1 = QToolButton(self.frame_PointMaterialSubTitle1)
        self.toolButton_cardPointMaterialSubTitle1.setObjectName(u"toolButton_cardPointMaterialSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_cardPointMaterialSubTitle1.setIcon(icon1)
        self.toolButton_cardPointMaterialSubTitle1.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardPointMaterialSubTitle1.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardPointMaterialSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_PointMaterialSubTitle1)

        self.frame_materialPoint2 = QFrame(self.frame_info)
        self.frame_materialPoint2.setObjectName(u"frame_materialPoint2")
        sizePolicy1.setHeightForWidth(self.frame_materialPoint2.sizePolicy().hasHeightForWidth())
        self.frame_materialPoint2.setSizePolicy(sizePolicy1)
        self.frame_materialPoint2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_materialPoint2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_materialPoint2)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_materialPoint2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_textPointMaterialName = QLabel(self.frame_3)
        self.label_textPointMaterialName.setObjectName(u"label_textPointMaterialName")
        self.label_textPointMaterialName.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialName.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_textPointMaterialName)

        self.lineEdit_textPointMaterialName = QLineEdit(self.frame_3)
        self.lineEdit_textPointMaterialName.setObjectName(u"lineEdit_textPointMaterialName")
        self.lineEdit_textPointMaterialName.setMinimumSize(QSize(150, 25))
        self.lineEdit_textPointMaterialName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textPointMaterialName.setProperty(u"QLineEditStyle", 1)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_textPointMaterialName)

        self.label_textPointMaterialBaseMesh = QLabel(self.frame_3)
        self.label_textPointMaterialBaseMesh.setObjectName(u"label_textPointMaterialBaseMesh")
        self.label_textPointMaterialBaseMesh.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialBaseMesh.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_textPointMaterialBaseMesh)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox_PointMaterialBaseMesh = QComboBox(self.frame_3)
        self.comboBox_PointMaterialBaseMesh.setObjectName(u"comboBox_PointMaterialBaseMesh")
        self.comboBox_PointMaterialBaseMesh.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialBaseMesh.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.comboBox_PointMaterialBaseMesh.setProperty(u"QComboBoxStyle", 1)

        self.horizontalLayout_11.addWidget(self.comboBox_PointMaterialBaseMesh)


        self.formLayout_3.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_11)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.toolButton_PointMaterialUploadFile = QToolButton(self.frame)
        self.toolButton_PointMaterialUploadFile.setObjectName(u"toolButton_PointMaterialUploadFile")
        sizePolicy4.setHeightForWidth(self.toolButton_PointMaterialUploadFile.sizePolicy().hasHeightForWidth())
        self.toolButton_PointMaterialUploadFile.setSizePolicy(sizePolicy4)
        icon2 = QIcon()
        icon2.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/cloud_computing.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_PointMaterialUploadFile.setIcon(icon2)
        self.toolButton_PointMaterialUploadFile.setIconSize(QSize(20, 20))
        self.toolButton_PointMaterialUploadFile.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_PointMaterialUploadFile.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_PointMaterialUploadFile.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_10.addWidget(self.toolButton_PointMaterialUploadFile)


        self.formLayout_3.setWidget(5, QFormLayout.ItemRole.FieldRole, self.frame)

        self.label_textPointMaterialProperty = QLabel(self.frame_3)
        self.label_textPointMaterialProperty.setObjectName(u"label_textPointMaterialProperty")
        self.label_textPointMaterialProperty.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialProperty.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_textPointMaterialProperty)

        self.label_textPointMaterialNPoints = QLabel(self.frame_3)
        self.label_textPointMaterialNPoints.setObjectName(u"label_textPointMaterialNPoints")
        self.label_textPointMaterialNPoints.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialNPoints.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_textPointMaterialNPoints)

        self.comboBox_PointMaterialProperty = QComboBox(self.frame_3)
        self.comboBox_PointMaterialProperty.setObjectName(u"comboBox_PointMaterialProperty")
        self.comboBox_PointMaterialProperty.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialProperty.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.comboBox_PointMaterialProperty.setProperty(u"QComboBoxStyle", 1)

        self.formLayout_3.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox_PointMaterialProperty)

        self.comboBox_PointMaterialNPoints = QComboBox(self.frame_3)
        self.comboBox_PointMaterialNPoints.setObjectName(u"comboBox_PointMaterialNPoints")
        self.comboBox_PointMaterialNPoints.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialNPoints.setProperty(u"QComboBoxStyle", 1)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboBox_PointMaterialNPoints)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.label_textPointMaterial_path = QLabel(self.frame_materialPoint2)
        self.label_textPointMaterial_path.setObjectName(u"label_textPointMaterial_path")
        self.label_textPointMaterial_path.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterial_path.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label_textPointMaterial_path.setProperty(u"QLabelStyle", 3)

        self.verticalLayout_6.addWidget(self.label_textPointMaterial_path)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.toolButton_PointMaterialCancel = QToolButton(self.frame_materialPoint2)
        self.toolButton_PointMaterialCancel.setObjectName(u"toolButton_PointMaterialCancel")
        self.toolButton_PointMaterialCancel.setMinimumSize(QSize(80, 0))
        self.toolButton_PointMaterialCancel.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterialCancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_PointMaterialCancel.setProperty(u"QToolButtonStyle", 3)

        self.horizontalLayout_12.addWidget(self.toolButton_PointMaterialCancel)

        self.toolButton_PointMaterial = QToolButton(self.frame_materialPoint2)
        self.toolButton_PointMaterial.setObjectName(u"toolButton_PointMaterial")
        self.toolButton_PointMaterial.setMinimumSize(QSize(150, 0))
        self.toolButton_PointMaterial.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterial.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.toolButton_PointMaterial.setProperty(u"QToolButtonStyle", 2)

        self.horizontalLayout_12.addWidget(self.toolButton_PointMaterial)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addWidget(self.frame_materialPoint2)

        self.frame_PointMaterialSubTitle3 = QFrame(self.frame_info)
        self.frame_PointMaterialSubTitle3.setObjectName(u"frame_PointMaterialSubTitle3")
        self.frame_PointMaterialSubTitle3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_PointMaterialSubTitle3.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_PointMaterialSubTitle3.setProperty(u"QFrameSubTitleStyle", 1)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_PointMaterialSubTitle3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_cardPointMaterialSubTitle3 = QLabel(self.frame_PointMaterialSubTitle3)
        self.label_cardPointMaterialSubTitle3.setObjectName(u"label_cardPointMaterialSubTitle3")
        self.label_cardPointMaterialSubTitle3.setMinimumSize(QSize(262, 0))
        self.label_cardPointMaterialSubTitle3.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_4.addWidget(self.label_cardPointMaterialSubTitle3)

        self.toolButton_showHideLabelVector = QToolButton(self.frame_PointMaterialSubTitle3)
        self.toolButton_showHideLabelVector.setObjectName(u"toolButton_showHideLabelVector")
        icon3 = QIcon()
        icon3.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_showHideLabelVector.setIcon(icon3)
        self.toolButton_showHideLabelVector.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_showHideLabelVector.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_4.addWidget(self.toolButton_showHideLabelVector)

        self.toolButton_cardPointMaterialSubTitle3 = QToolButton(self.frame_PointMaterialSubTitle3)
        self.toolButton_cardPointMaterialSubTitle3.setObjectName(u"toolButton_cardPointMaterialSubTitle3")
        self.toolButton_cardPointMaterialSubTitle3.setIcon(icon1)
        self.toolButton_cardPointMaterialSubTitle3.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardPointMaterialSubTitle3.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_4.addWidget(self.toolButton_cardPointMaterialSubTitle3)


        self.verticalLayout_5.addWidget(self.frame_PointMaterialSubTitle3)

        self.frame_materialPoint4 = QFrame(self.frame_info)
        self.frame_materialPoint4.setObjectName(u"frame_materialPoint4")
        sizePolicy1.setHeightForWidth(self.frame_materialPoint4.sizePolicy().hasHeightForWidth())
        self.frame_materialPoint4.setSizePolicy(sizePolicy1)
        self.frame_materialPoint4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_materialPoint4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_materialPoint4)
        self.verticalLayout_7.setSpacing(15)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_materialPoint4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textPM4 = QLabel(self.frame_4)
        self.label_textPM4.setObjectName(u"label_textPM4")
        self.label_textPM4.setMinimumSize(QSize(110, 0))
        self.label_textPM4.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_textPM4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_textMPSelected = QLineEdit(self.frame_4)
        self.lineEdit_textMPSelected.setObjectName(u"lineEdit_textMPSelected")
        self.lineEdit_textMPSelected.setEnabled(False)
        self.lineEdit_textMPSelected.setMinimumSize(QSize(120, 25))
        self.lineEdit_textMPSelected.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textMPSelected.setProperty(u"QLineEditStyle", 2)

        self.horizontalLayout_15.addWidget(self.lineEdit_textMPSelected)

        self.toolButton_btnMPDrawSelected = QToolButton(self.frame_4)
        self.toolButton_btnMPDrawSelected.setObjectName(u"toolButton_btnMPDrawSelected")
        icon4 = QIcon()
        icon4.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/select.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_btnMPDrawSelected.setIcon(icon4)
        self.toolButton_btnMPDrawSelected.setIconSize(QSize(20, 20))
        self.toolButton_btnMPDrawSelected.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_btnMPDrawSelected.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_15.addWidget(self.toolButton_btnMPDrawSelected)


        self.formLayout_4.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_15)

        self.label_textPM3 = QLabel(self.frame_4)
        self.label_textPM3.setObjectName(u"label_textPM3")
        self.label_textPM3.setMinimumSize(QSize(90, 0))
        self.label_textPM3.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_textPM3)

        self.frame_8 = QFrame(self.frame_4)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setSpacing(3)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_textPM_Velx = QLabel(self.frame_8)
        self.label_textPM_Velx.setObjectName(u"label_textPM_Velx")
        self.label_textPM_Velx.setMinimumSize(QSize(0, 0))
        self.label_textPM_Velx.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_22.addWidget(self.label_textPM_Velx)

        self.lineEdit_textPM_Velx = QLineEdit(self.frame_8)
        self.lineEdit_textPM_Velx.setObjectName(u"lineEdit_textPM_Velx")
        self.lineEdit_textPM_Velx.setMinimumSize(QSize(50, 25))
        self.lineEdit_textPM_Velx.setProperty(u"QLineEditStyle", 1)

        self.horizontalLayout_22.addWidget(self.lineEdit_textPM_Velx)

        self.label_textPM_Vely = QLabel(self.frame_8)
        self.label_textPM_Vely.setObjectName(u"label_textPM_Vely")
        self.label_textPM_Vely.setMinimumSize(QSize(0, 0))
        self.label_textPM_Vely.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_22.addWidget(self.label_textPM_Vely)

        self.lineEdit_textPM_Vely = QLineEdit(self.frame_8)
        self.lineEdit_textPM_Vely.setObjectName(u"lineEdit_textPM_Vely")
        self.lineEdit_textPM_Vely.setMinimumSize(QSize(50, 25))
        self.lineEdit_textPM_Vely.setProperty(u"QLineEditStyle", 1)

        self.horizontalLayout_22.addWidget(self.lineEdit_textPM_Vely)


        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.frame_8)

        self.label_textPM2 = QLabel(self.frame_4)
        self.label_textPM2.setObjectName(u"label_textPM2")
        self.label_textPM2.setMinimumSize(QSize(65, 0))
        self.label_textPM2.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_textPM2)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_23.setSpacing(3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_textPM_Felx = QLabel(self.frame_9)
        self.label_textPM_Felx.setObjectName(u"label_textPM_Felx")
        self.label_textPM_Felx.setMinimumSize(QSize(0, 0))
        self.label_textPM_Felx.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_23.addWidget(self.label_textPM_Felx)

        self.lineEdit_textPM_Felx = QLineEdit(self.frame_9)
        self.lineEdit_textPM_Felx.setObjectName(u"lineEdit_textPM_Felx")
        self.lineEdit_textPM_Felx.setMinimumSize(QSize(50, 25))
        self.lineEdit_textPM_Felx.setProperty(u"QLineEditStyle", 1)

        self.horizontalLayout_23.addWidget(self.lineEdit_textPM_Felx)

        self.label_textPM_Pely = QLabel(self.frame_9)
        self.label_textPM_Pely.setObjectName(u"label_textPM_Pely")
        self.label_textPM_Pely.setMinimumSize(QSize(0, 0))
        self.label_textPM_Pely.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_23.addWidget(self.label_textPM_Pely)

        self.lineEdit_textPM_Fely = QLineEdit(self.frame_9)
        self.lineEdit_textPM_Fely.setObjectName(u"lineEdit_textPM_Fely")
        self.lineEdit_textPM_Fely.setMinimumSize(QSize(50, 25))
        self.lineEdit_textPM_Fely.setProperty(u"QLineEditStyle", 1)

        self.horizontalLayout_23.addWidget(self.lineEdit_textPM_Fely)


        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_5)

        self.toolButton_PointMaterialCancel_2 = QToolButton(self.frame_materialPoint4)
        self.toolButton_PointMaterialCancel_2.setObjectName(u"toolButton_PointMaterialCancel_2")
        self.toolButton_PointMaterialCancel_2.setMinimumSize(QSize(80, 0))
        self.toolButton_PointMaterialCancel_2.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterialCancel_2.setProperty(u"QToolButtonStyle", 3)

        self.horizontalLayout_16.addWidget(self.toolButton_PointMaterialCancel_2)

        self.toolButton_PointMaterialAssing = QToolButton(self.frame_materialPoint4)
        self.toolButton_PointMaterialAssing.setObjectName(u"toolButton_PointMaterialAssing")
        self.toolButton_PointMaterialAssing.setMinimumSize(QSize(150, 0))
        self.toolButton_PointMaterialAssing.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterialAssing.setProperty(u"QToolButtonStyle", 2)

        self.horizontalLayout_16.addWidget(self.toolButton_PointMaterialAssing)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_16)


        self.verticalLayout_5.addWidget(self.frame_materialPoint4)

        self.frame_PointMaterialSubTitle2 = QFrame(self.frame_info)
        self.frame_PointMaterialSubTitle2.setObjectName(u"frame_PointMaterialSubTitle2")
        self.frame_PointMaterialSubTitle2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_PointMaterialSubTitle2.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_PointMaterialSubTitle2.setProperty(u"QFrameSubTitleStyle", 1)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_PointMaterialSubTitle2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardPointMaterialSubTitle2 = QLabel(self.frame_PointMaterialSubTitle2)
        self.label_cardPointMaterialSubTitle2.setObjectName(u"label_cardPointMaterialSubTitle2")
        self.label_cardPointMaterialSubTitle2.setMinimumSize(QSize(100, 0))
        self.label_cardPointMaterialSubTitle2.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_7.addWidget(self.label_cardPointMaterialSubTitle2)

        self.horizontalSlider_PointMaterialSize = QSlider(self.frame_PointMaterialSubTitle2)
        self.horizontalSlider_PointMaterialSize.setObjectName(u"horizontalSlider_PointMaterialSize")
        self.horizontalSlider_PointMaterialSize.setMinimumSize(QSize(30, 0))
        self.horizontalSlider_PointMaterialSize.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.horizontalSlider_PointMaterialSize.setMinimum(1)
        self.horizontalSlider_PointMaterialSize.setMaximum(299)
        self.horizontalSlider_PointMaterialSize.setSingleStep(10)
        self.horizontalSlider_PointMaterialSize.setValue(100)
        self.horizontalSlider_PointMaterialSize.setTracking(False)
        self.horizontalSlider_PointMaterialSize.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider_PointMaterialSize.setInvertedAppearance(True)
        self.horizontalSlider_PointMaterialSize.setInvertedControls(True)
        self.horizontalSlider_PointMaterialSize.setTickPosition(QSlider.TickPosition.NoTicks)
        self.horizontalSlider_PointMaterialSize.setTickInterval(0)
        self.horizontalSlider_PointMaterialSize.setProperty(u"QSliderStyle", 1)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_PointMaterialSize)

        self.toolButton_showHideLabel = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_showHideLabel.setObjectName(u"toolButton_showHideLabel")
        self.toolButton_showHideLabel.setIcon(icon3)
        self.toolButton_showHideLabel.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_showHideLabel.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideLabel)

        self.toolButton_showHidePointMaterial = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_showHidePointMaterial.setObjectName(u"toolButton_showHidePointMaterial")
        icon5 = QIcon()
        icon5.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_showHidePointMaterial.setIcon(icon5)
        self.toolButton_showHidePointMaterial.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_showHidePointMaterial.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHidePointMaterial)

        self.toolButton_cardPointMaterialSubTitle2 = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_cardPointMaterialSubTitle2.setObjectName(u"toolButton_cardPointMaterialSubTitle2")
        self.toolButton_cardPointMaterialSubTitle2.setIcon(icon1)
        self.toolButton_cardPointMaterialSubTitle2.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardPointMaterialSubTitle2.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_cardPointMaterialSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_PointMaterialSubTitle2)

        self.frame_materialPoint3 = QFrame(self.frame_info)
        self.frame_materialPoint3.setObjectName(u"frame_materialPoint3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_materialPoint3.sizePolicy().hasHeightForWidth())
        self.frame_materialPoint3.setSizePolicy(sizePolicy5)
        self.frame_materialPoint3.setMinimumSize(QSize(0, 150))
        self.frame_materialPoint3.setStyleSheet(u"")
        self.frame_materialPoint3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_materialPoint3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_materialPoint3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_materialPoint3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 272, 128))
        self.horizontalLayout_14 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_containerCardMaterialPoint = QVBoxLayout()
        self.verticalLayout_containerCardMaterialPoint.setSpacing(0)
        self.verticalLayout_containerCardMaterialPoint.setObjectName(u"verticalLayout_containerCardMaterialPoint")
        self.frame_empty = QFrame(self.scrollAreaWidgetContents)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy5.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy5)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout_containerCardMaterialPoint.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardMaterialPoint)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_materialPoint3)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msn = QLabel(self.frame_info)
        self.label_msn.setObjectName(u"label_msn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_msn.sizePolicy().hasHeightForWidth())
        self.label_msn.setSizePolicy(sizePolicy6)
        self.label_msn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_msn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_pointMaterial)


        self.horizontalLayout_6.addWidget(self.frame_pointMaterialProject)


        self.retranslateUi(FormDrawMenuPointMaterial)

        QMetaObject.connectSlotsByName(FormDrawMenuPointMaterial)
    # setupUi

    def retranslateUi(self, FormDrawMenuPointMaterial):
        FormDrawMenuPointMaterial.setWindowTitle(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardPointMaterialTitle.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"PUNTO MATERIAL", None))
        self.label_cardPointMaterialSubTitle1.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Crear Puntos Material", None))
        self.toolButton_cardPointMaterialSubTitle1.setText("")
        self.label_textPointMaterialName.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Nombre:", None))
        self.lineEdit_textPointMaterialName.setText("")
        self.label_textPointMaterialBaseMesh.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Malla Base:", None))
        self.toolButton_PointMaterialUploadFile.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"   Subir Archivo", None))
        self.label_textPointMaterialProperty.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Material:", None))
        self.label_textPointMaterialNPoints.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Puntos x elemento:", None))
        self.label_textPointMaterial_path.setText("")
        self.toolButton_PointMaterialCancel.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Cancelar", None))
        self.toolButton_PointMaterial.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Crear Puntos", None))
        self.label_cardPointMaterialSubTitle3.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Asignar fuerzas y velocidades", None))
        self.toolButton_showHideLabelVector.setText("")
        self.toolButton_cardPointMaterialSubTitle3.setText("")
        self.label_textPM4.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Seleccionar:", None))
        self.lineEdit_textMPSelected.setText("")
        self.toolButton_btnMPDrawSelected.setText("")
        self.label_textPM3.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Velocidad [m/s]:", None))
        self.label_textPM_Velx.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"<html><head/><body><p>Vox </p></body></html>", None))
        self.lineEdit_textPM_Velx.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"0.0", None))
        self.label_textPM_Vely.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"<html><head/><body><p> Voy </p></body></html>", None))
        self.lineEdit_textPM_Vely.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"0.0", None))
        self.label_textPM2.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Fuerza [kN]:", None))
        self.label_textPM_Felx.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"<html><head/><body><p>Fox </p></body></html>", None))
        self.lineEdit_textPM_Felx.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"0.0", None))
        self.label_textPM_Pely.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"<html><head/><body><p>Foy </p></body></html>", None))
        self.lineEdit_textPM_Fely.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"0.0", None))
        self.toolButton_PointMaterialCancel_2.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Cancelar", None))
        self.toolButton_PointMaterialAssing.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Asignar", None))
        self.label_cardPointMaterialSubTitle2.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Lista de puntos", None))
        self.toolButton_showHideLabel.setText("")
        self.toolButton_showHidePointMaterial.setText("")
        self.toolButton_cardPointMaterialSubTitle2.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Empty", None))
    # retranslateUi

