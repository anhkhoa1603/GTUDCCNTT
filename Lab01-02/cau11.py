# -*- coding: utf-8 -*-
"""cau11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SNPrK5rHQIYo0XlBN2xfmLy8ahNbH4wq
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def cau11a():
    x = np.arange(-2, 2.1, 0.1)
    f = lambda x: (x ** 3) - x / 2
    y = list( map(f, x))

    plt.plot(x, y, label = "f = (x ** 3) - x / 2 is not one-to-one function")

    plt.legend()
    plt.grid()
    plt.show()

cau11a()

def cau11b():
    x = np.arange(-2, 2.1, 0.1)
    f = lambda x: (x ** 3) + x / 2
    y = list( map(f, x))

    plt.plot(x, y, label = "f = (x ** 3) + x / 2 is one-to-one function")

    plt.legend()
    plt.grid()
    plt.show()

cau11b()