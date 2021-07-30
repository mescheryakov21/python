from sys import argv
name_script, chas, tarif, premia = argv
zarplata = int(chas) * int(tarif) + int(premia)
print(f'Ваша зарплата составляет: {zarplata} рублей')

