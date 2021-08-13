from abc import ABC, abstractmethod

class Odejda(ABC):

    @abstractmethod
    def material(self):
        pass

class Palto(Odejda):

    def __init__(self, size):
        self.size = size

    @property
    def material(self):
        return self.size / 6.5 + 0.5

class Kostym(Odejda):

    def __init__(self, rost):
        self.rost = rost

    @property
    def material(self):
        return self.rost * 2 + 0.3

h = Kostym(float(input('Введите Рост для костюма: ')))
s = Palto(float(input('Введите Размер для пальто: ')))
print(f'Всего материала необходимо: {round((h.material + s.material), 2)}')

