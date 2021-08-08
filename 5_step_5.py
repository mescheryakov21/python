with open('Practic_5.txt', 'w') as file_num:
    stroka = 0
    while stroka != '':
        stroka = input("Введите числа через пробел: ")
        file_num.write(stroka + ' ')

with open('Practic_5.txt', 'r') as file_num:
    list_num = (file_num.read()).split()
    sum_list = 0
    for elem in list_num:
        sum_list += int(elem)
    print(sum_list)
