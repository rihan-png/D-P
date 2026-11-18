# Demonstrate common signal operations using a rectangular pulse.
import numpy as np
import matplotlib.pyplot as plt

# Create a detailed time axis from -20 to 20 so all shifted signals are visible.
t = np.linspace(-20, 20, 100000)

# Define x(t) = 1 for 0 <= t <= 5 and x(t) = 0 elsewhere.
sig = np.where((t >= 0) & (t <= 5), 1, 0)

# Amplitude scaling: y(t) = 2x(t). The amplitude becomes twice as large.
sig_amp = 2*sig

# Time compression: y(t) = x(2t). The pulse duration becomes 5/2 units.
sig_time = np.where((2*t >= 0) & (2*t <= 5), 1, 0)

# Time expansion: y(t) = x(0.5t). The pulse duration becomes 5/0.5 = 10 units.
sig_time_exp = np.where((0.5*t >= 0) & (0.5*t <= 5), 1, 0)

# Time delay: y(t) = x(t - 2). The signal moves 2 units to the right.
sig_time_shift = np.where((t-2 >= 0) & (t-2 <= 5), 1, 0)

# Time advance: y(t) = x(t + 3). The signal moves 3 units to the left.
sig_time_adv = np.where((t+3 >= 0) & (t+3 <= 5), 1, 0)

# Time folding: y(t) = x(-t). The signal is reflected about t = 0.
sig_time_fold = np.where((-t >= 0) & (-t <= 5), 1, 0)

# Arrange the original signal and each operation in one figure for comparison.
plt.figure(figsize=(12, 8))
plt.subplot(4, 2, 1)
plt.plot(t, sig, 'red')

# Plot y(t) = 2x(t).
plt.subplot(4, 2, 2)
plt.plot(t, sig_amp, 'green')
plt.title('Amplitude Scaling')

# Plot the compressed signal y(t) = x(2t).
plt.subplot(4, 2, 3)
plt.plot(t, sig_time, 'blue')
plt.title('Time Scaling')

# Plot the expanded signal y(t) = x(0.5t).
plt.subplot(4, 2, 4)
plt.plot(t, sig_time_exp, 'orange')
plt.title('Time Expansion')

# Plot the delayed signal y(t) = x(t - 2).
plt.subplot(4, 2, 5)
plt.plot(t, sig_time_shift, 'purple')
plt.title('Time Shifting')

# Plot the advanced signal y(t) = x(t + 3).
plt.subplot(4, 2, 6)
plt.plot(t, sig_time_adv, 'brown')
plt.title('Time Advancing')

# Plot the folded signal y(t) = x(-t).
plt.subplot(4, 2, 7)
plt.plot(t, sig_time_fold, 'gray')
plt.title('Time Folding')

# Fit the subplots neatly and display the final comparison figure.
plt.tight_layout()
plt.show()
