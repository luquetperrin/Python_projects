while True:
    age = int(input("Enter your age (or 'quit' when you are finished): "))
    if age == 'quit':
        break

    if age < 0:
        print("Please enter a valid age (non-negative number).")
        continue
    