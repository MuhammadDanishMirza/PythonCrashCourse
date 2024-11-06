prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""   # defning the variable message for while

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
    
    
    