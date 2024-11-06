

fluffy = {
    "kind":"cat",
    "owner's name":"alice"
}

buddy = {
    "kind":"dog",
    "owner's name":"bob"
}

nibbles = {
    "kind":"rabbit",
    "owner's name":"charlie"
}

spike = {
    "kind":"hamster",
    "owner's name":"david"
}

pets = [fluffy,buddy,nibbles,spike]

for pet in pets:
        print("Information about the pet is:")
        print("Kind of pet is " + pet['kind'].title())
        print("Owner of the pet is " + pet["owner's name"].title())
        print("\n")




    



