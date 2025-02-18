"""Композиция"""
import math


class WinDoor:
    def __init__(self, x, y):
        self.square = x * y


class Room:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.wd = []

    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))

    def work_surface(self):
        new_square = self.square()
        for i in self.wd:
            new_square = new_square - i.square
        return new_square

    def square(self):
        return 2 * self.z * (self.x + self.y)

    def roll_сount(self, x, y):
        return math.ceil(self.work_surface() / (x*y))


r1 = Room(float(input("Введите ширину комнаты: ")),
          float(input("Введите длину комнаты: ")),
          float(input("Введите высоту комнаты: ")))
for i in range(int(input("Введите сумму окон и дверей в комнате: "))):
    r1.add_wd(float(input("Введите ширину окна или двери: ")),
              float(input("Ввдетие длину окна или двери: ")))
print(f"Площадь оклеиваемой поверхности: {r1.work_surface()}")
rolls = r1.roll_сount(float(input("Введите ширину рулона обоев: ")),
                      float(input("Введите длину рулона обоев: ")))
print(f"Необходимое количество рулонов: {rolls}")
