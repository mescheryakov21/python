from math import factorial
def fact(n):
    for i in range(n + 1):
        yield i
num = int(input("Введите количество выводимых Факториалов: "))
a = fact(num)
for el in a:
    if el > 0:
        print(f'Факториал числа {el} равен {factorial(el)}')




