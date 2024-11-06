alien = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_alien)
    
    
for aliens in alien[0:5]:
    print(aliens)
    
    
for aliens in alien[0:3]:
    if aliens['color'] == "green":
        aliens['color'] = "yellow"
        aliens['points'] = 10
        aliens['speed'] = "medium"
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
for aliens in alien[0:5]:
    print(aliens)
    
print("......")
    
print(f"The number of aliens is {len(alien)}")