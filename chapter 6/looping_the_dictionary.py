user_0 = {
 'username': 'efermi',
 'first': 'enrico',
 'last': 'fermi',
 }

for k,v in user_0.items():
    print("key: " + k)
    print("value: " + v)
    print("\n")



favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

for name, language in favorite_languages.items():  #NAME IS KEYS   LANGUAGE IS VALUES
    
    print(name.title() + "'s favorite language is " + language.title() + ".")

    

