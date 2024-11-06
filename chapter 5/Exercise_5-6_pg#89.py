age = 14


if age<2:
    print("You are a baby")

elif age==2 or age<4:
    print("You are a toddler")
     
elif age==4 or age<13:
    print("You are a kid")
     
elif age==13 or age<20:
    print("You are a teenager")
     
elif age==20 or age<65:
    print("You are an adult")
    
else:
    print("You are an elder")

# same

# Set a value for the variable age
age = 14


# Determine the person's stage of life
if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
