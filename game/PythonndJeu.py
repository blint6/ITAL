'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui

class PythonndJeu(Ui_MainWindow):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        self.mainWindow.show()
        
        
