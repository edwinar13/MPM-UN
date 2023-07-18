# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_boundarymZlCUe.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QScrollArea,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormDrawMenuBoundary(object):
    def setupUi(self, FormDrawMenuBoundary):
        if not FormDrawMenuBoundary.objectName():
            FormDrawMenuBoundary.setObjectName(u"FormDrawMenuBoundary")
        FormDrawMenuBoundary.resize(350, 782)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuBoundary.sizePolicy().hasHeightForWidth())
        FormDrawMenuBoundary.setSizePolicy(sizePolicy)
        FormDrawMenuBoundary.setMinimumSize(QSize(0, 0))
        FormDrawMenuBoundary.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuBoundary.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_boundaryProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"/*####################"
                        "#############################################*/\n"
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
"/*####################       FRAME boundary       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_boundary{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardBoundaryTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_boundarySubTitle0,\n"
"QFrame#frame_boundarySubTitle1,"
                        "\n"
"QFrame#frame_boundarySubTitle2,\n"
"QFrame#frame_boundarySubTitle3{\n"
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
"QToolButton#toolButton_cardBoundaryDraw7,\n"
"QToolButton#toolButton_cardBoundaryDraw5,\n"
"QToolButton#toolButton_cardBoundaryDraw6{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"\n"
"QToolButton#toolButton_cardBoundaryDraw7:hover,\n"
"QToolButton#toolButton_cardBoundaryDraw5:hover, \n"
"QToolButton#toolButton_cardBoundaryDraw6:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardBoundaryDraw7:pressed,\n"
"QToolButton#toolButton_cardBoundar"
                        "yDraw5:pressed,\n"
"QToolButton#toolButton_cardBoundaryDraw6:pressed{\n"
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
"#verticalLayout_containerCardBoundary,\n"
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
"QScrollBar:vertical {    \n"
"	border: none;\n"
"    "
                        "width: 14px;\n"
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
"	border-bottom-right-radius: 7px;\n"
"	height: 15px;\n"
""
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
"  \n"
"QScrollBar::sub-line:h"
                        "orizontal{\n"
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
"QScrollBar::add-page:horizontal,QScrollBar::sub-page:horizontal{\n"
"background: none;\n"
""
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
"background-color: #77ACA2;\n"
"border: 1p"
                        "x solid #222222;\n"
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
"\n"
"/* \n"
"Azules #36C9C6 #"
                        "00BDB9 #77ACA2\n"
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
"    background-color: transparent;\n"
""
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
"font: 9pt \"Ubuntu\";\n"
"color:"
                        " #DDDDDD;\n"
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
"QLineEdit#lineEdit_textBoundary3{\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QCheckBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QCheckBox[QCheckBoxStyle=\"1\"] {\n"
"    \n"
"    background-color: #444444;\n"
"	color: #DDDDDD;\n"
"    padding"
                        ": 5px;\n"
"	font:  9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"\n"
"QCheckBox[QCheckBoxStyle=\"1\"]::indicator {\n"
"    background-color: transparent;\n"
"    border: 1px solid #808080;\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox[QCheckBoxStyle=\"1\"]::indicator:checked {\n"
"    background-color: #F94646;\n"
"    border: none;\n"
"	 border-radius: 3px;\n"
"}\n"
"\n"
"\n"
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
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuBoundary)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_boundaryProject = QFrame(FormDrawMenuBoundary)
        self.frame_boundaryProject.setObjectName(u"frame_boundaryProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_boundaryProject.sizePolicy().hasHeightForWidth())
        self.frame_boundaryProject.setSizePolicy(sizePolicy1)
        self.frame_boundaryProject.setFrameShape(QFrame.StyledPanel)
        self.frame_boundaryProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_boundaryProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_boundaryProject)
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

        self.frame_boundary = QFrame(self.frame_boundaryProject)
        self.frame_boundary.setObjectName(u"frame_boundary")
        sizePolicy1.setHeightForWidth(self.frame_boundary.sizePolicy().hasHeightForWidth())
        self.frame_boundary.setSizePolicy(sizePolicy1)
        self.frame_boundary.setFrameShape(QFrame.StyledPanel)
        self.frame_boundary.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_boundary)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_boundary)
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
        self.label_cardBoundaryTitle = QLabel(self.frame_title)
        self.label_cardBoundaryTitle.setObjectName(u"label_cardBoundaryTitle")
        self.label_cardBoundaryTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardBoundaryTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_boundary)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_boundarySubTitle1 = QFrame(self.frame_info)
        self.frame_boundarySubTitle1.setObjectName(u"frame_boundarySubTitle1")
        self.frame_boundarySubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_boundarySubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_boundarySubTitle1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardBoundarySubTitle1 = QLabel(self.frame_boundarySubTitle1)
        self.label_cardBoundarySubTitle1.setObjectName(u"label_cardBoundarySubTitle1")
        self.label_cardBoundarySubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardBoundarySubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardBoundarySubTitle1)

        self.toolButton_cardBoundarySubTitle1 = QToolButton(self.frame_boundarySubTitle1)
        self.toolButton_cardBoundarySubTitle1.setObjectName(u"toolButton_cardBoundarySubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardBoundarySubTitle1.setIcon(icon1)
        self.toolButton_cardBoundarySubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardBoundarySubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardBoundarySubTitle1)


        self.verticalLayout_5.addWidget(self.frame_boundarySubTitle1)

        self.frame_boundary1 = QFrame(self.frame_info)
        self.frame_boundary1.setObjectName(u"frame_boundary1")
        sizePolicy1.setHeightForWidth(self.frame_boundary1.sizePolicy().hasHeightForWidth())
        self.frame_boundary1.setSizePolicy(sizePolicy1)
        self.frame_boundary1.setFrameShape(QFrame.StyledPanel)
        self.frame_boundary1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_boundary1)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_boundary1)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textBoundary1_2 = QLabel(self.frame_4)
        self.label_textBoundary1_2.setObjectName(u"label_textBoundary1_2")
        self.label_textBoundary1_2.setMinimumSize(QSize(110, 0))
        self.label_textBoundary1_2.setProperty("QLabelStyle", 3)
        self.label_textBoundary1_2.setProperty("QCheckBoxStyle", 1)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_textBoundary1_2)

        self.label_textBoundary2_2 = QLabel(self.frame_4)
        self.label_textBoundary2_2.setObjectName(u"label_textBoundary2_2")
        self.label_textBoundary2_2.setMinimumSize(QSize(110, 0))
        self.label_textBoundary2_2.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_textBoundary2_2)

        self.label_textBoundary2_3 = QLabel(self.frame_4)
        self.label_textBoundary2_3.setObjectName(u"label_textBoundary2_3")
        self.label_textBoundary2_3.setMinimumSize(QSize(110, 0))
        self.label_textBoundary2_3.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_textBoundary2_3)

        self.frame_2 = QFrame(self.frame_4)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.checkBox_BoundaryRestrictionTXleft = QCheckBox(self.frame_2)
        self.checkBox_BoundaryRestrictionTXleft.setObjectName(u"checkBox_BoundaryRestrictionTXleft")
        self.checkBox_BoundaryRestrictionTXleft.setChecked(True)
        self.checkBox_BoundaryRestrictionTXleft.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_17.addWidget(self.checkBox_BoundaryRestrictionTXleft)

        self.checkBox_BoundaryRestrictionTYleft = QCheckBox(self.frame_2)
        self.checkBox_BoundaryRestrictionTYleft.setObjectName(u"checkBox_BoundaryRestrictionTYleft")
        self.checkBox_BoundaryRestrictionTYleft.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_17.addWidget(self.checkBox_BoundaryRestrictionTYleft)


        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.frame_2)

        self.label_textBoundary2_4 = QLabel(self.frame_4)
        self.label_textBoundary2_4.setObjectName(u"label_textBoundary2_4")
        self.label_textBoundary2_4.setMinimumSize(QSize(110, 0))
        self.label_textBoundary2_4.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_textBoundary2_4)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.checkBox_BoundaryRestrictionTXRight = QCheckBox(self.frame_5)
        self.checkBox_BoundaryRestrictionTXRight.setObjectName(u"checkBox_BoundaryRestrictionTXRight")
        self.checkBox_BoundaryRestrictionTXRight.setChecked(True)
        self.checkBox_BoundaryRestrictionTXRight.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_19.addWidget(self.checkBox_BoundaryRestrictionTXRight)

        self.checkBox_BoundaryRestrictionTYRight = QCheckBox(self.frame_5)
        self.checkBox_BoundaryRestrictionTYRight.setObjectName(u"checkBox_BoundaryRestrictionTYRight")
        self.checkBox_BoundaryRestrictionTYRight.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_19.addWidget(self.checkBox_BoundaryRestrictionTYRight)


        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.checkBox_BoundaryRestrictionTXBottom = QCheckBox(self.frame_6)
        self.checkBox_BoundaryRestrictionTXBottom.setObjectName(u"checkBox_BoundaryRestrictionTXBottom")
        self.checkBox_BoundaryRestrictionTXBottom.setChecked(True)
        self.checkBox_BoundaryRestrictionTXBottom.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_20.addWidget(self.checkBox_BoundaryRestrictionTXBottom)

        self.checkBox_BoundaryRestrictionTYBottom = QCheckBox(self.frame_6)
        self.checkBox_BoundaryRestrictionTYBottom.setObjectName(u"checkBox_BoundaryRestrictionTYBottom")
        self.checkBox_BoundaryRestrictionTYBottom.setChecked(True)
        self.checkBox_BoundaryRestrictionTYBottom.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_20.addWidget(self.checkBox_BoundaryRestrictionTYBottom)


        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.frame_6)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy1.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy1)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.checkBox_BoundaryRestrictionTXTop = QCheckBox(self.frame_7)
        self.checkBox_BoundaryRestrictionTXTop.setObjectName(u"checkBox_BoundaryRestrictionTXTop")
        self.checkBox_BoundaryRestrictionTXTop.setChecked(False)
        self.checkBox_BoundaryRestrictionTXTop.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_21.addWidget(self.checkBox_BoundaryRestrictionTXTop)

        self.checkBox_BoundaryRestrictionTYTop = QCheckBox(self.frame_7)
        self.checkBox_BoundaryRestrictionTYTop.setObjectName(u"checkBox_BoundaryRestrictionTYTop")
        self.checkBox_BoundaryRestrictionTYTop.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_21.addWidget(self.checkBox_BoundaryRestrictionTYTop)


        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.frame_7)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)

        self.toolButton_boundaryCreate_1 = QToolButton(self.frame_boundary1)
        self.toolButton_boundaryCreate_1.setObjectName(u"toolButton_boundaryCreate_1")
        self.toolButton_boundaryCreate_1.setMinimumSize(QSize(150, 0))
        self.toolButton_boundaryCreate_1.setMaximumSize(QSize(150, 16777215))
        self.toolButton_boundaryCreate_1.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_18.addWidget(self.toolButton_boundaryCreate_1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)


        self.verticalLayout_5.addWidget(self.frame_boundary1)

        self.frame_boundarySubTitle2 = QFrame(self.frame_info)
        self.frame_boundarySubTitle2.setObjectName(u"frame_boundarySubTitle2")
        self.frame_boundarySubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_boundarySubTitle2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_boundarySubTitle2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardBoundarySubTitle2 = QLabel(self.frame_boundarySubTitle2)
        self.label_cardBoundarySubTitle2.setObjectName(u"label_cardBoundarySubTitle2")
        self.label_cardBoundarySubTitle2.setMinimumSize(QSize(262, 0))
        self.label_cardBoundarySubTitle2.setProperty("QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardBoundarySubTitle2)

        self.toolButton_cardBoundarySubTitle2 = QToolButton(self.frame_boundarySubTitle2)
        self.toolButton_cardBoundarySubTitle2.setObjectName(u"toolButton_cardBoundarySubTitle2")
        self.toolButton_cardBoundarySubTitle2.setIcon(icon1)
        self.toolButton_cardBoundarySubTitle2.setArrowType(Qt.NoArrow)
        self.toolButton_cardBoundarySubTitle2.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardBoundarySubTitle2)


        self.verticalLayout_5.addWidget(self.frame_boundarySubTitle2)

        self.frame_boundary2 = QFrame(self.frame_info)
        self.frame_boundary2.setObjectName(u"frame_boundary2")
        sizePolicy1.setHeightForWidth(self.frame_boundary2.sizePolicy().hasHeightForWidth())
        self.frame_boundary2.setSizePolicy(sizePolicy1)
        self.frame_boundary2.setFrameShape(QFrame.StyledPanel)
        self.frame_boundary2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_boundary2)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_boundary2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_textBoundary1 = QLabel(self.frame_3)
        self.label_textBoundary1.setObjectName(u"label_textBoundary1")
        self.label_textBoundary1.setMinimumSize(QSize(110, 0))
        self.label_textBoundary1.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_textBoundary1)

        self.lineEdit_textBoundaryName = QLineEdit(self.frame_3)
        self.lineEdit_textBoundaryName.setObjectName(u"lineEdit_textBoundaryName")
        self.lineEdit_textBoundaryName.setMinimumSize(QSize(150, 25))
        self.lineEdit_textBoundaryName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textBoundaryName.setProperty("QLineEditStyle", 1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textBoundaryName)

        self.label_textBoundary4 = QLabel(self.frame_3)
        self.label_textBoundary4.setObjectName(u"label_textBoundary4")
        self.label_textBoundary4.setMinimumSize(QSize(110, 0))
        self.label_textBoundary4.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_textBoundary4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_textBoundarySelected = QLineEdit(self.frame_3)
        self.lineEdit_textBoundarySelected.setObjectName(u"lineEdit_textBoundarySelected")
        self.lineEdit_textBoundarySelected.setEnabled(False)
        self.lineEdit_textBoundarySelected.setMinimumSize(QSize(120, 25))
        self.lineEdit_textBoundarySelected.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textBoundarySelected.setProperty("QLineEditStyle", 2)

        self.horizontalLayout_11.addWidget(self.lineEdit_textBoundarySelected)

        self.toolButton_cardBoundaryDrawSelected = QToolButton(self.frame_3)
        self.toolButton_cardBoundaryDrawSelected.setObjectName(u"toolButton_cardBoundaryDrawSelected")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_menu_draw_mesh/select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardBoundaryDrawSelected.setIcon(icon2)
        self.toolButton_cardBoundaryDrawSelected.setIconSize(QSize(20, 20))
        self.toolButton_cardBoundaryDrawSelected.setArrowType(Qt.NoArrow)
        self.toolButton_cardBoundaryDrawSelected.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_11.addWidget(self.toolButton_cardBoundaryDrawSelected)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.label_textBoundary3 = QLabel(self.frame_3)
        self.label_textBoundary3.setObjectName(u"label_textBoundary3")
        self.label_textBoundary3.setMinimumSize(QSize(110, 0))
        self.label_textBoundary3.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_textBoundary3)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.checkBox_BoundaryRestrictionTX = QCheckBox(self.frame_8)
        self.checkBox_BoundaryRestrictionTX.setObjectName(u"checkBox_BoundaryRestrictionTX")
        self.checkBox_BoundaryRestrictionTX.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_22.addWidget(self.checkBox_BoundaryRestrictionTX)

        self.checkBox_BoundaryRestrictionTY = QCheckBox(self.frame_8)
        self.checkBox_BoundaryRestrictionTY.setObjectName(u"checkBox_BoundaryRestrictionTY")
        self.checkBox_BoundaryRestrictionTY.setProperty("QCheckBoxStyle", 1)

        self.horizontalLayout_22.addWidget(self.checkBox_BoundaryRestrictionTY)


        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.frame_8)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.toolButton_boundaryCancel_2 = QToolButton(self.frame_boundary2)
        self.toolButton_boundaryCancel_2.setObjectName(u"toolButton_boundaryCancel_2")
        self.toolButton_boundaryCancel_2.setMinimumSize(QSize(80, 0))
        self.toolButton_boundaryCancel_2.setMaximumSize(QSize(150, 16777215))
        self.toolButton_boundaryCancel_2.setProperty("QToolButtonStyle", 3)

        self.horizontalLayout_12.addWidget(self.toolButton_boundaryCancel_2)

        self.toolButton_boundaryCreate_2 = QToolButton(self.frame_boundary2)
        self.toolButton_boundaryCreate_2.setObjectName(u"toolButton_boundaryCreate_2")
        self.toolButton_boundaryCreate_2.setMinimumSize(QSize(150, 0))
        self.toolButton_boundaryCreate_2.setMaximumSize(QSize(150, 16777215))
        self.toolButton_boundaryCreate_2.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_12.addWidget(self.toolButton_boundaryCreate_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addWidget(self.frame_boundary2)

        self.frame_boundarySubTitle3 = QFrame(self.frame_info)
        self.frame_boundarySubTitle3.setObjectName(u"frame_boundarySubTitle3")
        self.frame_boundarySubTitle3.setFrameShape(QFrame.StyledPanel)
        self.frame_boundarySubTitle3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_boundarySubTitle3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardBoundarySubTitle3 = QLabel(self.frame_boundarySubTitle3)
        self.label_cardBoundarySubTitle3.setObjectName(u"label_cardBoundarySubTitle3")
        self.label_cardBoundarySubTitle3.setMinimumSize(QSize(262, 0))
        self.label_cardBoundarySubTitle3.setProperty("QLabelStyle", 2)

        self.horizontalLayout_7.addWidget(self.label_cardBoundarySubTitle3)

        self.toolButton_showHideLabel = QToolButton(self.frame_boundarySubTitle3)
        self.toolButton_showHideLabel.setObjectName(u"toolButton_showHideLabel")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideLabel.setIcon(icon3)
        self.toolButton_showHideLabel.setArrowType(Qt.NoArrow)
        self.toolButton_showHideLabel.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideLabel)

        self.toolButton_showHideBoundary = QToolButton(self.frame_boundarySubTitle3)
        self.toolButton_showHideBoundary.setObjectName(u"toolButton_showHideBoundary")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideBoundary.setIcon(icon4)
        self.toolButton_showHideBoundary.setArrowType(Qt.NoArrow)
        self.toolButton_showHideBoundary.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideBoundary)

        self.toolButton_cardBoundarySubTitle3 = QToolButton(self.frame_boundarySubTitle3)
        self.toolButton_cardBoundarySubTitle3.setObjectName(u"toolButton_cardBoundarySubTitle3")
        self.toolButton_cardBoundarySubTitle3.setIcon(icon1)
        self.toolButton_cardBoundarySubTitle3.setArrowType(Qt.NoArrow)
        self.toolButton_cardBoundarySubTitle3.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_cardBoundarySubTitle3)


        self.verticalLayout_5.addWidget(self.frame_boundarySubTitle3)

        self.frame_boundary3 = QFrame(self.frame_info)
        self.frame_boundary3.setObjectName(u"frame_boundary3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_boundary3.sizePolicy().hasHeightForWidth())
        self.frame_boundary3.setSizePolicy(sizePolicy5)
        self.frame_boundary3.setMinimumSize(QSize(0, 150))
        self.frame_boundary3.setStyleSheet(u"")
        self.frame_boundary3.setFrameShape(QFrame.StyledPanel)
        self.frame_boundary3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_boundary3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_boundary3)
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
        self.verticalLayout_containerCardBoundary = QVBoxLayout()
        self.verticalLayout_containerCardBoundary.setSpacing(0)
        self.verticalLayout_containerCardBoundary.setObjectName(u"verticalLayout_containerCardBoundary")
        self.frame_empty = QFrame(self.scrollAreaWidgetContents)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy5.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy5)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.verticalLayout_containerCardBoundary.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardBoundary)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_boundary3)

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


        self.horizontalLayout.addWidget(self.frame_boundary)


        self.horizontalLayout_6.addWidget(self.frame_boundaryProject)


        self.retranslateUi(FormDrawMenuBoundary)

        QMetaObject.connectSlotsByName(FormDrawMenuBoundary)
    # setupUi

    def retranslateUi(self, FormDrawMenuBoundary):
        FormDrawMenuBoundary.setWindowTitle(QCoreApplication.translate("FormDrawMenuBoundary", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardBoundaryTitle.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"CONTORNO", None))
        self.label_cardBoundarySubTitle1.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Crear restricci\u00f3n de contorno autom\u00e1tico", None))
        self.toolButton_cardBoundarySubTitle1.setText("")
        self.label_textBoundary1_2.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Superior:", None))
        self.label_textBoundary2_2.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Inferior:", None))
        self.label_textBoundary2_3.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Derecho:", None))
        self.checkBox_BoundaryRestrictionTXleft.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Tx", None))
        self.checkBox_BoundaryRestrictionTYleft.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Ty", None))
        self.label_textBoundary2_4.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Izquierdo:", None))
        self.checkBox_BoundaryRestrictionTXRight.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Tx", None))
        self.checkBox_BoundaryRestrictionTYRight.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Ty", None))
        self.checkBox_BoundaryRestrictionTXBottom.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Tx", None))
        self.checkBox_BoundaryRestrictionTYBottom.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Ty", None))
        self.checkBox_BoundaryRestrictionTXTop.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Tx", None))
        self.checkBox_BoundaryRestrictionTYTop.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Ty", None))
        self.toolButton_boundaryCreate_1.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Crear restricci\u00f3n", None))
        self.label_cardBoundarySubTitle2.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Crear restricci\u00f3n contorno manual", None))
        self.toolButton_cardBoundarySubTitle2.setText("")
        self.label_textBoundary1.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Nombre:", None))
        self.lineEdit_textBoundaryName.setText("")
        self.label_textBoundary4.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Seleccionar:", None))
        self.lineEdit_textBoundarySelected.setText("")
        self.toolButton_cardBoundaryDrawSelected.setText("")
        self.label_textBoundary3.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Restricci\u00f3n:", None))
        self.checkBox_BoundaryRestrictionTX.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Tx", None))
        self.checkBox_BoundaryRestrictionTY.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Ty", None))
        self.toolButton_boundaryCancel_2.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Cancelar", None))
        self.toolButton_boundaryCreate_2.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Crear restricci\u00f3n", None))
        self.label_cardBoundarySubTitle3.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Lista de restricciones de contorno", None))
        self.toolButton_showHideLabel.setText("")
        self.toolButton_showHideBoundary.setText("")
        self.toolButton_cardBoundarySubTitle3.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuBoundary", u"Empty", None))
    # retranslateUi

