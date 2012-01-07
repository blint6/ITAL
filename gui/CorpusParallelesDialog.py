'''
Created on 6 janv. 2012

@author: Nicolas Gasull
'''

from CorpusParallelesDialogUi import Ui_CorpusParallelesDialog
from PySide import QtGui

import subprocess

class CorpusParallelesDialog(Ui_CorpusParallelesDialog):
    
    def __init__(self, pythonndITAL):
        self.pythonndITAL = pythonndITAL
        
        self.widget = QtGui.QDialog()
        self.setupUi(self.widget)
        
        self.buttonBox.accepted.connect(self.processCorpus)
        
        self.widget.show()
    
    def processCorpus(self):
        
        self.pythonndITAL.statusbar.showMessage("Generation du dictionnaire pour le Bi-Corpus")
        
        file_name = 'para'
        dir_binaries = 'bin'
        dir_dictionnary = 'dic'
        dir_log = 'log'
        dir_process = 'process'
        '''        
        print "Creating dictionnary directory... ", 
        subprocess.call(['mkdir', dir_dictionnary])
        print
        
        print "Creating log directory... ", 
        subprocess.call(['mkdir', dir_log])
        print
        
        print "Creating processing directory... ", 
        subprocess.call(['mkdir', dir_process])
        print
        '''        
        with open('{0}/{1}.src'.format(dir_process, file_name), 'w') as src:
            src.write(self.srcTextEdit.toPlainText())
        with open('{0}/{1}.tgt'.format(dir_process, file_name), 'w') as src:
            src.write(self.destTextEdit.toPlainText())
        
        subprocess.call(['{0}/plain2snt.out'.format(dir_binaries),
                         '{0}/{1}.src'.format(dir_process, file_name),
                         '{0}/{1}.tgt'.format(dir_process, file_name)])
        
        with open('{0}/mkcls1.src.log'.format(dir_log), 'w') as log:
            subprocess.call(['{0}/mkcls'.format(dir_binaries), '-m2',
                             '-p{0}/{1}.src'.format(dir_process, file_name), '-c50',
                             '-V{0}/{1}.src.vcb.classes'.format(dir_process, file_name), 'opt'],
                             stderr=log)
        
        with open('{0}/mkcls1.tgt.log'.format(dir_log), 'w') as log:
            subprocess.call(['{0}/mkcls'.format(dir_binaries), '-m2',
                             '-p{0}/{1}.tgt'.format(dir_process, file_name), '-c50',
                             '-V{0}/{1}.tgt.vcb.classes'.format(dir_process, file_name), 'opt'],
                             stderr=log)
        
        with open('{0}/dictionary.log'.format(dir_log), 'w') as log:
            subprocess.call(['{0}/GIZA++'.format(dir_binaries),
                            '-S', '{0}/{1}.src.vcb'.format(dir_process, file_name),
                            '-T', '{0}/{1}.tgt.vcb'.format(dir_process, file_name),
                            '-C', '{0}/{1}.src_{1}.tgt.snt'.format(dir_process, file_name),
                            '-p0', '0.98',
                            '-o', '{0}/{1}-dictionary'.format(dir_dictionnary, file_name)],
                             stderr=log)
        
        self.widget.close()