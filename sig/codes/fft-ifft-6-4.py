import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

# If using termux
# import subprocess
# import shlex
# end if

N = 18
n = np.arange(N)
fn = (-1 / 2) ** n
hn1 = np.pad(fn, (0, 2), 'constant', constant_values=(0, 0))
hn2 = np.pad(fn, (2, 0), 'constant', constant_values=(0, 0))
h = hn1 + hn2
xtemp = np.array([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
x = np.pad(xtemp, (0, 14), 'constant', constant_values=(0))

X = fft(x)
H = fft(h)
Y = H * X
y = ifft(Y).real
# plots
plt.stem(range(0, 20), y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()  # minor

np.savetxt("./prob-6-4.txt", y)
# If using termux
plt.savefig('../figs/prob_6-4.png')
plt.savefig('../figs/prob_6-4.eps')
plt.savefig('../figs/prob_6-4.pdf')
# subprocess.run(shlex.split("termux-open ../figs/yndft.pdf"))
# else
plt.show()