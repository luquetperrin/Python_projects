"""Write a script that takes two numbers as arguments and prints their sum, difference, product, and quotient. Use sys.argv to access the numbers."""

import sys

if len(sys.argv) > 2:
    try:
        # Convert arguments to numbers by handling potential erros
        number1 = float(sys.argv[1])
        number2 = float(sys.argv[2])

        # Perform calculations
        sum_numbers = number1 + number2
        difference = number1 - number2
        product = number1 * number2

        # Check for zero denominator before division
        if number2 == 0:
            print("Error: Division by zero is not allowed.")
            quotient = None
        else:
            quotient = number1 / number2

        # Print formated output
        print(f"The sum is: {sum_numbers:.2f}")
        print(f"The difference is: {difference: .2f}")
        print(f"The product is: {product:.2f}")
        if quotient is not None:
            print(f"The quotient is: {quotient:.2f}")

    except ValueError:
        print("Error: please provide valid numbers as arguments.")
else:
    print("Usage: script_name.py number1 number2")

       
