# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:59:58 2016

@author: charles
"""

from tools import *

data = pkl.load(open('Data/movies_150k.pkl'))
print 'Data loaded'

F = {}
cpt = 0
N = len(data)

for review in data:
    
    if cpt%(N/100) == 0:
        print str((100*cpt)/N) + ' %'
        
    cpt += 1
    
    rText = review['reviewText']
    rId = review['reviewerID']
    r3G = string2trigram(rText)
    
    if not F.has_key(rId):
        F[rId] = []
        
    F[rId].append(r3G)

f = gzip.open('Data/reviews_trigrams.pklz', 'wb')
pkl.dump(F, f)
f.close()