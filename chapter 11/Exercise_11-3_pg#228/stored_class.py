class Employee:
    def __init__(self,first_name,last_name,annualsalary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annualsalary = annualsalary
        
    def give_raise(self, raisesalary = 5000):
        self.annualsalary = self.annualsalary + raisesalary
        return self.annualsalary
        