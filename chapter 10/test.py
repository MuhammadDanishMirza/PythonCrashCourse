file = "table.txt"
with open(file,"a")as table:
    try:
        number = int(input("Enter the number You want to print the table of: "))
        a = int(input("Now Enter the number till the table you want to print: "))
        table.write(f"****** Table of {number} is ******\n")
        for i in range(1,a+1):
            table.write(f"{number} x {i} = {number*i}\n")
        print(f"Table of {number} is saved in the file named {file}")
        
    except ValueError:
        print("Enter integer number only")

