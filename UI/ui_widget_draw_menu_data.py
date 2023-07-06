# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_draw_menu_dataMtNrMX.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QSpacerItem, QTextEdit, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormDrawMenuData(object):
    def setupUi(self, FormDrawMenuData):
        if not FormDrawMenuData.objectName():
            FormDrawMenuData.setObjectName(u"FormDrawMenuData")
        FormDrawMenuData.resize(350, 616)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FormDrawMenuData.sizePolicy().hasHeightForWidth())
        FormDrawMenuData.setSizePolicy(sizePolicy)
        FormDrawMenuData.setMinimumSize(QSize(0, 0))
        FormDrawMenuData.setMaximumSize(QSize(350, 16777215))
        FormDrawMenuData.setStyleSheet(u"/*Colores primarios*/\n"
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
"QWidget#FormDataProject{\n"
"\n"
"}\n"
"\n"
"QFrame#frame_dataProject{\n"
"background: #333333;\n"
"border-radius: 8px\n"
"}\n"
""
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
"/*####################       FRAME DATA       ###########################*/\n"
"/*#################################################################*/\n"
"QFrame#frame_data{\n"
"background: transparent;\n"
"}\n"
"QFrame#frame_title{\n"
"background: #222222;\n"
"border-top-right-radius: 8px;\n"
"}\n"
"QLabel#label_cardDataTitle{\n"
"font: 700 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QFrame#frame_dataSubTitle1,\n"
"QFrame#frame_dataSub"
                        "Title2,\n"
"QFrame#frame_dataSubTitle3{\n"
"background: #222222;\n"
"border-radius:2px;\n"
"}\n"
"QLabel#label_cardDataSubTitle1,\n"
"QLabel#label_cardDataSubTitle2,\n"
"QLabel#label_cardDataSubTitle3{\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QToolButton#toolButton_cardDataSubTitle1,\n"
"QToolButton#toolButton_cardDataSubTitle2,\n"
"QToolButton#toolButton_cardDataSubTitle3{\n"
"background-color: transparent;\n"
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
"QTextEdit[QTextEditStyle=\"1\"]{\n"
"font: 9pt \"Ubuntu\""
                        ";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
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
"/*\n"
"\n"
"QLabel#label_textData1,\n"
"QLabel#label_textData2,\n"
"QLabel#label_textData3,\n"
"QLabel#label_textData4,\n"
"QLabel#label_textData5{\n"
"font: 300 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"QLineEdit#lineEdit_textData1,\n"
"QLineEdit#lineEdit_textData2,\n"
"QLineEdit#lineEdit_textData3,\n"
"QLineEdi"
                        "t#lineEdit_textData5{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
"\n"
"*/\n"
"QTextEdit#textEdit_textData4{\n"
"font: 9pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"background-color: #444444;\n"
"border-radius: 2px ;\n"
"padding-right: 6px;\n"
"padding-left: 6px;\n"
"}\n"
"QToolButton#toolButton_updateData{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #222222;\n"
"background-color: #77ACA2;\n"
"border: none;\n"
"padding: 6px 25px;\n"
"border-radius: 15px ;\n"
"}\n"
"\n"
"QToolButton#toolButton_saveData:hover{\n"
"background-color: #36C9C6;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QLabel#label_msn{\n"
"font: 500 10pt \"Ubuntu\";\n"
"color: #333333;\n"
"}\n"
"\n"
"\n"
"\n"
"QToolButton[style_draw_button=\"1\"]{\n"
"background-color: transparent;\n"
"border: 1px solid #888888;\n"
"border-radius: 3px ;\n"
"}\n"
"\n"
"QToolButton[style_draw_button=\"1\"]:hover{ \n"
"background-color: #555555;\n"
"}\n"
"QToolButton[style_dr"
                        "aw_button=\"1\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"\n"
"\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(FormDrawMenuData)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.frame_dataProject = QFrame(FormDrawMenuData)
        self.frame_dataProject.setObjectName(u"frame_dataProject")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_dataProject.sizePolicy().hasHeightForWidth())
        self.frame_dataProject.setSizePolicy(sizePolicy1)
        self.frame_dataProject.setFrameShape(QFrame.StyledPanel)
        self.frame_dataProject.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_dataProject)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_hide = QFrame(self.frame_dataProject)
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

        self.frame_data = QFrame(self.frame_dataProject)
        self.frame_data.setObjectName(u"frame_data")
        sizePolicy1.setHeightForWidth(self.frame_data.sizePolicy().hasHeightForWidth())
        self.frame_data.setSizePolicy(sizePolicy1)
        self.frame_data.setFrameShape(QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_data)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.frame_data)
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
        self.label_cardDataTitle = QLabel(self.frame_title)
        self.label_cardDataTitle.setObjectName(u"label_cardDataTitle")

        self.horizontalLayout_2.addWidget(self.label_cardDataTitle)

        self.horizontalSpacer = QSpacerItem(58, 7, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addWidget(self.frame_title)

        self.frame_info = QFrame(self.frame_data)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_info)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_dataSubTitle1 = QFrame(self.frame_info)
        self.frame_dataSubTitle1.setObjectName(u"frame_dataSubTitle1")
        self.frame_dataSubTitle1.setFrameShape(QFrame.StyledPanel)
        self.frame_dataSubTitle1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_dataSubTitle1)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle1 = QLabel(self.frame_dataSubTitle1)
        self.label_cardDataSubTitle1.setObjectName(u"label_cardDataSubTitle1")
        self.label_cardDataSubTitle1.setMinimumSize(QSize(262, 0))

        self.horizontalLayout_7.addWidget(self.label_cardDataSubTitle1)

        self.toolButton_cardDataSubTitle1 = QToolButton(self.frame_dataSubTitle1)
        self.toolButton_cardDataSubTitle1.setObjectName(u"toolButton_cardDataSubTitle1")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataSubTitle1.setIcon(icon1)
        self.toolButton_cardDataSubTitle1.setArrowType(Qt.NoArrow)

        self.horizontalLayout_7.addWidget(self.toolButton_cardDataSubTitle1)


        self.verticalLayout_5.addWidget(self.frame_dataSubTitle1)

        self.frame_data0 = QFrame(self.frame_info)
        self.frame_data0.setObjectName(u"frame_data0")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_data0.sizePolicy().hasHeightForWidth())
        self.frame_data0.setSizePolicy(sizePolicy5)
        self.frame_data0.setMaximumSize(QSize(16777215, 200))
        self.frame_data0.setFrameShape(QFrame.StyledPanel)
        self.frame_data0.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_data0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.toolButton_cardDataDrawRule = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawRule.setObjectName(u"toolButton_cardDataDrawRule")
        self.toolButton_cardDataDrawRule.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawRule.setMaximumSize(QSize(35, 35))
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_menu_draw_mesh/rule.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawRule.setIcon(icon2)
        self.toolButton_cardDataDrawRule.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawRule.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawRule.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawRule, 0, 5, 1, 1)

        self.toolButton_cardDataDrawMove = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawMove.setObjectName(u"toolButton_cardDataDrawMove")
        self.toolButton_cardDataDrawMove.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawMove.setMaximumSize(QSize(35, 35))
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_draw_mesh/move.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawMove.setIcon(icon3)
        self.toolButton_cardDataDrawMove.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawMove.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawMove.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawMove, 1, 2, 1, 1)

        self.toolButton_cardDataDrawCopy = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawCopy.setObjectName(u"toolButton_cardDataDrawCopy")
        self.toolButton_cardDataDrawCopy.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawCopy.setMaximumSize(QSize(35, 35))
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawCopy.setIcon(icon4)
        self.toolButton_cardDataDrawCopy.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawCopy.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawCopy.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawCopy, 1, 4, 1, 1)

        self.toolButton_cardDataDrawPoint = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawPoint.setObjectName(u"toolButton_cardDataDrawPoint")
        sizePolicy5.setHeightForWidth(self.toolButton_cardDataDrawPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_cardDataDrawPoint.setSizePolicy(sizePolicy5)
        self.toolButton_cardDataDrawPoint.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawPoint.setMaximumSize(QSize(35, 35))
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_draw_mesh/point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawPoint.setIcon(icon5)
        self.toolButton_cardDataDrawPoint.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawPoint.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawPoint, 0, 2, 1, 1)

        self.toolButton_cardDataDrawLine = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawLine.setObjectName(u"toolButton_cardDataDrawLine")
        self.toolButton_cardDataDrawLine.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawLine.setMaximumSize(QSize(35, 35))
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_draw_mesh/line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawLine.setIcon(icon6)
        self.toolButton_cardDataDrawLine.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawLine.setArrowType(Qt.NoArrow)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawLine, 0, 3, 1, 1)

        self.toolButton_cardDataDrawErase = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawErase.setObjectName(u"toolButton_cardDataDrawErase")
        self.toolButton_cardDataDrawErase.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawErase.setMaximumSize(QSize(35, 35))
        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/iconos_menu_draw_mesh/erase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawErase.setIcon(icon7)
        self.toolButton_cardDataDrawErase.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawErase.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawErase.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawErase, 1, 5, 1, 1)

        self.toolButton_cardDataDrawImport = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawImport.setObjectName(u"toolButton_cardDataDrawImport")
        self.toolButton_cardDataDrawImport.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawImport.setMaximumSize(QSize(35, 35))
        icon8 = QIcon()
        icon8.addFile(u"recursos/iconos/iconos_menu_draw_mesh/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawImport.setIcon(icon8)
        self.toolButton_cardDataDrawImport.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawImport.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawImport.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawImport, 0, 4, 1, 1)

        self.toolButton_cardDataDrawRotate = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawRotate.setObjectName(u"toolButton_cardDataDrawRotate")
        self.toolButton_cardDataDrawRotate.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawRotate.setMaximumSize(QSize(35, 35))
        icon9 = QIcon()
        icon9.addFile(u"recursos/iconos/iconos_menu_draw_mesh/rotate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawRotate.setIcon(icon9)
        self.toolButton_cardDataDrawRotate.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawRotate.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawRotate.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawRotate, 1, 3, 1, 1)

        self.toolButton_cardDataDrawIntersection = QToolButton(self.frame_data0)
        self.toolButton_cardDataDrawIntersection.setObjectName(u"toolButton_cardDataDrawIntersection")
        self.toolButton_cardDataDrawIntersection.setMinimumSize(QSize(35, 35))
        self.toolButton_cardDataDrawIntersection.setMaximumSize(QSize(35, 35))
        icon10 = QIcon()
        icon10.addFile(u"recursos/iconos/iconos_menu_draw_mesh/point_in_lines.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardDataDrawIntersection.setIcon(icon10)
        self.toolButton_cardDataDrawIntersection.setIconSize(QSize(35, 35))
        self.toolButton_cardDataDrawIntersection.setArrowType(Qt.NoArrow)
        self.toolButton_cardDataDrawIntersection.setProperty("style_draw_button", 1)

        self.gridLayout.addWidget(self.toolButton_cardDataDrawIntersection, 0, 6, 1, 1)


        self.verticalLayout_5.addWidget(self.frame_data0)

        self.frame_dataSubTitle2 = QFrame(self.frame_info)
        self.frame_dataSubTitle2.setObjectName(u"frame_dataSubTitle2")
        self.frame_dataSubTitle2.setFrameShape(QFrame.StyledPanel)
        self.frame_dataSubTitle2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_dataSubTitle2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle2 = QLabel(self.frame_dataSubTitle2)
        self.label_cardDataSubTitle2.setObjectName(u"label_cardDataSubTitle2")
        self.label_cardDataSubTitle2.setMinimumSize(QSize(262, 0))

        self.horizontalLayout_4.addWidget(self.label_cardDataSubTitle2)

        self.toolButton_cardDataSubTitle2 = QToolButton(self.frame_dataSubTitle2)
        self.toolButton_cardDataSubTitle2.setObjectName(u"toolButton_cardDataSubTitle2")
        self.toolButton_cardDataSubTitle2.setIcon(icon1)
        self.toolButton_cardDataSubTitle2.setArrowType(Qt.NoArrow)

        self.horizontalLayout_4.addWidget(self.toolButton_cardDataSubTitle2)


        self.verticalLayout_5.addWidget(self.frame_dataSubTitle2)

        self.frame_data1 = QFrame(self.frame_info)
        self.frame_data1.setObjectName(u"frame_data1")
        self.frame_data1.setFrameShape(QFrame.StyledPanel)
        self.frame_data1.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_data1)
        self.formLayout.setObjectName(u"formLayout")
        self.label_textData_DataTitleProject = QLabel(self.frame_data1)
        self.label_textData_DataTitleProject.setObjectName(u"label_textData_DataTitleProject")
        self.label_textData_DataTitleProject.setMinimumSize(QSize(110, 0))
        self.label_textData_DataTitleProject.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_textData_DataTitleProject)

        self.lineEdit_textData_DataTitleProject = QLineEdit(self.frame_data1)
        self.lineEdit_textData_DataTitleProject.setObjectName(u"lineEdit_textData_DataTitleProject")
        self.lineEdit_textData_DataTitleProject.setMinimumSize(QSize(150, 25))
        self.lineEdit_textData_DataTitleProject.setProperty("QLineEditStyle", 1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textData_DataTitleProject)

        self.label_textData_DataLocation = QLabel(self.frame_data1)
        self.label_textData_DataLocation.setObjectName(u"label_textData_DataLocation")
        self.label_textData_DataLocation.setMinimumSize(QSize(110, 0))
        self.label_textData_DataLocation.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_textData_DataLocation)

        self.lineEdit_textData_DataLocation = QLineEdit(self.frame_data1)
        self.lineEdit_textData_DataLocation.setObjectName(u"lineEdit_textData_DataLocation")
        self.lineEdit_textData_DataLocation.setMinimumSize(QSize(150, 25))
        self.lineEdit_textData_DataLocation.setProperty("QLineEditStyle", 1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_textData_DataLocation)

        self.label_textData_DataAuthor = QLabel(self.frame_data1)
        self.label_textData_DataAuthor.setObjectName(u"label_textData_DataAuthor")
        self.label_textData_DataAuthor.setMinimumSize(QSize(110, 0))
        self.label_textData_DataAuthor.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_textData_DataAuthor)

        self.lineEdit_textData_DataAuthor = QLineEdit(self.frame_data1)
        self.lineEdit_textData_DataAuthor.setObjectName(u"lineEdit_textData_DataAuthor")
        self.lineEdit_textData_DataAuthor.setMinimumSize(QSize(150, 25))
        self.lineEdit_textData_DataAuthor.setProperty("QLineEditStyle", 1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.lineEdit_textData_DataAuthor)

        self.label_textData_DataDescription = QLabel(self.frame_data1)
        self.label_textData_DataDescription.setObjectName(u"label_textData_DataDescription")
        self.label_textData_DataDescription.setMinimumSize(QSize(110, 0))
        self.label_textData_DataDescription.setProperty("QLabelStyle", 3)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_textData_DataDescription)

        self.textEdit_textData_DataDescription = QTextEdit(self.frame_data1)
        self.textEdit_textData_DataDescription.setObjectName(u"textEdit_textData_DataDescription")
        sizePolicy6 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.textEdit_textData_DataDescription.sizePolicy().hasHeightForWidth())
        self.textEdit_textData_DataDescription.setSizePolicy(sizePolicy6)
        self.textEdit_textData_DataDescription.setMinimumSize(QSize(150, 75))
        self.textEdit_textData_DataDescription.setProperty("QTextEditStyle", 1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.textEdit_textData_DataDescription)


        self.verticalLayout_5.addWidget(self.frame_data1)

        self.frame_dataSubTitle3 = QFrame(self.frame_info)
        self.frame_dataSubTitle3.setObjectName(u"frame_dataSubTitle3")
        self.frame_dataSubTitle3.setFrameShape(QFrame.StyledPanel)
        self.frame_dataSubTitle3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_dataSubTitle3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.label_cardDataSubTitle3 = QLabel(self.frame_dataSubTitle3)
        self.label_cardDataSubTitle3.setObjectName(u"label_cardDataSubTitle3")
        self.label_cardDataSubTitle3.setMinimumSize(QSize(262, 0))

        self.horizontalLayout_3.addWidget(self.label_cardDataSubTitle3)

        self.toolButton_cardDataSubTitle3 = QToolButton(self.frame_dataSubTitle3)
        self.toolButton_cardDataSubTitle3.setObjectName(u"toolButton_cardDataSubTitle3")
        self.toolButton_cardDataSubTitle3.setIcon(icon1)
        self.toolButton_cardDataSubTitle3.setArrowType(Qt.NoArrow)

        self.horizontalLayout_3.addWidget(self.toolButton_cardDataSubTitle3)


        self.verticalLayout_5.addWidget(self.frame_dataSubTitle3)

        self.frame_data2 = QFrame(self.frame_info)
        self.frame_data2.setObjectName(u"frame_data2")
        self.frame_data2.setFrameShape(QFrame.StyledPanel)
        self.frame_data2.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_data2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_textData_DataGravity = QLabel(self.frame_data2)
        self.label_textData_DataGravity.setObjectName(u"label_textData_DataGravity")
        self.label_textData_DataGravity.setMinimumSize(QSize(110, 0))
        self.label_textData_DataGravity.setProperty("QLabelStyle", 3)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_textData_DataGravity)

        self.lineEdit_textData_DataGravity = QLineEdit(self.frame_data2)
        self.lineEdit_textData_DataGravity.setObjectName(u"lineEdit_textData_DataGravity")
        self.lineEdit_textData_DataGravity.setMinimumSize(QSize(150, 25))
        self.lineEdit_textData_DataGravity.setProperty("QLineEditStyle", 1)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_textData_DataGravity)


        self.verticalLayout_5.addWidget(self.frame_data2)

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

        self.toolButton_updateData = QToolButton(self.frame_info)
        self.toolButton_updateData.setObjectName(u"toolButton_updateData")

        self.horizontalLayout_5.addWidget(self.toolButton_updateData)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame_info)


        self.horizontalLayout.addWidget(self.frame_data)


        self.horizontalLayout_6.addWidget(self.frame_dataProject)


        self.retranslateUi(FormDrawMenuData)

        QMetaObject.connectSlotsByName(FormDrawMenuData)
    # setupUi

    def retranslateUi(self, FormDrawMenuData):
        FormDrawMenuData.setWindowTitle(QCoreApplication.translate("FormDrawMenuData", u"Form", None))
        self.toolButton_hideShow.setText("")
        self.label_cardDataTitle.setText(QCoreApplication.translate("FormDrawMenuData", u"DIBUJO E INFORMACI\u00d3N DEL PROYECTO", None))
        self.label_cardDataSubTitle1.setText(QCoreApplication.translate("FormDrawMenuData", u"Dibujo", None))
        self.toolButton_cardDataSubTitle1.setText("")
        self.toolButton_cardDataDrawRule.setText("")
        self.toolButton_cardDataDrawMove.setText("")
        self.toolButton_cardDataDrawCopy.setText("")
        self.toolButton_cardDataDrawPoint.setText("")
        self.toolButton_cardDataDrawPoint.setProperty("style_draw_button", QCoreApplication.translate("FormDrawMenuData", u"1", None))
        self.toolButton_cardDataDrawLine.setText("")
        self.toolButton_cardDataDrawLine.setProperty("style_draw_button", QCoreApplication.translate("FormDrawMenuData", u"1", None))
        self.toolButton_cardDataDrawErase.setText("")
        self.toolButton_cardDataDrawImport.setText("")
        self.toolButton_cardDataDrawRotate.setText("")
        self.toolButton_cardDataDrawIntersection.setText("")
        self.label_cardDataSubTitle2.setText(QCoreApplication.translate("FormDrawMenuData", u"Datos del proyecto", None))
        self.toolButton_cardDataSubTitle2.setText("")
        self.label_textData_DataTitleProject.setText(QCoreApplication.translate("FormDrawMenuData", u"T\u00edtulo del proyecto:", None))
        self.label_textData_DataLocation.setText(QCoreApplication.translate("FormDrawMenuData", u"Localizaci\u00f3n:", None))
        self.label_textData_DataAuthor.setText(QCoreApplication.translate("FormDrawMenuData", u"Autor:", None))
        self.label_textData_DataDescription.setText(QCoreApplication.translate("FormDrawMenuData", u"Descripci\u00f3n:", None))
        self.label_cardDataSubTitle3.setText(QCoreApplication.translate("FormDrawMenuData", u"Configuraci\u00f3n del proyecto", None))
        self.toolButton_cardDataSubTitle3.setText("")
        self.label_textData_DataGravity.setText(QCoreApplication.translate("FormDrawMenuData", u"<html><head/><body><p>Gravedad [m/s<span style=\" vertical-align:super;\">2</span>]:</p></body></html>", None))
        self.lineEdit_textData_DataGravity.setText("")
        self.label_msn.setText(QCoreApplication.translate("FormDrawMenuData", u"Empty", None))
        self.toolButton_updateData.setText(QCoreApplication.translate("FormDrawMenuData", u"Actualizar", None))
    # retranslateUi

