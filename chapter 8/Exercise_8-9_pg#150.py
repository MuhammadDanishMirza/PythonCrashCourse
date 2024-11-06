def show_magicians(magician_names):
    for i,magician_name in enumerate(magician_names,start=1):
        print(f"{i}.{magician_name.title()}")
        
        
magician_names = ['David Copperfield', 'Doug Henning', 'Lance Burton', 'Ricky Jay']     
show_magicians(magician_names)
  
    