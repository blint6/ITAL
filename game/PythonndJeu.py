'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui
from PySide import QtCore
import Tkinter as tk

class PythonndJeu(Ui_MainWindow):
    '''
    classdocss
    '''

    def __init__(self, dict, nbParties):
        '''
        Constructor
        '''
        self.dico = dict
        self.nbDevinettes = nbParties
        self.score = 0
        self.nbIndice = 0
        self.nbErreurs = 0
        self.nbParties = 0
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        self.reponse ="super"
        self.updateLabelPartie()
        
        self.setNewPhrase()        
        self.indiceButton.clicked.connect(self.callIndice)
        self.validerButton.clicked.connect(self.validate)
        self.passerButton.clicked.connect(self.passPartie)
        
        self.textEditEntry.textChanged.connect(self.emptyMessage)
        
        self.scoreLabel.setText("0")
        self.mainWindow.show()
        
        self.pal = QtGui.QPalette(QtGui.QColor(255,0,0));
        #pal.setColor( QPalette::Text, QColor(255,0,0) );
        #pal.setColor( QPalette::Foreground, QColor(255,0,0) );
    
    def reinit(self):
        self.nbIndice = 0
        self.nbErreurs = 0
    
    def updateLabelPartie(self):
        self.labelPartie.setText("Partie " + str(self.nbParties) + "/" + str(self.nbDevinettes))
        
    
    def emptyMessage(self):
        self.updateMessage(2)
    
    def callIndice(self):
        label = QtGui.QLabel("eopgerk")
        self.gridLayout.addWidget(label)
        self.nbIndice = self.nbIndice + 1
     
    def setNewPhrase(self):
        self.sentence = self.dico.getRandomSentence()
        self.phrase = str(self.sentence)
        self.phraseLabel.setText(self.phrase)
        self.nbParties = self.nbParties + 1
        self.updateLabelPartie()
        #set reponse
        
    def updateScore(self):
        self.score = self.score + 100 - self.nbIndice * 10 - self.nbErreurs - 10
        
    def updateScoreLabel(self):
        self.scoreLabel.setText(str(self.score))
        
    def updateMessage(self,code):
        if code == 0:
            self.labelMessage.set
            self.labelMessage.setText("Mauvaise reponse. Essaie encore !")
        elif code == 1:
            self.labelMessage.setText("Bonne reponse !! T'es trop fort !")
        elif code == 2:
            self.labelMessage.setText("")
    
    def validate(self):
        tentative = self.textEditEntry.toPlainText()
        if tentative == self.reponse:
            self.updateMessage(1)
            self.emptyMessage()
            #self.setNewPhrase("BIATCH")
        else:
            self.updateMessage(0)
            self.nbErreurs = self.nbErreurs + 1
            
    def passPartie(self):
        self.score = self.score - 50
        self.updateScoreLabel()
        
            
   
        
        
