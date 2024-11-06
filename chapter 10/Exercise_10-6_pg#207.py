print("Provide Two numbers and I will add them for you")
    
try:
    a= float(input("Enter number 1: "))
    b= float(input("Enter number 2: "))
    print(f'Sum of {a} and {b} is {a+b}')
    
except ValueError:
        print("Addition can only be done on numbers.")
        print("Please enter number not text")
    
   
        