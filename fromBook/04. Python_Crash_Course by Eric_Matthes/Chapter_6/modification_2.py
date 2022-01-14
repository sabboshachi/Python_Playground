alien_0 = {"x_position" : 0 , "y_position" : 25 , "speed" : "fast"}

print("Original x_position : "  + str(alien_0["x_position"]))

#Move the alien to the right

#determine how far to move the alien based on its current position
if alien_0["speed"] == "slow":
    x_inc = 1
elif alien_0["speed"] == "medium":
    x_inc = 2
else:
    #This must be a fast alien
    x_inc = 3

# The new position is the old position plus the incriment
alien_0["x_position"] = alien_0["x_position"] + x_inc

print("New x_position: " + str(alien_0["x_position"]))

