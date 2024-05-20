def decribe_pet(pet_name, animal_type='dog'):
    """Display information about pet.
    
    Args:
    animal_type (string): The kind of animal.
    pet_name (string): The name of a pet.
    """

    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

decribe_pet(pet_name='harry')
decribe_pet(pet_name='willie')