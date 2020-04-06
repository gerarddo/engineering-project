class Explorer:
    
    def __init__(self, split, intervals, periods, index):
        self.split = split
        self.intervals = intervals
        self.periods = periods
        self.index = index
        
    def data(self,key,normalize=False):
        idx = self.getIndex(key)
        data = self.split[idx]
        if normalize:
            maxAmp = max(data.min(), data.max(), key=abs)
            data = data*(1/maxAmp)
        return data, self.intervals[idx], self.periods[idx], self.title(key)
    
    def title(self,key):
        idx = self.getIndex(key)
        return self.index['LABEL'].to_numpy()[idx]
        
    def getIndex(self,key):
        return self.index.index[self.index['KEY'] == key][0]
    
#     def split(self,key):
#         return self.split[idx],self.title(key)