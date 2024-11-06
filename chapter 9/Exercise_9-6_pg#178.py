class Restraunt:
    def __init__(self,restraunt_name,cuisine_type):
        
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Welcome to the Restraunt {self.restraunt_name}.")
        print(f"There is a {self.cuisine_type} cuisine in this restraunt.")
        
    def open_restaurant(self):
        print("Restraunt is open") 
        
    def show_number_seved(self):
        print(f"Total numbers of customer served is {self.number_served}.")
    
    def set_number_served(self,served):   
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You canot decrease the number of the customers.")

    def increment_number_served(self,served):
        if served>=0:
            self.number_served = self.number_served + served
        else:
            print("Enter valid number")


class IceCreamStand(Restraunt):
    def __init__(self,restraunt_name,cuisine_type,flavours):
        super().__init__(restraunt_name,cuisine_type)
        self.flavours = flavours
        
    def display_flavours(self):
        print("We provide follwing flavours of icecream")
        for flavour in self.flavours:
            print(flavour.title())
            
restraunt = IceCreamStand('IceCreamStand',"Icecream",['chocolate','vanila'])
restraunt.describe_restaurant()
restraunt.display_flavours()


    