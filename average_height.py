"""
Program to calculate average height from a list of heights
Don't use in-built functions (sum and len), 
but you must use for loop to take input from the user..
"""

# Prompt the user to enter a list of heights separated by spaces
heights = input("Enter all heights separated by a space: \n")

# Split the input string into a list of strings (one for each height)
height_list = heights.split()

# Count the number of heights entered
count = 0
for _ in height_list:  
    count += 1

print(count)

# Convert each string in the list to a float (assuming heights are numerical)
for i in range(count):
    height_list[i] = float(height_list[i])

# Print the converted list of heights (for debugging purposes)
# print(height_list)

# Calculate the total height
total = 0
for element in height_list:
    total += element

# Calculate the average height
avg = total / count

# Print the average height in a user-friendly format
print("Average height is:", round(avg, 2))  # Round to 2 decimal places


