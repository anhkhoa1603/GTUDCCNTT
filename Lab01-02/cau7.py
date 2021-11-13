# -*- coding: utf-8 -*-
"""cau7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aivbhZg91G8hba8pe4KEEuOmcYr6CQL6
"""

import numpy as np
from numpy import sin, cos
import matplotlib.pyplot as plt

def f1(t): return 4 * sin(t)**5 + 5
def f2(t): return 3 * cos(t) - 1.7 * cos(2*t) - cos(3*t) + 1

t = np.arange(-10, 10, 0.1)
plt.plot(t, f1(t), label="x(t)")
plt.plot(t, f2(t), label="y(t)")
plt.legend()
plt.grid()
plt.show()