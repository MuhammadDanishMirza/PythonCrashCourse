age = 17

if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
    
else:
 print("Sorry, you are too young to vote.")
 print("Please register to vote as soon as you turn 18!")
 
print("\n")




list_of_pizza_toppings = ["peproni","cheeese","tikka"]

if "peproni" in list_of_pizza_toppings:
    print("Adding the topping peproni")

if "mushrooms" in list_of_pizza_toppings:
    print("Adding the topping mushroom")

if "cheeese" in list_of_pizza_toppings:
    print("Adding the topping cheeese")
    
print("\nFinish mking pizza")




# this block of if elif statements does not work properly in this case

if "peproni" in list_of_pizza_toppings:
    print("Adding the topping peproni")

elif "mushrooms" in list_of_pizza_toppings:
    print("Adding the topping mushroom")

elif "cheeese" in list_of_pizza_toppings:
    print("Adding the topping cheeese")
    
print("\nFinish mking pizza")


