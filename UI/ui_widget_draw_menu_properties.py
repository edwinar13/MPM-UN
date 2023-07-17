# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_propertiesxkyiYA.ui'
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
    QScrollArea, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormDrawMenuProperties(object):
    def setupUi(self, FormDrawMenuProperties):
        if not FormDrawMenuProperties.objectName():
            FormDrawMenuProperties.setObjectName(u"FormDrawMenuProperties")
        FormDrawMenuProperties.resize(350, 782)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuProperties.sizePolicy().hasHeightForWidth())
        FormDrawMenuProperties.setSizePolicy(sizePolicy)
        FormDrawMenuProperties.setMinimumSize(QSize(0, 0))
        FormDrawMenuProperties.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuProperties.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_propertiesProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"/*##################"
                        "###############################################*/\n"
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
"QFrame#frame_properties{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardPropertiesTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_propertiesSubTitle0,\n"
"QFrame#frame_propertiesSubT"
                        "itle1,\n"
"QFrame#frame_propertiesSubTitle2,\n"
"QFrame#frame_propertiesSubTitle3{\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*###########################################################################*/\n"
"/*################      FRAME MALLA REGULAR CUADRIL\u00c1TERO       ######################*/\n"
"/*###########################################################################*/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QToolButton#toolButton_cardPropertiesDraw7,\n"
"QToolButton#toolButton_cardPropertiesDraw5,\n"
"QToolButton#toolButton_cardPropertiesDraw6{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"\n"
"QToolButton#toolButton_cardPropertiesDraw7:hover,\n"
"QToolButton#toolButton_cardPropertiesDraw5:hover, \n"
"QToolButton#toolButton_cardPropertiesDraw6:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardPropertiesDraw7:pressed,\n"
"QToolButto"
                        "n#toolButton_cardPropertiesDraw5:pressed,\n"
"QToolButton#toolButton_cardPropertiesDraw6:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
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
"#verticalLayout_containerCardProperties,\n"
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
"color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*######################      SCROLL BAR    VERTICAL  ############################*/\n"
"\n"
"QScrollBar:vertical {  "
                        "  \n"
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
"/*BOTTON*/\n"
"QScrollBar::add-line:vertical{\n"
"    background-color: #444444;\n"
"	border: none;	\n"
"	border-bottom-left-radius: 7px;\n"
"	border-bottom-right-rad"
                        "ius: 7px;\n"
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
"QScrollBar::handle:horizontal:hover {\n"
"    background-color: #777777;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"    background-color: #666666;\n"
"}\n"
""
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
"QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:horizontal{\n"
"background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizonta"
                        "l{\n"
"background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox[QDoubleSpinBoxStyle=\"1\"]{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
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
"QToolButton[QToolButtonStyle=\"4\"]{\n"
"\n"
"background-c"
                        "olor: #77ACA2;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"4\"]:hover{ \n"
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
"\n"
""
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
"	border-top-left-radius: 10px;\n"
"	border-top-right-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	border-bottom-left-radius: 10px;\n"
"	color: #222222;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"7\"] {\n"
"    ba"
                        "ckground-color: transparent;\n"
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
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
""
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
"QLineEdit#lineEdit_textProperties3{\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFrame          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QFrame[QFrameSubTitleStyle=\"1\"] {\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QLabel[QLabelStyle=\"3\"] {\n"
"font: 300 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuProperties)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_propertiesProject = QFrame(FormDrawMenuProperties)
        self.frame_propertiesProject.setObjectName(u"frame_propertiesProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_propertiesProject.sizePolicy().hasHeightForWidth())
        self.frame_propertiesProject.setSizePolicy(sizePolicy1)
        self.frame_propertiesProject.setFrameShape(QFrame.StyledPanel)
        self.frame_propertiesProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_propertiesProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_propertiesProject)
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
        icon.addFile(u"recursos/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_hideShow.setIcon(icon)
        self.toolButton_hideShow.setIconSize(QSize(15, 15))
        self.toolButton_hideShow.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hideShow)


        self.verticalLayout_2.addWidget(self.frame_hide2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_properties = QFrame(self.frame_propertiesProject)
        self.frame_properties.setObjectName(u"frame_properties")
        sizePolicy1.setHeightForWidth(self.frame_properties.sizePolicy().hasHeightForWidth())
        self.frame_properties.setSizePolicy(sizePolicy1)
        self.frame_properties.setFrameShape(QFrame.StyledPanel)
        self.frame_properties.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_properties)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_properties)
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
        self.label_cardPropertiesTitle = QLabel(self.frame_title)
        self.label_cardPropertiesTitle.setObjectName(u"label_cardPropertiesTitle")
        self.label_cardPropertiesTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardPropertiesTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_properties)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_propertiesSubTitle1 = QFrame(self.frame_info)
        self.frame_propertiesSubTitle1.setObjectName(u"frame_propertiesSubTitle1")
        self.frame_propertiesSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_propertiesSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_propertiesSubTitle1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardPropertiesSubTitle1 = QLabel(self.frame_propertiesSubTitle1)
        self.label_cardPropertiesSubTitle1.setObjectName(u"label_cardPropertiesSubTitle1")
        self.label_cardPropertiesSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardPropertiesSubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardPropertiesSubTitle1)

        self.toolButton_cardPropertiesSubTitle1 = QToolButton(self.frame_propertiesSubTitle1)
        self.toolButton_cardPropertiesSubTitle1.setObjectName(u"toolButton_cardPropertiesSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardPropertiesSubTitle1.setIcon(icon1)
        self.toolButton_cardPropertiesSubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardPropertiesSubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardPropertiesSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_propertiesSubTitle1)

        self.frame_properties1 = QFrame(self.frame_info)
        self.frame_properties1.setObjectName(u"frame_properties1")
        sizePolicy1.setHeightForWidth(self.frame_properties1.sizePolicy().hasHeightForWidth())
        self.frame_properties1.setSizePolicy(sizePolicy1)
        self.frame_properties1.setFrameShape(QFrame.StyledPanel)
        self.frame_properties1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_properties1)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_properties1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textProperties1 = QLabel(self.frame_4)
        self.label_textProperties1.setObjectName(u"label_textProperties1")
        self.label_textProperties1.setMinimumSize(QSize(110, 0))
        self.label_textProperties1.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_textProperties1)

        self.lineEdit_textPropertiesName = QLineEdit(self.frame_4)
        self.lineEdit_textPropertiesName.setObjectName(u"lineEdit_textPropertiesName")
        self.lineEdit_textPropertiesName.setMinimumSize(QSize(150, 25))
        self.lineEdit_textPropertiesName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textPropertiesName.setProperty("QLineEditStyle", 1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textPropertiesName)

        self.label_textProperties2 = QLabel(self.frame_4)
        self.label_textProperties2.setObjectName(u"label_textProperties2")
        self.label_textProperties2.setMinimumSize(QSize(110, 0))
        self.label_textProperties2.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_textProperties2)

        self.doubleSpinBoxl_textPropertiesE = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textPropertiesE.setObjectName(u"doubleSpinBoxl_textPropertiesE")
        self.doubleSpinBoxl_textPropertiesE.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesE.setMinimumSize(QSize(80, 25))
        self.doubleSpinBoxl_textPropertiesE.setDecimals(0)
        self.doubleSpinBoxl_textPropertiesE.setMinimum(1.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setMaximum(1000000.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesE.setValue(1000.000000000000000)
        self.doubleSpinBoxl_textPropertiesE.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesE)

        self.label_textProperties3 = QLabel(self.frame_4)
        self.label_textProperties3.setObjectName(u"label_textProperties3")
        self.label_textProperties3.setMinimumSize(QSize(110, 0))
        self.label_textProperties3.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_textProperties3)

        self.doubleSpinBoxl_textPropertiesV = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textPropertiesV.setObjectName(u"doubleSpinBoxl_textPropertiesV")
        self.doubleSpinBoxl_textPropertiesV.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesV.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesV.setDecimals(2)
        self.doubleSpinBoxl_textPropertiesV.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesV.setMaximum(0.500000000000000)
        self.doubleSpinBoxl_textPropertiesV.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesV.setValue(0.300000000000000)
        self.doubleSpinBoxl_textPropertiesV.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesV)

        self.label_textProperties4 = QLabel(self.frame_4)
        self.label_textProperties4.setObjectName(u"label_textProperties4")
        self.label_textProperties4.setMinimumSize(QSize(110, 0))
        self.label_textProperties4.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_textProperties4)

        self.label_textProperties5 = QLabel(self.frame_4)
        self.label_textProperties5.setObjectName(u"label_textProperties5")
        self.label_textProperties5.setMinimumSize(QSize(110, 0))
        self.label_textProperties5.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_textProperties5)

        self.label_textProperties6 = QLabel(self.frame_4)
        self.label_textProperties6.setObjectName(u"label_textProperties6")
        self.label_textProperties6.setMinimumSize(QSize(110, 0))
        self.label_textProperties6.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_textProperties6)

        self.doubleSpinBoxl_textPropertiesPsi = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textPropertiesPsi.setObjectName(u"doubleSpinBoxl_textPropertiesPsi")
        self.doubleSpinBoxl_textPropertiesPsi.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesPsi.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesPsi.setDecimals(1)
        self.doubleSpinBoxl_textPropertiesPsi.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setSingleStep(0.100000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBoxl_textPropertiesPsi.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesPsi.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesPsi)

        self.doubleSpinBoxl_textPropertiesPhi = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textPropertiesPhi.setObjectName(u"doubleSpinBoxl_textPropertiesPhi")
        self.doubleSpinBoxl_textPropertiesPhi.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesPhi.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesPhi.setDecimals(1)
        self.doubleSpinBoxl_textPropertiesPhi.setMinimum(0.000000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setSingleStep(0.100000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesPhi.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesPhi)

        self.doubleSpinBoxl_textPropertiesC = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textPropertiesC.setObjectName(u"doubleSpinBoxl_textPropertiesC")
        self.doubleSpinBoxl_textPropertiesC.setEnabled(True)
        self.doubleSpinBoxl_textPropertiesC.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textPropertiesC.setDecimals(2)
        self.doubleSpinBoxl_textPropertiesC.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesC.setMaximum(10000.000000000000000)
        self.doubleSpinBoxl_textPropertiesC.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textPropertiesC.setValue(5.000000000000000)
        self.doubleSpinBoxl_textPropertiesC.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.doubleSpinBoxl_textPropertiesC)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.frame_properties1_1 = QFrame(self.frame_properties1)
        self.frame_properties1_1.setObjectName(u"frame_properties1_1")
        sizePolicy1.setHeightForWidth(self.frame_properties1_1.sizePolicy().hasHeightForWidth())
        self.frame_properties1_1.setSizePolicy(sizePolicy1)
        self.frame_properties1_1.setFrameShape(QFrame.StyledPanel)
        self.frame_properties1_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_properties1_1)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.toolButton_PropertiesCancel = QToolButton(self.frame_properties1_1)
        self.toolButton_PropertiesCancel.setObjectName(u"toolButton_PropertiesCancel")
        self.toolButton_PropertiesCancel.setMinimumSize(QSize(80, 0))
        self.toolButton_PropertiesCancel.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PropertiesCancel.setProperty("QToolButtonStyle", 3)

        self.horizontalLayout_12.addWidget(self.toolButton_PropertiesCancel)

        self.toolButton_PropertiesCreateProperty = QToolButton(self.frame_properties1_1)
        self.toolButton_PropertiesCreateProperty.setObjectName(u"toolButton_PropertiesCreateProperty")
        self.toolButton_PropertiesCreateProperty.setMinimumSize(QSize(150, 0))
        self.toolButton_PropertiesCreateProperty.setMaximumSize(QSize(150, 16777215))
        self.toolButton_PropertiesCreateProperty.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_12.addWidget(self.toolButton_PropertiesCreateProperty)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_7.addWidget(self.frame_properties1_1)


        self.verticalLayout_5.addWidget(self.frame_properties1)

        self.frame_propertiesSubTitle2 = QFrame(self.frame_info)
        self.frame_propertiesSubTitle2.setObjectName(u"frame_propertiesSubTitle2")
        self.frame_propertiesSubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_propertiesSubTitle2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_propertiesSubTitle2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardPropertiesSubTitle2 = QLabel(self.frame_propertiesSubTitle2)
        self.label_cardPropertiesSubTitle2.setObjectName(u"label_cardPropertiesSubTitle2")
        self.label_cardPropertiesSubTitle2.setMinimumSize(QSize(262, 0))
        self.label_cardPropertiesSubTitle2.setProperty("QLabelStyle", 2)

        self.horizontalLayout_7.addWidget(self.label_cardPropertiesSubTitle2)

        self.toolButton_cardPropertiesSubTitle2 = QToolButton(self.frame_propertiesSubTitle2)
        self.toolButton_cardPropertiesSubTitle2.setObjectName(u"toolButton_cardPropertiesSubTitle2")
        self.toolButton_cardPropertiesSubTitle2.setIcon(icon1)
        self.toolButton_cardPropertiesSubTitle2.setArrowType(Qt.NoArrow)
        self.toolButton_cardPropertiesSubTitle2.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_cardPropertiesSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_propertiesSubTitle2)

        self.frame_properties2 = QFrame(self.frame_info)
        self.frame_properties2.setObjectName(u"frame_properties2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_properties2.sizePolicy().hasHeightForWidth())
        self.frame_properties2.setSizePolicy(sizePolicy5)
        self.frame_properties2.setMinimumSize(QSize(0, 150))
        self.frame_properties2.setStyleSheet(u"")
        self.frame_properties2.setFrameShape(QFrame.StyledPanel)
        self.frame_properties2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_properties2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_properties2)
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
        self.verticalLayout_containerCardProperties = QVBoxLayout()
        self.verticalLayout_containerCardProperties.setSpacing(0)
        self.verticalLayout_containerCardProperties.setObjectName(u"verticalLayout_containerCardProperties")
        self.frame_empty = QFrame(self.scrollAreaWidgetContents)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy5.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy5)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.verticalLayout_containerCardProperties.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardProperties)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_properties2)

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


        self.horizontalLayout.addWidget(self.frame_properties)


        self.horizontalLayout_6.addWidget(self.frame_propertiesProject)


        self.retranslateUi(FormDrawMenuProperties)

        QMetaObject.connectSlotsByName(FormDrawMenuProperties)
    # setupUi

    def retranslateUi(self, FormDrawMenuProperties):
        FormDrawMenuProperties.setWindowTitle(QCoreApplication.translate("FormDrawMenuProperties", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardPropertiesTitle.setText(QCoreApplication.translate("FormDrawMenuProperties", u"MATERIALES", None))
        self.label_cardPropertiesSubTitle1.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Crear material", None))
        self.toolButton_cardPropertiesSubTitle1.setText("")
        self.label_textProperties1.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Nombre:", None))
        self.lineEdit_textPropertiesName.setText("")
#if QT_CONFIG(tooltip)
        self.label_textProperties2.setToolTip(QCoreApplication.translate("FormDrawMenuProperties", u"M\u00f3dulo de espasticidad", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties2.setText(QCoreApplication.translate("FormDrawMenuProperties", u"E (KPa):", None))
        self.doubleSpinBoxl_textPropertiesE.setSuffix(QCoreApplication.translate("FormDrawMenuProperties", u" KPa", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties3.setToolTip(QCoreApplication.translate("FormDrawMenuProperties", u"Coeficiente de poisson", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties3.setText(QCoreApplication.translate("FormDrawMenuProperties", u"\u03bd :", None))
        self.doubleSpinBoxl_textPropertiesV.setSuffix("")
#if QT_CONFIG(tooltip)
        self.label_textProperties4.setToolTip(QCoreApplication.translate("FormDrawMenuProperties", u"Cohesi\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties4.setText(QCoreApplication.translate("FormDrawMenuProperties", u"C' (KPa):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties5.setToolTip(QCoreApplication.translate("FormDrawMenuProperties", u"\u00c1ngulo  de fricci\u00f3n ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties5.setText(QCoreApplication.translate("FormDrawMenuProperties", u"\u03d5 (\u00b0):", None))
#if QT_CONFIG(tooltip)
        self.label_textProperties6.setToolTip(QCoreApplication.translate("FormDrawMenuProperties", u"\u00c1ngulo  de dilatancia ", None))
#endif // QT_CONFIG(tooltip)
        self.label_textProperties6.setText(QCoreApplication.translate("FormDrawMenuProperties", u"\u03c8 (\u00b0):", None))
        self.doubleSpinBoxl_textPropertiesPsi.setSuffix(QCoreApplication.translate("FormDrawMenuProperties", u" \u00b0", None))
        self.doubleSpinBoxl_textPropertiesPhi.setSuffix(QCoreApplication.translate("FormDrawMenuProperties", u" \u00b0", None))
        self.doubleSpinBoxl_textPropertiesC.setSuffix(QCoreApplication.translate("FormDrawMenuProperties", u" KPa", None))
        self.toolButton_PropertiesCancel.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Cancelar", None))
        self.toolButton_PropertiesCreateProperty.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Crear material", None))
        self.label_cardPropertiesSubTitle2.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Lista de materiales", None))
        self.toolButton_cardPropertiesSubTitle2.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuProperties", u"Empty", None))
    # retranslateUi

