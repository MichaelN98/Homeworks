from mammal import Mammal


class FlyingMammals(Mammal):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, num_legs: int, wings: int):
        super().__init__(name, food, type_animal, intelligence, size, num_legs)
        self.wings = wings
        self.food = 'insects'

    def type_of_animal(self):
        return (f'{self.type_animal} is type of animal')

    def fly(self):
        return (f"{self.name} can fly on {self.wings} wings")

    def eat(self):
        return (f'{self.name} eat the {self.food}')

