# Using the inbuilt property function with the @decorator syntax.
# It allows us to define getters & setters, thereby controlling access & modification of private variables,
# but still access them like regular variables, in a concise and readable manner.

class Animal:
    def __init__(self, age):
        self.__age = age  # Private variable age

    @property  # Property-getter via @decorator syntax
    def age(self):
        return self.__age

    @age.setter  # Property-setter via @decorator syntax
    def age(self, new_age):  # The method names should always be same as the attribute name : age in this case
        if isinstance(new_age, int):  # Validation check
            self.__age = new_age
        else:
            raise TypeError("Animal age must be an integer")


leo = Animal(2)
print(leo.age)  # Accessing the private variable like regular

leo.age = 4  # Modifying the private variable like regular
print(leo.age)

leo.age = "old"
print(leo.age)  # Still raises Type Error as required
