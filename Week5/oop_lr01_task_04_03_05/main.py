# main.py
# Программирование на языке высокого уровня (Python).
# Задание № 04.03.05. Вариант 8
#
# Выполнил: Черников Дмитрий Дмитриевич
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dima.chernikov.053@mail.ru

from queueCollection import QueueCollection
from my_queue import Queue

if __name__ == "__main__":

    collection = QueueCollection()

    queue1 = Queue()
    queue1.enqueue(1)
    queue1.enqueue(2)
    queue1.enqueue(3)
    collection.add(queue1)

    queue2 = Queue()
    queue2.enqueue(4)
    queue2.enqueue(5)
    collection.add(queue2)

    print(collection)

    print("Queue at index 0:", collection[0])

    collection.remove(0)
    print("After removing index 0:", collection)

    collection.save("queues.json")

    new_collection = QueueCollection()
    new_collection.load("queues.json")
    print("Loaded collection:", new_collection)
