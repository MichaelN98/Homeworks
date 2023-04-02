class Dog:

    def __init__(self, age: int):
        self.age = age

    def __str__(self):
        return f'{self.__class__.__name__}: \n \t {self.__dict__}'
