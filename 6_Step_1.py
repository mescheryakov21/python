class TrafficLight:
    colors = ('red', 'yellow', 'green')
    time_show = (7, 2, 3)
    def running(self, vari):
        while True:
            if vari < 3:
                self.__color = TrafficLight.colors[vari]
                print(self.__color)
                sleep(TrafficLight.time_show[vari])
                vari += 1
            else:
                vari = 0

from time import sleep

a = TrafficLight()
b = int(input('Введите с какого цвета начинать: \n 0 - c красного \n 1 - c желтого \n 2 - c зеленого \n'))
if 0 <= b < 3:
    a.running(b)
else:
    print("Параметры не верны")
