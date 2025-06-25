"""
The employee module defines an Employee class with attributes and methods
for managing employee information.
"""

class Employee:
    def __init__(self, name=None, id_number=None, department=None, job_title=None):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__job_title = job_title
    
    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number
    
    def set_department(self, department):
        self.__department = department
    
    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_name(self):
        return self.__name
    
    def get_id_number(self):
        return self.__id_number
    
    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__job_title

    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"ID Number: {self.__id_number}\n"
                f"Department: {self.__department}\n"
                f"Title: {self.__job_title}\n")