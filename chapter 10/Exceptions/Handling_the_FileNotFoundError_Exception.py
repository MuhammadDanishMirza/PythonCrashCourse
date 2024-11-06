filename = 'alice.txt'

try:
    with open(filename) as file:
        contents = file.read()

except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)