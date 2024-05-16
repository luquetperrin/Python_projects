sandwich_orders = ["Tuna", "Club", "BLT", "Grilled Cheese"]
finished_sandwiches = []

# Loop through sandwich orders
for sandwich in sandwich_orders:
  print(f"I made your {sandwich} sandwich.")
  finished_sandwiches.append(sandwich)  # Move to finished list

# Print finished sandwiches
print("\nFinished Sandwiches:")
for sandwich in finished_sandwiches:
  print(f"- {sandwich}")
