import numpy as np
x=[0,1,2,3]
x = np.asarray(x, dtype=float)
print(x)
N = x.shape[0]
print(N)
n = np.arange(N)
print(n)
k = n.reshape((N, 1))
print(k)
