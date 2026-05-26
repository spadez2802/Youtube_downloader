# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mini.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_miniCard(object):
    def setupUi(self, miniCard):
        if not miniCard.objectName():
            miniCard.setObjectName(u"miniCard")
        miniCard.resize(450, 150)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(miniCard.sizePolicy().hasHeightForWidth())
        miniCard.setSizePolicy(sizePolicy)
        miniCard.setMinimumSize(QSize(450, 150))
        miniCard.setMaximumSize(QSize(450, 150))
        miniCard.setStyleSheet(u"#miniCard{\n"
"	border: 5px solid transparent;\n"
"	border-radius:20px;\n"
"	background-color: rgb(0, 0, 0);\n"
"\n"
"}")
        self.horizontalLayout = QHBoxLayout(miniCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelImg = QLabel(miniCard)
        self.labelImg.setObjectName(u"labelImg")

        self.horizontalLayout.addWidget(self.labelImg)

        self.labelName = QLabel(miniCard)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayout.addWidget(self.labelName)

        self.widgetDownloadOpt = QWidget(miniCard)
        self.widgetDownloadOpt.setObjectName(u"widgetDownloadOpt")
        self.widgetDownloadOpt.setMinimumSize(QSize(100, 100))
        self.widgetDownloadOpt.setMaximumSize(QSize(100, 200))
        self.widgetDownloadOpt.setStyleSheet(u"#widgetDownloadOpt{\n"
"	\n"
"	background-color: transparent;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widgetDownloadOpt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.downloadVBtn = QPushButton(self.widgetDownloadOpt)
        self.downloadVBtn.setObjectName(u"downloadVBtn")
        self.downloadVBtn.setMinimumSize(QSize(80, 40))
        self.downloadVBtn.setMaximumSize(QSize(80, 40))
        self.downloadVBtn.setStyleSheet(u"#downloadVBtn{\n"
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
"#downloadVBtn:hover{\n"
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

        self.verticalLayout.addWidget(self.downloadVBtn)

        self.comboBoxDownloadOpt = QComboBox(self.widgetDownloadOpt)
        self.comboBoxDownloadOpt.addItem("")
        self.comboBoxDownloadOpt.addItem("")
        self.comboBoxDownloadOpt.setObjectName(u"comboBoxDownloadOpt")
        self.comboBoxDownloadOpt.setMinimumSize(QSize(80, 40))
        self.comboBoxDownloadOpt.setMaximumSize(QSize(80, 40))
        self.comboBoxDownloadOpt.setStyleSheet(u"#comboBoxDownloadOpt{\n"
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
"#comboBoxDownloadOpt:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color :black;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDownloadOpt::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
""
                        "    width: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#comboBoxDownloadOpt::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.comboBoxDownloadOpt)

        self.comboBoxDQuality = QComboBox(self.widgetDownloadOpt)
        self.comboBoxDQuality.setObjectName(u"comboBoxDQuality")
        self.comboBoxDQuality.setMinimumSize(QSize(80, 40))
        self.comboBoxDQuality.setMaximumSize(QSize(80, 40))
        self.comboBoxDQuality.setStyleSheet(u"#comboBoxDQuality{\n"
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
"#comboBoxDQuality:hover{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: #1ED761;\n"
"	border-radius:20px;\n"
"	background-color:#1ED761;\n"
"	color : black;\n"
"	\n"
"}\n"
"\n"
"#comboBoxDQuality::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    wi"
                        "dth: 25px;\n"
"    border-top-right-radius: 10px; /* Bo g\u00f3c cho ph\u1ea7n n\u00fat b\u00ean ph\u1ea3i */\n"
"    border-bottom-right-radius: 10px;\n"
"    \n"
"}\n"
"\n"
"#comboBoxDQuality::down-arrow {\n"
"	image: url(\"E:/design/ytb_playlist_downloader/img/icon/down_arrow.png\");\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    \n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right: 10px;\n"
"}")

        self.verticalLayout.addWidget(self.comboBoxDQuality)


        self.horizontalLayout.addWidget(self.widgetDownloadOpt)


        self.retranslateUi(miniCard)

        QMetaObject.connectSlotsByName(miniCard)
    # setupUi

    def retranslateUi(self, miniCard):
        miniCard.setWindowTitle(QCoreApplication.translate("miniCard", u"Form", None))
        self.labelImg.setText("")
        self.labelName.setText("")
        self.downloadVBtn.setText(QCoreApplication.translate("miniCard", u"Download", None))
        self.comboBoxDownloadOpt.setItemText(0, QCoreApplication.translate("miniCard", u"MP3", None))
        self.comboBoxDownloadOpt.setItemText(1, QCoreApplication.translate("miniCard", u"MP4", None))

    # retranslateUi

