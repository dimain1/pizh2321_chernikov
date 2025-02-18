"""Конструктор класса - метод __init__()"""


class Person:
    def __init__(self, name, second_name, qualification=1):
        self.name = name
        self.second_name = second_name
        self.qualification = qualification

    def info(self):
        print(f"Имя: {self.name}, Фамилия: {self.second_name}, "
              f"Квалификация:{self.qualification}")

    def __del__(self):
        print(f"До свидания мистер {self.name} {self.second_name}")


first_person = Person("Ivan", "Ivanov", 3)
second_person = Person("Petr", "Petrov", 2)
third_person = Person("Oleg", "Olegov")

first_person.info()
second_person.info()
third_person.info()
del third_person
input()

