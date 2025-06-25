"""
This file defines the pet class
"""

class Pet():
    def __init__(self):
        self.__name = "Unknown"
        self.__animal_type = "Unknown"
        self.__age = 0
    def set_name(self, name):
        if name is None:
            self.__name = input("Pet name: ")
        else: self.__name = str(name)

    def set_animal_type(self, type):
        if type is None:
            self.__animal_type = input("Pet type: ")
        else: self.__animal_type = str(type)
    
    def set_age(self, age):
        if age is None:
            self.__age = int(input("Pet age: "))
        else: self.__age = int(age)
    
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type
    
    def get_age(self):
        return self.__age
    
    def __str__(self):
        return f"Pet Name: {self.__name}, Type: {self.__animal_type}, Age: {self.__age}"