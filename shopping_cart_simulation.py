"""
Simulate a shopping cart using a tuple. 
Add items, iterate through them, 
and check if a specific item exists.
"""

# Initialize an empty shopping cart tuple
shopping_cart = ()

# Function to add items to the shopping cart
def add_to_cart(item):
    global shopping_cart
    shopping_cart += (item,)

# Function to check if an item exists in the shopping cart
def item_exists(item):
    return item in shopping_cart

# Function to iterate through the items in the shopping cart
def display_cart():
    print("Items in the shopping cart:")
    for item in shopping_cart:
        print("-", item)

# Add items to the shopping cart
add_to_cart("Apple")
add_to_cart("Banana")
add_to_cart("Orange")

# Display the items in the shopping cart
display_cart()

# Check if a specific item exists in the shopping cart
item_to_check = "Banana"
if item_exists(item_to_check):
    print(f"{item_to_check} exists in the shopping cart.")
else:
    print(f"{item_to_check} does not exist in the shopping cart.")