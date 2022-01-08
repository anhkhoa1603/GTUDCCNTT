import sympy as sp

#c2a
x = sp.Symbol('x')
f_a = 3 * x**4 - 16 * x**3 + 18 * x*x - 9

df_a = sp.diff(f_a, x)
cvls_a = sp.solve(df_a, x) 

dff_a = sp.diff(f_a, x, 2)
print("dfx_2: ",dff_a)
for i in cvls_a: 
    result = dff_a.subs(x, i)
    if result > 0:
        GTNN = f_a.subs(x, result) 
        print("Minimum f({}): ".format(result), GTNN)
    if result < 0:
        GTLN = f_a.subs(x, result)
        print("Maximum f({}): ".format(result), GTLN)
        
#c2b
x = sp.Symbol('x')
f_b = (x + 2) / (2 * x*x)

df_b = sp.diff(f_b, x)
cvls_b = sp.solve(df_b, x) 

dff_b = sp.diff(f_b, x, 2)
print("dfx_2: ",dff_b)
for i in cvls_b: 
    result = dff_b.subs(x, i)
    if result > 0:
        GTNN = f_b.subs(x, result) 
        print("Minimum f({}): ".format(result), GTNN)
    if result < 0:
        GTLN = f_b.subs(x, result)
        print("Maximum f({}): ".format(result), GTLN)
        
#c2c
x = sp.Symbol('x')
f_c = -x**2/3 + x**2 +3*x +4

df_c = sp.diff(f_c, x)
cvls_c = sp.solve(df_c, x) 

dff_c = sp.diff(f_c, x, 2)
print("dfx_2: ",dff_c)
for i in cvls_c: 
    result = dff_c.subs(x, i)
    if result > 0:
        GTNN = f_c.subs(x, result) 
        print("Minimum f({}): ".format(result), GTNN)
    if result < 0:
        GTLN = f_c.subs(x, result)
        print("Maximum f({}): ".format(result), GTLN)
        
#c2d
x = sp.Symbol('x')
f_d = (5*x**5 + 5)/x


df_d = sp.diff(f_d, x)
cvls_d = sp.solve(df_d, x) 

dff_d = sp.diff(f_d, x, 2)
print("dfx_2: ",dff_d)
for i in cvls_d: 
    result = dff_d.subs(x, i)
    if result > 0:
        GTNN = f_d.subs(x, result) 
        print("Minimum f({}): ".format(result), GTNN)
    if result < 0:
        GTLN = f_d.subs(x, result)
        print("Maximum f({}): ".format(result), GTLN)