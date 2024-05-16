"""using a while loop with lists and dictionaries"""

"""
A for loop is effective for looping through a list, but you shouldn’t modify
a list inside a for loop because Python will have trouble keeping track of the
items in the list. To modify a list as you work through it, use a while loop.
Using while loops with lists and dictionaries allows you to collect, store, and
organize lots of input to examine and report on later.
"""

"""Moving Items from One List to Another"""

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verifiy each user until are no more unconfirmed users.
# Move each verified user into the list of confirmed users.

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())