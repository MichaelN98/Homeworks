class Worker:
    """A class that describes a worker"""

    def __init__(self, name, age, salary):
        """
        Initializes a company instance with the given name, age and salary.

        Parameters
        ----------
        name : str
            The name of the company
        age : int
            The age of  the worker is in
        salary : int
            The salary of worker at the company
        """
        self.__name = name
        self.__age = age
        self.__salary = salary

    @property
    def name(self):
        """
        Get the name of the company
        """
        return self.__name

    @name.setter
    def name(self, name):
        """
        Set the name of the company

         Parameters
         ----------
         name : str
         The name of the company with that conditions
        """
        if len(name) >= 2:
            self.__name = name
        else:
            raise ValueError("Name should have at least 2 characters.")

    @property
    def age(self):
        """
        Get the age of the worker
        """
        return self.__age

    @age.setter
    def age(self, age):
        """
        Set the agw of the company

         Parameters
         ----------
         age : int
         The age of the worker with that conditions
        """
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
        """
        Get the salary of the worker
        """
        return self.__salary

    @salary.setter
    def salary(self, salary):
        """
        Set the salary of the worker

         Parameters
         ----------
        salary : int
         The the salary of the workers with that conditions
        """
        if salary <= 1000:
            print(f'{salary} is small salary')
        if salary >= 1000 and salary <= 2000:
            print(f'{salary} is good salary')
        if salary > 2000 :
            print(f'{salary} is big salary')

    @staticmethod
    def time_work(years_of_work):
        """
        Add bonus for work in the company if worked more 8 years
        Parameters
         ----------
         years_of_work : int
        """
        if years_of_work > 8:
            return years_of_work * 0.5
