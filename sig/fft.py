import numpy as np
import matplotlib.pyplot as plt


def x(n):
    if n >= 0 and n < 6:
        x_dict = {0:1,1:2,2:3,3:4,4:2,5:1}
        return x_dict[n]
    else:
        return 0

def h(n):
    if n < 0:
        return 0

    elif n == 0:
        return 1    #h(0) = 1
        
    elif n == 1:
        return -0.5 #h(1) = -1/2
    else:
        return 5.0 * ((-0.5)**n)

n = 16
xn_i = [x(i) for i in range(n)]
hn_i = [h(i) for i in range(n)]


########################################################    FFT    ########################################################


def fft(x):

    N = len(x)
    
    if N == 1:
        return x
    else:
        X_even = fft(x[::2])
        X_odd = fft(x[1::2])
        factor = np.exp(-2j*np.pi*np.arange(N)/ N)
        
        X = np.concatenate(\
            [X_even+factor[:int(N/2)]*X_odd,
             X_even+factor[int(N/2):]*X_odd])
        return X




################################    PLOTS   #################################################

############################    X(k)    ###########################

Xo = fft(xn_i)
X = np.real(Xo)


###########################     H(k)    ###########################

Ho = fft(hn_i)
H = np.real(Ho)/n
#print("\nRe{H}\n")
#print(H)
'''


###########################     Y(k)    ###########################
'''
Yo = []
for k in range(n):
    Yo.append(Xo[k] * Ho[k])
#print("\nRe{Y}\n")
#print(Y)
Y = np.real(Yo)



plt.figure(figsize=(12,10))
plt.subplot(3,1,1)
plt.stem(range(0,n),X)
plt.ylabel('$X(k)$')
plt.grid()
plt.title('X(k) ')
plt.subplot(3,1,2)
plt.stem(range(0,n),H)
plt.ylabel('$H(k)$')
plt.grid()
plt.title('H(k)')
plt.subplot(3,1,3)
plt.stem(range(0,n),Y)
plt.xlabel('$k$')
plt.ylabel('$Y(k)$')
plt.title('Y(k)')
plt.grid()
plt.savefig('./figs/FFT.jpg')
plt.show()






########################################################    IFFT    ########################################################

def ifft(X):
    '''
    N = len(X)
    
    if N == 1:
        return X
    else:
        x_even = fft(X[::2])
        x_odd = fft(X[1::2])
        factor = np.exp(2j*np.pi*np.arange(N)/ N)
        
        x = np.concatenate([x_even+factor[:int(N/2)]*x_odd,
             x_even+factor[int(N/2):]*x_odd])
        return x
    '''
    Xx = np.conjugate(X)
    x = fft(Xx)
    return x

yn = ifft(Yo)
y = np.real(yn)
print('Re{y}')
print(y)


plt.figure(figsize=(12,10))
plt.subplot(2,1,1)
plt.stem(range(0,n),Y)
plt.title('Y(k)')
plt.ylabel('$Y(k)$')
plt.grid()
plt.subplot(2,1,2)
plt.stem(range(0,n),y)
plt.xlabel('$k$')
plt.ylabel('$y(k)$')
plt.title('y(n) using IFFT')
plt.grid()
plt.savefig('./figs/IFFT.jpg')
plt.show()