# -*- coding: utf-8 -*-
"""cau4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bhsiVchMYtPcR1DK0ChGqMsfXgrjHImB
"""

import sympy as sp

x = sp.symbols('x')
root = sp.solve(x**2 + 2*x - 1)
print(root)