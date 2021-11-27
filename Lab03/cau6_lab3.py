# -*- coding: utf-8 -*-
"""Cau6_Lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RKW-Es2byaaVqQDZI134oaW2cQML9IeK
"""

import numpy as np
import sympy as sp

x = sp.symbols('x')
f6a = (x**2 - x - 6) / (x - 3)

lm_x_0 = sp.limit(f6a, x, 0)
print("So sanh lm_x_0 va f(0):", lm_x_0, 5)

for c in np.arange(-100, 100, 1):
  if c != 0:
    lm_c = sp.limit(f6a, x, c)
    if lm_c != f6a.subs(x, c):
      print("Fx khong lien tuc tai x =", c, lm_c, f6a.subs(x, c))

import numpy as np
import sympy as sp

x = sp.symbols('x')
f6b = (x**3 - 8) / (x**2 - 4)

lm_x_2 = sp.limit(f6b, x, 2)
print("So sanh lm_x_2 va f(2):", lm_x_2, 3)

lm_x_n2 = sp.limit(f6b, x, -2)
print("So sanh lm_x_-2 va f(-2):", lm_x_n2, 4)

for c in np.arange(-100, 100, 1):
  if c != 2 & c != -2:
    lm_c = sp.limit(f6b, x, c)
    if lm_c != f6b.subs(x, c):
      print("Fx khong lien tuc tai x =", c, lm_c, f6a.subs(x, c))

import numpy as np
import sympy as sp

x = sp.symbols('x')
f6c = (x**2 - x - 2) / (x - 2)

lm_x_2 = sp.limit(f6c, x, 2)
print("So sanh lm_x_2 va f(2):", lm_x_2, 1)

for c in np.arange(-100, 100, 1):
  if c != 0:
    lm_c = sp.limit(f6c, x, c)
   if lm_c != f6c.subs(x, c):
      print("Fx khong lien tuc tai x =", c, lm_c, f6c.subs(x, c))

import numpy as np
import sympy as sp

x = sp.symbols('x')
f6d = 1 / (x**2)

lm_x_0 = sp.limit(f6d, x, 0)
print("So sanh lm_x_0 va f(0):", lm_x_0, 1)

for c in np.arange(-100, 100, 1):
  if c != 0:
    lm_c = sp.limit(f6d, x, c)
    if lm_c != f6d.subs(x, c):
      print("Fx khong lien tuc tai x =", c, lm_c, f6d.subs(x, c))