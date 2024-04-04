height = float(input("Enter your height: \n"))
if (height < 2.00):
    print("You can ride!")
    age = int(input("what is your age?\n"))
    if (age < 12):
        print("Pay 1500 CFFA")
    elif (age <= 18):
        print("Pay 2500 FCFA")
    else:
        print("Pay 500 FCFA")
else:
    print("You can't ride")
print("Bye!")