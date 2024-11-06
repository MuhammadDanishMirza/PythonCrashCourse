filename = 'chapter 10/text_files/file_1.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
print("\n") 
   
pi_string = ''
for line in lines:
    pi_string = pi_string + line.strip()

print(pi_string[:5] + "...")
print(pi_string)
print(len(pi_string))