#Create a class
class Pet:

#init attributes
    def __init__(self, name, animal_type, age):
        self.__name =  name
        self.__animal_type = animal_type
        self.__age = age

#show result: name, type, and age
    
#Include the data attributes

#Setter method
    def set_name(self):
        return self.__name
    def set_type(self, animal_type):
        self.__animal_type = animal_type

#Getter method
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal_type
