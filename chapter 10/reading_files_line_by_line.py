with open('chapter 10/text_files/file.txt') as file_object:
    for line in file_object:
        print(line.rstrip())