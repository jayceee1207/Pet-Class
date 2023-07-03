#Create a class
class Pet:

#init attributes
    def __init__(self, name, animal_type, age):
        self.__name =  name
        self.__animal_type = animal_type
        self.__age = age

#show result: name, type, and age
    def show(self):
            print("\n\n'\033[96m'*****'\033[37m'PET's INFO'\033[96m'*****\033[37m'")
            print('\033[92m'"Name:", self.__name, '\033[37m' ,'\033[92m' "\nType:", self.__animal_type, '\033[37m', '\033[92m' "\nAge:", self.__age, '\033[37m')
#Setter method
    def set_name(self):
        return self.__name
    
    def set_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

#Getter method
    def get_name(self):
        return self.__name
    
    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age