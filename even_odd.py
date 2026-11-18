import numpy as np
import matplotlib.pyplot as plt

# Create a time axis from -2 to 2 seconds. Negative time is needed to study
# signal folding and the even and odd parts of the signal.
t = np.linspace(-2, 2, 1000)

# Define a rectangular signal x(t). Its value is 1 for 0 <= t <= 1 and 0
# everywhere else.
xt = np.where((t>=0) & (t<=1), 1, 0)

# Plot the original signal x(t).
plt.subplot(6, 1, 1)
plt.plot(t, xt, 'red')
plt.grid()
plt.title('original signal', pad=20)
plt.tight_layout(h_pad=50)

# Fold the signal around the vertical axis by replacing t with -t. This gives
# the time-reversed signal x(-t).
xtm = np.where((-t>=0) & (-t<=1), 1, 0)

# Plot the folded signal x(-t).
plt.subplot(6, 1, 2)
plt.plot(t, xtm, 'blue')
plt.title('modified xt minus signal', pad=10)
plt.tight_layout(h_pad=50)

# Calculate the even part using xe(t) = [x(t) + x(-t)] / 2.
# An even signal has the property xe(t) = xe(-t).
x_even = (xt + xtm) / 2

# Plot the even component.
plt.subplot(6, 1, 3)
plt.plot(t, x_even, 'green')
plt.grid()
plt.title('even component', pad=10)
plt.tight_layout(h_pad=50)

# Calculate the odd part using xo(t) = [x(t) - x(-t)] / 2.
# An odd signal has the property xo(t) = -xo(-t).
x_odd = (xt - xtm) / 2

# Plot the odd component.
plt.subplot(6, 1, 4)
plt.plot(t, x_odd, 'orange')
plt.grid()
plt.title('odd component', pad=10)
plt.tight_layout(h_pad=50)

# Reconstruct the original signal using x(t) = xe(t) + xo(t).
x_rec = x_even + x_odd

# Plot the reconstructed signal and compare it with the original waveform.
plt.subplot(6, 1, 5)
plt.plot(t, x_rec, 'purple')
plt.grid()
plt.title('reconstructed signal', pad=10)
plt.tight_layout(h_pad=50)
 
plt.show()
