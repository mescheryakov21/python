'''
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input()
'''
str_base = input('Введите элементы списка через запятую ')
input_list = list(str_base.split(','))
a = len(input_list)
irc = 0
while irc < (a - 1):
    if a == 1 :
        break
    input_list[(irc)], input_list[(irc + 1)] = input_list[(irc + 1)], input_list[irc]
    irc += 2
print(input_list)