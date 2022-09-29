import numpy as np
import matplotlib.pyplot as plt
x=np.loadtxt("x.dat")
def dft (x,N):
	X=[]
	for k in range(N):
		X.append(0)
		for n in range(N):
			X[k]+=x[n]*np.exp(-1j*2*np.pi*k*n/N)
	return X

X=dft(x,len(x))
print(len(X))
#print(X)

arr = np.arange(10)
arr_1=(-1/2)**arr
hn1=np.pad(arr_1, (0,2), 'constant', constant_values=(0))
hn2=np.pad(arr_1, (2,0), 'constant', constant_values=(0))
hn=hn1+hn2
hn=hn[:6]
'''plt.plot(hn)
plt.show()'''
H=dft(hn,6)
#print(H)
Y=[]
for k in range(6):
	Y.append(X[k]*H[k])
'''plt.plot(Y)
plt.show()
'''
print(Y)	

