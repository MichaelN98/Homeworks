from squamata import Squamata


class Python(Squamata):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, legs: bool, scale: bool, length: int):
        super().__init__(name, food, type_animal, intelligence, size, legs, scale)
        self.length = length

    def type_of_animal(self):
        return f'{self.type_animal} is type of animal'

    def eat(self):
        return f'{self.name} eat the {self.food}'

    def spot(self):
        if self.length >= 25:
            print(f"{self.length} it is python")
        elif 25 > self.length > 0:
            print(f"{self.length} another snake")
        elif self.length <= 0:
            raise ValueError(f"{self.length} should have a size")

