favorite_numbers = {
    "danish"  : [9,65],
    "mujtaba" : [45,12],
    "kamran"  : [23,1],
    "anas"    : [936,452],
    "ammi"    : [987,21]
    
}


for key,value in favorite_numbers.items():
    print("\n")
    print(f"Favourite numbers of {key.title()} are: ")
    for i,value in enumerate(value,start=1):
        print(f"{i}. {value}")