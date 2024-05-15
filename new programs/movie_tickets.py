while True:
  prompt = input("Enter your age (or 'q' to exit from the program): ")
  if prompt.lower() == 'q':
    break

  try:
    age = int(prompt)
    if age < 0:
      print("Please enter a valid age (non-negative number).")
      continue
  except ValueError:
    print("Invalid input. Please enter a valid age (or 'q' when you are finished).")
    continue

  # Calculate and print ticket price based on valid age (properly indented)
  if age < 3:
    price = 0
  elif age <= 12:
    price = 10
  else:
    price = 15

  if age < 3:
    print("You are too young to need a ticket.")
  else:
    print(f"Your ticket price is ${price}.")






    