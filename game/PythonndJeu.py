'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui
from PySide import QtCore
from time import sleep

class PythonndJeu(Ui_MainWindow):
    '''
    classdocss
    '''

    def __init__(self, dictionnaire, nbParties):
        '''
        Constructor
        '''
        
        '''
        Parametres de score
        '''
        self.penaliteErreur = 5
        self.penaliteIndice = 5
        self.penalitePasser = 30
        
        self.dico = dictionnaire
        self.nbDevinettes = nbParties
        self.score = 0
        self.nbIndice = 0
        self.nbErreurs = 0
        self.nbParties = 0
        
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        self.setNewPhrase() 
        
        self.indiceButton.clicked.connect(self.callIndice)
        self.validerButton.clicked.connect(self.validate)
        self.passerButton.clicked.connect(self.passPartie)
        self.textEditEntry.textChanged.connect(self.emptyMessage)
        
        self.updateScoreLabel()
        self.mainWindow.show()
        self.updateLabelPartie()
        
    
    def reinit(self):
        self.nbIndice = 0
        self.nbErreurs = 0
        self.updateIndicesErrorsLabels()
    
    def updateIndicesErrorsLabels(self):
        self.errorsLabel.setText(str(self.nbErreurs))
        self.indicesNbLabel.setText(str(self.nbIndice))
    
    def updateLabelPartie(self):
        self.labelPartie.setText("Partie " + str(self.nbParties) + "/" + str(self.nbDevinettes))
    
    def emptyMessage(self):
        self.updateMessage(2)
    
    def callIndice(self):
        label = QtGui.QLabel("eopgerk")
        self.gridLayout.addWidget(label)
        self.nbIndice = self.nbIndice + 1
        self.updateIndicesErrorsLabels()
     
    def setNewPhrase(self):
        self.nbParties = self.nbParties + 1
        if(self.nbParties > self.nbDevinettes):
            #fin de la partie
            self.mainWindow.close()
        else:
            self.reinit()
            self.sentence = self.dico.getRandomSentence()
            self.reponse = self.sentence.removeRandomExpression().lower()
            print(self.reponse)
            self.phrase = unicode(self.sentence)
            self.phraseLabel.setText(self.phrase)        
            self.updateLabelPartie()
            
            #set reponse
        
    def updateScore(self):
        self.score = self.score + 100 - self.nbIndice * self.penaliteIndice - self.nbErreurs * self.penaliteErreur
        
    def updateScoreLabel(self):
        self.scoreLabel.setText(str(self.score))
        
    def updateMessage(self,code):
        if code == 0:
            self.labelMessage.setText("Mauvaise reponse. Essaie encore !")
            pal = QtGui.QPalette(QtGui.QColor(255,0,0));
            self.labelMessage.setPalette(pal)
        elif code == 1:
            self.labelMessage.setText("Bonne reponse !! T'es trop fort !")
        elif code == 2:
            self.labelMessage.setText("")
    
    def validate(self):
        tentative = self.textEditEntry.text()
        if tentative == self.reponse:
            self.updateMessage(1)
            self.updateScore()
            self.updateScoreLabel()
            self.setNewPhrase()
        else:
            self.updateMessage(0)
            self.nbErreurs = self.nbErreurs + 1
            self.updateIndicesErrorsLabels()
            
    def passPartie(self):
        self.score = self.score - self.penalitePasser
        self.updateScoreLabel()
        self.setNewPhrase()
        
            
   
        
        
