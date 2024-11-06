def city_country(city,country):
    formatted_string = '"'+city.title()+', '+country.title()+'"'
    return formatted_string


print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan"))
print(city_country("paris", "france"))