# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_item.ui'
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
        Form.resize(400, 48)
        Form.setMinimumSize(QSize(0, 40))
        Form.setMaximumSize(QSize(16777215, 48))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.deleteHistoryBtn = QPushButton(Form)
        self.deleteHistoryBtn.setObjectName(u"deleteHistoryBtn")
        self.deleteHistoryBtn.setMinimumSize(QSize(30, 30))
        self.deleteHistoryBtn.setMaximumSize(QSize(30, 30))
        self.deleteHistoryBtn.setStyleSheet(u"#deleteHistoryBtn { \n"
"                background: transparent; \n"
"                color: #888; \n"
"                font-size: 16px; \n"
"                font-weight: bold; \n"
"                border: none; \n"
"                border-radius: 12px; \n"
"}\n"
"#deleteHistoryBtn:hover { \n"
"color: #ff4444; /* \u0110\u1ecf l\u00ean khi hover */\n"
" background: rgba(255, 68, 68, 0.2); \n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.deleteHistoryBtn, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.deleteHistoryBtn.setText(QCoreApplication.translate("Form", u"\u2715", None))
    # retranslateUi

