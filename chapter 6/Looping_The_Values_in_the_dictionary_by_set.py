favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("The following languages have been mentioned:")

for language in set(favorite_languages.values()):    # store the values in the form of the set
    print(language.title())
    
a = set(favorite_languages.values()) 
print(type(a))
print(a)