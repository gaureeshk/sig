import matplotlib.pyplot as plt
import numpy as np
x=np.loadtxt("x.dat")
y=np.loadtxt("y.dat")
plt.subplot(2, 1, 1)
plt.stem(range(0,6),x)
plt.title('Digital Filter Input-Output')
plt.ylabel('$x(n)$')
plt.grid()

plt.subplot(2,1,2)
plt.stem(range(0,20),y)
plt.xlabel('$n$')
plt.ylabel('$y(n)$')
plt.grid()

plt.show()



