# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_result_menu_graphYhEDCx.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QRadioButton,
    QScrollArea, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormMenuResultGraph(object):
    def setupUi(self, FormMenuResultGraph):
        if not FormMenuResultGraph.objectName():
            FormMenuResultGraph.setObjectName(u"FormMenuResultGraph")
        FormMenuResultGraph.resize(350, 766)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormMenuResultGraph.sizePolicy().hasHeightForWidth())
        FormMenuResultGraph.setSizePolicy(sizePolicy)
        FormMenuResultGraph.setMinimumSize(QSize(0, 0))
        FormMenuResultGraph.setMaximumSize(QSize(350, 16777215))
        FormMenuResultGraph.setStyleSheet(u"/*Colores primarios*/\n"
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
"\n"
"\n"
"QFrame#frame_ResultAnimationProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"/*###"
                        "##############################################################*/\n"
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
"/*####################       FRAME ResultAnimation       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_ResultAnimation{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardMeshTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_ResultAnimationSubTitle0,\n"
""
                        "QFrame#frame_ResultAnimationSubTitle1,\n"
"QFrame#frame_ResultAnimationSubTitle2,\n"
"QFrame#frame_ResultAnimationSubTitle3{\n"
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
"QToolButton#toolButton_cardResultAnimationDraw7,\n"
"QToolButton#toolButton_cardResultAnimationDraw5,\n"
"QToolButton#toolButton_cardResultAnimationDraw6{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"\n"
"QToolButton#toolButton_cardResultAnimationDraw7:hover,\n"
"QToolButton#toolButton_cardResultAnimationDraw5:hover, \n"
"QToolButton#toolButton_cardResultAnimationDraw6:hover{ \n"
"background-color: #444444;\n"
""
                        "}\n"
"QToolButton#toolButton_cardResultAnimationDraw7:pressed,\n"
"QToolButton#toolButton_cardResultAnimationDraw5:pressed,\n"
"QToolButton#toolButton_cardResultAnimationDraw6:pressed{\n"
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
"#verticalLayout_containerCardResultAnimation,\n"
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
"/*###################### "
                        "     SCROLL BAR    VERTICAL  ############################*/\n"
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
"\n"
"\n"
"/*BOTTON*/\n"
"QScrollBar::add-line:vertical{\n"
"    background"
                        "-color: #444444;\n"
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
"QScrollBar::handle:horizontal:hover {\n"
"    background-color"
                        ": #777777;\n"
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
"QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:"
                        "horizontal{\n"
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
"\n"
"QGroupBox{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"padding-top: 8px;\n"
"border: 1px solid #666666;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"\n"
"\n"
"QToolButton[QToolButtonStyle=\"0\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 1px;\n"
""
                        "}\n"
"\n"
"QToolButton[QToolButtonStyle=\"0\"]:hover{ \n"
"background-color: #444444;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"0\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
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
""
                        "\n"
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton - Habilitado           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QToolButton[QToolButtonStyle=\"2\"] {\n"
"    font: 500 10pt \"Ubuntu\";\n"
"    color: #222222;\n"
"    background-color: #77ACA2;\n"
"    border: none;\n"
"    padding: 6px 25px;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"2\"]:hover {\n"
"    background-color: #36C9C6;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"2\"]:enabled {\n"
"    /* Estilos adicionales cuando el QToolButton est\u00e1 habilitado */\n"
"    background-color: #77ACA2;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton - Deshabilitado           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QToolButton[QToolButtonStyle=\"2\"]:disabled {\n"
"    color: #888888;\n"
"    background-color: #444444;\n"
"    border: none;\n"
"}\n"
"\n"
"QToolButton[QToolButtonStyle=\"2\"]:disabled:hover {\n"
"    background-color: #444444;\n"
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
"    fon"
                        "t: 500 10pt \"Ubuntu\";    \n"
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
"	border-top-right-radius: "
                        "10px;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit - Habilitado           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QLineEdit[QLineEditStyle=\"1\"] {\n"
"    font: 9pt \"Ubuntu\";\n"
"    color: #DDDDDD;\n"
"    background-color: #444444;\n"
"    border-radius: 2px;\n"
"    padding-right: 6px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"1\"]:enabled {\n"
"    /* Estilos adicionale"
                        "s cuando el QLineEdit est\u00e1 habilitado */\n"
"    background-color: #444444;\n"
"    border: 1px solid #555555;\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"2\"] {\n"
"    font: 9pt \"Ubuntu\";\n"
"    color: #DDDDDD;\n"
"    background-color: #333333;\n"
"    border: 1px solid #444444;\n"
"    border-radius: 2px;\n"
"    padding-right: 6px;\n"
"    padding-left: 6px;\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"2\"]:enabled {\n"
"    /* Estilos adicionales cuando el QLineEdit est\u00e1 habilitado */\n"
"    background-color: #333333;\n"
"    border: 1px solid #444444;\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit - Deshabilitado           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QLineEdit[QLineEditStyle=\"1\"]:disabled {\n"
"    color: #888888;\n"
"    background-color: #333333;\n"
"    border: 1px solid #44444"
                        "4;\n"
"}\n"
"\n"
"QLineEdit[QLineEditStyle=\"2\"]:disabled {\n"
"    color: #888888;\n"
"    background-color: #222222;\n"
"    border: 1px solid #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"QLineEdit#lineEdit_textResultAnimation3{\n"
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
"QLineEdit#lineEdit_textResultAnimation3,\n"
"QLineEdit#lineEdit_textResultAnimation5{\n"
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
"QLabel[QLabelStyle=\"4\"] {\n"
"font: 900 25pt \"Ubuntu\";\n"
"color: #77ACA2;\n"
"}\n"
"QLabel[QLabelStyle=\"5\"] {\n"
"fo"
                        "nt: 300 8pt \"Ubuntu\";\n"
"color: #aaa;\n"
"}\n"
"\n"
"\n"
"/*Colores primarios*/\n"
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
""
                        "    color: white;\n"
"    selection-background-color: #808080;\n"
"    font: 700 9pt \"Ubuntu\";\n"
"}\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8           QRadioButton            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QRadioButton[QRadioButtonStyle=\"1\"] {    \n"
"    color: #DDDDDD;\n"
"    padding: 5px;\n"
"    font: 9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator {\n"
"    background-color: transparent;\n"
"    border: 1px solid #808080;\n"
"    border-radius: 50%; /* Se utiliza 50% para hacer el c\u00edrculo */\n"
"}\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator:checked {\n"
"    background-color: #F94646;\n"
"    border: none;\n"
"}\n"
"")
        self.formLayout = QFormLayout(FormMenuResultGraph)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_ResultAnimationProject = QFrame(FormMenuResultGraph)
        self.frame_ResultAnimationProject.setObjectName(u"frame_ResultAnimationProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimationProject.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimationProject.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimationProject.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimationProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ResultAnimationProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_ResultAnimationProject)
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

        self.frame_ResultAnimation = QFrame(self.frame_ResultAnimationProject)
        self.frame_ResultAnimation.setObjectName(u"frame_ResultAnimation")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_ResultAnimation)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_ResultAnimation)
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
        self.label_cardResultAnimationTitle = QLabel(self.frame_title)
        self.label_cardResultAnimationTitle.setObjectName(u"label_cardResultAnimationTitle")
        self.label_cardResultAnimationTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardResultAnimationTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_ResultAnimation)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_ResultAnimationSubTitle1 = QFrame(self.frame_info)
        self.frame_ResultAnimationSubTitle1.setObjectName(u"frame_ResultAnimationSubTitle1")
        self.frame_ResultAnimationSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimationSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_ResultAnimationSubTitle1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardResultAnimationSubTitle1 = QLabel(self.frame_ResultAnimationSubTitle1)
        self.label_cardResultAnimationSubTitle1.setObjectName(u"label_cardResultAnimationSubTitle1")
        self.label_cardResultAnimationSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardResultAnimationSubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardResultAnimationSubTitle1)

        self.toolButton_cardResultAnimationSubTitle1 = QToolButton(self.frame_ResultAnimationSubTitle1)
        self.toolButton_cardResultAnimationSubTitle1.setObjectName(u"toolButton_cardResultAnimationSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardResultAnimationSubTitle1.setIcon(icon1)
        self.toolButton_cardResultAnimationSubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardResultAnimationSubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardResultAnimationSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimationSubTitle1)

        self.frame_ResultAnimation1 = QFrame(self.frame_info)
        self.frame_ResultAnimation1.setObjectName(u"frame_ResultAnimation1")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation1.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation1.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation1.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimation1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_ResultAnimation1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_ResultAnimation1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_text_char1 = QLabel(self.frame_3)
        self.label_text_char1.setObjectName(u"label_text_char1")
        self.label_text_char1.setMinimumSize(QSize(0, 0))
        self.label_text_char1.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_text_char1)

        self.comboBox_chartTypeResult = QComboBox(self.frame_3)
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

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.comboBox_chartTypeResult)

        self.label_text_chart2 = QLabel(self.frame_3)
        self.label_text_chart2.setObjectName(u"label_text_chart2")
        self.label_text_chart2.setMinimumSize(QSize(85, 0))
        self.label_text_chart2.setMaximumSize(QSize(85, 16777215))
        self.label_text_chart2.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_text_chart2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_chartPointName = QLineEdit(self.frame_3)
        self.lineEdit_chartPointName.setObjectName(u"lineEdit_chartPointName")
        self.lineEdit_chartPointName.setMinimumSize(QSize(0, 25))
        self.lineEdit_chartPointName.setMaximumSize(QSize(200, 16777215))
        self.lineEdit_chartPointName.setProperty("QLineEditStyle", 1)

        self.horizontalLayout_8.addWidget(self.lineEdit_chartPointName)

        self.toolButton_chartAddPoint = QToolButton(self.frame_3)
        self.toolButton_chartAddPoint.setObjectName(u"toolButton_chartAddPoint")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/icono_result/add.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_chartAddPoint.setIcon(icon2)
        self.toolButton_chartAddPoint.setIconSize(QSize(20, 20))
        self.toolButton_chartAddPoint.setArrowType(Qt.NoArrow)
        self.toolButton_chartAddPoint.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_8.addWidget(self.toolButton_chartAddPoint)


        self.formLayout_2.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label_text_chart2_3 = QLabel(self.frame_3)
        self.label_text_chart2_3.setObjectName(u"label_text_chart2_3")
        self.label_text_chart2_3.setMinimumSize(QSize(85, 0))
        self.label_text_chart2_3.setMaximumSize(QSize(85, 16777215))
        self.label_text_chart2_3.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_text_chart2_3)

        self.toolButton_chartTypeStyle = QToolButton(self.frame_3)
        self.toolButton_chartTypeStyle.setObjectName(u"toolButton_chartTypeStyle")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.toolButton_chartTypeStyle.sizePolicy().hasHeightForWidth())
        self.toolButton_chartTypeStyle.setSizePolicy(sizePolicy5)
        self.toolButton_chartTypeStyle.setMinimumSize(QSize(35, 25))
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/icono_result/graphics.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_chartTypeStyle.setIcon(icon3)
        self.toolButton_chartTypeStyle.setIconSize(QSize(30, 15))
        self.toolButton_chartTypeStyle.setProperty("QToolButtonStyle", 0)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.toolButton_chartTypeStyle)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.label_text_chart2_2 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart2_2.setObjectName(u"label_text_chart2_2")
        self.label_text_chart2_2.setMinimumSize(QSize(0, 0))
        self.label_text_chart2_2.setMaximumSize(QSize(16777215, 16777215))
        self.label_text_chart2_2.setTextFormat(Qt.PlainText)
        self.label_text_chart2_2.setScaledContents(True)
        self.label_text_chart2_2.setAlignment(Qt.AlignCenter)
        self.label_text_chart2_2.setWordWrap(True)
        self.label_text_chart2_2.setProperty("QLabelStyle", 5)

        self.verticalLayout_6.addWidget(self.label_text_chart2_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 15, -1, 10)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.radioButton_manual = QRadioButton(self.frame_ResultAnimation1)
        self.radioButton_manual.setObjectName(u"radioButton_manual")
        self.radioButton_manual.setProperty("QRadioButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.radioButton_manual)

        self.radioButton_automatic = QRadioButton(self.frame_ResultAnimation1)
        self.radioButton_automatic.setObjectName(u"radioButton_automatic")
        self.radioButton_automatic.setChecked(True)
        self.radioButton_automatic.setProperty("QRadioButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.radioButton_automatic)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.label_text_chart5_7 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_7.setObjectName(u"label_text_chart5_7")
        self.label_text_chart5_7.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_7.setProperty("QLabelStyle", 3)

        self.verticalLayout_7.addWidget(self.label_text_chart5_7)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_6.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_6.setHorizontalSpacing(10)
        self.formLayout_6.setVerticalSpacing(10)
        self.formLayout_6.setContentsMargins(10, 10, 10, 10)
        self.label_text_chart5_11 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_11.setObjectName(u"label_text_chart5_11")
        self.label_text_chart5_11.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_11.setProperty("QLabelStyle", 3)

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.label_text_chart5_11)

        self.label_text_chart5_12 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_12.setObjectName(u"label_text_chart5_12")
        self.label_text_chart5_12.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_12.setProperty("QLabelStyle", 3)

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.label_text_chart5_12)

        self.lineEdit_Xmin = QLineEdit(self.frame_ResultAnimation1)
        self.lineEdit_Xmin.setObjectName(u"lineEdit_Xmin")
        self.lineEdit_Xmin.setEnabled(False)
        self.lineEdit_Xmin.setMinimumSize(QSize(0, 25))
        self.lineEdit_Xmin.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_Xmin.setProperty("QLineEditStyle", 1)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Xmin)

        self.lineEdit_Xmax = QLineEdit(self.frame_ResultAnimation1)
        self.lineEdit_Xmax.setObjectName(u"lineEdit_Xmax")
        self.lineEdit_Xmax.setEnabled(False)
        self.lineEdit_Xmax.setMinimumSize(QSize(0, 25))
        self.lineEdit_Xmax.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_Xmax.setProperty("QLineEditStyle", 1)

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Xmax)


        self.verticalLayout_7.addLayout(self.formLayout_6)

        self.label_text_chart5_10 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_10.setObjectName(u"label_text_chart5_10")
        self.label_text_chart5_10.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_10.setProperty("QLabelStyle", 3)

        self.verticalLayout_7.addWidget(self.label_text_chart5_10)

        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setHorizontalSpacing(10)
        self.formLayout_7.setVerticalSpacing(10)
        self.formLayout_7.setContentsMargins(10, 10, 10, 10)
        self.lineEdit_Ymax = QLineEdit(self.frame_ResultAnimation1)
        self.lineEdit_Ymax.setObjectName(u"lineEdit_Ymax")
        self.lineEdit_Ymax.setEnabled(False)
        self.lineEdit_Ymax.setMinimumSize(QSize(0, 25))
        self.lineEdit_Ymax.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_Ymax.setProperty("QLineEditStyle", 1)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.lineEdit_Ymax)

        self.lineEdit_Ymin = QLineEdit(self.frame_ResultAnimation1)
        self.lineEdit_Ymin.setObjectName(u"lineEdit_Ymin")
        self.lineEdit_Ymin.setEnabled(False)
        self.lineEdit_Ymin.setMinimumSize(QSize(0, 25))
        self.lineEdit_Ymin.setMaximumSize(QSize(120, 16777215))
        self.lineEdit_Ymin.setProperty("QLineEditStyle", 1)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.lineEdit_Ymin)

        self.label_text_chart5_14 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_14.setObjectName(u"label_text_chart5_14")
        self.label_text_chart5_14.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_14.setProperty("QLabelStyle", 3)

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_text_chart5_14)

        self.label_text_chart5_13 = QLabel(self.frame_ResultAnimation1)
        self.label_text_chart5_13.setObjectName(u"label_text_chart5_13")
        self.label_text_chart5_13.setMinimumSize(QSize(110, 0))
        self.label_text_chart5_13.setProperty("QLabelStyle", 3)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_text_chart5_13)


        self.verticalLayout_7.addLayout(self.formLayout_7)


        self.verticalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.toolButton_updateLimit = QToolButton(self.frame_ResultAnimation1)
        self.toolButton_updateLimit.setObjectName(u"toolButton_updateLimit")
        self.toolButton_updateLimit.setEnabled(True)
        self.toolButton_updateLimit.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_6.addWidget(self.toolButton_updateLimit)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation1)

        self.frame_ResultAnimationSubTitle0 = QFrame(self.frame_info)
        self.frame_ResultAnimationSubTitle0.setObjectName(u"frame_ResultAnimationSubTitle0")
        self.frame_ResultAnimationSubTitle0.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimationSubTitle0.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ResultAnimationSubTitle0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_textResultAnimation1_2 = QLabel(self.frame_ResultAnimationSubTitle0)
        self.label_textResultAnimation1_2.setObjectName(u"label_textResultAnimation1_2")
        self.label_textResultAnimation1_2.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_2.setProperty("QLabelStyle", 3)

        self.horizontalLayout_16.addWidget(self.label_textResultAnimation1_2)

        self.toolButton_deleteSeries = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_deleteSeries.setObjectName(u"toolButton_deleteSeries")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_deleteSeries.setIcon(icon4)
        self.toolButton_deleteSeries.setArrowType(Qt.NoArrow)
        self.toolButton_deleteSeries.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_deleteSeries)

        self.toolButton_showHideLabel = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_showHideLabel.setObjectName(u"toolButton_showHideLabel")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideLabel.setIcon(icon5)
        self.toolButton_showHideLabel.setArrowType(Qt.NoArrow)
        self.toolButton_showHideLabel.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_showHideLabel)

        self.toolButton_showHideSeries = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_showHideSeries.setObjectName(u"toolButton_showHideSeries")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideSeries.setIcon(icon6)
        self.toolButton_showHideSeries.setArrowType(Qt.NoArrow)
        self.toolButton_showHideSeries.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_showHideSeries)

        self.toolButton_cardResultAnimationSubTitle0 = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_cardResultAnimationSubTitle0.setObjectName(u"toolButton_cardResultAnimationSubTitle0")
        self.toolButton_cardResultAnimationSubTitle0.setIcon(icon1)
        self.toolButton_cardResultAnimationSubTitle0.setArrowType(Qt.NoArrow)
        self.toolButton_cardResultAnimationSubTitle0.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardResultAnimationSubTitle0)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimationSubTitle0)

        self.frame_ResultAnimation3 = QFrame(self.frame_info)
        self.frame_ResultAnimation3.setObjectName(u"frame_ResultAnimation3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_ResultAnimation3.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation3.setSizePolicy(sizePolicy6)
        self.frame_ResultAnimation3.setMinimumSize(QSize(0, 150))
        self.frame_ResultAnimation3.setStyleSheet(u"")
        self.frame_ResultAnimation3.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimation3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_ResultAnimation3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_ResultAnimation3)
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
        self.verticalLayout_containerCardPoint = QVBoxLayout()
        self.verticalLayout_containerCardPoint.setSpacing(0)
        self.verticalLayout_containerCardPoint.setObjectName(u"verticalLayout_containerCardPoint")
        self.frame_empty = QFrame(self.scrollAreaWidgetContents)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy6.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy6)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.verticalLayout_containerCardPoint.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardPoint)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation3)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

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


        self.horizontalLayout.addWidget(self.frame_ResultAnimation)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_ResultAnimationProject)


        self.retranslateUi(FormMenuResultGraph)

        QMetaObject.connectSlotsByName(FormMenuResultGraph)
    # setupUi

    def retranslateUi(self, FormMenuResultGraph):
        FormMenuResultGraph.setWindowTitle(QCoreApplication.translate("FormMenuResultGraph", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardResultAnimationTitle.setText(QCoreApplication.translate("FormMenuResultGraph", u"GR\u00c1FICAS", None))
        self.label_cardResultAnimationSubTitle1.setText(QCoreApplication.translate("FormMenuResultGraph", u"Datos de visualizaci\u00f3n", None))
        self.toolButton_cardResultAnimationSubTitle1.setText("")
        self.label_text_char1.setText(QCoreApplication.translate("FormMenuResultGraph", u"Graficar:", None))
        self.comboBox_chartTypeResult.setItemText(0, QCoreApplication.translate("FormMenuResultGraph", u"Coordenada X", None))
        self.comboBox_chartTypeResult.setItemText(1, QCoreApplication.translate("FormMenuResultGraph", u"Coordenada Y", None))
        self.comboBox_chartTypeResult.setItemText(2, QCoreApplication.translate("FormMenuResultGraph", u"sigxx", None))
        self.comboBox_chartTypeResult.setItemText(3, QCoreApplication.translate("FormMenuResultGraph", u"sigyy", None))
        self.comboBox_chartTypeResult.setItemText(4, QCoreApplication.translate("FormMenuResultGraph", u"sigxy", None))
        self.comboBox_chartTypeResult.setItemText(5, QCoreApplication.translate("FormMenuResultGraph", u"epsxx", None))
        self.comboBox_chartTypeResult.setItemText(6, QCoreApplication.translate("FormMenuResultGraph", u"epsyy", None))
        self.comboBox_chartTypeResult.setItemText(7, QCoreApplication.translate("FormMenuResultGraph", u"epsxy", None))

        self.label_text_chart2.setText(QCoreApplication.translate("FormMenuResultGraph", u"Punto material:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_chartPointName.setToolTip(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Puede buscar por id como 1 o 2 o 3 etc. O por conjuntos separados por coma, por ejemplo 1,2,3\u2026</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_chartPointName.setText("")
        self.lineEdit_chartPointName.setPlaceholderText(QCoreApplication.translate("FormMenuResultGraph", u"id puntos", None))
        self.toolButton_chartAddPoint.setText("")
        self.label_text_chart2_3.setText(QCoreApplication.translate("FormMenuResultGraph", u"Tipo de gr\u00e1fica", None))
        self.toolButton_chartTypeStyle.setText("")
        self.label_text_chart2_2.setText(QCoreApplication.translate("FormMenuResultGraph", u"NOTA: los puntos materiales se pueden seleccionar, por id como 1 o 2 o 3 etc. Por conjuntos de ids separados por coma, por ejemplo 1,2,3\u2026 o por rangos de ids separados por dos puntos ejemplo 5:10", None))
        self.radioButton_manual.setText(QCoreApplication.translate("FormMenuResultGraph", u"Manual", None))
        self.radioButton_automatic.setText(QCoreApplication.translate("FormMenuResultGraph", u"Autom\u00e1tico", None))
        self.label_text_chart5_7.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>L\u00edmites eje x</p></body></html>", None))
        self.label_text_chart5_11.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>M\u00ednimo:</p></body></html>", None))
        self.label_text_chart5_12.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>M\u00e1ximo:</p></body></html>", None))
        self.label_text_chart5_10.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>L\u00edmites eje y</p></body></html>", None))
        self.label_text_chart5_14.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>M\u00e1ximo:</p></body></html>", None))
        self.label_text_chart5_13.setText(QCoreApplication.translate("FormMenuResultGraph", u"<html><head/><body><p>M\u00ednimo:</p></body></html>", None))
        self.toolButton_updateLimit.setText(QCoreApplication.translate("FormMenuResultGraph", u"Actualizar l\u00edmites", None))
        self.label_textResultAnimation1_2.setText(QCoreApplication.translate("FormMenuResultGraph", u"Estilos de colores:", None))
        self.toolButton_deleteSeries.setText("")
        self.toolButton_showHideLabel.setText("")
        self.toolButton_showHideSeries.setText("")
        self.toolButton_cardResultAnimationSubTitle0.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormMenuResultGraph", u"Empty", None))
    # retranslateUi

