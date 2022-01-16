class Person:
    """A class to represent a person
    Attributes:
        name: A string to represent the name of the person
        surname: A string to represent the surname of the person
        age: An integer to represent the age of the person
    """

    def __init__(self, name: str, surname: str, age: int):
        """Construct all the necessaries atributes for person
        Args:
            name (str): The name of the person
            surname (str): The surname of the person
            age (int): The age of the person
        """
        self.name = name
        self.surname = surname
        self.age = age

    def info(self, additional: str = ""):
        """Prints the person name and age
        If the argument additional is passed, then it is appended to the end of the main info.
        Args:
            additional (str, optional): Additional info. Defaults to "".
        """
        print(f"My name is {self.name}. I am {self.age} years old." + additional)
