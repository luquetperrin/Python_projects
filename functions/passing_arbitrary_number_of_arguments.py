def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'extra cheese', 'green peppers')

"""
The asterisk in the parameter name *toppings tells 
Python to make an empty tuple called toppings and pack 
whatever values it receives into this tuple
"""