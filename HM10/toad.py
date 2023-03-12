"""Бесхвостые земноводные"""
from amphibians import Amphibians

class Toad(Amphibians):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, cold_blooded: bool, tail: bool):
        super().__init__(name, food, type_animal, intelligence, size, cold_blooded)
        self.tail = tail

    def type_of_animal(self):
        return f'{self.type_animal} is type of animal'

    def eat(self):
        return f'{self.name} eat the {self.food}'

    def evolution(self):
        if self.tail:
            print(f"{self.name} it is tadpole")
        else:
            print(f"{self.name} it is toad")

