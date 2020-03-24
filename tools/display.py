import numpy as np
import matplotlib.pyplot as plt

class Display:
        
    def audio(self,data,title,timeInterval,maxAmp = 0,step = 1, figsize = (18, 4) ):
        xLabel = 'Time [s]'
        yLabel = 'Amplitude'
        N = len(data)
        time = np.linspace(timeInterval[0],timeInterval[1],N)
        plt.figure(figsize=figsize)
        plt.plot(time,data)
        plt.title(title)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.xticks(np.arange(timeInterval[0], timeInterval[1], step=step))
        if maxAmp > 0:
#             rearrange visible amplitude values
            plt.ylim((maxAmp, -maxAmp)) 

        
    def FFT(self,complexSpectra,Fs,xLabel,yLabel,title,figsize=(18, 4)):
        plt.figure(figsize=figsize)
        dataLength = len(complexSpectra)
        yData = abs(complexSpectra.real)
        xData = np.arange(0,dataLength)*Fs/dataLength

        halfIndex = np.floor(dataLength/2).astype(int) 

        plt.plot(xData[0:halfIndex], yData[0:halfIndex])
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.title(title)
        
    def spectra(self, complexSpectra,Fs,title, figsize=(18, 4)):
        xLabel = 'Frequency [Hz]'
        yLabel = 'Amplitude [Db]'
        self.FFT(complexSpectra,Fs,xLabel,yLabel,title,figsize=figsize)
        
    def specs(self, x, sr):

        # Show some specs
        print('Sample bits: ' + str(len(x)) + ' (bits)')
        print('Sampling rate: ' + str(sr) + ' (bits/second)')
        print('Duration: ' + str(len(x)/sr) + ' (seconds)')
    
        
disp = Display()