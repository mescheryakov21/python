'''
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
 Напишите решения через list и dict.
'''

mes = input("Пожалуйста, введите номер месяца: ")
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
vrem_god_dict = {'Зима': ('1', '2', '12'), 'Весна': ('3', '4', '5'), 'Лето': ('6', '7', '8'), 'Осень': ('9', '10', '11')}
if mes in num_list :
    dict_list = list(vrem_god_dict.keys())
    a = len(dict_list)
    irc = 0
    tmp_key = dict_list[1]
    while irc < a :
        tmp_key = dict_list[irc]
        irc += 1
        tmp_list = vrem_god_dict.setdefault(tmp_key)
        if mes in tmp_list :
            print(tmp_key)
else :
    print('Введите коректный номер месяца')