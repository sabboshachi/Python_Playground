avaiable_toppings = ["mushroom", "green peppers", "cheese", "chicken", "olives", "chilli"]
requested_toppings = ["mushroom", "mutton", "cheese"]

for requested_topping in requested_toppings:
    if requested_topping in avaiable_toppings:
        print("Adding " + requested_topping.title() + ".")
    else:
        print("Sorry! We are out of  " + requested_topping.title() + "." )

print("\nFinishing making Pizza!")

