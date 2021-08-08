class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью ручки")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью карандаша")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} с помощью маркера")

Stationery("Привет").draw()

p = Pen("Заголовок")
p.draw()

k = Pencil("Обращение")
k.draw()

h = Handle("Выделение")
h.draw()
