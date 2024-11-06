from module_1 import User


class Privileges:
    def __init__(self,privileges):
        self.privileges = privileges 
        
    def  show_privileges(self):
        print("Here is the list of administrator's set of privilege")
        for privilige in self.privileges:
            print(privilige)
        

class Admin(User):
    def __init__(self, first_name, last_name, username, email, age, location):
        super().__init__(first_name, last_name, username, email, age, location)
        self.privileges =  Privileges(["can add post", "can delete post", "can ban user"])