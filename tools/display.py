import numpy as np
import matplotlib.pyplot as plt

class Display:
        
    def audio(
        self,
        data,
        Fs,
        title="Audio",
        maxAmp = 0,
        ticks = 20, 
        figsize = (18, 4)
    ):
        
        
        t0 = 0
        xLabel = 'Time [s]'
        yLabel = 'Amplitude'
        N = len(data)
        duration = (1/Fs)*N
        time = np.linspace(t0,duration,N)
        
        # calculate shown second marks
        step = (duration - t0)/ticks
            
        plt.figure(figsize=figsize)
        plt.plot(time,data)
        plt.title(title)
        plt.ylabel(yLabel)
        plt.xlabel(xLabel)
        plt.xticks(np.arange(t0, duration, step=step))
        
        if maxAmp > 0:
            plt.ylim((maxAmp, -maxAmp)) 
    




        
    def FFT(
        self,
        complexSpectra,
        Fs,
        title="Fourier Transform",
        xLabel = 'Frequency [Hz]',
        yLabel = 'Amplitude',
        step=1000,
        figsize=(18, 4),
        fmin=0, 
        fmax=0,
        maxAmp=0,
        normalize=False
    ):
        
        plt.figure(figsize=figsize)
        domainLength = len(complexSpectra)
        yData = abs(complexSpectra.real)
        xData = np.arange(0,domainLength)*Fs/domainLength

        startIndex = 0
        reachIndex = np.floor(domainLength/2).astype(int) 
        
        if fmax > 0:
            reachIndex = len(xData[xData <= fmax])
#             plt.text(
#                 xData[reachIndex]*0.84, 
#                 300, 
#                 'Max frequency shown: ' + str(np.round(xData[reachIndex], decimals=2)) + ' [Hz]'
#             )
        
        if fmin > 0:
            startIndex = len(xData[xData <= fmin])
#             plt.text(
#                 xData[reachIndex]*0.84, 
#                 400, 
#                 'Min frequency shown: ' + str(np.round(xData[startIndex], decimals=2)) + ' [Hz]'
#             )

        # calculate shift 
        if fmin > 0:
            remainder = step % fmin
            if remainder > 0:
                fmin = fmin + remainder

        
        if normalize:
            print('normalizing')
            norm1 = yData / np.linalg.norm(yData)
            yData = norm1
#             yData = yData/yData.max()
            
        plt.plot(xData[startIndex:reachIndex], yData[startIndex:reachIndex])
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.xticks(np.arange(fmin, xData[reachIndex], step=step))
        plt.title(title)
        
#         if maxAmp > 0:
#             print('maxamp higher than zero alright')
#             plt.ylim((0, maxAmp)) 
        
    def spectra(self,complexSpectra,Fs,title,step=1000,fmin=0, fmax=0, figsize=(18, 4),maxAmp=0,
        normalize = False):
        xLabel = 'Frequency [Hz]'
        yLabel = 'Amplitude'
        
        self.FFT(complexSpectra,Fs,title,xLabel,yLabel,step,figsize=figsize,fmin=fmin,fmax=fmax,maxAmp=maxAmp,normalize=normalize)
        
        
    def specs(self, x, sr):

        # Show some specs
        print('Sample bits: ' + str(len(x)) + ' (bits)')
        print('Sampling rate: ' + str(sr) + ' (bits/second)')
        print('Duration: ' + str(len(x)/sr) + ' (seconds)')

#         plt.
(
#             20, 
#             200, 
#             'Sample bits: ' + str(len(x)) + ' (bits)'
#         )
#         plt.text(
#             20, 
#             300, 
#             'Sampling rate: ' + str(sr) + ' (bits/second)'
#         )
#         plt.text(
#             20, 
#             400, 
#             'Duration: ' + str(len(x)/sr) + ' (seconds)'
#         )
        
        
        
# # these are matplotlib.patch.Patch properties
# props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# # place a text box in upper left in axes coords
# ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
#         verticalalignment='top', bbox=props)
    
        
# disp = Display()