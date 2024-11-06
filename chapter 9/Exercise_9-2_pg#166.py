class Restraunt:
    def __init__(self,restraunt_name,cuisine_type):
        
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to the Restraunt {self.restraunt_name.title()}.")
        print(f"There is a {self.cuisine_type.title()} cuisine in this restraunt.")
        
    def open_restaurant(self):
        print("Restraunt is open") 
        
restraunt_1 = Restraunt("pizza Hut"," japanese")
restraunt_2 = Restraunt("china town","chinese")
restraunt_3 = Restraunt("california","pakistani")

restraunt_1.describe_restaurant()
restraunt_2.describe_restaurant()
restraunt_3.describe_restaurant()
