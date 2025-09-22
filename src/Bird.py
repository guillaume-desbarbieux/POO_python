from src.Animal import Animal

class Bird(Animal):
    def __init__(self, weight, size, max_elevation):
        super().__init__(weight, size)
        self.__max_elevation = max_elevation


    def move(self):
        return "I (believe I can) fly"