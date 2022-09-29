import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

N = 20
y2 = np.loadtxt('./prob-6-3.txt')
y3 = np.loadtxt('./prob-6-4.txt')

# plots
plt.stem(range(0, N), y2, label="DFT", linefmt='yellow', markerfmt='D', bottom=0)
plt.stem(range(0, N), y3, label="FFT and IFFT", linefmt='blue', bottom=0)
plt.title('Filter Output using DFT Vs FFT and IFFT')
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()  # minor
plt.legend()
#
# If using termux
plt.savefig('../figs/prob_6.pdf')
plt.savefig('../figs/prob_6.eps')
plt.savefig('../figs/prob_6.png')
plt.show()