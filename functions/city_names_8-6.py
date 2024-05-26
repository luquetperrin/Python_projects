def city_country(city_name, country):
    """
    Return a formatted string of a city and its country
    
    Arguments:
        city(str): The name of the city.
        country(str): The name of the country.

    Returns:
        A formated string with the city and the country 
        separated by a comma and a space (str).
    """

    formatted_city_country = city_name + "," + " " + country

    return formatted_city_country.title()

print(city_country("london", "england"))
print(city_country("Santiago", "Chile"))



    


