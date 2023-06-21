# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowoXPrnj.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSpacerItem, QStackedWidget, QStatusBar, QToolButton,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1118, 871)
        icon = QIcon()
        icon.addFile(u"recursos/iconos/iconos_logo/Logo_WindowIcon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
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
"QMainWindow#MainWindow{\n"
"background: #333333;\n"
"}\n"
"\n"
"#page_config{\n"
"background: #222222;\n"
"}\n"
"\n"
"/*####################       MENU BAR SUP      ###########################*/\n"
"QMenuBar#menubar {\n"
"background-color: #333333;\n"
"spacing: 5px; \n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubunt"
                        "u\";\n"
"}\n"
"QMenuBar#menubar::item {\n"
"padding: 5px 5px;\n"
"background-color: transparent;\n"
"border-radius: 2px;\n"
"}\n"
"QMenuBar#menubar::item:selected { \n"
"background-color: #222222;\n"
"}\n"
"QMenuBar#menubar::item:pressed {\n"
"background-color: #222222;\n"
"}\n"
"QMenu {\n"
"background-color: #333333;\n"
"border-radius: 4px; \n"
"border: 1px solid #222222;\n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubuntu\";\n"
"}\n"
"QMenu::item {\n"
"background-color: transparent; \n"
"padding: 5px 20px;\n"
"margin: 2px 10px; \n"
"}\n"
"QMenu::item:selected { \n"
"background-color: #444444;\n"
"color: #C8CC8E;\n"
"font: 500 10pt \"Ubuntu\";\n"
"}\n"
"QMenu::item:checked {\n"
"color: #DDDDDD;\n"
"}\n"
"QMenu::item:unchecked { \n"
"color: #999999;\n"
"}\n"
"\n"
"\n"
"/*####################         STATUS BAR          ##########################*/\n"
"QStatusbar#statusbar{\n"
"background-color: #333333;\n"
"}\n"
"\n"
"\n"
"/*####################     FRAME MENU IZQ      ##########################*/\n"
"QToolButton#"
                        "toolButton_home,\n"
"QToolButton#toolButton_drawPoint,\n"
"QToolButton#toolButton_drawBoundary,\n"
"QToolButton#toolButton_drawData,\n"
"QToolButton#toolButton_drawMesh,\n"
"QToolButton#toolButton_viewResult,\n"
"QToolButton#toolButton_setting{\n"
"background-color: transparent;\n"
"color: #DDDDDD;\n"
"font: 500 7pt \"Ubuntu\";\n"
"border: none;\n"
"padding: 8px 0px;\n"
"}\n"
"\n"
"QFrame#frame_home{\n"
"background: #222222;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QFrame#frame_viewResult,\n"
"QFrame#frame_drawPoint,\n"
"QFrame#frame_drawBoundary,\n"
"QFrame#frame_drawData,\n"
"QFrame#frame_drawMesh{\n"
"background: #333333;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"/*######################      CONTAINER PAGE       ############################*/\n"
"QFrame#frame_empty{\n"
"background-color: #444444;\n"
"}\n"
"\n"
"\n"
"\n"
"/*######################      SETTING       ############################*/\n"
"\n"
"\n"
"#scrollAreaWidgetContents,\n"
"#scrollArea{\n"
""
                        "background-color: transparent;\n"
"border: none;\n"
"}\n"
"#lineEdit_settingSearch{\n"
"font:  10pt \"Ubuntu\";\n"
"background: #555555;\n"
"border: none;\n"
"border-radius: 4px ;\n"
"padding-left: 20px;\n"
"color: #DDDDDD;\n"
"}\n"
"\n"
"#lineEdit_settingSearch:hover {\n"
"	 border-width: 1px; \n"
"	border-style: solid; \n"
"	border-color: #0D99FF; \n"
"\n"
"}\n"
"\n"
"#frame_3{\n"
"\n"
" border-width: 1px; \n"
"border-style: solid; \n"
"border-color: transparent #888888 transparent transparent; \n"
"}\n"
"\n"
"\n"
"/*####################     general setting     ##########################*/\n"
"/*crear un propiedad personalizada  a un widget y asignarle un estilo*/\n"
"/*https://stackoverflow.com/questions/46070524/qt-set-style-sheet-for-multiple-labels*/\n"
"/*https://stackoverflow.com/questions/29736228/is-it-possible-to-set-add-custom-properties-to-qt-widgets-in-qtcreator*/\n"
"\n"
"/*etiquetas lateral izq*/ \n"
"QLabel[type_label=\"1\"]{\n"
"color: #DDDDDD;\n"
"font: 300 8pt \"Ubuntu\";\n"
"}\n"
"/*titulo"
                        "s*/\n"
" QLabel[type_label=\"2\"]{\n"
"color: #DDDDDD;\n"
"font: 800 18pt \"Ubuntu\";\n"
"margin-bottom: 10px;\n"
"margin-top: 20px;\n"
"}\n"
"/*sub titulos*/\n"
" QLabel[type_label=\"3\"]{\n"
"color: #DDDDDD;\n"
"font: 500 12pt \"Ubuntu\";\n"
"}\n"
"\n"
"/*descripciones*/\n"
" QLabel[type_label=\"4\"]{\n"
"color: #DDDDDD;\n"
"font: 300 10pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"/*####################     tabla setting     ##########################*/\n"
"\n"
"/* titulos de la tabla*/\n"
" QLabel[type_label_table=\"1\"]{\n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubuntu\";\n"
"background: #222222;\n"
"min-height:40px;\n"
"text-align: center;\n"
"}\n"
"\n"
" QLabel[type_label_title_table=\"1\"]{\n"
"border-top-left-radius: 10px;\n"
"}\n"
" QLabel[type_label_title_table=\"2\"]{\n"
"border-top-right-radius: 10px;\n"
"}\n"
"\n"
"\n"
"\n"
"/*descripciones tipo 1 de la tabla*/\n"
" QLabel[type_label_table=\"2\"]{\n"
"color: #DDDDDD;\n"
"font: 10pt \"Ubuntu\";\n"
"background: #3d3d3d;\n"
"padding-left:10px;\n"
"min-height:30"
                        "px;\n"
"max-height:30px;\n"
"}\n"
"/*frame tipo 1 de la tabla*/\n"
" QFrame[type_frame_table=\"2\"]{\n"
"background: #3d3d3d;\n"
"padding-left:10px;\n"
"min-height:30px;\n"
"}\n"
"\n"
"/*descripciones tipo 2 de la tabla*/\n"
" QLabel[type_label_table=\"3\"]{\n"
"color: #DDDDDD;\n"
"font: 10pt \"Ubuntu\";\n"
"background: #393939;\n"
"padding-left:10px;\n"
"min-height:30px;\n"
"}\n"
"\n"
"/*frame tipo 1 de la tabla*/\n"
" QFrame[type_frame_table=\"3\"]{\n"
"background: #393939;\n"
"padding-left:10px;\n"
"min-height:30px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*atajos de teclado*/\n"
" QLabel[type_label_table=\"4\"]{\n"
"	color: #DDDDDD;\n"
"	font: 10pt \"Ubuntu\";\n"
"	background: #373737;\n"
"  	border-width: 1; \n"
"	border-style: solid; \n"
"	border-color: #555555; \n"
"	margin: 3px 0px 3px 0px;\n"
"}\n"
"\n"
"/*atajos de teclado aux*/\n"
" QLabel[type_label_table=\"5\"]{\n"
"	color: #DDDDDD;\n"
"	font: 900 12pt \"Ubuntu\";\n"
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
"\n"
"\n"
"QFrame[type_frame=\"1\"]{\n"
""
                        "background: #333333;\n"
"border-radius: 5px ;\n"
"}\n"
"QFrame[type_frame=\"1\"]:hover{\n"
"background: #373737;\n"
"border: 1px solid #888888;\n"
"}\n"
"\n"
"QComboBox{\n"
"background: transparent;\n"
"border: 1px solid #555555;\n"
"border-radius: 3px ;\n"
"color: #DDDDDD;\n"
"font:  10pt \"Ubuntu\";\n"
"}\n"
"QComboBox:hover{\n"
"border-color: #0D99FF; \n"
"}\n"
"QComboBox:disabled {\n"
"	border-color: #444444; \n"
"	color: #444444;\n"
"}\n"
"\n"
"\n"
"\n"
"QDoubleSpinBox[type_spinBox=\"1\"],\n"
"QSpinBox[type_spinBox=\"1\"] {\n"
"    padding-right: 15px; \n"
"    border-width: 1; \n"
"	border-style: solid; \n"
"	border-color: #555555; \n"
"	border-radius: 3px ;\n"
"	background: transparent;\n"
"	color: #DDDDDD;\n"
"	font:  10pt \"Ubuntu\";\n"
"}\n"
"\n"
"QDoubleSpinBox[type_spinBox=\"1\"]:hover,\n"
"QSpinBox[type_spinBox=\"1\"]:hover {\n"
"	border-color: #0D99FF; \n"
"}\n"
"QDoubleSpinBox[type_spinBox=\"1\"]:disabled,\n"
"QSpinBox[type_spinBox=\"1\"]:disabled {\n"
"	border-color: #444444; \n"
"	color: #4444"
                        "44;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    border: 1px solid darkgray;\n"
"    background: #333333;\n"
"	border-radius: 2px ;\n"
"	padding: 2px;\n"
"	selection-background-color: red;\n"
"	color: #dddddd;\n"
"	font:  10pt \"Ubuntu\";\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"/*QSlider#horizontalSlider_1::handle:horizontal {*/\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 1px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 12px;\n"
"    margin: -10px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */\n"
"    border-radius: 3px;\n"
"}\n"
"QSlider:"
                        ":handle:horizontal:hover {\n"
"    border: 1px solid #0D99FF;\n"
"\n"
"}\n"
"\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: white;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: #C8CC8E;\n"
"}\n"
"\n"
"\n"
"QCheckBox{\n"
"	color: #DDDDDD;\n"
"	font:  10pt \"Ubuntu\";\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 15px;\n"
"    height: 15px;\n"
"}\n"
"\n"
"")
        self.action_nuevo = QAction(MainWindow)
        self.action_nuevo.setObjectName(u"action_nuevo")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_superior/new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_nuevo.setIcon(icon1)
        self.action_abrir = QAction(MainWindow)
        self.action_abrir.setObjectName(u"action_abrir")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_menu_superior/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_abrir.setIcon(icon2)
        self.action_guardar = QAction(MainWindow)
        self.action_guardar.setObjectName(u"action_guardar")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_superior/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_guardar.setIcon(icon3)
        self.action_guardarComo = QAction(MainWindow)
        self.action_guardarComo.setObjectName(u"action_guardarComo")
        self.action_importar = QAction(MainWindow)
        self.action_importar.setObjectName(u"action_importar")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_superior/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_importar.setIcon(icon4)
        self.action_exportar = QAction(MainWindow)
        self.action_exportar.setObjectName(u"action_exportar")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_superior/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_exportar.setIcon(icon5)
        self.action_ayuda = QAction(MainWindow)
        self.action_ayuda.setObjectName(u"action_ayuda")
        self.action_acerdaDe = QAction(MainWindow)
        self.action_acerdaDe.setObjectName(u"action_acerdaDe")
        self.action_grid = QAction(MainWindow)
        self.action_grid.setObjectName(u"action_grid")
        self.action_grid.setCheckable(True)
        self.action_rule = QAction(MainWindow)
        self.action_rule.setObjectName(u"action_rule")
        self.action_rule.setCheckable(True)
        self.action_rule.setEnabled(True)
        self.action_dibujo = QAction(MainWindow)
        self.action_dibujo.setObjectName(u"action_dibujo")
        self.action_dibujo.setCheckable(True)
        self.action_console = QAction(MainWindow)
        self.action_console.setObjectName(u"action_console")
        self.action_console.setCheckable(True)
        self.action_origin = QAction(MainWindow)
        self.action_origin.setObjectName(u"action_origin")
        self.action_origin.setCheckable(True)
        self.action_opcionVisualizacion = QAction(MainWindow)
        self.action_opcionVisualizacion.setObjectName(u"action_opcionVisualizacion")
        self.action_deshacer = QAction(MainWindow)
        self.action_deshacer.setObjectName(u"action_deshacer")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_superior/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_deshacer.setIcon(icon6)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.action_deshacer.setFont(font)
        self.action_rehacer = QAction(MainWindow)
        self.action_rehacer.setObjectName(u"action_rehacer")
        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/iconos_menu_superior/redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_rehacer.setIcon(icon7)
        self.action_copiar = QAction(MainWindow)
        self.action_copiar.setObjectName(u"action_copiar")
        self.action_pegar = QAction(MainWindow)
        self.action_pegar.setObjectName(u"action_pegar")
        self.action_cortar = QAction(MainWindow)
        self.action_cortar.setObjectName(u"action_cortar")
        self.action_listadoRecinetes = QAction(MainWindow)
        self.action_listadoRecinetes.setObjectName(u"action_listadoRecinetes")
        self.action_axis = QAction(MainWindow)
        self.action_axis.setObjectName(u"action_axis")
        self.action_axis.setCheckable(True)
        self.action_label = QAction(MainWindow)
        self.action_label.setObjectName(u"action_label")
        self.action_label.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout_7 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menuLeft = QFrame(self.frame)
        self.frame_menuLeft.setObjectName(u"frame_menuLeft")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menuLeft.sizePolicy().hasHeightForWidth())
        self.frame_menuLeft.setSizePolicy(sizePolicy)
        self.frame_menuLeft.setMinimumSize(QSize(0, 0))
        self.frame_menuLeft.setMaximumSize(QSize(16777215, 16777215))
        self.frame_menuLeft.setStyleSheet(u"")
        self.frame_menuLeft.setFrameShape(QFrame.StyledPanel)
        self.frame_menuLeft.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menuLeft)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_homeInf = QFrame(self.frame_menuLeft)
        self.frame_homeInf.setObjectName(u"frame_homeInf")
        self.frame_homeInf.setFrameShape(QFrame.StyledPanel)
        self.frame_homeInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_homeInf)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.toolButton_home = QToolButton(self.frame_homeInf)
        self.toolButton_home.setObjectName(u"toolButton_home")
        self.toolButton_home.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_home.sizePolicy().hasHeightForWidth())
        self.toolButton_home.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u"recursos/iconos/iconos_menu_lateral/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_home.setIcon(icon8)
        self.toolButton_home.setIconSize(QSize(30, 30))
        self.toolButton_home.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_22.addWidget(self.toolButton_home)

        self.frame_home = QFrame(self.frame_homeInf)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setMinimumSize(QSize(5, 0))
        self.frame_home.setMaximumSize(QSize(5, 16777215))
        self.frame_home.setStyleSheet(u"")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_home)


        self.verticalLayout_2.addWidget(self.frame_homeInf)

        self.frame_drawDataInf = QFrame(self.frame_menuLeft)
        self.frame_drawDataInf.setObjectName(u"frame_drawDataInf")
        self.frame_drawDataInf.setFrameShape(QFrame.StyledPanel)
        self.frame_drawDataInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_drawDataInf)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.toolButton_drawData = QToolButton(self.frame_drawDataInf)
        self.toolButton_drawData.setObjectName(u"toolButton_drawData")
        self.toolButton_drawData.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_drawData.sizePolicy().hasHeightForWidth())
        self.toolButton_drawData.setSizePolicy(sizePolicy1)
        self.toolButton_drawData.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"recursos/iconos/iconos_menu_lateral/control.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_drawData.setIcon(icon9)
        self.toolButton_drawData.setIconSize(QSize(30, 30))
        self.toolButton_drawData.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_21.addWidget(self.toolButton_drawData)

        self.frame_drawData = QFrame(self.frame_drawDataInf)
        self.frame_drawData.setObjectName(u"frame_drawData")
        self.frame_drawData.setEnabled(True)
        self.frame_drawData.setMinimumSize(QSize(5, 0))
        self.frame_drawData.setMaximumSize(QSize(5, 16777215))
        self.frame_drawData.setStyleSheet(u"")
        self.frame_drawData.setFrameShape(QFrame.StyledPanel)
        self.frame_drawData.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_drawData)


        self.verticalLayout_2.addWidget(self.frame_drawDataInf)

        self.frame_drawMeshInf = QFrame(self.frame_menuLeft)
        self.frame_drawMeshInf.setObjectName(u"frame_drawMeshInf")
        self.frame_drawMeshInf.setFrameShape(QFrame.StyledPanel)
        self.frame_drawMeshInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_drawMeshInf)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.toolButton_drawMesh = QToolButton(self.frame_drawMeshInf)
        self.toolButton_drawMesh.setObjectName(u"toolButton_drawMesh")
        self.toolButton_drawMesh.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_drawMesh.sizePolicy().hasHeightForWidth())
        self.toolButton_drawMesh.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u"recursos/iconos/iconos_menu_lateral/mesh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_drawMesh.setIcon(icon10)
        self.toolButton_drawMesh.setIconSize(QSize(30, 30))
        self.toolButton_drawMesh.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_20.addWidget(self.toolButton_drawMesh)

        self.frame_drawMesh = QFrame(self.frame_drawMeshInf)
        self.frame_drawMesh.setObjectName(u"frame_drawMesh")
        self.frame_drawMesh.setEnabled(True)
        self.frame_drawMesh.setMinimumSize(QSize(5, 0))
        self.frame_drawMesh.setMaximumSize(QSize(5, 16777215))
        self.frame_drawMesh.setStyleSheet(u"")
        self.frame_drawMesh.setFrameShape(QFrame.StyledPanel)
        self.frame_drawMesh.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_drawMesh)


        self.verticalLayout_2.addWidget(self.frame_drawMeshInf)

        self.frame_drawPointInf = QFrame(self.frame_menuLeft)
        self.frame_drawPointInf.setObjectName(u"frame_drawPointInf")
        self.frame_drawPointInf.setFrameShape(QFrame.StyledPanel)
        self.frame_drawPointInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_drawPointInf)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolButton_drawPoint = QToolButton(self.frame_drawPointInf)
        self.toolButton_drawPoint.setObjectName(u"toolButton_drawPoint")
        self.toolButton_drawPoint.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_drawPoint.sizePolicy().hasHeightForWidth())
        self.toolButton_drawPoint.setSizePolicy(sizePolicy1)
        icon11 = QIcon()
        icon11.addFile(u"recursos/iconos/iconos_menu_lateral/particle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_drawPoint.setIcon(icon11)
        self.toolButton_drawPoint.setIconSize(QSize(30, 30))
        self.toolButton_drawPoint.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.toolButton_drawPoint)

        self.frame_drawPoint = QFrame(self.frame_drawPointInf)
        self.frame_drawPoint.setObjectName(u"frame_drawPoint")
        self.frame_drawPoint.setEnabled(True)
        self.frame_drawPoint.setMinimumSize(QSize(5, 0))
        self.frame_drawPoint.setMaximumSize(QSize(5, 16777215))
        self.frame_drawPoint.setStyleSheet(u"")
        self.frame_drawPoint.setFrameShape(QFrame.StyledPanel)
        self.frame_drawPoint.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_drawPoint)


        self.verticalLayout_2.addWidget(self.frame_drawPointInf)

        self.frame_drawBoundaryInf = QFrame(self.frame_menuLeft)
        self.frame_drawBoundaryInf.setObjectName(u"frame_drawBoundaryInf")
        self.frame_drawBoundaryInf.setFrameShape(QFrame.StyledPanel)
        self.frame_drawBoundaryInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_drawBoundaryInf)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolButton_drawBoundary = QToolButton(self.frame_drawBoundaryInf)
        self.toolButton_drawBoundary.setObjectName(u"toolButton_drawBoundary")
        self.toolButton_drawBoundary.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_drawBoundary.sizePolicy().hasHeightForWidth())
        self.toolButton_drawBoundary.setSizePolicy(sizePolicy1)
        icon12 = QIcon()
        icon12.addFile(u"recursos/iconos/iconos_menu_lateral/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_drawBoundary.setIcon(icon12)
        self.toolButton_drawBoundary.setIconSize(QSize(30, 30))
        self.toolButton_drawBoundary.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.toolButton_drawBoundary)

        self.frame_drawBoundary = QFrame(self.frame_drawBoundaryInf)
        self.frame_drawBoundary.setObjectName(u"frame_drawBoundary")
        self.frame_drawBoundary.setMinimumSize(QSize(5, 0))
        self.frame_drawBoundary.setMaximumSize(QSize(5, 16777215))
        self.frame_drawBoundary.setStyleSheet(u"")
        self.frame_drawBoundary.setFrameShape(QFrame.StyledPanel)
        self.frame_drawBoundary.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_drawBoundary)


        self.verticalLayout_2.addWidget(self.frame_drawBoundaryInf)

        self.frame_viewResultInf = QFrame(self.frame_menuLeft)
        self.frame_viewResultInf.setObjectName(u"frame_viewResultInf")
        self.frame_viewResultInf.setFrameShape(QFrame.StyledPanel)
        self.frame_viewResultInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_viewResultInf)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toolButton_viewResult = QToolButton(self.frame_viewResultInf)
        self.toolButton_viewResult.setObjectName(u"toolButton_viewResult")
        self.toolButton_viewResult.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.toolButton_viewResult.sizePolicy().hasHeightForWidth())
        self.toolButton_viewResult.setSizePolicy(sizePolicy1)
        icon13 = QIcon()
        icon13.addFile(u"recursos/iconos/iconos_menu_lateral/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_viewResult.setIcon(icon13)
        self.toolButton_viewResult.setIconSize(QSize(30, 30))
        self.toolButton_viewResult.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.toolButton_viewResult)

        self.frame_viewResult = QFrame(self.frame_viewResultInf)
        self.frame_viewResult.setObjectName(u"frame_viewResult")
        self.frame_viewResult.setEnabled(True)
        self.frame_viewResult.setMinimumSize(QSize(5, 0))
        self.frame_viewResult.setMaximumSize(QSize(5, 16777215))
        self.frame_viewResult.setStyleSheet(u"")
        self.frame_viewResult.setFrameShape(QFrame.StyledPanel)
        self.frame_viewResult.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_viewResult)


        self.verticalLayout_2.addWidget(self.frame_viewResultInf)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolButton_setting = QToolButton(self.frame_menuLeft)
        self.toolButton_setting.setObjectName(u"toolButton_setting")
        sizePolicy1.setHeightForWidth(self.toolButton_setting.sizePolicy().hasHeightForWidth())
        self.toolButton_setting.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setItalic(False)
        self.toolButton_setting.setFont(font1)
        icon14 = QIcon()
        icon14.addFile(u"recursos/iconos/iconos_menu_lateral/config.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_setting.setIcon(icon14)
        self.toolButton_setting.setIconSize(QSize(30, 30))
        self.toolButton_setting.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_2.addWidget(self.toolButton_setting)


        self.horizontalLayout_3.addWidget(self.frame_menuLeft)

        self.frame_empty = QFrame(self.frame)
        self.frame_empty.setObjectName(u"frame_empty")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_empty.sizePolicy().hasHeightForWidth())
        self.frame_empty.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(7)
        self.frame_empty.setFont(font2)
        self.frame_empty.setStyleSheet(u"")
        self.frame_empty.setFrameShape(QFrame.NoFrame)
        self.frame_empty.setFrameShadow(QFrame.Raised)
        self.frame_empty.setLineWidth(0)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_empty)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_container = QStackedWidget(self.frame_empty)
        self.stackedWidget_container.setObjectName(u"stackedWidget_container")
        self.stackedWidget_container.setFrameShape(QFrame.NoFrame)
        self.stackedWidget_container.setFrameShadow(QFrame.Raised)
        self.stackedWidget_container.setLineWidth(0)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_17 = QHBoxLayout(self.page_home)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_emptyHome = QVBoxLayout()
        self.verticalLayout_emptyHome.setObjectName(u"verticalLayout_emptyHome")

        self.horizontalLayout_17.addLayout(self.verticalLayout_emptyHome)

        self.stackedWidget_container.addWidget(self.page_home)
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.horizontalLayout = QHBoxLayout(self.page_draw)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_emptyDraw = QVBoxLayout()
        self.verticalLayout_emptyDraw.setObjectName(u"verticalLayout_emptyDraw")

        self.horizontalLayout.addLayout(self.verticalLayout_emptyDraw)

        self.stackedWidget_container.addWidget(self.page_draw)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.label_2 = QLabel(self.page_view)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(340, 290, 144, 90))
        font3 = QFont()
        font3.setPointSize(50)
        self.label_2.setFont(font3)
        self.stackedWidget_container.addWidget(self.page_view)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.verticalLayout = QVBoxLayout(self.page_config)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_emptySetting = QVBoxLayout()
        self.verticalLayout_emptySetting.setObjectName(u"verticalLayout_emptySetting")

        self.verticalLayout.addLayout(self.verticalLayout_emptySetting)

        self.stackedWidget_container.addWidget(self.page_config)

        self.horizontalLayout_19.addWidget(self.stackedWidget_container)


        self.horizontalLayout_3.addWidget(self.frame_empty)


        self.horizontalLayout_7.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1118, 26))
        self.menu_archivo = QMenu(self.menubar)
        self.menu_archivo.setObjectName(u"menu_archivo")
        self.menu_archivo.setGeometry(QRect(2269, 217, 186, 293))
        font4 = QFont()
        font4.setFamilies([u"Ubuntu"])
        font4.setPointSize(10)
        font4.setBold(False)
        font4.setItalic(False)
        self.menu_archivo.setFont(font4)
        self.menu_archivo.setMouseTracking(True)
        self.menu_recientes = QMenu(self.menu_archivo)
        self.menu_recientes.setObjectName(u"menu_recientes")
        self.menu_recientes.setFont(font4)
        icon15 = QIcon()
        icon15.addFile(u"recursos/iconos/iconos_menu_superior/recent.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_recientes.setIcon(icon15)
        self.menu_editar = QMenu(self.menubar)
        self.menu_editar.setObjectName(u"menu_editar")
        self.menu_editar.setFont(font4)
        self.menu_vista = QMenu(self.menubar)
        self.menu_vista.setObjectName(u"menu_vista")
        self.menu_vista.setFont(font4)
        self.menu_ayuda = QMenu(self.menubar)
        self.menu_ayuda.setObjectName(u"menu_ayuda")
        self.menu_ayuda.setFont(font4)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_archivo.menuAction())
        self.menubar.addAction(self.menu_editar.menuAction())
        self.menubar.addAction(self.menu_vista.menuAction())
        self.menubar.addAction(self.menu_ayuda.menuAction())
        self.menu_archivo.addAction(self.action_nuevo)
        self.menu_archivo.addAction(self.action_abrir)
        self.menu_archivo.addAction(self.menu_recientes.menuAction())
        self.menu_archivo.addAction(self.action_guardar)
        self.menu_archivo.addAction(self.action_guardarComo)
        self.menu_archivo.addSeparator()
        self.menu_archivo.addSeparator()
        self.menu_archivo.addAction(self.action_importar)
        self.menu_archivo.addAction(self.action_exportar)
        self.menu_archivo.addSeparator()
        self.menu_recientes.addAction(self.action_listadoRecinetes)
        self.menu_editar.addAction(self.action_deshacer)
        self.menu_editar.addAction(self.action_rehacer)
        self.menu_editar.addSeparator()
        self.menu_editar.addAction(self.action_copiar)
        self.menu_editar.addAction(self.action_pegar)
        self.menu_editar.addAction(self.action_cortar)
        self.menu_vista.addAction(self.action_origin)
        self.menu_vista.addAction(self.action_axis)
        self.menu_vista.addAction(self.action_grid)
        self.menu_vista.addAction(self.action_console)
        self.menu_vista.addAction(self.action_label)
        self.menu_vista.addAction(self.action_rule)
        self.menu_vista.addAction(self.action_dibujo)
        self.menu_vista.addSeparator()
        self.menu_vista.addAction(self.action_opcionVisualizacion)
        self.menu_ayuda.addAction(self.action_ayuda)
        self.menu_ayuda.addAction(self.action_acerdaDe)

        self.retranslateUi(MainWindow)

        self.stackedWidget_container.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MPM-UN", None))
        self.action_nuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.action_abrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.action_guardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.action_guardarComo.setText(QCoreApplication.translate("MainWindow", u"Guardar como", None))
        self.action_importar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.action_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.action_ayuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.action_acerdaDe.setText(QCoreApplication.translate("MainWindow", u"Acerda de", None))
        self.action_grid.setText(QCoreApplication.translate("MainWindow", u"Grilla", None))
        self.action_rule.setText(QCoreApplication.translate("MainWindow", u"Regla", None))
        self.action_dibujo.setText(QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.action_console.setText(QCoreApplication.translate("MainWindow", u"Consola", None))
        self.action_origin.setText(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.action_opcionVisualizacion.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n de visualizaci\u00f3n", None))
        self.action_deshacer.setText(QCoreApplication.translate("MainWindow", u"Deshacer", None))
        self.action_rehacer.setText(QCoreApplication.translate("MainWindow", u"Rehacer", None))
        self.action_copiar.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.action_pegar.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
        self.action_cortar.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
        self.action_listadoRecinetes.setText(QCoreApplication.translate("MainWindow", u"listado_recientes", None))
        self.action_axis.setText(QCoreApplication.translate("MainWindow", u"Ejes", None))
        self.action_label.setText(QCoreApplication.translate("MainWindow", u"Etiquetas", None))
        self.toolButton_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.toolButton_drawData.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.toolButton_drawMesh.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.toolButton_drawPoint.setText(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.toolButton_drawBoundary.setText(QCoreApplication.translate("MainWindow", u"Contorno", None))
        self.toolButton_viewResult.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.toolButton_setting.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vista", None))
        self.menu_archivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menu_recientes.setTitle(QCoreApplication.translate("MainWindow", u"Recientes", None))
        self.menu_editar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menu_vista.setTitle(QCoreApplication.translate("MainWindow", u"Vista", None))
        self.menu_ayuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

