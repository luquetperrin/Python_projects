magicians = ['Perrin', 'Sara', 'Reine', 'Gloire', 'Franck', 'Destre', 'Destin']

def show_magicians(magicians):
    """Print the name of each magician in the list."""
    for magician in magicians:
        print(magician)

def make_great(magicians):
    """Modifies the list of magicians by adding
    'the Great' to each name.

     Returns:
        A new list containing the modified magicians' names
    """
     # Create a new list to store the modified names
    great_magicians = []
    for magician in magicians:
        great_magician = "the Great " + magician
        great_magicians.append(great_magician)
    
    return great_magicians

# Print the original list
print("Original magicians:")
show_magicians(magicians)

# Create a new list with modified names
great_magicians = make_great(magicians[:])

# Print the list of great magicians
print("\nGreat magicians:")
show_magicians(great_magicians)

