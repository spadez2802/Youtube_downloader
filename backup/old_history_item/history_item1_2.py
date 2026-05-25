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

class Ui_historyItm(object):
    def setupUi(self, historyItm):
        if not historyItm.objectName():
            historyItm.setObjectName(u"historyItm")
        historyItm.resize(400, 38)
        historyItm.setMinimumSize(QSize(0, 32))
        historyItm.setMaximumSize(QSize(16777215, 38))
        historyItm.setStyleSheet(u"#historyItm:hover{\n"
"	border: 1px solid transparent;\n"
"	border-radius:16px;\n"
"	background-color: rgb(67,67,67);\n"
"}")
        self.horizontalLayout = QHBoxLayout(historyItm)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(historyItm)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignLeft)

        self.deleteHistoryBtn = QPushButton(historyItm)
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


        self.retranslateUi(historyItm)

        QMetaObject.connectSlotsByName(historyItm)
    # setupUi

    def retranslateUi(self, historyItm):
        historyItm.setWindowTitle(QCoreApplication.translate("historyItm", u"Form", None))
        self.label.setText("")
        self.deleteHistoryBtn.setText(QCoreApplication.translate("historyItm", u"\u2715", None))
    # retranslateUi

