import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.sqrt(1 - (abs(x) - 1)**2)

def f2(x):
    return -3 * np.sqrt(1 - np.sqrt(abs(x)/2))

x = np.arange(-2, 2.1, 0.2)
plt.plot(x, f1(x), color = 'm', label="f1(x)")
plt.plot(x, f2(x), color = 'r', label="f2(x)")
plt.legend()
plt.grid()
plt.show()
