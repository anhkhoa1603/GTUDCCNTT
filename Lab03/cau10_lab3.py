import sympy as sp

x = sp.symbols('x')
f10b = (x**2 + x - 6) / (x**2 - 4)

lm_x_2 = sp.limit(f10b, x, 2)
print("Gioi han cua ham so fx khi x tien ve 2 =", lm_x_2)
