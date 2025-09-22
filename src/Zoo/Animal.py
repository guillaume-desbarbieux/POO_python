import abc
from abc import ABC


class Animal(ABC):

    def __init__(self, weight, size):
        self.weight = weight
        self.size = size

    @abc.abstractmethod
    def move(self):
        pass

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if weight < 0:
            raise ValueError
        else:
            self._weight = weight

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError
        else :
            self._size = size

    def __str__(self):
        return f"{type(self).__name__} de {self.size}m et de {self.weight}kg"