class Any_company:
    """A class that describes a company"""

    def __init__(self, name, age, budget):
        """
        Initializes a company instance with the given name, age, budget.

        Parameters
        ----------
        name : str
            The name of the company
        age : int
            The age of the company
         budget : int
            The  budget of  the company
        """
        self.__name = name
        self.__age = age
        self.__budget =  budget

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
        if len(name) >= 3:
            self.__name = name
        else:
            raise ValueError("Name should have at least 3 characters.")

    @property
    def age(self):
        """
        Get the age of the company
        """
        return self.__age

    @age.setter
    def age(self, value):
        """
        Set the agw of the company

         Parameters
         ----------
         age : int
         The age of the company with that conditions
        """
        if not isinstance(value, int):
            raise ValueError("age of the company must be an integer")
        if value < 0:
            raise ValueError("age of the company cannot be negative")
        if value > 100:
            raise ValueError("age of the company cannot be greater than 100")
        self.__age = value

    @property
    def  budget(self):
        """
        Get the  budget of the company
        """
        return self.__budget

    @ budget.setter
    def  startup(self,  budget):
        """
        Set the  budget of the company

         Parameters
         ----------
          budget : int
         The  budget of the company with that conditions
        """
        if not isinstance( budget, int):
            raise ValueError(" budget must be an integer")
        if  budget <= 0:
            raise ValueError(" budget cannot be negative")
        if  budget < 10000:
            print(f'{ budget} is a startup')
        if  budget >= 10000:
            print(f'{ budget} is a business')

    @staticmethod
    def bonus_of_timework(years_of_work):
        """
        Add bonus for work in the company
        Parameters
         ----------
         bonus : int
        """
        return years_of_work * 0.5
