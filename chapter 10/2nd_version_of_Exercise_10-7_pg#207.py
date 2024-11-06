print("Provide Two numbers and I will add them for you")
print("Enter 'exit' anywhere to quit the program")
while True: 
    
    try:
        a= input("Enter number 1: ")
        if a.lower() == "exit":
            print("Exiting from the program....")
            break
        
        b= input("Enter number 2: ")
        if b.lower() == "exit":
            print("Exiting from the program....")
            break
        
        print(f'Sum of {a} and {b} is {float(a)+float(b)}')
    
    except ValueError:
        print("Addition can only be done on numbers.")
        print("Please enter number not text")
    