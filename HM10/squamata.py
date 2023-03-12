"""Чешу́йчатые"""

from reptiles import Reptiles


class Squamata(Reptiles):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, legs: bool, scale: bool):
        super().__init__(name, food, type_animal, intelligence, size, legs)
        self.scale = scale

    def type_of_animal(self):
        return f'{self.type_animal} is type of animal'

    def eat(self):
        return f'{self.name} eat the {self.food}'

    def armour(self):
        if self.scale:
            print(f"{self.name} it is scaly")
        else:
            print(f"{self.name} another reptiles")

