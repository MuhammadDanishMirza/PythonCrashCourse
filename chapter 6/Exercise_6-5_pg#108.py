river_countries = {
    "nile":"egypt",
    "Amazon ":"Brazil",
    "Yangtz":"China",
    
}
print("\n")   

for river,country in river_countries.items():
    print("The "+river+" runs through "+country+ ".")

print("\n")   

for river in river_countries:
    print(river.title())
    
print("\n")

for country in river_countries.values():
    print(country.title())