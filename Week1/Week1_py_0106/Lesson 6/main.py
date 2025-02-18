"""Инкапсуляция"""


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y


point = Point(5, 7)
print(f"x = {point.getX()}, y = {point.getY()}")
point.setX(1)
point.setY(2)
print(f"x = {point.getX()}, y = {point.getY()}")
