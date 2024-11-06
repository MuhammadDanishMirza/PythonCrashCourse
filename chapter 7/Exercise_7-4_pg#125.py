while True:
    toppings = input("Enter the pizza toppings one by one: ") 
    if toppings.lower() =="quit":
        print("Exiting...... pizza topping selection.")
        break
    else:
        print(f" I am adding {toppings} to your pizza.")
        