# -*- coding: utf-8 -*-
"""521h0459_c9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xsMLk3ofbZ9y8744mBSg_he0lYH9vSEL
"""

import sympy as sp
import math

#c9a
x1, x2 = sp.symbols('x1, x2')
f_a = x1**2+x2**2 -4*x1 -4*x2

dfx1 = sp.diff(f_a, x1)
dfx2 = sp.diff(f_a, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9b
x1, x2 = sp.symbols('x1, x2')
f_b = 3 * x1*x1 + 2 * x2**4 - x2 + x2*x2 + 1

dfx1 = sp.diff(f_b, x1)
dfx2 = sp.diff(f_b, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9c
x1, x2 = sp.symbols('x1, x2')
f_c = math.e**(x1**2)+x2**2 -3-2*x2

dfx1 = sp.diff(f_c, x1)
dfx2 = sp.diff(f_c, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9d
x1, x2 = sp.symbols('x1, x2')
f_d = (x1**2-1)**2+x2**2-3*x2+1

dfx1 = sp.diff(f_d, x1)
dfx2 = sp.diff(f_d, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9e
x1, x2 = sp.symbols('x1, x2')
f_e = x1**2*math.e**x1+51*x2+x2**4+3

dfx1 = sp.diff(f_e, x1)
dfx2 = sp.diff(f_e, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9f
x1, x2 = sp.symbols('x1, x2')
f_f = math.e**(x1**2-3)+x2**2-3*x2

dfx1 = sp.diff(f_f, x1)
dfx2 = sp.diff(f_f, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')

#c9g
x1, x2 = sp.symbols('x1, x2')
f_g = x1*x2**3+ 2*x1**2+2*x2**4-5

dfx1 = sp.diff(f_g, x1)
dfx2 = sp.diff(f_g, x2)

x1_cvals = sp.solve(dfx1, x1)
x2_cvals = sp.solve(dfx2, x2)

print(x1_cvals)
print(x2_cvals)
print('\n')