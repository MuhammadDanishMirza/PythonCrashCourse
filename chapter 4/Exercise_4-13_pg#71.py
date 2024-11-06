foods = ["pizza","burger","biryani","bar-b-q","fries","roll","shawarma"]
print('This restraunt offers the following foods')
for food in foods:
    print(food.title())
print("\n")  
#foods[0]="Icecreame" this line throws an error because tuple cannot update valu
foods = ["pizza","burger","biryani","gol-gapa","fries","roll","gulab-jaman"]
print('Menue of the restraunt "Sip and bite"')
for food in foods:
    print(food.title())