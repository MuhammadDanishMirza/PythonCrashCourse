user_names = []

if user_names:
    for user_name in user_names:
        
        if user_name == "admin":
            print("Hello , "+ user_name +" would you like to see a status report?")
        else:
            print("Hello , "+ user_name +" thank you for logging in again")
else:
    print("We need to find some users!")