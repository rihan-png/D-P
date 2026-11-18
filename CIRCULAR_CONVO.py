import numpy as np
import matplotlib.pyplot as plt
#define input sequence 
x1=[1,2]
x2=[1,2,3,4]
#determine the length of  the  sequence and and maximum length(N)
N=max(len(x1),len(x2))
#zero-pad both sequences to make them of equal  length N for circular concolution
x1.extend([0]*(N-len(x1)))
x2.extend([0]*(N-len(x2)))
#compute the circular convolution using numpy's fft function
x1k = np.fft.fft(x1)
x2k = np.fft.fft(x2)
#perform circular convolution in the time domain by multiplying the FFTs
#and  taking the inverse FFT,the n extraction only the real part
yn=np.real(np.fft.ifft(x1k*x2k))
#create a figure  to plot the sequence and  their convolution result
plt.figure(figsize=(10,8))
#plot the first input sequence
plt.subplot(3,1,1)
plt.stem(np.arange(len(x1)),x1)
plt.title("first sequence")
#plot the second input sequence
plt.subplot(3,1,2)
plt.stem(np.arange(len(x2)),x2)
plt.title("second sequence")
#plot the circular convolution result
plt.subplot(3,1,3)
plt.stem(np.arange(len(yn)),yn)
plt.title("circular convolution result")
#print the input sequence and the convolution result to console first
print("the first sequece is :",x1)
print("the second sequence is :",x2)
print("the circular convolution result is :",yn)
plt.show()

