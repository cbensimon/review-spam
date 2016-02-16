# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:37:44 2016

@author: 3000120
"""

from tools import *

data = pkl.load(open('Data/movies_150k.pkl'))
print 'Data loaded'

F = pkl.load(gzip.open('Dumped/trigramCounts.pklz', 'r'))
print 'Trigrams loaded'

for rId in F.keys():
    F[rId] = F[rId] / float(F[rId].sum())
    
print 'normalized'
    
scores = []

#for review in data:
#    rText = review['reviewText']
#    r3G = string2trigram(rText)
#    r3G = r3G / float(r3G.sum())
#    
#    _, predIds = zip(*sorted([(((F[i] - r3G) * (F[i] - r3G).transpose())[0,0], i) for i in F.keys()]))
#    
#    rId = review['reviewerID']
#        
#    scores.append(predIds.index(rId))
#    print scores[-1]


import random

randomData = range(len(data))
random.shuffle(randomData)
for i in range(1000):
    index = randomData[i]
    review = data[index]
    rText = review['reviewText']
    r3G = string2trigram(rText)
    r3G = r3G / float(r3G.sum())
    
    _, predIds = zip(*sorted([(squareSum(F[i] - r3G), i) for i in F.keys()]))
    
    rId = review['reviewerID']
        
    scores.append(predIds.index(rId))
    print scores[-1]
    
scores = np.array(scores)

print (scores == 0).mean()
print (scores <= 1).mean()
print (scores <= 2).mean()
print (scores <= 3).mean()
print (scores <= 4).mean()
    
print np.mean(scores)