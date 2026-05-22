# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_result_menu_animationhDMrsB.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormMenuResultAnimation(object):
    def setupUi(self, FormMenuResultAnimation):
        if not FormMenuResultAnimation.objectName():
            FormMenuResultAnimation.setObjectName(u"FormMenuResultAnimation")
        FormMenuResultAnimation.resize(350, 941)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormMenuResultAnimation.sizePolicy().hasHeightForWidth())
        FormMenuResultAnimation.setSizePolicy(sizePolicy)
        FormMenuResultAnimation.setMinimumSize(QSize(0, 0))
        FormMenuResultAnimation.setMaximumSize(QSize(350, 16777215))
        FormMenuResultAnimation.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFram"
                        "e#frame_info,\n"
"QFrame#frame_ResultAnimation0,\n"
"QFrame#frame_ResultAnimation1,\n"
"QFrame#frame_3,\n"
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
"/*####################       FRAME ResultAnimation       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_ResultAnimation{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;"
                        "\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardMeshTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_ResultAnimationSubTitle0,\n"
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
"QToolButton#toolButton_closePointL"
                        "abel{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QToolButton#toolButton_closePointLabel:hover,\n"
"QToolButton#toolButton_cardResultAnimationDraw7:hover,\n"
"QToolButton#toolButton_cardResultAnimationDraw5:hover, \n"
"QToolButton#toolButton_cardResultAnimationDraw6:hover{ \n"
"background-color: #444444;\n"
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
"/*##################################"
                        "#########################*/\n"
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
"	border-top-right-radius: 7px;\n"
"	height: 15px;\n"
"	subcont"
                        "rol-position: top;\n"
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
""
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
"	border-bottom-right-radius: 7px;\n"
"	width: 15"
                        "px;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton   "
                        "        \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*******************************************/\n"
"QToolButton[QTool"
                        "ButtonStyle=\"2\"]{\n"
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
"    font: 500 10pt \"Ubuntu\";    \n"
"    padding: 4px 20px;\n"
"	bord"
                        "er: 2px solid #C8CC8E;\n"
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
"	border-bottom-right-radius: 10px;\n"
"	border-bottom-"
                        "left-radius: 0px;\n"
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
"QLineEdit#lineEdit_textResultAnimation3{\n"
"font: 7pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #333333;\n"
"border: 1px solid #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 2px;\n"
"pad"
                        "ding-left: 2px;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QCheckBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QCheckBox[QCheckBoxStyle=\"1\"] {\n"
"    \n"
"    background-"
                        "color: #444444;\n"
"	color: #DDDDDD;\n"
"    padding: 5px;\n"
"	font:  9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"\n"
"QCheckBox[QCheckBoxStyle=\"1\"]:disabled {    \n"
"    background-color: #333;\n"
"	color: #777;\n"
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
"QCheckBox[QCheckBoxStyle=\"1\"]::indicator:checked:disabled {\n"
"    background-color: #666;\n"
"\n"
"}\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QRadioButton            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QRadioButton[QRadioButtonStyle=\"1\"] {    \n"
"    "
                        "background-color: transparent;\n"
"	color: #DDDDDD;\n"
"    padding: 5px;\n"
"	font:  9pt \"Ubuntu\";\n"
"    selection-background-color: #808080;\n"
"}\n"
"QRadioButton[QRadioButtonStyle=\"1\"]:disabled {    \n"
"    background-color: #333;\n"
"	color: #777;\n"
"}\n"
"\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator {\n"
"    background-color: #333;\n"
"    border: 1px solid #555;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator:disabled {\n"
"    background-color: #444;\n"
"    border: 1px solid #444;\n"
"	border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator:checked{\n"
"    background-color: #F94646;\n"
" /*#00BDB9 #77ACA2*/\n"
"    border: none;\n"
"	 border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton[QRadioButtonStyle=\"1\"]::indicator:checked:disabled {\n"
"    background-color: #666;\n"
"\n"
"}\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormMenuResultAnimation)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_ResultAnimationProject = QFrame(FormMenuResultAnimation)
        self.frame_ResultAnimationProject.setObjectName(u"frame_ResultAnimationProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimationProject.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimationProject.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimationProject.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimationProject.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_ResultAnimationProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_ResultAnimationProject)
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

        self.frame_ResultAnimation = QFrame(self.frame_ResultAnimationProject)
        self.frame_ResultAnimation.setObjectName(u"frame_ResultAnimation")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimation.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_ResultAnimation)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_ResultAnimation)
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
        self.label_cardResultAnimationTitle = QLabel(self.frame_title)
        self.label_cardResultAnimationTitle.setObjectName(u"label_cardResultAnimationTitle")
        self.label_cardResultAnimationTitle.setProperty(u"QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardResultAnimationTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_ResultAnimation)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_ResultAnimationSubTitle1 = QFrame(self.frame_info)
        self.frame_ResultAnimationSubTitle1.setObjectName(u"frame_ResultAnimationSubTitle1")
        self.frame_ResultAnimationSubTitle1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimationSubTitle1.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_ResultAnimationSubTitle1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardResultAnimationSubTitle1 = QLabel(self.frame_ResultAnimationSubTitle1)
        self.label_cardResultAnimationSubTitle1.setObjectName(u"label_cardResultAnimationSubTitle1")
        self.label_cardResultAnimationSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardResultAnimationSubTitle1.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardResultAnimationSubTitle1)

        self.toolButton_cardResultAnimationSubTitle1 = QToolButton(self.frame_ResultAnimationSubTitle1)
        self.toolButton_cardResultAnimationSubTitle1.setObjectName(u"toolButton_cardResultAnimationSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_cardResultAnimationSubTitle1.setIcon(icon1)
        self.toolButton_cardResultAnimationSubTitle1.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardResultAnimationSubTitle1.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardResultAnimationSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimationSubTitle1)

        self.frame_ResultAnimation1 = QFrame(self.frame_info)
        self.frame_ResultAnimation1.setObjectName(u"frame_ResultAnimation1")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation1.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation1.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimation1.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_ResultAnimation1)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_ResultAnimation1)
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
        self.label_textPointMaterialName.setMinimumSize(QSize(0, 30))
        self.label_textPointMaterialName.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_textPointMaterialName)

        self.comboBox_sceneTypeResult = QComboBox(self.frame_3)
        self.comboBox_sceneTypeResult.setObjectName(u"comboBox_sceneTypeResult")
        self.comboBox_sceneTypeResult.setMinimumSize(QSize(0, 25))
        self.comboBox_sceneTypeResult.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.comboBox_sceneTypeResult.setProperty(u"QComboBoxStyle", 1)

        self.formLayout_3.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_sceneTypeResult)

        self.label_textResultAnimation3 = QLabel(self.frame_3)
        self.label_textResultAnimation3.setObjectName(u"label_textResultAnimation3")
        self.label_textResultAnimation3.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation3.setProperty(u"QLabelStyle", 3)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_textResultAnimation3)

        self.spinBox_ResultAnimationVelocity = QSpinBox(self.frame_3)
        self.spinBox_ResultAnimationVelocity.setObjectName(u"spinBox_ResultAnimationVelocity")
        self.spinBox_ResultAnimationVelocity.setMinimumSize(QSize(120, 25))
        self.spinBox_ResultAnimationVelocity.setMinimum(1)
        self.spinBox_ResultAnimationVelocity.setMaximum(100)
        self.spinBox_ResultAnimationVelocity.setSingleStep(1)
        self.spinBox_ResultAnimationVelocity.setValue(50)
        self.spinBox_ResultAnimationVelocity.setDisplayIntegerBase(10)
        self.spinBox_ResultAnimationVelocity.setProperty(u"QSpinBoxStyle", 1)

        self.formLayout_3.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_ResultAnimationVelocity)

        self.checkBox_ResultVector = QCheckBox(self.frame_3)
        self.checkBox_ResultVector.setObjectName(u"checkBox_ResultVector")
        self.checkBox_ResultVector.setEnabled(False)
        self.checkBox_ResultVector.setChecked(False)
        self.checkBox_ResultVector.setProperty(u"QCheckBoxStyle", 1)

        self.formLayout_3.setWidget(2, QFormLayout.ItemRole.FieldRole, self.checkBox_ResultVector)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.radioButton_ResultXY = QRadioButton(self.frame_3)
        self.radioButton_ResultXY.setObjectName(u"radioButton_ResultXY")
        self.radioButton_ResultXY.setEnabled(False)
        self.radioButton_ResultXY.setChecked(True)
        self.radioButton_ResultXY.setProperty(u"QRadioButtonStyle", 1)

        self.horizontalLayout_9.addWidget(self.radioButton_ResultXY)

        self.radioButton_ResultX = QRadioButton(self.frame_3)
        self.radioButton_ResultX.setObjectName(u"radioButton_ResultX")
        self.radioButton_ResultX.setEnabled(False)
        self.radioButton_ResultX.setCheckable(True)
        self.radioButton_ResultX.setChecked(False)
        self.radioButton_ResultX.setProperty(u"QRadioButtonStyle", 1)

        self.horizontalLayout_9.addWidget(self.radioButton_ResultX)

        self.radioButton_ResultY = QRadioButton(self.frame_3)
        self.radioButton_ResultY.setObjectName(u"radioButton_ResultY")
        self.radioButton_ResultY.setEnabled(False)
        self.radioButton_ResultY.setProperty(u"QRadioButtonStyle", 1)

        self.horizontalLayout_9.addWidget(self.radioButton_ResultY)


        self.formLayout_3.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_9)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.groupBox = QGroupBox(self.frame_ResultAnimation1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.toolButton_sceneRegress = QToolButton(self.groupBox)
        self.toolButton_sceneRegress.setObjectName(u"toolButton_sceneRegress")
        self.toolButton_sceneRegress.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"app/resources/iconos/icono_result/atras.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_sceneRegress.setIcon(icon2)
        self.toolButton_sceneRegress.setIconSize(QSize(25, 25))
        self.toolButton_sceneRegress.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneRegress)

        self.toolButton_sceneStop = QToolButton(self.groupBox)
        self.toolButton_sceneStop.setObjectName(u"toolButton_sceneStop")
        self.toolButton_sceneStop.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"app/resources/iconos/icono_result/stop.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_sceneStop.setIcon(icon3)
        self.toolButton_sceneStop.setIconSize(QSize(25, 25))
        self.toolButton_sceneStop.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneStop)

        self.toolButton_scenePlay = QToolButton(self.groupBox)
        self.toolButton_scenePlay.setObjectName(u"toolButton_scenePlay")
        self.toolButton_scenePlay.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"app/resources/iconos/icono_result/play.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_scenePlay.setIcon(icon4)
        self.toolButton_scenePlay.setIconSize(QSize(25, 25))
        self.toolButton_scenePlay.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_scenePlay)

        self.toolButton_sceneAdvance = QToolButton(self.groupBox)
        self.toolButton_sceneAdvance.setObjectName(u"toolButton_sceneAdvance")
        self.toolButton_sceneAdvance.setMinimumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u"app/resources/iconos/icono_result/adelante.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_sceneAdvance.setIcon(icon5)
        self.toolButton_sceneAdvance.setIconSize(QSize(25, 25))
        self.toolButton_sceneAdvance.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneAdvance)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_textResultTime = QLabel(self.groupBox)
        self.label_textResultTime.setObjectName(u"label_textResultTime")
        self.label_textResultTime.setMinimumSize(QSize(60, 30))
        self.label_textResultTime.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_textResultTime.setProperty(u"QLabelStyle", 4)

        self.verticalLayout_12.addWidget(self.label_textResultTime)

        self.label_text_7 = QLabel(self.groupBox)
        self.label_text_7.setObjectName(u"label_text_7")
        self.label_text_7.setMinimumSize(QSize(0, 0))
        self.label_text_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_text_7.setProperty(u"QLabelStyle", 3)

        self.verticalLayout_12.addWidget(self.label_text_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_textResultStep = QLabel(self.groupBox)
        self.label_textResultStep.setObjectName(u"label_textResultStep")
        self.label_textResultStep.setMinimumSize(QSize(60, 30))
        self.label_textResultStep.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_textResultStep.setProperty(u"QLabelStyle", 4)

        self.verticalLayout_13.addWidget(self.label_textResultStep)

        self.label_text_8 = QLabel(self.groupBox)
        self.label_text_8.setObjectName(u"label_text_8")
        self.label_text_8.setMinimumSize(QSize(0, 0))
        self.label_text_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_text_8.setProperty(u"QLabelStyle", 3)

        self.verticalLayout_13.addWidget(self.label_text_8)


        self.horizontalLayout_11.addLayout(self.verticalLayout_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_text = QLabel(self.frame_ResultAnimation1)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setMinimumSize(QSize(0, 30))
        self.label_text.setProperty(u"QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_text)

        self.label_textResultSteps = QLabel(self.frame_ResultAnimation1)
        self.label_textResultSteps.setObjectName(u"label_textResultSteps")
        self.label_textResultSteps.setMinimumSize(QSize(60, 30))
        self.label_textResultSteps.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_textResultSteps.setProperty(u"QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.label_textResultSteps)


        self.verticalLayout_6.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation1)

        self.frame_ResultAnimationSubTitle0 = QFrame(self.frame_info)
        self.frame_ResultAnimationSubTitle0.setObjectName(u"frame_ResultAnimationSubTitle0")
        self.frame_ResultAnimationSubTitle0.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimationSubTitle0.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ResultAnimationSubTitle0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardResultAnimationSubTitle0 = QLabel(self.frame_ResultAnimationSubTitle0)
        self.label_cardResultAnimationSubTitle0.setObjectName(u"label_cardResultAnimationSubTitle0")
        self.label_cardResultAnimationSubTitle0.setMinimumSize(QSize(262, 0))
        self.label_cardResultAnimationSubTitle0.setProperty(u"QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardResultAnimationSubTitle0)

        self.toolButton_cardResultAnimationSubTitle0 = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_cardResultAnimationSubTitle0.setObjectName(u"toolButton_cardResultAnimationSubTitle0")
        self.toolButton_cardResultAnimationSubTitle0.setIcon(icon1)
        self.toolButton_cardResultAnimationSubTitle0.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_cardResultAnimationSubTitle0.setProperty(u"QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardResultAnimationSubTitle0)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimationSubTitle0)

        self.frame_ResultAnimation0 = QFrame(self.frame_info)
        self.frame_ResultAnimation0.setObjectName(u"frame_ResultAnimation0")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation0.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation0.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation0.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_ResultAnimation0.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_ResultAnimation0)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_ResultAnimation0)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textResultAnimation1_2 = QLabel(self.frame_4)
        self.label_textResultAnimation1_2.setObjectName(u"label_textResultAnimation1_2")
        self.label_textResultAnimation1_2.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_2.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_textResultAnimation1_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.comboBox_ResultAnimationColorStyles_Resultados = QComboBox(self.frame_4)
        self.comboBox_ResultAnimationColorStyles_Resultados.setObjectName(u"comboBox_ResultAnimationColorStyles_Resultados")
        self.comboBox_ResultAnimationColorStyles_Resultados.setMinimumSize(QSize(0, 25))
        self.comboBox_ResultAnimationColorStyles_Resultados.setProperty(u"QComboBoxStyle", 1)

        self.horizontalLayout_4.addWidget(self.comboBox_ResultAnimationColorStyles_Resultados)

        self.comboBox_ResultAnimationColorStyles_Puntos = QComboBox(self.frame_4)
        self.comboBox_ResultAnimationColorStyles_Puntos.setObjectName(u"comboBox_ResultAnimationColorStyles_Puntos")
        self.comboBox_ResultAnimationColorStyles_Puntos.setMinimumSize(QSize(0, 25))
        self.comboBox_ResultAnimationColorStyles_Puntos.setProperty(u"QComboBoxStyle", 1)

        self.horizontalLayout_4.addWidget(self.comboBox_ResultAnimationColorStyles_Puntos)


        self.formLayout_4.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_4)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_textColor = QLineEdit(self.frame_4)
        self.lineEdit_textColor.setObjectName(u"lineEdit_textColor")
        self.lineEdit_textColor.setEnabled(False)
        self.lineEdit_textColor.setMinimumSize(QSize(120, 25))
        self.lineEdit_textColor.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(51, 51, 51, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        brush2 = QBrush(QColor(221, 221, 221, 128))
        brush2.setStyle(Qt.BrushStyle.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.PlaceholderText, brush2)
#endif
        self.lineEdit_textColor.setPalette(palette)
        self.lineEdit_textColor.setStyleSheet(u"")
        self.lineEdit_textColor.setProperty(u"QLineEditStyle", 2)

        self.horizontalLayout_8.addWidget(self.lineEdit_textColor)

        self.btn_select_color = QToolButton(self.frame_4)
        self.btn_select_color.setObjectName(u"btn_select_color")
        icon6 = QIcon()
        icon6.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_select_color.setIcon(icon6)
        self.btn_select_color.setIconSize(QSize(20, 20))
        self.btn_select_color.setArrowType(Qt.ArrowType.NoArrow)
        self.btn_select_color.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_8.addWidget(self.btn_select_color)


        self.formLayout_4.setLayout(1, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_8)

        self.label_textResultAnimation1_3 = QLabel(self.frame_4)
        self.label_textResultAnimation1_3.setObjectName(u"label_textResultAnimation1_3")
        self.label_textResultAnimation1_3.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_3.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_textResultAnimation1_3)

        self.doubleSpinBoxl_textResultAnimationSizePoints = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setObjectName(u"doubleSpinBoxl_textResultAnimationSizePoints")
        self.doubleSpinBoxl_textResultAnimationSizePoints.setEnabled(True)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textResultAnimationSizePoints.setDecimals(3)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMaximum(2.000000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setValue(0.050000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setProperty(u"QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.doubleSpinBoxl_textResultAnimationSizePoints)

        self.label_textResultAnimation1_4 = QLabel(self.frame_4)
        self.label_textResultAnimation1_4.setObjectName(u"label_textResultAnimation1_4")
        self.label_textResultAnimation1_4.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_4.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_textResultAnimation1_4)

        self.spinBox_ResultAnimationSizeText = QSpinBox(self.frame_4)
        self.spinBox_ResultAnimationSizeText.setObjectName(u"spinBox_ResultAnimationSizeText")
        self.spinBox_ResultAnimationSizeText.setMinimumSize(QSize(120, 25))
        self.spinBox_ResultAnimationSizeText.setMinimum(1)
        self.spinBox_ResultAnimationSizeText.setMaximum(100)
        self.spinBox_ResultAnimationSizeText.setSingleStep(1)
        self.spinBox_ResultAnimationSizeText.setValue(12)
        self.spinBox_ResultAnimationSizeText.setDisplayIntegerBase(10)
        self.spinBox_ResultAnimationSizeText.setProperty(u"QSpinBoxStyle", 1)

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.spinBox_ResultAnimationSizeText)

        self.label_textResultAnimation1_5 = QLabel(self.frame_4)
        self.label_textResultAnimation1_5.setObjectName(u"label_textResultAnimation1_5")
        self.label_textResultAnimation1_5.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_5.setProperty(u"QLabelStyle", 3)

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_textResultAnimation1_5)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lineEdit_ResultAnimation_LabelByPointId = QLineEdit(self.frame_4)
        self.lineEdit_ResultAnimation_LabelByPointId.setObjectName(u"lineEdit_ResultAnimation_LabelByPointId")
        self.lineEdit_ResultAnimation_LabelByPointId.setMinimumSize(QSize(0, 25))
        self.lineEdit_ResultAnimation_LabelByPointId.setProperty(u"QLineEditStyle", 1)

        self.horizontalLayout_10.addWidget(self.lineEdit_ResultAnimation_LabelByPointId)

        self.toolButton_AddPointLabel = QToolButton(self.frame_4)
        self.toolButton_AddPointLabel.setObjectName(u"toolButton_AddPointLabel")
        icon7 = QIcon()
        icon7.addFile(u"app/app/app/MPM-UN_2025/app/resources/iconos/icono_result/add.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_AddPointLabel.setIcon(icon7)
        self.toolButton_AddPointLabel.setIconSize(QSize(20, 20))
        self.toolButton_AddPointLabel.setArrowType(Qt.ArrowType.NoArrow)
        self.toolButton_AddPointLabel.setProperty(u"QToolButtonStyle", 1)

        self.horizontalLayout_10.addWidget(self.toolButton_AddPointLabel)

        self.toolButton_closePointLabel = QToolButton(self.frame_4)
        self.toolButton_closePointLabel.setObjectName(u"toolButton_closePointLabel")
        sizePolicy3.setHeightForWidth(self.toolButton_closePointLabel.sizePolicy().hasHeightForWidth())
        self.toolButton_closePointLabel.setSizePolicy(sizePolicy3)
        self.toolButton_closePointLabel.setMinimumSize(QSize(25, 25))
        self.toolButton_closePointLabel.setMaximumSize(QSize(25, 25))
        self.toolButton_closePointLabel.setFont(font)
        self.toolButton_closePointLabel.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"app/app/app/MPM-UN_2025/app/resources/iconos/iconos_consola/exit.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_closePointLabel.setIcon(icon8)
        self.toolButton_closePointLabel.setIconSize(QSize(15, 15))
        self.toolButton_closePointLabel.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.toolButton_closePointLabel.setProperty(u"style_mesh_card_button", 1)

        self.horizontalLayout_10.addWidget(self.toolButton_closePointLabel)


        self.formLayout_4.setLayout(4, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_ResultAnimationCountour = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationCountour.setObjectName(u"checkBox_ResultAnimationCountour")
        self.checkBox_ResultAnimationCountour.setChecked(True)
        self.checkBox_ResultAnimationCountour.setProperty(u"QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationCountour)

        self.checkBox_ResultAnimationLabel = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationLabel.setObjectName(u"checkBox_ResultAnimationLabel")
        self.checkBox_ResultAnimationLabel.setChecked(True)
        self.checkBox_ResultAnimationLabel.setProperty(u"QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationLabel)

        self.checkBox_ResultAnimationGrid = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationGrid.setObjectName(u"checkBox_ResultAnimationGrid")
        self.checkBox_ResultAnimationGrid.setChecked(True)
        self.checkBox_ResultAnimationGrid.setProperty(u"QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationGrid)

        self.checkBox_ResultAnimationValues = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationValues.setObjectName(u"checkBox_ResultAnimationValues")
        self.checkBox_ResultAnimationValues.setChecked(False)
        self.checkBox_ResultAnimationValues.setProperty(u"QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationValues)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation0)

        self.verticalSpacer_2 = QSpacerItem(20, 227, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_msn = QLabel(self.frame_info)
        self.label_msn.setObjectName(u"label_msn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_msn.sizePolicy().hasHeightForWidth())
        self.label_msn.setSizePolicy(sizePolicy5)
        self.label_msn.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_msn)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_ResultAnimation)


        self.horizontalLayout_6.addWidget(self.frame_ResultAnimationProject)


        self.retranslateUi(FormMenuResultAnimation)

        QMetaObject.connectSlotsByName(FormMenuResultAnimation)
    # setupUi

    def retranslateUi(self, FormMenuResultAnimation):
        FormMenuResultAnimation.setWindowTitle(QCoreApplication.translate("FormMenuResultAnimation", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardResultAnimationTitle.setText(QCoreApplication.translate("FormMenuResultAnimation", u"ANIMACIONES", None))
        self.label_cardResultAnimationSubTitle1.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Datos de visualizaci\u00f3n", None))
        self.toolButton_cardResultAnimationSubTitle1.setText("")
        self.label_textPointMaterialName.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tipo de resultado:", None))
        self.label_textResultAnimation3.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Velocidad anim.:", None))
        self.checkBox_ResultVector.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Campo de vectores", None))
        self.radioButton_ResultXY.setText(QCoreApplication.translate("FormMenuResultAnimation", u"XY", None))
        self.radioButton_ResultX.setText(QCoreApplication.translate("FormMenuResultAnimation", u"XX", None))
        self.radioButton_ResultY.setText(QCoreApplication.translate("FormMenuResultAnimation", u"YY", None))
        self.groupBox.setTitle("")
        self.toolButton_sceneRegress.setText(QCoreApplication.translate("FormMenuResultAnimation", u"...", None))
        self.toolButton_sceneStop.setText(QCoreApplication.translate("FormMenuResultAnimation", u"...", None))
        self.toolButton_scenePlay.setText(QCoreApplication.translate("FormMenuResultAnimation", u"...", None))
        self.toolButton_sceneAdvance.setText(QCoreApplication.translate("FormMenuResultAnimation", u"...", None))
        self.label_textResultTime.setText(QCoreApplication.translate("FormMenuResultAnimation", u"0", None))
        self.label_text_7.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tiempo", None))
        self.label_textResultStep.setText(QCoreApplication.translate("FormMenuResultAnimation", u"0", None))
        self.label_text_8.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Pasos", None))
        self.label_text.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Numero de pasos", None))
        self.label_textResultSteps.setText(QCoreApplication.translate("FormMenuResultAnimation", u"11532", None))
        self.label_cardResultAnimationSubTitle0.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Estilo de visualizaci\u00f3n", None))
        self.toolButton_cardResultAnimationSubTitle0.setText("")
        self.label_textResultAnimation1_2.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Estilos de colores:", None))
        self.lineEdit_textColor.setText("")
        self.btn_select_color.setText("")
        self.label_textResultAnimation1_3.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tama\u00f1o puntos (r):", None))
        self.doubleSpinBoxl_textResultAnimationSizePoints.setSuffix(QCoreApplication.translate("FormMenuResultAnimation", u"m", None))
        self.label_textResultAnimation1_4.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tama\u00f1o textos:", None))
        self.label_textResultAnimation1_5.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Agregar etiqueta:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_ResultAnimation_LabelByPointId.setToolTip(QCoreApplication.translate("FormMenuResultAnimation", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Puede buscar por id como 1 o 2 o 3 etc. O por conjuntos separados por coma, por ejemplo 1,2,3\u2026</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_ResultAnimation_LabelByPointId.setInputMask("")
        self.lineEdit_ResultAnimation_LabelByPointId.setText("")
        self.lineEdit_ResultAnimation_LabelByPointId.setPlaceholderText(QCoreApplication.translate("FormMenuResultAnimation", u"id punto", None))
        self.toolButton_AddPointLabel.setText("")
        self.toolButton_closePointLabel.setText("")
        self.checkBox_ResultAnimationCountour.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Contorno", None))
        self.checkBox_ResultAnimationLabel.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Etiquetas", None))
        self.checkBox_ResultAnimationGrid.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Grilla", None))
        self.checkBox_ResultAnimationValues.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver numeraci\u00f3n", None))
        self.label_msn.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Empty", None))
    # retranslateUi

