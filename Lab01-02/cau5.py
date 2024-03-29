# -*- coding: utf-8 -*-
"""cau5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OUBfsCB1MJH9d8PXk8gYVrOJ_JkYiAWj
"""

import sympy as sp
import math

x = sp.symbols('x')
f5a = abs(x)**(1/2)

fig_5a = sp.plot(f5a, (x, -10, 10), line_color = 'red')

import sympy as sp
import math

x = sp.symbols('x')
f5b = x**4 + 3*x**2 - 1

fig_5b = sp.plot(f5b, (x, -5, 5), line_color = 'red')

import sympy as sp
import math

x = sp.symbols('x')
f5c = x**3 + x

fig_5c = sp.plot(f5c, (x, -5, 5), line_color = 'red')

import sympy as sp
import math

x = sp.symbols('x')
f5d = math.e**x

fig_5d = sp.plot(f5d, (x, -5, 5), line_color = 'red')

import sympy as sp
import math

x = sp.symbols('x')
f5e = sp.ln(x)

fig_5e = sp.plot(f5e, (x, -5, 5), line_color = 'red')

import sympy as sp
import math

x = sp.symbols('x')
f5f = (2*x**2 - 3) / (7*x + 4)

fig_5f = sp.plot(f5f, (x, -5, 5), line_color = 'red')