import math
import numpy as np

def cau2a(x):
    res = (2 + (x ** 2) / ((x ** 2) + 4))
    return res

fmin = math.inf
fmax = -math.inf

for x in np.arange(-2, 2.1, 0.1):
    if cau2a(x) < fmin:
        fmin = cau2a(x)

    if cau2a(x) > fmax:
        fmax = cau2a(x)
   
print(fmin)
print(fmax)

def cau2e(x):
    if x >= 0:
        return x
    else:
        return -x

fmin = math.inf
fmax = -math.inf

for x in np.arange(-3, 3.1, 0.1):
    if cau2e(x) < fmin:
        fmin = cau2e(x)

    if cau2e(x) > fmax:
        fmax = cau2e(x)
        
print(fmin)
print(fmax)