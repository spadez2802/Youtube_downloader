# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

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
        self.centralwidget.setMinimumSize(QSize(1000, 800))
        self.centralwidget.setCursor(QCursor(Qt.CursorShape.WaitCursor))
        self.centralwidget.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.centralwidget.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.centralwidget.setStyleSheet(u"#centralwidget{\n"
"    background-color: rgb(50, 50, 50)/* \u0110\u00e2y l\u00e0 m\u00e0u x\u00e1m \u0111en hi\u1ec7n \u0111\u1ea1i */\n"
"\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(600, 100))
        self.widget.setMaximumSize(QSize(600, 100))
        self.widget.setSizeIncrement(QSize(0, 0))
        self.widget.setStyleSheet(u"#widget{\n"
"	background-color: rgb(71, 71, 71);\n"
"	border-radius: 15px;\n"
"	background: #2b2b2b;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(141, 16777215))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(450, 40))
        self.lineEdit.setMaximumSize(QSize(450, 40))
        self.lineEdit.setStyleSheet(u"#lineEdit {\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: black;\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#lineEdit:hover{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(52, 52, 52);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"\n"
"#lineEdit:focus{\n"
"    /* Quan tr\u1ecdng: Ph\u1ea3i c\u00f3 border th\u00ec radius m\u1edbi ho\u1ea1"
                        "t \u0111\u1ed9ng chu\u1ea9n */\n"
"    border: 2px solid transparent; \n"
"    border-radius: 20px; /* Ch\u1ec9nh s\u1ed1 n\u00e0y cho \u0111\u1ebfn khi v\u1eeba \u00fd */\n"
"	background-color: rgb(29, 29, 29);\n"
"    color: white;\n"
"    padding: 5px 15px; /* Cho ch\u1eef c\u00e1ch l\u1ec1 ra m\u1ed9t ch\u00fat nh\u00ecn s\u1ebd sang h\u01a1n */\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

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
    # retranslateUi


