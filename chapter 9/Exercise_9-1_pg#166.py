class Restraunt:
    def __init__(self,restraunt_name,cuisine_type):
        
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to the Restraunt {self.restraunt_name}.")
        print(f"There is a {self.cuisine_type} cuisine in this restraunt.")
        
    def open_restaurant(self):
        print("Restraunt is open") 
        
restraunt = Restraunt("Pizza Hut","chinese")

print(f"Name is {restraunt.restraunt_name}")
print(f"Cuisine type is {restraunt.cuisine_type}")

restraunt.describe_restaurant()
restraunt.open_restaurant()
        