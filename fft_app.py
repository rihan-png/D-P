import numpy as np
import matplotlib.pyplot as plt
fs=1000
t=np.arange(0,1,1/fs)
x=np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)+0.5*np.sin(2*np.pi*200*t)
N=len(x)
xk= np.fft.fft(x)
freq_val=np.fft.fftfreq(N,d=1/fs)
plt.plot(t,x)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.title('signal')
plt.figure(figsize=(10,6))
plt.plot(freq_val[freq_val >= 0], np.abs(xk[freq_val >= 0]))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency Spectrum')
plt.grid(True)
plt.show()
