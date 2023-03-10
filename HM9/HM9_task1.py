class AnyCompany:

    def __init__(self, name: str, age: int, budget: int, type_of_work: str):
        self.__name = name
        self.__age = age
        self.__budget = budget
        self.__type_of_work = type_of_work

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, name):

        if len(str(name)) >= 3:
            self.__name = name
        else:
            raise ValueError("Name should have at least 3 characters.")

    @property
    def age(self):

        return self.__age

    @age.setter
    def age(self, value):

        if not isinstance(value, int):
            raise ValueError("age of the company must be an integer")
        if value < 0:
            raise ValueError("age of the company cannot be negative")
        if value > 100:
            raise ValueError("age of the company cannot be greater than 100")
        self.__age = value

    @property
    def budget(self):

        return self.__budget

    @ budget.setter
    def budget(self, budget):

        if not isinstance(budget, int):
            raise ValueError(" budget must be an integer")
        elif budget <= 0:
            raise ValueError(" budget cannot be negative")
        elif budget < 10000:
            print(f'{budget} is a startup')
        elif budget >= 10000:
            print(f'{budget} is a business')
        self.__budget = budget

    @staticmethod
    def bonus_of_timework(years_of_work):

        return years_of_work * 0.5

    @classmethod
    def create_company_name_budget(cls, name, budget):
        return cls(name, budget)

    def show_name(self):
        print(self.__name, 'is name of the company')

    def type_of_work(self):
        return self.__type_of_work
