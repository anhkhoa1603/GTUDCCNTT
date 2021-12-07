# -*- coding: utf-8 -*-
"""cau_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16AzmOxsj2qAHn1DwP9dHxxE2FW6o3vy2
"""

import numpy as np
import sympy as sp
A = 459
B = 1

def f(x): return (x**2 - A*x - B*x + A*B) / (x - A)

x = sp.symbols('x')
fx = (x**2 - A*x - B*x + A*B) / (x - A)

lm_fx = sp.limit(fx, x, 0)
lm_fx1 = sp.limit(fx, x, B)
lm_fx2 = sp.limit(fx, x, A + B + 1)

print("Cau a:")
print("Gioi han cua ham so khi x dan tien ve 0 la", lm_fx)
print("Gioi han cua ham so khi x dan tien ve B la", lm_fx1)
print("Gioi han cua ham so khi x dan tien ve A + B + 1 la", lm_fx2)
print("\n")

print("Cau b:")
lm_fA = sp.limit(fx, x, A)
print("So sanh lim_f(A) va f(A):", lm_fA, A)
if lm_fA == A:
  print("Ham so lien tuc tai x=", A)
else:
  print("Ham so khong lien tuc tai x =", A)
print("\n")

print("Cau c:")
for n in np.arange(A - 10, A + 11, 1):
  lm_f = sp.limit(fx, x, n)
  if lm_f == f(n):
    print("Ham so lien tục tai x=", n)