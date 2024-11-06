favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
print("\n")
list = favorite_languages.keys()
sorted_list = sorted(list)

for lists in sorted_list:
    print(lists.title())
    
print("\n")  
# or
for names in sorted(favorite_languages.keys()):
    print(names.title())
    
print("\n")  
