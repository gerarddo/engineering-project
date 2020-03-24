# 
# import numpy as np
from tools.pathbuilder import PathBuilder
import pandas as pd
import librosa
path = PathBuilder()

class Load:  

    def __init__(self, pathToIndex = ['..','data','processed','index.csv'], delimiter=','):
        index = pd.read_csv(path.build(pathToIndex))
        self.path = path.build(pathToIndex[0:-1])
        self.index = index
        self.cache = {}
    
    def audio(self, key, visual = False):
        row = self.index[self.index['KEY'] == key]
        ID = row['ID'].iloc[0]
        KEY = row['KEY'].iloc[0]
        loaded = self.isLoaded(KEY)
        if loaded:
            print('Retrieving ' + key + ' from cache')
            data = self.cache[KEY]
        else:
            audioPath = self.path + '/' + ID 
            print('Loading ' + audioPath)
            data = librosa.load(audioPath)
            self.toCache(KEY, data)        
    
        if visual:
            print(data)
            
        return data
    
    def getID(self,KEY):
        if KEY in self.getKEYs():
            return self.index[self.index['KEY'] == KEY]['ID'].iloc[0]
        
    def getKEY(self,ID):
        if ID in self.getIDs():
            return self.index[self.index['ID'] == ID]['KEY'].iloc[0]
        
    def getIDs(self):
        return self.index['ID'].array
    
    def getKEYs(self):
        return self.index['KEY'].array

    def cacheKEYs(self):
        return self.cache.keys()
        
    def isLoaded(self,key):
        if key in self.cacheKEYs():
            return True
        else:
            return False
        
    def toCache(self,key,data):
        self.cache[key] = data

    def cutConfig(self,key):
        path = self.path + '/' + key + '.cutconfig.csv'
        print(path)
        config = pd.read_csv(path)
        return config
        
load = Load(['data','original','index.csv'])
        
