# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:59:58 2016

@author: charles
"""

from tools import *

data = pkl.load(open('Data/movies_150k.pkl'))
print 'Data loaded'

N = len(data)
X = None
Y = []

for i in range(200):
    
    review = data[i]
    
    print i
    
    if i%(N/100) == 0:
        print str((100*i)/N) + ' %'
    
    rText = review['reviewText']
    rId = review['reviewerID']
    r3G = string2trigram(rText)
    
    if X == None:
        X = r3G
    else:
        X = vstack([X, r3G])
        
    Y.append(rId)
    
    
f = gzip.open('Data/reviews_trigrams.pklz', 'wb')
pkl.dump((X, Y), f)
f.close()