dohod = int(input("Введите, пожалуйста, выручку фирмы в рублях"))
izder = int(input("Введите сумму издержек по предприятию в рублях"))
#sotrud = int(input("Введите количество сотрудников в фирме"))
if dohod > izder:
    print("Фирма работает с прибылью " +str(dohod-izder) +" рублей")
    rent = 1-izder/dohod
    print("Рентабельность фирмы равна"+ str(round(rent, 2)))
    sotrud = int(input("Введите количество сотрудников в фирме"))
    print("Прибыль на одного сотрудника равна " + str(sotrud/(dohod-izder)) + "Рублей")
elif dohod < izder:
    print("Фирма работает с убытком " + str(dohod - izder) + " рублей")
else:
    print("Фирма работает без убытка и без прибыли!")
