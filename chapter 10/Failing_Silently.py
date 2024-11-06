def count_words(file_path):
    try:
        with open(file_path,encoding='utf-8') as file_obj:    # default encoding is 'cp1252'
            contents = file_obj.read()
    except FileNotFoundError:
        pass
    except UnicodeDecodeError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print("The file has about " + str(num_words) + " words.")
        
        
count_words("chapter 10/text_files/book.txt")

lists = ["chapter 10/text_files/book.txt","chapter 10/text_files/book1.txt","chapter 10/text_files/file_1.txt","chapter 10/text_files/list_of_reasons.txt","chapter 10/text_files/learning_python.txt","main_file.txt"]

for list in lists:
    count_words(list)