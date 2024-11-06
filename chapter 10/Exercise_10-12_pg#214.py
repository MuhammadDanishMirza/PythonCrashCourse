import json



file = 'favourite_numbers.json'

try:
    with open(file) as secret:
        number = json.load(secret)
        print(f"“I know your favorite number! It's {number}.”")
        
except FileNotFoundError:
    try:
        number = int(input("Enter your favourite number: "))
    except ValueError:
        print("Enter number only")
    else:
        with open(file,'w') as secret:
            json.dump(number,secret)