def my_func_1 (base, stepen):
    return base ** stepen
def my_func_2 (base, stepen):
    while stepen < 0:
        base *= 1/base
        stepen += 1
    return base
x = float(input('Введите, пожалуйста, основание степенной функции: '))
y = float(input('Введите, пожалуйста, показатель отрицательной степени: '))
print(f"По первому варианту:  + {my_func_1(x, y)} ")
print(f"По второму варианту: + {my_func_2(x, y)}")