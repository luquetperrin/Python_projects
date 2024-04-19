"""
Write a program to find a 
maximum number from a list of 
numbers without using the max function
"""

# Prompt the user to enter a list of numbers separated by spaces
numbers = input("Enter a list of numbers separated by a space:\n")

# Split the input string into a list of strings (one for each number)
numbers_list = numbers.split()
print(numbers_list)

# Count the number of elements in the list
count = 0
for i in numbers_list:
    count += 1
print(count)

# Convert each string in the list to an integer
for i in range(count):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)

# Initialize the maximum number to the first element in the list
max_number = numbers_list[0]

# Iterate through the list and compare each number with the current maximum
for number in numbers_list:
    if (number > max_number):
        max_number = number

# Print the maximum number in two different formats
print(f"The maximum number is {max_number:d}")
print("The maximum number is", max_number)
