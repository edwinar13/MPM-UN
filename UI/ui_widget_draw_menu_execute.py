# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_executeoBCnpL.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QSizePolicy,
    QSpacerItem, QToolButton, QVBoxLayout, QWidget)

class Ui_FormDrawMenuExecute(object):
    def setupUi(self, FormDrawMenuExecute):
        if not FormDrawMenuExecute.objectName():
            FormDrawMenuExecute.setObjectName(u"FormDrawMenuExecute")
        FormDrawMenuExecute.resize(350, 809)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuExecute.sizePolicy().hasHeightForWidth())
        FormDrawMenuExecute.setSizePolicy(sizePolicy)
        FormDrawMenuExecute.setMinimumSize(QSize(0, 0))
        FormDrawMenuExecute.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuExecute.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_ExecuteProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"/*#####################"
                        "############################################*/\n"
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
"QFrame#frame_Execute{\n"
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
"QFrame#frame_ExecuteSubTitle1,\n"
"QFrame#frame_ExecuteSubTitle2{\n"
""
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
"QToolButton#toolButton_cardBoundaryDraw6:pressed{\n"
"bor"
                        "der-top: 2px solid #222222;\n"
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
"	margin: 15px 0px 15px 0px;\n"
"}\n"
""
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
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
""
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
"background-color: #666666;\n"
"border: none;\n"
"border-top-le"
                        "ft-radius: 7px;\n"
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
"QDoubleSpinBox[QDoubleSpinBoxStyle=\"1\"]"
                        "{\n"
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
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
""
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
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 "
                        "#F7F052\n"
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
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 10px;\n"
"	bor"
                        "der-bottom-right-radius: 10px;\n"
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
"/*******************************************/\n"
"QToolButton[QToolButtonStyle=\"9\"]{\n"
"font: 500 14pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #34eb98;\n"
"border: none;\n"
"padding: 6px 6px;\n"
"border-radius: 8px ;\n"
"}\n"
"QToolButton[QToolButtonStyle=\"9\"]:hover{\n"
"background-color: #15ab67;\n"
"}\n"
"\n"
"/* \n"
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFr"
                        "ame          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"colo"
                        "r: #DDDDDD;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QCheckBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QListView            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"QListWidget[QListWidgetStyle=\"1\"] {\n"
"	color: #DDDDDD;\n"
"    background-color: #333;\n"
"	font:  9pt \"Ubuntu\";\n"
" 	border: 1px solid #444;\n"
"	border-radius: 5px;\n"
"	\n"
"    }\n"
"\n"
"QListWidget[QListWidgetStyle=\"1\"]::item {\n"
"	border: 1px solid #808080;\n"
"    border-radius: 5px;\n"
"	padding: 2px 0px;\n"
"background-color: #928ECC;\n"
"color: #222;\n"
"    }\n"
"\n"
"QListWidget[QListWidgetStyle=\"1\"]::item:selected {\n"
"        color: #444444;\n"
"        background-color: #DDDDDD;\n"
"    }\n"
"\n"
"\n"
"QListWidget[QListWidgetItemStyle=\"2\"]::item {\n"
"	border: 1px solid #808080;\n"
"    border-radius: 5px;\n"
"	padding: 2px 0px;\n"
"	background-color: #C8CC8E;\n"
"	color: #222;\n"
"    }\n"
"\n"
"\n"
"\n"
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
"rojos #910"
                        "D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuExecute)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_ExecuteProject = QFrame(FormDrawMenuExecute)
        self.frame_ExecuteProject.setObjectName(u"frame_ExecuteProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_ExecuteProject.sizePolicy().hasHeightForWidth())
        self.frame_ExecuteProject.setSizePolicy(sizePolicy1)
        self.frame_ExecuteProject.setFrameShape(QFrame.StyledPanel)
        self.frame_ExecuteProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ExecuteProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_ExecuteProject)
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

        self.frame_Execute = QFrame(self.frame_ExecuteProject)
        self.frame_Execute.setObjectName(u"frame_Execute")
        sizePolicy1.setHeightForWidth(self.frame_Execute.sizePolicy().hasHeightForWidth())
        self.frame_Execute.setSizePolicy(sizePolicy1)
        self.frame_Execute.setFrameShape(QFrame.StyledPanel)
        self.frame_Execute.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Execute)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_Execute)
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
        self.label_cardExecuteTitle = QLabel(self.frame_title)
        self.label_cardExecuteTitle.setObjectName(u"label_cardExecuteTitle")
        self.label_cardExecuteTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardExecuteTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_Execute)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_ExecuteSubTitle1 = QFrame(self.frame_info)
        self.frame_ExecuteSubTitle1.setObjectName(u"frame_ExecuteSubTitle1")
        self.frame_ExecuteSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_ExecuteSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ExecuteSubTitle1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardExecuteSubTitle1 = QLabel(self.frame_ExecuteSubTitle1)
        self.label_cardExecuteSubTitle1.setObjectName(u"label_cardExecuteSubTitle1")
        self.label_cardExecuteSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardExecuteSubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardExecuteSubTitle1)

        self.toolButton_cardExecuteSubTitle1 = QToolButton(self.frame_ExecuteSubTitle1)
        self.toolButton_cardExecuteSubTitle1.setObjectName(u"toolButton_cardExecuteSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardExecuteSubTitle1.setIcon(icon1)
        self.toolButton_cardExecuteSubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardExecuteSubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardExecuteSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_ExecuteSubTitle1)

        self.frame_Execute1 = QFrame(self.frame_info)
        self.frame_Execute1.setObjectName(u"frame_Execute1")
        self.frame_Execute1.setStyleSheet(u"")
        self.frame_Execute1.setFrameShape(QFrame.StyledPanel)
        self.frame_Execute1.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Execute1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_textBoundary1 = QLabel(self.frame_Execute1)
        self.label_textBoundary1.setObjectName(u"label_textBoundary1")
        self.label_textBoundary1.setMinimumSize(QSize(110, 0))
        self.label_textBoundary1.setProperty("QLabelStyle", 3)

        self.verticalLayout.addWidget(self.label_textBoundary1)

        self.frame_8 = QFrame(self.frame_Execute1)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.listWidget_execute_pointMaterialFrom = QListWidget(self.frame_8)
        self.listWidget_execute_pointMaterialFrom.setObjectName(u"listWidget_execute_pointMaterialFrom")
        self.listWidget_execute_pointMaterialFrom.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialFrom.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialFrom.setSpacing(3)
        self.listWidget_execute_pointMaterialFrom.setProperty("QListWidgetStyle", 1)

        self.horizontalLayout_22.addWidget(self.listWidget_execute_pointMaterialFrom)

        self.listWidget_execute_pointMaterialTo = QListWidget(self.frame_8)
        self.listWidget_execute_pointMaterialTo.setObjectName(u"listWidget_execute_pointMaterialTo")
        self.listWidget_execute_pointMaterialTo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialTo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialTo.setSpacing(3)
        self.listWidget_execute_pointMaterialTo.setProperty("QListWidgetStyle", 1)
        self.listWidget_execute_pointMaterialTo.setProperty("QListWidgetItemStyle", 2)

        self.horizontalLayout_22.addWidget(self.listWidget_execute_pointMaterialTo)

        self.listWidget_execute_pointMaterialTo.raise_()
        self.listWidget_execute_pointMaterialFrom.raise_()

        self.verticalLayout.addWidget(self.frame_8)

        self.label_textBoundary3 = QLabel(self.frame_Execute1)
        self.label_textBoundary3.setObjectName(u"label_textBoundary3")
        self.label_textBoundary3.setMinimumSize(QSize(110, 0))
        self.label_textBoundary3.setProperty("QLabelStyle", 3)

        self.verticalLayout.addWidget(self.label_textBoundary3)

        self.frame_9 = QFrame(self.frame_Execute1)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.listWidget_execute_boundariesFrom = QListWidget(self.frame_9)
        self.listWidget_execute_boundariesFrom.setObjectName(u"listWidget_execute_boundariesFrom")
        self.listWidget_execute_boundariesFrom.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesFrom.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesFrom.setSpacing(3)
        self.listWidget_execute_boundariesFrom.setProperty("QListWidgetStyle", 1)

        self.horizontalLayout_23.addWidget(self.listWidget_execute_boundariesFrom)

        self.listWidget_execute_boundariesTo = QListWidget(self.frame_9)
        self.listWidget_execute_boundariesTo.setObjectName(u"listWidget_execute_boundariesTo")
        self.listWidget_execute_boundariesTo.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesTo.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesTo.setSpacing(3)
        self.listWidget_execute_boundariesTo.setProperty("QListWidgetStyle", 1)
        self.listWidget_execute_boundariesTo.setProperty("QListWidgetItemStyle", 2)

        self.horizontalLayout_23.addWidget(self.listWidget_execute_boundariesTo)


        self.verticalLayout.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_Execute1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_textResultAnimation3_2 = QLabel(self.frame_info)
        self.label_textResultAnimation3_2.setObjectName(u"label_textResultAnimation3_2")
        self.label_textResultAnimation3_2.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation3_2.setProperty("QLabelStyle", 3)

        self.horizontalLayout_4.addWidget(self.label_textResultAnimation3_2)

        self.doubleSpinBoxl_textExecuteTimeAnalysis = QDoubleSpinBox(self.frame_info)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setObjectName(u"doubleSpinBoxl_textExecuteTimeAnalysis")
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setEnabled(True)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setDecimals(1)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMinimum(0.100000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMaximum(100.000000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setValue(1.000000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setProperty("QDoubleSpinBoxStyle", 1)

        self.horizontalLayout_4.addWidget(self.doubleSpinBoxl_textExecuteTimeAnalysis)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.toolButton_Execute = QToolButton(self.frame_info)
        self.toolButton_Execute.setObjectName(u"toolButton_Execute")
        self.toolButton_Execute.setMinimumSize(QSize(180, 0))
        self.toolButton_Execute.setMaximumSize(QSize(200, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_analisis/excute.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_Execute.setIcon(icon2)
        self.toolButton_Execute.setIconSize(QSize(30, 30))
        self.toolButton_Execute.setPopupMode(QToolButton.InstantPopup)
        self.toolButton_Execute.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_Execute.setAutoRaise(False)
        self.toolButton_Execute.setArrowType(Qt.RightArrow)
        self.toolButton_Execute.setProperty("QToolButtonStyle", 9)

        self.horizontalLayout_8.addWidget(self.toolButton_Execute)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msn = QLabel(self.frame_info)
        self.label_msn.setObjectName(u"label_msn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_msn.sizePolicy().hasHeightForWidth())
        self.label_msn.setSizePolicy(sizePolicy7)
        self.label_msn.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_msn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_Execute)


        self.horizontalLayout_6.addWidget(self.frame_ExecuteProject)


        self.retranslateUi(FormDrawMenuExecute)

        QMetaObject.connectSlotsByName(FormDrawMenuExecute)
    # setupUi

    def retranslateUi(self, FormDrawMenuExecute):
        FormDrawMenuExecute.setWindowTitle(QCoreApplication.translate("FormDrawMenuExecute", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardExecuteTitle.setText(QCoreApplication.translate("FormDrawMenuExecute", u"AN\u00c1LISIS", None))
        self.label_cardExecuteSubTitle1.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Datos", None))
        self.toolButton_cardExecuteSubTitle1.setText("")
        self.label_textBoundary1.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Puntos materiales", None))
        self.label_textBoundary3.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Contornos:", None))
        self.label_textResultAnimation3_2.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Tiempo de an\u00e1lisis:", None))
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setSuffix("")
        self.toolButton_Execute.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Ejecutar An\u00e1lisis", None))
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Empty", None))
    # retranslateUi

