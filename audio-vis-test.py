# https://jfraj.github.io/2015/06/17/recording_audio.html
import pyaudio
import numpy as np
import pylab
import time

p = pyaudio.PyAudio()

p.get_default_input_device_info()

FRAMES_PERBUFF = 4096 # number of frames per buffer
FORMAT = pyaudio.paInt16 # 16 bit int
CHANNELS = 1 # I guess this is for mono sounds
FRAME_RATE = 22050 # sample rate

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=FRAME_RATE,
                input=True,
                frames_per_buffer=FRAMES_PERBUFF) #buffer

frames = []


RECORD_SECONDS = 120
nchunks = int(RECORD_SECONDS * FRAME_RATE / FRAMES_PERBUFF)

def soundplot(stream):
    t1=time.time()
    data = np.fromstring(stream.read(FRAMES_PERBUFF),dtype=np.int16)
    pylab.plot(data)
    pylab.title(i)
    pylab.grid()
    pylab.axis([0,len(data),-2**16/2,2**16/2])
    pylab.savefig("03.png",dpi=50)
    pylab.close('all')
    print("took %.02f ms"%((time.time()-t1)*1000))

for i in range(0, nchunks):
#     data = stream.read(FRAMES_PERBUFF)
    data = np.fromstring(stream.read(FRAMES_PERBUFF),dtype=np.int16)
    frames.append(data) # 2 bytes(16 bits) per channel
    soundplot(stream)
print("* done recording")
stream.stop_stream()
stream.close()
p.terminate()
