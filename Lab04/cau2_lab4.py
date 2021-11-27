# -*- coding: utf-8 -*-
"""Cau2_Lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E71oVQVKRJtfmCdmAkuzcxbMWYALcX3s
"""

#Cau4a
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = x**2 + 1
df = sp.diff(f, x)

slope = df.subs(x, 2)
y_tangentLine = slope * (x - 2) + 5

sp.plot(f, y_tangentLine, (x, -5, 5))

#Cau4b
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = x - 2 * x**2
df = sp.diff(f, x)

slope = df.subs(x, 1)
y_tangentLine = slope * (x - 1) - 1

sp.plot(f, y_tangentLine, (x, -5, 5))

#Cau4c
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = x / (x - 2)
df = sp.diff(f, x)

slope = df.subs(x, 3)
y_tangentLine = slope * (x - 3) + 3

sp.plot(f, y_tangentLine, (x, 0, 4))

#Cau4d
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
g = 8 / x**2
dg = sp.diff(g, x)

slope = dg.subs(x, 2)
y_tangentLine = slope * (x - 2) + 2

sp.plot(g, y_tangentLine, (x, -5, 5))

#Cau4e
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
g = sp.sqrt(x)
dg = sp.diff(g, x)

slope = dg.subs(x, 4)
y_tangentLine = slope * (x - 4) + 2

sp.plot(g, y_tangentLine, (x, -5, 5))

#Cau4f
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols('t')
h = t**3 + 3 * t
dh = sp.diff(f, t)

slope = dh.subs(t, 1)
y_tangentLine = slope * (t - 1) + 4

sp.plot(h, y_tangentLine, (t, -5, 5))

#Cau4g
import sympy as sp
import matplotlib.pyplot as plt

x = sp.symbols('x')
f = 8 / sp.sqrt(x - 2)
df = sp.diff(f, x)

slope = df.subs(x, 6)
y_tangentLine = slope * (x - 6) + 4

sp.plot(f, y_tangentLine, (x, -5, 5))

import sympy as sp
import matplotlib.pyplot as plt

z = sp.symbols('z')
g = 1 + sp.sqrt(4 - z)
dg = sp.diff(g, z)

slope = dg.subs(z, 3)
y_tangentLine = slope * (z - 3) + 2

sp.plot(g, y_tangentLine, (z, -5, 5))