from animal import Animal


class Reptiles(Animal):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, legs: bool):
        super().__init__(name, food, type_animal, intelligence, size)
        # self.name = name
        # self.food = food
        # self.type_animal = type_animal
        self.legs = legs

    def type_of_animal(self):
        return f'{self.type_animal} is type of animal'

    def eat(self):
        return f'{self.name} eat the {self.food}'

    def move(self):
        if self.legs:
            print(f"{self.name} crawling on the ground")
        else:
            print(f"{self.name} crawl")

