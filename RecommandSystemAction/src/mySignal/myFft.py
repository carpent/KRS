'''
Created on May 14, 2017

@author: Kevin
'''
import numpy as np
from scipy import fft

class MyFft(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    
    def Fft(self):    
        a=np.zeros(10000)
        a[:100]=1
        b=fft(a)
        return b