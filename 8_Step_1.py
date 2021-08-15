
class Data:

    @staticmethod
    def validate_num(list_int):
        if 0 < list_int[0] < 32 and 0 < list_int[1] < 12 and list_int[2] > 0:
            print(f'Дата соответствует формату')
        else:
            print(f'Дата несоответствует формату')

    @classmethod
    def magic(cls, d):
        cls.list = d.split('-')
        new_list = []
        if len(cls.list) == 3:
            new_list = [int(el) for el in cls.list if el.isdigit()]
            print(new_list)
        else:
            print(f"Дата не коректна!")
            return None
        return new_list if len(new_list) == 3 else None

d = "20-03-87"
a = Data()
list_num = Data.magic(d)
if list_num != None:
    a.validate_num(list_num)
else:
    print(f'Дата несоответствует формату')
