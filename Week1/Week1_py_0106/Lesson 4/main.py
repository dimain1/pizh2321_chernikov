"""Наследование"""
from random import randint


class instance:
    def __init__(self, id, team):
        self.id = id
        self.team = team


class Solider(instance):
    def follow_the_hero(self, hero):
        self.hero = hero


class Hero(instance):
    level = 1

    def level_up(self):
        self.level += 1


first_hero = Hero(1, "Red")
second_hero = Hero(2, "Blue")

red_soliders = []
blue_soliders = []
id_counter = 3

for i in range(10):
    num = randint(1, 2)
    if num == 1:
        red_soliders.append(Solider(id_counter, "Red"))
    else:
        blue_soliders.append(Solider(id_counter, "Blue"))
    id_counter += 1

print(f"Количество солдат красной команды: {red_soliders.__len__()}")
print(f"Количество солдат красной команды: {blue_soliders.__len__()}")

if red_soliders.__len__() > blue_soliders.__len__():
    first_hero.level_up()
elif red_soliders.__len__() < blue_soliders.__len__():
    second_hero.level_up()

red_soliders[0].follow_the_hero(first_hero)
print(f"Идентификационный номер солдата: {red_soliders[0].id}")
print(f"Идентификационный номер солдата: {first_hero.id}")
