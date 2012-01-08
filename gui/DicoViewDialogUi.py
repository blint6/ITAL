# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_dicoView.ui'
#
# Created: Sun Jan  8 17:02:36 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DicoViewDialog(object):
    def setupUi(self, DicoViewDialog):
        DicoViewDialog.setObjectName("DicoViewDialog")
        DicoViewDialog.resize(400, 300)
        self.gridLayout = QtGui.QGridLayout(DicoViewDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtGui.QTableView(DicoViewDialog)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DicoViewDialog)
        QtCore.QMetaObject.connectSlotsByName(DicoViewDialog)

    def retranslateUi(self, DicoViewDialog):
        DicoViewDialog.setWindowTitle(QtGui.QApplication.translate("DicoViewDialog", "Dictionnaire", None, QtGui.QApplication.UnicodeUTF8))

