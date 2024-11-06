squares = []
for value in range(1,10+1):
    square = value**2
    squares.append(square)
    
print(squares)


# or

squares = []
for value in range(1,10+1):
    squares.append(value**2)
print(squares)

# or
#list comprehension
list=[a**2 for a in range(1,10+1)]
print(list)