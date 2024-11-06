file_path = "chapter 10/text_files/list_of_reasons.txt"

with open(file_path,'w') as file:
    
    file.write("NAME AND THEIR RESONS THAT WHY THEY LIKE PROGRAMMING\n\n")
    print("Enter 'Quit' anywhere to quit the program\n")
    
    while True:
        
        name = input("Please Enter Your Name: ")
        reason = input("Please write the reason that why you like programming: ") 
        file.write(f"{name.title()}: \n\t\t")
        file.write(f"{reason.title()} \n")
        a= input("Do you want to enter more names and reasons Enter 'Yes' or 'No' ")
        if a.lower()=='no':
            break
        