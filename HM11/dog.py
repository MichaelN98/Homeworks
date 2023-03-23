from abc import ABC

from HM11.activity import IActivity
from HM11.animal import IAnimal


# Inheritance
# Abstraction
class Dog(IAnimal, IActivity):

    def __init__(self, naming):
        self.__dog_name = naming
        self.__dog_activity = True
        self.__x = 0
        self.__y = 0
        self.__z = 0

    @property
    def dog_name(self):
        return self.__dog_name

    @dog_name.setter
    def dog_name(self, new_dog_name):
        self.__dog_name = new_dog_name

    # Polymorphism
    # Hiding
    def _make_sound(self):
        print(f'{self.__dog_name} make sound "gav"')
        self.__dog_activity = True

    # Polymorphism
    # Hiding
    def _move(self):
        self._make_sound()
        print(f'{self.__dog_name} move')
        self.__z = 10
        self.__dog_activity = True

    # Polymorphism
    # Hiding
    def _move_to(self, x, y):
        self._move()
        print(f'{self.__dog_name} run to the point z: {self.__z}')
        self.__x = x
        self.__y = y

    # Encapsulation
    def sniffing_food(self, x, y):
        self._move_to(x, y)
        print(f'Dog sniffing at x: {x} and y: {y}.')
        self._bring_food()

    # Polymorphism
    # Hiding
    def _bring_food(self):
        print('Returning back')
        self.__z = 0
        self.__dog_activity = True
        print('Returning with food.')
        self._calm_down()

    # Polymorphism
    # Hiding
    def _calm_down(self):
        print(f'{self.__dog_name} is not active')
        self.__dog_activity = False

    def stress_trigger(self, x, y, z):
        if z > 50:
            print(f'Somthing wrong! at these coordinates at x: {x} and y: {y} and point z: {z} is danger.')

