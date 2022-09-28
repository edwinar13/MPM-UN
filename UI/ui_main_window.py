# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowlNqFdR.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QStatusBar, QToolButton, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1118, 809)
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
"\n"
"\n"
"\n"
"QSpinBox {\n"
"    padding-right: 15px; \n"
"    border-width: 1; \n"
"	border-style: solid; \n"
"	border-color: #555555; \n"
"	border-radius: 3px ;\n"
"	background: transparent;\n"
"	color: #DDDDDD;\n"
"	font:  10pt \"Ubuntu\";\n"
"	\n"
"\n"
"}\n"
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
"QSpinBox:hover {\n"
"	border-color: #0D99FF; \n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"/*QSlider#horizontalSlider_1::handle:horizontal {*/\n"
"\n"
"\n"
"QS"
                        "lider::groove:horizontal {\n"
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
"QSlider::handle:horizontal:hover {\n"
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
""
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
        self.lineEdit_settingSearch = QLineEdit(self.page_config)
        self.lineEdit_settingSearch.setObjectName(u"lineEdit_settingSearch")
        self.lineEdit_settingSearch.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lineEdit_settingSearch)

        self.frame_2 = QFrame(self.page_config)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_settingTitleTree_1 = QLabel(self.frame_3)
        self.label_settingTitleTree_1.setObjectName(u"label_settingTitleTree_1")
        self.label_settingTitleTree_1.setProperty("type_label", 1)

        self.verticalLayout_5.addWidget(self.label_settingTitleTree_1)

        self.label_settingTitleTree_2 = QLabel(self.frame_3)
        self.label_settingTitleTree_2.setObjectName(u"label_settingTitleTree_2")
        self.label_settingTitleTree_2.setProperty("type_label", 1)

        self.verticalLayout_5.addWidget(self.label_settingTitleTree_2)

        self.verticalSpacer_4 = QSpacerItem(20, 603, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.scrollArea = QScrollArea(self.frame_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 857, 1158))
        self.scrollAreaWidgetContents.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 50, -1)
        self.label_settingTitle_1 = QLabel(self.scrollAreaWidgetContents)
        self.label_settingTitle_1.setObjectName(u"label_settingTitle_1")
        self.label_settingTitle_1.setProperty("type_label", 2)

        self.verticalLayout_8.addWidget(self.label_settingTitle_1)

        self.frame_containerSetting_1 = QFrame(self.scrollAreaWidgetContents)
        self.frame_containerSetting_1.setObjectName(u"frame_containerSetting_1")
        self.frame_containerSetting_1.setFrameShape(QFrame.StyledPanel)
        self.frame_containerSetting_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_containerSetting_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_settingCard_1 = QFrame(self.frame_containerSetting_1)
        self.frame_settingCard_1.setObjectName(u"frame_settingCard_1")
        self.frame_settingCard_1.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_1.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_1.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_1.setProperty("type_frame", 1)
        self.verticalLayout_3 = QVBoxLayout(self.frame_settingCard_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_settingSubtitle_1 = QLabel(self.frame_settingCard_1)
        self.label_settingSubtitle_1.setObjectName(u"label_settingSubtitle_1")
        self.label_settingSubtitle_1.setProperty("type_label", 3)

        self.verticalLayout_3.addWidget(self.label_settingSubtitle_1)

        self.label_settingDescription_1 = QLabel(self.frame_settingCard_1)
        self.label_settingDescription_1.setObjectName(u"label_settingDescription_1")
        self.label_settingDescription_1.setWordWrap(True)
        self.label_settingDescription_1.setProperty("type_label", 4)

        self.verticalLayout_3.addWidget(self.label_settingDescription_1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.spinBox_1 = QSpinBox(self.frame_settingCard_1)
        self.spinBox_1.setObjectName(u"spinBox_1")
        self.spinBox_1.setMinimumSize(QSize(60, 25))
        self.spinBox_1.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.spinBox_1)

        self.horizontalSlider_1 = QSlider(self.frame_settingCard_1)
        self.horizontalSlider_1.setObjectName(u"horizontalSlider_1")
        self.horizontalSlider_1.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_1.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_7.addWidget(self.frame_settingCard_1)

        self.frame_settingCard_2 = QFrame(self.frame_containerSetting_1)
        self.frame_settingCard_2.setObjectName(u"frame_settingCard_2")
        self.frame_settingCard_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_2.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_2.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_2.setProperty("type_frame", 1)
        self.verticalLayout_4 = QVBoxLayout(self.frame_settingCard_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_settingSubtitle_2 = QLabel(self.frame_settingCard_2)
        self.label_settingSubtitle_2.setObjectName(u"label_settingSubtitle_2")
        self.label_settingSubtitle_2.setProperty("type_label", 3)

        self.verticalLayout_4.addWidget(self.label_settingSubtitle_2)

        self.label_settingDescription_2 = QLabel(self.frame_settingCard_2)
        self.label_settingDescription_2.setObjectName(u"label_settingDescription_2")
        self.label_settingDescription_2.setWordWrap(True)
        self.label_settingDescription_2.setProperty("type_label", 4)

        self.verticalLayout_4.addWidget(self.label_settingDescription_2)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_4 = QFrame(self.frame_settingCard_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(50, 50))
        self.frame_4.setMaximumSize(QSize(50, 50))
        self.frame_4.setStyleSheet(u"background-color: #444444;")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(4)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(5, 5))
        self.frame_7.setStyleSheet(u"background-color: transparent;\n"
"border: 1px solid #DDDDDD;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_7)


        self.horizontalLayout_9.addWidget(self.frame_4)

        self.horizontalSlider_2 = QSlider(self.frame_settingCard_2)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_9.addWidget(self.horizontalSlider_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_7.addWidget(self.frame_settingCard_2)

        self.frame_settingCard_3 = QFrame(self.frame_containerSetting_1)
        self.frame_settingCard_3.setObjectName(u"frame_settingCard_3")
        self.frame_settingCard_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_3.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_3.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_3.setProperty("type_frame", 1)
        self.verticalLayout_9 = QVBoxLayout(self.frame_settingCard_3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_settingSubtitle_3 = QLabel(self.frame_settingCard_3)
        self.label_settingSubtitle_3.setObjectName(u"label_settingSubtitle_3")
        self.label_settingSubtitle_3.setProperty("type_label", 3)

        self.verticalLayout_9.addWidget(self.label_settingSubtitle_3)

        self.label_settingDescription_3 = QLabel(self.frame_settingCard_3)
        self.label_settingDescription_3.setObjectName(u"label_settingDescription_3")
        self.label_settingDescription_3.setWordWrap(True)
        self.label_settingDescription_3.setProperty("type_label", 4)

        self.verticalLayout_9.addWidget(self.label_settingDescription_3)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.comboBox_3 = QComboBox(self.frame_settingCard_3)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy3)
        self.comboBox_3.setMinimumSize(QSize(150, 25))

        self.horizontalLayout_10.addWidget(self.comboBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.frame_settingCard_3)


        self.verticalLayout_8.addWidget(self.frame_containerSetting_1)

        self.label_settingTitle_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_settingTitle_2.setObjectName(u"label_settingTitle_2")
        self.label_settingTitle_2.setProperty("type_label", 2)

        self.verticalLayout_8.addWidget(self.label_settingTitle_2)

        self.frame_containerSetting_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_containerSetting_2.setObjectName(u"frame_containerSetting_2")
        self.frame_containerSetting_2.setMinimumSize(QSize(0, 0))
        self.frame_containerSetting_2.setStyleSheet(u"")
        self.frame_containerSetting_2.setFrameShape(QFrame.StyledPanel)
        self.frame_containerSetting_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_containerSetting_2)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.frame_containerSetting_2)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setFrameShadow(QFrame.Raised)
        self.splitter.setLineWidth(1)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.frame_5 = QFrame(self.splitter)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 40))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setProperty("type_label_table", 1)
        self.label.setProperty("type_label_title_table", 1)

        self.verticalLayout_10.addWidget(self.label)

        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setWordWrap(False)
        self.label_7.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy4.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy4)
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setWordWrap(False)
        self.label_8.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setWordWrap(False)
        self.label_9.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setWordWrap(False)
        self.label_15.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy4.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy4)
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setWordWrap(False)
        self.label_16.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy4.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy4)
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setWordWrap(False)
        self.label_17.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)
        self.label_18.setMinimumSize(QSize(0, 30))
        self.label_18.setWordWrap(False)
        self.label_18.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_18)

        self.splitter.addWidget(self.frame_5)
        self.frame_6 = QFrame(self.splitter)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.frame_6.setLineWidth(2)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 40))
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setProperty("type_label_table", 1)
        self.label_3.setProperty("type_label_title_table", 2)

        self.verticalLayout_11.addWidget(self.label_3)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 32))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setProperty("type_frame_table", 2)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setProperty("type_label_table", 4)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 0))
        self.label_10.setProperty("type_label_table", 5)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.label_14 = QLabel(self.frame_12)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setProperty("type_label_table", 4)

        self.horizontalLayout_13.addWidget(self.label_14)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_6)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 32))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setProperty("type_frame_table", 3)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setSpacing(10)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setProperty("type_label_table", 4)

        self.horizontalLayout_15.addWidget(self.label_12)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_6)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 32))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.frame_10.setProperty("type_frame_table", 2)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setProperty("type_label_table", 4)

        self.horizontalLayout_14.addWidget(self.label_11)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setMinimumSize(QSize(0, 32))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setProperty("type_frame_table", 3)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.frame_14)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setProperty("type_label_table", 4)

        self.horizontalLayout_18.addWidget(self.label_22)

        self.label_23 = QLabel(self.frame_14)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(0, 0))
        self.label_23.setProperty("type_label_table", 5)

        self.horizontalLayout_18.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_14)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setProperty("type_label_table", 4)

        self.horizontalLayout_18.addWidget(self.label_24)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 32))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.frame_13.setProperty("type_frame_table", 2)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_16.setSpacing(10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_13)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setProperty("type_label_table", 4)

        self.horizontalLayout_16.addWidget(self.label_19)

        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMinimumSize(QSize(0, 0))
        self.label_20.setProperty("type_label_table", 5)

        self.horizontalLayout_16.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setProperty("type_label_table", 4)

        self.horizontalLayout_16.addWidget(self.label_21)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_9)


        self.verticalLayout_11.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_6)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 32))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setProperty("type_frame_table", 3)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_23.setSpacing(10)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.frame_15)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setProperty("type_label_table", 4)

        self.horizontalLayout_23.addWidget(self.label_25)

        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(0, 0))
        self.label_26.setProperty("type_label_table", 5)

        self.horizontalLayout_23.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_15)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setProperty("type_label_table", 4)

        self.horizontalLayout_23.addWidget(self.label_27)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_11)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_6)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 32))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setProperty("type_frame_table", 2)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_24.setSpacing(10)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.frame_16)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setProperty("type_label_table", 4)

        self.horizontalLayout_24.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_16)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(0, 0))
        self.label_29.setProperty("type_label_table", 5)

        self.horizontalLayout_24.addWidget(self.label_29)

        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setProperty("type_label_table", 4)

        self.horizontalLayout_24.addWidget(self.label_30)

        self.label_32 = QLabel(self.frame_16)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(0, 0))
        self.label_32.setProperty("type_label_table", 5)

        self.horizontalLayout_24.addWidget(self.label_32)

        self.label_33 = QLabel(self.frame_16)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setProperty("type_label_table", 4)

        self.horizontalLayout_24.addWidget(self.label_33)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_12)


        self.verticalLayout_11.addWidget(self.frame_16)

        self.splitter.addWidget(self.frame_6)

        self.horizontalLayout_11.addWidget(self.splitter)


        self.verticalLayout_8.addWidget(self.frame_containerSetting_2)

        self.label_settingTitle_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_settingTitle_3.setObjectName(u"label_settingTitle_3")
        self.label_settingTitle_3.setProperty("type_label", 2)

        self.verticalLayout_8.addWidget(self.label_settingTitle_3)

        self.frame_containerSetting_3 = QFrame(self.scrollAreaWidgetContents)
        self.frame_containerSetting_3.setObjectName(u"frame_containerSetting_3")
        self.frame_containerSetting_3.setFrameShape(QFrame.StyledPanel)
        self.frame_containerSetting_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_containerSetting_3)
        self.verticalLayout_13.setSpacing(6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_settingCard_4 = QFrame(self.frame_containerSetting_3)
        self.frame_settingCard_4.setObjectName(u"frame_settingCard_4")
        self.frame_settingCard_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_4.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_4.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_4.setProperty("type_frame", 1)
        self.verticalLayout_12 = QVBoxLayout(self.frame_settingCard_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_settingSubtitle_4 = QLabel(self.frame_settingCard_4)
        self.label_settingSubtitle_4.setObjectName(u"label_settingSubtitle_4")
        self.label_settingSubtitle_4.setProperty("type_label", 3)

        self.verticalLayout_12.addWidget(self.label_settingSubtitle_4)

        self.label_settingDescription_4 = QLabel(self.frame_settingCard_4)
        self.label_settingDescription_4.setObjectName(u"label_settingDescription_4")
        self.label_settingDescription_4.setWordWrap(True)
        self.label_settingDescription_4.setProperty("type_label", 4)

        self.verticalLayout_12.addWidget(self.label_settingDescription_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.checkBox_autoSave = QCheckBox(self.frame_settingCard_4)
        self.checkBox_autoSave.setObjectName(u"checkBox_autoSave")

        self.horizontalLayout_12.addWidget(self.checkBox_autoSave)

        self.label_settingDescription_5 = QLabel(self.frame_settingCard_4)
        self.label_settingDescription_5.setObjectName(u"label_settingDescription_5")
        self.label_settingDescription_5.setWordWrap(True)
        self.label_settingDescription_5.setProperty("type_label", 4)

        self.horizontalLayout_12.addWidget(self.label_settingDescription_5)

        self.comboBox_intervalAutoSave = QComboBox(self.frame_settingCard_4)
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.setObjectName(u"comboBox_intervalAutoSave")
        self.comboBox_intervalAutoSave.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.comboBox_intervalAutoSave.sizePolicy().hasHeightForWidth())
        self.comboBox_intervalAutoSave.setSizePolicy(sizePolicy3)
        self.comboBox_intervalAutoSave.setMinimumSize(QSize(100, 25))

        self.horizontalLayout_12.addWidget(self.comboBox_intervalAutoSave)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)


        self.verticalLayout_12.addLayout(self.horizontalLayout_12)


        self.verticalLayout_13.addWidget(self.frame_settingCard_4)


        self.verticalLayout_8.addWidget(self.frame_containerSetting_3)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 200))
        self.frame_8.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_8)

        self.verticalSpacer_3 = QSpacerItem(20, 58, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.menu_vista.addAction(self.action_rule)
        self.menu_vista.addAction(self.action_dibujo)
        self.menu_vista.addSeparator()
        self.menu_vista.addAction(self.action_opcionVisualizacion)
        self.menu_ayuda.addAction(self.action_ayuda)
        self.menu_ayuda.addAction(self.action_acerdaDe)

        self.retranslateUi(MainWindow)

        self.stackedWidget_container.setCurrentIndex(3)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_intervalAutoSave.setCurrentIndex(0)


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
        self.toolButton_home.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.toolButton_drawData.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.toolButton_drawMesh.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.toolButton_drawPoint.setText(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.toolButton_drawBoundary.setText(QCoreApplication.translate("MainWindow", u"Contorno", None))
        self.toolButton_viewResult.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.toolButton_setting.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vista", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_settingSearch.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_settingSearch.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_settingSearch.setPlaceholderText(QCoreApplication.translate("MainWindow", u"b\u00fasqueda", None))
#if QT_CONFIG(accessibility)
        self.label_settingTitleTree_1.setAccessibleName(QCoreApplication.translate("MainWindow", u"label_settingTitleTree_1", None))
#endif // QT_CONFIG(accessibility)
        self.label_settingTitleTree_1.setText(QCoreApplication.translate("MainWindow", u"Pantalla de dibujo", None))
        self.label_settingTitleTree_2.setText(QCoreApplication.translate("MainWindow", u"Atajos de teclado", None))
        self.label_settingTitle_1.setText(QCoreApplication.translate("MainWindow", u"Pantalla de dibujo", None))
        self.label_settingSubtitle_1.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o de  la cruz del puntero", None))
        self.label_settingDescription_1.setText(QCoreApplication.translate("MainWindow", u"Valor para el tama\u00f1o de la cruz del puntero cuando est\u00e1 en la vista de dibujo.", None))
        self.label_settingSubtitle_2.setText(QCoreApplication.translate("MainWindow", u"Tama\u00f1o de la caja del puntero", None))
        self.label_settingDescription_2.setText(QCoreApplication.translate("MainWindow", u"Establece el tama\u00f1o para la caja del puntero cuando est\u00e1 en la vista de dibujo.", None))
        self.label_settingSubtitle_3.setText(QCoreApplication.translate("MainWindow", u"Estilos de vista", None))
        self.label_settingDescription_3.setText(QCoreApplication.translate("MainWindow", u"Estilo de colores para la vista de dibujo", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Claro", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Gris", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Oscuro", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("MainWindow", u"Claro", None))
        self.label_settingTitle_2.setText(QCoreApplication.translate("MainWindow", u"Atajos de teclado", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Comando", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Abrir ajustes del programa", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Ocultar o mostrar ejes ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ocultar o mostrar grilla", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nuevo Proyecto", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Abrir proyecto", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Guardar proyecto ", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Guardar proyecto en otra ruta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Atajo de teclado", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"F7", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"F7", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Ctrl", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Shift", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.label_settingTitle_3.setText(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.label_settingSubtitle_4.setText(QCoreApplication.translate("MainWindow", u"Guardado autom\u00e1tico", None))
        self.label_settingDescription_4.setText(QCoreApplication.translate("MainWindow", u"Al seleccionarse esta opci\u00f3n se guardar\u00e1 el proyecto en cierto intervalos de tiempo", None))
        self.checkBox_autoSave.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.label_settingDescription_5.setText(QCoreApplication.translate("MainWindow", u"         Intervalo de:", None))
        self.comboBox_intervalAutoSave.setItemText(0, QCoreApplication.translate("MainWindow", u"5 min", None))
        self.comboBox_intervalAutoSave.setItemText(1, QCoreApplication.translate("MainWindow", u"15 min", None))
        self.comboBox_intervalAutoSave.setItemText(2, QCoreApplication.translate("MainWindow", u"30 min", None))
        self.comboBox_intervalAutoSave.setItemText(3, QCoreApplication.translate("MainWindow", u"60 min", None))

        self.comboBox_intervalAutoSave.setCurrentText(QCoreApplication.translate("MainWindow", u"5 min", None))
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

