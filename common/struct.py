'''
Created on 7 janv. 2012

@author: Nicolas Gasull
'''

import random



class Player(object):
    
    def __init__(self):
        self.dicFile = None
        self.gameCount = 0
        self.hiScore = 0
        self.name = u'nouveau'
        self.points = 0
        #
    
    def score(self, score):
        self.gameCount += 1
        self.points += score
        
        if score > self.hiScore:
            self.hiScore = score
        #


class Dictionnary(object):
    '''
    synonyms : Liste d'expressions couplees a une liste de couples (synonyme, score)
    '''
    
    def __init__(self):
        self.sentences = []
        self.synonyms = {}
        #
    
    def add(self, word, synonym, scoreCoeff = 1, reverse = True):
        
        if word.isExcluded() or synonym.isExcluded() or word == synonym:
            return
        
        word_s = unicode(word)
        synonym_s = unicode(synonym)
        
        if word_s in self.synonyms:
            l = self.synonyms[word_s]
        else:
            l = {}

        if synonym_s in l:
            occ = l[synonym_s]
            occ += scoreCoeff
        else:
            occ = scoreCoeff
            
        l[synonym_s] = occ
        
        self.synonyms[word_s] = l
        
        if reverse:
            self.add(synonym, word, scoreCoeff, False)
        #
    
    def addSentence(self, sentence):
        self.sentences += [sentence]
        #
        
    def wordSynonyms(self, word):
        
        if not self.synonyms.has_key(word):
            return []

        return self.synonyms[word].keys()
        #
    
    def getRandomSentence(self):
        if len(self.sentences) <= 0:
            return None
        else:
            return random.choice(self.sentences)
        #
    
    def empty(self):
        return not len(self.synonyms) > 0 or not len(self.sentences) > 0
        #
    
    def __str__(self):
        ret = u''
        
        for expr, l in self.synonyms.items():
            ret += u'%s :' % expr
            
            for syn, occur in l.items():
                ret += u' %s (%d),' % (syn, occur)
                
            ret += u'\n'
            
        return ret
        #
            


class Sentence(object):
    
    def __init__(self, *expressions):
        self.expressions = []
        for e in expressions:
            self += e
        #
    
    def getRandomExpression(self):
        if len(self.expressions) <= 0:
            return None
        else:
            return random.choice(self.expressions)
        #
        
    def removeRandomExpression(self):
        expressionsCount = len(self.expressions)
        if expressionsCount <= 0:
            return None
        
        expression = None
        while expression == None or expression.isExcluded():
            i = random.randrange(0, expressionsCount - 1)
            expression = self.expressions[i]
        
        expressionStr = unicode(expression)
        expression.hide()
        return expressionStr
        #
            
    def __iadd__(self, expression):
        self.expressions += [expression]
        return self
        #
        
    def __str__(self):
        
        words = []
        for e in self.expressions:
            words += [unicode(e)]
        
        return u'%s.' % u' '.join(words)
        #
    
    
        
class Expression(object):
    '''
    words : Liste les mots de l'expression
    '''
    
    def __init__(self, *words):
        
        self.words = []
        for m in words:
            self += m
        #

    def isExcluded(self):
        return len(self.words) == 1 and self.words[0].lower() in [u'de', u'au', u'le', u'la', u'les', u'et', u'se', u'sa', u'ses', u'pour', u'un', u'une', u'dans']
        #
    
    def hide(self):
        for i in range(len(self.words)):
            self.words[i] = u'xxxx'
        #
        
    # +=
    def __iadd__(self, w):
        
        # On enleve l'eventuelle ponctuation
        if w[len(w) - 1] in [u',', u'.', u'!', u'?', u':', u';']:
            w = w[:len(w) - 1]
        
        # On retire les espaces a gauche et a droite
        w = w.strip()
        
        # On n'ajoute le mot que si on n'a pas tout rogne
        if(len(w) > 0):
            self.words += [w]
        
        return self
        #
        
    def __eq__(self, expr):
        return unicode(self) == unicode(expr)
        #
    
    def __str__(self):
        return ' '.join(self.words)
        #
