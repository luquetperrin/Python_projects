# Write a program which select a random name 
# from a list of names and the person selected 
# has to pay for everybody's food bill.

import random

names = input("Enter everybody's name separated by comma: \n")
list_of_names = names.split(",")

# First method
#person_selected = random.choice(list_of_names)
#print(f"{chosen_person} will pay for everybody's food bill")

# Second method 
length = len(list_of_names)
random_choice = random.randint(0, length -1)
print(f"{list_of_names[random_choice]} will pay for everybody's food bill")
