'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui
from PySide import QtCore

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
        
        self.indiceButton.clicked.connect(self.callIndice)
        
        self.mainWindow.setWindowTitle("HEY BITCH")
        self.scoreLabel.setText("FUCK")
        self.mainWindow.show()
    
    def callIndice(self):
        self.scoreLabel.setText("FUCKER")
        label = QtGui.QLabel("eopgerk")
        self.verticalLayout.addWidget(label)
    '''     
    def validate(self):
        if self.textEditEntry.
    
    #def callPass(self):
    '''  
        
        
