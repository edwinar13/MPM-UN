# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_result_menu_tableOYmtqh.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_FormMenuResultTable(object):
    def setupUi(self, FormMenuResultTable):
        if not FormMenuResultTable.objectName():
            FormMenuResultTable.setObjectName(u"FormMenuResultTable")
        FormMenuResultTable.resize(350, 937)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormMenuResultTable.sizePolicy().hasHeightForWidth())
        FormMenuResultTable.setSizePolicy(sizePolicy)
        FormMenuResultTable.setMinimumSize(QSize(0, 0))
        FormMenuResultTable.setMaximumSize(QSize(350, 16777215))
        FormMenuResultTable.setStyleSheet(u"/*Colores primarios*/\n"
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
"padding: 6px "
                        "25px;\n"
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
"background-color: #910D3F;\n"
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
"QToolButton#toolButton_cardResultAnimationDraw7,\n"
"QToolButton#toolButton_cardResultAnimationDraw5,\n"
"QToolButton#toolButton_cardResultAnimationDraw6{\n"
"background-color: transparent;\n"
"border: 1px solid "
                        "#222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"\n"
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
"/*###########################################################*/\n"
""
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
"	subcontrol-position: top;\n"
"	subcontr"
                        "ol-origin: margin;\n"
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
"height: 14px;\n"
"border: no"
                        "ne;\n"
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
"	width: 15px;\n"
"	subcontrol-position"
                        ": right;\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"QToolButton[QToolButtonStyle=\"2\"]{\n"
"font: 50"
                        "0 10pt \"Ubuntu\";\n"
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
"	border: 2px solid #C8CC8E;\n"
"    \n"
""
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
"	border-bottom-left-radius: 0px;\n"
"	color: #22222"
                        "2;\n"
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
"padding-left: 2px;\n"
"\n"
"}\n"
"\n"
""
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8           QLabel           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           Q"
                        "ComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"    background-color: #444444;\n"
"	color: #DDDDDD;"
                        "\n"
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
"")
        self.horizontalLayout_6 = QHBoxLayout(FormMenuResultTable)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_ResultAnimationProject = QFrame(FormMenuResultTable)
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
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_textPointMaterialName = QLabel(self.frame_ResultAnimation1)
        self.label_textPointMaterialName.setObjectName(u"label_textPointMaterialName")
        self.label_textPointMaterialName.setMinimumSize(QSize(0, 30))
        self.label_textPointMaterialName.setProperty("QLabelStyle", 3)

        self.verticalLayout_6.addWidget(self.label_textPointMaterialName)

        self.lineEdit_tableSearchByPointId = QLineEdit(self.frame_ResultAnimation1)
        self.lineEdit_tableSearchByPointId.setObjectName(u"lineEdit_tableSearchByPointId")
        self.lineEdit_tableSearchByPointId.setMinimumSize(QSize(0, 25))
        self.lineEdit_tableSearchByPointId.setProperty("QLineEditStyle", 1)

        self.verticalLayout_6.addWidget(self.lineEdit_tableSearchByPointId)

        self.label_textResultAnimation3 = QLabel(self.frame_ResultAnimation1)
        self.label_textResultAnimation3.setObjectName(u"label_textResultAnimation3")
        self.label_textResultAnimation3.setMinimumSize(QSize(110, 0))
        self.label_textResultAnimation3.setProperty("QLabelStyle", 3)

        self.verticalLayout_6.addWidget(self.label_textResultAnimation3)

        self.pushButton_ClearTable = QPushButton(self.frame_ResultAnimation1)
        self.pushButton_ClearTable.setObjectName(u"pushButton_ClearTable")
        self.pushButton_ClearTable.setProperty("QPushButtonStyle", 3)

        self.verticalLayout_6.addWidget(self.pushButton_ClearTable)

        self.pushButton_tableShowHideColumn = QPushButton(self.frame_ResultAnimation1)
        self.pushButton_tableShowHideColumn.setObjectName(u"pushButton_tableShowHideColumn")
        self.pushButton_tableShowHideColumn.setProperty("QPushButtonStyle", 3)

        self.verticalLayout_6.addWidget(self.pushButton_tableShowHideColumn)

        self.pushButton_SaveData = QPushButton(self.frame_ResultAnimation1)
        self.pushButton_SaveData.setObjectName(u"pushButton_SaveData")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_SaveData.setIcon(icon2)
        self.pushButton_SaveData.setIconSize(QSize(30, 30))
        self.pushButton_SaveData.setProperty("QPushButtonStyle", 1)

        self.verticalLayout_6.addWidget(self.pushButton_SaveData)


        self.verticalLayout_5.addWidget(self.frame_ResultAnimation1)

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


        self.retranslateUi(FormMenuResultTable)

        QMetaObject.connectSlotsByName(FormMenuResultTable)
    # setupUi

    def retranslateUi(self, FormMenuResultTable):
        FormMenuResultTable.setWindowTitle(QCoreApplication.translate("FormMenuResultTable", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardResultAnimationTitle.setText(QCoreApplication.translate("FormMenuResultTable", u"TABLA RESUMEN", None))
        self.label_cardResultAnimationSubTitle1.setText(QCoreApplication.translate("FormMenuResultTable", u"Datos de visualizaci\u00f3n", None))
        self.toolButton_cardResultAnimationSubTitle1.setText("")
        self.label_textPointMaterialName.setText(QCoreApplication.translate("FormMenuResultTable", u"Filtrar por puntos:", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_tableSearchByPointId.setToolTip(QCoreApplication.translate("FormMenuResultTable", u"<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">Puede buscar por id como 1 o 2 o 3 etc. O por conjuntos separados por coma, por ejemplo 1,2,3\u2026</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_tableSearchByPointId.setInputMask("")
        self.lineEdit_tableSearchByPointId.setText("")
        self.lineEdit_tableSearchByPointId.setPlaceholderText(QCoreApplication.translate("FormMenuResultTable", u"id puntos", None))
        self.label_textResultAnimation3.setText(QCoreApplication.translate("FormMenuResultTable", u"Otras opciones:", None))
        self.pushButton_ClearTable.setText(QCoreApplication.translate("FormMenuResultTable", u"Limpiar tabla", None))
#if QT_CONFIG(whatsthis)
        self.pushButton_tableShowHideColumn.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_tableShowHideColumn.setText(QCoreApplication.translate("FormMenuResultTable", u"Mostrar/ocultar columnas", None))
        self.pushButton_SaveData.setText(QCoreApplication.translate("FormMenuResultTable", u"     Guardar en csv", None))
        self.label_msn.setText(QCoreApplication.translate("FormMenuResultTable", u"Empty", None))
    # retranslateUi

