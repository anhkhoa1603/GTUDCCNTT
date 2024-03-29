# -*- coding: utf-8 -*-
"""cau8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KXD7SQIV39PF30gs5mcaFgrTElBoM_2h
"""

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10, 10, dtype=np.float)
f1 = lambda x: -x + 5
f2 = lambda x: x/2 + 2
plt.plot(x, f1(x), color = 'b', label="f1(x)")
plt.plot(x, f2(x), color = 'r', label="f2(x)")

x = sp.symbols('x')
f1 = -x + 5
f2 = x/2 + 2
x_root = sp.solve(f1-f2)
print(x_root)
y_root = f1.subs(x, x_root[0])


plt.plot(x_root[0], y_root, 'mo')
plt.title('Find intersection point of f1(x) = - x + 5 and f2(x) = x/2 +2')
plt.legend()
plt.grid()
plt.show()