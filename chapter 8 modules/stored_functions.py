def make_pizza(size, *toppings): 

    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:") 
    for topping in toppings: 
        print("- " + topping) 
        
        
def describe_pet(animal_type, pet_name):
    
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
    
def sum(num1,num2):
    return print(f'The sum of {num1} and {num2} is {num1+num2}.')


