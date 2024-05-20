# List of sandwich orders (including Pastrami)
sandwich_orders = ['Pastrami', 'Grilled Cheese', 'BLT', 'Pastrami', 'Tuna', 'Club', 'Pork Chop Bun', 'Pastrami', 'Leberkase', 'Chimichurri']

print("We are out of pastrami")  # Announce shortage

# List to store completed sandwiches
finished_sandwiches = []

# Loop through sandwich orders
while sandwich_orders:
  # Remove pastrami occurrences (if any)
  sandwich_orders.remove('Pastrami')

  # Get the next sandwich order (last item)
  current_order = sandwich_orders.pop()

  # Skip pastrami and inform user (handled by removal)

  # Print a message indicating the sandwich is being made
  print(f"I made your {current_order} sandwich")

  # Add the completed sandwich (except pastrami) to finished list
  finished_sandwiches.append(current_order)

# Print finished sandwiches
print("\n--- Finished sandwiches ---")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
