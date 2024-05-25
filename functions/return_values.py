def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

engineer = get_formatted_name('perrin', 'letembet')
print(engineer)

"""
The return statement takes a value from inside a function 
and sends it back to the line that called the function
"""