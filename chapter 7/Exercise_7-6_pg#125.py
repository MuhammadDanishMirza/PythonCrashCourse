# 1st version
age = ""            
while age != "exit":

    age = input("Enter your age to print the cost of your cinema ticket\nOr enter exit to exit the program: ")
    if age.lower() == "exit":
        print("Exiting from the program.......")
        break
    
    age = int(age)
            
        
    if age<3:
            print("Your ticket is free")
    elif age==3 or age<=12:
            print("The cost of your ticket is $10")
    else:
            print("The cost of your ticket is $15")
            
            
 # 2nd version          
active = True            
while active:

    age = input("Enter your age to print the cost of your cinema ticket\nOr enter exit to exit the program: ")
    if age.lower() == "exit":
        print("Exiting from the program.......")
        active = False
    
    elif int(age)<3:
        print("Your ticket is free")
        
    elif int(age)==3 or int(age)<=12:
        print("The cost of your ticket is $10")
        
    else:
        print("The cost of your ticket is $15")
            
            
# 3rd version

while True:

    age = input("Enter your age to print the cost of your cinema ticket\nOr enter exit to exit the program: ")
    if age.lower() == "exit":
        print("Exiting from the program.......")
        break
    
    age = int(age)
            
        
    if age<3:
            print("Your ticket is free")
    elif age==3 or age<=12:
            print("The cost of your ticket is $10")
    else:
            print("The cost of your ticket is $15")
            