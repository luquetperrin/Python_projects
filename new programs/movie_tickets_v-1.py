"""1. Conditional Test in while Statement:"""

while True:
    # Get user's age with error handling
    while True:
        prompt = input("\nEnter your age (or 'q' to exit): ")
        if prompt.lower() == 'q':
            break

        try:
            age = int(prompt)
            if age < 0:
                print("Please enter a valid age (non-negative number).")
                continue
        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.")
            continue
        
        # If a valid age is provided, break out of the inner loop
        break
        
    # Check if user wants to quit (conditional test in while)   
    if prompt.lower() == 'q':
        break

    if age < 3:
        price = 0
    elif age <= 12:
        price = 10
    else:
        price = 15

    # Pront ticket price
    if age < 3:
        print("You are too young to buy a ticket")
    else:
        print(f"Your ticket price is ${price}.")