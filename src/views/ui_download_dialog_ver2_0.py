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

        self.verticalLayout_3.addWidget(self.btnPauseContinue)

        self.btnCancel = QPushButton(self.widget_3)
        self.btnCancel.setObjectName(u"btnCancel")

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

