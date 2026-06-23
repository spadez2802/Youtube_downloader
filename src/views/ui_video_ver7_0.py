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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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
        self.horizontalLayout = QHBoxLayout(miniCard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelImg = QLabel(miniCard)
        self.labelImg.setObjectName(u"labelImg")

        self.horizontalLayout.addWidget(self.labelImg)

        self.widget = QWidget(miniCard)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelName = QLabel(self.widget)
        self.labelName.setObjectName(u"labelName")

        self.verticalLayout_2.addWidget(self.labelName)

        self.checkBoxDownload = QCheckBox(self.widget)
        self.checkBoxDownload.setObjectName(u"checkBoxDownload")

        self.verticalLayout_2.addWidget(self.checkBoxDownload)


        self.horizontalLayout.addWidget(self.widget)

        self.widgetDownloadOpt = QWidget(miniCard)
        self.widgetDownloadOpt.setObjectName(u"widgetDownloadOpt")
        self.widgetDownloadOpt.setMinimumSize(QSize(100, 100))
        self.widgetDownloadOpt.setMaximumSize(QSize(100, 200))
        self.verticalLayout = QVBoxLayout(self.widgetDownloadOpt)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 5, -1, 5)
        self.downloadVBtn = QPushButton(self.widgetDownloadOpt)
        self.downloadVBtn.setObjectName(u"downloadVBtn")
        self.downloadVBtn.setMinimumSize(QSize(80, 40))
        self.downloadVBtn.setMaximumSize(QSize(80, 40))

        self.verticalLayout.addWidget(self.downloadVBtn)

        self.comboBoxDownloadOpt = QComboBox(self.widgetDownloadOpt)
        self.comboBoxDownloadOpt.addItem("")
        self.comboBoxDownloadOpt.addItem("")
        self.comboBoxDownloadOpt.setObjectName(u"comboBoxDownloadOpt")
        self.comboBoxDownloadOpt.setMinimumSize(QSize(80, 40))
        self.comboBoxDownloadOpt.setMaximumSize(QSize(80, 40))

        self.verticalLayout.addWidget(self.comboBoxDownloadOpt)

        self.comboBoxDQuality = QComboBox(self.widgetDownloadOpt)
        self.comboBoxDQuality.setObjectName(u"comboBoxDQuality")
        self.comboBoxDQuality.setMinimumSize(QSize(80, 40))
        self.comboBoxDQuality.setMaximumSize(QSize(80, 40))

        self.verticalLayout.addWidget(self.comboBoxDQuality)


        self.horizontalLayout.addWidget(self.widgetDownloadOpt)


        self.retranslateUi(miniCard)

        QMetaObject.connectSlotsByName(miniCard)
    # setupUi

    def retranslateUi(self, miniCard):
        miniCard.setWindowTitle(QCoreApplication.translate("miniCard", u"Form", None))
        self.labelImg.setText("")
        self.labelName.setText("")
        self.checkBoxDownload.setText(QCoreApplication.translate("miniCard", u"Download", None))
        self.downloadVBtn.setText(QCoreApplication.translate("miniCard", u"Download", None))
        self.comboBoxDownloadOpt.setItemText(0, QCoreApplication.translate("miniCard", u"MP3", None))
        self.comboBoxDownloadOpt.setItemText(1, QCoreApplication.translate("miniCard", u"MP4", None))

    # retranslateUi

