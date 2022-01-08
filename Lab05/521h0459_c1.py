import sympy as sp

x = sp.Symbol('x')
f_a = 3 * x**4 - 16 * x**3 + 18 * x*x - 9
f_b = (x + 2) / (2 * x*x)
f_c = -x**2/3 + x**2 +3*x +4
f_d = (5*x**5 + 5)/x

df_a = sp.diff(f_a, x)
df_b = sp.diff(f_b, x)
df_c = sp.diff(f_c, x)
df_d = sp.diff(f_d, x)

cvl_a = sp.solve(df_a, x)
cvl_b = sp.solve(df_b, x)
cvl_c = sp.solve(df_c, x)
cvl_d = sp.solve(df_d, x)

print("1a. Critical values:", cvl_a)
print("1b. Critical values:", cvl_b)
print("1c. Critical values:", cvl_c)
print("1d. Critical values:", cvl_d)