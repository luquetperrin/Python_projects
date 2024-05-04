total = 0
number =int(input("Enter a number (0 to quit): \n"))
while (number != 0):
    total += number
    number =int(input("Enter a number (0 to quit): \n"))
print(f"The total is {total:d}")