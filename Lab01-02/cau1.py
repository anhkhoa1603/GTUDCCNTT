import math

def squareRoot_1a(x):
    return x ** (1 / 2)
    return math.sqrt(x)

print( squareRoot_1a( 16 ) )

def cubeRoot_1b(x):
    return x ** (1 / 3)

print( cubeRoot_1b( 27 ) )

def expression_1c(x):
    return x ** (2 / 3)

print( expression_1c( 8 ) )

def expression_1d(x):
    return ((x ^ 3) / 3 + (x ^ 2) / 2 - 2 * x + 1 / 3)

print( expression_1d(9) )

def expression_1e(x):
    return((2 * (x ^ 2) - 3) / (7 * x + 4))

print( expression_1e( 7 ) )

def expression_1f(x):
    return((5 * (x ^ 2) + 8 * x - 3) / (3 * (x ^ 2) + 2))
    
print( expression_1f( 4 ) )

def sin_1g(x):
    return math.sin(x)

print( sin_1g( 45 ) )

def cos_1h(x):
    return math.cos(x)

print( cos_1h( 90 ) )
    