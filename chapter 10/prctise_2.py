from random import randint

class die:
    def __init__(self,sides=6):
        self.sides = sides
        
    def roll_die(self):
        return randint(0,self.sides)

dice = die(9)
result_list = []
for i in range(1000000):
    result_list.append(str(dice.roll_die()))
    
result_string = ''.join(result_list)
print(result_string)