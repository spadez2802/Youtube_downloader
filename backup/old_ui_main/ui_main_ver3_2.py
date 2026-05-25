# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 800)
        MainWindow.setMinimumSize(QSize(1000, 800))
        MainWindow.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        MainWindow.setStyleSheet(u"\n"
"QMainWindow {\n"
"    background-color: rgb(0, 85, 127); /* \u0110\u00e2y l\u00e0 m\u00e0u x\u00e1m \u0111en hi\u1ec7n \u0111\u1ea1i */\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(1000, 800))
        self.centralwidget.setMaximumSize(QSize(1000, 800))
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.centralwidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.centralwidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"    background-color: rgb(50, 50, 50)/* \u0110\u00e2y l\u00e0 m\u00e0u x\u00e1m \u0111en hi\u1ec7n \u0111\u1ea1i */\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(650, 400))
        self.widget_3.setMaximumSize(QSize(650, 400))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"		\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.widget_3)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(600, 100))
        self.widget.setMaximumSize(QSize(600, 100))
        self.widget.setSizeIncrement(QSize(0, 0))
        self.widget.setStyleSheet(u"#widget{\n"
"\n"
"	border-radius: 25px;\n"
"	background: #2b2b2b;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(140, 20))
        self.label.setMaximumSize(QSize(140, 20))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy)
        self.widget_6.setMinimumSize(QSize(590, 70))
        self.widget_6.setMaximumSize(QSize(590, 70))
        self.horizontalLayout_4 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.enterPlace = QLineEdit(self.widget_6)
        self.enterPlace.setObjectName(u"enterPlace")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.enterPlace.sizePolicy().hasHeightForWidth())
        self.enterPlace.setSizePolicy(sizePolicy1)
        self.enterPlace.setMinimumSize(QSize(450, 40))
        self.enterPlace.setMaximumSize(QSize(450, 40))
        self.enterPlace.setStyleSheet(u"#enterPlace {\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: black;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#enterPlace:hover{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(52, 52, 52);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#enterPlace:focus{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi"
                        " ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(29, 29, 29);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.enterPlace)

        self.findBtn = QPushButton(self.widget_6)
        self.findBtn.setObjectName(u"findBtn")
        self.findBtn.setMinimumSize(QSize(100, 40))
        self.findBtn.setMaximumSize(QSize(100, 40))
        self.findBtn.setStyleSheet(u"#findBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 85, 0);\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"\n"
"}\n"
"\n"
"#findBtn:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(67, 67, 67);\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 85, 0);\n"
"	color : white;\n"
"	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_4.addWidget(self.findBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(600, 250))
        self.widget_2.setMaximumSize(QSize(600, 250))
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"	border: 2px solid transparent;\n"
"	border-radius:25px;\n"
"	background-color:#2b2b2b;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(590, 50))
        self.widget_4.setMaximumSize(QSize(590, 50))
        self.widget_4.setStyleSheet(u"#widget_4{\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.linkName = QLabel(self.widget_4)
        self.linkName.setObjectName(u"linkName")
        self.linkName.setMinimumSize(QSize(450, 40))
        self.linkName.setMaximumSize(QSize(450, 40))
        self.linkName.setStyleSheet(u"#linkName {\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: black;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}")

        self.horizontalLayout.addWidget(self.linkName)

        self.comboBoxDownloadOption = QComboBox(self.widget_4)
        self.comboBoxDownloadOption.addItem("")
        self.comboBoxDownloadOption.addItem("")
        self.comboBoxDownloadOption.setObjectName(u"comboBoxDownloadOption")
        sizePolicy.setHeightForWidth(self.comboBoxDownloadOption.sizePolicy().hasHeightForWidth())
        self.comboBoxDownloadOption.setSizePolicy(sizePolicy)
        self.comboBoxDownloadOption.setMinimumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setMaximumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBoxDownloadOption.setStyleSheet(u"#comboBoxDownloadOption{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 85, 0);\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	padding-left: 30px;\n"
"}\n"
"\n"
"#comboBoxDownloadOption:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(67, 67, 67);\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 85, 0);\n"
"	color : white;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDownloadOption::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#comboBoxDownloadOption::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}")

        self.horizontalLayout.addWidget(self.comboBoxDownloadOption)


        self.verticalLayout_3.addWidget(self.widget_4, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.widget_5 = QWidget(self.widget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(590, 160))
        self.widget_5.setMaximumSize(QSize(590, 160))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 0)
        self.videoImg = QLabel(self.widget_5)
        self.videoImg.setObjectName(u"videoImg")
        self.videoImg.setMinimumSize(QSize(175, 125))
        self.videoImg.setMaximumSize(QSize(200, 125))

        self.horizontalLayout_3.addWidget(self.videoImg, 0, Qt.AlignmentFlag.AlignTop)

        self.videoName = QLabel(self.widget_5)
        self.videoName.setObjectName(u"videoName")
        self.videoName.setMinimumSize(QSize(200, 100))
        self.videoName.setMaximumSize(QSize(250, 100))
        self.videoName.setFont(font)
        self.videoName.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_3.addWidget(self.videoName, 0, Qt.AlignmentFlag.AlignTop)

        self.downloadBtn = QPushButton(self.widget_5)
        self.downloadBtn.setObjectName(u"downloadBtn")
        self.downloadBtn.setMinimumSize(QSize(100, 40))
        self.downloadBtn.setMaximumSize(QSize(100, 40))
        self.downloadBtn.setStyleSheet(u"#downloadBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 85, 0);\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"\n"
"}\n"
"\n"
"#downloadBtn:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(67, 67, 67);\n"
"	border-radius:20px;\n"
"	background-color: rgb(255, 85, 0);\n"
"	color : white;\n"
"	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.downloadBtn, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.widget_5, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_2, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Enter link", None))
        self.findBtn.setText(QCoreApplication.translate("MainWindow", u"Find", None))
        self.linkName.setText("")
        self.comboBoxDownloadOption.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.comboBoxDownloadOption.setItemText(1, QCoreApplication.translate("MainWindow", u"MP4", None))

        self.videoImg.setText("")
        self.videoName.setText("")
        self.downloadBtn.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
    # retranslateUi

