# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowkRygcW.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QStatusBar,
    QTextBrowser, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(871, 696)
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
"\n"
"\n"
"\n"
"\n"
"QMainWindow#MainWindow{\n"
"background: #333333;\n"
"}\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*####################       MENU BAR SUP      ###########################*/\n"
"/*#################################################################*/\n"
""
                        "\n"
"QMenuBar#menubar {\n"
"background-color: #333333;\n"
"spacing: 5px; \n"
"color: #DDDDDD;\n"
"font: 500 10pt \"Ubuntu\";\n"
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
"\n"
"QStatusbar#statusbar{\n"
"background-color: #333333;\n"
"}\n"
"\n"
"/*######################################################"
                        "###########*/\n"
"/*####################     FRAME MENU IZQ      ##########################*/\n"
"/*#################################################################*/\n"
"\n"
"QToolButton#toolButton_inicio,\n"
"QToolButton#toolButton_resultados,\n"
"QToolButton#toolButton_puntos,\n"
"QToolButton#toolButton_contorno,\n"
"QToolButton#toolButton_data,\n"
"QToolButton#toolButton_malla,\n"
"QToolButton#toolButton_resultados,\n"
"QToolButton#toolButton_config{\n"
"background-color: transparent;\n"
"color: #DDDDDD;\n"
"font: 500 7pt \"Ubuntu\";\n"
"border: none;\n"
"padding: 8px 0px;\n"
"}\n"
"\n"
"QFrame#frame_inicio{\n"
"background: #222222;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"\n"
"QFrame#frame_resultados,\n"
"QFrame#frame_puntos,\n"
"QFrame#frame_contorno,\n"
"QFrame#frame_data,\n"
"QFrame#frame_malla{\n"
"background: #333333;\n"
"border-radius: 2px ;\n"
"border-radius: 2px;\n"
"}\n"
"\n"
"/*#################################################################*/\n"
"/*#####################"
                        "#      CONTAINER PAGE       ############################*/\n"
"/*#################################################################*/\n"
"\n"
"QFrame#frame_empty_2{\n"
"background-color: #222222;\n"
"}\n"
"\n"
"/*#################################################################*/\n"
"/*######################      PAGE HOME      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"QLabel#label_title_1{\n"
"color: #DDDDDD; \n"
"font: 500 30pt \"Ubuntu\";\n"
"}\n"
"QLabel#label_title_2{\n"
"color: #C8CC8E;\n"
"font: 700 30pt \"Ubuntu\";\n"
"font-weight:bold;\n"
"}\n"
"QFrame#frame_infEjemplos1,\n"
"QFrame#frame_infEjemplos2,\n"
"QFrame#frame_infAbrirProyecto,\n"
"QFrame#frame_infNuevoProyecto{\n"
"background-color: #C8CC8E;\n"
"border-radius: 10px\n"
"}\n"
"QFrame#frame_supEjemplos1,\n"
"QFrame#frame_supEjemplos2,\n"
"QFrame#frame_supAbrirProyecto,\n"
"QFrame#frame_supNuevoProyecto{\n"
"background-color: #DDDDDD;\n"
"border-radius: 10px\n"
"}\n"
"QToolBu"
                        "tton#toolButton_abrirProyecto,\n"
"QToolButton#toolButton_nuevoProyecto,\n"
"QToolButton#toolButton_ejemplos1,\n"
"QToolButton#toolButton_ejemplos2{\n"
"background-color: transparent;\n"
"font: 500 9pt \"Ubuntu\";\n"
"color: #222222;\n"
"}\n"
"#frame_card_1, #frame_card_2{\n"
"background: #DDDDDD;\n"
"border-radius: 5px\n"
"}\n"
"\n"
"QFrame#frame_proyectos{\n"
"background: #444444;\n"
"}\n"
"\n"
"/*\n"
"Esto no funciona pero lo necesito ajustar\n"
"QFrame#frame_proyectos > QLabel{\n"
"color: #DDDDDD;\n"
"font: 500 9pt \"Ubuntu\";\n"
"}\n"
"*/\n"
"\n"
"\n"
"/*#################################################################*/\n"
"/*######################      PAGE DRAW      ############################*/\n"
"/*#################################################################*/\n"
"\n"
"\n"
"/*###################### graphicsView draw  ############################*/\n"
"QGraphicsView#graphicsView_draw{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.943, stop:0 rgba(175, 175, 175, 255), "
                        "stop:0.971591 rgba(141, 211, 211, 220), stop:1 rgba(170, 255, 255, 255));\n"
"}\n"
"\n"
"/*###################### frame consola  ############################*/\n"
"QTextBrowser#textBrowser_2{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"}\n"
"QToolButton#toolButton_close_console{\n"
"background-color: transparent;\n"
"}\n"
"QLineEdit#lineEdit_console{\n"
"background-color: #444444;\n"
"color: #DDDDDD;\n"
"border-radius: 2px ;\n"
"padding-left: 10px;\n"
"}\n"
"QLineEdit#lineEdit_console:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit#lineEdit_console:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        icon1 = QIcon()
        icon1.addFile(u"recursos/iconos/iconos_menu_superior/new.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNuevo.setIcon(icon1)
        self.actionAbrir = QAction(MainWindow)
        self.actionAbrir.setObjectName(u"actionAbrir")
        icon2 = QIcon()
        icon2.addFile(u"recursos/iconos/iconos_menu_superior/open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbrir.setIcon(icon2)
        self.actionGuardar = QAction(MainWindow)
        self.actionGuardar.setObjectName(u"actionGuardar")
        icon3 = QIcon()
        icon3.addFile(u"recursos/iconos/iconos_menu_superior/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionGuardar.setIcon(icon3)
        self.actionGuardar_como = QAction(MainWindow)
        self.actionGuardar_como.setObjectName(u"actionGuardar_como")
        self.actionImportar = QAction(MainWindow)
        self.actionImportar.setObjectName(u"actionImportar")
        icon4 = QIcon()
        icon4.addFile(u"recursos/iconos/iconos_menu_superior/import.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionImportar.setIcon(icon4)
        self.actionExportar = QAction(MainWindow)
        self.actionExportar.setObjectName(u"actionExportar")
        icon5 = QIcon()
        icon5.addFile(u"recursos/iconos/iconos_menu_superior/export.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExportar.setIcon(icon5)
        self.actionAyuda = QAction(MainWindow)
        self.actionAyuda.setObjectName(u"actionAyuda")
        self.actionAcerda_de = QAction(MainWindow)
        self.actionAcerda_de.setObjectName(u"actionAcerda_de")
        self.actionRejilla = QAction(MainWindow)
        self.actionRejilla.setObjectName(u"actionRejilla")
        self.actionRejilla.setCheckable(True)
        self.actionRegla = QAction(MainWindow)
        self.actionRegla.setObjectName(u"actionRegla")
        self.actionRegla.setCheckable(True)
        self.actionRegla.setEnabled(True)
        self.actionDibujo = QAction(MainWindow)
        self.actionDibujo.setObjectName(u"actionDibujo")
        self.actionDibujo.setCheckable(True)
        self.actionConsola = QAction(MainWindow)
        self.actionConsola.setObjectName(u"actionConsola")
        self.actionConsola.setCheckable(True)
        self.actionOrigen = QAction(MainWindow)
        self.actionOrigen.setObjectName(u"actionOrigen")
        self.actionOrigen.setCheckable(True)
        self.actionOpci_n_de_visualizaci_n = QAction(MainWindow)
        self.actionOpci_n_de_visualizaci_n.setObjectName(u"actionOpci_n_de_visualizaci_n")
        self.actionDeshacer = QAction(MainWindow)
        self.actionDeshacer.setObjectName(u"actionDeshacer")
        icon6 = QIcon()
        icon6.addFile(u"recursos/iconos/iconos_menu_superior/undo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDeshacer.setIcon(icon6)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.actionDeshacer.setFont(font)
        self.actionRehacer = QAction(MainWindow)
        self.actionRehacer.setObjectName(u"actionRehacer")
        icon7 = QIcon()
        icon7.addFile(u"recursos/iconos/iconos_menu_superior/redo.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionRehacer.setIcon(icon7)
        self.actionCopiar = QAction(MainWindow)
        self.actionCopiar.setObjectName(u"actionCopiar")
        self.actionPegar = QAction(MainWindow)
        self.actionPegar.setObjectName(u"actionPegar")
        self.actionCortar = QAction(MainWindow)
        self.actionCortar.setObjectName(u"actionCortar")
        self.actionlistado_recinetes = QAction(MainWindow)
        self.actionlistado_recinetes.setObjectName(u"actionlistado_recinetes")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_menu_izq = QFrame(self.frame)
        self.frame_menu_izq.setObjectName(u"frame_menu_izq")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menu_izq.sizePolicy().hasHeightForWidth())
        self.frame_menu_izq.setSizePolicy(sizePolicy)
        self.frame_menu_izq.setMinimumSize(QSize(0, 0))
        self.frame_menu_izq.setMaximumSize(QSize(16777215, 16777215))
        self.frame_menu_izq.setStyleSheet(u"")
        self.frame_menu_izq.setFrameShape(QFrame.StyledPanel)
        self.frame_menu_izq.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_menu_izq)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.frame_inicioInf = QFrame(self.frame_menu_izq)
        self.frame_inicioInf.setObjectName(u"frame_inicioInf")
        self.frame_inicioInf.setFrameShape(QFrame.StyledPanel)
        self.frame_inicioInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_inicioInf)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.toolButton_inicio = QToolButton(self.frame_inicioInf)
        self.toolButton_inicio.setObjectName(u"toolButton_inicio")
        self.toolButton_inicio.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolButton_inicio.sizePolicy().hasHeightForWidth())
        self.toolButton_inicio.setSizePolicy(sizePolicy1)
        icon8 = QIcon()
        icon8.addFile(u"recursos/iconos/iconos_menu_lateral/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_inicio.setIcon(icon8)
        self.toolButton_inicio.setIconSize(QSize(30, 30))
        self.toolButton_inicio.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_22.addWidget(self.toolButton_inicio)

        self.frame_inicio = QFrame(self.frame_inicioInf)
        self.frame_inicio.setObjectName(u"frame_inicio")
        self.frame_inicio.setMinimumSize(QSize(5, 0))
        self.frame_inicio.setMaximumSize(QSize(5, 16777215))
        self.frame_inicio.setStyleSheet(u"")
        self.frame_inicio.setFrameShape(QFrame.StyledPanel)
        self.frame_inicio.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_22.addWidget(self.frame_inicio)


        self.verticalLayout_2.addWidget(self.frame_inicioInf)

        self.frame_dataInf = QFrame(self.frame_menu_izq)
        self.frame_dataInf.setObjectName(u"frame_dataInf")
        self.frame_dataInf.setFrameShape(QFrame.StyledPanel)
        self.frame_dataInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_dataInf)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.toolButton_data = QToolButton(self.frame_dataInf)
        self.toolButton_data.setObjectName(u"toolButton_data")
        sizePolicy1.setHeightForWidth(self.toolButton_data.sizePolicy().hasHeightForWidth())
        self.toolButton_data.setSizePolicy(sizePolicy1)
        self.toolButton_data.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u"recursos/iconos/iconos_menu_lateral/control.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_data.setIcon(icon9)
        self.toolButton_data.setIconSize(QSize(30, 30))
        self.toolButton_data.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_21.addWidget(self.toolButton_data)

        self.frame_data = QFrame(self.frame_dataInf)
        self.frame_data.setObjectName(u"frame_data")
        self.frame_data.setEnabled(True)
        self.frame_data.setMinimumSize(QSize(5, 0))
        self.frame_data.setMaximumSize(QSize(5, 16777215))
        self.frame_data.setStyleSheet(u"")
        self.frame_data.setFrameShape(QFrame.StyledPanel)
        self.frame_data.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_21.addWidget(self.frame_data)


        self.verticalLayout_2.addWidget(self.frame_dataInf)

        self.frame_mallaInf = QFrame(self.frame_menu_izq)
        self.frame_mallaInf.setObjectName(u"frame_mallaInf")
        self.frame_mallaInf.setFrameShape(QFrame.StyledPanel)
        self.frame_mallaInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_mallaInf)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.toolButton_malla = QToolButton(self.frame_mallaInf)
        self.toolButton_malla.setObjectName(u"toolButton_malla")
        sizePolicy1.setHeightForWidth(self.toolButton_malla.sizePolicy().hasHeightForWidth())
        self.toolButton_malla.setSizePolicy(sizePolicy1)
        icon10 = QIcon()
        icon10.addFile(u"recursos/iconos/iconos_menu_lateral/mesh.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_malla.setIcon(icon10)
        self.toolButton_malla.setIconSize(QSize(30, 30))
        self.toolButton_malla.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_20.addWidget(self.toolButton_malla)

        self.frame_malla = QFrame(self.frame_mallaInf)
        self.frame_malla.setObjectName(u"frame_malla")
        self.frame_malla.setEnabled(True)
        self.frame_malla.setMinimumSize(QSize(5, 0))
        self.frame_malla.setMaximumSize(QSize(5, 16777215))
        self.frame_malla.setStyleSheet(u"")
        self.frame_malla.setFrameShape(QFrame.StyledPanel)
        self.frame_malla.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.frame_malla)


        self.verticalLayout_2.addWidget(self.frame_mallaInf)

        self.frame_puntosInf = QFrame(self.frame_menu_izq)
        self.frame_puntosInf.setObjectName(u"frame_puntosInf")
        self.frame_puntosInf.setFrameShape(QFrame.StyledPanel)
        self.frame_puntosInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_puntosInf)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_puntos = QFrame(self.frame_puntosInf)
        self.frame_puntos.setObjectName(u"frame_puntos")
        self.frame_puntos.setEnabled(True)
        self.frame_puntos.setMinimumSize(QSize(5, 0))
        self.frame_puntos.setMaximumSize(QSize(5, 16777215))
        self.frame_puntos.setStyleSheet(u"")
        self.frame_puntos.setFrameShape(QFrame.StyledPanel)
        self.frame_puntos.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_puntos)

        self.toolButton_puntos = QToolButton(self.frame_puntosInf)
        self.toolButton_puntos.setObjectName(u"toolButton_puntos")
        sizePolicy1.setHeightForWidth(self.toolButton_puntos.sizePolicy().hasHeightForWidth())
        self.toolButton_puntos.setSizePolicy(sizePolicy1)
        icon11 = QIcon()
        icon11.addFile(u"recursos/iconos/iconos_menu_lateral/particle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_puntos.setIcon(icon11)
        self.toolButton_puntos.setIconSize(QSize(30, 30))
        self.toolButton_puntos.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_5.addWidget(self.toolButton_puntos)


        self.verticalLayout_2.addWidget(self.frame_puntosInf)

        self.frame_contornoInf = QFrame(self.frame_menu_izq)
        self.frame_contornoInf.setObjectName(u"frame_contornoInf")
        self.frame_contornoInf.setFrameShape(QFrame.StyledPanel)
        self.frame_contornoInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_contornoInf)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_contorno = QFrame(self.frame_contornoInf)
        self.frame_contorno.setObjectName(u"frame_contorno")
        self.frame_contorno.setMinimumSize(QSize(5, 0))
        self.frame_contorno.setMaximumSize(QSize(5, 16777215))
        self.frame_contorno.setStyleSheet(u"")
        self.frame_contorno.setFrameShape(QFrame.StyledPanel)
        self.frame_contorno.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_contorno)

        self.toolButton_contorno = QToolButton(self.frame_contornoInf)
        self.toolButton_contorno.setObjectName(u"toolButton_contorno")
        sizePolicy1.setHeightForWidth(self.toolButton_contorno.sizePolicy().hasHeightForWidth())
        self.toolButton_contorno.setSizePolicy(sizePolicy1)
        icon12 = QIcon()
        icon12.addFile(u"recursos/iconos/iconos_menu_lateral/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_contorno.setIcon(icon12)
        self.toolButton_contorno.setIconSize(QSize(30, 30))
        self.toolButton_contorno.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_4.addWidget(self.toolButton_contorno)


        self.verticalLayout_2.addWidget(self.frame_contornoInf)

        self.frame_resultadosInf = QFrame(self.frame_menu_izq)
        self.frame_resultadosInf.setObjectName(u"frame_resultadosInf")
        self.frame_resultadosInf.setFrameShape(QFrame.StyledPanel)
        self.frame_resultadosInf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_resultadosInf)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_resultados = QFrame(self.frame_resultadosInf)
        self.frame_resultados.setObjectName(u"frame_resultados")
        self.frame_resultados.setEnabled(True)
        self.frame_resultados.setMinimumSize(QSize(5, 0))
        self.frame_resultados.setMaximumSize(QSize(5, 16777215))
        self.frame_resultados.setStyleSheet(u"")
        self.frame_resultados.setFrameShape(QFrame.StyledPanel)
        self.frame_resultados.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_resultados)

        self.toolButton_resultados = QToolButton(self.frame_resultadosInf)
        self.toolButton_resultados.setObjectName(u"toolButton_resultados")
        sizePolicy1.setHeightForWidth(self.toolButton_resultados.sizePolicy().hasHeightForWidth())
        self.toolButton_resultados.setSizePolicy(sizePolicy1)
        icon13 = QIcon()
        icon13.addFile(u"recursos/iconos/iconos_menu_lateral/view.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_resultados.setIcon(icon13)
        self.toolButton_resultados.setIconSize(QSize(30, 30))
        self.toolButton_resultados.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.horizontalLayout_8.addWidget(self.toolButton_resultados)


        self.verticalLayout_2.addWidget(self.frame_resultadosInf)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolButton_config = QToolButton(self.frame_menu_izq)
        self.toolButton_config.setObjectName(u"toolButton_config")
        sizePolicy1.setHeightForWidth(self.toolButton_config.sizePolicy().hasHeightForWidth())
        self.toolButton_config.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setItalic(False)
        self.toolButton_config.setFont(font1)
        icon14 = QIcon()
        icon14.addFile(u"recursos/iconos/iconos_menu_lateral/config.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_config.setIcon(icon14)
        self.toolButton_config.setIconSize(QSize(30, 30))
        self.toolButton_config.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.verticalLayout_2.addWidget(self.toolButton_config)


        self.horizontalLayout_3.addWidget(self.frame_menu_izq)

        self.frame_empty_2 = QFrame(self.frame)
        self.frame_empty_2.setObjectName(u"frame_empty_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_empty_2.sizePolicy().hasHeightForWidth())
        self.frame_empty_2.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(7)
        self.frame_empty_2.setFont(font2)
        self.frame_empty_2.setStyleSheet(u"")
        self.frame_empty_2.setFrameShape(QFrame.StyledPanel)
        self.frame_empty_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_empty_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget_container = QStackedWidget(self.frame_empty_2)
        self.stackedWidget_container.setObjectName(u"stackedWidget_container")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout_17 = QHBoxLayout(self.page_home)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_2 = QFrame(self.page_home)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 20, -1, 20)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy3)
        self.label_8.setMinimumSize(QSize(100, 100))
        self.label_8.setMaximumSize(QSize(100, 100))
        self.label_8.setPixmap(QPixmap(u"recursos/iconos/iconos_logo/Logo_V1.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)

        self.horizontalLayout_7.addWidget(self.label_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(15)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(30, -1, -1, -1)
        self.label_title_1 = QLabel(self.frame_2)
        self.label_title_1.setObjectName(u"label_title_1")

        self.horizontalLayout_9.addWidget(self.label_title_1)

        self.label_title_2 = QLabel(self.frame_2)
        self.label_title_2.setObjectName(u"label_title_2")

        self.horizontalLayout_9.addWidget(self.label_title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_9)


        self.verticalLayout_12.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_5 = QFrame(self.frame_9)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_infAbrirProyecto = QFrame(self.frame_5)
        self.frame_infAbrirProyecto.setObjectName(u"frame_infAbrirProyecto")
        sizePolicy3.setHeightForWidth(self.frame_infAbrirProyecto.sizePolicy().hasHeightForWidth())
        self.frame_infAbrirProyecto.setSizePolicy(sizePolicy3)
        self.frame_infAbrirProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_infAbrirProyecto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_infAbrirProyecto)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.frame_supAbrirProyecto = QFrame(self.frame_infAbrirProyecto)
        self.frame_supAbrirProyecto.setObjectName(u"frame_supAbrirProyecto")
        sizePolicy3.setHeightForWidth(self.frame_supAbrirProyecto.sizePolicy().hasHeightForWidth())
        self.frame_supAbrirProyecto.setSizePolicy(sizePolicy3)
        self.frame_supAbrirProyecto.setStyleSheet(u"")
        self.frame_supAbrirProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_supAbrirProyecto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_supAbrirProyecto)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(5, 0, 0, 0)
        self.toolButton_abrirProyecto = QToolButton(self.frame_supAbrirProyecto)
        self.toolButton_abrirProyecto.setObjectName(u"toolButton_abrirProyecto")
        self.toolButton_abrirProyecto.setMinimumSize(QSize(150, 40))
        self.toolButton_abrirProyecto.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u"recursos/iconos/iconos_frame_inicio/new_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_abrirProyecto.setIcon(icon15)
        self.toolButton_abrirProyecto.setIconSize(QSize(20, 20))
        self.toolButton_abrirProyecto.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_abrirProyecto.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_12.addWidget(self.toolButton_abrirProyecto)


        self.verticalLayout_5.addWidget(self.frame_supAbrirProyecto)


        self.verticalLayout_13.addWidget(self.frame_infAbrirProyecto)

        self.frame_infNuevoProyecto = QFrame(self.frame_5)
        self.frame_infNuevoProyecto.setObjectName(u"frame_infNuevoProyecto")
        sizePolicy3.setHeightForWidth(self.frame_infNuevoProyecto.sizePolicy().hasHeightForWidth())
        self.frame_infNuevoProyecto.setSizePolicy(sizePolicy3)
        self.frame_infNuevoProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_infNuevoProyecto.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_infNuevoProyecto)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.frame_supNuevoProyecto = QFrame(self.frame_infNuevoProyecto)
        self.frame_supNuevoProyecto.setObjectName(u"frame_supNuevoProyecto")
        sizePolicy3.setHeightForWidth(self.frame_supNuevoProyecto.sizePolicy().hasHeightForWidth())
        self.frame_supNuevoProyecto.setSizePolicy(sizePolicy3)
        self.frame_supNuevoProyecto.setStyleSheet(u"")
        self.frame_supNuevoProyecto.setFrameShape(QFrame.StyledPanel)
        self.frame_supNuevoProyecto.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_supNuevoProyecto)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, 0, 0, 0)
        self.toolButton_nuevoProyecto = QToolButton(self.frame_supNuevoProyecto)
        self.toolButton_nuevoProyecto.setObjectName(u"toolButton_nuevoProyecto")
        self.toolButton_nuevoProyecto.setMinimumSize(QSize(150, 40))
        self.toolButton_nuevoProyecto.setStyleSheet(u"")
        icon16 = QIcon()
        icon16.addFile(u"recursos/iconos/iconos_frame_inicio/open_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_nuevoProyecto.setIcon(icon16)
        self.toolButton_nuevoProyecto.setIconSize(QSize(20, 20))
        self.toolButton_nuevoProyecto.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_nuevoProyecto.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_nuevoProyecto.setArrowType(Qt.NoArrow)

        self.horizontalLayout_13.addWidget(self.toolButton_nuevoProyecto)


        self.verticalLayout_6.addWidget(self.frame_supNuevoProyecto)


        self.verticalLayout_13.addWidget(self.frame_infNuevoProyecto)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_9)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_6)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_infEjemplos2 = QFrame(self.frame_6)
        self.frame_infEjemplos2.setObjectName(u"frame_infEjemplos2")
        sizePolicy3.setHeightForWidth(self.frame_infEjemplos2.sizePolicy().hasHeightForWidth())
        self.frame_infEjemplos2.setSizePolicy(sizePolicy3)
        self.frame_infEjemplos2.setFrameShape(QFrame.StyledPanel)
        self.frame_infEjemplos2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_infEjemplos2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, -1, 0)
        self.frame_supEjemplos2 = QFrame(self.frame_infEjemplos2)
        self.frame_supEjemplos2.setObjectName(u"frame_supEjemplos2")
        sizePolicy3.setHeightForWidth(self.frame_supEjemplos2.sizePolicy().hasHeightForWidth())
        self.frame_supEjemplos2.setSizePolicy(sizePolicy3)
        self.frame_supEjemplos2.setFrameShape(QFrame.StyledPanel)
        self.frame_supEjemplos2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_supEjemplos2)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(5, 0, 0, 0)
        self.toolButton_ejemplos2 = QToolButton(self.frame_supEjemplos2)
        self.toolButton_ejemplos2.setObjectName(u"toolButton_ejemplos2")
        self.toolButton_ejemplos2.setMinimumSize(QSize(150, 40))
        self.toolButton_ejemplos2.setStyleSheet(u"")
        self.toolButton_ejemplos2.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_ejemplos2.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_14.addWidget(self.toolButton_ejemplos2)


        self.verticalLayout_7.addWidget(self.frame_supEjemplos2)


        self.verticalLayout_11.addWidget(self.frame_infEjemplos2)

        self.frame_infEjemplos1 = QFrame(self.frame_6)
        self.frame_infEjemplos1.setObjectName(u"frame_infEjemplos1")
        sizePolicy3.setHeightForWidth(self.frame_infEjemplos1.sizePolicy().hasHeightForWidth())
        self.frame_infEjemplos1.setSizePolicy(sizePolicy3)
        self.frame_infEjemplos1.setStyleSheet(u"")
        self.frame_infEjemplos1.setFrameShape(QFrame.StyledPanel)
        self.frame_infEjemplos1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_infEjemplos1)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.frame_supEjemplos1 = QFrame(self.frame_infEjemplos1)
        self.frame_supEjemplos1.setObjectName(u"frame_supEjemplos1")
        sizePolicy3.setHeightForWidth(self.frame_supEjemplos1.sizePolicy().hasHeightForWidth())
        self.frame_supEjemplos1.setSizePolicy(sizePolicy3)
        self.frame_supEjemplos1.setStyleSheet(u"")
        self.frame_supEjemplos1.setFrameShape(QFrame.StyledPanel)
        self.frame_supEjemplos1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_supEjemplos1)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(5, 0, 0, 0)
        self.toolButton_ejemplos1 = QToolButton(self.frame_supEjemplos1)
        self.toolButton_ejemplos1.setObjectName(u"toolButton_ejemplos1")
        self.toolButton_ejemplos1.setMinimumSize(QSize(150, 40))
        self.toolButton_ejemplos1.setStyleSheet(u"")
        self.toolButton_ejemplos1.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_ejemplos1.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_15.addWidget(self.toolButton_ejemplos1)


        self.verticalLayout_10.addWidget(self.frame_supEjemplos1)


        self.verticalLayout_11.addWidget(self.frame_infEjemplos1)


        self.verticalLayout_8.addWidget(self.frame_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addWidget(self.frame_9)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_proyectos = QFrame(self.frame_2)
        self.frame_proyectos.setObjectName(u"frame_proyectos")
        self.frame_proyectos.setFrameShape(QFrame.StyledPanel)
        self.frame_proyectos.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_proyectos)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_card_1 = QFrame(self.frame_proyectos)
        self.frame_card_1.setObjectName(u"frame_card_1")
        sizePolicy3.setHeightForWidth(self.frame_card_1.sizePolicy().hasHeightForWidth())
        self.frame_card_1.setSizePolicy(sizePolicy3)
        self.frame_card_1.setFrameShape(QFrame.StyledPanel)
        self.frame_card_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_card_1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.frame_card_1)
        self.label_9.setObjectName(u"label_9")
        sizePolicy3.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy3)
        self.label_9.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_9.setScaledContents(True)
        self.label_9.setWordWrap(False)
        self.label_9.setOpenExternalLinks(False)

        self.verticalLayout_9.addWidget(self.label_9)

        self.frame_11 = QFrame(self.frame_card_1)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_11)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_10 = QLabel(self.frame_11)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_14.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)


        self.verticalLayout_9.addWidget(self.frame_11)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_card_1)

        self.frame_card_2 = QFrame(self.frame_proyectos)
        self.frame_card_2.setObjectName(u"frame_card_2")
        sizePolicy3.setHeightForWidth(self.frame_card_2.sizePolicy().hasHeightForWidth())
        self.frame_card_2.setSizePolicy(sizePolicy3)
        self.frame_card_2.setFrameShape(QFrame.StyledPanel)
        self.frame_card_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_card_2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_13 = QLabel(self.frame_card_2)
        self.label_13.setObjectName(u"label_13")
        sizePolicy3.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy3)
        self.label_13.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_13.setScaledContents(True)
        self.label_13.setWordWrap(False)
        self.label_13.setOpenExternalLinks(False)

        self.verticalLayout_15.addWidget(self.label_13)

        self.frame_13 = QFrame(self.frame_card_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_13)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_14 = QLabel(self.frame_13)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_16.addWidget(self.label_14)

        self.label_15 = QLabel(self.frame_13)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"")

        self.verticalLayout_16.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_13)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)


        self.verticalLayout_15.addWidget(self.frame_13)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_card_2)


        self.horizontalLayout_16.addWidget(self.frame_proyectos)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_16)


        self.verticalLayout_12.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_17.addWidget(self.frame_2)

        self.stackedWidget_container.addWidget(self.page_home)
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.horizontalLayout = QHBoxLayout(self.page_draw)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter = QSplitter(self.page_draw)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.graphicsView_draw = QGraphicsView(self.splitter)
        self.graphicsView_draw.setObjectName(u"graphicsView_draw")
        self.graphicsView_draw.setStyleSheet(u"")
        self.splitter.addWidget(self.graphicsView_draw)
        self.frame_3 = QFrame(self.splitter)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.textBrowser_2 = QTextBrowser(self.frame_3)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.textBrowser_2.sizePolicy().hasHeightForWidth())
        self.textBrowser_2.setSizePolicy(sizePolicy5)
        self.textBrowser_2.setMinimumSize(QSize(0, 38))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 16777215))
        self.textBrowser_2.setStyleSheet(u"")
        self.textBrowser_2.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.textBrowser_2)

        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolButton_close_console = QToolButton(self.frame_10)
        self.toolButton_close_console.setObjectName(u"toolButton_close_console")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.toolButton_close_console.sizePolicy().hasHeightForWidth())
        self.toolButton_close_console.setSizePolicy(sizePolicy6)
        self.toolButton_close_console.setMinimumSize(QSize(15, 15))
        self.toolButton_close_console.setMaximumSize(QSize(15, 15))
        self.toolButton_close_console.setFont(font2)
        self.toolButton_close_console.setStyleSheet(u"")
        icon17 = QIcon()
        icon17.addFile(u"recursos/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_close_console.setIcon(icon17)
        self.toolButton_close_console.setIconSize(QSize(15, 15))
        self.toolButton_close_console.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_2.addWidget(self.toolButton_close_console)

        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(50)
        sizePolicy7.setVerticalStretch(50)
        sizePolicy7.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy7)
        self.label_4.setMinimumSize(QSize(15, 15))
        self.label_4.setMaximumSize(QSize(15, 15))
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setPixmap(QPixmap(u"recursos/iconos/iconos_consola/code.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_console = QLineEdit(self.frame_10)
        self.lineEdit_console.setObjectName(u"lineEdit_console")
        self.lineEdit_console.setMinimumSize(QSize(0, 18))
        self.lineEdit_console.setMaximumSize(QSize(16777215, 18))
        font3 = QFont()
        font3.setPointSize(8)
        self.lineEdit_console.setFont(font3)
        self.lineEdit_console.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.lineEdit_console)


        self.verticalLayout_3.addWidget(self.frame_10)

        self.splitter.addWidget(self.frame_3)

        self.horizontalLayout.addWidget(self.splitter)

        self.stackedWidget_subMenu = QStackedWidget(self.page_draw)
        self.stackedWidget_subMenu.setObjectName(u"stackedWidget_subMenu")
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.label_3 = QLabel(self.page_data)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 400, 49, 16))
        self.stackedWidget_subMenu.addWidget(self.page_data)
        self.page_mesh = QWidget()
        self.page_mesh.setObjectName(u"page_mesh")
        self.label_5 = QLabel(self.page_mesh)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 180, 49, 16))
        self.stackedWidget_subMenu.addWidget(self.page_mesh)
        self.page_point = QWidget()
        self.page_point.setObjectName(u"page_point")
        self.label_6 = QLabel(self.page_point)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(350, 230, 49, 16))
        self.stackedWidget_subMenu.addWidget(self.page_point)
        self.page_contour = QWidget()
        self.page_contour.setObjectName(u"page_contour")
        self.label_7 = QLabel(self.page_contour)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(310, 250, 49, 16))
        self.stackedWidget_subMenu.addWidget(self.page_contour)

        self.horizontalLayout.addWidget(self.stackedWidget_subMenu)

        self.stackedWidget_container.addWidget(self.page_draw)
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.horizontalLayout_6 = QHBoxLayout(self.page_view)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.graphicsView_2 = QGraphicsView(self.page_view)
        self.graphicsView_2.setObjectName(u"graphicsView_2")

        self.horizontalLayout_6.addWidget(self.graphicsView_2)

        self.frame_4 = QFrame(self.page_view)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setPointSize(50)
        self.label_2.setFont(font4)

        self.verticalLayout_4.addWidget(self.label_2)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.stackedWidget_container.addWidget(self.page_view)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.pushButton = QPushButton(self.page_config)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(340, 260, 131, 62))
        font5 = QFont()
        font5.setPointSize(30)
        self.pushButton.setFont(font5)
        self.stackedWidget_container.addWidget(self.page_config)

        self.verticalLayout.addWidget(self.stackedWidget_container)


        self.horizontalLayout_3.addWidget(self.frame_empty_2)


        self.horizontalLayout_11.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 871, 26))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuArchivo.setGeometry(QRect(2230, 159, 166, 207))
        font6 = QFont()
        font6.setFamilies([u"Ubuntu"])
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setItalic(False)
        self.menuArchivo.setFont(font6)
        self.menuArchivo.setMouseTracking(True)
        self.menuRecientes = QMenu(self.menuArchivo)
        self.menuRecientes.setObjectName(u"menuRecientes")
        self.menuRecientes.setFont(font6)
        icon18 = QIcon()
        icon18.addFile(u"recursos/iconos/iconos_menu_superior/recent.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuRecientes.setIcon(icon18)
        self.menuEditar = QMenu(self.menubar)
        self.menuEditar.setObjectName(u"menuEditar")
        self.menuEditar.setFont(font6)
        self.menuVista = QMenu(self.menubar)
        self.menuVista.setObjectName(u"menuVista")
        self.menuVista.setFont(font6)
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        self.menuAyuda.setFont(font6)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuEditar.menuAction())
        self.menubar.addAction(self.menuVista.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.menuRecientes.menuAction())
        self.menuArchivo.addAction(self.actionGuardar)
        self.menuArchivo.addAction(self.actionGuardar_como)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionImportar)
        self.menuArchivo.addAction(self.actionExportar)
        self.menuArchivo.addSeparator()
        self.menuRecientes.addAction(self.actionlistado_recinetes)
        self.menuEditar.addAction(self.actionDeshacer)
        self.menuEditar.addAction(self.actionRehacer)
        self.menuEditar.addSeparator()
        self.menuEditar.addAction(self.actionCopiar)
        self.menuEditar.addAction(self.actionPegar)
        self.menuEditar.addAction(self.actionCortar)
        self.menuVista.addAction(self.actionRejilla)
        self.menuVista.addAction(self.actionRegla)
        self.menuVista.addAction(self.actionDibujo)
        self.menuVista.addAction(self.actionConsola)
        self.menuVista.addAction(self.actionOrigen)
        self.menuVista.addSeparator()
        self.menuVista.addAction(self.actionOpci_n_de_visualizaci_n)
        self.menuAyuda.addAction(self.actionAyuda)
        self.menuAyuda.addAction(self.actionAcerda_de)

        self.retranslateUi(MainWindow)

        self.stackedWidget_container.setCurrentIndex(1)
        self.stackedWidget_subMenu.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MPM-UN", None))
        self.actionNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.actionAbrir.setText(QCoreApplication.translate("MainWindow", u"Abrir", None))
        self.actionGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.actionGuardar_como.setText(QCoreApplication.translate("MainWindow", u"Guardar como", None))
        self.actionImportar.setText(QCoreApplication.translate("MainWindow", u"Importar", None))
        self.actionExportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.actionAyuda.setText(QCoreApplication.translate("MainWindow", u"Ayuda", None))
        self.actionAcerda_de.setText(QCoreApplication.translate("MainWindow", u"Acerda de", None))
        self.actionRejilla.setText(QCoreApplication.translate("MainWindow", u"Rejilla", None))
        self.actionRegla.setText(QCoreApplication.translate("MainWindow", u"Regla", None))
        self.actionDibujo.setText(QCoreApplication.translate("MainWindow", u"Dibujo", None))
        self.actionConsola.setText(QCoreApplication.translate("MainWindow", u"Consola", None))
        self.actionOrigen.setText(QCoreApplication.translate("MainWindow", u"Origen", None))
        self.actionOpci_n_de_visualizaci_n.setText(QCoreApplication.translate("MainWindow", u"Opci\u00f3n de visualizaci\u00f3n", None))
        self.actionDeshacer.setText(QCoreApplication.translate("MainWindow", u"Deshacer", None))
        self.actionRehacer.setText(QCoreApplication.translate("MainWindow", u"Rehacer", None))
        self.actionCopiar.setText(QCoreApplication.translate("MainWindow", u"Copiar", None))
        self.actionPegar.setText(QCoreApplication.translate("MainWindow", u"Pegar", None))
        self.actionCortar.setText(QCoreApplication.translate("MainWindow", u"Cortar", None))
        self.actionlistado_recinetes.setText(QCoreApplication.translate("MainWindow", u"listado_recientes", None))
        self.toolButton_inicio.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.toolButton_data.setText(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.toolButton_malla.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.toolButton_puntos.setText(QCoreApplication.translate("MainWindow", u"Particulas", None))
        self.toolButton_contorno.setText(QCoreApplication.translate("MainWindow", u"Contorno", None))
        self.toolButton_resultados.setText(QCoreApplication.translate("MainWindow", u"Resultados", None))
        self.toolButton_config.setText(QCoreApplication.translate("MainWindow", u"Mallado", None))
        self.label_8.setText("")
        self.label_title_1.setText(QCoreApplication.translate("MainWindow", u"Bienvenidos a", None))
        self.label_title_2.setText(QCoreApplication.translate("MainWindow", u"MPM-UN", None))
        self.toolButton_abrirProyecto.setText(QCoreApplication.translate("MainWindow", u"  Abrir proyecto", None))
        self.toolButton_nuevoProyecto.setText(QCoreApplication.translate("MainWindow", u"  Nuevo proyecto", None))
        self.toolButton_ejemplos2.setText(QCoreApplication.translate("MainWindow", u"Ejemplos", None))
        self.toolButton_ejemplos1.setText(QCoreApplication.translate("MainWindow", u"Ejemplos", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"3 SIG 83 obras", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"25/02/2022 07:32:52 A.M.l", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"D:/Document/Ejem", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"3 SIG 83 obras", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"25/02/2022 07:32:52 A.M.l", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"D:/Document/Ejem", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-weight:700;\">ERROR</span><span style=\" font-family:'Ubuntu';\">: asd asdas df</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING:"
                        " fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu'; font-style:italic;\">WARNING</span><span style=\" "
                        "font-family:'Ubuntu';\">: sdfsdfsdfsdfsd</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Ubuntu';\">RUNNING: fdgdfg dfgdf</span></p></body></html>", None))
        self.toolButton_close_console.setText("")
        self.label_4.setText("")
        self.lineEdit_console.setInputMask("")
        self.lineEdit_console.setText("")
        self.lineEdit_console.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Ingrese comando", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"malla", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"particulas", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"contorno", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Vista", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuRecientes.setTitle(QCoreApplication.translate("MainWindow", u"Recientes", None))
        self.menuEditar.setTitle(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.menuVista.setTitle(QCoreApplication.translate("MainWindow", u"Vista", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
#if QT_CONFIG(statustip)
        self.statusbar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(accessibility)
        self.statusbar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
    # retranslateUi

