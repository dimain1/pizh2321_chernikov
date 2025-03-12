# Иерархия классов

Выберите класс под номером №, где № Ваш порядковый номер в журнале.

№8 = №3 - ТранспортноеСредство, ВодноеТС, КолесноеТС, Автомобиль

Методы базового класса - ехать()

Далее:

- выстройте классы в иерархию, продумайте их общие и отличительные характеристики и действия;
- добавьте собственную реализацию методов базового класса в каждый из классов. предусмотрев:
  - необходимые параметры для базовых методов
  - необходимые поля для функционирования базовых методов
  - вывод на экран работы метода
- по желанию добавьте собственные методы в классы иерархии



```PYTHON
# main.py
# Программирование на языке высокого уровня (Python).
# Задание № 04.03.06. Вариант 8
#
# Выполнил: Черников Дмитрий Дмитриевич
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dima.chernikov.053@mail.ru


from transport import WaterTransport, WheeledTransport, Car

if __name__ == "__main__":
    boat = WaterTransport(speed=30, capacity=10, water_type="река")
    bike = WheeledTransport(speed=20, capacity=1, wheels=2)
    car = Car(speed=120, capacity=5, fuel_type="бензин")

    print(boat)
    boat.move()
    boat.stop()

    print("\n" + str(bike))
    bike.move()
    bike.stop()

    print("\n" + str(car))
    car.move()
    car.honk()
    car.stop()
```

```PYTHON
# transport.py
# Программирование на языке высокого уровня (Python).
# Задание № 04.03.06. Вариант 8
#
# Выполнил: Черников Дмитрий Дмитриевич
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dima.chernikov.053@mail.ru
from abc import ABC, abstractmethod


class Transport(ABC):
    """
    An abstract base class to represent a transport.
    """

    def __init__(self, speed: float, capacity: int) -> None:
        """
        Initialize the Transport object with a speed and capacity.

        :param speed: The speed of the transport.
        :param capacity: The capacity of the transport.
        """
        self.speed: float = speed
        self.capacity: int = capacity

    @abstractmethod
    def move(self) -> None:
        """
        Move the transport.
        """
        pass

    def stop(self) -> None:
        """
        Stop the transport.
        """
        print(f"{self.__class__.__name__}: Остановился.")

    def __str__(self) -> str:
        """
        Return the string representation of the transport.

        :return: The string representation of the transport.
        """
        return (f"{self.__class__.__name__}:"
                f"скорость={self.speed}, вместимость={self.capacity}")


class WaterTransport(Transport):
    """
    A class to represent a water transport.
    """

    def __init__(self, speed: float, capacity: int, water_type: str) -> None:
        """
        Initialize the WaterTransport object with a speed,
        capacity, and water type.

        :param speed: The speed of the water transport.
        :param capacity: The capacity of the water transport.
        :param water_type: The type of water the water transport is on.
        """
        super().__init__(speed, capacity)
        self.water_type: str = water_type

    def move(self) -> None:
        """
        Move the water transport.
        """
        print(f"{self.__class__.__name__}: Плывет со скоростью"
              f"{self.speed} узлов по {self.water_type}.")


class WheeledTransport(Transport):
    """
    A class to represent a wheeled transport.
    """

    def __init__(self, speed: float, capacity: int, wheels: int) -> None:
        """
        Initialize the WheeledTransport object with a speed,
        capacity, and number of wheels.

        :param speed: The speed of the wheeled transport.
        :param capacity: The capacity of the wheeled transport.
        :param wheels: The number of wheels of the wheeled transport.
        """
        super().__init__(speed, capacity)
        self.wheels: int = wheels

    def move(self) -> None:
        """
        Move the wheeled transport.
        """
        print(f"{self.__class__.__name__}: Едет со скоростью"
              f"{self.speed} км/ч на {self.wheels} колесах.")


class Car(WheeledTransport):
    """
    A class to represent a car.
    """

    def __init__(self, speed: float, capacity: int, fuel_type: str) -> None:
        """
        Initialize the Car object with a speed, capacity, and fuel type.

        :param speed: The speed of the car.
        :param capacity: The capacity of the car.
        :param fuel_type: The type of fuel the car uses.
        """
        super().__init__(speed, capacity, wheels=4)
        self.fuel_type: str = fuel_type

    def move(self) -> None:
        """
        Move the car.
        """
        print(f"{self.__class__.__name__}: Едет на {self.fuel_type} "
              f"со скоростью {self.speed} км/ч.")

    def honk(self) -> None:
        """
        Honk the car.
        """
        print("Автомобиль: Бип-бип!")
```
При выполнении задания необходимо построить UML-диаграмма классов приложения
<image src="image.png">