players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print("Here are the first three players of my team")
for player in players[:3]:
    print(player.title())
print("Here are the last three players of my team")
for player in players[-3:]:
    print(player.title())