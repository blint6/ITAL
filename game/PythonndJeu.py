'''
Created on 8 janv. 2012

@author: Komo
'''
from game.PythonndJeuUi import Ui_MainWindow
from PySide import QtGui

class PythonndJeu(Ui_MainWindow):
    '''
    classdocss
    '''

    def __init__(self, pythonndITAL, dictionnaire, nbParties):
        '''
        Constructor
        '''
        
        '''
        Parametres de score
        '''
        self.penaliteErreur = 5
        self.penaliteIndice = 5
        self.penalitePasser = 30
        
        self.pythonndITAL = pythonndITAL
        self.dico = dictionnaire
        self.nbDevinettes = nbParties
        self.score = 0
        self.nbIndice = 0
        self.nbErreurs = 0
        self.nbParties = 0
        
        self.indiceWidgets = []
        
        self.mainWindow = QtGui.QMainWindow()
        self.setupUi(self.mainWindow)
        self.setNewPhrase() 
        
        self.indiceButton.clicked.connect(self.callIndice)
        self.textEditEntry.returnPressed.connect(self.validate)
        self.validerButton.clicked.connect(self.validate)
        self.passerButton.clicked.connect(self.passPartie)
        self.textEditEntry.textChanged.connect(self.emptyMessage)
        
        self.updateScoreLabel()
        self.mainWindow.show()
        self.updateLabelPartie()
        
    
    def reinit(self):
        self.nbIndice = 0
        self.nbErreurs = 0
        
        for i in self.indiceWidgets[:]:
            i.hide()
            self.gridLayout.removeWidget(i)
            self.indiceWidgets.remove(i)
            del i
        
        self.updateIndicesErrorsLabels()
        self.updateMessage(2)
        self.textEditEntry.setText(u'')
    
    def updateIndicesErrorsLabels(self):
        self.errorsLabel.setText(str(self.nbErreurs))
        self.indicesNbLabel.setText(str(self.nbIndice))
    
    def updateLabelPartie(self):
        self.labelPartie.setText("Partie " + str(self.nbParties) + "/" + str(self.nbDevinettes))
    
    def emptyMessage(self):
        self.updateMessage(2)
    
    
    def callIndice(self):
        if len(self.synonyms) > 0:
            label = QtGui.QLabel(self.synonyms[0])
            del self.synonyms[0]
            
            self.indiceWidgets += [label]
            self.gridLayout.addWidget(label)
            self.nbIndice = self.nbIndice + 1
            self.updateIndicesErrorsLabels()
        else:
            self.statusbar.showMessage("Plus d'indices disponibles !")
        
        
    def setNewPhrase(self):
        self.nbParties = self.nbParties + 1
        if(self.nbParties > self.nbDevinettes):
            #fin de la partie
            self.pythonndITAL.finalizeJeu()
            self.mainWindow.close()
        else:
            self.reinit()
            self.sentence = self.dico.getRandomSentence()
            self.reponse = self.sentence.removeRandomExpression()
            self.synonyms = self.dico.wordSynonyms(self.reponse)
            self.phraseLabel.setText(unicode(self.sentence))        
            self.updateLabelPartie()
            
            print(self.reponse)
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
            self.labelMessage.setText("Seriez-vous a la hauteur..?")
    
    
    def validate(self):
        tentative = self.textEditEntry.text()
        if tentative.lower() == self.reponse.lower():
            self.updateMessage(1)
            self.updateScore()
            self.updateScoreLabel()
            self.setNewPhrase()
        else:
            self.textEditEntry.setText(u'')
            self.updateMessage(0)
            self.nbErreurs = self.nbErreurs + 1
            self.updateIndicesErrorsLabels()
            
        
    def passPartie(self):
        self.score = self.score - self.penalitePasser
        self.updateScoreLabel()
        self.setNewPhrase()
        
            
   
        
        
