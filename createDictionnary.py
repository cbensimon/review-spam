# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 12:23:12 2016

@author: 3000120
"""

from tools import *

data = pkl.load(open('Data/movies_150k.pkl'))
print 'Data loaded'

F = lil_matrix((1, 128**3)).astype(np.uint32)
cpt = 0
N = len(data)

for i in range(len(data)):
    
    review = data[i]
    
    if i%(N/100) == 0:
        print str((100*i)/N) + ' %'
    
    rText = review['reviewText']
    rId = review['reviewerID']
    r3G = string2trigram(rText)
        
    F = F + r3G
    
F = F.toarray()

f = open('Dumped/globalTrigram.pkl', 'wb')
pkl.dump(F, f)

low = 5
high = F.max()

result = (F >= low) * (F <= high)

f = open('Dumped/dict.pkl', 'wb')
pkl.dump(result, f)
f.close()
