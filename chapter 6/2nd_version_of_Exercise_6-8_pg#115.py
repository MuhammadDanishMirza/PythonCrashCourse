favorite_places = {
    "danish": ['Beach', 'Mountains'],
    "mujtaba": ['City', 'Park', 'Museum'],
    "hamza": ['Countryside']
}

for key, values in favorite_places.items():
    print("\n")
    
    if len(values) > 1:
        print("Following are the favorite places of " + key.title() + ":")
        for i, value in enumerate(values, start=1):
            print(f"{i}. {value.title()}")
    else:
        print(f"Favorite place of {key.title()} is {values[0].title()}")
     