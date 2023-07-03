#John Carlo Ablay
#BSCPE 1-5
#July 1, 2023
#Pet Class

import pyfiglet
import emoji
from Pet import Pet

import pyfiglet
  
result = pyfiglet.figlet_format("PET", font = "isometric1" )
print(result)

author_name = ("Programmed by: John Carlo R. Ablay")
author_name_center = author_name.center(120)
print("\u001b[33;1m",author_name_center)

#ask the name of the pet

name = input('\u001b[37m'"Enter your pet's name: ")

#ask the animal type
animal_type = input("Enter what type of pet it is: ")

#ask the age of the animal
age = input("Enter your pet's age: ")

#create an object
pet = Pet(name, animal_type, age)

#display the data
pet.show()

print("\nThank you for using my program! Have a good day!")
print(emoji.emojize('Have a good day! :grinning_face:'))
print(emoji.emojize(':dog_face:'))
print(emoji.emojize(':cat_face:'))
print(emoji.emojize(':turtle:'))


