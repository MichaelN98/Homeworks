from abc import ABC, abstractmethod


# Interface
class IAnimal(ABC):
    @abstractmethod
    def _make_sound(self): ...

    @abstractmethod
    def _move(self): ...

    @abstractmethod
    def _move_to(self, x, y): ...
