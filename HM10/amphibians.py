
from animal import Animal


class Amphibians(Animal):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, cold_blooded: bool):
        super().__init__(name, food, type_animal, intelligence, size)
        self.cold_blooded = cold_blooded

    def type_of_animal(self):
        return f'{self.type_animal} is type of animal'

    def eat(self):
        return f'{self.name} eat the {self.food}'

    def blood(self):
        if self.cold_blooded:
            print(f"{self.name} it is amphibians")
        else:
            print(f"{self.name} another animal")

