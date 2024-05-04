"""Functions"""


# Definition:
# A function is a reusable block of code that performs a specific task.
# It can take inputs(arguments), process them, and optionally return
# an output(return value).


# How to use a function:
def function_name(arguments):
    # Code to be executed
    return # output (optional)


# Call the function
# We call a function by typing is name (here, it's function_name), then pass arguments if it was specify.
function_name
# Example 1:
def greet_function(name):
    """Prints a greeting message."""
    print(f"Hello, {name}!")

greet_function("Perrin")

"""Functions with arguments"""

# Example 2:
def greet(name):
    print(f"Hello {name:s}\n")
    print("Are you from ALX?\n")

greet("Perrin")

# Example 3:
def add(a, b):
    c = a + b
    print(f"Sum is {c:d}\n")

add(5, 7)


# Functions Not Using return
# Functions can still be useful even without an explicit return statement.
# They might modify variables outside the function or produce side effects (like printing output)
# Example:
def calculate_area(length, width):
    """Calculates and prints the area of a rectangle."""
    area = length * width
    print(f"The area of the rectangle is {area}.")

calculate_area(5, 3) # Output: The area of the rectangle is 15.

"""Types of Arguments"""
# There are basically four types of arguments in Python:
# Positional Arguments
# Defaut Arguments
# Keyword Arguments (Named Arguments)
# Arbitrary Arguments (Arbitrary positional arguments and  
# Arbitrary keyword arguments)

# 1. Positional Arguments
# These are arguments passed to a function in the order 
# they are defined in the function's parameter list.
# The function expects a specific number of arguments in a specific order.

def greet1(name, age):
    print(f"Hello, {name:s}! You are {age:d} years old.\n")

greet1("Perrin", 29)

# 2. Keyword Arguments(Named Arguments):
# You can pass arguments by name when calling a function,
# regardless of the order they appear in the parameter list.
# This improves readability, especially when functions have many parameters.

def greet2(name, age):
    print(f"Hello, {name}! You are {age} years old.\n")

greet2(age = 22, name = "Reine")

# 3. Default Arguments:
# You can assign default values to parameters in the function definition.
# If no argument is provided during the function call, the default value is used.

def greet3(name = "World", age = None):
    print(f"Hello, {name}! You are {'unknown' if age is None else age} years old\n")

greet3()
greet3("Franck", 24)

# 4. Arbitrary Arguments:
# 4.1. Arbitrary positional arguments (*args):
# Capture a variable number of positional arguments as a tuple within the function.
# Use *args in the parameter list.

def calculate_average(*numbers):
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
    average = sum_numbers / len(numbers)
    print(f"The average of numbers provided is {average: .2f}\n")

calculate_average(10, 25, 16, 19, 30, 76)

def multiply(*numbs):
    mul = 1
    for numb in numbs:
        mul *= numb
    print(f"The multiplication of the given numbers is {mul:d}\n")

multiply(2, 3, -6, 8)
multiply(2,5,8,9,6,0)

# 4.2. Arbitrary keyword arguments(**kwargs):
# Capture a varaible number of keyword arguments as a disctionary
# within the function.
# Use **kwargs in the parameter list.

def info_person(**data):
    for key, value in data.items():
        print(key, value)
    #print(f"Hello, {data['name']}! You are {data['age']} years old and you work as a(an) {data['position']}")
info_person(name = "Perrin", age = 29, position = "Engineer")
print("\n")
info_person(name = "Reine", age = 22, position = "Technician")

