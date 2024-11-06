file_path = "chapter 10/text_files/visit_list.txt"

with open(file_path,'w') as visit_list:
    
    while True:
        name = input("Please Enter Your Name or Enter 'Quit' to quit the program: ")
        if name.lower()=='quit':
            break
        else:
            print(f"Asalamualikum {name.capitalize()}")
            visit_list.write(f"{name.capitalize()} \n")