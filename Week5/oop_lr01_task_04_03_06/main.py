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
