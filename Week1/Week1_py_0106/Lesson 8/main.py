"""Перегрузка операторов"""


class Snow:
    def __init__(self, value):
        self.snowflakes = value

    def __add__(self, n):
        self.snowflakes += n

    def __sub__(self, n):
        self.snowflakes -= n

    def __mul__(self, n):
        self.snowflakes *= n

    def __truediv__(self, n):
        self.snowflakes = round(self.snowflakes / n)

    def makeSnow(self, num):
        result = ""
        for i in range(self.snowflakes//num):
            result += "*" * num + "\n"
        result += "*" * (self.snowflakes % num)
        return result

    def __call__(self, value):
        self.snowflakes = value


snow = Snow(7)
snow + 3
snow - 2
snow * 4
snow / 2
print(snow.makeSnow(3))

snow(4)
print(snow.snowflakes)
