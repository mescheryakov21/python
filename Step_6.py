day_one = float(input("Введите,пожалуйста, сколько киллометров пробежали сегодня"))
#print(day_one)
zell = float(input("Какая у Вас цель,в киллометрах?"))
day_itog = 1
while zell > day_one:
    day_one = day_one * 1.1
    day_itog = day_itog + 1
print("На " + str(day_itog) + " день Вы достигнете результата — не менее " + str(zell) + "км.")


