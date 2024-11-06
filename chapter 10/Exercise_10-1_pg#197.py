file_path  = 'chapter 10/text_files/learning_python.txt'
# 1st approach
with open(file_path) as text:
    contents = text.read()
    print(contents)


print("\n\n\n")   


# 2nd approach
with open(file_path) as text:
    for line in text:
        print(line.strip())
        

print("\n\n\n")   


# 3rd approach
with open(file_path) as text:
    list = text.readlines()
    
for line in list:
    print(line.strip())
    
