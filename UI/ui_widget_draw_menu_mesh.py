# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_meshCziUld.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QScrollArea, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_FormDrawMenuMesh(object):
    def setupUi(self, FormDrawMenuMesh):
        if not FormDrawMenuMesh.objectName():
            FormDrawMenuMesh.setObjectName(u"FormDrawMenuMesh")
        FormDrawMenuMesh.resize(350, 782)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuMesh.sizePolicy().hasHeightForWidth())
        FormDrawMenuMesh.setSizePolicy(sizePolicy)
        FormDrawMenuMesh.setMinimumSize(QSize(0, 0))
        FormDrawMenuMesh.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuMesh.setStyleSheet(u"/*Colores primarios*/\n"
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
"QFrame#frame_meshProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
"\n"
"/*########################"
                        "#########################################*/\n"
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
"QLabel#label_cardMeshTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_meshSubTitle0,\n"
"QFrame#frame_meshSubTitle1,\n"
"QFrame#frame_meshSu"
                        "bTitle2,\n"
"QFrame#frame_meshSubTitle3{\n"
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
"QToolButton#toolButton_cardMeshDraw7,\n"
"QToolButton#toolButton_cardMeshDraw5,\n"
"QToolButton#toolButton_cardMeshDraw6{\n"
"background-color: transparent;\n"
"border: 1px solid #222222;\n"
"border-radius: 3px;\n"
"margin-left: 4px;\n"
"}\n"
"\n"
"\n"
"QToolButton#toolButton_cardMeshDraw7:hover,\n"
"QToolButton#toolButton_cardMeshDraw5:hover, \n"
"QToolButton#toolButton_cardMeshDraw6:hover{ \n"
"background-color: #444444;\n"
"}\n"
"QToolButton#toolButton_cardMeshDraw7:pressed,\n"
"QToolButton#toolButton_cardMeshDraw5:pressed,\n"
"QToolButton#toolButton_cardMeshDraw6:pressed"
                        "{\n"
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
""
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
"	subcontrol-origin: margin;\n"
"}\n"
""
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
"background-color: #666666;\n"
"border: none;\n"
"border-t"
                        "op-left-radius: 7px;\n"
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
"QDoubleSpinBox[QDoubleSpinBoxStyle=\""
                        "1\"]{\n"
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
""
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
"Azules #36C9C6 #00BDB9 #77ACA2\n"
"rojos #910D3F #C70039 #F94646\n"
"naranjas #D34E24 #F2"
                        "8123 #F7F052\n"
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
""
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
"color: #DDDDDD;\n"
"background-color: #333333;\n"
"border: 1px solid #444444"
                        ";\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QToolButton           \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
"/*\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8           QComboBox            \u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8"
                        "\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8\u25d8*/\n"
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
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuMesh)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_meshProject = QFrame(FormDrawMenuMesh)
        self.frame_meshProject.setObjectName(u"frame_meshProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_meshProject.sizePolicy().hasHeightForWidth())
        self.frame_meshProject.setSizePolicy(sizePolicy1)
        self.frame_meshProject.setFrameShape(QFrame.StyledPanel)
        self.frame_meshProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_meshProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_meshProject)
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

        self.frame_mesh = QFrame(self.frame_meshProject)
        self.frame_mesh.setObjectName(u"frame_mesh")
        sizePolicy1.setHeightForWidth(self.frame_mesh.sizePolicy().hasHeightForWidth())
        self.frame_mesh.setSizePolicy(sizePolicy1)
        self.frame_mesh.setFrameShape(QFrame.StyledPanel)
        self.frame_mesh.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_mesh)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_mesh)
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
        self.label_cardMeshTitle = QLabel(self.frame_title)
        self.label_cardMeshTitle.setObjectName(u"label_cardMeshTitle")
        self.label_cardMeshTitle.setProperty("QLabelStyle", 1)

        self.horizontalLayout_2.addWidget(self.label_cardMeshTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_mesh)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_meshSubTitle0 = QFrame(self.frame_info)
        self.frame_meshSubTitle0.setObjectName(u"frame_meshSubTitle0")
        self.frame_meshSubTitle0.setFrameShape(QFrame.StyledPanel)
        self.frame_meshSubTitle0.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_meshSubTitle0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 0)
        self.label_cardMeshSubTitle0 = QLabel(self.frame_meshSubTitle0)
        self.label_cardMeshSubTitle0.setObjectName(u"label_cardMeshSubTitle0")
        self.label_cardMeshSubTitle0.setMinimumSize(QSize(262, 0))
        self.label_cardMeshSubTitle0.setProperty("QLabelStyle", 2)

        self.horizontalLayout_16.addWidget(self.label_cardMeshSubTitle0)

        self.toolButton_cardMeshSubTitle0 = QToolButton(self.frame_meshSubTitle0)
        self.toolButton_cardMeshSubTitle0.setObjectName(u"toolButton_cardMeshSubTitle0")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshSubTitle0.setIcon(icon1)
        self.toolButton_cardMeshSubTitle0.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshSubTitle0.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_16.addWidget(self.toolButton_cardMeshSubTitle0)


        self.verticalLayout_5.addWidget(self.frame_meshSubTitle0)

        self.frame_mesh2_2 = QFrame(self.frame_info)
        self.frame_mesh2_2.setObjectName(u"frame_mesh2_2")
        sizePolicy1.setHeightForWidth(self.frame_mesh2_2.sizePolicy().hasHeightForWidth())
        self.frame_mesh2_2.setSizePolicy(sizePolicy1)
        self.frame_mesh2_2.setFrameShape(QFrame.StyledPanel)
        self.frame_mesh2_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_mesh2_2)
        self.verticalLayout_7.setSpacing(8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_4 = QFrame(self.frame_mesh2_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.frame_4)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setHorizontalSpacing(0)
        self.formLayout_4.setVerticalSpacing(6)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_textMesh1_2 = QLabel(self.frame_4)
        self.label_textMesh1_2.setObjectName(u"label_textMesh1_2")
        self.label_textMesh1_2.setMinimumSize(QSize(110, 0))
        self.label_textMesh1_2.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_textMesh1_2)

        self.doubleSpinBoxl_textMeshDx = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textMeshDx.setObjectName(u"doubleSpinBoxl_textMeshDx")
        self.doubleSpinBoxl_textMeshDx.setEnabled(True)
        self.doubleSpinBoxl_textMeshDx.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textMeshDx.setDecimals(2)
        self.doubleSpinBoxl_textMeshDx.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textMeshDx.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textMeshDx.setValue(1.000000000000000)
        self.doubleSpinBoxl_textMeshDx.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.doubleSpinBoxl_textMeshDx)

        self.label_textMesh2_2 = QLabel(self.frame_4)
        self.label_textMesh2_2.setObjectName(u"label_textMesh2_2")
        self.label_textMesh2_2.setMinimumSize(QSize(110, 0))
        self.label_textMesh2_2.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_textMesh2_2)

        self.doubleSpinBoxl_textMeshDy = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textMeshDy.setObjectName(u"doubleSpinBoxl_textMeshDy")
        self.doubleSpinBoxl_textMeshDy.setEnabled(True)
        self.doubleSpinBoxl_textMeshDy.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textMeshDy.setDecimals(2)
        self.doubleSpinBoxl_textMeshDy.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textMeshDy.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textMeshDy.setValue(1.000000000000000)
        self.doubleSpinBoxl_textMeshDy.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.doubleSpinBoxl_textMeshDy)

        self.label_textMesh2_3 = QLabel(self.frame_4)
        self.label_textMesh2_3.setObjectName(u"label_textMesh2_3")
        self.label_textMesh2_3.setMinimumSize(QSize(110, 0))
        self.label_textMesh2_3.setProperty("QLabelStyle", 3)

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.label_textMesh2_3)

        self.doubleSpinBoxl_textMeshSize_2 = QDoubleSpinBox(self.frame_4)
        self.doubleSpinBoxl_textMeshSize_2.setObjectName(u"doubleSpinBoxl_textMeshSize_2")
        self.doubleSpinBoxl_textMeshSize_2.setEnabled(True)
        self.doubleSpinBoxl_textMeshSize_2.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textMeshSize_2.setDecimals(2)
        self.doubleSpinBoxl_textMeshSize_2.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textMeshSize_2.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textMeshSize_2.setValue(1.000000000000000)
        self.doubleSpinBoxl_textMeshSize_2.setProperty("QDoubleSpinBoxStyle", 1)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.doubleSpinBoxl_textMeshSize_2)

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

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.frame_2)


        self.verticalLayout_7.addWidget(self.frame_4)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_7)

        self.toolButton_cardMeshDrawUpdate = QToolButton(self.frame_mesh2_2)
        self.toolButton_cardMeshDrawUpdate.setObjectName(u"toolButton_cardMeshDrawUpdate")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_menu_draw_mesh/update.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawUpdate.setIcon(icon2)
        self.toolButton_cardMeshDrawUpdate.setIconSize(QSize(20, 20))
        self.toolButton_cardMeshDrawUpdate.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawUpdate.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_18.addWidget(self.toolButton_cardMeshDrawUpdate)

        self.frame_5 = QFrame(self.frame_mesh2_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(10, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_18.addWidget(self.frame_5)

        self.toolButton_meshShow = QToolButton(self.frame_mesh2_2)
        self.toolButton_meshShow.setObjectName(u"toolButton_meshShow")
        self.toolButton_meshShow.setMinimumSize(QSize(120, 0))
        self.toolButton_meshShow.setMaximumSize(QSize(150, 16777215))
        self.toolButton_meshShow.setProperty("QToolButtonStyle", 5)

        self.horizontalLayout_18.addWidget(self.toolButton_meshShow)

        self.toolButton_meshHide = QToolButton(self.frame_mesh2_2)
        self.toolButton_meshHide.setObjectName(u"toolButton_meshHide")
        self.toolButton_meshHide.setMinimumSize(QSize(120, 0))
        self.toolButton_meshHide.setMaximumSize(QSize(150, 16777215))
        self.toolButton_meshHide.setProperty("QToolButtonStyle", 8)

        self.horizontalLayout_18.addWidget(self.toolButton_meshHide)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_8)


        self.verticalLayout_7.addLayout(self.horizontalLayout_18)


        self.verticalLayout_5.addWidget(self.frame_mesh2_2)

        self.frame_meshSubTitle1 = QFrame(self.frame_info)
        self.frame_meshSubTitle1.setObjectName(u"frame_meshSubTitle1")
        self.frame_meshSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_meshSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_meshSubTitle1)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardMeshSubTitle1 = QLabel(self.frame_meshSubTitle1)
        self.label_cardMeshSubTitle1.setObjectName(u"label_cardMeshSubTitle1")
        self.label_cardMeshSubTitle1.setMinimumSize(QSize(262, 0))
        self.label_cardMeshSubTitle1.setProperty("QLabelStyle", 2)

        self.horizontalLayout_3.addWidget(self.label_cardMeshSubTitle1)

        self.toolButton_cardMeshSubTitle1 = QToolButton(self.frame_meshSubTitle1)
        self.toolButton_cardMeshSubTitle1.setObjectName(u"toolButton_cardMeshSubTitle1")
        self.toolButton_cardMeshSubTitle1.setIcon(icon1)
        self.toolButton_cardMeshSubTitle1.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshSubTitle1.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_3.addWidget(self.toolButton_cardMeshSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_meshSubTitle1)

        self.frame_mesh2 = QFrame(self.frame_info)
        self.frame_mesh2.setObjectName(u"frame_mesh2")
        sizePolicy1.setHeightForWidth(self.frame_mesh2.sizePolicy().hasHeightForWidth())
        self.frame_mesh2.setSizePolicy(sizePolicy1)
        self.frame_mesh2.setFrameShape(QFrame.StyledPanel)
        self.frame_mesh2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_mesh2)
        self.verticalLayout_6.setSpacing(15)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_3 = QFrame(self.frame_mesh2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.frame_3)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(0)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_textMesh1 = QLabel(self.frame_3)
        self.label_textMesh1.setObjectName(u"label_textMesh1")
        self.label_textMesh1.setMinimumSize(QSize(110, 0))
        self.label_textMesh1.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_textMesh1)

        self.label_textMesh2 = QLabel(self.frame_3)
        self.label_textMesh2.setObjectName(u"label_textMesh2")
        self.label_textMesh2.setMinimumSize(QSize(110, 0))
        self.label_textMesh2.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_textMesh2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lineEdit_textMeshColor = QLineEdit(self.frame_3)
        self.lineEdit_textMeshColor.setObjectName(u"lineEdit_textMeshColor")
        self.lineEdit_textMeshColor.setEnabled(False)
        self.lineEdit_textMeshColor.setMinimumSize(QSize(120, 25))
        self.lineEdit_textMeshColor.setMaximumSize(QSize(16777215, 16777215))
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
        self.lineEdit_textMeshColor.setPalette(palette)
        self.lineEdit_textMeshColor.setStyleSheet(u"")
        self.lineEdit_textMeshColor.setProperty("QLineEditStyle", 2)

        self.horizontalLayout_9.addWidget(self.lineEdit_textMeshColor)

        self.toolButton_cardMeshDrawColor = QToolButton(self.frame_3)
        self.toolButton_cardMeshDrawColor.setObjectName(u"toolButton_cardMeshDrawColor")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_draw_mesh/colo_picker.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawColor.setIcon(icon3)
        self.toolButton_cardMeshDrawColor.setIconSize(QSize(20, 20))
        self.toolButton_cardMeshDrawColor.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawColor.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_9.addWidget(self.toolButton_cardMeshDrawColor)


        self.formLayout_3.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_9)

        self.label_textMesh3 = QLabel(self.frame_3)
        self.label_textMesh3.setObjectName(u"label_textMesh3")
        self.label_textMesh3.setMinimumSize(QSize(110, 0))
        self.label_textMesh3.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_textMesh3)

        self.lineEdit_textMeshName = QLineEdit(self.frame_3)
        self.lineEdit_textMeshName.setObjectName(u"lineEdit_textMeshName")
        self.lineEdit_textMeshName.setMinimumSize(QSize(150, 25))
        self.lineEdit_textMeshName.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textMeshName.setProperty("QLineEditStyle", 1)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textMeshName)

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
        self.doubleSpinBoxl_textMeshSize = QDoubleSpinBox(self.frame)
        self.doubleSpinBoxl_textMeshSize.setObjectName(u"doubleSpinBoxl_textMeshSize")
        self.doubleSpinBoxl_textMeshSize.setEnabled(True)
        self.doubleSpinBoxl_textMeshSize.setMinimumSize(QSize(120, 25))
        self.doubleSpinBoxl_textMeshSize.setDecimals(2)
        self.doubleSpinBoxl_textMeshSize.setMinimum(0.010000000000000)
        self.doubleSpinBoxl_textMeshSize.setSingleStep(0.010000000000000)
        self.doubleSpinBoxl_textMeshSize.setValue(1.000000000000000)
        self.doubleSpinBoxl_textMeshSize.setProperty("QDoubleSpinBoxStyle", 1)

        self.horizontalLayout_10.addWidget(self.doubleSpinBoxl_textMeshSize)

        self.toolButton_cardMeshDrawSize = QToolButton(self.frame)
        self.toolButton_cardMeshDrawSize.setObjectName(u"toolButton_cardMeshDrawSize")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/click.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawSize.setIcon(icon4)
        self.toolButton_cardMeshDrawSize.setIconSize(QSize(20, 20))
        self.toolButton_cardMeshDrawSize.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawSize.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_10.addWidget(self.toolButton_cardMeshDrawSize)


        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.frame)

        self.label_textMesh4 = QLabel(self.frame_3)
        self.label_textMesh4.setObjectName(u"label_textMesh4")
        self.label_textMesh4.setMinimumSize(QSize(110, 0))
        self.label_textMesh4.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_textMesh4)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit_textMeshSelected = QLineEdit(self.frame_3)
        self.lineEdit_textMeshSelected.setObjectName(u"lineEdit_textMeshSelected")
        self.lineEdit_textMeshSelected.setEnabled(False)
        self.lineEdit_textMeshSelected.setMinimumSize(QSize(120, 25))
        self.lineEdit_textMeshSelected.setMaximumSize(QSize(16777215, 16777215))
        self.lineEdit_textMeshSelected.setProperty("QLineEditStyle", 2)

        self.horizontalLayout_11.addWidget(self.lineEdit_textMeshSelected)

        self.toolButton_cardMeshDrawSelected = QToolButton(self.frame_3)
        self.toolButton_cardMeshDrawSelected.setObjectName(u"toolButton_cardMeshDrawSelected")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_draw_mesh/select.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawSelected.setIcon(icon5)
        self.toolButton_cardMeshDrawSelected.setIconSize(QSize(20, 20))
        self.toolButton_cardMeshDrawSelected.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawSelected.setProperty("QToolButtonStyle", 1)

        self.horizontalLayout_11.addWidget(self.toolButton_cardMeshDrawSelected)


        self.formLayout_3.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_11)

        self.label_textMesh5 = QLabel(self.frame_3)
        self.label_textMesh5.setObjectName(u"label_textMesh5")
        self.label_textMesh5.setMinimumSize(QSize(110, 0))
        self.label_textMesh5.setProperty("QLabelStyle", 3)

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_textMesh5)

        self.comboBox_MeshType = QComboBox(self.frame_3)
        self.comboBox_MeshType.setObjectName(u"comboBox_MeshType")
        self.comboBox_MeshType.setMinimumSize(QSize(0, 25))
        self.comboBox_MeshType.setProperty("QComboBoxStyle", 1)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.comboBox_MeshType)


        self.verticalLayout_6.addWidget(self.frame_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.toolButton_meshCancel = QToolButton(self.frame_mesh2)
        self.toolButton_meshCancel.setObjectName(u"toolButton_meshCancel")
        self.toolButton_meshCancel.setMinimumSize(QSize(80, 0))
        self.toolButton_meshCancel.setMaximumSize(QSize(150, 16777215))
        self.toolButton_meshCancel.setProperty("QToolButtonStyle", 3)

        self.horizontalLayout_12.addWidget(self.toolButton_meshCancel)

        self.toolButton_meshMeshing = QToolButton(self.frame_mesh2)
        self.toolButton_meshMeshing.setObjectName(u"toolButton_meshMeshing")
        self.toolButton_meshMeshing.setMinimumSize(QSize(150, 0))
        self.toolButton_meshMeshing.setMaximumSize(QSize(150, 16777215))
        self.toolButton_meshMeshing.setProperty("QToolButtonStyle", 2)

        self.horizontalLayout_12.addWidget(self.toolButton_meshMeshing)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_6.addLayout(self.horizontalLayout_12)


        self.verticalLayout_5.addWidget(self.frame_mesh2)

        self.frame_meshSubTitle2 = QFrame(self.frame_info)
        self.frame_meshSubTitle2.setObjectName(u"frame_meshSubTitle2")
        self.frame_meshSubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_meshSubTitle2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_meshSubTitle2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardMeshSubTitle2 = QLabel(self.frame_meshSubTitle2)
        self.label_cardMeshSubTitle2.setObjectName(u"label_cardMeshSubTitle2")
        self.label_cardMeshSubTitle2.setMinimumSize(QSize(262, 0))
        self.label_cardMeshSubTitle2.setProperty("QLabelStyle", 2)

        self.horizontalLayout_7.addWidget(self.label_cardMeshSubTitle2)

        self.toolButton_showHideLabel = QToolButton(self.frame_meshSubTitle2)
        self.toolButton_showHideLabel.setObjectName(u"toolButton_showHideLabel")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_draw_mesh/label_not.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideLabel.setIcon(icon6)
        self.toolButton_showHideLabel.setArrowType(Qt.NoArrow)
        self.toolButton_showHideLabel.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideLabel)

        self.toolButton_showHideMesh = QToolButton(self.frame_meshSubTitle2)
        self.toolButton_showHideMesh.setObjectName(u"toolButton_showHideMesh")
        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/iconos_menu_draw_mesh/view_draw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_showHideMesh.setIcon(icon7)
        self.toolButton_showHideMesh.setArrowType(Qt.NoArrow)
        self.toolButton_showHideMesh.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_showHideMesh)

        self.toolButton_cardMeshSubTitle2 = QToolButton(self.frame_meshSubTitle2)
        self.toolButton_cardMeshSubTitle2.setObjectName(u"toolButton_cardMeshSubTitle2")
        self.toolButton_cardMeshSubTitle2.setIcon(icon1)
        self.toolButton_cardMeshSubTitle2.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshSubTitle2.setProperty("QToolButtonSubTitleStyle", 1)

        self.horizontalLayout_7.addWidget(self.toolButton_cardMeshSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_meshSubTitle2)

        self.frame_mesh3 = QFrame(self.frame_info)
        self.frame_mesh3.setObjectName(u"frame_mesh3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_mesh3.sizePolicy().hasHeightForWidth())
        self.frame_mesh3.setSizePolicy(sizePolicy5)
        self.frame_mesh3.setMinimumSize(QSize(0, 150))
        self.frame_mesh3.setStyleSheet(u"")
        self.frame_mesh3.setFrameShape(QFrame.StyledPanel)
        self.frame_mesh3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_mesh3)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.scrollArea = QScrollArea(self.frame_mesh3)
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
        self.verticalLayout_containerCardMesh = QVBoxLayout()
        self.verticalLayout_containerCardMesh.setSpacing(0)
        self.verticalLayout_containerCardMesh.setObjectName(u"verticalLayout_containerCardMesh")
        self.frame_empty = QFrame(self.scrollAreaWidgetContents)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy5.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy5)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.StyledPanel)
        self.frame_empty.setFrameShadow(QFrame.Raised)

        self.verticalLayout_containerCardMesh.addWidget(self.frame_empty)


        self.horizontalLayout_14.addLayout(self.verticalLayout_containerCardMesh)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_13.addWidget(self.scrollArea)


        self.verticalLayout_5.addWidget(self.frame_mesh3)

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


        self.horizontalLayout.addWidget(self.frame_mesh)


        self.horizontalLayout_6.addWidget(self.frame_meshProject)


        self.retranslateUi(FormDrawMenuMesh)

        QMetaObject.connectSlotsByName(FormDrawMenuMesh)
    # setupUi

    def retranslateUi(self, FormDrawMenuMesh):
        FormDrawMenuMesh.setWindowTitle(QCoreApplication.translate("FormDrawMenuMesh", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardMeshTitle.setText(QCoreApplication.translate("FormDrawMenuMesh", u"MALLADO", None))
        self.label_cardMeshSubTitle0.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Crear malla de fondo", None))
        self.toolButton_cardMeshSubTitle0.setText("")
        self.label_textMesh1_2.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Ancho (dx):", None))
        self.doubleSpinBoxl_textMeshDx.setSuffix(QCoreApplication.translate("FormDrawMenuMesh", u"m", None))
        self.label_textMesh2_2.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Alto (dy):", None))
        self.doubleSpinBoxl_textMeshDy.setSuffix(QCoreApplication.translate("FormDrawMenuMesh", u"m", None))
        self.label_textMesh2_3.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Tama\u00f1o del elemento :", None))
        self.doubleSpinBoxl_textMeshSize_2.setSuffix(QCoreApplication.translate("FormDrawMenuMesh", u"m", None))
        self.toolButton_cardMeshDrawUpdate.setText("")
        self.toolButton_meshShow.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Motrar", None))
        self.toolButton_meshHide.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Ocultar", None))
        self.label_cardMeshSubTitle1.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Crear malla para PM", None))
        self.toolButton_cardMeshSubTitle1.setText("")
        self.label_textMesh1.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Nombre:", None))
        self.label_textMesh2.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Color:", None))
        self.lineEdit_textMeshColor.setText("")
        self.toolButton_cardMeshDrawColor.setText("")
        self.label_textMesh3.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Tama\u00f1o de la malla:", None))
        self.lineEdit_textMeshName.setText("")
        self.doubleSpinBoxl_textMeshSize.setSuffix(QCoreApplication.translate("FormDrawMenuMesh", u"m", None))
        self.toolButton_cardMeshDrawSize.setText("")
        self.label_textMesh4.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Seleccionar:", None))
        self.lineEdit_textMeshSelected.setText("")
        self.toolButton_cardMeshDrawSelected.setText("")
        self.label_textMesh5.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Tipo malla:", None))
        self.toolButton_meshCancel.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Cancelar", None))
        self.toolButton_meshMeshing.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Mallar", None))
        self.label_cardMeshSubTitle2.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Lista de mallas", None))
        self.toolButton_showHideLabel.setText("")
        self.toolButton_showHideMesh.setText("")
        self.toolButton_cardMeshSubTitle2.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuMesh", u"Empty", None))
    # retranslateUi

