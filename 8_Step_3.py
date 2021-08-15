class DigitalError(Exception):
    # def __init__(self, str):
    #     self.str = str
    def __str__(self):
        return f' - Это не число\nВведите число!\n'

class ListAdd:
    list_digit = []
    def list_metod(self, str):
        self.str = str
        try:
            if self.str.isdigit():
                self.list_digit.append(int(self.str))
            else:
                self.list_digit.append(float(self.str))
        except:
            print(DigitalError())

lst_cls = ListAdd()
while True:
    digital = input("Введите число, чтобы остановиться введите stop: ")
    if digital == 'stop':
        break
    else:
        lst_cls.list_metod(digital)
print(lst_cls.list_digit)
