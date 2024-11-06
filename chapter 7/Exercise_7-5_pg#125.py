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
            

        
    
    
