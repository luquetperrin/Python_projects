# Loop continues indefinitely until user exits
while True:

  # Get user's age with error handling
  prompt = input("\nPlease enter your age: ")
  try:
    age = int(prompt)  
    if age < 0:  
      print("Enter a valid age (non-negative).")
      continue  
  except ValueError:  
    print("Invalid input. Please enter a number.")
    continue 

  # Determine ticket price based on age
  if age < 3:
    price = 0
  elif age <= 12:
    price = 10
  else:
    price = 15

  # Print ticket information based on age
  if age < 3:
    print("You are too young to buy a ticket.")
  else:
    print(f"Your ticket price is ${price}.")

  # Check for 'q' to exit (break statement)
  choice = input("Enter 'q' to exit or anything else to continue: ")
  if choice.lower() == 'q':
    break  
