pizzas = ["fajita","supreme","tikka","cheese","peproni"]
friends_pizzas = pizzas[:]
pizzas.append("bar-b-q")
friends_pizzas.append("afghani-tikka")
print("My favourite pizzas are:")
for pizza in pizzas:
    print(pizza)
    
print("\n")

print("My friend's favourite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)