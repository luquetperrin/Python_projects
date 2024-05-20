# Initialize an empty list to store poll responses
poll_results = []

# Loop to collect responses until user quits
while True:
    place = input("\nIf you could visit one place in the world, where would you go? (or 'q' to quit): ")
    if place == 'q':
        break
    poll_results.append(place)

# Print poll results
print("\nDream Vacation Poll Results:")
if poll_results:
    for place in poll_results:
        print(f"- {place}")
else:
    print("No responses collected.")
