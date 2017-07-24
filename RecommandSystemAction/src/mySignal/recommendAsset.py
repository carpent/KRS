'''
Created on June 11, 2017

@author: Kevins
'''
import numpy as np

class RecommendAsset(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def PredictScore(self, simMats, scoreMats, neighbors):  
        (maxUsers,maxMovies) = np.shape(scoreMats)  
        avarageScore=np.mean(scoreMats, 1)
#         print(avarageScore)
        knnNeighbor = np.argsort(-(simMats), 1)
#         print(knnNeighbor)
        predictScore = np.zeros((maxUsers,maxMovies))
        sum1,sum2 = 0,0
        for i in range(0, maxUsers):
            for j in range(0, maxMovies): 
                for k in range(0, neighbors):
                    if scoreMats[i,knnNeighbor[j, k]] != 0 :
                        sum1 = sum1 + simMats[j,knnNeighbor[j, k]]*(scoreMats[i,knnNeighbor[j, k]]-avarageScore[i])
                        sum2 = sum2 + simMats[j,knnNeighbor[j, k]]
                        
                if sum2 == 0:
                    predictScore[i, j] = np.round(avarageScore[i])
                else:
                    predictScore[i, j] = np.round(sum1/sum2 + avarageScore[i])
#         print (predictScore)            
        return predictScore
    
    def RecomAsset(self, scoreMats, predictMats):  
        (maxUsers,maxMovies) = np.shape(scoreMats)
        mae = np.sum(np.abs(np.subtract(scoreMats,predictMats)))/(maxUsers*maxMovies)
        return mae