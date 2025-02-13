# Урок 2. Создание классов и объектов.
## Практическая работа
Напишите программу по следующему описанию. Есть класс "Воин". От него создаются два экземпляра-юнита. Каждому устанавливается здоровье в 100 очков. В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, какой юнит атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
```PYTHON 
from random import randint

class Warrior:
   health: int = 0

    def attack(self):
       self.health -= 20

    def setHealth(self, value):
        self.health = value


first_warrior = Warrior()
second_warrior = Warrior()
first_warrior.setHealth(100)
second_warrior.setHealth(100)

while first_warrior.health > 0 and second_warrior.health > 0:
    step = randint(1, 2)
    if step == 1:
        second_warrior.attack()
        print("Атаковал первый")
        print(f"Здоровье противника: {second_warrior.health}")
    else:
        first_warrior.attack()
        print("Атаковал второй")
        print(f"Здоровье противника: {first_warrior.health}")

if first_warrior.health == 0:
   print("Победил второй воин")
else:
    print("Победил первый воин")
```
