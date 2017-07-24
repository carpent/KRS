'''
Created on May 14, 2017

@author: Kevin
'''

import matplotlib.pyplot as plt
import numpy as np
from myFft import MyFft
from matTrims import MatTrims
from matplotlib.pyplot import axis
from numpy import int32
from simCos import SimCosine
import time
from scoreMatsFromMovieLens import ScoreMatsFromMoiveLens
from mySignal.recommendAsset import RecommendAsset

if __name__ == '__main__':
    
    timeStart = time.time()
#     testMat = np.loadtxt('F:/00 EclipseWorkSpace/myPythonML/ml-100k/u1.base',dtype=int32)
#     testMat = np.delete(testMat, 3, 1)
#     maxUsers = testMat[:,0].max()
#     maxMovies = testMat[:,1].max()
#     (maxRows,maxCols)=np.shape(testMat)
#     scoreMat = np.zeros((maxUsers,maxMovies))
# #     simMatbyMovies = np.zeros(maxMovies,maxMovies)
#     for i in range(0,maxRows):
#         scoreMat[testMat[i,0]-1,testMat[i,1]-1]=testMat[i,2]
#
    scoreObj = ScoreMatsFromMoiveLens()
    scoreMat = scoreObj.GetScoreMats('F:/00 EclipseWorkSpace/myPythonML/ml-100k/u1.test')
     
    timeTemp = time.time()  
       
    simObj = SimCosine()
    simMat = simObj.SimCos(scoreMat)
 
#     print(simMat)
    timeStop = time.time()
    
#     
#     scoreMat = np.array([[1,2,1,3],[0,3,1,0],[2,1,4,1]])
#     simMat = np.array([[0,0.2,0.1,0.3],[0.3,0,0.1,0],[0.2,0.1,0,0.1],[0.2,0.3,0.1,0]])
#     scoreMat = scoreObj.GetScoreMats('F:/00 EclipseWorkSpace/myPythonML/ml-100k/u1.base')
    recomObj = RecommendAsset()
#     recomObj.PredictScore(simMat, scoreMat, 10) 
    mae = recomObj.RecomAsset(scoreMat, recomObj.PredictScore(simMat, scoreMat, 2))
    print(mae)
    
    print(timeStart, timeTemp, timeStop, timeStop-timeStart, time.time()-timeStart)
#     myMattemp = np.hstack((srcMat[:,0].reshape((maxRows,1)), srcMat[:,1].reshape((maxRows,1))))
#     myMattemp = np.hstack((myMat[:,0].reshape((m,1)), myMat[:,1].reshape((m,1))))
#     print myMattemp
#     myTrim = MatTrims()
#     myNewMat=myTrim.RowTrims(myMattemp)
#     print(myMat)
#     print myNewMat
#     print(np.delete(myMat, 0, 0))