responses = []

while True:
    
    response = input(" If you could visit one place in the world, where would you go?  ")
    
    responses.append(response)
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat.lower() == 'no':
        break
    
print("\n--- Poll Results ---")
for i,response in enumerate(responses,start=1):
    if i==1:
        print(f"{i}st. Person likes to visit {response}")
    elif i==2:
        print(f"{i}nd. Person likes to visit {response}")
    elif i==3:
        print(f"{i}rd. Person likes to visit {response}")
    else:
        print(f"{i}th. Person likes to visit {response}")
    
    