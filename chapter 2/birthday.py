age = 23 
message = "Happy " + age + "rd Birthday!"
'''Above line throws a type error because numbers cannot be con catente with string'''
print(message)


age = 23 
message = "Happy " + str(age) + "rd Birthday!"
print(message)