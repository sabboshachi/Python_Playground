requested_toppings = ["mushroom", "green peppers", "cheese", "chicken"]

for topping in requested_toppings:
    if topping != "chicken":
        print("Adding " + topping + "!")
    else:
        print("Sorry chicken is dead!")

print("\nFinished making Pizza!!")

