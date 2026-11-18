
# Signal Generation

import numpy as np
import matplotlib.pyplot as plt

# Time variables
t = np.linspace(0, 5, 1000)
t1 = np.linspace(-5, 5, 1000)

# Continuous-Time (CT) Signals
sine = np.sin(2 * np.pi * 1 * t)
cosine = np.cos(2 * np.pi * 1 * t)
step = np.where(t >= 0, 1, 0)
ramp = np.where(t >= 0, t, 0)

expo_incr = np.exp(t)
expo_dcr = np.exp(-t)

n = np.arange(-5, 5, 0.001)
impulse = np.where(n == 0, 1, 0)

syn = np.sinc(t1)
y_sig = np.sign(t1)

# CT Signal Plotting
plt.figure(figsize=(8, 8))

plt.subplot(4, 4, 1)
plt.plot(t, sine)
plt.title('Sine Wave')

plt.subplot(4, 4, 2)
plt.plot(t, cosine)
plt.title('Cosine Wave')

# CT Signals
plt.subplot(4, 4, 3)
plt.plot(t, step)

plt.subplot(4, 4, 4)
plt.plot(t, ramp)
plt.title('ramp')
plt.subplot(4, 4, 5)
plt.plot(impulse, n)
plt.title('impulse')
plt.subplot(4, 4, 6)
plt.plot(t, expo_incr)
plt.title('exponential')
plt.subplot(4, 4, 7)
plt.plot(t, expo_dcr)
plt.title('exponential decrease')
plt.subplot(4, 4, 8)
plt.plot(t1, syn)
plt.title('syn')
plt.subplot(4, 4, 9)
plt.plot(t1, y_sig)
plt.title('signal')
plt.tight_layout()

plt.figure()

# DT Signals
# %%

plt.subplot(4, 4, 1)
plt.stem(t, sine)
plt.title('Sine Wave')

plt.subplot(4, 4, 2)
plt.stem(t, cosine)
plt.title('Cosine Wave')

plt.subplot(4, 4, 3)
plt.stem(t, step)

plt.subplot(4, 4, 4)
plt.stem(t, ramp)

plt.subplot(4, 4, 5)
plt.stem(impulse, n)

plt.subplot(4, 4, 6)
plt.stem(t, expo_incr)

plt.subplot(4, 4, 7)
plt.stem(t, expo_dcr)

plt.subplot(4, 4, 8)
plt.stem(t1, syn)

plt.subplot(4, 4, 9)
plt.stem(t1, y_sig)

plt.tight_layout()
plt.show()
