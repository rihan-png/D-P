#find out linear and circular convolution of given sequences
import numpy as np 
import matplotlib.pyplot as plt
x1=[1,2,3,4]
x2=[5,6,7,8]
yn=np.convolve(x1,x2)
plt.subplot(6,1,1)
plt.stem(np.arange(len(x1)),x1)
plt.title('first sequence')
plt.subplot(6,1,2)
plt.stem(np.arange(len(x2)),x2)
plt.title('second sequence')
plt.subplot(6,1,3)
plt.stem(np.arange(len(yn)),yn)
plt.title('linear convolution')
plt.show()
