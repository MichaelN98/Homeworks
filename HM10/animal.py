from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, food: str, type_animal: str, intelligence: str, size: str):
        self.food = food
        self.name = name
        self.type_animal = type_animal
        self.intelligence = intelligence
        self.size = size



    @abstractmethod
    def type_of_animal(self):
        pass

    @abstractmethod
    def eat(self):
        pass

