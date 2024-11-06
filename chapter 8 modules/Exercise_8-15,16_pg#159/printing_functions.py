def table(b,a):
    for i in range(1,int(a)+1):
        print(f"{int(b)} x {i} = {int(b)*i}")
        

def sum_of_first_n_natural_numbers(a):
    if a==1:
        return 1
    if a==0:
        return 0
    
    return a + sum_of_first_n_natural_numbers(a-1)


def sum(a):
    sum=0
    for i in range(a):
        b=float(input(f"Enter number {i+1}:  "))
        sum=sum+b
    return sum

def Product(a):
    Product=1
    for i in range(a):
        b=float(input(f"Enter number {i+1}:  "))
        Product=Product*b
    return Product

def difference():
    a=float(input("Enter the first number: "))
    b=float(input("Enter the first number: "))
    return (a-b)

def division():
    a=float(input("Enter the first number: "))
    b=float(input("Enter the first number: "))
    if b==0:
        print("infinity(A number cannot be divided by zero)\n")
    else:
        return a/b
    
def average(a):
    average=0
    for i in range(a):
        b=float(input(f"Enter number {i+1}:  "))
        average= average+b
    return (average)/a


def maximum(a):
    max_val = 0
    for i in range(a):
        a=int(input(f"Enter number {i+1}: \n"))
        if a>max_val:
            max_val=a
    return max_val

def minimum(a):
    min_val = 9999999999999999999999999999999999999999999999999
    for i in range(a):
        a=int(input(f"Enter number {i+1} \n"))
        if a<min_val:
            min_val=a
    return min_val


    
def printing_list(list):
    for i,a in enumerate(list,start = 1):
        if i == 1:
            print(f"{i}st element of list is {a}.")
        elif i == 2:
            print(f"{i}nd element of list is {a}.")
        elif i == 3:
            print(f"{i}rd element of list is {a}.")
        else:
            print(f"{i}th element of list is {a}.")


    
    