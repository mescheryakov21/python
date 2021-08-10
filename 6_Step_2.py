class Road:
    _length = 0
    _width = 0
    def __init__(self, param_l, param_w):
        Road._length = param_l
        Road._width = param_w
    def asfalt(self):
        fit = int(input("Какова толщина слоя асфальта:\n"))
        return Road._length * Road._width * fit * 25

length = int(input("Введите длину дороги: "))
width = int(input("Введите ширину дороги: "))
way = Road(length, width)
sque = way.asfalt()
print(f"Всего масса асфальта равна {sque}кг")
