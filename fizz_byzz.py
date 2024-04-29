"""
FizzByzz Job Interview Question
Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and 
for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

numbers = list(range(1, 101))

for number in numbers:
    if (number % 3 == 0 and number % 5 == 0):
        print("FizzBuzz")
    elif (number % 3 == 0):
        print("Fizz")
    elif (number % 5 == 0):
        print("Buzz")
    else:
        print(number)

# Second method
numbers = list(range(1, 101))

for index, number in enumerate(numbers):
    if number % 3 == 0 and number % 5 == 0:
        numbers[index] = "FizzBuzz"
    elif number % 3 == 0:
        numbers[index] = "Fizz"
    elif number % 5 == 0:
        numbers[index] = "Buzz"

print(numbers)

