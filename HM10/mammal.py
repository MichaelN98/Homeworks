from animal import Animal


class Mammal(Animal):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, num_legs: int):
        super().__init__(name, food, type_animal, intelligence, size)
        self.num_legs = num_legs

    def type_of_animal(self):
        return (f'{self.type_animal} is type of animal')

    def walk(self):
        return (f"{self.name} is walking on {self.num_legs} legs.")

    def eat(self):
        return (f'{self.name} eat the {self.food}')
