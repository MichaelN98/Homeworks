from abc import ABC, abstractmethod


# Interface
class IActivity(ABC):

    @abstractmethod
    def sniffing_food(self, x, y): ...

    @abstractmethod
    def _bring_food(self): ...

    @abstractmethod
    def _calm_down(self): ...
