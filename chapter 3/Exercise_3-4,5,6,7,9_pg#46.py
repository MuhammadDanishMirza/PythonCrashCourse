guests = ["danish","mujtaba","kamran"]
invitation_1 = guests[0].title()+ ", You are invited to dinnner. Please join us!"
invitation_2 = guests[1].title()+ ", You are invited to dinnner. Please join us!"
invitation_3 = guests[2].title()+ ", You are invited to dinnner. Please join us!\n"
print(invitation_1)
print(invitation_2)
print(invitation_3)

print("Unfortunately "+guests[0].title()+" can't make it to dinner\n")
guests[0]= "Aslam"
invitation_4 = guests[0].title()+ ", You are invited to dinnner. Please join us!"
invitation_5 = guests[1].title()+ ", You are invited to dinnner. Please join us!"
invitation_6 = guests[2].title()+ ", You are invited to dinnner. Please join us!\n"
print(invitation_4)
print(invitation_5)
print(invitation_6)

print("Congratulations! We have found a bigger dinner table, so the space of three more guests is available")
guests.insert(0,"orhan")
guests.insert(2,"osman")
guests.append("muhammad")
print("Total guests are " + str(len(guests)))
invitation_7 = guests[0].title()+ ", You are invited to dinnner. Please join us!"
invitation_8 = guests[1].title()+ ", You are invited to dinnner. Please join us!"
invitation_9 = guests[2].title()+ ", You are invited to dinnner. Please join us!"
invitation_10 = guests[3].title()+ ", You are invited to dinnner. Please join us!"
invitation_11 = guests[4].title()+ ", You are invited to dinnner. Please join us!"
invitation_12 = guests[5].title()+ ", You are invited to dinnner. Please join us!\n"
print(invitation_7)
print(invitation_8)
print(invitation_9)
print(invitation_10)
print(invitation_11)
print(invitation_12)

print("Sorry for inconvinience! We can invite only two people for dinner because new dinner table won't arrive in time for the dinner.")
a=guests.pop(0)
print("Sorry, We can't invite you " +a.title()+" to the dinner because new dinner table won't arrive in time for the dinner")
b=guests.pop(1)
print("Sorry, We can't invite you " +b.title()+" to the dinner because new dinner table won't arrive in time for the dinner")
c=guests.pop(0)
print("Sorry, We can't invite you " +c.title()+" to the dinner because new dinner table won't arrive in time for the dinner")
d=guests.pop(2)
print("Sorry, We can't invite you " +d.title()+" to the dinner because new dinner table won't arrive in time for the dinner\n")

invitation_13 = guests[0].title()+ ", You are invited to dinnner. Please join us!"
invitation_14 = guests[1].title()+ ", You are invited to dinnner. Please join us!\n"
print(invitation_13)
print(invitation_14)

del guests[0]
del guests[0]
print("Number of guests",len(guests))
print(guests)








