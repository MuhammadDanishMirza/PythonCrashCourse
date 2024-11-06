my_foods = ['pizza', 'falafel', 'carrot cake']  
friend_foods = my_foods[:]
my_foods.append("bar-b-q")
friend_foods.append("afghani-tikka")

print("My favorite foods are:") 
for food in my_foods:
    print(food.title())
    
print("\n")
print("\nMy friend's favorite foods are:") 
for food in friend_foods:
    print(food.title())
