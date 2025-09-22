from src.Animal import Animal


class Zoo:
    def __init__(self, list_animals):
        self.__list_animals = []
        for animal in list_animals:
            self.add(animal)

    def add(self, animal):
        if isinstance(animal, Animal):
            self.__list_animals.append(animal)
        else:
            print(animal," n'est pas un animal" )

    def list(self):
        return self.__list_animals

    def __add__(self, zoo):
        return Zoo(self.list() + zoo.list())
