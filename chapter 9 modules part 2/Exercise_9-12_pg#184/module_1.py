class User:
    def __init__(self, first_name, last_name, username, email, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.age = age
        self.location = location
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Name is {self.first_name}.")
        print(f"Last Name is {self.last_name}.")
        print(f"User Name is {self.username}")
        print(f"Email of {self.first_name+self.last_name} is {self.email}.")
        print(f"Age of {self.first_name+self.last_name} is {self.age}.")
        print(f"Location of {self.first_name+self.last_name} is {self.location}.")
        
    def greet_user(self):
        print(f"Assalamualikum {self.first_name+self.last_name}.")
        
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        
    def show_login_attempts(self):
        print(f"Total login attempts the user made is {self.login_attempts}.")