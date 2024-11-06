import json



file = 'chapter 10/Exercise_10-11_pg#214/favourite_numbers.json'

try:
    number = int(input("Enter your favourite number: "))
    with open(file,'w') as secret:
        json.dump(number,secret)
        
except ValueError:
    print("Please enter only integer number")
    

    