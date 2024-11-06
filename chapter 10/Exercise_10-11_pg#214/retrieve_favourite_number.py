import json

file = 'chapter 10/Exercise_10-11_pg#214/favourite_numbers.json'
try:
    with open(file) as secret:
        a=json.load(secret)
        print(f"“I know your favorite number! It's {a}.”")
        
except FileNotFoundError:
    print("First run the store_favourite_number.py file")