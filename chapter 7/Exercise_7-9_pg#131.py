sandwich_orders = ["Classic Ham Delight","Eggstraordinary Delight","Tuna Tango",
                   "Cuban Fusion","Monte Cristo Marvel","Veggie Bliss","Shrimp Symphony",
                   "Bahn Mi Bonanza","Italian Stallion Sub","Pesto Paradise Panini",
                   "Rye Sensation","Caesar Supreme Wrap","Gyro Glory","Bacon Avocado Affair",
                   "Salmon Serenade","Pulled Pork Pleaser","Caprese Celebration",
                   "Falafel Fiesta","Philly Cheesesteak Sensation","Croque Monsieur Magic",
                   'pastrami', 'pastrami', 'pastrami']

finished_sandwiches = []

print(f"\nDeli has run out of {sandwich_orders[21]} sandwitch")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')


while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"I made your {finished_sandwich} sandwitch.")
    finished_sandwiches.append(finished_sandwich)
    
print("\nFollowing sandwitches have been made")
for i,finished_sandwiche in enumerate(finished_sandwiches,start=1):
    print(f"{i}. {finished_sandwiche}")
