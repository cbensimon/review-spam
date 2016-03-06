# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:41:51 2016

@author: charles
"""

from threading import Thread as Th
from multiprocessing import cpu_count
import numpy as np

nCores = cpu_count()

class Thread(Th):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Th.__init__(self, group, target, name, args, kwargs, Verbose)
        self._return = None
    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args,
                                                **self._Thread__kwargs)
    def join(self):
        Th.join(self)
        return self._return
        
def asyncQueue(f, args):
    args = np.array(args)
    nArgs = args.shape[0]
    split = nArgs - nArgs%nCores
    
    argsToSplit = args[:split]
    remainingArgs = args[split:]
    
    argsArray = np.split(argsToSplit, nCores)
    
    T = []
    for i in range(nCores):
        t = Thread(target=f, args=(argsArray[i],))
        t.start()
        T.append(t)
        
    R = []
    for t in T:
        R.append(t.join())
        
    if remainingArgs.shape[0] > 0:
        R.append(f(remainingArgs))
        
    return R
    