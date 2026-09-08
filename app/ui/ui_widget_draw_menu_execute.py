# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_executeSAPnlM.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QSizePolicy, QSpacerItem, QSpinBox,
    QToolButton, QVBoxLayout, QWidget)

class Ui_FormDrawMenuExecute(object):
    def setupUi(self, FormDrawMenuExecute):
        if not FormDrawMenuExecute.objectName():
            FormDrawMenuExecute.setObjectName(u"FormDrawMenuExecute")
        FormDrawMenuExecute.resize(350, 829)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
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
"QFrame#frame_info,\n"
""
                        "QFrame#frame,\n"
"QFrame#frame_8,\n"
"QFrame#frame_9,\n"
"QFrame#frame_Execute1,\n"
"QFrame#frame_Execute2,\n"
"QFrame#frame_Execute3{\n"
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
"/*####################       FRAME boundary       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_Execute{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
""
                        "border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardBoundaryTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_ExecuteSubTitle1,\n"
"QFrame#frame_ExecuteSubTitle2,\n"
"QFrame#frame_ExecuteSubTitle3{\n"
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
"QToolButton#toolBu"
                        "tton_cardBoundaryDraw6:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardBoundaryDraw7:pressed,\n"
"QToolButton#toolButton_cardBoundaryDraw5:pressed,\n"
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
""
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
"/*BOTTON*/\n"
"QScrollBar::add-line:ver"
                        "tical{\n"
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
"QScrollBar::handle:horizontal:hover {"
                        "\n"
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
"QScrollBar::up-arrow:horizonta"
                        "l,QScrollBar::down-arrow:horizontal{\n"
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
"QDoubleSpinBox[QDoubleSpinBoxStyle=\"1\"],\n"
"QSpinBox[QSpinBoxStyle=\"1\"]{\n"
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
"QDoubleSpinBox[QDoubleSpinBoxStyle=\"1\"]:enabled,\n"
"QSpinBox[QSpinBoxStyle=\"1\"]:enabled {\n"
"    font: 9pt \"Ubuntu\";\n"
"    color: #DDDDDD;\n"
"    background-color: #444444;\n"
"    border-radius: 2px;\n"
"    padding-right: 6px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QDoubleSpinBox[QDoubleSpinBoxStyle=\"1\"]:disabled,\n"
"QSpinBox[QSpinBoxStyle=\"1\"]:disabled {\n"
"    font: 9pt \"Ubuntu\";\n"
"    color: #666666;  \n"
"    background-color: #393939; \n"
"    border-radius: 2px;\n"
"    padding-right: 6px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"\n"
"\n"
""
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
"QToolButton[QToolButtonStyle=\"4\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"4\"]:pressed{\n"
"border-top: 2px solid #222"
                        "222;\n"
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
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"/*******************************************/\n"
"QToolButton[QToolButtonStyle=\"5\"],\n"
"QToolButton[QToolButtonStyle=\"6\"],\n"
"QToolButton[QT"
                        "oolButtonStyle=\"7\"],\n"
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
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-left-radius: 0px;\n"
"	color: #DDDDDD;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"8\"] {\n"
"    background-colo"
                        "r: #C8CC8E;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"\n"
"\n"
"QLineEdit[QLineEditStyle=\"1\"]{\n"
"font: 9pt \"Ubuntu\";\n"
""
                        "color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"1\"]:disabled {\n"
"    font: 9pt \"Ubuntu\";\n"
"    color: #666666;\n"
"    background-color: #393939;\n"
"    border: 1px solid #333333;\n"
"    border-radius: 2px;\n"
"    padding-right: 6px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
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
"/*\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFrame          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QComboBox[QComboBoxStyle=\"1\"] QAbstractItemView {\n"
"    border: none;\n"
"    background-color: #404040;\n"
"    color: white;\n"
"    selection-background-col"
                        "or: #808080;\n"
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
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QListView  "
                        "          \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"vinot"
                        "into #742427\n"
"*/\n"
"/*Colores secundarios */\n"
"/* \n"
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F28123 #F7F052\n"
"*/\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuExecute)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_ExecuteProject = QFrame(FormDrawMenuExecute)
        self.frame_ExecuteProject.setObjectName(u"frame_ExecuteProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_ExecuteProject.sizePolicy().hasHeightForWidth())
        self.frame_ExecuteProject.setSizePolicy(sizePolicy1)
        self.frame_ExecuteProject.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ExecuteProject.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ExecuteProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_ExecuteProject)
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
        icon.addFile(u"../resources/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_hideShow.setIcon(icon)
        self.toolButton_hideShow.setIconSize(QSize(15, 15))
        self.toolButton_hideShow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)

        self.verticalLayout_4.addWidget(self.toolButton_hideShow)


        self.verticalLayout_2.addWidget(self.frame_hide2)

        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_hide)

        self.frame_Execute = QFrame(self.frame_ExecuteProject)
        self.frame_Execute.setObjectName(u"frame_Execute")
        sizePolicy1.setHeightForWidth(self.frame_Execute.sizePolicy().hasHeightForWidth())
        self.frame_Execute.setSizePolicy(sizePolicy1)
        self.frame_Execute.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Execute.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Execute)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_Execute)
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
        self.label_cardExecuteTitle = QLabel(self.frame_title)
        self.label_cardExecuteTitle.setObjectName(u"label_cardExecuteTitle")
        self.label_cardExecuteTitle.setProperty(u"QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardExecuteTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_Execute)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_ExecuteSubTitle2 = QFrame(self.frame_info)
        self.frame_ExecuteSubTitle2.setObjectName(u"frame_ExecuteSubTitle2")
        self.frame_ExecuteSubTitle2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ExecuteSubTitle2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_ExecuteSubTitle2)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 0, 0, 0)
        self.label_cardExecuteSubTitle2 = QLabel(self.frame_ExecuteSubTitle2)
        self.label_cardExecuteSubTitle2.setObjectName(u"label_cardExecuteSubTitle2")
        self.label_cardExecuteSubTitle2.setMinimumSize(QSize(262, 0))
        self.label_cardExecuteSubTitle2.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_17.addWidget(self.label_cardExecuteSubTitle2)

        self.toolButton_cardExecuteSubTitle2 = QToolButton(self.frame_ExecuteSubTitle2)
        self.toolButton_cardExecuteSubTitle2.setObjectName(u"toolButton_cardExecuteSubTitle2")
        icon1 = QIcon()
        icon1.addFile(u"../resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_cardExecuteSubTitle2.setIcon(icon1)
        self.toolButton_cardExecuteSubTitle2.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardExecuteSubTitle2.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_17.addWidget(self.toolButton_cardExecuteSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_ExecuteSubTitle2)

        self.frame_Execute2 = QFrame(self.frame_info)
        self.frame_Execute2.setObjectName(u"frame_Execute2")
        self.frame_Execute2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Execute2.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_Execute2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(9)
        self.formLayout.setVerticalSpacing(9)
        self.label_texExcute_5 = QLabel(self.frame_Execute2)
        self.label_texExcute_5.setObjectName(u"label_texExcute_5")
        self.label_texExcute_5.setMinimumSize(QSize(110, 0))
        self.label_texExcute_5.setWordWrap(True)
        self.label_texExcute_5.setProperty(u"QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_texExcute_5)

        self.doubleSpinBoxl_textExecuteNumberCourant = QDoubleSpinBox(self.frame_Execute2)
        self.doubleSpinBoxl_textExecuteNumberCourant.setObjectName(u"doubleSpinBoxl_textExecuteNumberCourant")
        self.doubleSpinBoxl_textExecuteNumberCourant.setEnabled(True)
        self.doubleSpinBoxl_textExecuteNumberCourant.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textExecuteNumberCourant.setDecimals(2)
        self.doubleSpinBoxl_textExecuteNumberCourant.setMinimum(0.100000000000000)
        self.doubleSpinBoxl_textExecuteNumberCourant.setMaximum(1.000000000000000)
        self.doubleSpinBoxl_textExecuteNumberCourant.setSingleStep(0.100000000000000)
        self.doubleSpinBoxl_textExecuteNumberCourant.setValue(0.500000000000000)
        self.doubleSpinBoxl_textExecuteNumberCourant.setProperty(u"QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxl_textExecuteNumberCourant)

        self.label_texExcute_8 = QLabel(self.frame_Execute2)
        self.label_texExcute_8.setObjectName(u"label_texExcute_8")
        self.label_texExcute_8.setMinimumSize(QSize(110, 0))
        self.label_texExcute_8.setProperty(u"QLabelStyle", 3)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_texExcute_8)

        self.doubleSpinBoxl_textExecuteTimeAnalysis = QDoubleSpinBox(self.frame_Execute2)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setObjectName(u"doubleSpinBoxl_textExecuteTimeAnalysis")
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setEnabled(True)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setDecimals(2)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMinimum(0.100000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setMaximum(100.000000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setStepType(QAbstractSpinBox.StepType.DefaultStepType)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setValue(2.000000000000000)
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setProperty(u"QDoubleSpinBoxStyle", 1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxl_textExecuteTimeAnalysis)

        self.label_texExcute_10 = QLabel(self.frame_Execute2)
        self.label_texExcute_10.setObjectName(u"label_texExcute_10")
        self.label_texExcute_10.setMinimumSize(QSize(110, 0))
        self.label_texExcute_10.setProperty(u"QLabelStyle", 3)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_texExcute_10)

        self.doubleSpinBoxl_textExecuteFps = QSpinBox(self.frame_Execute2)
        self.doubleSpinBoxl_textExecuteFps.setObjectName(u"doubleSpinBoxl_textExecuteFps")
        self.doubleSpinBoxl_textExecuteFps.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textExecuteFps.setMinimum(1)
        self.doubleSpinBoxl_textExecuteFps.setMaximum(1000)
        self.doubleSpinBoxl_textExecuteFps.setSingleStep(1)
        self.doubleSpinBoxl_textExecuteFps.setValue(30)
        self.doubleSpinBoxl_textExecuteFps.setDisplayIntegerBase(10)
        self.doubleSpinBoxl_textExecuteFps.setProperty(u"QSpinBoxStyle", 1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxl_textExecuteFps)

        self.groupBox = QGroupBox(self.frame_Execute2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"color: rgb(198, 198, 198);")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_texExcuteStepAnalysis = QLabel(self.frame)
        self.label_texExcuteStepAnalysis.setObjectName(u"label_texExcuteStepAnalysis")
        self.label_texExcuteStepAnalysis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_texExcuteStepAnalysis, 0, 2, 1, 1)

        self.label_texExcuteDtAnalysis = QLabel(self.frame)
        self.label_texExcuteDtAnalysis.setObjectName(u"label_texExcuteDtAnalysis")
        self.label_texExcuteDtAnalysis.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_texExcuteDtAnalysis, 0, 1, 1, 1)

        self.label_texExcute_6 = QLabel(self.frame)
        self.label_texExcute_6.setObjectName(u"label_texExcute_6")
        self.label_texExcute_6.setMinimumSize(QSize(0, 0))
        self.label_texExcute_6.setWordWrap(True)
        self.label_texExcute_6.setProperty(u"QLabelStyle", 3)

        self.gridLayout.addWidget(self.label_texExcute_6, 0, 0, 1, 1)

        self.label_texExcute_7 = QLabel(self.frame)
        self.label_texExcute_7.setObjectName(u"label_texExcute_7")
        self.label_texExcute_7.setMinimumSize(QSize(0, 0))
        self.label_texExcute_7.setWordWrap(True)
        self.label_texExcute_7.setProperty(u"QLabelStyle", 3)

        self.gridLayout.addWidget(self.label_texExcute_7, 1, 0, 1, 1)

        self.label_texExcuteDtGraphic = QLabel(self.frame)
        self.label_texExcuteDtGraphic.setObjectName(u"label_texExcuteDtGraphic")
        self.label_texExcuteDtGraphic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_texExcuteDtGraphic, 1, 1, 1, 1)

        self.label_texExcuteStepGraphic = QLabel(self.frame)
        self.label_texExcuteStepGraphic.setObjectName(u"label_texExcuteStepGraphic")
        self.label_texExcuteStepGraphic.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_texExcuteStepGraphic, 1, 2, 1, 1)


        self.verticalLayout_7.addWidget(self.frame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_texExcute_11 = QLabel(self.groupBox)
        self.label_texExcute_11.setObjectName(u"label_texExcute_11")
        self.label_texExcute_11.setMinimumSize(QSize(110, 0))
        self.label_texExcute_11.setScaledContents(False)
        self.label_texExcute_11.setWordWrap(True)
        self.label_texExcute_11.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_4.addWidget(self.label_texExcute_11)

        self.label_texExcuteProperty = QLabel(self.groupBox)
        self.label_texExcuteProperty.setObjectName(u"label_texExcuteProperty")
        self.label_texExcuteProperty.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_texExcuteProperty)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_texExcute_9 = QLabel(self.groupBox)
        self.label_texExcute_9.setObjectName(u"label_texExcute_9")
        self.label_texExcute_9.setMinimumSize(QSize(110, 0))
        self.label_texExcute_9.setScaledContents(False)
        self.label_texExcute_9.setWordWrap(True)
        self.label_texExcute_9.setProperty(u"QLabelStyle", 3)

        self.horizontalLayout_3.addWidget(self.label_texExcute_9)

        self.label_texExcuteVelocityCp = QLabel(self.groupBox)
        self.label_texExcuteVelocityCp.setObjectName(u"label_texExcuteVelocityCp")
        self.label_texExcuteVelocityCp.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_texExcuteVelocityCp)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)


        self.formLayout.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.groupBox)


        self.verticalLayout_5.addWidget(self.frame_Execute2)

        self.frame_ExecuteSubTitle3 = QFrame(self.frame_info)
        self.frame_ExecuteSubTitle3.setObjectName(u"frame_ExecuteSubTitle3")
        self.frame_ExecuteSubTitle3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ExecuteSubTitle3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_ExecuteSubTitle3)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(10, 0, 0, 0)
        self.checkBox_ExecuteAnalysisCE = QCheckBox(self.frame_ExecuteSubTitle3)
        self.checkBox_ExecuteAnalysisCE.setObjectName(u"checkBox_ExecuteAnalysisCE")
        self.checkBox_ExecuteAnalysisCE.setChecked(True)
        self.checkBox_ExecuteAnalysisCE.setProperty(u"QCheckBoxStyle", 2)

        self.horizontalLayout_18.addWidget(self.checkBox_ExecuteAnalysisCE)

        self.label_cardExecuteSubTitle3 = QLabel(self.frame_ExecuteSubTitle3)
        self.label_cardExecuteSubTitle3.setObjectName(u"label_cardExecuteSubTitle3")
        self.label_cardExecuteSubTitle3.setMinimumSize(QSize(262, 0))
        self.label_cardExecuteSubTitle3.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_18.addWidget(self.label_cardExecuteSubTitle3)

        self.toolButton_cardExecuteSubTitle3 = QToolButton(self.frame_ExecuteSubTitle3)
        self.toolButton_cardExecuteSubTitle3.setObjectName(u"toolButton_cardExecuteSubTitle3")
        self.toolButton_cardExecuteSubTitle3.setIcon(icon1)
        self.toolButton_cardExecuteSubTitle3.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardExecuteSubTitle3.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_18.addWidget(self.toolButton_cardExecuteSubTitle3)


        self.verticalLayout_5.addWidget(self.frame_ExecuteSubTitle3)

        self.frame_Execute3 = QFrame(self.frame_info)
        self.frame_Execute3.setObjectName(u"frame_Execute3")
        self.frame_Execute3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Execute3.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_Execute3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(9)
        self.formLayout_2.setVerticalSpacing(9)
        self.label_ExecuteAnalysisCE1 = QLabel(self.frame_Execute3)
        self.label_ExecuteAnalysisCE1.setObjectName(u"label_ExecuteAnalysisCE1")
        self.label_ExecuteAnalysisCE1.setMinimumSize(QSize(65, 0))
        self.label_ExecuteAnalysisCE1.setProperty(u"QLabelStyle", 3)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_ExecuteAnalysisCE1)

        self.lineEdit_ExecuteAnalysisCE_dincre = QLineEdit(self.frame_Execute3)
        self.lineEdit_ExecuteAnalysisCE_dincre.setObjectName(u"lineEdit_ExecuteAnalysisCE_dincre")
        self.lineEdit_ExecuteAnalysisCE_dincre.setEnabled(False)
        self.lineEdit_ExecuteAnalysisCE_dincre.setMinimumSize(QSize(50, 25))
        self.lineEdit_ExecuteAnalysisCE_dincre.setProperty(u"QLineEditStyle", 1)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_ExecuteAnalysisCE_dincre)

        self.label_ExecuteAnalysisCE2 = QLabel(self.frame_Execute3)
        self.label_ExecuteAnalysisCE2.setObjectName(u"label_ExecuteAnalysisCE2")
        self.label_ExecuteAnalysisCE2.setMinimumSize(QSize(65, 0))
        self.label_ExecuteAnalysisCE2.setProperty(u"QLabelStyle", 3)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_ExecuteAnalysisCE2)

        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre = QSpinBox(self.frame_Execute3)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setObjectName(u"doubleSpinBoxl_ExecuteAnalysisCE_noIncre")
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setEnabled(False)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setMinimum(1)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setMaximum(10000)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setSingleStep(1)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setValue(1)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setDisplayIntegerBase(10)
        self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre.setProperty(u"QSpinBoxStyle", 1)

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxl_ExecuteAnalysisCE_noIncre)

        self.label_ExecuteAnalysisCE1_2 = QLabel(self.frame_Execute3)
        self.label_ExecuteAnalysisCE1_2.setObjectName(u"label_ExecuteAnalysisCE1_2")
        self.label_ExecuteAnalysisCE1_2.setMinimumSize(QSize(65, 0))
        self.label_ExecuteAnalysisCE1_2.setProperty(u"QLabelStyle", 3)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_ExecuteAnalysisCE1_2)

        self.lineEdit_ExecuteAnalysisCE_dincreGrav = QLineEdit(self.frame_Execute3)
        self.lineEdit_ExecuteAnalysisCE_dincreGrav.setObjectName(u"lineEdit_ExecuteAnalysisCE_dincreGrav")
        self.lineEdit_ExecuteAnalysisCE_dincreGrav.setEnabled(False)
        self.lineEdit_ExecuteAnalysisCE_dincreGrav.setMinimumSize(QSize(50, 25))
        self.lineEdit_ExecuteAnalysisCE_dincreGrav.setProperty(u"QLineEditStyle", 1)

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit_ExecuteAnalysisCE_dincreGrav)


        self.verticalLayout_5.addWidget(self.frame_Execute3)

        self.frame_ExecuteSubTitle1 = QFrame(self.frame_info)
        self.frame_ExecuteSubTitle1.setObjectName(u"frame_ExecuteSubTitle1")
        self.frame_ExecuteSubTitle1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ExecuteSubTitle1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ExecuteSubTitle1)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardExecuteSubTitle1 = QLabel(self.frame_ExecuteSubTitle1)
        self.label_cardExecuteSubTitle1.setObjectName(u"label_cardExecuteSubTitle1")
        self.label_cardExecuteSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardExecuteSubTitle1.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardExecuteSubTitle1)

        self.toolButton_cardExecuteSubTitle1 = QToolButton(self.frame_ExecuteSubTitle1)
        self.toolButton_cardExecuteSubTitle1.setObjectName(u"toolButton_cardExecuteSubTitle1")
        self.toolButton_cardExecuteSubTitle1.setIcon(icon1)
        self.toolButton_cardExecuteSubTitle1.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardExecuteSubTitle1.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardExecuteSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_ExecuteSubTitle1)

        self.frame_Execute1 = QFrame(self.frame_info)
        self.frame_Execute1.setObjectName(u"frame_Execute1")
        self.frame_Execute1.setStyleSheet(u"")
        self.frame_Execute1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_Execute1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_Execute1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_textBoundary1 = QLabel(self.frame_Execute1)
        self.label_textBoundary1.setObjectName(u"label_textBoundary1")
        self.label_textBoundary1.setMinimumSize(QSize(110, 0))
        self.label_textBoundary1.setProperty(u"QLabelStyle", 3)

        self.verticalLayout.addWidget(self.label_textBoundary1)

        self.frame_8 = QFrame(self.frame_Execute1)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy5)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.listWidget_execute_pointMaterialFrom = QListWidget(self.frame_8)
        self.listWidget_execute_pointMaterialFrom.setObjectName(u"listWidget_execute_pointMaterialFrom")
        self.listWidget_execute_pointMaterialFrom.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialFrom.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialFrom.setSpacing(3)
        self.listWidget_execute_pointMaterialFrom.setProperty(u"QListWidgetStyle", 1)

        self.horizontalLayout_22.addWidget(self.listWidget_execute_pointMaterialFrom)

        self.listWidget_execute_pointMaterialTo = QListWidget(self.frame_8)
        self.listWidget_execute_pointMaterialTo.setObjectName(u"listWidget_execute_pointMaterialTo")
        self.listWidget_execute_pointMaterialTo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialTo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_pointMaterialTo.setSpacing(3)
        self.listWidget_execute_pointMaterialTo.setProperty(u"QListWidgetStyle", 1)
        self.listWidget_execute_pointMaterialTo.setProperty(u"QListWidgetItemStyle", 2)

        self.horizontalLayout_22.addWidget(self.listWidget_execute_pointMaterialTo)

        self.listWidget_execute_pointMaterialTo.raise_()
        self.listWidget_execute_pointMaterialFrom.raise_()

        self.verticalLayout.addWidget(self.frame_8)

        self.label_textBoundary3 = QLabel(self.frame_Execute1)
        self.label_textBoundary3.setObjectName(u"label_textBoundary3")
        self.label_textBoundary3.setMinimumSize(QSize(110, 0))
        self.label_textBoundary3.setProperty(u"QLabelStyle", 3)

        self.verticalLayout.addWidget(self.label_textBoundary3)

        self.frame_9 = QFrame(self.frame_Execute1)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy6)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_23.setSpacing(5)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.listWidget_execute_boundariesFrom = QListWidget(self.frame_9)
        self.listWidget_execute_boundariesFrom.setObjectName(u"listWidget_execute_boundariesFrom")
        self.listWidget_execute_boundariesFrom.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesFrom.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesFrom.setSpacing(3)
        self.listWidget_execute_boundariesFrom.setProperty(u"QListWidgetStyle", 1)

        self.horizontalLayout_23.addWidget(self.listWidget_execute_boundariesFrom)

        self.listWidget_execute_boundariesTo = QListWidget(self.frame_9)
        self.listWidget_execute_boundariesTo.setObjectName(u"listWidget_execute_boundariesTo")
        self.listWidget_execute_boundariesTo.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesTo.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.listWidget_execute_boundariesTo.setSpacing(3)
        self.listWidget_execute_boundariesTo.setProperty(u"QListWidgetStyle", 1)
        self.listWidget_execute_boundariesTo.setProperty(u"QListWidgetItemStyle", 2)

        self.horizontalLayout_23.addWidget(self.listWidget_execute_boundariesTo)


        self.verticalLayout.addWidget(self.frame_9)


        self.verticalLayout_5.addWidget(self.frame_Execute1)

        self.toolButton_ExecuteStages = QToolButton(self.frame_info)
        self.toolButton_ExecuteStages.setObjectName(u"toolButton_ExecuteStages")
        self.toolButton_ExecuteStages.setMinimumSize(QSize(180, 0))
        self.toolButton_ExecuteStages.setMaximumSize(QSize(200, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"../resources/iconos/iconos_analisis/excute.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_ExecuteStages.setIcon(icon2)
        self.toolButton_ExecuteStages.setIconSize(QSize(30, 30))
        self.toolButton_ExecuteStages.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_ExecuteStages.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_ExecuteStages.setAutoRaise(False)
        self.toolButton_ExecuteStages.setArrowType(Qt.ArrowType.RightArrow)
        self.toolButton_ExecuteStages.setProperty(u"QToolButtonStyle", 9)

        self.verticalLayout_5.addWidget(self.toolButton_ExecuteStages)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.verticalLayout_5.addLayout(self.verticalLayout_6)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.toolButton_Execute = QToolButton(self.frame_info)
        self.toolButton_Execute.setObjectName(u"toolButton_Execute")
        self.toolButton_Execute.setMinimumSize(QSize(180, 0))
        self.toolButton_Execute.setMaximumSize(QSize(200, 16777215))
        self.toolButton_Execute.setIcon(icon2)
        self.toolButton_Execute.setIconSize(QSize(30, 30))
        self.toolButton_Execute.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.toolButton_Execute.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        self.toolButton_Execute.setAutoRaise(False)
        self.toolButton_Execute.setArrowType(Qt.ArrowType.RightArrow)
        self.toolButton_Execute.setProperty(u"QToolButtonStyle", 9)

        self.horizontalLayout_8.addWidget(self.toolButton_Execute)


        self.verticalLayout_5.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msn = QLabel(self.frame_info)
        self.label_msn.setObjectName(u"label_msn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_msn.sizePolicy().hasHeightForWidth())
        self.label_msn.setSizePolicy(sizePolicy7)
        self.label_msn.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.label_cardExecuteSubTitle2.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Tiempo cr\u00edtico", None))
        self.toolButton_cardExecuteSubTitle2.setText("")
        self.label_texExcute_5.setText(QCoreApplication.translate("FormDrawMenuExecute", u"N\u00famero de Courant (C):", None))
        self.doubleSpinBoxl_textExecuteNumberCourant.setSuffix("")
        self.label_texExcute_8.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Tiempo de an\u00e1lisis :", None))
        self.doubleSpinBoxl_textExecuteTimeAnalysis.setSuffix("")
        self.label_texExcute_10.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Fps:", None))
        self.groupBox.setTitle(QCoreApplication.translate("FormDrawMenuExecute", u"Resultados", None))
        self.label_texExcuteStepAnalysis.setText(QCoreApplication.translate("FormDrawMenuExecute", u"0pasos", None))
        self.label_texExcuteDtAnalysis.setText(QCoreApplication.translate("FormDrawMenuExecute", u"0.00s", None))
        self.label_texExcute_6.setText(QCoreApplication.translate("FormDrawMenuExecute", u"<html><head/><body><p>\u0394<span style=\" font-size:11pt;\">t</span><span style=\" font-size:11pt; vertical-align:sub;\">(An\u00e1lisis):</span></p></body></html>", None))
        self.label_texExcute_7.setText(QCoreApplication.translate("FormDrawMenuExecute", u"<html><head/><body><p>\u0394<span style=\" font-size:11pt;\">t</span><span style=\" font-size:11pt; vertical-align:sub;\">(Graficar)</span><span style=\" font-size:11pt;\">:</span></p></body></html>", None))
        self.label_texExcuteDtGraphic.setText(QCoreApplication.translate("FormDrawMenuExecute", u"0.00s", None))
        self.label_texExcuteStepGraphic.setText(QCoreApplication.translate("FormDrawMenuExecute", u"0Pasos", None))
        self.label_texExcute_11.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Valores m\u00ednimos para el material:", None))
        self.label_texExcuteProperty.setText(QCoreApplication.translate("FormDrawMenuExecute", u"-/-", None))
        self.label_texExcute_9.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Velocidad m\u00e1xima del sonido en el material (Cp):", None))
        self.label_texExcuteVelocityCp.setText(QCoreApplication.translate("FormDrawMenuExecute", u"0.00m/s", None))
        self.checkBox_ExecuteAnalysisCE.setText("")
        self.label_cardExecuteSubTitle3.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Condici\u00f3n  cuasi-est\u00e1tica ", None))
        self.toolButton_cardExecuteSubTitle3.setText("")
        self.label_ExecuteAnalysisCE1.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Incremento Carga [kN/m]:", None))
        self.lineEdit_ExecuteAnalysisCE_dincre.setText(QCoreApplication.translate("FormDrawMenuExecute", u"1.0", None))
        self.label_ExecuteAnalysisCE2.setText(QCoreApplication.translate("FormDrawMenuExecute", u"No incrementos:", None))
        self.label_ExecuteAnalysisCE1_2.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Increm. Gravedad [m/s2]:", None))
        self.lineEdit_ExecuteAnalysisCE_dincreGrav.setText(QCoreApplication.translate("FormDrawMenuExecute", u"1.0", None))
        self.label_cardExecuteSubTitle1.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Datos", None))
        self.toolButton_cardExecuteSubTitle1.setText("")
        self.label_textBoundary1.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Puntos materiales", None))
        self.label_textBoundary3.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Contornos:", None))
        self.toolButton_ExecuteStages.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Ejecutar etapas", None))
        self.toolButton_Execute.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Ejecutar An\u00e1lisis", None))
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuExecute", u"Empty", None))
    # retranslateUi

