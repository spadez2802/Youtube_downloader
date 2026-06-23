# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'newui.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 854)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(700, 400))
        MainWindow.setMaximumSize(QSize(1200, 1000))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.actionHistory = QAction(MainWindow)
        self.actionHistory.setObjectName(u"actionHistory")
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(700, 400))
        self.centralwidget.setMaximumSize(QSize(1200, 1000))
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.centralwidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.historyList = QScrollArea(self.centralwidget)
        self.historyList.setObjectName(u"historyList")
        self.historyList.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 114, 796))
        self.widget_12 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(-40, 0, 141, 258))
        self.verticalLayout_8 = QVBoxLayout(self.widget_12)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_7 = QWidget(self.widget_12)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.checkBox = QCheckBox(self.widget_7)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout_6.addWidget(self.checkBox)

        self.labelHistory = QLabel(self.widget_7)
        self.labelHistory.setObjectName(u"labelHistory")

        self.horizontalLayout_6.addWidget(self.labelHistory)

        self.pushButton = QPushButton(self.widget_7)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_6.addWidget(self.pushButton)

        self.btnShowLeft = QPushButton(self.widget_7)
        self.btnShowLeft.setObjectName(u"btnShowLeft")

        self.horizontalLayout_6.addWidget(self.btnShowLeft)


        self.verticalLayout_8.addWidget(self.widget_7)

        self.plainTextEdit = QPlainTextEdit(self.widget_12)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.historyList.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayout_2.addWidget(self.historyList)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(650, 400))
        self.widget_3.setMaximumSize(QSize(650, 600))
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(600, 100))
        self.widget.setMaximumSize(QSize(600, 300))
        self.widget.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelEnterLink = QLabel(self.widget)
        self.labelEnterLink.setObjectName(u"labelEnterLink")
        self.labelEnterLink.setMinimumSize(QSize(140, 20))
        self.labelEnterLink.setMaximumSize(QSize(140, 20))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(18)
        font.setBold(True)
        self.labelEnterLink.setFont(font)
        self.labelEnterLink.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelEnterLink, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.widget_9 = QWidget(self.widget)
        self.widget_9.setObjectName(u"widget_9")
        sizePolicy1.setHeightForWidth(self.widget_9.sizePolicy().hasHeightForWidth())
        self.widget_9.setSizePolicy(sizePolicy1)
        self.widget_9.setMinimumSize(QSize(600, 50))
        self.widget_9.setMaximumSize(QSize(600, 150))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, 25, -1)
        self.widget_6 = QWidget(self.widget_9)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy1.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy1)
        self.widget_6.setMinimumSize(QSize(470, 50))
        self.widget_6.setMaximumSize(QSize(470, 150))
        self.verticalLayout_6 = QVBoxLayout(self.widget_6)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 0, 5, -1)
        self.enterWidget = QWidget(self.widget_6)
        self.enterWidget.setObjectName(u"enterWidget")
        self.enterWidget.setMinimumSize(QSize(450, 50))
        self.enterWidget.setMaximumSize(QSize(450, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.enterWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.enterPlace = QLineEdit(self.enterWidget)
        self.enterPlace.setObjectName(u"enterPlace")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.enterPlace.sizePolicy().hasHeightForWidth())
        self.enterPlace.setSizePolicy(sizePolicy2)
        self.enterPlace.setMinimumSize(QSize(400, 40))
        self.enterPlace.setMaximumSize(QSize(400, 40))

        self.horizontalLayout_4.addWidget(self.enterPlace)

        self.clearBtn = QPushButton(self.enterWidget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_4.addWidget(self.clearBtn)


        self.verticalLayout_6.addWidget(self.enterWidget)

        self.listWidget = QListWidget(self.widget_6)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy1.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy1)
        self.listWidget.setMinimumSize(QSize(450, 0))
        self.listWidget.setMaximumSize(QSize(450, 60))
        self.listWidget.setAutoFillBackground(False)
        self.listWidget.setProperty(u"showDropIndicator", True)

        self.verticalLayout_6.addWidget(self.listWidget)


        self.horizontalLayout_7.addWidget(self.widget_6, 0, Qt.AlignmentFlag.AlignTop)

        self.findBtn = QPushButton(self.widget_9)
        self.findBtn.setObjectName(u"findBtn")
        self.findBtn.setMinimumSize(QSize(100, 40))
        self.findBtn.setMaximumSize(QSize(100, 40))

        self.horizontalLayout_7.addWidget(self.findBtn, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(600, 250))
        self.widget_2.setMaximumSize(QSize(600, 250))
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(590, 50))
        self.widget_4.setMaximumSize(QSize(590, 50))
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.linkName = QLabel(self.widget_4)
        self.linkName.setObjectName(u"linkName")
        self.linkName.setMinimumSize(QSize(450, 40))
        self.linkName.setMaximumSize(QSize(450, 40))

        self.horizontalLayout.addWidget(self.linkName)

        self.comboBoxDownloadOption = QComboBox(self.widget_4)
        self.comboBoxDownloadOption.addItem("")
        self.comboBoxDownloadOption.addItem("")
        self.comboBoxDownloadOption.setObjectName(u"comboBoxDownloadOption")
        sizePolicy1.setHeightForWidth(self.comboBoxDownloadOption.sizePolicy().hasHeightForWidth())
        self.comboBoxDownloadOption.setSizePolicy(sizePolicy1)
        self.comboBoxDownloadOption.setMinimumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setMaximumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.horizontalLayout.addWidget(self.comboBoxDownloadOption)


        self.verticalLayout_3.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.linkContentWidget = QWidget(self.widget_2)
        self.linkContentWidget.setObjectName(u"linkContentWidget")
        self.linkContentWidget.setMinimumSize(QSize(590, 160))
        self.linkContentWidget.setMaximumSize(QSize(590, 160))
        self.horizontalLayout_3 = QHBoxLayout(self.linkContentWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 0)
        self.videoImg = QLabel(self.linkContentWidget)
        self.videoImg.setObjectName(u"videoImg")
        self.videoImg.setMinimumSize(QSize(175, 125))
        self.videoImg.setMaximumSize(QSize(200, 125))

        self.horizontalLayout_3.addWidget(self.videoImg, 0, Qt.AlignmentFlag.AlignTop)

        self.videoName = QLabel(self.linkContentWidget)
        self.videoName.setObjectName(u"videoName")
        self.videoName.setMinimumSize(QSize(200, 100))
        self.videoName.setMaximumSize(QSize(250, 100))
        font1 = QFont()
        font1.setPointSize(16)
        self.videoName.setFont(font1)
        self.videoName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3.addWidget(self.videoName, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_8 = QWidget(self.linkContentWidget)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_5 = QVBoxLayout(self.widget_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.downloadBtn = QPushButton(self.widget_8)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMinimumSize(QSize(100, 40))
        self.downloadBtn.setMaximumSize(QSize(100, 40))

        self.verticalLayout_5.addWidget(self.downloadBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBoxDownloadQuality = QComboBox(self.widget_8)
        self.comboBoxDownloadQuality.setObjectName(u"comboBoxDownloadQuality")
        sizePolicy1.setHeightForWidth(self.comboBoxDownloadQuality.sizePolicy().hasHeightForWidth())
        self.comboBoxDownloadQuality.setSizePolicy(sizePolicy1)
        self.comboBoxDownloadQuality.setMinimumSize(QSize(150, 40))
        self.comboBoxDownloadQuality.setMaximumSize(QSize(150, 40))

        self.verticalLayout_5.addWidget(self.comboBoxDownloadQuality, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.linkContentWidget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.sideBarWidget = QWidget(self.centralwidget)
        self.sideBarWidget.setObjectName(u"sideBarWidget")
        sizePolicy.setHeightForWidth(self.sideBarWidget.sizePolicy().hasHeightForWidth())
        self.sideBarWidget.setSizePolicy(sizePolicy)
        self.sideBarWidget.setMinimumSize(QSize(0, 400))
        self.sideBarWidget.setMaximumSize(QSize(550, 800))
        self.verticalLayout_4 = QVBoxLayout(self.sideBarWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 50)
        self.widget_10 = QWidget(self.sideBarWidget)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 100))
        self.widget_10.setMaximumSize(QSize(550, 110))
        self.verticalLayout_7 = QVBoxLayout(self.widget_10)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.widget_5 = QWidget(self.widget_10)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy1.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy1)
        self.widget_5.setMinimumSize(QSize(0, 50))
        self.widget_5.setMaximumSize(QSize(550, 50))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.downloadAllBtn = QPushButton(self.widget_5)
        self.downloadAllBtn.setObjectName(u"downloadAllBtn")
        self.downloadAllBtn.setMinimumSize(QSize(100, 40))
        self.downloadAllBtn.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_5.addWidget(self.downloadAllBtn)

        self.comboBoxDownloadAllOpt = QComboBox(self.widget_5)
        self.comboBoxDownloadAllOpt.addItem("")
        self.comboBoxDownloadAllOpt.addItem("")
        self.comboBoxDownloadAllOpt.setObjectName(u"comboBoxDownloadAllOpt")
        self.comboBoxDownloadAllOpt.setMinimumSize(QSize(100, 40))
        self.comboBoxDownloadAllOpt.setMaximumSize(QSize(200, 40))

        self.horizontalLayout_5.addWidget(self.comboBoxDownloadAllOpt)

        self.miniSideBarBtn = QPushButton(self.widget_5)
        self.miniSideBarBtn.setObjectName(u"miniSideBarBtn")
        self.miniSideBarBtn.setMaximumSize(QSize(30, 30))

        self.horizontalLayout_5.addWidget(self.miniSideBarBtn)


        self.verticalLayout_7.addWidget(self.widget_5)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        sizePolicy1.setHeightForWidth(self.widget_11.sizePolicy().hasHeightForWidth())
        self.widget_11.setSizePolicy(sizePolicy1)
        self.horizontalLayout_8 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_8.setSpacing(8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btnClearAll = QPushButton(self.widget_11)
        self.btnClearAll.setObjectName(u"btnClearAll")
        self.btnClearAll.setMinimumSize(QSize(100, 20))

        self.horizontalLayout_8.addWidget(self.btnClearAll)

        self.btnChooseAll = QPushButton(self.widget_11)
        self.btnChooseAll.setObjectName(u"btnChooseAll")
        self.btnChooseAll.setMinimumSize(QSize(100, 20))

        self.horizontalLayout_8.addWidget(self.btnChooseAll)


        self.verticalLayout_7.addWidget(self.widget_11, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_10, 0, Qt.AlignmentFlag.AlignTop)

        self.scrollArea = QScrollArea(self.sideBarWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setMinimumSize(QSize(0, 0))
        self.scrollArea.setMaximumSize(QSize(500, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 54, 54))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(500, 600))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.sideBarWidget, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        self.menuAAA = QMenu(self.menubar)
        self.menuAAA.setObjectName(u"menuAAA")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuAAA.menuAction())
        self.menuAAA.addSeparator()
        self.menuAAA.addSeparator()
        self.menuAAA.addAction(self.actionHistory)
        self.menuAAA.addAction(self.actionSetting)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionHistory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.actionSetting.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.checkBox.setText("")
        self.labelHistory.setText(QCoreApplication.translate("MainWindow", u"History", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
        self.btnShowLeft.setText("")
        self.labelEnterLink.setText(QCoreApplication.translate("MainWindow", u"Enter link", None))
        self.clearBtn.setText("")
        self.findBtn.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.linkName.setText("")
        self.comboBoxDownloadOption.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.comboBoxDownloadOption.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4", None))

        self.videoImg.setText("")
        self.videoName.setText("")
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
        self.downloadAllBtn.setText(QCoreApplication.translate("MainWindow", u"Download ALL", None))
        self.comboBoxDownloadAllOpt.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.comboBoxDownloadAllOpt.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4", None))

        self.miniSideBarBtn.setText("")
        self.btnClearAll.setText(QCoreApplication.translate("MainWindow", u"Clear All", None))
        self.btnChooseAll.setText(QCoreApplication.translate("MainWindow", u"Choose All", None))
        self.menuAAA.setTitle(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

