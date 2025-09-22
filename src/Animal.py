class Animal:

    def __init__(self, weight, size):
        self.__weight = None
        self.__size = None
        self.set_weight(weight)
        self.set_size(size)

    def move(self):
        pass

    def get_weight(self):
        return self.__weight

    def get_size(self):
        return self.__size

    def set_weight(self, weight):
        if weight < 0:
            raise ValueError
        else :
            self.__weight = weight

    def set_size(self, size):
        if size < 0:
            raise ValueError
        else :
            self.__size = size

    def __str__(self):
        return f"{type(self).__name__} de {self.get_size()}m et de {self.get_weight()}kg"