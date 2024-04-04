# Pizza order program in Python
size = input("What is the size of the pizza you want(S/M/L)? \n")
bill = 0
if (size == 'S' or size == 's'):
    bill += 2500
    print(f"Small pizza size is {bill}.")
elif (size == 'M' or size == 'm'):
    bill += 5000
    print(f"Medium pizza size is {bill}.")
else:
    bill += 7500
    print(f"Large pizza size is {bill}.")

add_pepperoni = input("Do you want pepperoni(Y/N)? \n")
if (add_pepperoni == 'Y' or add_pepperoni == 'y'):
    if (size == 'S' or size == 's'):
        bill += 30
    else:
        bill += 50

extra_cheese = input("Do you want extra cheese(Y/N)? \n")
if (extra_cheese == 'Y' or extra_cheese == 'y'):
    bill += 20

print(f"Your total bill is {bill}.")

