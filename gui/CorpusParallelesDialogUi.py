# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_corpusParalleles.ui'
#
# Created: Fri Jan  6 15:07:17 2012
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_CorpusParallelesDialog(object):
    def setupUi(self, CorpusParallelesDialog):
        CorpusParallelesDialog.setObjectName("CorpusParallelesDialog")
        CorpusParallelesDialog.resize(723, 344)
        self.gridLayout = QtGui.QGridLayout(CorpusParallelesDialog)
        self.gridLayout.setContentsMargins(-1, 10, -1, 10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(25)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(CorpusParallelesDialog)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.srcTextEdit = QtGui.QTextEdit(CorpusParallelesDialog)
        self.srcTextEdit.setObjectName("srcTextEdit")
        self.verticalLayout_2.addWidget(self.srcTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtGui.QLabel(CorpusParallelesDialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.destTextEdit = QtGui.QTextEdit(CorpusParallelesDialog)
        self.destTextEdit.setObjectName("destTextEdit")
        self.verticalLayout.addWidget(self.destTextEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(CorpusParallelesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(CorpusParallelesDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), CorpusParallelesDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), CorpusParallelesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(CorpusParallelesDialog)

    def retranslateUi(self, CorpusParallelesDialog):
        CorpusParallelesDialog.setWindowTitle(QtGui.QApplication.translate("CorpusParallelesDialog", "Pythonn\'d - Apprendre par corpus parallèles", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CorpusParallelesDialog", "Texte <b>source</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CorpusParallelesDialog", "Texte <b>destination</b>", None, QtGui.QApplication.UnicodeUTF8))

