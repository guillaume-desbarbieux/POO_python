from src.Zoo.Bird import Bird
from src.Zoo.Snake import Snake
from src.Zoo.Zoo import Zoo

if __name__ == "__main__":
    bird = Bird (1,1, 1)
    snake = Snake(1,1)
    zoo1 = Zoo([snake, bird])

    chicken = Bird(2,2,2)
    boa = Snake(2,2)
    zoo2 = Zoo([chicken, boa])

    print("Zoo1:")
    for animal in zoo1.list():
        print(str(animal))

    print("Zoo2:")
    for animal in zoo2.list():
        print(str(animal))

    zoo3 = zoo1 + zoo2
    print("Zoo3:")
    for animal in zoo3.list():
        print(str(animal))