class ComplexNum:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other.num

    def __mul__(self, other):
        return self.num * other.num

try:
    num_one = complex(input("Введите комплексное число 1: "))
    num_too = complex(input("Введите комплексное число 2: "))
except:
    print("Вы ввели не комплексные числа")
else:
    a = ComplexNum(num_one)
    b = ComplexNum(num_too)
    print(a + b)
    print(a * b)

