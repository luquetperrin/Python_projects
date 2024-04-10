"""
Write a Python program to create a tuple of your favorite fruits 
and print each fruit in the tuple.
"""

# Create a tuple of favorite fruits
favorite_fruits = ('strawberry', 'orange', 'apple', 'banana', 'mango')

# Print each fruit in the tuple
for fruit in favorite_fruits:
    print(fruit)
print("\n")

# Sort the favorite fruits in alphabetical order
sorted_fruits = sorted(favorite_fruits)
for fruit1 in sorted_fruits:
    print(fruit1)
print("\n")

# Sort the favorite fruits in reverse alphabetical order
reverse_sorted_fruits = sorted(favorite_fruits, reverse=True)
for fruit2 in reverse_sorted_fruits:
    print(fruit2)