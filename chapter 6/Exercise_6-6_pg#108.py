favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }

lst = ["jen","mujtaba","danish","phil"]

for lsst in lst:
    if lsst in favorite_languages.keys():
        print("Thanking for responding "+ lsst.title()) 
    else:
        print(lsst.title() + " is invited to take the poll" )   
    
    
    
    
