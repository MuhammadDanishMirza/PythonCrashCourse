import json


file = 'chapter 10/text_files/username.json'
with open(file) as content:
    name = json.load(content)
    print("Welcome back, " + name.title() + "!")