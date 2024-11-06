from random import randint

class die:
    def __init__(self,sides=6):
        self.sides = sides
        
    def roll_die(self):
        return randint(1,self.sides)

dice = die()
sided_die_10 = die(10)
sided_die_20 = die(20)
    
print("Normal die")  
for i in range(10):
    print(f"Rolling the dice : {dice.roll_die()}")
    
print("\n")   
print("10 sided die") 

for i in range(10):
    print(f"Rolling the dice : {sided_die_10.roll_die()}")
    
print("\n") 
print("20 sided die")   

for i in range(10):
    print(f"Rolling the dice : {sided_die_20.roll_die()}")