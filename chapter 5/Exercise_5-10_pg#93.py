current_user = ["Danish","kamran","admin","mujtaba","hamza"]
new_users = ["Anas","danish","ahmed","kamran","rasheed"]
for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_user ]:
        print("You will need to enter a new username.")
        
    else:
        print("The username is available")