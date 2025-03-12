# Класс-контейнер

Создайте класс-контейнер, который будет содержать набор объектов из предыдущей задачи.

№8 - Queue - Очередь -> QueueCollection - Коллекция очередей

Для класса-контейнера предусмотрите:
- специальные методы:
  - `__init__(self, ...)` - инициализация с необходимыми параметрами;
  - `__str__(self)` - представление объекта удобным для человека виде;
  - `__getitem__()` - индексация и срез для класса-контейнера
- поля, методы, свойства:
  - поле `_data` - содержит набор данных;
  - метод `add(self, value)` - добавляет элемент value в контейнер;
  - метод `remove(self, index)` - удаляет элемент из контейнера по индексу index;
  - метод `save(self, filename)` - сохраняет объект в JSON-файл filename;
  - метод `load(self, filename)` - загружает объект из JSON-файл filename;

```PYTHON
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
```

```PYTHON
# queue.py
# Программирование на языке высокого уровня (Python).
# Задание № 04.03.03. Вариант 8
#
# Выполнил: Черников Дмитрий Дмитриевич
# Группа: ПИЖ-б-о-23-2(1)
# E-mail: dima.chernikov.053@mail.ru
import json
from typing import List


class Queue:
    """
    A class to represent a queue.
    """

    def __init__(self) -> None:
        """
        Initialize the Queue object with an empty list of items.
        """
        self.items: List[int] = []

    def __str__(self) -> str:
        """
        Return the string representation of the queue.

        :return: The string representation of the queue.
        """
        return "Queue: " + str(self.items)

    def enqueue(self, item: int) -> None:
        """
        Add an item to the end of the queue.

        :param item: The item to be added.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the first item from the queue.

        :return: The first item from the queue.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        :return: True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self) -> int:
        """
        Return the size of the queue.

        :return: The size of the queue.
        """
        return len(self.items)

    @classmethod
    def from_string(cls, str_value: str) -> "Queue":
        """
        Create a queue from a string.

        :param str_value: The string representation of the queue.
        :return: The created queue.
        """
        items = json.loads(str_value)
        queue = cls()
        queue.items = items
        return queue

    def save(self, filename: str) -> None:
        """
        Save the queue to a file.

        :param filename: The name of the file to save the queue to.
        """
        with open(filename, 'w') as f:
            json.dump(self.items, f)

    def load(self, filename: str) -> None:
        """
        Load the queue from a file.

        :param filename: The name of the file to load the queue from.
        """
        with open(filename, 'r') as f:
            self.items = json.load(f)

    def reverse(self) -> None:
        """
        Reverse the order of the items in the queue.
        """
        self.items.reverse()

    def __add__(self, other: 'Queue') -> 'Queue':
        """
        Add two queues together.

        :param other: The other queue to be added.
        :return: The new queue.
        """
        new_queue = Queue()
        new_queue.items = self.items + other.items
        return new_queue
```

```PYTHON
#queueCollection.py
import json
from typing import List
from my_queue import Queue


class QueueCollection:
    """
    A container class for storing multiple Queue objects.
    """

    def __init__(self) -> None:
        """
        Initialize the QueueCollection object
        with an empty list of Queue objects.
        """
        self._data: List[Queue] = []

    def __str__(self) -> str:
        """
        Return the string representation of the queue collection.
        """
        return "QueueCollection: " + str([str(queue) for queue in self._data])

    def __getitem__(self, index: int) -> Queue:
        """
        Get the queue at the specified index.
        """
        return self._data[index]

    def add(self, value: Queue) -> None:
        """
        Add a Queue object to the collection.
        """
        self._data.append(value)

    def remove(self, index: int) -> None:
        """
        Remove a Queue object from the collection by index.
        """
        if 0 <= index < len(self._data):
            del self._data[index]

    def save(self, filename: str) -> None:
        """
        Save the collection to a JSON file.
        """
        with open(filename, 'w') as f:
            json.dump([queue.items for queue in self._data], f)

    def load(self, filename: str) -> None:
        """
        Load the collection from a JSON file.
        """
        with open(filename, 'r') as f:
            data = json.load(f)
            self._data = [Queue.from_string(json.dumps(queue_items))
                          for queue_items in data]

```
При выполнении задания необходимо построить UML-диаграмма классов приложения
<image src="image.png">