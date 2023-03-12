from bird import Bird


class Raven(Bird):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str, num_legs: int, wings: int, hackle: str, color_hackle: int):
        super().__init__(name, food, type_animal, intelligence, size, num_legs, wings, hackle)
        self.color_hackle = color_hackle

    def type_of_animal(self):
        return (f'{self.type_animal} is type of animal')

    def what_color(self):
        return (f'{self.name} has {self.color_hackle} color of {self.hackle}')

    def eat(self):
        return (f'{self.name} eat the {self.food}')

