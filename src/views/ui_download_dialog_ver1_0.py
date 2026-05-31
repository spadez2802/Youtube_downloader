# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'download_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.progressBar = QProgressBar(self.widget_2)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.horizontalLayout.addWidget(self.progressBar)

        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_3 = QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btnPauseContinue = QPushButton(self.widget_3)
        self.btnPauseContinue.setObjectName(u"btnPauseContinue")
        self.btnPauseContinue.setStyleSheet(u"#btnPauseContinue{\n"
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
"#btnPauseContinue:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#btnPauseContinue::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    wi"
                        "dth: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#btnPauseContinue::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"#btnPauseContinue:disabled{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(136, 136, 136);\n"
"	border-radius:20px;\n"
"	background-color:rgb(67, 67, 67);\n"
"	color : transparent;\n"
"	\n"
"}")

        self.verticalLayout_3.addWidget(self.btnPauseContinue)

        self.btnCancel = QPushButton(self.widget_3)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setStyleSheet(u"#btnCancel{\n"
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
"#btnCancel:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#btnCancel::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    bo"
                        "rder-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#btnCancel::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}\n"
"\n"
"#btnCancel:disabled{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(136, 136, 136);\n"
"	border-radius:20px;\n"
"	background-color:rgb(67, 67, 67);\n"
"	color : transparent;\n"
"	\n"
"}")

        self.verticalLayout_3.addWidget(self.btnCancel)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labelThumbnail = QLabel(self.widget)
        self.labelThumbnail.setObjectName(u"labelThumbnail")

        self.verticalLayout.addWidget(self.labelThumbnail)

        self.videoName = QTextEdit(self.widget)
        self.videoName.setObjectName(u"videoName")

        self.verticalLayout.addWidget(self.videoName)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.btnPauseContinue.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.btnCancel.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.labelThumbnail.setText(QCoreApplication.translate("Dialog", u"TextLabel", None))
    # retranslateUi

