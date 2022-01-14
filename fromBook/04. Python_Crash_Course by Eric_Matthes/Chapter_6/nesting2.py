#Making an empty list for storing aliens

aliens = []

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, "speed" : "medium"}
    aliens.append(new_alien)

print(aliens)

for alien in aliens[0:5]:
    #if alien["color"] == "green":
    if alien["speed"] == "medium":
        alien["color"] = "red"
        alien["points"] = 10
        alien["speed"] = "fast"

#Show first 10 aliens

for alien in aliens[0:10]:
    print(alien)
print(".....")
