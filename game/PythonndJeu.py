'''
Created on 8 janv. 2012

@author: Komo
'''
from PythonndJeuUi import Ui_MainWindow
from PySide import QtCore, QtGui

class PythonndJeu(Ui_MainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.mainWindow = QtGui.QMainWindow()
        #self.setupUi(self.mainWindow)
        
        
    def show(self):
        self.mainWindow.show()
        
