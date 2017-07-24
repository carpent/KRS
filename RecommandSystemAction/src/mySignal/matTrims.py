'''
Created on May 22, 2017

@author: Kevin
'''
import numpy as np

class MatTrims(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def RowTrims(self, Mats):
        temp = Mats
        (m,n) = np.shape(Mats)
        for row in range(0,m)[::-1]:
            if np.abs(np.multiply.reduce(Mats[row,:]))<0.1:
                temp=np.delete(temp, row, 0)
        return temp;
    
    def ColTrims(self, Mats):
        temp = Mats
        (m,n) = np.shape(Mats)
        for col in range(0,n)[::-1]:
            if np.abs(np.multiply.reduce(Mats[:,col]))<0.1:
                temp=np.delete(temp, col, 1)
        return temp;