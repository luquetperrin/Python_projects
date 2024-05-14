prompt = "\nPlease enter (a) topping(s) you would like to add to your pizza."
prompt += "\nEnter 'quit' when you are finished. "

toppings = []
while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break

    toppings.append(topping)        
    print(f"You'll add {topping.title()} to your pizza.")
if toppings:
    print("\nYou have added:")
    for topping in toppings:
        print(f"\t{topping.title()}")
else:
    print("\nYou did not add any toppings.")



