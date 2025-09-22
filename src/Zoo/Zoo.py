from src.Zoo.Animal import Animal


class Zoo:
    def __init__(self, animals):
        self._animals = []
        self.animals = animals

    def add(self, animal):
        if isinstance(animal, Animal):
            self._animals.append(animal)
        else:
            print(animal," n'est pas un animal" )

    @property
    def animals(self):
        return self._animals

    @animals.setter
    def animals(self, animals):
        self._animals = []
        for animal in animals:
            self.add(animal)

    def __add__(self, zoo):
        if isinstance(zoo, Zoo):
            return Zoo(self.animals + zoo.animals)
        return NotImplemented