supplies = ["pens", "pencel", "binders", "notebook"] #calling the list

for item in range(len(supplies)): #working with for loop
    print("Index " + str(item+1) + " in supplies is: " + supplies[item].title() + '.')

