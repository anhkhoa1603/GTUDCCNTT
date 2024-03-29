import numpy as np  #khai báo thư viện
import sympy as sp  #khai báo thư viện
import matplotlib.pyplot as plt  #khai báo thư viện

A = 459
B = 1
fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa hàm f(x) bằng hàm ẩn danh
gx = lambda x: -A * x**2 + A**2 * x + A #định nghĩa hàm g(x) bằng hàm ẩn danh

def cau_1a():
    print("Câu 1a:")
    print("f(0) = " + str(fx(0))) #giá thị của f(x) khi x bằng 0
    print("f(1) = " + str(fx(1))) #giá thị của f(x) khi x bằng 1
    print("f(A) = " + str(fx(A))) #giá thị của f(x) khi x bằng A

def cau_1b():
    print("Câu 1b:")
    print("g(0) = " + str(gx(0))) #giá thị của g(x) khi x bằng 0
    print("g(1) = " + str(gx(1))) #giá thị của g(x) khi x bằng 1
    print("g(A) = " + str(gx(A))) #giá thị của g(x) khi x bằng A

def cau_1c():
    fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa hàm f(x) bằng hàm ẩn danh
    gx = lambda x: -A * x**2 + A**2 * x + A #định nghĩa hàm g(x) bằng hàm ẩn danh
    x = np.arange(-100, 300, dtype=np.float) #Khởi tạo mảng của x từ -100 tới 300 với bước nhảy là 1
    plt.plot(x, fx(x), color = 'b', label="fx") #vẽ đồ thị của fx
    plt.plot(x, gx(x), color = 'g', label="gx") #vẽ đồ thị của gx

    plt.title("Câu 1c") #tiêu đề
    plt.legend() #hiện chú thích
    plt.grid() #vẽ lưới cho dồ thị
    plt.show() #hiển thị dồ thị

def cau_1d():
    x = np.arange(-10, 10.1, 0.1)
    fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa hàm f(x) bằng hàm ẩn danh

    y = list( map( fx, x)) #tạo trục tung thêo từng giá trị x của fx
    y_keo_dan = list( map( fx, x / (B + 2))) #tạo trục tung thêo từng giá trị x của fx bị kéo dãn

    plt.plot(x,y,label="Đồ thị ban đầu") #vẽ đồ thị fx
    plt.plot(x,y_keo_dan,label="Đồ thị kéo giãn") #vẽ đồ thị fx bị kéo dãn

    plt.title("câu 1d") #hiện tiêu đề
    plt.legend() #hiện chú thích
    plt.show() #hiển thị dồ thị

def cau_1e():
    fx = lambda x: A * x**2 - 2 * A * x + A #định nghĩa hàm f(x) bằng hàm ẩn danh
    gx = lambda x: -A * x**2 + A**2 * x + A #định nghĩa hàm g(x) bằng hàm ẩn danh
    x = np.arange(-100, 300, 1, dtype=np.float) #Khởi tạo mảng của x từ -100 tới 300 với bước nhảy là 1
    plt.plot(x, fx(x), color = 'k', label="fx ") #vẽ đồ thị của fx
    plt.plot(x, gx(x), color = 'y', label="gx ") #vẽ đồ thị của gx

    x = sp.symbols('x') #tạo biến x là 1 hàm biểu tượng
    fx = A * x**2 - 2 * A * x + A #khai báo phương trình fx
    gx = -A * x**2 + A**2 * x + A #khai báo phương trình gx

    x_root = sp.solve(fx - gx) #giải phương trình fx - gx tìm nghiệm

    y_root0 = fx.subs(x, x_root[0]) #thay nghiệm x1 vào phương trình fx
    y_root1 = fx.subs(x, x_root[1]) #thay nghiệm x2 vào phương trình gx

    print("Toạ độ X1:(",x_root[0],",",y_root0,")") #in ra toạ độ của x1
    print("Toạ độ X2:(",x_root[1],",",y_root1,")") #in ra toạ độ của x2

    plt.plot(x_root[0], y_root0, 'ro') #vẽ giao điểm thứ nhất
    plt.plot(x_root[1], y_root1, 'ro') #vẽ giao điểm thứ hai

    plt.title("Câu 1e") #in tiêu đề
    plt.legend() #hiện chú thích
    plt.grid() #vẽ lưới cho đồ thị
    plt.show() #hiển thị đồ thị


cau_1a() #gọi câu a
print("\n") #xuống dòng
cau_1b() #gọi câu b
print("\n") #xuống dòng
cau_1c() #gọi câu c
cau_1d() #gọi câu d
print("Câu e") #in "Câu e"
cau_1e() # gọi câu e