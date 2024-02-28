# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frame_settingPjUjeG.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QSpinBox, QSplitter, QVBoxLayout,
    QWidget)

class Ui_FormSetting(object):
    def setupUi(self, FormSetting):
        if not FormSetting.objectName():
            FormSetting.setObjectName(u"FormSetting")
        FormSetting.resize(665, 559)
        self.verticalLayout = QVBoxLayout(FormSetting)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_settingSearch = QLineEdit(FormSetting)
        self.lineEdit_settingSearch.setObjectName(u"lineEdit_settingSearch")
        self.lineEdit_settingSearch.setMinimumSize(QSize(0, 30))

        self.verticalLayout.addWidget(self.lineEdit_settingSearch)

        self.frame_2 = QFrame(FormSetting)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 487, 1521))
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
        self.frame_settingCard_2 = QFrame(self.frame_containerSetting_1)
        self.frame_settingCard_2.setObjectName(u"frame_settingCard_2")
        self.frame_settingCard_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_2.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_2.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_2.setProperty("type_frame", 1)
        self.verticalLayout_4 = QVBoxLayout(self.frame_settingCard_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_settingCard_1 = QFrame(self.frame_settingCard_2)
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
        self.spinBox_1.setProperty("type_spinBox", 1)

        self.horizontalLayout_6.addWidget(self.spinBox_1)

        self.horizontalSlider_1 = QSlider(self.frame_settingCard_1)
        self.horizontalSlider_1.setObjectName(u"horizontalSlider_1")
        self.horizontalSlider_1.setMinimumSize(QSize(200, 0))
        self.horizontalSlider_1.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.frame_settingCard_1)

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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setMinimumSize(QSize(150, 25))

        self.horizontalLayout_10.addWidget(self.comboBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout_10)


        self.verticalLayout_7.addWidget(self.frame_settingCard_3)


        self.verticalLayout_8.addWidget(self.frame_containerSetting_1)

        self.frame_settingCard_a_4 = QFrame(self.scrollAreaWidgetContents)
        self.frame_settingCard_a_4.setObjectName(u"frame_settingCard_a_4")
        self.frame_settingCard_a_4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_a_4.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_a_4.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_a_4.setProperty("type_frame", 1)
        self.verticalLayout_14 = QVBoxLayout(self.frame_settingCard_a_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_settingSubtitle_a_4 = QLabel(self.frame_settingCard_a_4)
        self.label_settingSubtitle_a_4.setObjectName(u"label_settingSubtitle_a_4")
        self.label_settingSubtitle_a_4.setProperty("type_label", 3)

        self.verticalLayout_14.addWidget(self.label_settingSubtitle_a_4)

        self.label_settingDescription_a_4 = QLabel(self.frame_settingCard_a_4)
        self.label_settingDescription_a_4.setObjectName(u"label_settingDescription_a_4")
        self.label_settingDescription_a_4.setWordWrap(True)
        self.label_settingDescription_a_4.setProperty("type_label", 4)

        self.verticalLayout_14.addWidget(self.label_settingDescription_a_4)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.doubleSpinBox_grid_spacing = QDoubleSpinBox(self.frame_settingCard_a_4)
        self.doubleSpinBox_grid_spacing.setObjectName(u"doubleSpinBox_grid_spacing")
        self.doubleSpinBox_grid_spacing.setMinimumSize(QSize(60, 25))
        self.doubleSpinBox_grid_spacing.setDecimals(1)
        self.doubleSpinBox_grid_spacing.setMinimum(0.100000000000000)
        self.doubleSpinBox_grid_spacing.setMaximum(1000.000000000000000)
        self.doubleSpinBox_grid_spacing.setSingleStep(1.000000000000000)
        self.doubleSpinBox_grid_spacing.setValue(1.000000000000000)
        self.doubleSpinBox_grid_spacing.setProperty("type_spinBox", 1)

        self.horizontalLayout_25.addWidget(self.doubleSpinBox_grid_spacing)

        self.checkBox_grid_adaptative = QCheckBox(self.frame_settingCard_a_4)
        self.checkBox_grid_adaptative.setObjectName(u"checkBox_grid_adaptative")

        self.horizontalLayout_25.addWidget(self.checkBox_grid_adaptative)

        self.horizontalSpacer_a_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_a_4)


        self.verticalLayout_14.addLayout(self.horizontalLayout_25)


        self.verticalLayout_8.addWidget(self.frame_settingCard_a_4)

        self.frame_settingCard_a_5 = QFrame(self.scrollAreaWidgetContents)
        self.frame_settingCard_a_5.setObjectName(u"frame_settingCard_a_5")
        self.frame_settingCard_a_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_settingCard_a_5.setFrameShape(QFrame.StyledPanel)
        self.frame_settingCard_a_5.setFrameShadow(QFrame.Raised)
        self.frame_settingCard_a_5.setProperty("type_frame", 1)
        self.verticalLayout_15 = QVBoxLayout(self.frame_settingCard_a_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_settingSubtitle_a_5 = QLabel(self.frame_settingCard_a_5)
        self.label_settingSubtitle_a_5.setObjectName(u"label_settingSubtitle_a_5")
        self.label_settingSubtitle_a_5.setProperty("type_label", 3)

        self.verticalLayout_15.addWidget(self.label_settingSubtitle_a_5)

        self.label_settingDescription_a_5 = QLabel(self.frame_settingCard_a_5)
        self.label_settingDescription_a_5.setObjectName(u"label_settingDescription_a_5")
        self.label_settingDescription_a_5.setWordWrap(True)
        self.label_settingDescription_a_5.setProperty("type_label", 4)

        self.verticalLayout_15.addWidget(self.label_settingDescription_a_5)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.doubleSpinBox_snap_grid_spacing = QDoubleSpinBox(self.frame_settingCard_a_5)
        self.doubleSpinBox_snap_grid_spacing.setObjectName(u"doubleSpinBox_snap_grid_spacing")
        self.doubleSpinBox_snap_grid_spacing.setEnabled(True)
        self.doubleSpinBox_snap_grid_spacing.setMinimumSize(QSize(60, 25))
        self.doubleSpinBox_snap_grid_spacing.setDecimals(1)
        self.doubleSpinBox_snap_grid_spacing.setMinimum(0.100000000000000)
        self.doubleSpinBox_snap_grid_spacing.setMaximum(1000.000000000000000)
        self.doubleSpinBox_snap_grid_spacing.setSingleStep(1.000000000000000)
        self.doubleSpinBox_snap_grid_spacing.setStepType(QAbstractSpinBox.DefaultStepType)
        self.doubleSpinBox_snap_grid_spacing.setValue(1.000000000000000)
        self.doubleSpinBox_snap_grid_spacing.setProperty("type_spinBox", 1)

        self.horizontalLayout_26.addWidget(self.doubleSpinBox_snap_grid_spacing)

        self.checkBox_snap_grid_adaptative = QCheckBox(self.frame_settingCard_a_5)
        self.checkBox_snap_grid_adaptative.setObjectName(u"checkBox_snap_grid_adaptative")

        self.horizontalLayout_26.addWidget(self.checkBox_snap_grid_adaptative)

        self.horizontalSpacer_a_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_a_5)


        self.verticalLayout_15.addLayout(self.horizontalLayout_26)


        self.verticalLayout_8.addWidget(self.frame_settingCard_a_5)

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
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setWordWrap(False)
        self.label_7.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_7)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        sizePolicy1.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy1)
        self.label_15.setMinimumSize(QSize(0, 30))
        self.label_15.setWordWrap(False)
        self.label_15.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        sizePolicy1.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy1)
        self.label_16.setMinimumSize(QSize(0, 30))
        self.label_16.setWordWrap(False)
        self.label_16.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_16)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        sizePolicy1.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy1)
        self.label_17.setMinimumSize(QSize(0, 30))
        self.label_17.setWordWrap(False)
        self.label_17.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        sizePolicy1.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy1)
        self.label_18.setMinimumSize(QSize(0, 30))
        self.label_18.setWordWrap(False)
        self.label_18.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_18)

        self.label_36 = QLabel(self.frame_5)
        self.label_36.setObjectName(u"label_36")
        sizePolicy1.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy1)
        self.label_36.setMinimumSize(QSize(0, 30))
        self.label_36.setWordWrap(False)
        self.label_36.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_36)

        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(0, 30))
        self.label_8.setWordWrap(False)
        self.label_8.setProperty("type_label_table", 3)

        self.verticalLayout_10.addWidget(self.label_8)

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy1.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy1)
        self.label_9.setMinimumSize(QSize(0, 30))
        self.label_9.setWordWrap(False)
        self.label_9.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_9)

        self.label_35 = QLabel(self.frame_5)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        self.label_35.setMinimumSize(QSize(0, 30))
        self.label_35.setWordWrap(False)
        self.label_35.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_35)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        sizePolicy1.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy1)
        self.label_31.setMinimumSize(QSize(0, 30))
        self.label_31.setWordWrap(False)
        self.label_31.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_31)

        self.label_37 = QLabel(self.frame_5)
        self.label_37.setObjectName(u"label_37")
        sizePolicy1.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy1)
        self.label_37.setMinimumSize(QSize(0, 30))
        self.label_37.setWordWrap(False)
        self.label_37.setProperty("type_label_table", 2)

        self.verticalLayout_10.addWidget(self.label_37)

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

        self.frame_20 = QFrame(self.frame_6)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMinimumSize(QSize(0, 32))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.frame_20.setProperty("type_frame_table", 3)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_20)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setProperty("type_label_table", 4)

        self.horizontalLayout_30.addWidget(self.label_45)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_16)


        self.verticalLayout_11.addWidget(self.frame_20)

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

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 32))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.frame_19.setProperty("type_frame_table", 3)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_29.setSpacing(10)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_19)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setProperty("type_label_table", 4)

        self.horizontalLayout_29.addWidget(self.label_44)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_15)


        self.verticalLayout_11.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.frame_6)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 32))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setProperty("type_frame_table", 3)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_28.setSpacing(10)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_18)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setProperty("type_label_table", 4)

        self.horizontalLayout_28.addWidget(self.label_41)

        self.label_42 = QLabel(self.frame_18)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(0, 0))
        self.label_42.setProperty("type_label_table", 5)

        self.horizontalLayout_28.addWidget(self.label_42)

        self.label_43 = QLabel(self.frame_18)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setProperty("type_label_table", 4)

        self.horizontalLayout_28.addWidget(self.label_43)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_14)


        self.verticalLayout_11.addWidget(self.frame_18)

        self.frame_17 = QFrame(self.frame_6)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(0, 32))
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setProperty("type_frame_table", 3)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_27.setSpacing(10)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_17)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setProperty("type_label_table", 4)

        self.horizontalLayout_27.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_17)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(0, 0))
        self.label_39.setProperty("type_label_table", 5)

        self.horizontalLayout_27.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_17)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setProperty("type_label_table", 4)

        self.horizontalLayout_27.addWidget(self.label_40)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_13)


        self.verticalLayout_11.addWidget(self.frame_17)

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

        self.comboBox_intervalAutoSave = QComboBox(self.frame_settingCard_4)
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.addItem("")
        self.comboBox_intervalAutoSave.setObjectName(u"comboBox_intervalAutoSave")
        self.comboBox_intervalAutoSave.setEnabled(True)
        sizePolicy.setHeightForWidth(self.comboBox_intervalAutoSave.sizePolicy().hasHeightForWidth())
        self.comboBox_intervalAutoSave.setSizePolicy(sizePolicy)
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


        self.retranslateUi(FormSetting)

        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_intervalAutoSave.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(FormSetting)
    # setupUi

    def retranslateUi(self, FormSetting):
        FormSetting.setWindowTitle(QCoreApplication.translate("FormSetting", u"Form", None))
#if QT_CONFIG(tooltip)
        self.lineEdit_settingSearch.setToolTip(QCoreApplication.translate("FormSetting", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_settingSearch.setWhatsThis(QCoreApplication.translate("FormSetting", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.lineEdit_settingSearch.setPlaceholderText(QCoreApplication.translate("FormSetting", u"b\u00fasqueda", None))
#if QT_CONFIG(accessibility)
        self.label_settingTitleTree_1.setAccessibleName(QCoreApplication.translate("FormSetting", u"label_settingTitleTree_1", None))
#endif // QT_CONFIG(accessibility)
        self.label_settingTitleTree_1.setText(QCoreApplication.translate("FormSetting", u"Pantalla de dibujo", None))
        self.label_settingTitleTree_2.setText(QCoreApplication.translate("FormSetting", u"Atajos de teclado", None))
        self.label_settingTitle_1.setText(QCoreApplication.translate("FormSetting", u"Pantalla de dibujo", None))
        self.label_settingSubtitle_1.setText(QCoreApplication.translate("FormSetting", u"Cruz del puntero", None))
        self.label_settingDescription_1.setText(QCoreApplication.translate("FormSetting", u"Valor para el tama\u00f1o de la cruz del puntero cuando est\u00e1 en la vista de dibujo.", None))
        self.label_settingSubtitle_2.setText(QCoreApplication.translate("FormSetting", u"Caja del puntero", None))
        self.label_settingDescription_2.setText(QCoreApplication.translate("FormSetting", u"Establece el tama\u00f1o para la caja del puntero cuando est\u00e1 en la vista de dibujo.", None))
        self.label_settingSubtitle_3.setText(QCoreApplication.translate("FormSetting", u"Estilos de vista", None))
        self.label_settingDescription_3.setText(QCoreApplication.translate("FormSetting", u"Estilo de colores para la vista de dibujo", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("FormSetting", u"Claro", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("FormSetting", u"Gris", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("FormSetting", u"Oscuro", None))

        self.comboBox_3.setCurrentText(QCoreApplication.translate("FormSetting", u"Claro", None))
        self.label_settingSubtitle_a_4.setText(QCoreApplication.translate("FormSetting", u"Grilla", None))
        self.label_settingDescription_a_4.setText(QCoreApplication.translate("FormSetting", u"<html><head/><body><p>Se establece la distancia entre cada l\u00ednea de la grilla, la cual ser\u00e1 igual tanto en X como en Y, si se presenta una elevada cantidad de l\u00edneas de la grilla, estas se desactivan para evitar bajo rendimiento en el renderizado. Al seleccionar <span style=\" color:#c8cc8e;\">\u00ab Grilla adaptativa \u00bb</span>, la distancia tomar\u00e1 un valor din\u00e1mico que depende del zoom de la vista y var\u00eda entre 0.1-1000 </p></body></html>", None))
        self.checkBox_grid_adaptative.setText(QCoreApplication.translate("FormSetting", u"Grilla adaptativa", None))
        self.label_settingSubtitle_a_5.setText(QCoreApplication.translate("FormSetting", u"Snap", None))
        self.label_settingDescription_a_5.setText(QCoreApplication.translate("FormSetting", u"<html><head/><body><p>Se establece la distancia entre puntos de amarre, para facilitar el dibujo de elementos (punto, l\u00ednea, etc.) con precisi\u00f3n, esta distancia ser\u00e1 igual tanto en X como en Y, al seleccionar <span style=\" color:#c8cc8e;\">\u00ab Ajustar a la grilla \u00bb</span> los puntos de amarre ser\u00e1n las intersecciones entre la l\u00edneas verticales y horizontales de la grilla. </p></body></html>", None))
        self.checkBox_snap_grid_adaptative.setText(QCoreApplication.translate("FormSetting", u"Ajustar a la grilla ", None))
        self.label_settingTitle_2.setText(QCoreApplication.translate("FormSetting", u"Atajos de teclado", None))
        self.label.setText(QCoreApplication.translate("FormSetting", u"Comando", None))
        self.label_7.setText(QCoreApplication.translate("FormSetting", u"Abrir ajustes del programa", None))
        self.label_15.setText(QCoreApplication.translate("FormSetting", u"Nuevo Proyecto", None))
        self.label_16.setText(QCoreApplication.translate("FormSetting", u"Abrir proyecto", None))
        self.label_17.setText(QCoreApplication.translate("FormSetting", u"Guardar proyecto ", None))
        self.label_18.setText(QCoreApplication.translate("FormSetting", u"Guardar proyecto en otra ruta", None))
        self.label_36.setText(QCoreApplication.translate("FormSetting", u"Ocultar o mostrar origen ", None))
        self.label_8.setText(QCoreApplication.translate("FormSetting", u"Ocultar o mostrar ejes ", None))
        self.label_9.setText(QCoreApplication.translate("FormSetting", u"Ocultar o mostrar grilla", None))
        self.label_35.setText(QCoreApplication.translate("FormSetting", u"Ocultar o mostrar consola ", None))
        self.label_31.setText(QCoreApplication.translate("FormSetting", u"## Ctrl+a imprime los elemetos en la escena", None))
        self.label_37.setText(QCoreApplication.translate("FormSetting", u"## Ctrl++ cambia el estilo de la vista", None))
        self.label_3.setText(QCoreApplication.translate("FormSetting", u"Atajo de teclado", None))
        self.label_13.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_10.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_14.setText(QCoreApplication.translate("FormSetting", u"P", None))
        self.label_22.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_23.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_24.setText(QCoreApplication.translate("FormSetting", u"N", None))
        self.label_19.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_20.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_21.setText(QCoreApplication.translate("FormSetting", u"O", None))
        self.label_25.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_26.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_27.setText(QCoreApplication.translate("FormSetting", u"S", None))
        self.label_28.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_29.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_30.setText(QCoreApplication.translate("FormSetting", u"Shift", None))
        self.label_32.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_33.setText(QCoreApplication.translate("FormSetting", u"S", None))
        self.label_45.setText(QCoreApplication.translate("FormSetting", u"F6", None))
        self.label_12.setText(QCoreApplication.translate("FormSetting", u"F7", None))
        self.label_11.setText(QCoreApplication.translate("FormSetting", u"F8", None))
        self.label_44.setText(QCoreApplication.translate("FormSetting", u"F9", None))
        self.label_41.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_42.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_43.setText(QCoreApplication.translate("FormSetting", u"a", None))
        self.label_38.setText(QCoreApplication.translate("FormSetting", u"Ctrl", None))
        self.label_39.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_40.setText(QCoreApplication.translate("FormSetting", u"+", None))
        self.label_settingTitle_3.setText(QCoreApplication.translate("FormSetting", u"Archivo", None))
        self.label_settingSubtitle_4.setText(QCoreApplication.translate("FormSetting", u"Guardado autom\u00e1tico", None))
        self.label_settingDescription_4.setText(QCoreApplication.translate("FormSetting", u"<html><head/><body><p>Al seleccionar <span style=\" color:#c8cc8e;\">\u00ab Auto guardado \u00bb</span> se realizar\u00e1 un guardado autom\u00e1tico del proyecto en intervalos, seg\u00fan el tiempo seleccionado </p></body></html>", None))
        self.checkBox_autoSave.setText(QCoreApplication.translate("FormSetting", u"Auto guardado", None))
        self.comboBox_intervalAutoSave.setItemText(0, QCoreApplication.translate("FormSetting", u"5 min", None))
        self.comboBox_intervalAutoSave.setItemText(1, QCoreApplication.translate("FormSetting", u"15 min", None))
        self.comboBox_intervalAutoSave.setItemText(2, QCoreApplication.translate("FormSetting", u"30 min", None))
        self.comboBox_intervalAutoSave.setItemText(3, QCoreApplication.translate("FormSetting", u"60 min", None))

        self.comboBox_intervalAutoSave.setCurrentText(QCoreApplication.translate("FormSetting", u"5 min", None))
    # retranslateUi

