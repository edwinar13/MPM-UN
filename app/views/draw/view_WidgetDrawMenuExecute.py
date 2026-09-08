
from PySide6.QtCore import ( Signal, QSize,QTimer, QStringListModel)
from PySide6.QtGui import (QIcon, QFont, QColor,  QPixmap, QPainter, QPen , QBrush)
from PySide6.QtWidgets import ( QFrame, QSpacerItem, QSizePolicy)

from PySide6.QtCore import Signal, QStringListModel, Qt, QMimeData
from PySide6.QtGui import QIcon, QFont, QDrag
from PySide6.QtWidgets import QFrame, QSpacerItem, QSizePolicy, QListWidget, QListWidgetItem

from ui.ui_widget_draw_menu_execute import Ui_FormDrawMenuExecute
from utils import class_general


class ViewWidgetDrawMenuExecute(QFrame, Ui_FormDrawMenuExecute):
    """Panel Ejecutar: selección de puntos materiales y contornos, fps y
    los botones de etapas y ejecutar. Toda la configuración por-etapa
    (Courant, tiempo, damping, incrementos, plasticidad...) vive en
    DialogStages, no aquí."""

    signal_execute= Signal()
    signal_state_view_boundary= Signal(dict)
    signal_stages = Signal()  # abrir diálogo de etapas de análisis

    def __init__(self):
        super(ViewWidgetDrawMenuExecute, self).__init__()
        self.setupUi(self)

        self.__hide_show_frame_execute=True
        self.__hide_show_frame_execute_1=True
        self.__hide_show_frame_execute_2=True

        self.menu_active = False
        self.count_items_to = 0
        self.item = 1
        self.i = 0

        # Configura la UI
        self.__configUi()
        self.__initEventUi()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """ Configura la interface de usuario (ui) """
        # Se agrega los dos iconos para maximizar y minimizar
        self.icon_minimize = QIcon()
        self.icon_minimize.addFile(u"app/resources/iconos/iconos_menu_draw_data/minimize.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_maximize = QIcon()
        self.icon_maximize.addFile(u"app/resources/iconos/iconos_menu_draw_data/maximize.svg", QSize(), QIcon.Normal, QIcon.Off)

        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('INFORMACIÓN DEL PROYECTO')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}");
        self.verticalLayout_2.addWidget(self.label_lat)
        self.label_lat.setVisible(False)

        # Se agrega la etiqueta Qlabel vertical al menú y por defecto es no visible
        self.label_lat = class_general.QLabelVertical('ANÁLISIS')
        self.label_lat.setFont(QFont('Ubuntu', 9))
        self.label_lat.setStyleSheet("QLabel { background-color : transparent; color : #DDDDDD; font: 700 9pt Ubuntu;}");
        self.verticalLayout_2.addWidget(self.label_lat)
        self.verticalSpacer = QSpacerItem(20, 507, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)
        self.label_lat.setVisible(False)
        self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.listWidget_execute_pointMaterialFrom.setSelectionMode(QListWidget.ExtendedSelection)
        self.listWidget_execute_pointMaterialFrom.setDragEnabled(True)
        self.listWidget_execute_pointMaterialFrom.setAcceptDrops(True)
        self.listWidget_execute_pointMaterialFrom.viewport().setAcceptDrops(True)
        self.listWidget_execute_pointMaterialFrom.setDropIndicatorShown(True)
        self.listWidget_execute_pointMaterialFrom.dragEnterEvent = lambda event: self.dragEnterEventPointMaterialFrom(event)
        self.listWidget_execute_pointMaterialFrom.show()

        self.listWidget_execute_pointMaterialTo.setSelectionMode(QListWidget.ExtendedSelection)
        self.listWidget_execute_pointMaterialTo.setDragEnabled(True)
        self.listWidget_execute_pointMaterialTo.setAcceptDrops(True)
        self.listWidget_execute_pointMaterialTo.viewport().setAcceptDrops(True)
        self.listWidget_execute_pointMaterialTo.setDropIndicatorShown(True)
        self.listWidget_execute_pointMaterialTo.dragEnterEvent = lambda event: self.dragEnterEventPointMaterialTo(event)
        self.listWidget_execute_pointMaterialTo.show()

        self.listWidget_execute_boundariesFrom.setSelectionMode(QListWidget.ExtendedSelection)
        self.listWidget_execute_boundariesFrom.setDragEnabled(True)
        self.listWidget_execute_boundariesFrom.setAcceptDrops(True)
        self.listWidget_execute_boundariesFrom.viewport().setAcceptDrops(True)
        self.listWidget_execute_boundariesFrom.setDropIndicatorShown(True)
        self.listWidget_execute_boundariesFrom.dragEnterEvent = lambda event: self.dragEnterEventBoundaryFrom(event)
        self.listWidget_execute_boundariesFrom.show()

        self.listWidget_execute_boundariesTo.setSelectionMode(QListWidget.ExtendedSelection)
        self.listWidget_execute_boundariesTo.setDragEnabled(True)
        self.listWidget_execute_boundariesTo.setAcceptDrops(True)
        self.listWidget_execute_boundariesTo.viewport().setAcceptDrops(True)
        self.listWidget_execute_boundariesTo.setDropIndicatorShown(True)
        self.listWidget_execute_boundariesTo.dragEnterEvent = lambda event: self.dragEnterEventBoundaryTo(event)
        self.listWidget_execute_boundariesTo.show()

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """

        # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
        self.toolButton_hideShow.clicked.connect(self.__clickedToolButtonHideShow)
        self.toolButton_cardExecuteSubTitle1.clicked.connect(self.__clickedToolButtonCardxecuteSubTitle1)
        self.toolButton_cardExecuteSubTitle2.clicked.connect(self.__clickedToolButtonCardxecuteSubTitle2)

        # ::::::::::::::::::::      EVENTOS DRAW MENU EXECUTE     ::::::::::::::::::::
        self.listWidget_execute_pointMaterialFrom.dropEvent = self.onDropEventFrom
        self.listWidget_execute_pointMaterialTo.dropEvent = self.onDropEventTo
        self.listWidget_execute_boundariesFrom.itemChanged.connect(self.changeBoundaryFrom)
        self.listWidget_execute_boundariesTo.itemChanged.connect(self.changeBoundaryTo)

        self.toolButton_Execute.clicked.connect(self.__clickedToolButtonExecute)
        self.toolButton_ExecuteStages.clicked.connect(self.signal_stages.emit)

    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    # ::::::::::::::::::::      EVENTOS MENU     ::::::::::::::::::::
    def __clickedToolButtonHideShow(self):
        if self.__hide_show_frame_execute == True:
            self.frame_Execute.setVisible(False)
            self.__hide_show_frame_execute = False
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;border-top-right-radius: 8px;")
            self.label_lat.setVisible(True)

        elif self.__hide_show_frame_execute == False:
            self.frame_Execute.setVisible(True)
            self.__hide_show_frame_execute = True
            self.frame_hide.setStyleSheet(u"background: transparent;border-top-left-radius: 8px;")
            self.frame_hide2.setStyleSheet(u"background: #222222;border-top-left-radius: 8px;")
            self.label_lat.setVisible(False)

    def __clickedToolButtonCardxecuteSubTitle1(self):
        if self.__hide_show_frame_execute_1 == True:
            self.frame_Execute1.setVisible(False)
            self.__hide_show_frame_execute_1 = False
            self.toolButton_cardExecuteSubTitle1.setIcon(self.icon_maximize)
            self.verticalSpacer_2.changeSize(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        elif self.__hide_show_frame_execute_1 == False:
            self.frame_Execute1.setVisible(True)
            self.__hide_show_frame_execute_1 = True
            self.toolButton_cardExecuteSubTitle1.setIcon(self.icon_minimize)
            self.verticalSpacer_2.changeSize(0, 0, QSizePolicy.Fixed, QSizePolicy.Fixed)

    def __clickedToolButtonCardxecuteSubTitle2(self):
        if self.__hide_show_frame_execute_2 == True:
            self.frame_Execute2.setVisible(False)
            self.__hide_show_frame_execute_2 = False
            self.toolButton_cardExecuteSubTitle2.setIcon(self.icon_maximize)
        elif self.__hide_show_frame_execute_2 == False:
            self.frame_Execute2.setVisible(True)
            self.__hide_show_frame_execute_2 = True
            self.toolButton_cardExecuteSubTitle2.setIcon(self.icon_minimize)

    # ::::::::::::::::::::      EVENTOS DRAW MENU MESH     ::::::::::::::::::::
    def dragEnterEventPointMaterialFrom(self, event):
        if event.source() == self.listWidget_execute_pointMaterialFrom or event.source() == self.listWidget_execute_boundariesFrom or event.source() == self.listWidget_execute_boundariesTo:
            event.ignore()
        else:
            event.accept()

    def dragEnterEventPointMaterialTo(self, event):
        if event.source() == self.listWidget_execute_pointMaterialTo or event.source() == self.listWidget_execute_boundariesFrom or event.source() == self.listWidget_execute_boundariesTo:
            event.ignore()
        else:
            event.accept()

    def dragEnterEventBoundaryFrom(self, event):
        if event.source() == self.listWidget_execute_boundariesFrom or event.source() == self.listWidget_execute_pointMaterialFrom or event.source() == self.listWidget_execute_pointMaterialTo:
            event.ignore()
        else:
            event.accept()

    def dragEnterEventBoundaryTo(self, event):
        if event.source() == self.listWidget_execute_boundariesTo or event.source() == self.listWidget_execute_pointMaterialFrom or event.source() == self.listWidget_execute_pointMaterialTo:
            event.ignore()
        else:
            event.accept()

    def onDropEventFrom(self, event):
        selected_items = self.listWidget_execute_pointMaterialTo.selectedItems()

        for item in selected_items:
            # Agregar el elemento al QListWidget de destino
            self.listWidget_execute_pointMaterialFrom.addItem(item.text())

            # Transferir el ID del elemento
            id_data = item.data(Qt.UserRole)
            new_item = self.listWidget_execute_pointMaterialFrom.item(self.listWidget_execute_pointMaterialFrom.count() - 1)
            new_item.setData(Qt.UserRole, id_data)

            # Eliminar el elemento del QListWidget de origen
            self.listWidget_execute_pointMaterialTo.takeItem(self.listWidget_execute_pointMaterialTo.row(item))

        event.accept()

    def onDropEventTo(self, event):
        selected_items = self.listWidget_execute_pointMaterialFrom.selectedItems()

        for item in selected_items:
            # Agregar el elemento al QListWidget de destino
            self.listWidget_execute_pointMaterialTo.addItem(item.text())

            # Transferir el ID del elemento
            id_data = item.data(Qt.UserRole)
            new_item = self.listWidget_execute_pointMaterialTo.item(self.listWidget_execute_pointMaterialTo.count() - 1)
            new_item.setData(Qt.UserRole, id_data)

            # Eliminar el elemento del QListWidget de origen
            self.listWidget_execute_pointMaterialFrom.takeItem(self.listWidget_execute_pointMaterialFrom.row(item))

        event.accept()

    def changeBoundaryFrom(self, item):
        selected_items = self.listWidget_execute_boundariesTo.selectedItems()
        for selected_item in selected_items:
            self.listWidget_execute_boundariesTo.takeItem(self.listWidget_execute_boundariesTo.row(selected_item))
        id_boundary = item.data(Qt.UserRole)
        if id_boundary:
            self.signal_state_view_boundary.emit({'id_boundary':id_boundary,'state_view':False})

    def changeBoundaryTo(self, item):
        selected_items = self.listWidget_execute_boundariesFrom.selectedItems()
        for selected_item in selected_items:
            self.listWidget_execute_boundariesFrom.takeItem(self.listWidget_execute_boundariesFrom.row(selected_item))
        id_boundary = item.data(Qt.UserRole)
        if id_boundary:
            self.signal_state_view_boundary.emit({'id_boundary':id_boundary,'state_view':True})

    def __clickedToolButtonExecute(self):
        print('Ejecutar análisis')
        self.signal_execute.emit()

    def activateMenu(self):
        self.menu_active = True

    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getListExecutePointMaterial (self):
        items = {}
        for index in range(self.listWidget_execute_pointMaterialTo.count()):
            item = self.listWidget_execute_pointMaterialTo.item(index)
            name = item.text()
            id = item.data(Qt.UserRole)
            items[id] = {
                'name': name,
            }
        return items

    def getListExecuteBoundaries (self):
        items = []
        for index in range(self.listWidget_execute_boundariesTo.count()):
            item = self.listWidget_execute_boundariesTo.item(index)
            name = item.text()
            id = item.data(Qt.UserRole)
            items.append({'name': name, 'id': id})
        return items

    def getFps (self):
        return self.doubleSpinBoxl_textExecuteFps.value()

    def setFps (self, fps):
        self.doubleSpinBoxl_textExecuteFps.setValue(fps)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################

    def removeItemsLists(self):
        self.listWidget_execute_pointMaterialFrom.clear()
        self.listWidget_execute_pointMaterialTo.clear()
        self.listWidget_execute_boundariesFrom.clear()
        self.listWidget_execute_boundariesTo.clear()

    def removeItemsListsMaterialPoint(self):
        self.listWidget_execute_pointMaterialFrom.clear()
        self.listWidget_execute_pointMaterialTo.clear()

    def removeItemsListsBoundaries(self):
        self.listWidget_execute_boundariesFrom.clear()
        self.listWidget_execute_boundariesTo.clear()

    def addItemsListsMaterialPointFrom(self, material_point):
        """ este metodo agrega los items a la lista de puntos materiales a ejecutar

        Args:
            material_point (list): lista de puntos materiales (diccionarios con los datos de los puntos materiales
            tales como el name, id y color)
            ejemplo:
            [{'name': 'pm ejemplo 1', 'id': '5555555-b6ea-4db4-b646-0000000000', 'color': '#190421'},
            {'name': 'pm ejemplo 2', 'id': '999999999-a327-4176-859f-111111111', 'color': '#6abfc8'}]

        """
        for item_data in material_point:
            item = QListWidgetItem(item_data['name'])
            item.setData(Qt.UserRole, item_data['id'])
            color_icon = QColor(item_data['color'])
            pixmap = QPixmap(10, 10)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.white, 2))
            painter.setBrush(QBrush(color_icon))
            painter.drawEllipse(pixmap.rect())
            painter.end()
            item.setIcon(QIcon(pixmap))

            self.listWidget_execute_pointMaterialFrom.addItem(item)

    def addItemsListsMaterialPointTo(self, material_point):
        """
        args: material_point (list): lista de puntos materiales (diccionarios con los datos de los puntos materiales)
        ejemplo: [{'name': 'pm ejemplo 1', 'id': '5555555-b6ea-4db4-b646-0000000000', 'color': '#190421'},....
        """
        for item_data in material_point:
            item = QListWidgetItem(item_data['name'])
            item.setData(Qt.UserRole, item_data['id'])
            color_icon = QColor(item_data['color'])
            pixmap = QPixmap(10, 10)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(QPen(Qt.white, 2))
            painter.setBrush(QBrush(color_icon))
            painter.drawEllipse(pixmap.rect())
            painter.end()
            item.setIcon(QIcon(pixmap))
            self.listWidget_execute_pointMaterialTo.addItem(item)

    def addItemsListsBoundariesFrom(self, boundaries):
        """
        args: boundaries (list): lista de boundaries (diccionarios con los datos de los boundaries)
        ejemplo: [{'name': 'boundary ejemplo 1', 'id': '5555555-b6ea-4db4-b646-0000000000'},....
        """
        for item_data in boundaries:
            item = QListWidgetItem(item_data['name'])
            item.setData(Qt.UserRole, item_data['id'])
            self.listWidget_execute_boundariesFrom.addItem(item)
            self.signal_state_view_boundary.emit({'id_boundary':item_data['id'],'state_view':False})

    def addItemsListsBoundariesTo(self, boundaries):
        """
        args: boundaries (list): lista de boundaries (diccionarios con los datos de los boundaries)
        ejemplo: [{'name': 'boundary ejemplo 1', 'id': '5555555-b6ea-4db4-b646-0000000000'},....
        """
        for item_data in boundaries:
            item = QListWidgetItem(item_data['name'])
            item.setData(Qt.UserRole, item_data['id'])
            self.listWidget_execute_boundariesTo.addItem(item)
            self.signal_state_view_boundary.emit({'id_boundary':item_data['id'],'state_view':True})

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  MENSAJES         ::::::::::::::::::::
	##############################################################################

    def msnAlertDefault(self,error, msn=""):
        if not error:
            self.label_msn.setStyleSheet("border-radius: 3px ;padding-top: 4px; padding-bottom: 4px; background: #aaa; color:  #222;")
            self.label_msn.setText(msn)
            QTimer.singleShot(4000, self.clearLabel)

        else:
            self.label_msn.setStyleSheet("color:  #F94646")
            self.label_msn.setText(msn)
            QTimer.singleShot(4000, self.clearLabel)

    def clearLabel(self):
        self.label_msn.setText("")
        self.label_msn.setStyleSheet("border-radius: 0px ;padding-top: 0px; padding-bottom: 0px; background: transparent; color: #222;")
