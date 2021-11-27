# -*- coding: utf-8 -*-
"""Cau10_lab3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AIFtdDdoUszR6J-IVBJkCk5-l4IaU5XG
"""

import numpy as np
import sympy as sp

x = sp.symbols('x')
f10b = (x**2 + x - 6) / ( x**2 - 4)

lm_x_2 = sp.limit(f10b, x, 2)
print("Gioi han cua ham so fx khi x tien ve 2 =", lm_x_2)