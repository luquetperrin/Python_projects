def make_shirt(size, message):
    """
    Summarizes the size of the shirt and the message printed on it

    Args:
        size(string): The size of the shirt.
        message(string): The message to be printed on the shirt.
    """

    print(f"We are making a {size} t-shirt with '{message}' printed on it.")

make_shirt('M', 'I love Python')
make_shirt(size='L', message='I love coding')
