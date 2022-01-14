#Making an empty list for storing aliens

aliens = []

for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : 5, "speed" : "medium"}
    aliens.append(new_alien)

print(aliens)

#Show the first 5 aliens

for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created

print("The number of aliens : " + str(len(aliens)))

