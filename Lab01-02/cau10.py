import numpy as np
import matplotlib.pyplot as plt

def f10_a(x, k):
    return (x ** 2) + k

def cau10a():
    k = np.arange(2,14,2) 
    x = np.arange(-10, 10.1, 0.1)
    
    for ki in k:
        y = []
        for xi in x:
            y.append(f10_a(xi, ki))

        plt.plot(x, y, label="k="+str(ki))
    
    plt.title("Cau 10a")
    plt.legend()
    plt.show()

cau10a()

def f10_b(x, k):
    return (x + k)**2

def cau10b():
    k = np.arange(2,14,2) 
    x = np.arange(-10, 10.1, 0.1)
    
    for ki in k:
        y = []
        for xi in x:
            y.append(f10_b(xi, ki))

        plt.plot(x, y, label="k="+str(ki))
    
    plt.title("Cau 10b")
    plt.legend()
    plt.show()

cau10b()

def f10_c(x, k):
    return k * x** 1/2

def cau10c():
    k = [1/3, 1, 3, 6]
    x = np.arange(1, 50.1, 0.1)
    
    for ki in k:
        y = []
        for xi in x:
            y.append(f10_c(xi, ki))

        plt.plot(x, y, label="k="+str(ki))
    
    plt.title("Cau 10c")
    plt.legend()
    plt.show()

cau10c()

def cau10d():
    x = np.arange(-10, 10.1, 0.1)
    f10_d = lambda x: x ** 3
    y = np.array( list( map( f10_d, x)))
    
    plt.plot(x,y,label="original graph")
    plt.plot(x-1, y-1, label="shifted graph")

    plt.title("Cau 10d")
    plt.legend()
    plt.show()

cau10d()

def cau10e():
    x = np.arange(-10, 10.1, 0.1)
    f10_e = lambda x: x ** 2/3
    y = np.array( list( map( f10_e, x)))
    
    plt.plot(x,y,label="original graph")
    plt.plot(x+1, y-1, label="shifted graph")

    plt.title("Cau 10e")
    plt.legend()
    plt.show()

cau10e()

def cau10f():
    x = np.arange(-10, 10.1, 0.1)
    f10_f = lambda x: 1/2 + (x + 1) + 5
    y = np.array( list( map( f10_f, x)))
    
    plt.plot(x,y,label="original graph")
    plt.plot(x+1, y-5, label="shifted graph")

    plt.title("Cau 10f")
    plt.legend()
    plt.show()

cau10f()

def cau10g():
    x = np.arange(-10, 10.1, 0.1)
    f10_g = lambda x: 1 / (x ** 2)
    y = np.array( list( map( f10_g, x)))
    
    plt.plot(x,y,label="original graph")
    plt.plot(x-1,y-1,label="shifted graph")

    plt.title("Cau 10g")
    plt.legend()
    plt.show()

cau10g()

def cau10h():
    x = np.arange(-10, 10.1, 0.1)
    f10_h = lambda x: 1 - (x ** 3)
    y = list( map( f10_h, x))
    yStretched = list( map( f10_h, x/2))

    plt.plot(x,y,label="original graph")
    plt.plot(x,yStretched,label="stretched horizontally graph")

    plt.title("Cau 10h")
    plt.legend()
    plt.show()

cau10h()

def cau10i():
    x = np.arange(-10, 10.1, 0.1)
    f10_i = lambda x: (x + 1) ** 1/2
    y = list( map( f10_i, x))
    yCompressed = list( map( f10_i, x * 4))

    plt.plot(x,y,label="original graph")
    plt.plot(x,yCompressed,label="compressed horizontally graph")

    plt.title("Cau 10i")
    plt.legend()
    plt.show()

cau10i()

def cau10j():
    x = np.arange(-10, 10.1, 0.1)
    f10_j = lambda x: (x + 1) ** 1/2
    y = list( map( f10_j, x))
    xStretched = list( map( f10_j, x / 3))

    plt.plot(x,y,label="original graph")
    plt.plot(xStretched,y,label="stretched horizontally graph")

    plt.title("Cau 10j")
    plt.legend()
    plt.show()

cau10j()