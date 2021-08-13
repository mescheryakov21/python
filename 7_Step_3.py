
class Cito:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        print(
            f'При сложении двух клеток в результирующей получаем количество ячеек равно: {self.count + other.count} !')
        return self.count + other.count

    def __sub__(self, other):
        if self.count < other.count:
            print('Количество ячеек второй клетки не может быть больше чем у первой!')
            return
        print(
            f'При вычитании двух клеток в результирующей получаем количество ячеек равно: {self.count - other.count} !')
        return self.count - other.count

    def __mul__(self, other):
        print(
            f'При умножении двух клеток в результирующей получаем количество ячеек равно: {self.count * other.count} !')
        return self.count * other.count

    def __truediv__(self, other):
        if other.count == 0:
            print("Значение ячеек второй клетки не может равняться 0")
            return
        print(
            f'При делении двух клеток в результирующей получаем количество ячеек равно: {self.count // other.count} !')
        return self.count // other.count

    def make_order(self, argument):  #организация ячеек
        a = self.count // argument
        b = self.count % argument
        c = 0
        while c < a:
            print("*" * argument)
            c += 1
        print("*" * b)
        print()

kletka_1 = Cito(int(input("Введите количество ячеек в первой клетке: ")))
kletka_2 = Cito(int(input("Введите количество ячеек во второй клетке: ")))
kletka_sum = Cito(kletka_1 + kletka_2)
kletka_raz = Cito(kletka_1 - kletka_2)
kletka_multi = Cito(kletka_1 * kletka_2)
kletka_del_zel = Cito(kletka_1 / kletka_2)
in_ryd = int(input("Введите количество ячеек в ряду для мультиклетки: "))
kletka_1.make_order(in_ryd)
kletka_2.make_order(in_ryd)
