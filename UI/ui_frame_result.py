# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_resultYqRVtC.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_FormResult(object):
    def setupUi(self, FormResult):
        if not FormResult.objectName():
            FormResult.setObjectName(u"FormResult")
        FormResult.resize(751, 458)
        FormResult.setStyleSheet(u"/*Colores primarios*/\n"
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
"#FormResult{\n"
"background: #333333;\n"
"}\n"
"\n"
"/*############################################################"
                        "#####*/\n"
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
"QFrame#frame_boundarySubTitle1,\n"
"QFrame#frame_boundarySubTitle2,\n"
""
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
"QToolButton#toolButton_cardBoundaryDraw5:pressed,\n"
"QToolButton#toolButto"
                        "n_cardBoundaryDraw6:pressed{\n"
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
"    width: 14px;\n"
"	border-radius: 0px;\n"
""
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
"	subcontrol-position: bottom;\n"
"	subc"
                        "ontrol-origin: margin;\n"
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
"QScrollBar::sub-line:horizontal{\n"
"background-color: #66666"
                        "6;\n"
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
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QDo"
                        "ubleSpinBox[QDoubleSpinBoxStyle=\"1\"]{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QPushButtonStyle           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*******************************************/\n"
"QPushButton[QPushButtonStyle=\"1\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 6px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"1\"]:hover{\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"/*****************************************/\n"
"QPushButton[QPushButtonStyle=\"2\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #"
                        "910D3F;\n"
"border: none;\n"
"padding: 6px 5px;\n"
"border-radius: 6px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"2\"]:hover{\n"
"background-color: #C70039;\n"
"}\n"
"\n"
"/*****************************************/\n"
"QPushButton[QPushButtonStyle=\"3\"]{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #333;\n"
"background-color: #aaa;\n"
"border: none;\n"
"padding: 6px 5px;\n"
"border-radius: 6px ;\n"
"}\n"
"QPushButton[QPushButtonStyle=\"3\"]:hover{\n"
"background-color: #ddd;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"QToolButton[QToolButtonStyle=\"0\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 1px;\n"
"}\n"
"\n"
"QToolButton[QToolButtonS"
                        "tyle=\"0\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"0\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
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
"\n"
"\n"
"/***************"
                        "****************************/\n"
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
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"/*******************************************/\n"
"QToolButton[QToolButtonStyle=\"5\"],\n"
"QToolButton[QToolButtonStyle=\"6\"],\n"
"QToolButton[QToolButtonStyle=\"7\"],\n"
"QToolButton[QToolButtonStyle=\"8\"] {\n"
"    font: 500 10pt \""
                        "Ubuntu\";    \n"
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
"	bor"
                        "der-bottom-right-radius: 10px;\n"
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
"QLineEdit[QLineEditStyle='1']::placeholder { color: #FF0000; }\n"
"QLineEdit[QLineEditStyle=\"1\"]::placeholder{\n"
"color: #777777;\n"
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
"QL"
                        "ineEdit#lineEdit_textBoundary3{\n"
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
"QFrame[QFrameStyle=\"1\"] {\n"
"background: #333333;\n"
"border-radius:2px;\n"
"}\n"
"\n"
"\n"
"QFrame[QFrameStyle=\"2\"] {\n"
"background: #eee;\n"
"border-radius:10px;\n"
"border: 1px solid #808080;\n"
"padding: 5px;\n"
"margin: 5px;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QTableWidget          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"QTableWidget[QTableWidgetStyle=\"1\"] {\n"
"background: #eee;\n"
"border-radius:10px;\n"
"border: 1px solid #808080;\n"
"padding: 5px;\n"
"margin: 5px;\n"
"color: #333;\n"
"font:  9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QComboBox[QComboBoxSt"
                        "yle=\"1\"] QAbstractItemView {\n"
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
"    padding: 5px;\n"
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
""
                        "\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QTabWidget            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"QTabWidget[QTabWidgetStyle=\"1\"] {\n"
"background: #333;\n"
"border-radius:10px;\n"
"border: 1px solid #808080;\n"
"padding: 5px;\n"
"margin: 5px;\n"
"color: #DDDDDD;\n"
"font:  300 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"QTabWidget[QTabWidgetStyle=\"1\"]::pane {\n"
"background: #333;\n"
"border: 1px solid #808080;\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"QTabBar {\n"
"background: #333;\n"
"border: none;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"background: #333;\n"
"border: 1px solid #555;\n"
"color: #DDDDDD;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"background: #C8CC8E;\n"
"border: 1px solid #C8CC8E;\n"
"padding: 5px;\n"
"color: #333;\n"
"font: 500 9pt \"Ubuntu\";\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"backg"
                        "round: #77ACA2;\n"
"color: #333;\n"
"}\n"
"\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QScrollArea            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QScrollArea{\n"
"border-radius:10px;\n"
"border: 1px solid #666;\n"
"}\n"
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
        self.horizontalLayout_5 = QHBoxLayout(FormResult)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(FormResult)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setProperty("QTabWidgetStyle", 1)
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.tab_1.setProperty("QTabBarStyle", 1)
        self.gridLayout_2 = QGridLayout(self.tab_1)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.tab_1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setProperty("QFrameStyle", 1)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 35))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 5, 10, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_textPointMaterialName = QLabel(self.frame_2)
        self.label_textPointMaterialName.setObjectName(u"label_textPointMaterialName")
        self.label_textPointMaterialName.setMinimumSize(QSize(0, 30))
        self.label_textPointMaterialName.setProperty("QLabelStyle", 3)

        self.horizontalLayout_2.addWidget(self.label_textPointMaterialName)

        self.comboBox_sceneTypeResult = QComboBox(self.frame_2)
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.addItem("")
        self.comboBox_sceneTypeResult.setObjectName(u"comboBox_sceneTypeResult")
        self.comboBox_sceneTypeResult.setMinimumSize(QSize(0, 25))
        self.comboBox_sceneTypeResult.setFocusPolicy(Qt.WheelFocus)
        self.comboBox_sceneTypeResult.setProperty("QComboBoxStyle", 1)

        self.horizontalLayout_2.addWidget(self.comboBox_sceneTypeResult)

        self.toolButton_sceneRegress = QToolButton(self.frame_2)
        self.toolButton_sceneRegress.setObjectName(u"toolButton_sceneRegress")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/icono_result/atras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneRegress.setIcon(icon)
        self.toolButton_sceneRegress.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_2.addWidget(self.toolButton_sceneRegress)

        self.toolButton_sceneStop = QToolButton(self.frame_2)
        self.toolButton_sceneStop.setObjectName(u"toolButton_sceneStop")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/icono_result/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneStop.setIcon(icon1)
        self.toolButton_sceneStop.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_2.addWidget(self.toolButton_sceneStop)

        self.toolButton_scenePlay = QToolButton(self.frame_2)
        self.toolButton_scenePlay.setObjectName(u"toolButton_scenePlay")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/icono_result/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_scenePlay.setIcon(icon2)
        self.toolButton_scenePlay.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_2.addWidget(self.toolButton_scenePlay)

        self.toolButton_sceneAdvance = QToolButton(self.frame_2)
        self.toolButton_sceneAdvance.setObjectName(u"toolButton_sceneAdvance")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/icono_result/adelante.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneAdvance.setIcon(icon3)
        self.toolButton_sceneAdvance.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_2.addWidget(self.toolButton_sceneAdvance)

        self.label_textPointMaterialName_2 = QLabel(self.frame_2)
        self.label_textPointMaterialName_2.setObjectName(u"label_textPointMaterialName_2")
        self.label_textPointMaterialName_2.setMinimumSize(QSize(0, 30))
        self.label_textPointMaterialName_2.setProperty("QLabelStyle", 3)

        self.horizontalLayout_2.addWidget(self.label_textPointMaterialName_2)

        self.label_textResultTime = QLabel(self.frame_2)
        self.label_textResultTime.setObjectName(u"label_textResultTime")
        self.label_textResultTime.setMinimumSize(QSize(60, 30))
        self.label_textResultTime.setProperty("QLabelStyle", 3)

        self.horizontalLayout_2.addWidget(self.label_textResultTime)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.frame_pointMaterial = QFrame(self.frame)
        self.frame_pointMaterial.setObjectName(u"frame_pointMaterial")
        self.frame_pointMaterial.setFrameShape(QFrame.StyledPanel)
        self.frame_pointMaterial.setFrameShadow(QFrame.Raised)
        self.frame_pointMaterial.setProperty("QFrameStyle", 0)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_pointMaterial)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_pointMaterial = QVBoxLayout()
        self.verticalLayout_pointMaterial.setSpacing(0)
        self.verticalLayout_pointMaterial.setObjectName(u"verticalLayout_pointMaterial")
        self.verticalLayout_pointMaterial.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addLayout(self.verticalLayout_pointMaterial)


        self.verticalLayout_4.addWidget(self.frame_pointMaterial)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/icono_result/view_points.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_1, icon4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setProperty("QTabBarStyle", 1)
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setProperty("QFrameStyle", 1)
        self.verticalLayout_5 = QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 35))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 5, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.label_text_char1 = QLabel(self.frame_5)
        self.label_text_char1.setObjectName(u"label_text_char1")
        self.label_text_char1.setMinimumSize(QSize(0, 0))
        self.label_text_char1.setProperty("QLabelStyle", 3)

        self.horizontalLayout_3.addWidget(self.label_text_char1)

        self.comboBox_chartTypeResult = QComboBox(self.frame_5)
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.addItem("")
        self.comboBox_chartTypeResult.setObjectName(u"comboBox_chartTypeResult")
        self.comboBox_chartTypeResult.setMinimumSize(QSize(0, 25))
        self.comboBox_chartTypeResult.setFocusPolicy(Qt.WheelFocus)
        self.comboBox_chartTypeResult.setProperty("QComboBoxStyle", 1)

        self.horizontalLayout_3.addWidget(self.comboBox_chartTypeResult)

        self.toolButton_chartTypeStyle = QToolButton(self.frame_5)
        self.toolButton_chartTypeStyle.setObjectName(u"toolButton_chartTypeStyle")
        self.toolButton_chartTypeStyle.setMinimumSize(QSize(35, 25))
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/icono_result/graphics.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_chartTypeStyle.setIcon(icon5)
        self.toolButton_chartTypeStyle.setIconSize(QSize(30, 15))
        self.toolButton_chartTypeStyle.setProperty("QToolButtonStyle", 0)

        self.horizontalLayout_3.addWidget(self.toolButton_chartTypeStyle)

        self.line = QFrame(self.frame_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line)

        self.label_text_chart2 = QLabel(self.frame_5)
        self.label_text_chart2.setObjectName(u"label_text_chart2")
        self.label_text_chart2.setMinimumSize(QSize(85, 0))
        self.label_text_chart2.setMaximumSize(QSize(85, 16777215))
        self.label_text_chart2.setProperty("QLabelStyle", 3)

        self.horizontalLayout_3.addWidget(self.label_text_chart2)

        self.lineEdit_chartPointName = QLineEdit(self.frame_5)
        self.lineEdit_chartPointName.setObjectName(u"lineEdit_chartPointName")
        self.lineEdit_chartPointName.setMinimumSize(QSize(0, 25))
        self.lineEdit_chartPointName.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_chartPointName.setProperty("QLineEditStyle", 1)

        self.horizontalLayout_3.addWidget(self.lineEdit_chartPointName)

        self.toolButton_chartAddPoint = QToolButton(self.frame_5)
        self.toolButton_chartAddPoint.setObjectName(u"toolButton_chartAddPoint")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/icono_result/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_chartAddPoint.setIcon(icon6)
        self.toolButton_chartAddPoint.setIconSize(QSize(20, 20))
        self.toolButton_chartAddPoint.setArrowType(Qt.NoArrow)
        self.toolButton_chartAddPoint.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_chartAddPoint)


        self.verticalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_chart = QFrame(self.frame_6)
        self.frame_chart.setObjectName(u"frame_chart")
        self.frame_chart.setFrameShape(QFrame.StyledPanel)
        self.frame_chart.setFrameShadow(QFrame.Raised)
        self.frame_chart.setProperty("QFrameStyle", 2)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_chart)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_chart = QVBoxLayout()
        self.verticalLayout_chart.setSpacing(0)
        self.verticalLayout_chart.setObjectName(u"verticalLayout_chart")

        self.horizontalLayout_4.addLayout(self.verticalLayout_chart)


        self.horizontalLayout_7.addWidget(self.frame_chart)

        self.scrollArea = QScrollArea(self.frame_6)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(80, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 78, 382))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_containerCardPoint = QVBoxLayout()
        self.verticalLayout_containerCardPoint.setSpacing(2)
        self.verticalLayout_containerCardPoint.setObjectName(u"verticalLayout_containerCardPoint")
        self.verticalLayout_containerCardPoint.setContentsMargins(-1, 5, -1, 5)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_containerCardPoint.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_containerCardPoint)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_7.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_6)


        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)

        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/icono_result/view_graphics.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_2, icon7, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_3.setProperty("QTabBarStyle", 1)
        self.verticalLayout_3 = QVBoxLayout(self.tab_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 5, 10, 0)
        self.lineEdit_tableSearchByPointId = QLineEdit(self.tab_3)
        self.lineEdit_tableSearchByPointId.setObjectName(u"lineEdit_tableSearchByPointId")
        self.lineEdit_tableSearchByPointId.setMinimumSize(QSize(0, 25))
        self.lineEdit_tableSearchByPointId.setProperty("QLineEditStyle", 1)

        self.horizontalLayout.addWidget(self.lineEdit_tableSearchByPointId)

        self.pushButton_tableSearchAllPoints = QPushButton(self.tab_3)
        self.pushButton_tableSearchAllPoints.setObjectName(u"pushButton_tableSearchAllPoints")
        self.pushButton_tableSearchAllPoints.setProperty("QPushButtonStyle", 1)

        self.horizontalLayout.addWidget(self.pushButton_tableSearchAllPoints)

        self.pushButton_tableShowHideColumn = QPushButton(self.tab_3)
        self.pushButton_tableShowHideColumn.setObjectName(u"pushButton_tableShowHideColumn")
        self.pushButton_tableShowHideColumn.setProperty("QPushButtonStyle", 3)

        self.horizontalLayout.addWidget(self.pushButton_tableShowHideColumn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.tableWidget_tableResult = QTableWidget(self.tab_3)
        if (self.tableWidget_tableResult.columnCount() < 10):
            self.tableWidget_tableResult.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_tableResult.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        self.tableWidget_tableResult.setObjectName(u"tableWidget_tableResult")
        self.tableWidget_tableResult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_tableResult.setAlternatingRowColors(True)
        self.tableWidget_tableResult.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.tableWidget_tableResult.setRowCount(0)
        self.tableWidget_tableResult.setColumnCount(10)
        self.tableWidget_tableResult.setProperty("QTableWidgetStyle", 1)
        self.tableWidget_tableResult.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_tableResult.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_tableResult.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_tableResult.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.tableWidget_tableResult)

        icon8 = QIcon()
        icon8.addFile(u"recursos/iconos/icono_result/view_board.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.tab_3, icon8, "")

        self.horizontalLayout_5.addWidget(self.tabWidget)


        self.retranslateUi(FormResult)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormResult)
    # setupUi

    def retranslateUi(self, FormResult):
        FormResult.setWindowTitle(QCoreApplication.translate("FormResult", u"Form", None))
        self.label_textPointMaterialName.setText(QCoreApplication.translate("FormResult", u"Tipo de resultado:", None))
        self.comboBox_sceneTypeResult.setItemText(0, QCoreApplication.translate("FormResult", u"default", None))
        self.comboBox_sceneTypeResult.setItemText(1, QCoreApplication.translate("FormResult", u"sigxx", None))
        self.comboBox_sceneTypeResult.setItemText(2, QCoreApplication.translate("FormResult", u"sigyy", None))
        self.comboBox_sceneTypeResult.setItemText(3, QCoreApplication.translate("FormResult", u"sigxy", None))
        self.comboBox_sceneTypeResult.setItemText(4, QCoreApplication.translate("FormResult", u"epsxx", None))
        self.comboBox_sceneTypeResult.setItemText(5, QCoreApplication.translate("FormResult", u"epsyy", None))
        self.comboBox_sceneTypeResult.setItemText(6, QCoreApplication.translate("FormResult", u"epsxy", None))

        self.toolButton_sceneRegress.setText(QCoreApplication.translate("FormResult", u"...", None))
        self.toolButton_sceneStop.setText(QCoreApplication.translate("FormResult", u"...", None))
        self.toolButton_scenePlay.setText(QCoreApplication.translate("FormResult", u"...", None))
        self.toolButton_sceneAdvance.setText(QCoreApplication.translate("FormResult", u"...", None))
        self.label_textPointMaterialName_2.setText(QCoreApplication.translate("FormResult", u"Tiempo:", None))
        self.label_textResultTime.setText(QCoreApplication.translate("FormResult", u"100.0000", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("FormResult", u"PUNTOS MATERIALES", None))
        self.label_text_char1.setText(QCoreApplication.translate("FormResult", u"Graficar:", None))
        self.comboBox_chartTypeResult.setItemText(0, QCoreApplication.translate("FormResult", u"Coordenada X", None))
        self.comboBox_chartTypeResult.setItemText(1, QCoreApplication.translate("FormResult", u"Coordenada Y", None))
        self.comboBox_chartTypeResult.setItemText(2, QCoreApplication.translate("FormResult", u"sigxx", None))
        self.comboBox_chartTypeResult.setItemText(3, QCoreApplication.translate("FormResult", u"sigyy", None))
        self.comboBox_chartTypeResult.setItemText(4, QCoreApplication.translate("FormResult", u"sigxy", None))
        self.comboBox_chartTypeResult.setItemText(5, QCoreApplication.translate("FormResult", u"epsxx", None))
        self.comboBox_chartTypeResult.setItemText(6, QCoreApplication.translate("FormResult", u"epsyy", None))
        self.comboBox_chartTypeResult.setItemText(7, QCoreApplication.translate("FormResult", u"epsxy", None))

        self.toolButton_chartTypeStyle.setText("")
        self.label_text_chart2.setText(QCoreApplication.translate("FormResult", u"Punto material:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_chartPointName.setToolTip(QCoreApplication.translate("FormResult", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Puede buscar por id como 1 o 2 o 3 etc. O por conjuntos separados por coma, por ejemplo 1,2,3\u2026</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_chartPointName.setText("")
        self.lineEdit_chartPointName.setPlaceholderText(QCoreApplication.translate("FormResult", u"id puntos", None))
        self.toolButton_chartAddPoint.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("FormResult", u"GRAFICAS ", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_tableSearchByPointId.setToolTip(QCoreApplication.translate("FormResult", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Puede buscar por id como 1 o 2 o 3 etc. O por conjuntos separados por coma, por ejemplo 1,2,3\u2026</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_tableSearchByPointId.setInputMask("")
        self.lineEdit_tableSearchByPointId.setText("")
        self.lineEdit_tableSearchByPointId.setPlaceholderText(QCoreApplication.translate("FormResult", u"id puntos", None))
        self.pushButton_tableSearchAllPoints.setText(QCoreApplication.translate("FormResult", u"Todos", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_tableShowHideColumn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_tableShowHideColumn.setText(QCoreApplication.translate("FormResult", u"Mostrar/ocultar columnas", None))
        ___qtablewidgetitem = self.tableWidget_tableResult.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("FormResult", u"ID Nodo", None));
        ___qtablewidgetitem1 = self.tableWidget_tableResult.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("FormResult", u"dt", None));
        ___qtablewidgetitem2 = self.tableWidget_tableResult.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("FormResult", u"cor x", None));
        ___qtablewidgetitem3 = self.tableWidget_tableResult.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("FormResult", u"cor y", None));
        ___qtablewidgetitem4 = self.tableWidget_tableResult.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("FormResult", u"sigxx", None));
        ___qtablewidgetitem5 = self.tableWidget_tableResult.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("FormResult", u"sigyy", None));
        ___qtablewidgetitem6 = self.tableWidget_tableResult.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("FormResult", u"sigxy", None));
        ___qtablewidgetitem7 = self.tableWidget_tableResult.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("FormResult", u"epsxx", None));
        ___qtablewidgetitem8 = self.tableWidget_tableResult.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("FormResult", u"epsyy", None));
        ___qtablewidgetitem9 = self.tableWidget_tableResult.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("FormResult", u"epsxy", None));
#if QT_CONFIG(tooltip)
        self.tableWidget_tableResult.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("FormResult", u"TABLA RESUMEN", None))
    # retranslateUi

