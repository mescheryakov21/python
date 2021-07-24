'''*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
  В кортеже должно быть два элемента — номер товара и словарь с параметрами,
   то есть характеристиками товара: название, цена, количество, единица измерения.
    Структуру нужно сформировать программно, запросив все данные у пользователя.
     Пример готовой структуры:
[ (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
  например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
Пример: { “название”: [“компьютер”, “принтер”, “сканер”], “цена”: [20000, 6000, 2000], “количество”: [5, 2, 7], “ед”: [“шт.”] }
'''
kol_tovarov = int(input("Введите, пожалуйста, количество товаров: "))
irc = 1
my_list = []
while irc <= kol_tovarov:
    dict_tmp = {'название' : input('Введите, пожалуйста, название товара номер ' + str(irc) + ": "),
                'цена' : input('Введите, пожалуйста, цену товара номер ' + str(irc) + ": "),
                'количество' : input('Введите, пожалуйста, количество товара номер ' + str(irc) + ": "),
                'ед.' : input('Введите, пожалуйста, единицы измерения товара номер ' + str(irc) + ": ")}
    korteg = ((irc), dict_tmp)
    my_list.append(korteg)
    irc += 1
irc = 0
list_name = []
list_price = []
list_kol = []
list_ed = []
while irc < kol_tovarov:
    a = dict((my_list[irc])[1])
    list_name.append(a.get("название"))
    list_price.append(a.get("цена"))
    list_kol.append(a.get("количество"))
    list_ed.append(a.get("ед."))
    irc += 1
itog = {"название" : list_name,"цена" : list_price, "количество" : list_kol, "ед." : list_ed}
print(itog)