'''
Created on 3 janv. 2012

@author: Nicolas Gasull
'''

import sys

from PythonndITALUi import Ui_PythonndITAL
from AboutDialogUi import Ui_AboutDialog
from CorpusParallelesDialog import CorpusParallelesDialog
from PySide import QtGui

class PythonndITAL(Ui_PythonndITAL):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.app = QtGui.QApplication(sys.argv)
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        
        self.actionAbout.triggered.connect(self.showAbout)
        self.actionBiCorpusMonolingue.triggered.connect(self.showCorpusParalleles)
        
    def show(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())
        
    def showAbout(self):
        self.about = QtGui.QDialog()
        aboutUi = Ui_AboutDialog()
        aboutUi.setupUi(self.about)
        self.about.show()

    def showCorpusParalleles(self):
        self.corpusParalleles = CorpusParallelesDialog(self)
        




