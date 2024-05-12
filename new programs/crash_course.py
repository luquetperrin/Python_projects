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
print("The alien_2 is " + alien_2['color'] + ".")
alien_2['color'] = 'red'
#print("The alien_2 is now " + alien_2['color'] + ".")

# Let's track the position of an alien that can move at different speeds.
alien_3 = {'color': 'black', 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_3['x_position']))

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
