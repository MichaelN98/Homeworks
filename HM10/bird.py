from flyingmammals import FlyingMammals


class Bird(FlyingMammals):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, num_legs: int, wings: int, hackle: str):
        super().__init__(name, food, type_animal, intelligence, size, num_legs, wings)
        self.hackle = hackle
    def type_of_animal(self):
        return (f'{self.type_animal} is type of animal')

    def clean_hackle(self):
        return (f'{self.name} clean his {self.hackle}')

    def eat(self):
        return (f'{self.name} eat the {self.food}')

