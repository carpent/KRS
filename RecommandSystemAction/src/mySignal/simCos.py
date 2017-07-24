'''
Created on May 23, 2017

@author: Kevin
'''
import numpy as np
from matTrims import MatTrims

class SimCosine(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    def SimCosbyItems(self, mats, i, j):
        (maxUsers,maxMovies) = np.shape(mats)
#         simUser = np.zeros(maxRows)
        sim1=sim2=sim3=0
#         myMattemp = np.hstack((Mats[:,i].reshape((maxRows,1)), Mats[:,j].reshape((maxRows,1))))
        for userId in range(0, maxUsers):
            if mats[userId,i] >= 1 and mats[userId,j] >= 1:
                sim1 += mats[userId,i] * mats[userId,j]
                sim2 += mats[userId,i]**2
                sim3 += mats[userId,j]**2
                
        if sim2 == 0 or sim3 == 0:
            return 0
        else:
            return sim1/np.sqrt(sim2*sim3)

    def SimCos(self,mats):
        (maxUsers,maxMovies) = np.shape(mats)
        simMats = np.zeros((maxMovies,maxMovies))
        for i1 in range(0, maxMovies-1):
            for i2 in range(i1+1, maxMovies):
                simMats[i1,i2] = self.SimCosbyItems(mats, i1, i2)
                
        simMats[simMats>=0.99999]=0
        simMats = np.transpose(simMats) + simMats   
        return simMats