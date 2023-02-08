# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_drawHDtkni.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QSplitter, QTextBrowser, QToolButton, QUndoView,
    QVBoxLayout, QWidget)

class Ui_FormDraw(object):
    def setupUi(self, FormDraw):
        if not FormDraw.objectName():
            FormDraw.setObjectName(u"FormDraw")
        FormDraw.resize(462, 513)
        FormDraw.setStyleSheet(u"\n"
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
"/****************************************************************************************************************************************************/\n"
"\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*######################      PAGE DRAW      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"\n"
"\n"
"/*###################### frame consola  ##########################"
                        "##*/\n"
"\n"
"QFrame#frame_3{\n"
"background-color: #333333;\n"
"border-top-right-radius: 8px ;\n"
"\n"
"}\n"
"\n"
"\n"
"QFrame#frame_console{\n"
"background-color: #333333;\n"
"}\n"
"\n"
"QTextBrowser#textBrowser_2{\n"
"background-color: #555555;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"border-top-right-radius: 8px ;\n"
"\n"
"}\n"
"QToolButton[style_console_button=\"1\"]{\n"
"background-color: transparent;\n"
"}\n"
"\n"
"QLineEdit#lineEdit_console{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius: 5px ;\n"
"\n"
"padding-left: 10px;\n"
"}\n"
"\n"
"#label_console_command{\n"
"background-color: #444444;\n"
"font: 700 10pt \"Ubuntu\";\n"
"color: #FFFFFF;\n"
"border-top-left-radius: 5px ;\n"
"border-bottom-left-radius: 5px ;\n"
"margin-left: 10px;\n"
"border-top: 1px solid rgb(254, 255, 198);\n"
"border-bottom: 1px solid rgb(254, 255, 198);\n"
"border-left: 1px solid rgb(254, 255, 198);\n"
"}\n"
"\n"
"#label_console_descrip{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-"
                        "top: 1px solid rgb(254, 255, 198);\n"
"border-bottom: 1px solid rgb(254, 255, 198);\n"
"}\n"
"\n"
"#undoView_draw{\n"
"background-color: #333333;\n"
"font: 300 10pt \"Ubuntu\";\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"\n"
"QLineEdit#lineEdit_console:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"/*\n"
"QLineEdit#lineEdit_console:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"*/\n"
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
"QToolButton[style_draw_button=\"1\"]:pressed{\n"
"border-top: 2px solid #222222;\n"
"border-left: 2px solid #222222;\n"
"}  \n"
"")
        self.horizontalLayout_3 = QHBoxLayout(FormDraw)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_draw = QHBoxLayout()
        self.horizontalLayout_draw.setSpacing(0)
        self.horizontalLayout_draw.setObjectName(u"horizontalLayout_draw")
        self.splitter = QSplitter(FormDraw)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout_graphics = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_graphics.setSpacing(0)
        self.horizontalLayout_graphics.setObjectName(u"horizontalLayout_graphics")
        self.horizontalLayout_graphics.setContentsMargins(0, 0, 0, 0)
        self.splitter.addWidget(self.horizontalLayoutWidget)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.frame_3.setLineWidth(0)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(8)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 8, 8, 0)
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.textBrowser_2 = QTextBrowser(self.frame_3)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy)
        self.textBrowser_2.setMinimumSize(QSize(0, 38))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser_2.setStyleSheet(u"")
        self.textBrowser_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setOpenExternalLinks(False)
        self.textBrowser_2.setOpenLinks(False)

        self.horizontalLayout_16.addWidget(self.textBrowser_2)

        self.undoView_draw = QUndoView(self.frame_3)
        self.undoView_draw.setObjectName(u"undoView_draw")
        sizePolicy.setHeightForWidth(self.undoView_draw.sizePolicy().hasHeightForWidth())
        self.undoView_draw.setSizePolicy(sizePolicy)
        self.undoView_draw.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_16.addWidget(self.undoView_draw)


        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.frame_console = QFrame(self.frame_3)
        self.frame_console.setObjectName(u"frame_console")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_console.sizePolicy().hasHeightForWidth())
        self.frame_console.setSizePolicy(sizePolicy2)
        self.frame_console.setStyleSheet(u"")
        self.frame_console.setFrameShape(QFrame.StyledPanel)
        self.frame_console.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_console)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 3)
        self.toolButton_closeConsole = QToolButton(self.frame_console)
        self.toolButton_closeConsole.setObjectName(u"toolButton_closeConsole")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.toolButton_closeConsole.sizePolicy().hasHeightForWidth())
        self.toolButton_closeConsole.setSizePolicy(sizePolicy3)
        self.toolButton_closeConsole.setMinimumSize(QSize(20, 20))
        self.toolButton_closeConsole.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(7)
        self.toolButton_closeConsole.setFont(font)
        self.toolButton_closeConsole.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_closeConsole.setIcon(icon)
        self.toolButton_closeConsole.setIconSize(QSize(15, 15))
        self.toolButton_closeConsole.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_closeConsole)

        self.toolButton_zoomExtend = QToolButton(self.frame_console)
        self.toolButton_zoomExtend.setObjectName(u"toolButton_zoomExtend")
        sizePolicy3.setHeightForWidth(self.toolButton_zoomExtend.sizePolicy().hasHeightForWidth())
        self.toolButton_zoomExtend.setSizePolicy(sizePolicy3)
        self.toolButton_zoomExtend.setMinimumSize(QSize(20, 20))
        self.toolButton_zoomExtend.setMaximumSize(QSize(20, 20))
        self.toolButton_zoomExtend.setFont(font)
        self.toolButton_zoomExtend.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_consola/zoom_extend.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_zoomExtend.setIcon(icon1)
        self.toolButton_zoomExtend.setIconSize(QSize(19, 19))
        self.toolButton_zoomExtend.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_zoomExtend)

        self.toolButton_zoomWindow = QToolButton(self.frame_console)
        self.toolButton_zoomWindow.setObjectName(u"toolButton_zoomWindow")
        sizePolicy3.setHeightForWidth(self.toolButton_zoomWindow.sizePolicy().hasHeightForWidth())
        self.toolButton_zoomWindow.setSizePolicy(sizePolicy3)
        self.toolButton_zoomWindow.setMinimumSize(QSize(20, 20))
        self.toolButton_zoomWindow.setMaximumSize(QSize(20, 20))
        self.toolButton_zoomWindow.setFont(font)
        self.toolButton_zoomWindow.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_consola/zoom_window.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_zoomWindow.setIcon(icon2)
        self.toolButton_zoomWindow.setIconSize(QSize(19, 19))
        self.toolButton_zoomWindow.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_zoomWindow)

        self.toolButton_views = QToolButton(self.frame_console)
        self.toolButton_views.setObjectName(u"toolButton_views")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(50)
        sizePolicy4.setVerticalStretch(50)
        sizePolicy4.setHeightForWidth(self.toolButton_views.sizePolicy().hasHeightForWidth())
        self.toolButton_views.setSizePolicy(sizePolicy4)
        self.toolButton_views.setMinimumSize(QSize(20, 20))
        self.toolButton_views.setMaximumSize(QSize(20, 20))
        self.toolButton_views.setFont(font)
        self.toolButton_views.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_consola/view_two.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_views.setIcon(icon3)
        self.toolButton_views.setIconSize(QSize(19, 19))
        self.toolButton_views.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_views)

        self.label_4 = QLabel(self.frame_console)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)
        self.label_4.setMinimumSize(QSize(20, 20))
        self.label_4.setMaximumSize(QSize(20, 20))
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setPixmap(QPixmap(u"recursos/iconos/iconos_consola/code.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.comboBox_console = QComboBox(self.frame_console)
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_draw_mesh/line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_console.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_draw_mesh/polyline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_console.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_draw_mesh/rectangle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox_console.addItem(icon6, "")
        self.comboBox_console.setObjectName(u"comboBox_console")

        self.horizontalLayout_2.addWidget(self.comboBox_console)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_console_command = QLabel(self.frame_console)
        self.label_console_command.setObjectName(u"label_console_command")

        self.horizontalLayout.addWidget(self.label_console_command)

        self.label_console_descrip = QLabel(self.frame_console)
        self.label_console_descrip.setObjectName(u"label_console_descrip")

        self.horizontalLayout.addWidget(self.label_console_descrip)

        self.lineEdit_console = QLineEdit(self.frame_console)
        self.lineEdit_console.setObjectName(u"lineEdit_console")
        self.lineEdit_console.setMinimumSize(QSize(0, 25))
        self.lineEdit_console.setMaximumSize(QSize(16777215, 25))
        font1 = QFont()
        font1.setPointSize(8)
        self.lineEdit_console.setFont(font1)
        self.lineEdit_console.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.lineEdit_console)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addWidget(self.frame_console)

        self.splitter.addWidget(self.frame_3)

        self.horizontalLayout_draw.addWidget(self.splitter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.toolButton_cardMeshDrawPoint = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawPoint.setObjectName(u"toolButton_cardMeshDrawPoint")
        self.toolButton_cardMeshDrawPoint.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawPoint.setMaximumSize(QSize(35, 35))
        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/iconos_menu_draw_mesh/point.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawPoint.setIcon(icon7)
        self.toolButton_cardMeshDrawPoint.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawPoint.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawPoint)

        self.toolButton_cardMeshDrawLine = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawLine.setObjectName(u"toolButton_cardMeshDrawLine")
        self.toolButton_cardMeshDrawLine.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawLine.setMaximumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawLine.setIcon(icon4)
        self.toolButton_cardMeshDrawLine.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawLine.setArrowType(Qt.NoArrow)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawLine)

        self.toolButton_cardMeshDrawRect = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawRect.setObjectName(u"toolButton_cardMeshDrawRect")
        self.toolButton_cardMeshDrawRect.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawRect.setMaximumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawRect.setIcon(icon6)
        self.toolButton_cardMeshDrawRect.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawRect.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawRect.setProperty("style_draw_button", 1)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawRect)

        self.toolButton_cardMeshDrawMove = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawMove.setObjectName(u"toolButton_cardMeshDrawMove")
        self.toolButton_cardMeshDrawMove.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawMove.setMaximumSize(QSize(35, 35))
        icon8 = QIcon()
        icon8.addFile(u"recursos/iconos/iconos_menu_draw_mesh/move.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawMove.setIcon(icon8)
        self.toolButton_cardMeshDrawMove.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawMove.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawMove.setProperty("style_draw_button", 1)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawMove)

        self.toolButton_cardMeshDrawCopy = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawCopy.setObjectName(u"toolButton_cardMeshDrawCopy")
        self.toolButton_cardMeshDrawCopy.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawCopy.setMaximumSize(QSize(35, 35))
        icon9 = QIcon()
        icon9.addFile(u"recursos/iconos/iconos_menu_draw_mesh/copy.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawCopy.setIcon(icon9)
        self.toolButton_cardMeshDrawCopy.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawCopy.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawCopy.setProperty("style_draw_button", 1)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawCopy)

        self.toolButton_cardMeshDrawRotate = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawRotate.setObjectName(u"toolButton_cardMeshDrawRotate")
        self.toolButton_cardMeshDrawRotate.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawRotate.setMaximumSize(QSize(35, 35))
        icon10 = QIcon()
        icon10.addFile(u"recursos/iconos/iconos_menu_draw_mesh/rotate.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawRotate.setIcon(icon10)
        self.toolButton_cardMeshDrawRotate.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawRotate.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawRotate.setProperty("style_draw_button", 1)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawRotate)

        self.toolButton_cardMeshDrawErase = QToolButton(FormDraw)
        self.toolButton_cardMeshDrawErase.setObjectName(u"toolButton_cardMeshDrawErase")
        self.toolButton_cardMeshDrawErase.setMinimumSize(QSize(35, 35))
        self.toolButton_cardMeshDrawErase.setMaximumSize(QSize(35, 35))
        icon11 = QIcon()
        icon11.addFile(u"recursos/iconos/iconos_menu_draw_mesh/erase.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_cardMeshDrawErase.setIcon(icon11)
        self.toolButton_cardMeshDrawErase.setIconSize(QSize(35, 35))
        self.toolButton_cardMeshDrawErase.setArrowType(Qt.NoArrow)
        self.toolButton_cardMeshDrawErase.setProperty("style_draw_button", 1)

        self.verticalLayout.addWidget(self.toolButton_cardMeshDrawErase)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout_draw.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_draw)


        self.retranslateUi(FormDraw)

        self.comboBox_console.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(FormDraw)
    # setupUi

    def retranslateUi(self, FormDraw):
        FormDraw.setWindowTitle(QCoreApplication.translate("FormDraw", u"Form", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("FormDraw", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.toolButton_closeConsole.setText("")
        self.toolButton_closeConsole.setProperty("style_console_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.toolButton_zoomExtend.setText("")
        self.toolButton_zoomExtend.setProperty("style_console_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.toolButton_zoomWindow.setText("")
        self.toolButton_zoomWindow.setProperty("style_console_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.toolButton_views.setText("")
        self.toolButton_views.setProperty("style_console_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.label_4.setText("")
        self.comboBox_console.setItemText(0, QCoreApplication.translate("FormDraw", u"_line", None))
        self.comboBox_console.setItemText(1, QCoreApplication.translate("FormDraw", u"_polyLine", None))
        self.comboBox_console.setItemText(2, QCoreApplication.translate("FormDraw", u"_rectangle", None))

        self.label_console_command.setText("")
        self.label_console_descrip.setText("")
        self.lineEdit_console.setInputMask("")
        self.lineEdit_console.setText("")
        self.lineEdit_console.setPlaceholderText(QCoreApplication.translate("FormDraw", u"Ingrese comando", None))
        self.toolButton_cardMeshDrawPoint.setText("")
        self.toolButton_cardMeshDrawPoint.setProperty("style_draw_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.toolButton_cardMeshDrawLine.setText("")
        self.toolButton_cardMeshDrawLine.setProperty("style_draw_button", QCoreApplication.translate("FormDraw", u"1", None))
        self.toolButton_cardMeshDrawRect.setText("")
        self.toolButton_cardMeshDrawMove.setText("")
        self.toolButton_cardMeshDrawCopy.setText("")
        self.toolButton_cardMeshDrawRotate.setText("")
        self.toolButton_cardMeshDrawErase.setText("")
    # retranslateUi

