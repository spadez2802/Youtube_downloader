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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 100)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(300, 100))
        Form.setMaximumSize(QSize(300, 100))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labelImg = QLabel(Form)
        self.labelImg.setObjectName(u"labelImg")

        self.horizontalLayout.addWidget(self.labelImg)

        self.labelName = QLabel(Form)
        self.labelName.setObjectName(u"labelName")

        self.horizontalLayout.addWidget(self.labelName)

        self.downloadVBtn = QPushButton(Form)
        self.downloadVBtn.setObjectName(u"downloadVBtn")
        self.downloadVBtn.setMinimumSize(QSize(80, 40))
        self.downloadVBtn.setMaximumSize(QSize(80, 40))
        self.downloadVBtn.setStyleSheet(u"#downloadVBtn{\n"
"	\n"
"	border: 2px solid;\n"
"	border-color: rgb(255, 85, 0);\n"
"	border-radius:20px;\n"
"	background-color: rgb(67, 67, 67);\n"
"	color : white;\n"
"\n"
"}\n"
"\n"
"#downloadVBtn:hover{\n"
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

        self.horizontalLayout.addWidget(self.downloadVBtn)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labelImg.setText("")
        self.labelName.setText("")
        self.downloadVBtn.setText(QCoreApplication.translate("Form", u"Download", None))
    # retranslateUi

