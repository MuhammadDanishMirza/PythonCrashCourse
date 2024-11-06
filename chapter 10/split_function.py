file_path = "chapter 10/text_files/book.txt"
try:
    with open(file_path,encoding='utf-8') as book:    # default encoding is 'cp1252'
        contents = book.read()
except FileNotFoundError:
    msg = "Sorry, the file " + file_path + " does not exist."
    print(msg)
except UnicodeDecodeError:
    print("File is not decoding properly")
else:
    words = contents.split()
    num_words = len(words)
    print("The file has about " + str(num_words) + " words.")
        
    