print("Provide Two numbers and I will add them for you")

while True: 
    
    f = input("If you want to perform the addition operation Enter 'Yes' otherwise Enter 'No' ")
    
    if f.lower()=='no':
        print("Exiting from the program.....")
        break
    
    else:
        try:
            a= float(input("Enter number 1: "))
            b= float(input("Enter number 2: "))
            
        
        except ValueError:
            print("Addition can only be done on numbers.")
            print("Please enter number not text")
            
        
        else:
            print(f'Sum of {a} and {b} is {a+b}')