# List of sandwich orders to be processed
sandwich_orders = ['Pastrami', 'Grilled Cheese', 'BLT', 'Pastrami', 'Tuna', 'Club', 'Pork Chop Bun', 'Pastrami', 'Leberkase', 'Chimichurri']

print("\nWe are out of pastrami\n")
# List to store completed sandwiches
finished_sandwiches = []

# Loop through sandwich orders until the list is empty
while sandwich_orders:
    if 'Pastrami' in sandwich_orders:
        sandwich_orders.remove("Pastrami")
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich")

    # Add the completed sandwich to the finished sandwiches list
    finished_sandwiches.append(current_order)

# Print finished sandwiches
print("\n--- Finished sandwiches ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
