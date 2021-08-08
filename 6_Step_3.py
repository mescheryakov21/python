class Worker:

    def __init__(self, param_1, param_2, param_3, param_4, param_5):
        self.name = param_1
        self.surename = param_2
        self.position = param_3
        self._income = {"Оклад": param_4, 'Премия': param_5}

class Position(Worker):

    def get_full_name(self):
        print(f'Полное имя: {self.name} {self.surename}')

    def get_total_income(self):
        itogo = self._income['Оклад'] + self._income['Премия']
        print(itogo)

a = Position('Владимир', 'Мещеряков', 'Провизор', 20000, 10000)
a.get_full_name()
a.get_total_income()
