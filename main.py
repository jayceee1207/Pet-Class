#John Carlo Ablay
#BSCPE 1-5
#July 1, 2023
#Pet Class

#import Pet class
from Pet import Pet

#ask the name of the pet
name = input("Enter your pet's name: ")

#ask the animal type
animal_type = input("Enter what type of pet it is: ")

#ask the age of the animal
age = input("Enter your pet's age: ")

#create an object
pet = Pet(name, animal_type, age)

#display the data
pet.show()