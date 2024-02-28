# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_result_menu_animationobjAzp.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

class Ui_FormMenuResultAnimation(object):
    def setupUi(self, FormMenuResultAnimation):
        if not FormMenuResultAnimation.objectName():
            FormMenuResultAnimation.setObjectName(u"FormMenuResultAnimation")
        FormMenuResultAnimation.resize(350, 889)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
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
"QToolButton[QToolButtonStyle=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
""
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
""
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
"QToolButto"
                        "n[QToolButtonStyle=\"6\"] {\n"
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
"\n"
"\n"
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QLineEdit           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QFrame          \u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
""
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
"QComboBox[QComboBoxStyle=\"1\"] {\n"
"    border: none;\n"
"    background-color: #444444;\n"
"	color: #DDDDDD;\n"
"    borde"
                        "r-radius: 2px;\n"
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
"QCheckBox[QCheckBoxS"
                        "tyle=\"1\"]::indicator:checked {\n"
"    background-color: #F94646;\n"
"    border: none;\n"
"	 border-radius: 3px;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormMenuResultAnimation)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_ResultAnimationProject = QFrame(FormMenuResultAnimation)
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
        icon.addFile(u"app/resources/iconos/iconos_menu_draw_data/hide_show.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        icon1.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_ResultAnimation1)
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
        self.label_textPointMaterialName.setMinimumSize(QSize(0, 30))
        self.label_textPointMaterialName.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_textPointMaterialName)

        self.comboBox_sceneTypeResult = QComboBox(self.frame_3)
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

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.comboBox_sceneTypeResult)

        self.label_textResultAnimation3 = QLabel(self.frame_3)
        self.label_textResultAnimation3.setObjectName(u"label_textResultAnimation3")
        self.label_textResultAnimation3.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation3.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_textResultAnimation3)

        self.spinBox_ResultAnimationVelocity = QSpinBox(self.frame_3)
        self.spinBox_ResultAnimationVelocity.setObjectName(u"spinBox_ResultAnimationVelocity")
        self.spinBox_ResultAnimationVelocity.setMinimumSize(QSize(120, 25))
        self.spinBox_ResultAnimationVelocity.setMinimum(1)
        self.spinBox_ResultAnimationVelocity.setMaximum(100)
        self.spinBox_ResultAnimationVelocity.setSingleStep(1)
        self.spinBox_ResultAnimationVelocity.setValue(50)
        self.spinBox_ResultAnimationVelocity.setDisplayIntegerBase(10)
        self.spinBox_ResultAnimationVelocity.setProperty("QSpinBoxStyle", 1)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.spinBox_ResultAnimationVelocity)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.groupBox = QGroupBox(self.frame_ResultAnimation1)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_4)

        self.toolButton_sceneRegress = QToolButton(self.groupBox)
        self.toolButton_sceneRegress.setObjectName(u"toolButton_sceneRegress")
        self.toolButton_sceneRegress.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u"app/resources/iconos/icono_result/atras.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneRegress.setIcon(icon2)
        self.toolButton_sceneRegress.setIconSize(QSize(25, 25))
        self.toolButton_sceneRegress.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneRegress)

        self.toolButton_sceneStop = QToolButton(self.groupBox)
        self.toolButton_sceneStop.setObjectName(u"toolButton_sceneStop")
        self.toolButton_sceneStop.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u"app/resources/iconos/icono_result/stop.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneStop.setIcon(icon3)
        self.toolButton_sceneStop.setIconSize(QSize(25, 25))
        self.toolButton_sceneStop.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneStop)

        self.toolButton_scenePlay = QToolButton(self.groupBox)
        self.toolButton_scenePlay.setObjectName(u"toolButton_scenePlay")
        self.toolButton_scenePlay.setMinimumSize(QSize(40, 40))
        icon4 = QIcon()
        icon4.addFile(u"app/resources/iconos/icono_result/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_scenePlay.setIcon(icon4)
        self.toolButton_scenePlay.setIconSize(QSize(25, 25))
        self.toolButton_scenePlay.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_scenePlay)

        self.toolButton_sceneAdvance = QToolButton(self.groupBox)
        self.toolButton_sceneAdvance.setObjectName(u"toolButton_sceneAdvance")
        self.toolButton_sceneAdvance.setMinimumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u"app/resources/iconos/icono_result/adelante.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_sceneAdvance.setIcon(icon5)
        self.toolButton_sceneAdvance.setIconSize(QSize(25, 25))
        self.toolButton_sceneAdvance.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_sceneAdvance)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_textResultTime = QLabel(self.groupBox)
        self.label_textResultTime.setObjectName(u"label_textResultTime")
        self.label_textResultTime.setMinimumSize(QSize(60, 30))
        self.label_textResultTime.setAlignment(Qt.AlignCenter)
        self.label_textResultTime.setProperty("QLabelStyle", 4)

        self.verticalLayout_12.addWidget(self.label_textResultTime)

        self.label_text_7 = QLabel(self.groupBox)
        self.label_text_7.setObjectName(u"label_text_7")
        self.label_text_7.setMinimumSize(QSize(0, 0))
        self.label_text_7.setAlignment(Qt.AlignCenter)
        self.label_text_7.setProperty("QLabelStyle", 3)

        self.verticalLayout_12.addWidget(self.label_text_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_textResultStep = QLabel(self.groupBox)
        self.label_textResultStep.setObjectName(u"label_textResultStep")
        self.label_textResultStep.setMinimumSize(QSize(60, 30))
        self.label_textResultStep.setAlignment(Qt.AlignCenter)
        self.label_textResultStep.setProperty("QLabelStyle", 4)

        self.verticalLayout_13.addWidget(self.label_textResultStep)

        self.label_text_8 = QLabel(self.groupBox)
        self.label_text_8.setObjectName(u"label_text_8")
        self.label_text_8.setMinimumSize(QSize(0, 0))
        self.label_text_8.setAlignment(Qt.AlignCenter)
        self.label_text_8.setProperty("QLabelStyle", 3)

        self.verticalLayout_13.addWidget(self.label_text_8)


        self.horizontalLayout_11.addLayout(self.verticalLayout_13)


        self.verticalLayout_8.addLayout(self.horizontalLayout_11)


        self.verticalLayout_6.addWidget(self.groupBox)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_text = QLabel(self.frame_ResultAnimation1)
        self.label_text.setObjectName(u"label_text")
        self.label_text.setMinimumSize(QSize(0, 30))
        self.label_text.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_text)

        self.label_textResultSteps = QLabel(self.frame_ResultAnimation1)
        self.label_textResultSteps.setObjectName(u"label_textResultSteps")
        self.label_textResultSteps.setMinimumSize(QSize(60, 30))
        self.label_textResultSteps.setAlignment(Qt.AlignCenter)
        self.label_textResultSteps.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_textResultSteps)


        self.verticalLayout_6.addLayout(self.formLayout)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation1)

        self.frame_ResultAnimationSubTitle0 = QFrame(self.frame_info)
        self.frame_ResultAnimationSubTitle0.setObjectName(u"frame_ResultAnimationSubTitle0")
        self.frame_ResultAnimationSubTitle0.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimationSubTitle0.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_ResultAnimationSubTitle0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardResultAnimationSubTitle0 = QLabel(self.frame_ResultAnimationSubTitle0)
        self.label_cardResultAnimationSubTitle0.setObjectName(u"label_cardResultAnimationSubTitle0")
        self.label_cardResultAnimationSubTitle0.setMinimumSize(QSize(262, 0))
        self.label_cardResultAnimationSubTitle0.setProperty("QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardResultAnimationSubTitle0)

        self.toolButton_cardResultAnimationSubTitle0 = QToolButton(self.frame_ResultAnimationSubTitle0)
        self.toolButton_cardResultAnimationSubTitle0.setObjectName(u"toolButton_cardResultAnimationSubTitle0")
        self.toolButton_cardResultAnimationSubTitle0.setIcon(icon1)
        self.toolButton_cardResultAnimationSubTitle0.setArrowType(Qt.NoArrow)
        self.toolButton_cardResultAnimationSubTitle0.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardResultAnimationSubTitle0)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimationSubTitle0)

        self.frame_ResultAnimation0 = QFrame(self.frame_info)
        self.frame_ResultAnimation0.setObjectName(u"frame_ResultAnimation0")
        sizePolicy1.setHeightForWidth(self.frame_ResultAnimation0.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation0.setSizePolicy(sizePolicy1)
        self.frame_ResultAnimation0.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimation0.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_ResultAnimation0)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_ResultAnimation0)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textResultAnimation1_2 = QLabel(self.frame_4)
        self.label_textResultAnimation1_2.setObjectName(u"label_textResultAnimation1_2")
        self.label_textResultAnimation1_2.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_2.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_textResultAnimation1_2)

        self.comboBox_ResultAnimationColorStyles = QComboBox(self.frame_4)
        self.comboBox_ResultAnimationColorStyles.addItem("")
        self.comboBox_ResultAnimationColorStyles.addItem("")
        self.comboBox_ResultAnimationColorStyles.addItem("")
        self.comboBox_ResultAnimationColorStyles.addItem("")
        self.comboBox_ResultAnimationColorStyles.setObjectName(u"comboBox_ResultAnimationColorStyles")
        self.comboBox_ResultAnimationColorStyles.setMinimumSize(QSize(0, 25))
        self.comboBox_ResultAnimationColorStyles.setProperty("QComboBoxStyle", 1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.comboBox_ResultAnimationColorStyles)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEdit_textColor = QLineEdit(self.frame_4)
        self.lineEdit_textColor.setObjectName(u"lineEdit_textColor")
        self.lineEdit_textColor.setEnabled(False)
        self.lineEdit_textColor.setMinimumSize(QSize(120, 25))
        self.lineEdit_textColor.setMaximumSize(QSize(16777215, 16777215))
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
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.lineEdit_textColor.setPalette(palette)
        self.lineEdit_textColor.setStyleSheet(u"")
        self.lineEdit_textColor.setProperty("QLineEditStyle", 2)

        self.horizontalLayout_8.addWidget(self.lineEdit_textColor)

        self.btn_select_color = QToolButton(self.frame_4)
        self.btn_select_color.setObjectName(u"btn_select_color")
        icon6 = QIcon()
        icon6.addFile(u"app/resources/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_select_color.setIcon(icon6)
        self.btn_select_color.setIconSize(QSize(20, 20))
        self.btn_select_color.setArrowType(Qt.NoArrow)
        self.btn_select_color.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_8.addWidget(self.btn_select_color)


        self.formLayout_4.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_8)

        self.label_textResultAnimation1_3 = QLabel(self.frame_4)
        self.label_textResultAnimation1_3.setObjectName(u"label_textResultAnimation1_3")
        self.label_textResultAnimation1_3.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_3.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_textResultAnimation1_3)

        self.doubleSpinBoxl_textResultAnimationSizePoints = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setObjectName(u"doubleSpinBoxl_textResultAnimationSizePoints")
        self.doubleSpinBoxl_textResultAnimationSizePoints.setEnabled(True)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textResultAnimationSizePoints.setDecimals(3)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setMaximum(2.000000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setValue(0.050000000000000)
        self.doubleSpinBoxl_textResultAnimationSizePoints.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBoxl_textResultAnimationSizePoints)

        self.label_textResultAnimation1_4 = QLabel(self.frame_4)
        self.label_textResultAnimation1_4.setObjectName(u"label_textResultAnimation1_4")
        self.label_textResultAnimation1_4.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation1_4.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.label_textResultAnimation1_4)

        self.spinBox_ResultAnimationSizeText = QSpinBox(self.frame_4)
        self.spinBox_ResultAnimationSizeText.setObjectName(u"spinBox_ResultAnimationSizeText")
        self.spinBox_ResultAnimationSizeText.setMinimumSize(QSize(120, 25))
        self.spinBox_ResultAnimationSizeText.setMinimum(1)
        self.spinBox_ResultAnimationSizeText.setMaximum(100)
        self.spinBox_ResultAnimationSizeText.setSingleStep(1)
        self.spinBox_ResultAnimationSizeText.setValue(5)
        self.spinBox_ResultAnimationSizeText.setDisplayIntegerBase(10)
        self.spinBox_ResultAnimationSizeText.setProperty("QSpinBoxStyle", 1)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.spinBox_ResultAnimationSizeText)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.checkBox_ResultAnimationCountour = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationCountour.setObjectName(u"checkBox_ResultAnimationCountour")
        self.checkBox_ResultAnimationCountour.setChecked(True)
        self.checkBox_ResultAnimationCountour.setProperty("QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationCountour)

        self.checkBox_ResultAnimationLabel = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationLabel.setObjectName(u"checkBox_ResultAnimationLabel")
        self.checkBox_ResultAnimationLabel.setChecked(True)
        self.checkBox_ResultAnimationLabel.setProperty("QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationLabel)

        self.checkBox_ResultAnimationGrid = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationGrid.setObjectName(u"checkBox_ResultAnimationGrid")
        self.checkBox_ResultAnimationGrid.setChecked(True)
        self.checkBox_ResultAnimationGrid.setProperty("QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationGrid)

        self.checkBox_ResultAnimationBase = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationBase.setObjectName(u"checkBox_ResultAnimationBase")
        self.checkBox_ResultAnimationBase.setChecked(False)
        self.checkBox_ResultAnimationBase.setProperty("QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationBase)

        self.checkBox_ResultAnimationValues = QCheckBox(self.frame_ResultAnimation0)
        self.checkBox_ResultAnimationValues.setObjectName(u"checkBox_ResultAnimationValues")
        self.checkBox_ResultAnimationValues.setChecked(False)
        self.checkBox_ResultAnimationValues.setProperty("QCheckBoxStyle", 1)

        self.verticalLayout_9.addWidget(self.checkBox_ResultAnimationValues)


        self.verticalLayout_7.addLayout(self.verticalLayout_9)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation0)

        self.frame_ResultAnimation3 = QFrame(self.frame_info)
        self.frame_ResultAnimation3.setObjectName(u"frame_ResultAnimation3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_ResultAnimation3.sizePolicy().hasHeightForWidth())
        self.frame_ResultAnimation3.setSizePolicy(sizePolicy5)
        self.frame_ResultAnimation3.setMinimumSize(QSize(0, 150))
        self.frame_ResultAnimation3.setStyleSheet(u"")
        self.frame_ResultAnimation3.setFrameShape(QFrame.StyledPanel)
        self.frame_ResultAnimation3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_ResultAnimation3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_5.addWidget(self.frame_ResultAnimation3)

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
        self.comboBox_sceneTypeResult.setItemText(0, QCoreApplication.translate("FormMenuResultAnimation", u"default", None))
        self.comboBox_sceneTypeResult.setItemText(1, QCoreApplication.translate("FormMenuResultAnimation", u"sigxx", None))
        self.comboBox_sceneTypeResult.setItemText(2, QCoreApplication.translate("FormMenuResultAnimation", u"sigyy", None))
        self.comboBox_sceneTypeResult.setItemText(3, QCoreApplication.translate("FormMenuResultAnimation", u"sigxy", None))
        self.comboBox_sceneTypeResult.setItemText(4, QCoreApplication.translate("FormMenuResultAnimation", u"epsxx", None))
        self.comboBox_sceneTypeResult.setItemText(5, QCoreApplication.translate("FormMenuResultAnimation", u"epsyy", None))
        self.comboBox_sceneTypeResult.setItemText(6, QCoreApplication.translate("FormMenuResultAnimation", u"epsxy", None))

        self.label_textResultAnimation3.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Velocidad anim.:", None))
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
        self.comboBox_ResultAnimationColorStyles.setItemText(0, QCoreApplication.translate("FormMenuResultAnimation", u"default", None))
        self.comboBox_ResultAnimationColorStyles.setItemText(1, QCoreApplication.translate("FormMenuResultAnimation", u"Rojo-Azul", None))
        self.comboBox_ResultAnimationColorStyles.setItemText(2, QCoreApplication.translate("FormMenuResultAnimation", u"Escala de grises", None))
        self.comboBox_ResultAnimationColorStyles.setItemText(3, QCoreApplication.translate("FormMenuResultAnimation", u"Escala color", None))

        self.lineEdit_textColor.setText("")
        self.btn_select_color.setText("")
        self.label_textResultAnimation1_3.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tama\u00f1o puntos:", None))
        self.doubleSpinBoxl_textResultAnimationSizePoints.setSuffix(QCoreApplication.translate("FormMenuResultAnimation", u"m", None))
        self.label_textResultAnimation1_4.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Tama\u00f1o textos:", None))
        self.checkBox_ResultAnimationCountour.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Contorno", None))
        self.checkBox_ResultAnimationLabel.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Etiquetas", None))
        self.checkBox_ResultAnimationGrid.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Grilla", None))
        self.checkBox_ResultAnimationBase.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Base", None))
        self.checkBox_ResultAnimationValues.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Ver Valores", None))
        self.label_msn.setText(QCoreApplication.translate("FormMenuResultAnimation", u"Empty", None))
    # retranslateUi

