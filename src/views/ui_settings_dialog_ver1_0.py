# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(480, 520)
        SettingsDialog.setMinimumSize(QSize(460, 480))
        self.rootLayout = QVBoxLayout(SettingsDialog)
        self.rootLayout.setSpacing(0)
        self.rootLayout.setObjectName(u"rootLayout")
        self.rootLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(SettingsDialog)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        self.tabGeneralLayout = QVBoxLayout(self.tabGeneral)
        self.tabGeneralLayout.setSpacing(14)
        self.tabGeneralLayout.setObjectName(u"tabGeneralLayout")
        self.tabGeneralLayout.setContentsMargins(16, 16, 16, 16)
        self.grpAppearance = QGroupBox(self.tabGeneral)
        self.grpAppearance.setObjectName(u"grpAppearance")
        self.grpAppearanceLayout = QHBoxLayout(self.grpAppearance)
        self.grpAppearanceLayout.setObjectName(u"grpAppearanceLayout")
        self.lblAccent = QLabel(self.grpAppearance)
        self.lblAccent.setObjectName(u"lblAccent")

        self.grpAppearanceLayout.addWidget(self.lblAccent)

        self.btnAccentPreview = QPushButton(self.grpAppearance)
        self.btnAccentPreview.setObjectName(u"btnAccentPreview")
        self.btnAccentPreview.setMinimumSize(QSize(36, 28))
        self.btnAccentPreview.setMaximumSize(QSize(36, 28))

        self.grpAppearanceLayout.addWidget(self.btnAccentPreview)

        self.spacerAppearance = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grpAppearanceLayout.addItem(self.spacerAppearance)


        self.tabGeneralLayout.addWidget(self.grpAppearance)

        self.grpFolder = QGroupBox(self.tabGeneral)
        self.grpFolder.setObjectName(u"grpFolder")
        self.grpFolderLayout = QVBoxLayout(self.grpFolder)
        self.grpFolderLayout.setSpacing(8)
        self.grpFolderLayout.setObjectName(u"grpFolderLayout")
        self.chkSubfolder = QCheckBox(self.grpFolder)
        self.chkSubfolder.setObjectName(u"chkSubfolder")

        self.grpFolderLayout.addWidget(self.chkSubfolder)

        self.chkOpenAfter = QCheckBox(self.grpFolder)
        self.chkOpenAfter.setObjectName(u"chkOpenAfter")

        self.grpFolderLayout.addWidget(self.chkOpenAfter)


        self.tabGeneralLayout.addWidget(self.grpFolder)

        self.grpDownload = QGroupBox(self.tabGeneral)
        self.grpDownload.setObjectName(u"grpDownload")
        self.grpDownloadLayout = QVBoxLayout(self.grpDownload)
        self.grpDownloadLayout.setSpacing(10)
        self.grpDownloadLayout.setObjectName(u"grpDownloadLayout")
        self.rowFormat = QHBoxLayout()
        self.rowFormat.setObjectName(u"rowFormat")
        self.lblFormat = QLabel(self.grpDownload)
        self.lblFormat.setObjectName(u"lblFormat")

        self.rowFormat.addWidget(self.lblFormat)

        self.cmbFormat = QComboBox(self.grpDownload)
        self.cmbFormat.addItem("")
        self.cmbFormat.addItem("")
        self.cmbFormat.setObjectName(u"cmbFormat")

        self.rowFormat.addWidget(self.cmbFormat)

        self.spacerFormat = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowFormat.addItem(self.spacerFormat)


        self.grpDownloadLayout.addLayout(self.rowFormat)

        self.rowQuality = QHBoxLayout()
        self.rowQuality.setObjectName(u"rowQuality")
        self.lblQuality = QLabel(self.grpDownload)
        self.lblQuality.setObjectName(u"lblQuality")

        self.rowQuality.addWidget(self.lblQuality)

        self.cmbQuality = QComboBox(self.grpDownload)
        self.cmbQuality.addItem("")
        self.cmbQuality.addItem("")
        self.cmbQuality.addItem("")
        self.cmbQuality.addItem("")
        self.cmbQuality.addItem("")
        self.cmbQuality.setObjectName(u"cmbQuality")

        self.rowQuality.addWidget(self.cmbQuality)

        self.spacerQuality = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowQuality.addItem(self.spacerQuality)


        self.grpDownloadLayout.addLayout(self.rowQuality)

        self.rowBitrate = QHBoxLayout()
        self.rowBitrate.setObjectName(u"rowBitrate")
        self.lblBitrate = QLabel(self.grpDownload)
        self.lblBitrate.setObjectName(u"lblBitrate")

        self.rowBitrate.addWidget(self.lblBitrate)

        self.cmbBitrate = QComboBox(self.grpDownload)
        self.cmbBitrate.addItem("")
        self.cmbBitrate.addItem("")
        self.cmbBitrate.addItem("")
        self.cmbBitrate.setObjectName(u"cmbBitrate")

        self.rowBitrate.addWidget(self.cmbBitrate)

        self.spacerBitrate = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.rowBitrate.addItem(self.spacerBitrate)


        self.grpDownloadLayout.addLayout(self.rowBitrate)


        self.tabGeneralLayout.addWidget(self.grpDownload)

        self.grpHistory = QGroupBox(self.tabGeneral)
        self.grpHistory.setObjectName(u"grpHistory")
        self.grpHistoryLayout = QHBoxLayout(self.grpHistory)
        self.grpHistoryLayout.setObjectName(u"grpHistoryLayout")
        self.lblHistory = QLabel(self.grpHistory)
        self.lblHistory.setObjectName(u"lblHistory")

        self.grpHistoryLayout.addWidget(self.lblHistory)

        self.spacerHistory = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.grpHistoryLayout.addItem(self.spacerHistory)

        self.btnClearHistory = QPushButton(self.grpHistory)
        self.btnClearHistory.setObjectName(u"btnClearHistory")

        self.grpHistoryLayout.addWidget(self.btnClearHistory)


        self.tabGeneralLayout.addWidget(self.grpHistory)

        self.stretchGeneral = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.tabGeneralLayout.addItem(self.stretchGeneral)

        self.tabWidget.addTab(self.tabGeneral, "")
        self.tabAdvanced = QWidget()
        self.tabAdvanced.setObjectName(u"tabAdvanced")
        self.tabAdvancedLayout = QVBoxLayout(self.tabAdvanced)
        self.tabAdvancedLayout.setSpacing(14)
        self.tabAdvancedLayout.setObjectName(u"tabAdvancedLayout")
        self.tabAdvancedLayout.setContentsMargins(16, 16, 16, 16)
        self.grpPath = QGroupBox(self.tabAdvanced)
        self.grpPath.setObjectName(u"grpPath")
        self.grpPathLayout = QVBoxLayout(self.grpPath)
        self.grpPathLayout.setSpacing(10)
        self.grpPathLayout.setObjectName(u"grpPathLayout")
        self.chkDefaultPath = QCheckBox(self.grpPath)
        self.chkDefaultPath.setObjectName(u"chkDefaultPath")

        self.grpPathLayout.addWidget(self.chkDefaultPath)

        self.rowPath = QHBoxLayout()
        self.rowPath.setObjectName(u"rowPath")
        self.txtPath = QLineEdit(self.grpPath)
        self.txtPath.setObjectName(u"txtPath")
        self.txtPath.setReadOnly(True)

        self.rowPath.addWidget(self.txtPath)

        self.btnChangePath = QPushButton(self.grpPath)
        self.btnChangePath.setObjectName(u"btnChangePath")

        self.rowPath.addWidget(self.btnChangePath)


        self.grpPathLayout.addLayout(self.rowPath)

        self.chkOriginalName = QCheckBox(self.grpPath)
        self.chkOriginalName.setObjectName(u"chkOriginalName")

        self.grpPathLayout.addWidget(self.chkOriginalName)


        self.tabAdvancedLayout.addWidget(self.grpPath)

        self.stretchAdvanced = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.tabAdvancedLayout.addItem(self.stretchAdvanced)

        self.tabWidget.addTab(self.tabAdvanced, "")

        self.rootLayout.addWidget(self.tabWidget)

        self.separator = QFrame(SettingsDialog)
        self.separator.setObjectName(u"separator")
        self.separator.setFrameShape(QFrame.Shape.HLine)
        self.separator.setFrameShadow(QFrame.Shadow.Sunken)

        self.rootLayout.addWidget(self.separator)

        self.btnRow = QHBoxLayout()
        self.btnRow.setObjectName(u"btnRow")
        self.btnRow.setContentsMargins(16, 10, 16, 10)
        self.spacerBtnRow = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.btnRow.addItem(self.spacerBtnRow)

        self.btnCancel = QPushButton(SettingsDialog)
        self.btnCancel.setObjectName(u"btnCancel")
        self.btnCancel.setMinimumSize(QSize(90, 0))

        self.btnRow.addWidget(self.btnCancel)

        self.btnSave = QPushButton(SettingsDialog)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(90, 0))

        self.btnRow.addWidget(self.btnSave)


        self.rootLayout.addLayout(self.btnRow)


        self.retranslateUi(SettingsDialog)

        self.tabWidget.setCurrentIndex(0)
        self.btnSave.setDefault(True)


        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Settings", None))
        self.grpAppearance.setTitle(QCoreApplication.translate("SettingsDialog", u"Giao di\u1ec7n", None))
        self.lblAccent.setText(QCoreApplication.translate("SettingsDialog", u"M\u00e0u Accent:", None))
#if QT_CONFIG(tooltip)
        self.btnAccentPreview.setToolTip(QCoreApplication.translate("SettingsDialog", u"Nh\u1ea5n \u0111\u1ec3 ch\u1ecdn m\u00e0u accent", None))
#endif // QT_CONFIG(tooltip)
        self.btnAccentPreview.setText("")
        self.grpFolder.setTitle(QCoreApplication.translate("SettingsDialog", u"Th\u01b0 m\u1ee5c l\u01b0u file", None))
        self.chkSubfolder.setText(QCoreApplication.translate("SettingsDialog", u"T\u1ef1 \u0111\u1ed9ng t\u1ea1o subfolder t\u00ean playlist", None))
        self.chkOpenAfter.setText(QCoreApplication.translate("SettingsDialog", u"M\u1edf th\u01b0 m\u1ee5c sau khi t\u1ea3i xong", None))
        self.grpDownload.setTitle(QCoreApplication.translate("SettingsDialog", u"T\u1ea3i xu\u1ed1ng m\u1eb7c \u0111\u1ecbnh", None))
        self.lblFormat.setText(QCoreApplication.translate("SettingsDialog", u"\u0110\u1ecbnh d\u1ea1ng m\u1eb7c \u0111\u1ecbnh:", None))
        self.cmbFormat.setItemText(0, QCoreApplication.translate("SettingsDialog", u"MP4", None))
        self.cmbFormat.setItemText(1, QCoreApplication.translate("SettingsDialog", u"MP3", None))

        self.lblQuality.setText(QCoreApplication.translate("SettingsDialog", u"Ch\u1ea5t l\u01b0\u1ee3ng m\u1eb7c \u0111\u1ecbnh:", None))
        self.cmbQuality.setItemText(0, QCoreApplication.translate("SettingsDialog", u"Best", None))
        self.cmbQuality.setItemText(1, QCoreApplication.translate("SettingsDialog", u"1080p", None))
        self.cmbQuality.setItemText(2, QCoreApplication.translate("SettingsDialog", u"720p", None))
        self.cmbQuality.setItemText(3, QCoreApplication.translate("SettingsDialog", u"480p", None))
        self.cmbQuality.setItemText(4, QCoreApplication.translate("SettingsDialog", u"360p", None))

        self.lblBitrate.setText(QCoreApplication.translate("SettingsDialog", u"Bitrate MP3:", None))
        self.cmbBitrate.setItemText(0, QCoreApplication.translate("SettingsDialog", u"320kbps", None))
        self.cmbBitrate.setItemText(1, QCoreApplication.translate("SettingsDialog", u"192kbps", None))
        self.cmbBitrate.setItemText(2, QCoreApplication.translate("SettingsDialog", u"128kbps", None))

        self.grpHistory.setTitle(QCoreApplication.translate("SettingsDialog", u"L\u1ecbch s\u1eed", None))
        self.lblHistory.setText(QCoreApplication.translate("SettingsDialog", u"X\u00f3a to\u00e0n b\u1ed9 l\u1ecbch s\u1eed:", None))
        self.btnClearHistory.setText(QCoreApplication.translate("SettingsDialog", u"X\u00f3a l\u1ecbch s\u1eed", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGeneral), QCoreApplication.translate("SettingsDialog", u"  C\u00e0i \u0111\u1eb7t chung  ", None))
        self.grpPath.setTitle(QCoreApplication.translate("SettingsDialog", u"\u0110\u01b0\u1eddng d\u1eabn t\u1ea3i xu\u1ed1ng", None))
        self.chkDefaultPath.setText(QCoreApplication.translate("SettingsDialog", u"S\u1eed d\u1ee5ng \u0111\u01b0\u1eddng d\u1eabn m\u1eb7c \u0111\u1ecbnh (kh\u00f4ng h\u1ecfi l\u1ea1i m\u1ed7i l\u1ea7n t\u1ea3i)", None))
        self.txtPath.setPlaceholderText(QCoreApplication.translate("SettingsDialog", u"Ch\u01b0a ch\u1ecdn th\u01b0 m\u1ee5c...", None))
        self.btnChangePath.setText(QCoreApplication.translate("SettingsDialog", u"Thay \u0111\u1ed5i...", None))
        self.chkOriginalName.setText(QCoreApplication.translate("SettingsDialog", u"T\u1ea3i xu\u1ed1ng v\u1edbi t\u00ean file g\u1ed1c (kh\u00f4ng h\u1ecfi t\u00ean)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAdvanced), QCoreApplication.translate("SettingsDialog", u"  N\u00e2ng cao  ", None))
        self.btnCancel.setText(QCoreApplication.translate("SettingsDialog", u"H\u1ee7y", None))
        self.btnSave.setText(QCoreApplication.translate("SettingsDialog", u"L\u01b0u", None))
    # retranslateUi

