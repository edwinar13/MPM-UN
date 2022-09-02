# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_inicioWelWzy.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QSizePolicy, QSpacerItem, QToolButton,
    QVBoxLayout, QWidget)

class Ui_frame_inicio_container(QFrame):
    def setupUi(self, frame_inicio_container):
        if not frame_inicio_container.objectName():
            frame_inicio_container.setObjectName(u"frame_inicio_container")
        frame_inicio_container.resize(966, 668)
        #frame_inicio_container.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(frame_inicio_container)
        self.verticalLayout_9.setSpacing(30)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(50, 20, -1, 20)
        self.label_4 = QLabel(frame_inicio_container)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(100, 100))
        self.label_4.setMaximumSize(QSize(100, 100))
        self.label_4.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setWordWrap(False)
        self.label_4.setOpenExternalLinks(False)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(30, -1, -1, -1)
        self.label_title_1 = QLabel(frame_inicio_container)
        self.label_title_1.setObjectName(u"label_title_1")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(30)
        self.label_title_1.setFont(font)

        self.horizontalLayout.addWidget(self.label_title_1)

        self.label_title_2 = QLabel(frame_inicio_container)
        self.label_title_2.setObjectName(u"label_title_2")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(30)
        font1.setBold(True)
        self.label_title_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_title_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_9 = QFrame(frame_inicio_container)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy1)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_4 = QFrame(self.frame_9)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, -1, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(150, 40))
        self.toolButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/iconos_frame_inicio/iconos/iconos_frame_inicio/new_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(20, 20))
        self.toolButton.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_4.addWidget(self.toolButton)


        self.verticalLayout.addWidget(self.frame_2)


        self.verticalLayout_13.addWidget(self.frame)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, -1, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy)
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.toolButton_5 = QToolButton(self.frame_8)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setMinimumSize(QSize(150, 40))
        self.toolButton_5.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/iconos_frame_inicio/iconos/iconos_frame_inicio/open_p.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QSize(20, 20))
        self.toolButton_5.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_5.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.toolButton_5.setArrowType(Qt.NoArrow)

        self.horizontalLayout_8.addWidget(self.toolButton_5)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.verticalLayout_13.addWidget(self.frame_7)


        self.verticalLayout_8.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_9)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, -1, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 0, 0)
        self.toolButton_4 = QToolButton(self.frame_6)
        self.toolButton_4.setObjectName(u"toolButton_4")
        self.toolButton_4.setMinimumSize(QSize(150, 40))
        self.toolButton_4.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/iconos_consola/iconos/iconos_consola/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton_4.setIcon(icon2)
        self.toolButton_4.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_4.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_7.addWidget(self.toolButton_4)


        self.verticalLayout_4.addWidget(self.frame_6)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setStyleSheet(u"")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, -1, 0)
        self.frame_14 = QFrame(self.frame_11)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 0, 0)
        self.toolButton_7 = QToolButton(self.frame_14)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setMinimumSize(QSize(150, 40))
        self.toolButton_7.setStyleSheet(u"")
        self.toolButton_7.setIcon(icon2)
        self.toolButton_7.setPopupMode(QToolButton.DelayedPopup)
        self.toolButton_7.setToolButtonStyle(Qt.ToolButtonTextOnly)

        self.horizontalLayout_10.addWidget(self.toolButton_7)


        self.verticalLayout_10.addWidget(self.frame_14)


        self.verticalLayout_11.addWidget(self.frame_11)


        self.verticalLayout_8.addWidget(self.frame_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.frame_9)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_proyectos = QFrame(frame_inicio_container)
        self.frame_proyectos.setObjectName(u"frame_proyectos")
        self.frame_proyectos.setFrameShape(QFrame.StyledPanel)
        self.frame_proyectos.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_proyectos)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_card_1 = QFrame(self.frame_proyectos)
        self.frame_card_1.setObjectName(u"frame_card_1")
        sizePolicy.setHeightForWidth(self.frame_card_1.sizePolicy().hasHeightForWidth())
        self.frame_card_1.setSizePolicy(sizePolicy)
        self.frame_card_1.setFrameShape(QFrame.StyledPanel)
        self.frame_card_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_card_1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.frame_card_1)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(False)
        self.label_7.setOpenExternalLinks(False)

        self.verticalLayout_3.addWidget(self.label_7)

        self.frame_10 = QFrame(self.frame_card_1)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy2)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_10)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_5 = QLabel(self.frame_10)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_2.addWidget(self.label_6)


        self.verticalLayout_3.addWidget(self.frame_10)


        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_card_1)

        self.frame_card_2 = QFrame(self.frame_proyectos)
        self.frame_card_2.setObjectName(u"frame_card_2")
        sizePolicy.setHeightForWidth(self.frame_card_2.sizePolicy().hasHeightForWidth())
        self.frame_card_2.setSizePolicy(sizePolicy)
        self.frame_card_2.setFrameShape(QFrame.StyledPanel)
        self.frame_card_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_card_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_8 = QLabel(self.frame_card_2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setPixmap(QPixmap(u":/iconos_logo/iconos/iconos_logo/Logo_V1.svg"))
        self.label_8.setScaledContents(True)
        self.label_8.setWordWrap(False)
        self.label_8.setOpenExternalLinks(False)

        self.verticalLayout_6.addWidget(self.label_8)

        self.frame_13 = QFrame(self.frame_card_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy2.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy2)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_9 = QLabel(self.frame_13)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_7.addWidget(self.label_9)

        self.label_10 = QLabel(self.frame_13)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_7.addWidget(self.label_10)

        self.label_11 = QLabel(self.frame_13)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_7.addWidget(self.label_11)


        self.verticalLayout_6.addWidget(self.frame_13)


        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_card_2)


        self.horizontalLayout_5.addWidget(self.frame_proyectos)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_3)


        self.retranslateUi(frame_inicio_container)

        QMetaObject.connectSlotsByName(frame_inicio_container)
    # setupUi

    def retranslateUi(self, frame_inicio_container):
        frame_inicio_container.setWindowTitle(QCoreApplication.translate("frame_inicio_container", u"Frame", None))
        self.label_4.setText("")
        self.label_title_1.setText(QCoreApplication.translate("frame_inicio_container", u"Bienvenidos a", None))
        self.label_title_2.setText(QCoreApplication.translate("frame_inicio_container", u"MPM-UN", None))
        self.toolButton.setText(QCoreApplication.translate("frame_inicio_container", u"  Abrir proyecto", None))
        self.toolButton_5.setText(QCoreApplication.translate("frame_inicio_container", u"  Nuevo proyecto", None))
        self.toolButton_4.setText(QCoreApplication.translate("frame_inicio_container", u"Ejemplos", None))
        self.toolButton_7.setText(QCoreApplication.translate("frame_inicio_container", u"Ejemplos", None))
        self.label_7.setText("")
        self.label_3.setText(QCoreApplication.translate("frame_inicio_container", u"3 SIG 83 obras", None))
        self.label_5.setText(QCoreApplication.translate("frame_inicio_container", u"25/02/2022 07:32:52 A.M.l", None))
        self.label_6.setText(QCoreApplication.translate("frame_inicio_container", u"D:/Document/Ejem", None))
        self.label_8.setText("")
        self.label_9.setText(QCoreApplication.translate("frame_inicio_container", u"3 SIG 83 obras", None))
        self.label_10.setText(QCoreApplication.translate("frame_inicio_container", u"25/02/2022 07:32:52 A.M.l", None))
        self.label_11.setText(QCoreApplication.translate("frame_inicio_container", u"D:/Document/Ejem", None))
    # retranslateUi

