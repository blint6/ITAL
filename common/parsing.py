'''
Created on 8 janv. 2012

@author: Nicolas Gasull
'''

from common.struct import *

class A3DictionnaryParser(object):
    '''
    classdocs
    '''

    def parse(self, dicFileName, dico = False):
        
        if not dico:
            dico = Dictionnary()
                
        with open('%s.A3.final' % dicFileName, 'r') as dicFile:
            labelLine = dicFile.readline()
            srcLine = dicFile.readline()
            tgtLine = dicFile.readline()
            
            # Tant qu'on n'atteint pas la fin du fichier
            while labelLine != '' and srcLine != '' and tgtLine != '':
                
                srcWords = srcLine.split(' ')
                tgtSplit = tgtLine.split(' ')
                tgtAlignedWords = []
                
                bracesMode = False # Whether we entered alignment braces
                
                for w in tgtSplit:
                    if w == '\n':
                        break
                    if bracesMode:
                        if w in ['({', '']:
                            continue
                        if w == '})':
                            bracesMode = False
                            continue
                        
                        # On a un numero d'alignement dans w. On l'ajoute au dernier mot
                        _, aligns = tgtAlignedWords[len(tgtAlignedWords) - 1]
                        aligns += [int(w) - 1]
                    else:
                        tgtAlignedWords += [(w, [])]
                        bracesMode = True
                
                
                tgtAlignedWords = tgtAlignedWords[1:] # On ne tient pas compte des valeurs NULL
                tgtAlignedExpressions = []
                i = 0
                while i < len(tgtAlignedWords):
                    w, aligns = tgtAlignedWords[i]
                    expression = Expression(w)
                    
                    # Par convention: pas d'alignement sur ce mot => compose avec les prochains
                    while i + 1 < len(tgtAlignedWords) and len(aligns) == 0:
                        i += 1
                        wNext, aligns = tgtAlignedWords[i]
                        expression += " %s" % wNext
                    
                    if len(aligns) != 0:
                        tgtAlignedExpressions += [(expression, aligns)]
                    
                    i += 1
                
                for e, aligns in tgtAlignedExpressions:
                    srcExpression = Expression()
                    
                    for a in aligns:
                        srcExpression += srcWords[a]
                    
                    dico.add(srcExpression, e)
                
                # Iterate to the next alignment
                labelLine = dicFile.readline()
                srcLine = dicFile.readline()
                tgtLine = dicFile.readline()
        
        return dico
        #