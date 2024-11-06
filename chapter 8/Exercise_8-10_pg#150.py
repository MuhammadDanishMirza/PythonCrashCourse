def show_magicians(magician_names):
    for i,magician_name in enumerate(magician_names,start=1):
        print(f"{i}.{magician_name.title()}")
        
def make_great(magician_names):
    for i  in range(len(magician_names)):
        magician_names[i]="The great" + magician_names[i]
    
        
        
magician_names = ['David Copperfield', 'Doug Henning', 'Lance Burton', 'Ricky Jay']     
make_great(magician_names)
show_magicians(magician_names)