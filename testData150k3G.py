# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:23:12 2016

@author: 3000120
"""

from tools import *

data = pkl.load(open('movies_150k.pkl'))
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
        F[rId] = csr_matrix((1, 128**3)).astype(np.uint32)
        
    F[rId] = F[rId] + r3G

f = gzip.open('trigramCounts.pklz', 'wb')    
pkl.dump(F, f)
f.close()