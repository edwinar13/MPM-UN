# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_pointMaterialpbLbgJ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QSlider, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormDrawMenuPointMaterial(object):
    def setupUi(self, FormDrawMenuPointMaterial):
        if not FormDrawMenuPointMaterial.objectName():
            FormDrawMenuPointMaterial.setObjectName(u"FormDrawMenuPointMaterial")
        FormDrawMenuPointMaterial.resize(350, 644)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
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
"/*###############"
                        "##################################################*/\n"
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
"QFrame#frame_mesh{\n"
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
"/*################      FRAME MALLA REGULAR CUADRIL\u00c1TERO  "
                        "     ######################*/\n"
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
"QToolButton#toolButton_cardMeshDraw9:hover, \n"
"QToolButton#toolButton_cardMeshDraw10:hover, \n"
"QToolButton#toolButton_cardMeshDraw11:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardMeshDraw1:pressed,\n"
"QToolButton#toolButton_cardMeshDraw2:pressed,\n"
"QToolButton#toolButto"
                        "n_cardMeshDraw3:pressed,\n"
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
"\n"
"/*###########################################################*/\n"
"/*################                 FRAME MSN          #####################*/\n"
"/*###########################################################*/\n"
"\n"
"\n"
"QLabel#label_msn{\n"
"font: 500 10pt \"Ubuntu\";\n"
"col"
                        "or: #333333;\n"
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
"	border-top-right-radius: 7px;\n"
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
"/*BOTT"
                        "ON*/\n"
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
"QScr"
                        "ollBar::handle:horizontal:hover {\n"
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
"	border-bottom-right-radius: 7px;\n"
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
""
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
"background-color: #444444;\n"
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
""
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
"QToolButton[Q"
                        "ToolButtonStyle=\"5\"] {\n"
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
"	border-top-left-radius: 10px;\n"
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
"/"
                        "*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit[QLineEditStyle=\"1\"]{\n"
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
""
                        "QLineEdit#lineEdit_textMesh5{\n"
"color: #888888;\n"
"}\n"
"*/\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFrame          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"    border: none"
                        ";\n"
"    background-color: #404040;\n"
"    color: white;\n"
"    selection-background-color: #808080;\n"
"    font: 700 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QSlider[QSliderStyle=\"1\"]:"
                        ":handle:horizontal:hover {\n"
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_pointMaterialProject.sizePolicy().hasHeightForWidth())
        self.frame_pointMaterialProject.setSizePolicy(sizePolicy1)
        self.frame_pointMaterialProject.setFrameShape(QFrame.StyledPanel)
        self.frame_pointMaterialProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_pointMaterialProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_pointMaterialProject)
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
        icon.addFile(u"app/resources/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_hideShow.setIcon(icon)
        self.toolButton_hideShow.setIconSize(QSize(15, 15))
        self.toolButton_hideShow.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hideShow)


        self.verticalLayout_2.addWidget(self.frame_hide2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_pointMaterial = QFrame(self.frame_pointMaterialProject)
        self.frame_pointMaterial.setObjectName(u"frame_pointMaterial")
        sizePolicy1.setHeightForWidth(self.frame_pointMaterial.sizePolicy().hasHeightForWidth())
        self.frame_pointMaterial.setSizePolicy(sizePolicy1)
        self.frame_pointMaterial.setFrameShape(QFrame.StyledPanel)
        self.frame_pointMaterial.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_pointMaterial)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_pointMaterial)
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
        self.label_cardPointMaterialTitle = QLabel(self.frame_title)
        self.label_cardPointMaterialTitle.setObjectName(u"label_cardPointMaterialTitle")
        self.label_cardPointMaterialTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardPointMaterialTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_pointMaterial)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_PointMaterialSubTitle1 = QFrame(self.frame_info)
        self.frame_PointMaterialSubTitle1.setObjectName(u"frame_PointMaterialSubTitle1")
        self.frame_PointMaterialSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_PointMaterialSubTitle1.setFrameShadow(QFrame.Raised)
        self.frame_PointMaterialSubTitle1.setProperty("QFrameSubTitleStyle", 1)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_PointMaterialSubTitle1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardPointMaterialSubTitle1 = QLabel(self.frame_PointMaterialSubTitle1)
        self.label_cardPointMaterialSubTitle1.setObjectName(u"label_cardPointMaterialSubTitle1")
        self.label_cardPointMaterialSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardPointMaterialSubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardPointMaterialSubTitle1)

        self.toolButton_cardPointMaterialSubTitle1 = QToolButton(self.frame_PointMaterialSubTitle1)
        self.toolButton_cardPointMaterialSubTitle1.setObjectName(u"toolButton_cardPointMaterialSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardPointMaterialSubTitle1.setIcon(icon1)
        self.toolButton_cardPointMaterialSubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardPointMaterialSubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardPointMaterialSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_PointMaterialSubTitle1)

        self.frame_materialPoint2 = QFrame(self.frame_info)
        self.frame_materialPoint2.setObjectName(u"frame_materialPoint2")
        sizePolicy1.setHeightForWidth(self.frame_materialPoint2.sizePolicy().hasHeightForWidth())
        self.frame_materialPoint2.setSizePolicy(sizePolicy1)
        self.frame_materialPoint2.setFrameShape(QFrame.StyledPanel)
        self.frame_materialPoint2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_materialPoint2)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_materialPoint2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_textPointMaterialName = QLabel(self.frame_3)
        self.label_textPointMaterialName.setObjectName(u"label_textPointMaterialName")
        self.label_textPointMaterialName.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialName.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_textPointMaterialName)

        self.lineEdit_textPointMaterialName = QLineEdit(self.frame_3)
        self.lineEdit_textPointMaterialName.setObjectName(u"lineEdit_textPointMaterialName")
        self.lineEdit_textPointMaterialName.setMinimumSize(QSize(150, 25))
        self.lineEdit_textPointMaterialName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textPointMaterialName.setProperty("QLineEditStyle", 1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textPointMaterialName)

        self.label_textPointMaterialColor = QLabel(self.frame_3)
        self.label_textPointMaterialColor.setObjectName(u"label_textPointMaterialColor")
        self.label_textPointMaterialColor.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialColor.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_textPointMaterialColor)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_textPointMaterialColor = QLineEdit(self.frame_3)
        self.lineEdit_textPointMaterialColor.setObjectName(u"lineEdit_textPointMaterialColor")
        self.lineEdit_textPointMaterialColor.setEnabled(False)
        self.lineEdit_textPointMaterialColor.setMinimumSize(QSize(120, 25))
        self.lineEdit_textPointMaterialColor.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(51, 51, 51, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lineEdit_textPointMaterialColor.setPalette(palette)
        self.lineEdit_textPointMaterialColor.setStyleSheet(u"")
        self.lineEdit_textPointMaterialColor.setProperty("QLineEditStyle", 2)

        self.horizontalLayout_9.addWidget(self.lineEdit_textPointMaterialColor)

        self.toolButton_PointMaterialColor = QToolButton(self.frame_3)
        self.toolButton_PointMaterialColor.setObjectName(u"toolButton_PointMaterialColor")
        icon2 = QIcon()
        icon2.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_PointMaterialColor.setIcon(icon2)
        self.toolButton_PointMaterialColor.setIconSize(QSize(20, 20))
        self.toolButton_PointMaterialColor.setArrowType(Qt.NoArrow)
        self.toolButton_PointMaterialColor.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_9.addWidget(self.toolButton_PointMaterialColor)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.comboBox_PointMaterialBaseMesh = QComboBox(self.frame_3)
        self.comboBox_PointMaterialBaseMesh.setObjectName(u"comboBox_PointMaterialBaseMesh")
        self.comboBox_PointMaterialBaseMesh.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialBaseMesh.setFocusPolicy(Qt.WheelFocus)
        self.comboBox_PointMaterialBaseMesh.setProperty("QComboBoxStyle", 1)

        self.horizontalLayout_11.addWidget(self.comboBox_PointMaterialBaseMesh)


        self.formLayout_3.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.label_textPointMaterialNPoints = QLabel(self.frame_3)
        self.label_textPointMaterialNPoints.setObjectName(u"label_textPointMaterialNPoints")
        self.label_textPointMaterialNPoints.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialNPoints.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_textPointMaterialNPoints)

        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.comboBox_PointMaterialNPoints = QComboBox(self.frame)
        self.comboBox_PointMaterialNPoints.setObjectName(u"comboBox_PointMaterialNPoints")
        self.comboBox_PointMaterialNPoints.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialNPoints.setProperty("QComboBoxStyle", 1)

        self.horizontalLayout_10.addWidget(self.comboBox_PointMaterialNPoints)


        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.frame)

        self.label_textPointMaterialBaseMesh = QLabel(self.frame_3)
        self.label_textPointMaterialBaseMesh.setObjectName(u"label_textPointMaterialBaseMesh")
        self.label_textPointMaterialBaseMesh.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialBaseMesh.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_textPointMaterialBaseMesh)

        self.label_textPointMaterialProperty = QLabel(self.frame_3)
        self.label_textPointMaterialProperty.setObjectName(u"label_textPointMaterialProperty")
        self.label_textPointMaterialProperty.setMinimumSize(QSize(110, 0))
        self.label_textPointMaterialProperty.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_textPointMaterialProperty)

        self.comboBox_PointMaterialProperty = QComboBox(self.frame_3)
        self.comboBox_PointMaterialProperty.setObjectName(u"comboBox_PointMaterialProperty")
        self.comboBox_PointMaterialProperty.setMinimumSize(QSize(0, 25))
        self.comboBox_PointMaterialProperty.setFocusPolicy(Qt.WheelFocus)
        self.comboBox_PointMaterialProperty.setProperty("QComboBoxStyle", 1)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.comboBox_PointMaterialProperty)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.toolButton_PointMaterialCancel = QToolButton(self.frame_materialPoint2)
        self.toolButton_PointMaterialCancel.setObjectName(u"toolButton_PointMaterialCancel")
        self.toolButton_PointMaterialCancel.setMinimumSize(QSize(80, 0))
        self.toolButton_PointMaterialCancel.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterialCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_PointMaterialCancel.setProperty("QToolButtonStyle", 3)

        self.horizontalLayout_12.addWidget(self.toolButton_PointMaterialCancel)

        self.toolButton_PointMaterial = QToolButton(self.frame_materialPoint2)
        self.toolButton_PointMaterial.setObjectName(u"toolButton_PointMaterial")
        self.toolButton_PointMaterial.setMinimumSize(QSize(150, 0))
        self.toolButton_PointMaterial.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PointMaterial.setCursor(QCursor(Qt.PointingHandCursor))
        self.toolButton_PointMaterial.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_12.addWidget(self.toolButton_PointMaterial)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addWidget(self.frame_materialPoint2)

        self.frame_PointMaterialSubTitle2 = QFrame(self.frame_info)
        self.frame_PointMaterialSubTitle2.setObjectName(u"frame_PointMaterialSubTitle2")
        self.frame_PointMaterialSubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_PointMaterialSubTitle2.setFrameShadow(QFrame.Raised)
        self.frame_PointMaterialSubTitle2.setProperty("QFrameSubTitleStyle", 1)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_PointMaterialSubTitle2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardPointMaterialSubTitle2 = QLabel(self.frame_PointMaterialSubTitle2)
        self.label_cardPointMaterialSubTitle2.setObjectName(u"label_cardPointMaterialSubTitle2")
        self.label_cardPointMaterialSubTitle2.setMinimumSize(QSize(100, 0))
        self.label_cardPointMaterialSubTitle2.setProperty("QLabelStyle", 2)

        self.horizontalLayout_7.addWidget(self.label_cardPointMaterialSubTitle2)

        self.horizontalSlider_PointMaterialSize = QSlider(self.frame_PointMaterialSubTitle2)
        self.horizontalSlider_PointMaterialSize.setObjectName(u"horizontalSlider_PointMaterialSize")
        self.horizontalSlider_PointMaterialSize.setMinimumSize(QSize(30, 0))
        self.horizontalSlider_PointMaterialSize.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalSlider_PointMaterialSize.setMinimum(1)
        self.horizontalSlider_PointMaterialSize.setMaximum(299)
        self.horizontalSlider_PointMaterialSize.setSingleStep(10)
        self.horizontalSlider_PointMaterialSize.setValue(100)
        self.horizontalSlider_PointMaterialSize.setTracking(False)
        self.horizontalSlider_PointMaterialSize.setOrientation(Qt.Horizontal)
        self.horizontalSlider_PointMaterialSize.setInvertedAppearance(True)
        self.horizontalSlider_PointMaterialSize.setInvertedControls(True)
        self.horizontalSlider_PointMaterialSize.setTickPosition(QSlider.NoTicks)
        self.horizontalSlider_PointMaterialSize.setTickInterval(0)
        self.horizontalSlider_PointMaterialSize.setProperty("QSliderStyle", 1)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_PointMaterialSize)

        self.toolButton_showHideLabel = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_showHideLabel.setObjectName(u"toolButton_showHideLabel")
        icon3 = QIcon()
        icon3.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideLabel.setIcon(icon3)
        self.toolButton_showHideLabel.setArrowType(Qt.NoArrow)
        self.toolButton_showHideLabel.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideLabel)

        self.toolButton_showHidePointMaterial = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_showHidePointMaterial.setObjectName(u"toolButton_showHidePointMaterial")
        icon4 = QIcon()
        icon4.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHidePointMaterial.setIcon(icon4)
        self.toolButton_showHidePointMaterial.setArrowType(Qt.NoArrow)
        self.toolButton_showHidePointMaterial.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHidePointMaterial)

        self.toolButton_cardPointMaterialSubTitle2 = QToolButton(self.frame_PointMaterialSubTitle2)
        self.toolButton_cardPointMaterialSubTitle2.setObjectName(u"toolButton_cardPointMaterialSubTitle2")
        self.toolButton_cardPointMaterialSubTitle2.setIcon(icon1)
        self.toolButton_cardPointMaterialSubTitle2.setArrowType(Qt.NoArrow)
        self.toolButton_cardPointMaterialSubTitle2.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_cardPointMaterialSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_PointMaterialSubTitle2)

        self.frame_materialPoint3 = QFrame(self.frame_info)
        self.frame_materialPoint3.setObjectName(u"frame_materialPoint3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_materialPoint3.sizePolicy().hasHeightForWidth())
        self.frame_materialPoint3.setSizePolicy(sizePolicy5)
        self.frame_materialPoint3.setMinimumSize(QSize(0, 150))
        self.frame_materialPoint3.setStyleSheet(u"")
        self.frame_materialPoint3.setFrameShape(QFrame.StyledPanel)
        self.frame_materialPoint3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_materialPoint3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_materialPoint3)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"background-color: transparent;\n"
"border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 278, 130))
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
        self.frame_empty.setFrameShape(QFrame.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.verticalLayout_containerCardMaterialPoint.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardMaterialPoint)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_materialPoint3)

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
        self.label_textPointMaterialColor.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Color:", None))
        self.lineEdit_textPointMaterialColor.setText("")
        self.toolButton_PointMaterialColor.setText("")
        self.label_textPointMaterialNPoints.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Puntos x elemento:", None))
        self.label_textPointMaterialBaseMesh.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Malla Base:", None))
        self.label_textPointMaterialProperty.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Material:", None))
        self.toolButton_PointMaterialCancel.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Cancelar", None))
        self.toolButton_PointMaterial.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Crear Puntos", None))
        self.label_cardPointMaterialSubTitle2.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Lista de puntos", None))
        self.toolButton_showHideLabel.setText("")
        self.toolButton_showHidePointMaterial.setText("")
        self.toolButton_cardPointMaterialSubTitle2.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuPointMaterial", u"Empty", None))
    # retranslateUi

