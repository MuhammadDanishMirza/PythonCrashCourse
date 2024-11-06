file_path = "chapter 10/text_files/guest_name.txt"

with open(file_path,'w') as guest_names:
    
    while True:
        a = input("Please Enter Your Name or Enter 'Quit' to quit the program: ")
        if a.lower()=='quit':
            break
        else:
            guest_names.write(f"{a.capitalize()} \n")
    