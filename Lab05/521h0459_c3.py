#Cau3a
import sympy as sp

#c3a
x = sp.Symbol('x')
f_a = x**3 - 27 * x

df_a = sp.diff(f_a, x)
cvls_a = sp.solve(df_a, x)
print("Critical values:", cvls_a)

for x_a in cvls_a:
    if x_a < 0 or x_a > 5: cvls_a.remove(x_a)
cvls_a.extend([0, 5])

yvals = [f_a.subs(x, v) for v in cvls_a]
print("The absolutate maximum is: ", max(yvals))
print("The absolutate minimum is: ", min(yvals))

#c3b
x = sp.Symbol('x')
f_b = (3/2)*x**4 - 4*x**3 + 4

df_b = sp.diff(f_b, x)
cvls_b = sp.solve(df_b, x)
print("Critical values:", cvls_b)

for x_b in cvls_b:
    if x_b < 0 or x_b > 3: cvls_b.remove(x_b)
cvls_b.extend([0, 3])

yvals = [f_b.subs(x, v) for v in cvls_b]
print("The absolutate maximum is: ", max(yvals))
print("The absolutate minimum is: ", min(yvals))

#c3c
x = sp.Symbol('x')
f_c = 1/2 *x**4 - 4*x**2 +5

df_c = sp.diff(f_c, x)
cvls_c = sp.solve(df_c, x)
print("Critical values:", cvls_c)

for x_c in cvls_c:
    if x_c < 1 or x_c > 3: cvls_c.remove(x_c)
cvls_c.extend([1, 3])

yvals = [f_c.subs(x, v) for v in cvls_c]
print("The absolutate maximum is: ", max(yvals))
print("The absolutate minimum is: ", min(yvals))

#c3d
x = sp.Symbol('x')
f_d = 5/2 *x**4 -20/3*x**3+6

df_d = sp.diff(f_d, x)
cvls_d = sp.solve(df_d, x)
print("Critical values:", cvls_d)

for x_d in cvls_d:
    if x_d < -1 or x_d > 3: cvls_d.remove(x_d)
cvls_d.extend([-1, 3])

yvals = [f_d.subs(x, v) for v in cvls_d]
print("The absolutate maximum is: ", max(yvals))
print("The absolutate minimum is: ", min(yvals))