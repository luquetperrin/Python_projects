def get_formatted_namme(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    
    return full_name.title()

engineer = get_formatted_namme('perrin', 'letembet')
print(engineer)

engineer = get_formatted_namme('perrin', 'letembet', 'luquet')
print(engineer)
