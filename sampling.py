import numpy as np
import matplotlib.pyplot as plt

# Create many time points to draw the continuous-time signal smoothly.
t= np.linspace(0,5,1000)

# Generate a 5 Hz sine wave using x(t) = sin(2*pi*f*t).
sine =np.sin(2*np.pi*5*t)

# Set different sampling frequencies for comparison. The sampling theorem
# requires fs >= 2*f for faithful sampling.
fs=10
fs1=25
fs3=50
fs3=100

# Calculate the sampling period from Ts = 1/fs.
Ts=1/fs
Ts1=1/fs1
Ts2=1/fs3
Ts3=1/fs3

# Create sampling instants from 0 to 5 seconds. A larger fs gives smaller Ts
# and therefore produces more samples.
ts=np.arrange(0,5,Ts)
ts=np.arrange(0,5,Ts1)
ts=np.arrange(0,5,Ts2)
ts3=np.arrange(0,5,Ts3)

# Calculate the sampled values using x[n] = sin(2*pi*f*tn).
sine_dt=np.sin(2*np.pi*5*ts)
sine_dt1=np.sin(2*np.pi*5*ts1)
sine_dt2=np.sin(2*np.pi*5*ts2)
sine_dt3=np.sin(2*np.pi*5*ts3)

# Plot the original continuous-time sine wave.
plt.subplot(8,1,1)
plt.plot(t,sine)
plt.title('Continuous time signal')

# Estimate signal values at the first sampling instants by interpolation.
xr=np.interp(ts,t,sine)

# Use stem plots to show each discrete sample clearly.
plt.subplot(8,1,2)
plt.stem(ts,sine_dt)
plt.subplot(8,1,3)
plt.stem(ts1,sine_dt)
plt.subplot(8,1,4)
plt.stem(ts2,sine_dt1)
plt.subplot(8,1,5)
plt.stem(ts3,sine_dt3)
plt.subplot(8,1,6)
plt.plot(k,xr)

# Display the sampling comparison figure.
plt.show()
