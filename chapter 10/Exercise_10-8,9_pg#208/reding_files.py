def read_file_contents(*files):
    
    for file in files:
        try:
            with open (file) as file_1:
                content_of_file = file_1.read()
                print(f"Contents of '{file}' file is")
                print(content_of_file)

        except FileNotFoundError:
            print(f"The File named {file} does not Exist")



read_file_contents("chapter 10/Exercise_10-8,9_pg#208/cats.txt","chapter 10/Exercise_10-8,9_pg#208/dogs.txt")

  

    