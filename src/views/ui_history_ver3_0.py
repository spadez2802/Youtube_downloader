# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_item2.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QToolButton, QVBoxLayout,
    QWidget)

class Ui_FormHistoryItem(object):
    def setupUi(self, FormHistoryItem):
        if not FormHistoryItem.objectName():
            FormHistoryItem.setObjectName(u"FormHistoryItem")
        FormHistoryItem.resize(400, 70)
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
        self.cbbOpt.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)

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

