class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f'{self.name} цвета {self.color   }, развивает скорость {self.speed}, является полицейской {self.is_police}')

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, param):
        print(f"Машина повернула на {param}!")

    def show_speed(self):
        print(f"Текущая скорость авто {self.speed}")

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Скорость превышена')
        else:
            super().show_speed()

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Скорость превышена')
        else:
            super().show_speed()

class PoliceCar(Car):
    pass

t = TownCar(60, "green", "Приора", False)
t.go()
t.stop()
t.turn("лево")
t.show_speed()

s = SportCar(100, "black", "Веста", False)
s.go()
s.stop()
s.turn("право")
s.show_speed()

w = WorkCar(45, "white", "Калина", False)
w.go()
w.stop()
w.turn("лево")
w.show_speed()

p = PoliceCar(80, "red", "Волга", True)
p.go()
p.stop()
p.turn("лево")
p.show_speed()
