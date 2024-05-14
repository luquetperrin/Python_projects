while True:
    # Get user's input
    user_input = input("Enter your age (or 'q' to quit): ")

    # Quit if user enters 'q'
    if user_input.lower() == 'q':
        break

    # Convert user input to integer
    try:
        age = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid age (or 'q' to quit).")
        continue

    # Validate age (basic check)
    if age < 0:
        print("Please enter a valid age (non-negative number).")
        continue

    # Determine ticket price based on age
    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    # Print ticket price
    if age < 3:
        print("You are too young to need a ticket.")
    else:
        print(f"Your ticket price is ${price}.")
