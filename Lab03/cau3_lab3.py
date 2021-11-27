# -*- coding: utf-8 -*-
"""cau3_lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C6aiGEQFvJSWUCBv9e2wGhedjDuBuAEa
"""

import sympy as sp
import math

##a
x = sp.symbols('x')
f3_1 = 1 / (1 + 2**(1/2))
lm = sp.limit(f3_1, x, 0, '-')
print("Gioi han ben trai cua ham so la: " + str(lm))

import sympy as sp
import math
import matplotlib.pyplot as plt
import numpy as np

def f3_b(x): return (x**2 + x) / (x**3 + x**2)**(1/2)
##b
x = sp.symbols('x')
lm1 = sp.limit(f3_b(x), x, 0, '-')
print("Gioi han ben trai cua ham so la: " + str(lm1))

lm2 = sp.limit(f3_b(x), x, 0, '+')
print("Gioi han ben phai cua ham so la: " + str(lm2))