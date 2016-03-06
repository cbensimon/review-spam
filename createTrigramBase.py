# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:59:58 2016

@author: charles
"""

from tools import *

data = pkl.load(open('Data/movies_150k.pkl'))
print 'Data loaded'

def createArrays(data):
    
    N = len(data)
    X = []
    Y = []
    
    for i in range(N):
    
        review = data[i]
        
        print i
        
        if i%(N/100) == 0:
            print str((100*i)/N) + ' %'
        
        rText = review['reviewText']
        rId = review['reviewerID']
        r3G = string2trigram(rText)
        
        X.append(r3G)           
        Y.append(rId)
        
    return (X, Y)
    

def reduceToMatrix(array):
    
    print 'r2m'
    
    n = len(array)
    if n == 1:
        return array[0]
        
    if n%2 == 0:
        rg = range(0, n, 2)
    else:
        rg = range(0, n-1, 2)
    
    R = []
    for i in rg:
        R.append(vstack([array[i], array[i+1]]))
    
    if not n%2 == 0:
        R.append(array[-1])
        
    return reduceToMatrix(R)
    
(X, Y) = createArrays(data)
X = reduceToMatrix(X)
    
f = gzip.open('Data/reviews_trigrams.pklz', 'wb')
pkl.dump((X, Y), f)
f.close()