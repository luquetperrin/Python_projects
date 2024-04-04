# Love Calculator program in Python

# Take input from the user
name1 = input("Enter your name: \n")
name2 = input("Enter your partner's name: \n")

# Combine both names into a single string and convert it to lowercase
combine_name = (name1 + name2).lower()

# Count the occurrences of each letter in the combined name
t = combine_name.count('t')
r = combine_name.count('r')
u = combine_name.count('u')
e = combine_name.count('e')
true = t + r + u + e

l = combine_name.count('l')
o = combine_name.count('o')
v = combine_name.count('v')
e = combine_name.count('e')
love = l + o + v + e

# Calculate the love score by concatenating the counts and converting it to an integer
love_score = int(str(true) + str(love))

# Output the result based on the love score
if (love_score < 10 or love_score > 90):
    print(f"Your love score is {love_score} and You're like fireworks together.")
elif (40 <= love_score <= 50):
    print(f"Your score is {love_score} and you are alright together.")
else:
    print(f"Your love score is {love_score}.")





