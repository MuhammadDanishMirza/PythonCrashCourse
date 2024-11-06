cities ={
    "Barcelona":{
        
        "country":"spain",
        "population":"1.6 million ",
        "fact":"it is famous for its architectural masterpiece"
        
        },
    
    
    
    "Tokyo":{
        
        "country":"japan",
        "population":"14 million ",
        "fact":"it is the most populous metropolitan area in the world"
        
        },
    
    
    
    "Vancouver":{
        
        "country":"canada",
        "population": 631000,
        "fact":"it is renowned for its stunning natural surroundings"
        
        }
}


for key,value in cities.items():
    print("\n")
    print("Here is the information about the "+key.title()+" city.")
    print(f"\tCountry in which the city is located: {value['country'].title()}")
    print(f"\tPopulation of the city is {value['population']}.")
    print(f"\tThe fact about the city is that {value['fact']}.")
    




