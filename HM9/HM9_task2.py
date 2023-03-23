class Worker:

    def __init__(self, name: str, age: int, salary: int, type_work: str):

        self.__name = name
        self.__age = age
        self.__salary = salary
        self.type_work = type_work
    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, name: str):

        if len(str(name)) >= 2:
            self.__name = name
        else:
            raise ValueError("Name should have at least 2 characters.")

    @property
    def age(self):

        return self.__age

    @age.setter
    def age(self, age: int):

        if not isinstance(age, int):
            raise ValueError("age of the worker must be an integer")
        elif age < 0:
            raise ValueError("age of the worker cannot be negative")
        elif age >= 0 and age < 18:
            raise ValueError("age of the worker cannot be less 18")
        elif age >= 18 and age <= 30:
            print('junior specialist')
        elif age > 30 and age <= 50:
            print('middle specialist')
        elif age > 50 and age <= 70:
            print('senior specialist')
        elif age > 70:
            print('pencion')
        self.__age = age

    @property
    def salary(self):

        return self.__salary

    @salary.setter
    def salary(self, salary: int):

        if salary <= 1000:
            print(f'{salary} is small salary')
        elif salary >= 1000 and salary <= 2000:
            print(f'{salary} is good salary')
        elif salary > 2000:
            print(f'{salary} is big salary')
        self.__salary = salary

    @staticmethod
    def time_work(years_of_work: int):

        if years_of_work > 8:
            return years_of_work * 0.5

    def what_level(self) :
        return self.age * self.salary
