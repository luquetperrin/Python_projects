pets = []

# First pet
pet_1 = {
    'name': 'garfield',
    'kind': 'cat',
    'owner': 'john'
}
pets.append(pet_1)
# Second pet
pet_2 = {
    'name': 'fido',
    'kind': 'dog',
    'owner': 'jane'
}
pets.append(pet_2)
# Third pet
pet_3 = {
    'name': 'polly',
    'kind': 'parrot',
    'owner': 'alice'
}
pets.append(pet_3)

for pet in pets:
    print("\nPet:")
    print(f"Name: {pet['name'].title()}")
    print(f"Kind: {pet['kind'].title()}")
    print(f"Owner: {pet['owner'].title()}")

