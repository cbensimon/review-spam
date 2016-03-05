# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:17:25 2016

@author: charles
"""

import numpy as np
from sklearn.svm import SVR
from sklearn.svm import SVC

class f1:
    
    def __init__(self, dim):
        self.coeffs = np.random.randn(1, dim)
        
    def compute(self, X):
        return X.dot(self.coeffs.T).reshape(X.shape[0])
        
    def computeC(self, X):
        result = np.zeros(X.shape[0])
        Y = self.compute(X)
        result[Y >= 0] = 1
        result[Y < 0] = -1
        return result

dim = 128

f1 = f1(dim)

nbTrain, nbTest = 10000, 100

xTrain = np.random.rand(nbTrain, dim)
xTest = np.random.rand(nbTest, dim)

#%%
yTrain = f1.compute(xTrain)
yTest = f1.compute(xTest)

svr = SVR()
print 'SVR'
print 'Learning...'
svr.fit(xTrain, yTrain)
print 'Scoring...'
print svr.score(xTest, yTest)

#%%
yTrain = f1.computeC(xTrain)
yTest = f1.computeC(xTest)

svc = SVC()
print 'SVC'
print 'Learning...'
svc.fit(xTrain, yTrain)
print 'Scoring...'
print svc.score(xTest, yTest)