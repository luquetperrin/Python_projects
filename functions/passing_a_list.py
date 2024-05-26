def greet_users(names):
    """Print a simple greting to each user in the list."""

    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['perrin', 'reine', 'gloire', 'franck', 'leo']
greet_users(usernames)