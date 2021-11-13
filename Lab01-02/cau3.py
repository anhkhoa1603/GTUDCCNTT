import matplotlib.pylot as plt
import numpy as np
import sympy as sp
import math

def even_function(x, f):
    if f(-x) == f(x):
        return True
    else:
        return False

def odd_function(x, f):
    if f(-x) == -f(x):
        return True
    else:
        return False



x = sp.symbols('x')
f = lambda x: (x ** 3) + x

print("Ham chan: ", even_function(x, f) )
print("Ham le:", odd_function(x, f) )

def cau3i(x):
    return -x**3

x = np.arange(-10, 10, 0.1, dtype=np.float)
y = list( map(cau3i, x))

plt.plot(x, y, color='red')

plt.grid()
plt.show()
    
