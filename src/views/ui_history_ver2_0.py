# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_item2.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormHistoryItem(object):
    def setupUi(self, FormHistoryItem):
        if not FormHistoryItem.objectName():
            FormHistoryItem.setObjectName(u"FormHistoryItem")
        FormHistoryItem.resize(400, 70)
        FormHistoryItem.setStyleSheet(u"/* Tr\u1ea1ng th\u00e1i b\u00ecnh th\u01b0\u1eddng: N\u1ec1n trong su\u1ed1t */\n"
"#FormHistoryItem {\n"
"  background-color: transparent;\n"
"  \n"
"  /* Ch\u1ec9 \u00e1p d\u1ee5ng hi\u1ec7u \u1ee9ng chuy\u1ec3n \u0111\u1ed5i cho m\u00e0u n\u1ec1n \u0111\u1ec3 tr\u00e1nh \u1ea3nh h\u01b0\u1edfng c\u00e1c thu\u1ed9c t\u00ednh kh\u00e1c */\n"
"  transition: background-color 0.2s ease-in-out; \n"
"}\n"
"\n"
"/* Tr\u1ea1ng th\u00e1i khi di chu\u1ed9t v\u00e0o (hover): N\u1ec1n s\u00e1ng l\u00ean */\n"
"#FormHistoryItem:hover {\n"
"  /* M\u00e3 m\u00e0u v\u00ed d\u1ee5: Tr\u1eafng m\u1edd. B\u1ea1n c\u00f3 th\u1ec3 \u0111\u1ed5i sang m\u00e0u kh\u00e1c ph\u00f9 h\u1ee3p v\u1edbi giao di\u1ec7n */\n"
"  background-color: rgba(255, 255, 255, 0.15); \n"
"}\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(FormHistoryItem)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetDate = QWidget(FormHistoryItem)
        self.widgetDate.setObjectName(u"widgetDate")
        self.horizontalLayoutDate = QHBoxLayout(self.widgetDate)
        self.horizontalLayoutDate.setSpacing(4)
        self.horizontalLayoutDate.setObjectName(u"horizontalLayoutDate")
        self.horizontalLayoutDate.setContentsMargins(4, 2, 4, 2)
        self.labelDate = QLabel(self.widgetDate)
        self.labelDate.setObjectName(u"labelDate")

        self.horizontalLayoutDate.addWidget(self.labelDate)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayoutDate.addItem(self.horizontalSpacer)

        self.labelType = QLabel(self.widgetDate)
        self.labelType.setObjectName(u"labelType")

        self.horizontalLayoutDate.addWidget(self.labelType)


        self.verticalLayout.addWidget(self.widgetDate)

        self.widget = QWidget(FormHistoryItem)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.checkBox)

        self.labelName = QLabel(self.widget)
        self.labelName.setObjectName(u"labelName")
        self.labelName.setMaximumSize(QSize(16777215, 34))
        self.labelName.setWordWrap(True)

        self.horizontalLayout.addWidget(self.labelName)

        self.cbbOpt = QToolButton(self.widget)
        self.cbbOpt.setObjectName(u"cbbOpt")
        self.cbbOpt.setMaximumSize(QSize(20, 16777215))
        self.cbbOpt.setStyleSheet(u"QToolButton { background: transparent; border: none; color: #b3b3b3; font-size: 16px; font-weight: bold; } QToolButton:hover { color: white; } QToolButton::menu-indicator { image: none; }")
        self.cbbOpt.setPopupMode(QToolButton.InstantPopup)

        self.horizontalLayout.addWidget(self.cbbOpt)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(FormHistoryItem)

        QMetaObject.connectSlotsByName(FormHistoryItem)
    # setupUi

    def retranslateUi(self, FormHistoryItem):
        FormHistoryItem.setWindowTitle(QCoreApplication.translate("FormHistoryItem", u"Form", None))
        self.labelDate.setText(QCoreApplication.translate("FormHistoryItem", u"TextLabel", None))
        self.labelType.setText(QCoreApplication.translate("FormHistoryItem", u"[Video]", None))
        self.checkBox.setText("")
        self.labelName.setText(QCoreApplication.translate("FormHistoryItem", u"TextLabel", None))
        self.cbbOpt.setText(QCoreApplication.translate("FormHistoryItem", u"\u22ee", None))
    # retranslateUi

