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
