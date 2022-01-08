# -*- coding: utf-8 -*-
"""cau_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GS-5Jj-WSm4GklbVyxuFkCM-byS0OCU_
"""

import numpy as np #khai báo thư viện 
import sympy as sp #khai báo thư viện 
import matplotlib.pyplot as plt #khai báo thư viện 

A = 459
B = 1

def cau_3a():
    x = sp.symbols('x') #tạo biến x là 1 hàm biểu tượng
    fx = A * x**2 - 2 * A * x + A #khai báo phương trình fx
    d_fx = sp.diff(fx, x) #đạo hàm phương trình fx
    slope = d_fx.subs(x, 2) #tính đạo hàm của fx khi thế x vào phương trình

    fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa fx bằng hàm ẩn danh
    fx1 = lambda x: slope * (x - 2) + A #định nghĩa phương trình tiếp tuyến của fx bằng hàm ẩn danh

    x = np.arange(-5, 5, 0.1, dtype=np.float) #Khởi tạo mảng của x từ -5 tới 5 với bước nhảy là 0.1
    plt.plot(x, fx(x), color = 'b', label="y = f(x)") #vẽ đồ thị phương trình fx
    plt.plot(x, fx1(x), color = 'g', label="y = f'(x)(x-2)+A") #vẽ đồ thị tiếp tuyến của fx

    plt.title("câu 3a") #in tiêu đề
    plt.legend() #hiện chú thích
    plt.grid() #vẽ lưới cho đồ thị
    plt.show() #hiển thị đồ thị
cau_3a() #gọi câu 3a

def cau_3b():
    x = sp.symbols('x') #tạo biến x là 1 hàm biểu tượng
    fx = A * x**2 - 2 * A * x + A #khai báo phương trình fx
    d_fx = sp.diff(fx, x) #đạo hàm phương trình fx
    ng = sp.solve(d_fx*(x - 0) + (-A) - fx) #giải nghiệm phương trình (f'(x) * (x - x0) + y0) - f(x)
    ng1 = fx.subs(x, ng[0]) #giá trị fx khi thế x1 vào phương trình
    ng2 = fx.subs(x, ng[1]) #giá trị fx khi thế x2 vào phương trình

    d_fx1 = d_fx.subs(x, ng[0]) #giá trị của f'x khi thế x1 vào phương trình
    d_fx2 = d_fx.subs(x, ng[1]) #giá trị của f'x khi thế x2 vào phương trình

    fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa phương trình fx bằng hàm ẩn danh
    fx1 = lambda x: d_fx1 * (x - ng[0]) + ng1 #định nghĩa phương trình tiếp tuyến thứ nhất bằng hàm ẩn danh
    fx2 = lambda x: d_fx2 * (x - ng[1]) + ng2 #định nghĩa phương trình tiếp tuyến thứ nhất bằng hàm ẩn danh

    x = np.arange(-5, 5, 0.1, dtype=np.float) #Khởi tạo mảng của x từ -5 tới 5 với bước nhảy là 0.1
    plt.plot(x, fx(x), color = 'b', label="y = f(x)") #vẽ đồ thị phương trình fx
    plt.plot(x, fx1(x), color = 'r', label="y = f'({0})(x {0}) - {1}".format(ng[0],ng1)) #vẽ đồ thị tiếp tuyến thứ nhất của fx
    plt.plot(x, fx2(x), color = 'g', label="y = f'({0})(x {0}) - {1}".format(ng[1],ng2)) #vẽ đồ thị tiếp tuyến thứ hai của fx

    plt.title("câu 3b") #in tiêu đề
    plt.legend() #hiện chú thích
    plt.grid() #vẽ lưới cho đồ thị
    plt.show() #hiển thị đồ thị
cau_3b() #gọi câu 3b