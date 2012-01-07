'''
Created on 6 janv. 2012

@author: Nicolas Gasull
'''

from CorpusParallelesDialogUi import Ui_CorpusParallelesDialog
from PySide import QtGui

class CorpusParallelesDialog(Ui_CorpusParallelesDialog):
    
    def __init__(self, pythonndITAL):
        self.widget = QtGui.QDialog()
        self.setupUi(self.widget)
        
        pythonndITAL.statusbar.showMessage("Voila")
        
        self.buttonBox.accepted.connect(self.processCorpus)
        
        self.widget.show()
    
    def processCorpus(self):
        self.accept()