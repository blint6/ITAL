'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui
from PySide import QtCore

class PythonndJeu(Ui_MainWindow):
    '''
    classdocss
    '''

    def __init__(self, dict):
        '''
        Constructor
        '''
        self.dico = dict
        self.score = 0
        self.nbIndice = 0
        self.nbErreurs = 0
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        self.reponse ="super"
        
        self.indiceButton.clicked.connect(self.callIndice)
        self.validerButton.clicked.connect(self.validate)
        
        self.mainWindow.setWindowTitle("PythonndJeu")
        self.scoreLabel.setText("0")
        self.mainWindow.show()
    
    #def reinit(self):
        
    
    def callIndice(self):
        label = QtGui.QLabel("eopgerk")
        self.gridLayout.addWidget(label)
        self.nbIndice = self.nbIndice + 1
     
    #def validate(self):
    
    def setNewPhrase(self, phrase):
        self.phraseLabel.setText(phrase)
        
    def updateScore(self,mod):
        self.score = self.score + mod
        self.scoreLabel.setText(str(self.score))
        
    def updateMessage(self,code):
        if code == 0:
            self.labelMessage.setText("Mauvaise reponse. Essaie encore !")
        elif code ==1:
            self.labelMessage.setText("Bonne reponse !! T'es trop fort !")
    
    def validate(self):
        tentative = self.textEditEntry.toPlainText()
        if tentative == self.reponse:
            self.updateMessage(1)
            self.setNewPhrase("BIATCH")
        else:
            self.updateMessage(0)
            self.nbErreurs = self.nbErreurs + 1
            
   
        
        
