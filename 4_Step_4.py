list_ishod = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
list_new = [el for el in list_ishod if list_ishod.count(el) < 2]
print(list_new)