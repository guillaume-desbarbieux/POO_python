from src.Zoo.Animal import Animal

class Bird(Animal):
    def __init__(self, weight, size, max_elevation):
        super().__init__(weight, size)
        self.max_elevation = max_elevation

    @property
    def max_elevation(self):
        return self.max_elevation

    @max_elevation.setter
    def max_elevation(self, max_elevation):
        if max_elevation < 0:
            raise ValueError
        else:
            self._max_elevation = max_elevation

    def move(self):
        return "I (believe I can) fly"