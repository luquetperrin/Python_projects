"""
List Sorter: 
Write a function that takes a list of numbers 
sorts them in ascending or descending order 
(based on an argument).
"""

def sort_numbers(numbers, ascending=True):
    """
    Sorts a list of numbers in ascending or descending order.

    Args:
        numbers (list of int/float): The list of numbers to sort.
        ascending (bool, optional): If True, sort in ascending order; if False, sort in descending order. Defaults to True.

    Returns:
        list of int/float: The sorted list of numbers.
    """
    # Sort the numbers based on the ascending parameter
    sorted_numbers = sorted(numbers, reverse=not ascending)
    return sorted_numbers

# Test the function
numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
print("Original list:", numbers)
print("Sorted list in ascending order:", sort_numbers(numbers))
print("Sorted list in descending order:", sort_numbers(numbers, ascending=False))