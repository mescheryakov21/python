sum_sek = int(input("Введите, пожалуйста время в секундах: "))
chas = sum_sek // 3600
minut  = (sum_sek // 60) % 60
sek = sum_sek % 60
print(str(chas) +" часов " + str(minut) + " минут " + str(sek) + " секунд")