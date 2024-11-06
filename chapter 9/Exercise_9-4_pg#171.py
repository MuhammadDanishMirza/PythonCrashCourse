class Restraunt:
    def __init__(self,restraunt_name,cuisine_type):
        
        self.restraunt_name = restraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"Welcome to the restaurant {self.restraunt_name}.")
        print(f"There is a {self.cuisine_type} cuisine in this restaurant.")
        
    def open_restaurant(self):
        print("restaurant is open")
        
    def show_number_seved(self):
        print(f"Total numbers of customer served is {self.number_served}.")
    
    def set_number_served(self,served):   
        if served >= self.number_served:
            self.number_served = served
        else:
            print("You cannot decrease the number of the customers.")

    def increment_number_served(self,served):
        if served>=0:
            self.number_served = self.number_served + served
        else:
            print("Enter valid number")


restraunt = Restraunt("Pizza Hut","chinese")

print(f"Name is {restraunt.restraunt_name}")
print(f"Cuisine type is {restraunt.cuisine_type}")

restraunt.describe_restaurant()
restraunt.open_restaurant()

restraunt.show_number_seved()

restraunt.number_served = 10
restraunt.show_number_seved()

restraunt.set_number_served(20)
restraunt.show_number_seved()

restraunt.set_number_served(3)
restraunt.show_number_seved()

restraunt.increment_number_served(10)
restraunt.show_number_seved()

    
    