def make_shirt(size = 'L', message = 'I love Python'):
    """
    Summarizes the size of the shirt and the message printed on it

    Args:
        size(string): The size of the shirt.
        message(string): The message to be printed on the shirt.
    """

    print(f"We are making a {size} t-shirt with '{message}' printed on it.")

make_shirt()
make_shirt(size='S', message='Coding in Python is funning')
make_shirt(size='M')