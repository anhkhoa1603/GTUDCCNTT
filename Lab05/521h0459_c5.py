import sympy as sp
x = sp.Symbol('x')

def Gold(f, a, b, e):
    d = b - a
    while b - a >= e:
        d = d * 0.618
        x1 = b - d
        x2 = a + d
        if(f.subs(x, x1) <= f.subs(x, x2)):
            b = x2
        else:
            a = x1
    
    print("a = {0}, b = {1}".format(a, b))   
    print("f(xa) = ", f.subs(x, a))
    print("f(xb) = ", f.subs(x, b))

print(Gold(x**2, -2, 1, 0.3))