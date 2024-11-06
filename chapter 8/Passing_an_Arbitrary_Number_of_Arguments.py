def make_pizza(*toopings):  # tooping is a empty tupple int th function parameter
    print(toopings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toopings):  # tooping is a empty tupple int th function parameter
    print("Making the pizza with the following toppings: ")
    for i,tooping in enumerate(toopings,start=1):
        print(f"{i}.{tooping.title()}")  
        
    
make_pizza('mushrooms', 'green peppers', 'extra cheese')

