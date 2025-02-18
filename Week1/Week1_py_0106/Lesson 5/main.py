"""Полиморфизм"""


class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)


first_point = Point(3, 4)
second_point = Point(5, 5)

first_point = first_point + second_point

print(f"x = {first_point.x}, y = {first_point.y}")
