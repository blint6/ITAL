'''
Created on 7 janv. 2012

@author: Nicolas Gasull
'''

class Dictionnary(object):
    '''
    synonyms : Liste d'expressions couplees a une liste de couples (synonyme, score)
    '''
    
    def __init__(self):
        self.synonyms = {}
        #
    
    def add(self, word, synonym, scoreCoeff = 1, reverse = True):
        
        if word.isExcluded() or synonym.isExcluded() or word == synonym:
            return
        
        word_s = str(word)
        synonym_s = str(synonym)
        
        if word_s in self.synonyms:
            l = self.synonyms[word_s]
        else:
            l = {}

        if synonym_s in l:
            occ, score = l[synonym_s]
            occ += 1
            scoreCoeff += score
        else:
            occ = 1
            
        l[synonym_s] = occ, scoreCoeff
        
        self.synonyms[word_s] = l
        
        if reverse:
            self.add(synonym, word, scoreCoeff, False)
        #
        
    def wordSynonyms(self, word):
        
        if not self.synonyms.has_key(word):
            return []

        return self.synonyms.keys()
        #
            
    def __str__(self):
        ret = ''
        
        for expr, l in self.synonyms.items():
            ret += '%s :' % expr
            
            for syn, (occur, _) in l.items():
                ret += ' %s (%d),' % (syn, occur)
                
            ret += '\n'
            
        return ret
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
        return len(self.words) == 1 and str.lower(self.words[0]) in ['de', 'au', 'le', 'la', 'les', 'et', 'se', 'sa', 'ses', 'pour', 'un', 'une', 'dans']
    
    # +=
    def __iadd__(self, w):
        
        # On enleve l'eventuelle ponctuation
        if w[len(w) - 1] in [',', '.', '!', '?', ':', ';']:
            w = w[:len(w) - 1]
             
        self.words += [w]
        return self
        #
        
    def __eq__(self, expr):
        return str(self) == str(expr)
    
    def __str__(self):
        return ' '.join(self.words)
        #
