people = {
    
"person 1" : {
    "first_name" : "mujtaba",
    "last_name"  : "rasheed",
    "age"        : "18"     ,
    "city"       : "karachi",
    
    },

"person 2" : {
    "first_name" : "danish",
    "last_name"  : "mirza",
    "age"        : "20"     ,
    "city"       : "karachi",
    
    },

"person 3" : {
    "first_name" : "kamran",
    "last_name"  : "mirza",
    "age"        : "30"     ,
    "city"       : "karachi",
    
    }

      }


for keys,values in people.items():
    print("\n")
    print( keys )
    print("     Full Name: " + values['first_name'].title()+" "+values['last_name'].title())
    print("     Age: "+values['age'].title())
    print("     City: "+ values['city'].title() )
     

