"""
You are tasked with painting a wall. 
You have to determine the number of cans needed to paint it. 
Each can covers 7 square meters of wall area. 
Write a Python function called calculate_cans_needed that 
takes two parameters: length and width representing 
the dimensions of the wall. 
The function should calculate and 
return the number of cans needed to paint the entire wall.

Additionally, ensure that your function:

Validates that both length and width are positive numbers. 
If either parameter is non-positive, 
the function should return a message indicating that the dimensions are invalid.
Rounds up the number of cans needed to the nearest whole number. 
For example, if the calculated number of cans needed is 2.3, 
the function should return 3.
You can use the following formula to calculate the number of cans needed:
Number of cans needed = (length * width of the wall) / coverage
"""
import math
def calculate_paint_cans(length, width, coverage_per_can):
    """
    Calculates the number of paints cans needed to paint a wall.

    Args:
        length(float): Length of the wall in meters.
        width (float): Width of the wall in meters.
        coverage_per_can (float): Area covered by one can of paint(square meters).

    Retunrs:
        float: The number of paint cans needed (rounded up to the nearest integer).
    """
    # Calculate the total wall area
    wall_erea = length * width

    # Calculate the number of cans needed (considering rounding up)
    number_of_cans = math.ceil(wall_erea/coverage_per_can)

    return  number_of_cans

# Get user input for the wall dimensions and point coverage
length = float(input("Enter the length of the wall (meters): "))
width = float(input("Enter the width of the wall (meters): "))
coverage_per_can = float(input("Enter the area covered by one can of point (square meters): "))

# Calculate the number of paint cans needed
number_of_cans = calculate_paint_cans(length, width, coverage_per_can)

# print the result
print(f"You will need approximately {number_of_cans: .0f} cans of paint to cover the wall.")
