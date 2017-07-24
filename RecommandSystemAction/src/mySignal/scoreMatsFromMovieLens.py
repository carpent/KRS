'''
Created on June 11, 2017

@author: Kevins
'''

import numpy as np

class ScoreMatsFromMoiveLens(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def GetScoreMats(self, datafile):    
        testMat = np.loadtxt(datafile,dtype=np.uint32)
        testMat = np.delete(testMat, 3, 1)
        maxUsers = testMat[:,0].max()
        maxMovies = testMat[:,1].max()
        (maxRows,maxCols)=np.shape(testMat)
        scoreMat = np.zeros((maxUsers,maxMovies))
    #     simMatbyMovies = np.zeros(maxMovies,maxMovies)
        for i in range(0, maxRows):
            scoreMat[testMat[i,0]-1,testMat[i,1]-1]=testMat[i,2]
        
        return scoreMat