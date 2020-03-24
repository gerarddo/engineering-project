
import numpy as np 
import pandas as pd

class Cutter:
    def __init__(self, index):
        self.index = index
        
    def getMarks(self):
        return self.index['MARK'].to_numpy()
     
    # if Fs given, returns index tuples
    # if not, returns time tuples
    def getIntervals(self,Fs):
        tuples = []
        timeTuples = []
        marks = self.getMarks()
        
        for index in range(len(marks)-1):
            lowMark = marks[index]
            uppMark = marks[index+1]
            tuples.append(self.calculateInterval(lowMark,uppMark,Fs))
            timeTuples.append((lowMark,uppMark))
                              
        return (tuples, timeTuples)
    
    def stripe(self,data,index0,index1):
        extractedData = data[index0:index1]
        return extractedData
    
    def getInterval(self,s0,s1,Fs):
        i0 = self.timeToIndex(s0, Fs)
        i1 = self.timeToIndex(s1, Fs)
        return (i0,i1)   
    
    def timeToIndex(self,seconds, sr):
        return np.floor(sr*seconds).astype(int)
    
    def calculateInterval(self,s0,s1,Fs):
        i0 = self.timeToIndex(s0, Fs)
        i1 = self.timeToIndex(s1, Fs)
        return (i0,i1)
    
    def cutAll(self,data,Fs):
        marks = self.getMarks()
        intervals, timeIntervals = self.getIntervals(Fs)
        split = []
        for interval in intervals:
            cutoutData = self.stripe(data,interval[0],interval[1])
            split.append(cutoutData)
        return (split, intervals, timeIntervals)