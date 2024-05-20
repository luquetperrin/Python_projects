def decribe_pet(animal_type, pet_name):
    """Display information about pet.
    
    Args:
    animal_type (string): The kind of animal.
    pet_name (string): The name of a pet.
    """

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

decribe_pet('hamster', 'harry')
decribe_pet('dog', 'willie')

