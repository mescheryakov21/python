def func_sum_str(str_1):
    list_1 = str_1.split(" ")
    sum_lst = 0
    for i in list_1:
        if i == "%":
            global personal_str
            personal_str = "%"
            return sum_lst
        sum_lst += int(i)
    return sum_lst
itog = 0
personal_str = input("Введите числа через пробел, если хотите остановить сложение введите %: ")
while personal_str != "%":
    itog = itog + func_sum_str(personal_str)
    if personal_str == "%":
        print(itog)
        break
    print(itog)
    personal_str = input("Введите числа через пробел, если хотите остановить сложение введите %: ")