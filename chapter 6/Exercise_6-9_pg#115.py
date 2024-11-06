favorite_places = {
    "danish":['Beach', 'Mountains'],
    "mujtaba":['City', 'Park', 'Museum'],
    "hamza":['Countryside']
    
 }


for key,values in favorite_places.items():
    print("\n")
    
    if len(values)>1:
        print("Following are the favourite places of "+ key.title() + ":")
        for value in values:
            print(value.title())
    else:
        print("Favourite place of "+ key.title() + " is "+values[0].title() )