from collections import OrderedDict

Glossary = OrderedDict()


Glossary["Algorithm" ]  = "An algorithm is a step-by-step set of instructions or a set of rules to follow to complete a task or solve a particular problem. In programming, algorithms are fundamental to designing efficient and effective solutions."
Glossary["Variable"]    = "A variable is a symbolic name or identifier associated with a storage location (memory address) that holds data in a program. Variables can store different types of information and can be manipulated during the program's execution."
Glossary["Function"]    = "A variable is a symbolic name or identifier associated with a storage location (memory address) that holds data in a program. Variables can store different types of information and can be manipulated during the program's execution."
Glossary["Syntax"]      = "Syntax refers to the set of rules that dictate how programs written in a programming language should be structured. It defines the correct combinations of symbols, keywords, and other elements that form valid and executable code."
Glossary["Debugging"]   = "Debugging is the process of identifying and fixing errors, or bugs, in a program. Programmers use debugging techniques and tools to locate and resolve issues in their code, ensuring that the program functions as intended."
Glossary["List"]        = "A list is a built-in data type in Python used to store a collection of items. It is mutable, meaning you can modify its elements by adding, removing, or changing them."
Glossary["Tuple"]       = "Similar to a list, a tuple is another built-in data type for storing ordered collections of items. The key difference is that tuples are immutable, meaning their elements cannot be changed once they are assigned."
Glossary["Dictionary"]  = "A dictionary is a data type that stores key-value pairs. It provides a way to organize and retrieve data using a unique key. Dictionaries are mutable and widely used for tasks involving mapping and associative arrays."
Glossary["Function"]    = "In Python, a function is a block of organized, reusable code that performs a specific task. Functions help in modularizing code, making it more readable and maintainable. They are defined using the def keyword."
Glossary["Module"]      = "A module in Python is a file containing Python definitions and statements. It allows you to organize code logically, and it provides a way to reuse code in different parts of your program or across multiple programs. Modules are imported using the import keyword."


for word , meaning in Glossary.items():
    print("The meaning of the "+ word +" is:\n\t\t\t\t"+ meaning + "\n\n" )