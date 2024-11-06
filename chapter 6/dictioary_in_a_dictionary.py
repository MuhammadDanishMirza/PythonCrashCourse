users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },

 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 
}

for keys,values in users.items():
    print("\n")
    print("User name: " + keys )
    print("     Full Name: " + values['first'].title()+" "+values['last'].title())
    print("     Location: "+values['location'].title())
    