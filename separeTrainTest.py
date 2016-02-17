# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:43:43 2016

@author: charles
"""

from tools import *

def separeTrainTest(data, tau):
    
    Xtrain, Xtest = [], []
    Ytrain, Ytest = [], []
    for key in data:
        rId = key
        rMatrix = data[rId]
        size = len(rMatrix)
        np.random.shuffle(rMatrix)
        
        tIndex = round(size * tau)
        Xtrain.append(rMatrix[:tIndex])
        Xtest.append(rMatrix[tIndex:])
        
        Ylabel[rId]*len
        Ytrain.append(Ylabel[:tIndex])
        Ytest.append(Ylabel[tIndex:])
    
    return Xtrain, Ytrain, Xtest, Ytest