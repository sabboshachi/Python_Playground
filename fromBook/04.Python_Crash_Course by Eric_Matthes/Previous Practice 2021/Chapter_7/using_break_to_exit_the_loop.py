
text = "\nPlease Enter a City you want to visit: "
text += "Enter 'quit' to end the program"

while True:
    city = input(text)
    if city == quit:
        break
    else:
        print("I'd lovw to go to " + city.title() + " too !")