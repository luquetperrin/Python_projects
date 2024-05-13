rivers = {
    'nile': 'egypt',
    'yangtse': 'chine',
    'amazone': 'brazil',
    'mississipi-missouri': 'united states',
    'congo': 'congo'
}
for river, country in rivers.items():
    print("The " + river.title() + 
          " runs through " + country.title() + ".")
    
print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())