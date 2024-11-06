import json

username = input("Enter your Username: ")
file = 'chapter 10/text_files/username.json'
with open(file,'w') as content:
    json.dump(username,content)
    print("We'll remember you when you come back, " + username.title() + "!")