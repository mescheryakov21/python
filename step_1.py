def func_del():
    param_1 = int(input('Введите делимое: '))
    param_2 = int(input('Введите делитель: '))
    if param_2 != 0:
        return param_1 / param_2
    return 'Делить на ноль нельзя!'
print(func_del())