#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
    #print(magician.title() + ", that was a great trick!")
    #print("I can't wait to see your next trick, " + magician.title() + "\n")
#print("Thank you, everyone. that was a great magic show!")

#squares =[]

#for value in range (1, 11):
    #square = value ** 2
    #squares.append(square)
#print(squares)

# Creating a Dictionary
#alien_o ={'color': 'green', 'points': 5}

#print(alien_o)
#print(type(alien_o))
#print(alien_o['color'])
#print(alien_o['points'])
#alien_o['x_position'] = 0
#alien_o['y_position'] = 25
#new_points = alien_o['points']
#print("You just earned " + str(new_points) + " points!")
#print(alien_o)
#print("\n")

# Starting with an Empty Dictionary
alien_1 ={}
alien_1['color'] = 'yellow'
alien_1['points'] = 10
#print(alien_1)

# Modifying Values in a Dictionary
# Let's consider an alien changing from yellow to red as a game progresses.
alien_2 = {'color': 'yellow', 'points': 15}
#print("The alien_2 is " + alien_2['color'] + ".")
alien_2['color'] = 'red'
#print("The alien_2 is now " + alien_2['color'] + ".")

# Let's track the position of an alien that can move at different speeds.
alien_3 = {'color': 'black', 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print("Original x_position: " + str(alien_3['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_3['speed'] == 'low':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new alien's position is the old position plus the increment.
alien_3['x_position'] = alien_3['x_position'] + x_increment
#print("New x_position: " + str(alien_3['x_position']))

# Removing Key-Value Pairs
alien_4 = {'color': 'pink', 'points': 5, 'speed': 'low'}
#print(alien_4)
del alien_4['points']
#print(alien_4)

# A Dictionary of Similar Objects
favorite_languages = {
    'perrin': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'franck': 'c++',
    'yves': 'java'
}
#print("Sarah's favorite language is " + 
      #favorite_languages['sarah'].title() + 
      #".")


# Glossary of programming terms
glossary = {
    "variable": "A named storage location that holds data.",
    "integer": "A whole number, positive, negative, or zero.",
    "float": "A number with a decimal point.",
    "string": "A sequence of characters enclosed in quotes.",
    "function": "A block of reusable code that performs a specific task."
}

# Print each word and its meaning
#for word, meaning in glossary.items():
    #print(word + ":")
    #print("\t" + meaning + "\n")

# Favorite numbers
favorite_numbers = {
    "Alice": 7,
    "Bob": 13,
    "Charlie": 21,
    "David": 5,
    "Eve": 8
}

# Print each person's name and their favorite number
#for name, number in favorite_numbers.items():
    # print(name + "'s favorite number is " + str(number))

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
 #for key, value in user_0.items():
    #print("\nKey: " + key)
    #print("Value: " + value)
     #print(key + ":")
     #print("\t" + value + "\n")

 #for name, language in favorite_languages.items():
     #print(name.title() + 
           #"'s favorite language is " + 
           #language.title() + ".")
    

    
# Looping Through All the Keys in a Dictionary
"""The keys() method is useful when you don’t need to 
work with all of the values in a dictionary"""
 #print("\n")
 #for name in favorite_languages.keys():
     #print(name.title())
 #print("\n")

#favorite_languages = {
    #'perrin': 'python',
    #'sarah': 'c',
     #'edward': 'ruby',
     #'franck': 'c++',
     #'yves': 'java'
 #}

 #friends = ['sarah', 'franck']
 #for name in favorite_languages.keys():
     #print(name.title())
     #if name in friends:
         #print("Hi " + name.title() + 
               #", I see your favorite language is " + 
               #favorite_languages[name].title() + "!")
        

# Looping Through All Values in a Dictionary
#favorite_languages = {
    #'perrin': 'python',
    #'sarah': 'c',
     #'edward': 'ruby',
     #'franck': 'c++',
     #'yves': 'java'
 #}
print("The following languages have been mentioned:")
for language in sorted(favorite_languages.values()):
    print(language.title())

# To see each language in chosen without repetition, we can use "set".
for language in set(favorite_languages.values()):
    print(language.title())
    """When you wrap set() around a list that contains duplicate items,
    Python identifiers the unique items in the list and build a set from those items.
    """
 