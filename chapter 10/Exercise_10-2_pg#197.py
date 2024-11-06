file_path  = 'chapter 10/text_files/learning_python.txt'


with open(file_path) as text:
    for line in text:
        modified_line = line.replace("Python","C++")
        print(modified_line.strip())