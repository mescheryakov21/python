
class OneError(Exception):
    def __str__(self):
        return f'Делить на ноль нельзя!'

delimoe = float(input("Введите Делимое: "))
delitel = float(input("Введите Делитель: "))
try:
   print(round(delimoe / delitel, 2))
except:
    print(OneError())

