# Make an empty list for storing aliens.
aliens = []
new_aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
print(aliens)
print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[:10]:
    print(alien)
    new_aliens.append(alien)
for alien in aliens[10:20]:
    new_alien_1 = {'color': 'yellow', 'points': 10, 'speed': 'mid'}
    alien = new_alien_1
    print(alien)
    new_aliens.append(alien)
for alien in aliens[20:30]:
    new_alien_1 = {'color': 'red', 'points': 15, 'speed': 'fast'}
    alien = new_alien_1
    print(alien)
    new_aliens.append(alien)
print(new_aliens)
print(aliens)