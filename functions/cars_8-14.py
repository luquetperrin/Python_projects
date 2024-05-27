def make_car(manufacturer, model, **car_info):
    """Create a dictionary storing information about a car.
    
    Args:
        manufacturer(str): The car's manufacturer.
        model(str): the car's model name.
        **car_info(dict): Additional information about the car (optional).
    """
    car = {}
    car['manufacturer'] = manufacturer.title()
    car['model_name'] = model.title()
    car.update(car_info)

    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

"""
The .update() method in Python is used to modify a dictionary by 
adding key-value pairs from another iterable object.

It takes a single argument, which can be a dictionary or any other 
iterable object that can generate key-value pairs.

It iterates through the provided iterable and adds or updates 
key-value pairs in the original dictionary.

If a key already exists in the original dictionary, the value 
associated with that key is replaced with the value from the iterable.

New key-value pairs from the iterable are added to 
the original dictionary if the keys don't exist.


"""

