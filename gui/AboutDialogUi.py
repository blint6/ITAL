# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_about.ui'
#
# Created: Tue Jan  3 22:43:42 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AboutDialog(object):
    def setupUi(self, AboutDialog):
        AboutDialog.setObjectName("AboutDialog")
        AboutDialog.resize(388, 194)
        self.buttonBox = QtGui.QDialogButtonBox(AboutDialog)
        self.buttonBox.setGeometry(QtCore.QRect(200, 150, 163, 25))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtGui.QLabel(AboutDialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setMargin(0)
        self.label.setObjectName("label")

        self.retranslateUi(AboutDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AboutDialog.close)
        QtCore.QMetaObject.connectSlotsByName(AboutDialog)

    def retranslateUi(self, AboutDialog):
        AboutDialog.setWindowTitle(QtGui.QApplication.translate("AboutDialog", "À propos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AboutDialog", "Ce programme a été conçu par Nicolas Gasull et Maxime Khoy dans le cadre du projet de traîtement automatique de la langue de l\'ENSIIE. (janvier 2012)", None, QtGui.QApplication.UnicodeUTF8))

