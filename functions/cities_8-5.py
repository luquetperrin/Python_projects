def describe_city(city, country = 'Congo'):
    """
    Prints a simple sentence about a city and its country

    Arguments:
        city(str): The name of the city.
        country(str): The country where the city is located.
    """
    print(f"{city} is in {country}.")

describe_city('Brazzaville')
describe_city('New Yord', 'USA')
describe_city(city='Paris', country='France')

    