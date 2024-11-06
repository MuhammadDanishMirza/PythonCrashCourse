class User:
    def __init__(self, first_name, last_name, username, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location
        
    def describe_user(self):
        print(f"Name is {self.first_name}.")
        print(f"Last Name is {self.last_name}.")
        print(f"User Name is {self.username}")
        print(f"Email of {self.first_name+self.last_name} is {self.email}.")
        print(f"Age of {self.first_name+self.last_name} is {self.age}.")
        print(f"Location of {self.first_name+self.last_name} is {self.location}.")
        
    def greet_user(self):
        print(f"Assalamualikum {self.first_name+self.last_name}.")
        
        
user1 = User("John", "Doe", "johndoe", "john.doe@example.com", 25, "Cityville")
user2 = User("Jane", "Smith", "janesmith", "jane.smith@example.com", 30, "Townsville")
user3 = User("Bob", "Johnson", "bobjohnson", "bob.johnson@example.com", 22, "Villageville")


user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
