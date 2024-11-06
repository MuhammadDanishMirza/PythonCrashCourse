favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

friends = ['phil', 'sarah']

for name,languages in favorite_languages.items():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +", I see your favorite language is " + favorite_languages[name].title() + "!")
    else:
        print("I don't see the name in the list")