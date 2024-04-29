"""
Calculate sum of even numbers from 
1 to 100, including 1 & 100 
"""
# First method
total = 0
for i in range(1,101):
    if (i % 2 == 0):
        total += i
print(f"The sum of numbers is {total:d}")

# Second method
total = 0
for i in range (2, 101, 2):
    total += i
print(f"The sum of numbers is {total:d}")