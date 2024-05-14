def get_favorite_places():
  """
  Prompts users for their names and favorite places, stores them in a dictionary,
  and returns the dictionary.
  """
  favorite_places = {}
  while True:
    name = input("Enter a name (or 'q' to quit): ")
    if name.lower() == 'q':
      break
    places = []
    while True:
      place = input("Enter one of " + name + "'s favorite places (or 'n' to finish): ")
      if place.lower() == 'n':
        break
      places.append(place)
    favorite_places[name] = places
  return favorite_places

# Get favorite places from users (optional)
# favorite_places = get_favorite_places()

# Pre-defined favorite places (replace with the above function call to get user input)
favorite_places = {
    'Eric': ['Mount Fuji', 'The Great Barrier Reef'],
    'Erin': ['Paris', 'The Grand Canyon'],
    'David': ['Yosemite National Park']
}

# Print each person's name and favorite places
for name, places in favorite_places.items():
  print(name.title() + "'s favorite places are:")
  for place in places:
    print("\t", place)
