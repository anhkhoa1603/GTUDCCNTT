import sympy as sp

# a
x = sp.symbols('x')
f3_1 = 1 / (1 + 2 ** (1 / 2))
lm = sp.limit(f3_1, x, 0, '-')
print("Gioi han ben trai cua ham so la: " + str(lm))


def f3_b(params):
    return (params ** 2 + params) / (params ** 3 + params ** 2) ** (1 / 2)

# Ủa rồi xuống dưới mình ghi sao, như bình thường à
#  uk
# ohhh
# cứ đặt tên theo chức năng chú làm nhưng bằng tiếng anh nha
# luyện tiếng anh chuyên ngành luôn
# nhưng biến thì em chỉ có thể đặt là x thôi à
# hừmmmmmmmmmm
x = sp.symbols('x')
lm1 = sp.limit(f3_b(x), x, 0, '-')
print("Gioi han ben trai cua ham so la: " + str(lm1))

lm2 = sp.limit(f3_b(x), x, 0, '+')
print("Gioi han ben phai cua ham so la: " + str(lm2))


time = lambda a, b: a - b if a > b else b - a
