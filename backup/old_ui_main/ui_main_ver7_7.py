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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenuBar, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

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
        MainWindow.setStyleSheet(u"\n"
"QMainWindow {\n"
"    background-color: #1ED761; /* \u0110\u00e2y l\u00e0 m\u00e0u x\u00e1m \u0111en hi\u1ec7n \u0111\u1ea1i */\n"
"}")
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
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"    background-color: black/* \u0110\u00e2y l\u00e0 m\u00e0u x\u00e1m \u0111en hi\u1ec7n \u0111\u1ea1i */\n"
"\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(650, 400))
        self.widget_3.setMaximumSize(QSize(650, 600))
        self.widget_3.setStyleSheet(u"#widget_3{\n"
"		\n"
"	background-color: transparent;\n"
"}")
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
        self.widget.setStyleSheet(u"#widget{\n"
"\n"
"	border-radius: 25px;\n"
"	background: #2b2b2b;\n"
"}")
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
        self.labelEnterLink.setStyleSheet(u"#labelEnterLink{\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 18pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"	color:white;\n"
"}")
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
        self.enterWidget.setStyleSheet(u"#enterWidget {\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 25px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: black;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#enterWidget:hover{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 25px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(52, 52, 52);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#enterWidget:focus{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edb"
                        "i ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(29, 29, 29);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"")
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
        self.enterPlace.setStyleSheet(u"#enterPlace {\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#enterPlace:focus{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: transparent;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.enterPlace)

        self.clearBtn = QPushButton(self.enterWidget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMaximumSize(QSize(40, 40))
        self.clearBtn.setStyleSheet(u"#clearBtn{\n"
"	background-color: transparent;\n"
"	border: 1px solid transparent;\n"
"}")

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
        self.findBtn.setStyleSheet(u"#findBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"}\n"
"\n"
"#findBtn:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: #1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.findBtn, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignBottom)

        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMinimumSize(QSize(600, 250))
        self.widget_2.setMaximumSize(QSize(600, 250))
        self.widget_2.setStyleSheet(u"#widget_2{\n"
"	border: 2px solid transparent;\n"
"	border-radius:25px;\n"
"	background-color:#2b2b2b;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 10)
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
        sizePolicy1.setHeightForWidth(self.comboBoxDownloadOption.sizePolicy().hasHeightForWidth())
        self.comboBoxDownloadOption.setSizePolicy(sizePolicy1)
        self.comboBoxDownloadOption.setMinimumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setMaximumSize(QSize(100, 40))
        self.comboBoxDownloadOption.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.comboBoxDownloadOption.setStyleSheet(u"#comboBoxDownloadOption{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	padding-left: 30px;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"}\n"
"\n"
"#comboBoxDownloadOption:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDownloadOption::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top"
                        " right;\n"
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

        self.linkContentWidget = QWidget(self.widget_2)
        self.linkContentWidget.setObjectName(u"linkContentWidget")
        self.linkContentWidget.setMinimumSize(QSize(590, 160))
        self.linkContentWidget.setMaximumSize(QSize(590, 160))
        self.linkContentWidget.setStyleSheet(u"#linkContentWidget{\n"
"	border: 2px solid transparent; \n"
"    border-radius: 25px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.linkContentWidget)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 0)
        self.videoImg = QLabel(self.linkContentWidget)
        self.videoImg.setObjectName(u"videoImg")
        self.videoImg.setMinimumSize(QSize(175, 125))
        self.videoImg.setMaximumSize(QSize(200, 125))
        self.videoImg.setStyleSheet(u"#videoImg{\n"
"	border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"}")

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
        self.downloadBtn.setStyleSheet(u"#downloadBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#downloadBtn:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: #1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.downloadBtn, 0, Qt.AlignmentFlag.AlignRight)

        self.comboBoxDownloadQuality = QComboBox(self.widget_8)
        self.comboBoxDownloadQuality.setObjectName(u"comboBoxDownloadQuality")
        sizePolicy1.setHeightForWidth(self.comboBoxDownloadQuality.sizePolicy().hasHeightForWidth())
        self.comboBoxDownloadQuality.setSizePolicy(sizePolicy1)
        self.comboBoxDownloadQuality.setMinimumSize(QSize(150, 40))
        self.comboBoxDownloadQuality.setMaximumSize(QSize(150, 40))
        self.comboBoxDownloadQuality.setStyleSheet(u"#comboBoxDownloadQuality{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	padding-left: 30px;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"}\n"
"\n"
"#comboBoxDownloadQuality:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDownloadQuality::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: "
                        "top right;\n"
"    width: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#comboBoxDownloadQuality::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"#comboBoxDowloadQuality:disable{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(136, 136, 136);\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : transparent;\n"
"	\n"
"}")

        self.verticalLayout_5.addWidget(self.comboBoxDownloadQuality, 0, Qt.AlignmentFlag.AlignRight)


        self.horizontalLayout_3.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.linkContentWidget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addWidget(self.widget_2)


        self.horizontalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignVCenter)

        self.sideBarWidget = QWidget(self.centralwidget)
        self.sideBarWidget.setObjectName(u"sideBarWidget")
        sizePolicy.setHeightForWidth(self.sideBarWidget.sizePolicy().hasHeightForWidth())
        self.sideBarWidget.setSizePolicy(sizePolicy)
        self.sideBarWidget.setMinimumSize(QSize(0, 400))
        self.sideBarWidget.setMaximumSize(QSize(550, 800))
        self.sideBarWidget.setStyleSheet(u"#sideBarWidget{\n"
"	\n"
"	background-color: #2b2b2b\n"
"}")
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
        self.downloadAllBtn.setStyleSheet(u"#downloadAllBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"}\n"
"\n"
"#downloadAllBtn:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: #1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"")

        self.horizontalLayout_5.addWidget(self.downloadAllBtn)

        self.comboBoxDownloadAllOpt = QComboBox(self.widget_5)
        self.comboBoxDownloadAllOpt.addItem("")
        self.comboBoxDownloadAllOpt.addItem("")
        self.comboBoxDownloadAllOpt.setObjectName(u"comboBoxDownloadAllOpt")
        self.comboBoxDownloadAllOpt.setMinimumSize(QSize(100, 40))
        self.comboBoxDownloadAllOpt.setMaximumSize(QSize(200, 40))
        self.comboBoxDownloadAllOpt.setStyleSheet(u"#comboBoxDownloadAllOpt{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"	padding-left: 80px;\n"
"	/* T\u00d9Y CH\u1ec8NH FONT CH\u1eee */\n"
"    font-family: \"Segoe UI\", Helvetica, Arial, sans-serif; /* D\u00f9ng font ch\u1eef kh\u00f4ng ch\u00e2n hi\u1ec7n \u0111\u1ea1i */\n"
"    font-size: 11pt;           /* T\u0103ng k\u00edch th\u01b0\u1edbc ch\u1eef cho c\u00e2n \u0111\u1ed1i (c\u00f3 th\u1ec3 ch\u1ec9nh l\u1ea1i s\u1ed1 n\u00e0y) */\n"
"    font-weight: bold;         /* \u0110\u1ed9 \u0111\u1eadm c\u1ee7a ch\u1eef (\u0110\u00e2y l\u00e0 ch\u00eca kh\u00f3a \u0111\u1ec3 gi\u1ed1ng \u1ea3nh m\u1eabu) */\n"
"}\n"
"\n"
"#comboBoxDownloadAllOpt:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDownloadAllOpt::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top"
                        " right;\n"
"    width: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#comboBoxDownloadAllOpt::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}")

        self.horizontalLayout_5.addWidget(self.comboBoxDownloadAllOpt)

        self.miniSideBarBtn = QPushButton(self.widget_5)
        self.miniSideBarBtn.setObjectName(u"miniSideBarBtn")
        self.miniSideBarBtn.setMaximumSize(QSize(30, 30))
        self.miniSideBarBtn.setStyleSheet(u"#miniSideBarBtn{\n"
"	border: 1px lipid transparent;\n"
"	\n"
"	background-color: transparent;\n"
"}")

        self.horizontalLayout_5.addWidget(self.miniSideBarBtn)


        self.verticalLayout_7.addWidget(self.widget_5)

        self.widget_7 = QWidget(self.widget_10)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy1.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, 20, -1)
        self.progressBar = QProgressBar(self.widget_7)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(200, 20))
        self.progressBar.setMaximumSize(QSize(200, 20))
        self.progressBar.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar)

        self.label_2 = QLabel(self.widget_7)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(300, 50))
        self.label_2.setMaximumSize(QSize(300, 50))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_7.addWidget(self.widget_7)


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
        self.scrollArea.setStyleSheet(u"#scrollArea{\n"
"	border:1px lipid black;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 54, 54))
        sizePolicy3.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy3)
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(500, 600))
        self.scrollAreaWidgetContents.setStyleSheet(u"#scrollAreaWidgetContents:vertical {\n"
"    width: 0px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"#scrollAreaWidgetContents:horizontal {\n"
"    height: 0px;\n"
"    background: transparent;\n"
"}")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_4.addWidget(self.scrollArea, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)


        self.horizontalLayout_2.addWidget(self.sideBarWidget, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.label_2.setText("")
    # retranslateUi

