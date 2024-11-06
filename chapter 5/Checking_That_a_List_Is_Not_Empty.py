requested_toppings = []

if requested_toppings: # this checks whether list is empty or not (in this case false)

    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we are out of green peppers right now.")
        else:
            print("Adding " + requested_topping + ".")
            
else:
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")