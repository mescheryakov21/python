numer = int(input("Введите, пожалуйста, целое  положительное число: "))
num_const = 1
if numer > 9:
    while numer // 10 > 0 :
        numer_ost = numer % 10
        numer = numer // 10
        if numer_ost > num_const:
            num_const = numer_ost
    print('Самая максимальная цифра в данном числе ' + str(num_const))
else:
    print('Самая максимальная цифра в данном числе ' + str(numer))
