from collections import deque

from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        return self._data.popleft()

    def search(self, index):
        if 0 <= index <= (len(self._data) - 1):
            return self._data[index]

        raise IndexError("index out of range")

    def is_empty(self):
        return not len(self._data)
