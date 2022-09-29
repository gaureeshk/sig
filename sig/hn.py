
import numpy as np
import matplotlib.pyplot as plt

n = np.arange(10000)
fn=(-1/2)**n
hn1=np.pad(fn, (0,2), 'constant', constant_values=(0))
hn2=np.pad(fn, (2,0), 'constant', constant_values=(0))
print(hn1,hn2)
print(sum(hn1)+sum(hn2))



