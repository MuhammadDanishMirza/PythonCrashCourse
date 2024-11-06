def count_words(file_path):
    try:
        with open(file_path,encoding='utf-8') as file_obj:    # default encoding is 'cp1252'
            contents = file_obj.read()
    
    except FileNotFoundError:
        print(f"The file named {file_path} does not exist")
    
    except UnicodeDecodeError:
        pass
    
    else:
        words = contents.lower().count("is")
        print("'IS' occur " + str(words) + " times in the file named " + file_path +".")
        
        
count_words("chapter 10/text_files/book.txt")


