# Multiple if statements in Python
height = float(input("Enter your height please: \n"))
bill = 0

if (height <= 2):
    age = int(input("How old are you?\n"))
    if (age < 12):
        bill = 1500
        print(f"You are {height:.2f} taller and {age:d} year(s) old. Your ticket price is {bill} FCFA")
    elif (age <= 18):
        bill = 2500
        print(f"You are {height:.2f} taller and {age:d} year(s) old. The ticket price is {bill} FCFA")
    else:
        bill = 5000
        print(f"You are {height:.2f} taller and {age:d} year(s) old. The ticket price is {bill} FCFA")
    
    want_photo = input("Do you want to take any photo(Y/N)? \n")
    if (want_photo == 'y' or want_photo == 'Y'):
        bill = bill + 1000
    print(f"Your total bill is {bill}.")
else:
    print("You can't ride")
        