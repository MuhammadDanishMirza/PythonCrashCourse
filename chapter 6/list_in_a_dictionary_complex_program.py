pizza = {
    "crust":"soft",
    "toppings":["cheese","peproni","olives"]
    
}
print("You ordered a "+ pizza["crust"]+ " crust pizza with the following toppings" )
for topping in pizza["toppings"]:
    print(topping)
    
print("\n")
    
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
 }

for names,favorite_language in favorite_languages.items():
    if len(favorite_language)>1:
        print("\n"+names.title()+"'s favourite languages are:")
        for favorite_languages in favorite_language:
            print(favorite_languages.title())
    else:
        print("\n"+names.title()+"'s favourite language is " +  favorite_language[0])