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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")

        self.horizontalLayout.addWidget(self.checkBox)

        self.timeText = QTextEdit(self.widget)
        self.timeText.setObjectName(u"timeText")

        self.horizontalLayout.addWidget(self.timeText)

        self.btnDelete = QPushButton(self.widget)
        self.btnDelete.setObjectName(u"btnDelete")

        self.horizontalLayout.addWidget(self.btnDelete)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nameText = QTextEdit(self.widget_2)
        self.nameText.setObjectName(u"nameText")

        self.horizontalLayout_2.addWidget(self.nameText)

        self.btnCopy = QPushButton(self.widget_2)
        self.btnCopy.setObjectName(u"btnCopy")

        self.horizontalLayout_2.addWidget(self.btnCopy)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox.setText("")
        self.btnDelete.setText(QCoreApplication.translate("Form", u"Delete", None))
        self.btnCopy.setText(QCoreApplication.translate("Form", u"Copy", None))
    # retranslateUi

